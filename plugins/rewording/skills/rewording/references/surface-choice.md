# 03 Surface Specs

Structure is stable. Plan facts must match 06. Status codes and source keys are in 09.

Each surface has its own voice, paste targets, template and format (01 section 3). Use only the matching section. Never apply one generic template to every surface.

## 1. Choosing the surface

Use the surface the user names. Otherwise pick the lightest surface that fully solves the need and give one line of reasoning. Decide the mode first: Automation (one-way execution), Augmentation (working together) or Agency (Claude set up to work on its own).

"Paid" means Pro, Max, Ultra, Team and Enterprise. Ultra fits wherever Max fits.

| Need | Surface | Plans | Status |
|---|---|---|---|
| One-off answer, draft or file | Chat | All | V S50 |
| Rules or reference reused across many chats | Project | All, Free max 5 | V S18 |
| Defaults for every chat | Global instructions | All | T S57 |
| Multi-step work on files, apps or the web, run once | Cowork task | Paid, merging into Claude | T S16 |
| The same work on a schedule | Scheduled task | Paid | V S50 |
| A procedure Claude loads when a matching request appears | Skill | All, code execution on | V S15 |
| Skills, connectors and agents packaged for a role | Plugin | U | U |
| Building or changing software | Claude Code build | Paid | V S30 |
| Standing repository rules | CLAUDE.md | With Claude Code | V S11 |
| A focused worker inside Claude Code | Subagent | With Claude Code | V S12 |
| An action that must run every time with no judgment | Hook | With Claude Code | V S13 |
| Work inside websites | Claude in Chrome | Paid | V S50 |
| Work inside Excel, PowerPoint, Word or Outlook | Microsoft 365 add-in | Paid | V S50 |
| Claude in Slack channels | Claude Tag | Team, Enterprise | V S50 |
| Visual design on a canvas | Claude Design brief | All | V S50 |
| Reaching an outside system | MCP connector | All | V S29 |
| A product or service that calls Claude | API system prompt | API billing. Max, Ultra and Team include monthly credits | V S31 |
| A custom agent whose steps cannot be known in advance | Agent build | U | U |
| Scientific research with code and data | Claude Science | Paid | V S50 |
| Finding and patching vulnerabilities in a codebase | Claude Security | Enterprise, beta | V S50 |
| A proactive agent you message, working across connected apps and asking before consequential actions | Claude Duet | Pro, Max and Ultra, research preview with a waitlist | T S28 |
| Anything not listed | Fallback (section 21) | | |

Rules:
- Chat when the work happens once. Project when the same rules or files serve many chats. Skill when a procedure should trigger on its own across chats and Projects. Plugin only to package several skills for a role.
- Code across a repository goes to Claude Code. Quick questions stay in Chat. Repeating work becomes a Scheduled task or a Skill.
- When the need spans two surfaces, deliver the main one and name the second in one line.
- When the surface needs a plan the user does not have, say so and offer the nearest option on their plan.
