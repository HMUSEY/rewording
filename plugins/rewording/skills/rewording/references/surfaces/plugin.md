## 8. Plugin

Voice: a plain list of its parts. Each skill, subagent or hook in it gets its own spec in its own format (skill-surface.md, subagent.md and hook.md).

Paste targets:
- Plugin name and purpose: (Required) the role or team it serves.
- Skills it bundles: (Required) each with its own Skill spec.
- Agents, hooks, MCP servers, commands: (Optional)

Notes:
- Write the skills first and package them last. Plans for plugins are U.
- Layout: .claude-plugin/plugin.json (name required, kebab-case, no claude- or anthropic- prefix), skills/NAME/SKILL.md, hooks/hooks.json, scripts. Plugin skills run as /plugin-name:skill-name (V S61).
- Share through your own marketplace: .claude-plugin/marketplace.json with name, owner and plugins, then `claude plugin marketplace add owner/repo` and `claude plugin install name@marketplace`. Check with `claude plugin validate` (V S62).
- In Claude Code, plugin subagents ignore hooks, mcpServers and permissionMode (V S12).
- Delivery: text with file names and paths, written to disk only on request.
