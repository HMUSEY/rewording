# 09 Maintenance and Changelog

For the owner, and for the skill when a fact is missing or marked U.

## 1. Status codes

- V: verified on an official page, with date and source key.
- T: in transition. A rollout, a beta with changing scope, conflicting official pages, or a fact seen only in secondary reports.
- U: unverified. Keep the row, never state the fact.

## 2. Template for a new model

```
### [Model name]
- API ID:
- Price $/MTok in/out:
- Context and max output:
- Thinking and default effort:
- Effort levels:
- Knowledge cutoff:
- Plan access in the apps:
- What it rejects (400 errors):
- Prompt tuning lines:
- Status: V YYYY-MM-DD [key]
- Source: [official URL]
```

## 3. Template for a new product or surface

```
### [Product name]
- What it is: one line
- Plans: Free / Pro / Max / Ultra / Team / Enterprise
- Stage: GA, beta or research preview
- Spec: section in 03, or Fallback
- Where the user configures or pastes:
- Limits with numbers:
- Facts that change a prompt:
- Status: V YYYY-MM-DD [key]
- Source: [official URL]
```

## 4. Source keys

All use https. P = platform.claude.com/docs/en, C = code.claude.com/docs/en, H = support.claude.com/en/articles.

| Key | URL |
|---|---|
| S1 | P/models/overview |
| S2 | P/build-with-claude/effort |
| S3 | P/build-with-claude/prompt-engineering/claude-prompting-best-practices |
| S4 | P/build-with-claude/thinking-troubleshooting |
| S5 | P/models/opus-5-5/whats-new-opus-5-5 |
| S6 | P/build-with-claude/batch-processing |
| S7 | P/build-with-claude/mid-conversation-system-messages |
| S8 | P/release-notes/overview |
| S9 | claude.com/resources/articles/the-advisor-strategy |
| S10 | P/build-with-claude/compaction |
| S11 | C/memory |
| S12 | C/sub-agents |
| S13 | C/hooks |
| S14 | P/agents-and-tools/agent-skills/best-practices |
| S15 | H/12512176-what-are-skills |
| S16 | claude.com/blog/cowork-is-now-claude |
| S17 | H/13854387-schedule-recurring-tasks-in-claude-cowork |
| S18 | H/9517075-what-are-projects |
| S19 | H/9519177-how-can-i-create-and-manage-projects |
| S20 | H/11088861-use-research-on-claude |
| S21 | H/17153992-what-are-artifacts-and-how-do-i-use-them |
| S22 | H/12902446-claude-in-chrome-permissions-guide |
| S23 | H/12650343-use-claude-for-excel (Word 14465370, PowerPoint 13521390, Outlook 14855664) |
| S24 | H/11506255-get-started-with-claude-in-slack |
| S25 | H/14604416-get-started-with-claude-design |
| S26 | H/16563838-get-started-with-claude-science |
| S27 | H/14661296-use-claude-security |
| S28 | H/17631495-get-started-with-claude-duet |
| S29 | H/11175166-get-started-with-custom-connectors-using-remote-mcp |
| S30 | H/11145838-use-claude-code-with-your-pro-max-or-ultra-plan |
| S31 | H/17154008-monthly-api-credits-for-max-ultra-and-team-plans |
| S32 | H/11647753-how-do-usage-and-length-limits-work |
| S33 | www.anthropic.com/legal/aup |
| S34 | www.anthropic.com/claude-opus-5-5 |
| S35 | P/models/haiku-5-5/overview |
| S36 | P/build-with-claude/task-budgets |
| S37 | P/build-with-claude/compaction-threshold |
| S38 | H/15424964-claude-fable-models-on-your-plan |
| S39 | H/11049741 (What is the Max plan) |
| S40 | H/17728952-what-is-the-ultra-plan |
| S41 | P/models/fable-5-1/overview |
| S42 | P/models/sonnet-5-5/whats-new-sonnet-5-5 |
| S43 | P/models/haiku-5-5/whats-new-haiku-5-5 |
| S44 | P/build-with-claude/prompt-engineering/prompting-claude-opus-5-5 |
| S45 | H/8664678-change-the-model-effort-and-thinking-settings |
| S46 | H/11473015-retrieval-augmented-generation-rag-for-projects |
| S47 | H/11817273-use-claude-s-chat-search-and-memory-to-build-on-previous-context |
| S48 | H/12111783-create-and-edit-files-with-claude |
| S49 | www.anthropic.com/news/2026-usage-policy-update |
| S50 | claude.com/pricing |
| S51 | C/skills |
| S52 | C/goal |
| S53 | P/build-with-claude/skills-guide |
| S54 | P/about-claude/pricing |
| S55 | P/agents-and-tools/mcp-connector |
| S56 | P/build-with-claude/structured-outputs |
| S57 | H/10185728-understanding-claude-s-personalization-features |
| S58 | C/permission-modes |
| S59 | C/cli-reference, and the installed CLI help (claude --help, 2.1.322, checked 2026-11-11) |
| S60 | P/build-with-claude/token-counting |
| S61 | C/plugins-reference |
| S62 | C/plugins/publish |
| S63 | H/12260368-use-incognito-chats |

