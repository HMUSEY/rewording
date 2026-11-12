## 11. CLAUDE.md

Voice: terse Markdown facts and commands. No XML tags and no prose.

Paste target: File content (Required) at ./CLAUDE.md or ./.claude/CLAUDE.md. Personal rules go in ~/.claude/CLAUDE.md. Topic rules go in .claude/rules/*.md (V S11).

```
# [Project]
[One line: what it is.]

## Commands
- Build: [command]
- Test: [command]
- Lint: [command]

## Structure
- [path]: [what lives there]

## Conventions
- [Rule Claude gets wrong without being told]

## Boundaries
- Ask before [action].
```

Notes: keep it under 200 lines (V S11). For each line, ask whether removing it would cause mistakes, and cut it if not. Import other files with @path.
