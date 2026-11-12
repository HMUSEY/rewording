#!/usr/bin/env python3
import argparse
import hashlib
import json
import re
import sys
import urllib.error
import urllib.parse
import urllib.request
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SOURCES = ROOT / "plugins" / "rewording" / "skills" / "rewording" / "references" / "sources.md"
SNAPSHOT = ROOT / "tools" / "snapshot.json"
ALLOWED_HOSTS = ("platform.claude.com", "code.claude.com", "support.claude.com", "docs.claude.com", "www.anthropic.com", "claude.com")
MAX_BYTES = 3_000_000


class NoRedirect(urllib.request.HTTPRedirectHandler):
    def redirect_request(self, req, fp, code, msg, headers, newurl):
        host = urllib.parse.urlparse(newurl).hostname
        if host in ALLOWED_HOSTS:
            return super().redirect_request(req, fp, code, msg, headers, newurl)
        return None


PREFIXES = {
    "P/": "https://platform.claude.com/docs/en/",
    "C/": "https://code.claude.com/docs/en/",
    "H/": "https://support.claude.com/en/articles/",
}
ROW_RE = re.compile(r"^\|\s*S\d+\s*\|\s*([^\s|]+)", re.M)


def collect_urls():
    text = SOURCES.read_text(encoding="utf-8")
    urls = []
    for match in ROW_RE.finditer(text):
        token = match.group(1).rstrip(",.")
        for prefix, base in PREFIXES.items():
            if token.startswith(prefix):
                token = base + token[len(prefix):]
                break
        else:
            token = "https://" + token
        host = urllib.parse.urlparse(token).hostname
        if host in ALLOWED_HOSTS and token not in urls:
            urls.append(token)
    return urls


def fingerprint(url):
    request = urllib.request.Request(url, headers={"User-Agent": "rewording-maintain/1.0"})
    opener = urllib.request.build_opener(NoRedirect)
    with opener.open(request, timeout=30) as response:
        body = response.read(MAX_BYTES).decode("utf-8", errors="replace")
    body = re.sub(r"<script.*?</script>|<style.*?</style>", " ", body, flags=re.S)
    body = re.sub(r"<[^>]+>", " ", body)
    body = re.sub(r"\s+", " ", body).strip().lower()
    return hashlib.sha256(body.encode("utf-8")).hexdigest()


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--accept", action="store_true", help="save the current fingerprints as the new snapshot")
    args = parser.parse_args()
    old = json.loads(SNAPSHOT.read_text(encoding="utf-8")) if SNAPSHOT.is_file() else {}
    new, changed, unreachable, fresh = {}, [], [], []
    for url in collect_urls():
        try:
            new[url] = fingerprint(url)
        except (urllib.error.URLError, TimeoutError, OSError) as error:
            unreachable.append("%s (%s)" % (url, getattr(error, "reason", error)))
            continue
        if url not in old:
            fresh.append(url)
        elif old[url] != new[url]:
            changed.append(url)
    print("checked %d pages" % (len(new) + len(unreachable)))
    for label, items in (("changed", changed), ("new, no earlier snapshot", fresh), ("unreachable", unreachable)):
        if items:
            print("%s:" % label)
            for item in items:
                print("  " + item)
    if changed:
        print("Review the rows that cite the changed pages in references/sources.md, then run with --accept.")
    if args.accept:
        merged = dict(old)
        merged.update(new)
        SNAPSHOT.write_text(json.dumps(merged, indent=2, sort_keys=True), encoding="utf-8")
        print("snapshot saved")
    return 1 if changed else 0


if __name__ == "__main__":
    sys.exit(main())
