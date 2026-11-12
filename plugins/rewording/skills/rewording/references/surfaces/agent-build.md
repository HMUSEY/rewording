## 19. Agent build (Agent SDK or Managed Agents)

Voice: one plain opening sentence on what the agent is and who it serves, then tagged sections.

Paste target: Spec (Required)

```
[One sentence: what the agent is and who it serves.]

<goal>
[Measurable goal and when it is done.]
</goal>

<tools>
- [name]: [purpose], [reversible or not]. Use when [condition]. Do not use when [condition].
</tools>

<permissions>
- Allowed without asking: [actions]
- Needs human approval: [actions]
</permissions>

<loop>
Make parallel calls for independent steps. Give a one-line progress update after each major step. Stop when [condition] or after [budget].
</loop>

<context_management>
[Compaction, state files, subagents for isolated work.]
</context_management>

<obstacles>
Report what blocked you, what you tried and what you need.
</obstacles>

<checks>
[How results are verified.]
</checks>
```

Notes: plans and billing are U. A single call with retrieval is often enough. Use fixed steps when steps are predictable. Test in a sandbox first.
