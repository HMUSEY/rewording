#!/usr/bin/env python3
import argparse
import datetime
import json
import re
import sys
from pathlib import Path

MAX_INPUT_CHARS = 400000
HEAVY_TOKENS = 20000
VERY_HEAVY_TOKENS = 50000
HOOK_COMMANDS = ("rewording", "rewording:rewording")
OVERRIDE_PREFIX = "NOSECRET:"

EXIT_OK = 0

_MARKS = re.compile("[ً-ٰٟـ]")
_LETTER_MAP = str.maketrans(
    {"أ": "ا", "إ": "ا", "آ": "ا", "ى": "ي", "ة": "ه"}
)
_ARABIC = re.compile("[؀-ۿݐ-ݿࢠ-ࣿﭐ-﷿ﹰ-﻿]")
_LATIN_LETTER = re.compile("[A-Za-z]")


def normalize(text):
    return _MARKS.sub("", text).translate(_LETTER_MAP).lower()


def _compile(patterns):
    return [re.compile(normalize(p), re.IGNORECASE) for p in patterns]


def _luhn_ok(digits):
    total = 0
    for index, char in enumerate(reversed(digits)):
        value = int(char)
        if index % 2 == 1:
            value *= 2
            if value > 9:
                value -= 9
        total += value
    return total % 10 == 0


def _iban_ok(candidate):
    rearranged = candidate[4:] + candidate[:4]
    number = "".join(str(int(ch, 36)) for ch in rearranged)
    return int(number) % 97 == 1


SECRET_PATTERNS = (
    ("anthropic_key", re.compile(r"sk-ant-[A-Za-z0-9_\-]{20,}")),
    ("openai_key", re.compile(r"\bsk-(?!ant-)(?:proj-)?[A-Za-z0-9_\-]{32,}")),
    ("github_token", re.compile(r"\b(?:gh[pousr]_[A-Za-z0-9]{30,}|github_pat_[A-Za-z0-9_]{20,})")),
    ("aws_key", re.compile(r"\b(?:AKIA|ASIA)[0-9A-Z]{16}\b")),
    ("google_key", re.compile(r"\bAIza[0-9A-Za-z_\-]{35}\b")),
    ("slack_token", re.compile(r"\bxox[abprs]-[A-Za-z0-9\-]{10,}")),
    ("stripe_key", re.compile(r"\b[rs]k_(?:live|test)_[0-9A-Za-z]{16,}")),
    ("private_key", re.compile(r"-----BEGIN (?:[A-Z]+ )?PRIVATE KEY-----")),
    ("jwt", re.compile(r"\beyJ[A-Za-z0-9_\-]{10,}\.eyJ[A-Za-z0-9_\-]{10,}\.[A-Za-z0-9_\-]{10,}")),
    ("bearer_token", re.compile(r"(?i)\bbearer\s+[A-Za-z0-9_\-.=]{24,}")),
    ("url_credentials", re.compile(r"\b[a-z][a-z0-9+.\-]*://[^\s:@/]+:[^\s:@/]{3,}@")),
    (
        "assigned_secret",
        re.compile(
            r"(?i)\b(?:api[_ -]?key|secret|client[_ -]?secret|access[_ -]?token|auth[_ -]?token|token|passwd|password|pwd)\b[\"']?\s*[:=]\s*[\"']?"
            r"(?=[^\s\"']*[A-Za-z])(?=[^\s\"']*\d)[^\s\"']{8,}"
        ),
    ),
    (
        "assigned_secret_ar",
        re.compile("(?:كلم[ةه] المرور|الرمز السري|مفتاح)\\s*(?:هي|هو|:|=)\\s*[A-Za-z0-9_\\-/+=.]{8,}"),
    ),
)
CARD_RE = re.compile(r"(?<![\dA-Za-z])(?:\d[ \-]?){13,19}(?![\dA-Za-z])")
IBAN_RE = re.compile(r"\b[A-Z]{2}\d{2}[A-Z0-9]{11,30}\b")

