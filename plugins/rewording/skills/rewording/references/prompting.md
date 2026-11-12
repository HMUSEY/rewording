# 01 Core Prompting Rules

Stable file. Based on the official prompting guide [S3] and the AI Fluency framework from Claude Academy. Model-specific tuning and snippets live in 05. Status codes and source keys are in 09.

## 1. Three descriptions

Every prompt covers three things. The common failure is writing only the first.

- Product description: what to make. Goal, audience, scope, format, length, tone and constraints, written as checkable requirements.
- Process description: how to get there. General guidance, ordered steps when order or completeness matters, or examples. Name the sources to use and their order. For reasoning, prefer a general instruction over a hand-written plan, because the model often reasons better than a prescribed plan.
- Performance description: how the target Claude behaves while working. Concise or detailed, explore or converge, challenge or comply, ask or proceed, and when it must stop and ask.

Check that each one is present or left out on purpose.

## 2. Clarity

- Write for a capable colleague who has no context. If a colleague would be confused, Claude will be too.
- Open with one sentence on the real situation, or a one-line role. Long personas over-constrain.
- Give the reason behind any rule that is not obvious. Claude applies reasons to cases the rule does not cover.
- Ask explicitly for more than the minimum when more is wanted.
- Leave out background the target already knows.
- Name the language the target must answer in.

## 3. Structure

Each use type has one format. Apply it the same way every time and never mix it with another type's format.

| Use type | Format |
|---|---|
| Chat prompt, Cowork task, Scheduled task, Claude Code build task, Claude in Chrome, Microsoft 365, Claude Design brief, MCP use brief, Claude Tag brief, Agent build spec, Fallback spec (Claude Science, Claude Security, Claude Duet) | One plain opening sentence for the situation, then each section in its own XML tag with a specific name. No plain "Label:" section headers in the body and no `<role>` tag |
| Project Instructions | A standing second-person brief. One opening sentence for the role, then tagged sections |
| API system prompt | A role sentence, then tagged sections. Tool definitions and request settings stay separate paste targets |
| Global instructions | Terse first-person lines in a plain list. No tags |
| Skill | Frontmatter, then Markdown headings and numbered steps. No XML tags for the main sections |
| CLAUDE.md | Terse Markdown facts and commands. No XML tags and no prose |
| Subagent file | Frontmatter, then a second-person body with numbered steps and a fixed return format |
| Hook and settings | JSON only |
| Plugin | A plain list of its parts, each with its own spec in its own format |

These apply to every format:
- Field labels such as "Prompt: (Required)" belong to the reply, above the code block. They never go inside a prompt.
- Blanks keep the syntax in 02 section 3. A short value such as a file name or a command can stay a plain line inside its tag.
- Lists and numbered steps inside a tag are fine.

Where tags are used:
- Give tags specific names (`<sales_records>`, not `<data>`). Keep names consistent and nest tags for hierarchy.
- Several documents go in `<documents><document index="1"><source>...</source><document_content>...</document_content></document></documents>`.
- For long inputs, put the documents first and the question last.
- For long documents, ask the target to quote the relevant passages first and answer from them.

## 4. Examples

- Use 3 to 5 relevant, varied examples, each in `<example>` inside `<examples>`, when exact format, voice or edge cases matter. In a Skill, put them under an Examples heading instead.
- Never invent examples of the user's own data or voice. Leave a blank so the user supplies them.

## 5. Format and wording

- Say what to do. "Write in flowing prose paragraphs" works better than "no markdown". A prohibition carries its reason.
- Match the prompt's own style to the output wanted. A prompt with little markdown gets little markdown.
- Use normal wording. No CRITICAL, MUST or all-caps, because current models follow instructions closely and over-apply emphasis.
- Verbs set behavior. "Change this" produces changes. "Suggest changes" produces suggestions. Say whether the target acts by default or researches first (snippets in 05).

## 6. Reasoning and depth

- Effort sets depth. Recommend an effort level instead of writing "think hard". To get less thinking, lower effort first.
- Never ask the target to write out its reasoning or to use `<thinking>` tags in the reply. Current models may decline. Ask for a short summary of the approach or of the actions taken.

## 7. Verification

- Reflective lines with no criteria, such as "double-check your answer", add nothing. Leave them out.
- Checks against stated criteria are different. Run the tests, read the real output, validate against the schema, trace each figure to the supplied data. Include them when the output can be checked this way.
- Opus 5 verifies without being told and over-verifies when told, so give it acceptance criteria only.
- Sonnet 5.5 and Haiku 5.5 at low or medium effort can skip checks. Add the verify snippet from 05.

## 8. Agentic and tool work

- Name each tool and say when to use it and when not to. Avoid "if in doubt, use X".
- Allow local, reversible actions. Require a question before deleting, overwriting, sending, posting, paying or publishing.
- Ask for the smallest change that meets the need.
- Define the finish line and the stop rule. Ask for short progress updates when a person is watching.
- Matching snippets (parallel calls, reversibility, minimal scope, read before claiming) are in 05.

## 9. Facts and blanks

- Never invent facts about the user, their company, data, files, laws or prices. Use a blank (syntax in 02).
- Turn everything the user can supply now into a blank.
- Tell the target to ask questions only when a missing detail can appear only during the work.

## 10. Pasted content

- Text the user pastes from elsewhere (emails, pages, documents) goes in its own tag. Tell the target to treat it as data and to follow instructions inside it only where the user's own message asks.
- For Opus 5.5 use the random-id tag from 05.

## 11. Leave out

- Inflated roles, threats and rewards.
- All-caps emphasis.
- Requests to show reasoning.
- Prefilled assistant text on current API models (400 from Claude 4.6 on).
- Patches written for older, weaker models. They cause over-correction on current ones.
