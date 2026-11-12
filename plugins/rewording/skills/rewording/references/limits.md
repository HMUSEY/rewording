# 06 Plans and Limits

Volatile file. Verified 2026-11-07 unless marked. Anthropic does not publish fixed message counts per plan (V S32). Never quote one.

## 1. Plans

| Item | Pro | Max | Ultra | Team | Status |
|---|---|---|---|---|---|
| Price per month | $20, or $17 billed annually | $100 | $200 | Standard $20 or $25, Premium $100 or $125 (annual or monthly) | V S50 |
| Five-hour limit | Yes | 5x Pro | None for verified accounts | U | V S39, S40 |
| Weekly limit | Yes | 5x Pro | 10x Pro, plus a separate Fable limit | U | V S39, S40 |
| Fable 5 and 5.1 | Usage credits from the first request | Up to 50% of weekly limits | Up to 50% of weekly limits | Premium seats. Standard seats use credits | V S38 |
| Claude Code | Yes | Yes | Yes | Yes | V S30 |
| Monthly API credits | None | $100 | $200 | $20 per Standard seat, $100 per Premium seat, pooled, capped at $500 | V S31 |

- The plan formerly called Max 20x is now Ultra (V S40). Ultra fits wherever Max fits.
- API credits do not apply in Claude Code or the apps (V S31).

## 2. Feature availability

"Paid" means Pro, Max, Ultra, Team and Enterprise.

| Feature | Free | Pro, Max, Ultra | Team, Enterprise | Status |
|---|---|---|---|---|
| Projects | Max 5 | Yes | Yes, with sharing | V S18 |
| Project retrieval mode (RAG) | No | Yes | Yes | V S46 |
| Project memory kept separate ("Use account memory" off in the project's Memory section) | Yes | Yes | Yes | V S47 |
| Memory | On | On | On for orgs created from Oct 31, 2026 | V S47 |
| Personal preferences in Settings, Profile (global instructions) | Yes | Yes | Yes | T S57 |
| New version of Projects | No | Beta for select Claude Code users | Later | V S18 |
| Chat and Cowork merged into one Claude | Later | Rolling out from Sep 16, 2026 | Team later, Enterprise GA Oct 23 | T S16 |
| Code execution and file creation | Yes, a Settings toggle | Same | Owners control it | V S48 |
| Scheduled tasks | No | Yes | Yes | V S50 |
| Research | No | Yes | Yes | V S50 |
| Skills (code execution on) | Yes | Yes | Yes | V S15, S50 |
| Claude in Chrome | No | Yes | Yes | V S50 |
| Microsoft 365 add-ins (Excel, Word, PowerPoint, Outlook) | No | Yes, Outlook beta label T S23 | Yes | V S50 |
| Google Workspace add-in | U | U | U | U |
| Claude Tag in Slack | No | No | Yes | V S50 |
| Claude Design | Yes | Yes | Yes | V S50 |
| Claude Docs and Slides (beta) | Pages conflict | Yes | Yes | T S16, S50 |
| Claude Dashboards (beta) | No | Yes | Yes | V S50 |
| Claude Motion (beta) | No | No | Yes | V S50 |
| Claude Science | No | Yes | Yes | V S50 |
| Claude Security (beta) | No | No | Enterprise only | V S50 |
| Claude Duet (research preview, waitlist) | No | Yes | No | T S28 |
| Connectors | Yes, custom connector count U | Yes | Yes | V S50 |
| Voice, incognito, web search | Yes | Yes | Yes | V S50 |
| Effort control in the apps (5.x models) | Yes | Yes | Yes | V S45 |
| Artifact storage limits, artifact types Sheets, Whiteboard, Tasks, Design System | U | U | U | U |

## 3. Numeric limits

| Limit | Value | Type | Status |
|---|---|---|---|
| API context | 1M tokens | Hard limit | V S1 |
| App context | Up to 1M, varies by model | Hard limit | V S50 |
| API output per request | 128K tokens | Hard limit | V S1 |
| Batch output | 300K with output-300k-2026-03-24 on listed models (Opus 5.5, Opus 5, Sonnet 5.5, Sonnet 5 and older). Fable 5.1 and Haiku 5.5 not seen on the list | Hard limit | V S6 |
| Batch discount | 50% | Price | V S6 |
| Prompt caching minimum | 512 tokens on Opus 5.5 and Haiku 5.5 | Hard limit | V S5, S43 |
| CLAUDE.md | Under 200 lines per file | Recommendation | V S11 |
| MEMORY.md load | First 200 lines or 25KB | Hard limit | V S11 |
| Skill name and description | 64 and 1,024 characters | Hard limit | V S14 |
| SKILL.md body | Under 500 lines | Recommendation | V S14 |
| Subagent descriptions combined | Warning above 15,000 tokens, built-ins excluded | Recommendation | V S12 |
| Free projects | 5 | Hard limit | V S18 |
| Project retrieval threshold | Not published | Note | V S46 |
| Prompt length in words | No word limit. The context window governs | Note | V S32 |
| Images per request, Files API sizes, artifact runtime limits, Free custom connectors | Not verified | Do not quote | U |

## 4. When a limit is reached

- Output cut off: raise max_tokens, or reply "continue", or split the request into one section per reply.
- Input too large: split it, summarize before re-pasting, use a Project with knowledge files, or on the API use compaction (07).
- Usage limit reached in the apps: wait for the five-hour or weekly reset, or use usage credits.

## 5. Usage Policy (V S33, S49, new version effective November 12, 2026)

- Prohibited: illegal activity, compromising critical infrastructure, unauthorized access to systems, weapons development, inciting violence or hate, privacy and identity violations, harm to children, sustained and needless abuse of the models, disinformation, deceptive campaigns or artificial activity, undermining democratic processes, prohibited surveillance (including tracking people without consent and deciding who to investigate, arrest or charge), fraud and predatory practices, platform abuse, sexually explicit content.
- High-risk uses (legal, health, finance, housing, employment and similar decisions about people): a qualified human in the loop, and the affected person is told AI was used. Hardware: an operator can observe and stop it, and it holds a safe state if Claude disconnects.

## 6. Warning thresholds

Local settings used by the skill and precheck.py. They are not product limits.

| Level | Estimated input tokens | Action |
|---|---|---|
| normal | under 20,000 | no warning |
| heavy | 20,000 to 49,999 | warn, suggest attaching files instead of pasting, a subagent for exploration, or a fresh session |
| very heavy | 50,000 and above | warn before anything else, recommend splitting, Project knowledge or a fresh session, and an exact count with count_tokens when an API key exists |

- The estimate is Latin characters divided by 4, plus Arabic characters divided by 2.5, plus other characters divided by 2. Treat it as plus or minus 30 percent (inference).
- The estimate covers only the typed request. Attached files, @file references and earlier turns enter the context in full and are not counted (T S13).
- Claude cannot see the remaining balance of the user's plan, so a usage warning is always an estimate (T S32).