IRREVERSIBLE_PATTERNS = _compile(
    [
        r"\bdelete\b",
        r"\bdrop\s+(?:table|database|schema)\b",
        r"\btruncate\b",
        r"\brm\s+-rf\b",
        r"force[- ]push",
        r"--force\b",
        r"\breset\s+--hard\b",
        r"\boverwrit(?:e|ing)\b",
        r"\bwipe\b",
        r"\bdeploy(?:ing|ment)?\b",
        r"\bproduction\b",
        r"\bpublish\b",
        r"\bsend\s+(?:an?\s+|the\s+)?(?:email|mail|message|invoice)s?\b",
        r"\bpay(?:ment)?s?\b",
        r"\btransfer\s+(?:money|funds)\b",
        r"\brefund\b",
        r"\bmigrat(?:e|ion)\b",
        "احذف",
        "حذف",
        "امسح",
        "تصفير",
        "انشر",
        "ارسل",
        "ادفع",
        "استرداد",
        "ترحيل",
        "الانتاج",
        "تحويل المال",
        "تحويل مبلغ",
    ]
)
RECENT_PATTERNS = _compile(
    [
        r"\btoday\b",
        r"\btonight\b",
        r"\blatest\b",
        r"\bcurrent(?:ly)?\b",
        r"\bright now\b",
        r"\bthis\s+(?:week|month|year)\b",
        r"\bnews\b",
        r"\bprices?\b",
        r"\bas of\b",
        r"\brecent(?:ly)?\b",
        r"\bnew(?:est)?\s+release\b",
        "اليوم",
        "الان",
        "احدث",
        "حاليا",
        "الاخبار",
        "اسعار",
        "سعر",
        "هذا الاسبوع",
        "هذا الشهر",
        "هذه السنه",
    ]
)
HEAVY_SCOPE_PATTERNS = _compile(
    [
        r"\b(?:whole|entire|full|complete)\s+(?:repo|repository|codebase|project|folder|directory|drive)\b",
        r"\ball\s+(?:the\s+)?(?:files|documents|docs|emails|messages|pdfs|pages)\b",
        r"\bevery\s+file\b",
        "كل الملفات",
        "جميع الملفات",
        "كامل المستودع",
        "كل المستودع",
        "كل المشروع",
        "كامل المشروع",
        "المشروع كامل",
        "كل المستندات",
        "جميع المستندات",
        "كامل الكود",
        "كل الكود",
    ]
)
FILE_REF_RE = re.compile(r"(?<![\w.@])@[A-Za-z0-9_.~/\\\-]*[A-Za-z0-9_/\\]")


def estimate_tokens(text):
    latin = arabic = other = 0
    for char in text:
        if ord(char) < 128:
            latin += 1
        elif _ARABIC.match(char):
            arabic += 1
        else:
            other += 1
    return int(latin / 4 + arabic / 2.5 + other / 2) + (1 if text else 0)


def level_for(tokens):
    if tokens >= VERY_HEAVY_TOKENS:
        return "very_heavy"
    if tokens >= HEAVY_TOKENS:
        return "heavy"
    return "normal"


def language_of(text):
    arabic = len(_ARABIC.findall(text))
    latin = len(_LATIN_LETTER.findall(text))
    total = arabic + latin
    if total == 0:
        return "none"
    ratio = arabic / total
    if ratio >= 0.7:
        return "ar"
    if ratio <= 0.1:
        return "en"
    return "mixed"


def find_secrets(text):
    found = {}

    def add(kind, position):
        line = text.count("\n", 0, position) + 1
        found.setdefault(kind, [])
        if line not in found[kind]:
            found[kind].append(line)

    for kind, pattern in SECRET_PATTERNS:
        for match in pattern.finditer(text):
            add(kind, match.start())
    for match in CARD_RE.finditer(text):
        digits = re.sub(r"\D", "", match.group(0))
        if 13 <= len(digits) <= 19 and _luhn_ok(digits):
            add("card_number", match.start())
    for match in IBAN_RE.finditer(text):
        if _iban_ok(match.group(0)):
            add("iban", match.start())
    return found


def strip_override(text):
    stripped = text.lstrip()
    if stripped.upper().startswith(OVERRIDE_PREFIX):
        return stripped[len(OVERRIDE_PREFIX):].lstrip(), True
    return text, False


def analyze(raw_text):
    text, overridden = strip_override(raw_text)
    normalized = normalize(text)
    flags = []
    year = datetime.date.today().year
    year_pattern = re.compile(r"\b(?:%d|%d)\b" % (year, year + 1))
    if any(p.search(normalized) for p in IRREVERSIBLE_PATTERNS):
        flags.append("irreversible")
    if any(p.search(normalized) for p in RECENT_PATTERNS) or year_pattern.search(text):
        flags.append("recent_info")
    if any(p.search(normalized) for p in HEAVY_SCOPE_PATTERNS):
        flags.append("heavy_scope")
    file_refs = len(FILE_REF_RE.findall(text))
    if file_refs:
        flags.append("file_refs")
    tokens = estimate_tokens(text)
    return {
        "text": text,
        "overridden": overridden,
        "chars": len(text),
        "tokens": tokens,
        "level": level_for(tokens),
        "lang": language_of(text),
        "secrets": {} if overridden else find_secrets(text),
        "flags": flags,
        "file_refs": file_refs,
    }


