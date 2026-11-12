## 7. Skill

Voice: an imperative procedure for Claude. Only what Claude does not already know. Frontmatter, then Markdown headings and numbered steps, no XML tags for the main sections. Description in third person (recommendation).

Paste targets:
- name: (Required) lowercase letters, numbers and hyphens, max 64 characters, no "claude" or "anthropic" (V S14).
- description: (Required) what it does and when to use it, with the phrases users really say, max 1,024 characters (V S14). The most important field, because Claude matches requests against it.
- SKILL.md body: (Required) under 500 lines (V S14).
- Reference files and scripts: (Optional) one level deep, each with a line saying when to load it.
- Tests: (Optional, recommended) 2 prompts that should trigger and 1 that should not.

```
---
name: [skill-name]
description: [What it does]. Use when [triggers and the phrases users say].
---

# [Title]

## Steps
1. [Exact step for fragile parts.]
2. [General guidance for judgment calls.]

## Output
[Format.]

## Check
[How to validate the output. Fix and re-check once.]

## References
- [reference.md]: read when [condition].
```

Notes:
- Only name and description preload. The body loads when triggered (V S14).
- Skills work on all plans with code execution on (V S15).
- In Claude Code, use .claude/skills/NAME/SKILL.md or ~/.claude/skills/NAME/SKILL.md (V S51). `allowed-tools` pre-approves tools for the invoking turn and does not restrict. `disallowed-tools` removes tools (V S51).
- The upload path in claude.ai is U. Tell the user to check S15.
- `disable-model-invocation: true` makes the skill manual only: it runs when the user types /name and Claude never loads it on its own. `${CLAUDE_SKILL_DIR}` gives the skill folder inside the body and in allowed-tools rules (V S51).
- Claude Code ignores unknown frontmatter fields. For claude.ai keep only name and description in the uploaded copy (inference, S14).
- If it does not trigger, fix the description, not the body.
- Delivery: text with the file name and path, written to disk only on request.
