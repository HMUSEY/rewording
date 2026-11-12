# 05 Models: selection, effort and tuning

Volatile file. V = verified (date and source key). T = in transition. U = unverified, never stated as fact. Keys are in 09.

Table of models, prices, app access and API rules: models-api.md.

## 2. Selection (V S1)

- Start with Opus 5.5 for most work.
- Fable 5.1 for demanding reasoning and long-horizon agentic work, or when Opus 5.5 at higher effort still falls short.
- Sonnet 5.5 for speed with quality on everyday coding, agent and business work.
- Haiku 5.5 for classification, extraction, routing, subagents and high volume.
- Older models only when the user names them.

## 4. Effort (V S2, S45)

- Levels: low, medium, high, xhigh, max on all four current models.
- low and medium: routine tasks, fast and cheap, subagents.
- high: the best overall balance for complex reasoning, hard coding and knowledge work.
- xhigh: long-running coding and agentic tasks.
- max: the deepest reasoning, with a risk of overthinking.
- Use xhigh and max only where a quality gain was measured (V S44).
- To get less thinking, lower effort first. Instructions work less reliably (V S44).
- Sonnet 5.5: medium for well-specified agentic work and chat, high for harder work.
- Haiku 5.5: low for chat and volume, high for knowledge work and longer agent tasks.
- Fable 5.1: high by default, xhigh or max for the most demanding work.
- max_tokens caps thinking plus text. At high and above, set it large. 128,000 works well for long agentic turns (V S44).

## 6. Prompt tuning per model

- Fable 5.1: it writes fewer user-facing updates, so ask for progress updates in long tool turns and remove "keep it brief" rules about them. It already formats less, so drop old anti-markdown blocks. State the length. When current facts matter, tell it to search (V S3, S41).
- Opus 5.5: remove "think carefully" from chat prompts, because replies start sooner with no clear quality loss. On multi-app work, tell it to explore all relevant sources before acting. Use the unattended snippet only for fully unattended agents. Mark pasted text with the random-id tag. Name frontend patterns to avoid. Its progress updates arrive as thinking blocks, which stay empty in the API unless display "updates" is set (07) (V S44).
- Sonnet 5.5: add the keep-working snippet at low or medium on long tasks, the finish-and-stop snippet to prevent extras, the no-extra-review snippet at xhigh or max, the search snippet for current facts, the verify snippet at low effort.
- Haiku 5.5: give today's date and a short search nudge, without blanket "search everything" rules. Add the no-early-stop snippet in long agent prompts, the verify snippet for code at low or medium, and the chatbot rules line.
- Opus 5: ask for concise replies explicitly. It verifies without being told and over-verifies when told, so skip verification instructions. Say when subagents are and are not warranted.