def precheck_line(result):
    if result["overridden"]:
        secrets = "skipped"
    elif result["secrets"]:
        secrets = ",".join(sorted(result["secrets"]))
    else:
        secrets = "none"
    flags = ",".join(result["flags"]) if result["flags"] else "none"
    return "PRECHECK tokens~%d level=%s lang=%s secrets=%s flags=%s file_refs=%d" % (
        result["tokens"],
        result["level"],
        result["lang"],
        secrets,
        flags,
        result["file_refs"],
    )


def public_view(result):
    return {
        "tokens_estimate": result["tokens"],
        "level": result["level"],
        "lang": result["lang"],
        "chars": result["chars"],
        "secret_kinds": result["secrets"],
        "secret_check_skipped": result["overridden"],
        "flags": result["flags"],
        "file_refs": result["file_refs"],
    }


def secret_report(result):
    parts = []
    for kind in sorted(result["secrets"]):
        lines = ",".join(str(n) for n in result["secrets"][kind][:5])
        parts.append("%s (line %s)" % (kind, lines))
    return "; ".join(parts)


def configure_streams():
    for stream, errors in ((sys.stdin, "replace"), (sys.stdout, "strict"), (sys.stderr, "replace")):
        try:
            stream.reconfigure(encoding="utf-8", errors=errors)
        except (AttributeError, ValueError):
            pass


def read_text(args):
    if getattr(args, "text", None) is not None:
        data = args.text
    elif getattr(args, "file", None):
        path = Path(args.file)
        if not path.is_file():
            fail("file not found: %s" % path.name, 2)
        with open(path, "r", encoding="utf-8", errors="replace") as handle:
            data = handle.read(MAX_INPUT_CHARS + 1)
    else:
        if sys.stdin.isatty():
            fail("no input: pipe the request on stdin, or use --text or --file", 2)
        data = sys.stdin.read(MAX_INPUT_CHARS + 1)
    if len(data) > MAX_INPUT_CHARS:
        fail("input is larger than %d characters" % MAX_INPUT_CHARS, 2)
    if not data.strip():
        fail("empty input", 2)
    return data


def fail(message, code):
    sys.stderr.write("rw: %s\n" % message)
    sys.exit(code)


def cmd_check(args):
    result = analyze(read_text(args))
    if args.line:
        print(precheck_line(result))
    else:
        print(json.dumps(public_view(result), ensure_ascii=False, indent=2))
    return EXIT_OK


def cmd_hook(args):
    raw = sys.stdin.read(MAX_INPUT_CHARS * 2 + 1)
    if len(raw) > MAX_INPUT_CHARS * 2:
        return EXIT_OK
    try:
        payload = json.loads(raw)
    except ValueError:
        return EXIT_OK
    if not isinstance(payload, dict):
        return EXIT_OK
    if str(payload.get("command_name", "")) not in HOOK_COMMANDS:
        return EXIT_OK
    arguments = payload.get("command_args")
    if not isinstance(arguments, str) or not arguments.strip():
        return EXIT_OK
    result = analyze(arguments[:MAX_INPUT_CHARS])
    if result["secrets"]:
        reason = (
            "Rewording stopped before sending: secret-like text found (%s). "
            "Remove it and run /rewording again. If this is a false positive, start the request with %s"
            % (secret_report(result), OVERRIDE_PREFIX)
        )
        output = {"decision": "block", "reason": reason}
    else:
        output = {
            "hookSpecificOutput": {
                "hookEventName": "UserPromptExpansion",
                "additionalContext": precheck_line(result)
                + " (computed by a local script, no model call, no network)",
            }
        }
    sys.stdout.write(json.dumps(output))
    return EXIT_OK


def add_input_options(parser):
    group = parser.add_mutually_exclusive_group()
    group.add_argument("--text", help="request text")
    group.add_argument("--file", help="read the request from a file")


def make_parser():
    parser = argparse.ArgumentParser(prog="precheck.py")
    sub = parser.add_subparsers(dest="command", required=True)

    check = sub.add_parser("check", help="local estimate and flags, no network")
    add_input_options(check)
    check.add_argument("--line", action="store_true", help="print one PRECHECK line")
    check.set_defaults(func=cmd_check)

    hook = sub.add_parser("hook", help="UserPromptExpansion hook entry point")
    hook.set_defaults(func=cmd_hook)
    return parser


def main(argv=None):
    configure_streams()
    args = make_parser().parse_args(argv)
    return args.func(args)


if __name__ == "__main__":
    sys.exit(main())
