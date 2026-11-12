# 07 API and Claude Code Reference

Volatile file. Status codes and keys are in 09.

## 1. API features

| Feature | Header or identifier | Status |
|---|---|---|
| Effort | output_config.effort | V S2 |
| Per-message effort | mid-conversation-output-config-2026-07-01 (beta), keeps the prompt cache | V S7 |
| Task budgets | task-budgets-2026-03-13, advisory only (beta) | V S36 |
| Mid-conversation system messages | GA, no header | V S7 |
| Turn-scoped system messages (clear_at) | mid-conversation-system-clear-at-2026-08-21 | V S7 |
| Inline tools and tool changes mid-conversation | inline-tools-2026-09-15. Release notes also list mid-conversation-tool-changes-2026-07-01. Check the page before hard-coding | T S7, S8 |
| MCP connector | mcp-client-2026-09-15, replaces mcp-client-2025-11-20 | V S55 |
| On-demand compaction | compact-2026-09-04 | V S8 |
| Threshold compaction | compact-2026-01-12, context_management edit compact_20260112 | V S37 |
| Advisor tool | advisor-tool-2026-03-01, tool type advisor_20260301. Opus 4.8, Opus 4.7 and Sonnet 5 are rejected as advisors | V S9 |
| Batch 300K output | output-300k-2026-03-24 | V S6 |
| Opus 5.5 progress updates | thinking display "updates" with thinking-display-updates-2026-08-18 | V S44 |
| Opus 5.5 thinking replay control | prefix_mismatch_behavior with thinking-binding-controls-2026-08-01 | V S5 |
| Computer use on Opus 5.5 | computer_toolset_20260801. computer_20251124 is rejected on the Claude API | V S5 |
| Opus 5.5 fast mode | speed "fast" | V S5 |
| Structured outputs | output_config.format with type json_schema for JSON outputs, no beta header. strict: true on a tool for strict tool use | V 2026-11-07 S56 |
| Skills in the API | GA, no skills header, code execution tool required | V S53 |
| Browser toolset version, Files API limits, memory tool limits, SessionStore | not verified | U |

API rules:
- The system prompt goes in the top-level system field.
- max_tokens is required and caps thinking plus text.
- The API is stateless. Send the full messages array and return thinking blocks unchanged.
- Use effort, not budget_tokens.
- Forced tool use returns 400 on Opus 5.5, Fable 5.1 and Sonnet 5.5. Use tool_choice auto with strict tools, or structured outputs.
- Put static content first and mark it for caching.

## 2. Claude Code

| Topic | Fact | Status |
|---|---|---|
| CLAUDE.md locations | managed policy, ~/.claude/CLAUDE.md, ./CLAUDE.md or ./.claude/CLAUDE.md, ./CLAUDE.local.md | V S11 |
| Rule files | .claude/rules/*.md. Without paths frontmatter they load at launch. With paths they load when matching files are read or edited | V S11 |
| Imports | @path inside CLAUDE.md, up to four hops | V S11 |
| Subagent files | .claude/agents/, ~/.claude/agents/, plugin agents/, --agents, managed | V S12 |
| Subagent fields | name and description required. tools, disallowedTools, model, permissionMode, maxTurns, autoCompactWindow, skills, mcpServers, hooks, memory, background, omitClaudeMd, effort, isolation, color, initialPrompt optional | V S12 |
| Built-in subagents | Explore (read-only), Plan, general-purpose | V S12 |
| Hook events | SessionStart, UserPromptSubmit, PreToolUse, PostToolUse, Stop, SubagentStart, SubagentStop, Notification and more. SubagentStart cannot block | V S13 |
| Hook handler types | command, http, mcp_tool, prompt, agent. Support varies by event | V S13 |
| UserPromptSubmit | fires on every prompt, matchers ignored. stdin field `prompt`. Output: `{"decision":"block","reason":...}` or `hookSpecificOutput.additionalContext`. Exit 2 blocks. Default timeout 30 seconds | V S13 |
| UserPromptExpansion | fires when a typed slash command or skill expands, matcher on `command_name`. stdin fields `prompt`, `command_name`, `command_args`, `command_source`, `expansion_type`. Same block and additionalContext output | V S13 |
| Plugin layout | .claude-plugin/plugin.json (only `name` required), skills/NAME/SKILL.md, hooks/hooks.json with a top-level "hooks" key, `${CLAUDE_PLUGIN_ROOT}` in hook commands. Plugin skills run as /plugin-name:skill-name. Names starting with claude- or anthropic- are reserved | V S61 |
| Marketplace | .claude-plugin/marketplace.json with name, owner, plugins (entry name, source "./"). `claude plugin marketplace add owner/repo` then `claude plugin install name@marketplace`. `claude plugin validate` checks both | V S62 |
| Headless mode | claude -p | V S52 |
| /goal, /loop | available | V S52 |
| /context, /init | available | V S11 |
| Plan mode | a permission mode where Claude reads and plans without editing. Entered with Shift+Tab or /plan | T S58 |
| /clear | not verified on an official page | U |
| CLI flags --model, --effort (low, medium, high, xhigh, max), --permission-mode (acceptEdits, auto, bypassPermissions, manual, dontAsk, plan), -p, --output-format, --max-budget-usd, --agents, --plugin-dir, --allowedTools | V S59 |
| CLAUDE_CODE_SUBAGENT_MODEL and CLAUDE_CODE_SUBAGENT_MODEL_FORCE | present in the installed CLI 2.1.322 | V S59 |
| --advisor | documented per the 2026-11-11 research report, absent from the installed CLI help. Stops when feature flags are disabled | T S59 |
| --subagents | not a real flag. Use CLAUDE_CODE_SUBAGENT_MODEL or `model:` in a subagent file | V S59 |
| --max-turns, opusplan alias | not seen in the installed CLI help | U |
| /doctor prompt audit | v2.1.283 and later | V S11 |
| dispatch command, default model, sandbox network rules | not verified | U |

## 3. Skills

| Rule | Status |
|---|---|
| Name max 64 characters, lowercase letters, numbers, hyphens, no XML, no reserved words | V S14 |
| Description max 1,024 characters, states what and when | V S14 |
| Body under 500 lines, detail in referenced files | V S14 |
| Only name and description preload | V S14 |
| allowed-tools pre-approves listed tools for the invoking turn. disallowed-tools removes tools | V S51 |
| $ARGUMENTS substitution | V S51 |
| Third-person descriptions | recommendation |
| Upload path in claude.ai | U |
| disable-model-invocation: true makes a skill manual only (user types /name) | V S51 |
| ${CLAUDE_SKILL_DIR} expands to the skill folder in the body and in allowed-tools rules | V S51 |
| Claude Code lists description plus when_to_use up to 1,536 characters. claude.ai caps description at 1,024 | V S51, S14 |
| Claude Code ignores unknown frontmatter fields | V S51 |

## 4. API calls used by tools/rw_api.py

| Call | Fact | Status |
|---|---|---|
| Token counting | POST /v1/messages/count_tokens with model and messages, returns input_tokens, no charge | T S60 |
| Messages | POST /v1/messages with x-api-key, anthropic-version 2023-06-01, system as a list of blocks with cache_control | V S2, S3 |
| Prompt improver and generator in the Console, and /v1/experimental improve_prompt | retired on 2026-08-17 | T S8 |
