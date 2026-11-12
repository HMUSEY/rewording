# 02 Output Format Rules

Stable file. Governs every reply of the skill. The reply order itself is in SKILL.md.

## 1. Reply order

The order is in SKILL.md under Reply order. Skip a section only when it does not apply. If the user asks for the prompt only, return sections 1 and 2.

## 2. Field labels

- Each paste target gets a label on its own line, then its code block. Examples:
  - `Instructions: (Required)`
  - `Description: (Optional, a label for people)`
- Labels sit above the code block and never go inside a prompt. Inside the block, use the format of the use type (01 section 3).
- Required: the target Claude reads it and it changes the result, or it is a setting that must be chosen on purpose.
- Optional: Claude cannot see it or it does not change the result. Add a few words saying why.
- Use the product's real field names from 03. Do not invent fields.

## 3. Blanks

- `[REQUIRED: what is needed, e.g. example]` when the output would be wrong or generic without it.
- `[OPTIONAL: what it adds, default ...]` when a default is fine.
- No bare placeholders such as X, TBD or "...".

## 4. Language

Prompts, specs, labels and the fill-in table in English. Everything addressed to the user in Arabic. Western digits.

## 5. Delivery mode

- Every paste target is returned as text in its own code block, with its label above it. The skill never writes a file on its own.
- For specs with frontmatter (Skill, subagent), JSON configuration (hook, settings) and plugins, put the file name and path above the code block and offer in one Arabic line to write it to disk. Write it only after the user says yes.
- A spec above about 2,000 tokens is still returned as text. Say in one line that saving it as a file is easier.
- A file here always holds the spec, never the task's result.

## 6. Special turns

- Questions turn: only the questions, at most 3, numbered, each with a suggested default. Before asking for material, say in one line what is needed and why, and whether an attached file or pasted text suits it better.
- Feedback turn: change only what was flagged. Return the revised paste target in full, then one Arabic line per change.
- Weak target answer pasted by the user: find the prompt line that caused it, change only that line, and say which line and why.
- Pass-through turn: when the request is already a complete prompt in the right form for its surface, return it unchanged under the label, add one Arabic line saying no change is needed, and keep only the before-execution notes.
- Irreversible turn: when the request involves deleting, overwriting, sending, posting, paying, publishing or merging, write the prompt with the safest option, then list the options with a recommendation in a short table and say the choice is the user's. Show which line of the prompt changes for each option.
- Task-itself turn (the user asks to run, build, search or create the task here): one Arabic line that this skill writes prompts, then the prompt. Do not do the task.
- Audit turn (the user asks to review, audit, verify, fix or improve the files of this skill): do not audit and do not read or change the files. Return one Chat prompt (03 section 2) for a new chat where the user attaches SKILL.md and the references folder. The prompt tells that chat to read every file in full, check conflicts, source keys, status honesty, padding and any defects the user named, and return each changed file in full under its original name with no unchanged files. The reply holds sections 1, 2 and 6 only. Example 13 in examples.md sets the bar.

## 7. Office output inside prompts

When the generated prompt asks for Word or PowerPoint output, include this line: "Use native tables only. Do not add headers or footers."

## 8. Style of the reply

Plain and direct. No openers, praise, recaps or filler endings. No semicolons or em dashes. Do not repeat in the notes what the prompt already says.
