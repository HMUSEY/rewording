# 04 Task Playbooks, Patterns and Checks

Stable file. Playbooks set what the body of a prompt contains, whatever the surface. The format of that body comes from 01 section 3. Baseline always applies. Enrichment applies only when enrichment is on. Watch lists known failures.

## 1. Playbooks

### Writing and communication (emails, proposals, reports, posts, speeches)
- Baseline: the situation, facts as blanks (names, numbers, dates), audience, language, tone, length, one clear purpose or ask, output format, a sample of the user's voice when voice matters.
- Enrichment: two angles then a pick, a critique-and-revise pass against stated criteria, the reader's likely objections, alternate lengths.
- Watch: invented facts and generic voice. State the length, because default length varies by model.

### Editing and rewriting
- Baseline: the text in its own tag, what to change and what to keep, the level (proofread, light, heavy), whether to return only the revised text. Use "change", not "suggest".
- Enrichment: a short list of the main changes, a tighter and a fuller version.
- Watch: the language of the text decides the language of the answer.

### Research
- Baseline: the question, what a good answer contains, scope (dates, regions, source types), whether facts newer than June 2026 are needed, cited output, what to do when sources conflict (report both) or nothing is found (say so).
- Enrichment: competing hypotheses, confidence per claim, cross-checks across sources, a self-critique pass against the stated criteria, what would change the conclusion.
- Watch: turn on web search or Research when facts may be recent. Tell the target to search, and give a model with a search tool today's date.

### Analysis and data
- Baseline: the data in its own tag, the question, assumptions to state, units and rounding, output form, every figure traceable to the supplied data, "not provided" for anything missing.
- Enrichment: a data quality check first, sensitivity cases, alternative explanations, a reconciliation check, an executive summary with the working in an appendix.
- Watch: invented figures. Prefer running code when a code tool exists.

### Planning and strategy
- Baseline: objective, constraints (time, cost, people, standards), horizon, the decision to be made, plan format, what good looks like.
- Enrichment: assumptions, risks with mitigations, base, best and worst cases, weighted criteria, milestones with owners and dates as blanks, stop criteria, a faster and a more thorough path.
- Watch: over-planning. Match the standard to the size of the project.

### Brainstorming and creative work
- Baseline: purpose, audience, constraints, number of ideas, what makes an idea good, overused patterns to avoid named specifically.
- Enrichment: a long list then a shortlist against criteria, angles borrowed from other fields, one deliberately unusual idea.
- Watch: performance should explore first, not converge early.

### Learning and explanation
- Baseline: topic, what the learner knows, goal, format (analogy, steps, worked example), depth.
- Enrichment: simple to complex order, common misconceptions, practice questions with answers held back, a short understanding check.
- Watch: tell the target to check understanding and to say when an assumption is wrong.

### Long documents
- Baseline: documents first in tags with sources, task last, quote the relevant passages first, answer only from the documents, cite the source, "not in the documents" when missing.
- Enrichment: a map pass then a synthesis pass, a contradiction check between documents, confidence flags.

### Extraction, classification, structured output
- Baseline: the schema, each field's definition and allowed values, the value for missing data, 3 to 5 examples with edge cases, structured outputs where the product offers them.
- Enrichment: a confidence field, a validation step, edge cases to flag.
- Watch: Haiku 5.5 suits high volume. For JSON on reasoning tasks with Sonnet 5.5, use the snippet in 05.

### Coding
- Baseline: outcome in one sentence, stack, files and patterns, constraints, runnable acceptance checks and an instruction to run them and read the output. A general solution for all valid inputs, not one tuned to the tests. Read the code before making claims about it.
- Enrichment: tests first, a security review against named vulnerability classes, edge cases, a rollback plan, a performance budget.
- Watch: over-engineering. State "only what was asked" when scope matters.

### Agentic and automation work
- Baseline: deliverable, inputs, boundaries, ask-before-acting rules, checkpoints, success criteria, Plan-Validate-Execute for batches, obstacle reporting.
- Enrichment: state files (progress notes, task list), a time budget, a final self-critique against the success criteria, subagents only for parallel or isolated work.
- Watch: unattended runs that end early (snippet in 05), context limits on long runs (save state to files), silent stretches (ask for progress updates).

### Health, legal and financial administration
- Baseline: keep the prompt to information, organization and drafting. Add one line telling the target to recommend a qualified professional for decisions.
- When the output feeds decisions about people in legal, health, financial, housing, employment or similar matters, tell the target that a qualified person reviews the result and that affected people are told AI was used, because the Usage Policy requires it for high-risk uses (V S49).
- Watch: no diagnosis, legal opinion or investment advice framed as final.

## 2. Workflow patterns

Start with the simplest that works.

| Pattern | Use when | Surface |
|---|---|---|
| Prompt chaining | Fixed stages with a check between them | Chat steps, Cowork, API |
| Routing | Inputs fall into distinct categories | API, Skills |
| Parallelization | Independent subtasks, or several runs for confidence | Subagents, API |
| Orchestrator-workers | Subtasks cannot be known in advance | Claude Code, Agent build |
| Evaluator-optimizer | Clear criteria and gains from iteration | API, Claude Code |
| Advisor | A cheaper executor needs occasional stronger guidance | API advisor tool (beta) |

Predictable step-by-step tasks get fixed steps, not an autonomous agent.

## 3. Checks bank

Pick 2 per prompt and make them specific to the task.

| Task | Good result | Bad result |
|---|---|---|
| Writing | Requested voice, length and language, one clear ask | Generic phrasing, filler openers, invented facts |
| Research | Cited claims, stated confidence, conflicts noted | Uncited claims, one source for a key fact |
| Analysis | Every figure traceable, assumptions stated | Round numbers with no source |
| Code | Runs, passes the stated tests, handles bad input | Works only on the happy path, secrets in code |
| Agent or file task | Stops at the boundaries, reports what changed | Acts outside the given folders or sites, silent changes |
| Setup spec | Every Required field filled, clear triggers | Vague description, rules in fields Claude cannot see |
| Structured output | Validates against the schema, missing values handled | Free text where JSON was asked |
| Design | Stated sizes, audience and character, named patterns avoided | Generic look, wrong sizes, crowded text |
| File audit | Every change quotes its defect, only changed files returned in full | Rewritten style, unchanged files returned, dropped lines |

Before use or sharing, the user verifies: facts, numbers, names, anything sent outside, and any product detail marked U or T.
