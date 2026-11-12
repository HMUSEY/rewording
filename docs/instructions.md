# Rewording: requirements as concepts

One system the owner controls. It researches, decides and produces professional, correctly formatted prompts for every Claude surface the owner uses.

## Ownership

- No browser extension, no external SaaS, no third-party rewriting service, no telemetry, no hidden calls.
- Allowed: Claude-native mechanisms, local scripts the owner runs, and the owner's own API key.

## Activation

- It runs only when the owner asks. It never runs in the background and never on other messages.
- Claude Code: the skill is manual-only and the hook fires only on the /rewording command.
- claude.ai: manual-only is a wording guarantee, not a technical one.

## What it does on each request

1. Rewrite the request to the form the target surface needs and say why in one line.
2. Choose the cheapest mechanism that does the job and justify it.
3. Warn before execution about token burn and limits, with do and avoid lines.
4. Say what to toggle (memory, search, fresh thread, Project memory) and the trade-off.
5. Enrich with research only when the owner asks for depth or context is clearly missing, and state the reason.
6. Send follow-up work to the same Project thread.
7. Before execution say what the owner missed, what to correct, and, for build requests, whether an open-source project already does it.
8. For anything irreversible, present options and let the owner decide.

## Output

- Prompt text, never the task result.
- Prompts and specs in English. Everything addressed to the owner in Arabic with Western digits.
- Reply order: goal, prompt, settings, before execution, fill-in table, verification.

## Facts

- Product facts come only from rows marked V or T in references/sources.md. U rows are never stated.
- tools/maintain.py compares the official pages against a local snapshot so stale rows are found.

## Local scripts

- rewording-guard/scripts/precheck.py check: local token estimate, secret scan and flags. No network.
- precheck.py hook: runs the same check when the owner types /rewording and blocks if a secret is present.
- tools/rw_api.py count and build: call the API with the owner's key, only when the owner runs them.

## Not in version 1

- Executing the rewritten prompt.
- Any scheduled or background run.
