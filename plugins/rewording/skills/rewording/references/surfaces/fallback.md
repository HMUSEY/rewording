## 20. Claude Science, Claude Security and Claude Duet

- Claude Science: paid plans, a research tool, not for clinical use (V S50, S26). Use the Fallback spec with the research playbook.
- Claude Security: Enterprise only, beta (V S50). Use the Fallback spec with the coding playbook.
- Claude Duet: research preview on Pro, Max and Ultra with a waitlist (T S28). You message it like a person. It works in connected apps, runs on Opus 5.5 with no model choice, checks in at set intervals and asks before sending messages, paying, signing documents or deleting (V S28). Use the Fallback spec with the agentic playbook and say access is limited.

## 21. Fallback spec

For any surface without a section here. Voice: one plain opening sentence for the situation, then tagged sections.

Paste targets: each labeled as in 02 section 2, using the product's real field names when the docs give them, otherwise `Prompt: (Required)`.

```
[One sentence: the situation and what I need.]

<deliverable>
[What comes out.]
</deliverable>

<inputs>
[What the product can access and what the user supplies.]
</inputs>

<process>
1. [Step]
2. [Step]
</process>

<boundaries>
[What needs approval, what is reversible, what never happens.]
</boundaries>

<done_when>
[Success criteria and checks.]
</done_when>

<output>
[Format and where it lands.]
</output>
```

Check the official docs first when search is allowed (SKILL.md, Facts). Mark assumed facts. Put a registry entry from the template in sources.md in the notes.
