## 10. Claude Code build

Voice: outcome plus a way to verify it, pointing at real files. One plain opening sentence with the outcome, then tagged sections. Outcome and constraints, not micro-steps.

Paste targets:
- Task prompt: (Required)
- CLAUDE.md: (Optional, for rules that repeat)
- Hook: (Optional, for actions that must run every time)

```
[Outcome in one sentence.]

<stack_and_constraints>
[REQUIRED: language, framework, versions]
</stack_and_constraints>

<files_and_patterns>
[OPTIONAL: paths to follow, default: read the repository first]
</files_and_patterns>

<scope>
Only [paths]. Make only the changes needed. No new dependencies unless asked.
</scope>

<security>
Validate all input on the server, no hardcoded secrets, secure defaults, current OWASP practices.
</security>

<done_when>
These pass. Run them and read the output.
1. [Check]
2. [Check]
</done_when>

<sequence>
Explore in plan mode without changes, write a plan and wait for my approval, implement against the plan, run the checks, commit.
</sequence>

<ask_before>
Deleting files, migrations, force pushes, anything outside scope.
</ask_before>
```

Notes: skip plan mode when the change fits in one sentence (T S58). Start a fresh session between unrelated tasks. After two failed corrections, start fresh and rewrite the first prompt with what was learned. For a long goal that should keep going until done, /goal exists (V S52).
