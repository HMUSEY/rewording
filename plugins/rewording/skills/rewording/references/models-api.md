# 05 Models: table, apps and API rules

Volatile file. V = verified (date and source key). T = in transition. U = unverified, never stated as fact. Keys are in 09.

Selection, effort and tuning: models.md.

## 1. Current models (API)

| Model | API ID | $/MTok in/out | Context | Max output | Thinking | Default effort | Cutoff | Status |
|---|---|---|---|---|---|---|---|---|
| Fable 5.1 | claude-fable-5-1 | 10 / 50 | 1M | 128K | Adaptive, always on | high | Jun 2026 | V 2026-11-07 S41 |
| Opus 5.5 | claude-opus-5-5 | 4 / 20 | 1M | 128K | Adaptive, always on | medium | Jun 2026 | V 2026-11-07 S5 |
| Sonnet 5.5 | claude-sonnet-5-5 | 2 / 10 | 1M | 128K | Adaptive, lowest setting between_tools | high | Jun 2026 | V 2026-11-07 S1 |
| Haiku 5.5 | claude-haiku-5-5 | 0.10 / 0.50 up to 100K prompt tokens, 0.50 / 2.50 above | 1M | 128K | Adaptive, can be disabled at high or below | medium | Jun 2026 | V 2026-11-07 S35, S50 |
| Opus 5 | claude-opus-5 | 5 / 25 | U | U | Adaptive, can be disabled at high or below | high | U | V Legacy S50 |

- Mythos 5.1: same specs and price as Fable 5.1, only for organizations verified through Anthropic programs such as the Cyber Verification Program. Do not recommend it (V S41).
- Opus 5.5 fast mode: `speed: "fast"` at 8 / 40 $/MTok, API and Claude Code (V S5).
- Prompt caching minimum: 512 tokens on Opus 5.5 and Haiku 5.5. Other models U (V S5, S43).

## 3. In the Claude apps

| Model | Free | Pro | Max, Ultra | Team | Status |
|---|---|---|---|---|---|
| Haiku 5.5, Sonnet 5.5 | Yes | Yes | Yes | Yes | V S50 |
| Opus 5.5 | No | Yes | Yes | Yes | V S50 |
| Fable 5 and 5.1 | No | Usage credits from the first request | Up to 50% of weekly limits, then credits | Premium seats. Standard seats use credits | V S38, S50 |

- Choose the model in the model selector. The apps have an effort control for the 5.x models, and thinking cannot be turned off there (V S45). Effort advice applies in the apps too.

## 5. Thinking and API rules

| Rule | Status |
|---|---|
| budget_tokens returns 400 on Claude 4.7 and later | V S4 |
| Prefill on the last assistant turn returns 400 from Claude 4.6 on | V S3 |
| Fable 5.1 and Opus 5.5 reject thinking "enabled" and "disabled" with 400 | V S4 |
| Sonnet 5.5 accepts between_tools at high or below. "disabled" returns 400 at every effort | V S4 |
| Haiku 5.5 and Opus 5 can disable thinking only at high or below | V S4 |
| Forced tool use (tool_choice any or tool) returns 400 on Opus 5.5, Fable 5.1 and Sonnet 5.5. Use auto with strict tools, or structured outputs | V S5, S41, S42 |
| Forced tool use on Haiku 5.5 appears supported (pricing lists its token cost) | T S54 |
| Opus 5.5 on API accounts created from August 31, 2026: replaying a thinking block after the prefix changed returns 400 unless prefix_mismatch_behavior is set | V S5 |
| Haiku 5.5: omit temperature, top_p and top_k | V S43 |
| Requests for written reasoning may be declined (reasoning_extraction) | V S44 |
