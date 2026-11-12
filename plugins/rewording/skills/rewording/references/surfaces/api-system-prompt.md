## 18. API system prompt

Voice: role sentence, then tagged sections. No facts about one person.

Paste targets:
- System prompt: (Required) the top-level system field, never inside messages.
- Tool definitions: (Required when tools are used)
- Request settings: (Required) listed beside the prompt, not inside it.

```
You [role] for [REQUIRED: product and users].

<reference>
[Long documents first.]
</reference>

<rules>
- [Rule with its reason.]
</rules>

<tools>
- [tool_name]: use when [condition]. Do not use when [condition].
</tools>

<output_format>
[Format. For JSON use structured outputs instead of prose rules.]
</output_format>
```

Request settings:

```
model: [model id]
max_tokens: [value with room for thinking]
output_config.effort: [level]
tool_choice: auto
```

Notes: forced tool use returns 400 on Opus 5.5, Fable 5.1 and Sonnet 5.5. See 05 and 07 for prefill, budget_tokens, structured outputs and sampling rules. Tool definitions read like an interface for a person: clear names, example use, edge cases, clear boundaries.