## 5. Monthly routine (about 30 minutes)

1. Run `python3 tools/maintain.py`. It lists the source pages that changed since the last accepted snapshot. Read only those, plus the platform release notes (S8) and claude.com/pricing (S50).
2. Edit the matching rows in 03, 05, 06 and 07. Update the date and status.
3. Add a line to the log below.
4. Run `python3 evals/run.py` (offline checks) and `python3 evals/run.py --claude-code` (live cases through Claude Code). Check that each reply is a prompt, not the task's result, that each prompt uses its use type's format (01 section 3), and that settings and limits reflect the new rows.
5. After the facts are re-verified, run `python3 tools/maintain.py --accept` to save the new snapshot.

Rules:
- Model launch: fill the model template, add the row to 05, add new tuning lines, mark the old model Legacy.
- New surface: fill the product template, add a row to surface-choice.md and a file in surfaces/, add the file to the table in SKILL.md, add a plan row to limits.md, add an example to examples.md in the surface's format.
- If a source page moves or contradicts a row, change V to T until it is settled. Fix the URL here.
- Edit SKILL.md only when a file is renamed or the reply order changes. Then run `python3 tools/build_zip.py` to rebuild the upload ZIP.

## 6. Verification log

| Date | Scope | Result |
|---|---|---|
| 2026-11-07 | Full rebuild | 64 claims checked. Most confirmed, 16 corrected, 12 removed or marked U |
| 2026-11-07 | Critical review | Restored real paste targets per surface, multi-block output, delivery mode, fill-in table, weak-answer rule, full examples and checks bank |
| 2026-11-07 | Official-source audit | Fixed: Cowork merge status, Project memory setting, conditional file delivery, Ultra and Team fit, Haiku 5.5 forced tools, CLAUDE.md 4 MiB claim removed, hook types, allowed-tools, mid-conversation messages GA, Skills API GA, computer use toolset, Usage Policy. Added: Dashboards, Motion, Security, Duet, fast mode, new Projects beta, effort control in apps. Instructions now forbid producing the task's result |
| 2026-11-07 | Format and audit-turn review | One format per use type set in 01 and applied in 02 to 05 and 08. Audit and task-itself turns return one prompt with no tool calls. Structured outputs and personal preferences verified (S56, S57). Duet key moved to S28 and set to T. Plan mode set to T (S58), /clear and Agent build plans set to U. Examples added for every surface |
| 2026-11-11 | Move to a skill | Content moved from the Project into one manual-only skill. Verified on official pages: disable-model-invocation, CLAUDE_SKILL_DIR, UserPromptSubmit and UserPromptExpansion hooks, plugin and marketplace layout (S51, S13, S61, S62). Verified on the installed CLI 2.1.322: flags, permission modes, CLAUDE_CODE_SUBAGENT_MODEL (S59). --advisor set to T. --subagents marked not real |

## 7. Open items

- Docs and Slides on Free: S16 and S50 conflict.
- Free custom connector count, artifact storage limits, artifact types Sheets, Whiteboard, Tasks, Design System.
- Images per request, Files API limits, caching minimum on Sonnet 5.5 and Fable 5.1.
- Batch 300K on Fable 5.1 and Haiku 5.5.
- Structured outputs GA list for Fable 5.1, Sonnet 5.5 and Haiku 5.5 on S56.
- Forced tools on Haiku 5.5.
- Team five-hour and weekly limits.
- Style location in Settings, and personal preferences plan coverage on S57.
- Plan mode on S58 and /clear on an official page.
- Agent build plans and billing.
- Claude Duet plan list on S28.
- Skill upload path in claude.ai and plugin install locations.
- Google Workspace add-in plans and the Outlook beta label.
- dispatch in Claude Code.
- Token counting endpoint details (S60) and prompt improver retirement (S8) were not re-fetched.
- claude.ai accepts only name and description in SKILL.md frontmatter: unverified.
- Exact command_name that UserPromptExpansion reports for a plugin skill.
- Menu locations of memory and search-chats controls (S47, S57, S63).
