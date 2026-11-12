## 17. MCP connector

Setup targets:
- Connector name and remote server URL: (Required)
- OAuth details: (Optional)

Use brief for prompts that rely on it: (Required). One plain opening sentence with the task, then tagged sections.

```
Use [connector] to [task].

<permissions>
You may read [scope]. You may change [scope] only after I approve each change.
</permissions>

<output>
[Format.]
</output>
```

Notes: connectors on all plans (V S50). The Free custom connector count is U. The server must be reachable from the public internet. Tools act, Resources provide data, Prompts provide templates.
