## 12. Hook (Claude Code)

Voice: JSON configuration only.

Choose the event by how narrow the trigger must be. UserPromptSubmit fires on every prompt and ignores matchers. UserPromptExpansion fires only when a typed slash command or skill expands and matches on command_name (V S13).

Paste targets:
- JSON in .claude/settings.json (project) or ~/.claude/settings.json (user): (Required)
- Test steps: (Required, steps for the user, not pasted anywhere)

```json
{
  "hooks": {
    "PostToolUse": [
      {
        "matcher": "Edit|Write",
        "hooks": [
          { "type": "command", "command": "[command]" }
        ]
      }
    ]
  }
}
```

Notes:
- Events include SessionStart, UserPromptSubmit, UserPromptExpansion, PreToolUse, PostToolUse, Stop, SubagentStart, SubagentStop and Notification (V S13).
- Handler types: command, http, mcp_tool, prompt, agent. Support varies by event (V S13).
- Exit code 2 blocks only on events that can block, such as PreToolUse. SubagentStart cannot block.
- Never put secrets in the command. Delivery: ملف.
