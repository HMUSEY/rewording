## 9. Subagent (Claude Code)

First ask whether the intermediate work matters to the user. If it does, keep it in the main conversation.

Voice: frontmatter, then a second-person body with a narrow role, numbered steps and a fixed return format.

Paste target: the file .claude/agents/NAME.md (project) or ~/.claude/agents/NAME.md (user).
- name: (Required)
- description: (Required) when to delegate. Add "Use proactively" for automatic use.
- tools: (Optional, recommended) least privilege. Read-only for research, Bash without Edit or Write for review.
- model, effort, skills, permissionMode, maxTurns, memory, isolation, background: (Optional)
- Body: (Required)

```
---
name: [name]
description: [When to delegate]. Use proactively [when].
tools: Read, Grep, Glob
---

You [role] and report back. [What you never do.]

1. [Step]
2. [Real check: run X and read the output.]
3. Return only:
   - [Field]
   - [Field]
If blocked, say what blocked you, what you tried and what you need.
```

Notes: the fixed return format gives the agent a natural stopping point. Delivery: ملف.
