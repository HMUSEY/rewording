#!/usr/bin/env python3
import json
import re
import sys
import zipfile
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent
PLUGIN = REPO / "plugins" / "rewording"
SKILL = PLUGIN / "skills" / "rewording"
DIST = REPO / "dist"
PLUGIN_ZIP = DIST / "rewording-plugin.zip"
SKILL_ZIP = DIST / "rewording-skill.zip"
SKIP_PARTS = {"__pycache__", ".DS_Store"}
NAME_RE = re.compile(r"^[a-z0-9]+(?:-[a-z0-9]+)*$")
MAX_DESCRIPTION = 200


def stop(message):
    sys.exit("build_zip: " + message)


def frontmatter(text):
    if not text.startswith("---\n"):
        stop("SKILL.md has no frontmatter")
    head, body = text[4:].split("\n---\n", 1)
    fields = {}
    for line in head.splitlines():
        key, _, value = line.partition(":")
        fields[key.strip()] = value.strip()
    return fields, body


def check_skill(fields):
    name = fields.get("name", "")
    description = fields.get("description", "")
    if not NAME_RE.match(name) or len(name) > 64 or "claude" in name or "anthropic" in name:
        stop("invalid skill name")
    if not description or len(description) > MAX_DESCRIPTION or "<" in description or ">" in description:
        stop("description must be 1 to %d characters with no angle brackets" % MAX_DESCRIPTION)
    if name != SKILL.name:
        stop("skill folder name must match the skill name")
    return name, description


def plugin_files():
    for path in sorted(PLUGIN.rglob("*")):
        relative = path.relative_to(PLUGIN)
        if path.is_file() and not SKIP_PARTS & set(relative.parts) and path.suffix != ".pyc":
            yield path, relative.as_posix()


def verify(archive_path, expect_manifest):
    with zipfile.ZipFile(archive_path) as archive:
        names = archive.namelist()
    roots = {name.split("/", 1)[0] for name in names}
    skill_files = [name for name in names if name.rsplit("/", 1)[-1].lower() == "skill.md"]
    manifests = [name for name in names if name.endswith(".claude-plugin/plugin.json")]
    if len(roots) != 1:
        stop("%s must have one top-level folder" % archive_path.name)
    if len(skill_files) != 1:
        stop("%s must hold exactly one SKILL.md, found %s" % (archive_path.name, skill_files))
    if expect_manifest and manifests != ["rewording/.claude-plugin/plugin.json"]:
        stop("%s must hold the manifest at rewording/.claude-plugin/plugin.json" % archive_path.name)
    if not expect_manifest and manifests:
        stop("%s must not hold a plugin manifest" % archive_path.name)
    print("%s: %d files, %d bytes, ok" % (archive_path.name, len(names), archive_path.stat().st_size))


def build_plugin_zip():
    json.loads((PLUGIN / ".claude-plugin" / "plugin.json").read_text(encoding="utf-8"))
    with zipfile.ZipFile(PLUGIN_ZIP, "w", zipfile.ZIP_DEFLATED) as archive:
        for path, relative in plugin_files():
            archive.write(path, "rewording/" + relative)
        archive.write(REPO / "LICENSE", "rewording/LICENSE")
    verify(PLUGIN_ZIP, True)


def build_skill_zip():
    fields, body = frontmatter((SKILL / "SKILL.md").read_text(encoding="utf-8"))
    name, description = check_skill(fields)
    body = body.replace("${CLAUDE_SKILL_DIR}/", "")
    text = "---\nname: %s\ndescription: %s\n---\n%s" % (name, description, body)
    with zipfile.ZipFile(SKILL_ZIP, "w", zipfile.ZIP_DEFLATED) as archive:
        archive.writestr("%s/SKILL.md" % name, text)
        for path in sorted((SKILL / "references").rglob("*.md")):
            archive.write(path, "%s/%s" % (name, path.relative_to(SKILL).as_posix()))
    verify(SKILL_ZIP, False)


def main():
    DIST.mkdir(exist_ok=True)
    check_skill(frontmatter((SKILL / "SKILL.md").read_text(encoding="utf-8"))[0])
    build_plugin_zip()
    build_skill_zip()


if __name__ == "__main__":
    main()
