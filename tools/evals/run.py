#!/usr/bin/env python3
import argparse
import json
import subprocess
import sys
import tempfile
from pathlib import Path

REPO = Path(__file__).resolve().parents[2]
ROOT = REPO / "plugins" / "rewording"
GUARD = REPO / "plugins" / "rewording-guard"
RW = GUARD / "scripts" / "precheck.py"
CASES = json.loads((Path(__file__).resolve().parent / "cases.json").read_text(encoding="utf-8"))


def request_text(case):
    if "request" in case:
        return case["request"]
    gen = case["request_generate"]
    return gen["unit"] * gen["repeat"] + case.get("request_suffix", "")


def run_offline(case):
    spec = case.get("offline")
    if not spec:
        return []
    proc = subprocess.run(
        [sys.executable, "-I", str(RW), "check"],
        input=request_text(case),
        capture_output=True,
        text=True,
        encoding="utf-8",
    )
    if proc.returncode != 0:
        return ["precheck.py check failed: " + proc.stderr.strip()]
    data = json.loads(proc.stdout)
    problems = []
    if "level" in spec and data["level"] != spec["level"]:
        problems.append("level %s, expected %s" % (data["level"], spec["level"]))
    if "secrets" in spec and bool(data["secret_kinds"]) != spec["secrets"]:
        problems.append("secrets detected=%s, expected %s" % (bool(data["secret_kinds"]), spec["secrets"]))
    for flag in spec.get("flags", []):
        if flag not in data["flags"]:
            problems.append("missing flag " + flag)
    return problems


def run_live(case, model, effort, budget):
    workdir = tempfile.mkdtemp(prefix="rw-live-")
    command = [
        "claude",
        "-p",
        "/rewording:rewording " + request_text(case),
        "--plugin-dir",
        str(ROOT),
        "--plugin-dir",
        str(GUARD),
        "--output-format",
        "stream-json",
        "--verbose",
        "--include-hook-events",
        "--no-session-persistence",
        "--max-budget-usd",
        str(budget),
        "--model",
        model,
        "--effort",
        effort,
        "--permission-mode",
        "dontAsk",
    ]
    proc = subprocess.run(command, cwd=workdir, capture_output=True, text=True, encoding="utf-8", timeout=600)
    tools, hook_decisions, result, cost = [], [], "", None
    for line in proc.stdout.splitlines():
        try:
            event = json.loads(line)
        except ValueError:
            continue
        kind = event.get("type")
        if kind == "assistant":
            for block in event["message"]["content"]:
                if block.get("type") == "tool_use":
                    tools.append(block["name"])
        elif kind == "system" and event.get("subtype") == "hook_response":
            hook_decisions.append(event.get("stdout", ""))
        elif kind == "result":
            result = event.get("result", "") or ""
            cost = event.get("total_cost_usd")
    problems = []
    blocked = any('"decision": "block"' in out for out in hook_decisions)
    if case.get("expect_blocked"):
        if not blocked:
            problems.append("hook did not block")
        if tools:
            problems.append("tools used after a block: %s" % tools)
        return problems, tools, result, cost
    if not hook_decisions:
        problems.append("hook did not run")
    allowed = set(CASES["allowed_tools"])
    for name in tools:
        if name not in allowed:
            problems.append("unexpected tool " + name)
    for name in case.get("must_not_use", []):
        if name in tools:
            problems.append("must not use " + name)
    for marker in case.get("must_contain", []):
        if marker not in result:
            problems.append("output lacks " + marker)
    return problems, tools, result, cost


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--claude-code", action="store_true", help="also run each case live through claude -p")
    parser.add_argument("--only", help="run one case id")
    parser.add_argument("--model", default="claude-sonnet-5-5")
    parser.add_argument("--effort", default="low")
    parser.add_argument("--budget", type=float, default=1.5)
    args = parser.parse_args()
    failed = 0
    for case in CASES["cases"]:
        if args.only and case["id"] != args.only:
            continue
        problems = run_offline(case)
        line = "offline " + ("ok" if not problems else "FAIL " + "; ".join(problems))
        if args.claude_code:
            live, tools, result, cost = run_live(case, args.model, args.effort, args.budget)
            problems += live
            line += " | live " + ("ok" if not live else "FAIL " + "; ".join(live))
            line += " | tools=%s cost=%s" % (sorted(set(tools)), cost)
            out_dir = Path(tempfile.gettempdir())
            (out_dir / ("rw-eval-%s.txt" % case["id"])).write_text(result, encoding="utf-8")
        print("%-16s %s" % (case["id"], line))
        failed += 1 if problems else 0
    return 1 if failed else 0


if __name__ == "__main__":
    sys.exit(main())
