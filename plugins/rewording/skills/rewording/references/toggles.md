# Toggles

Tell the user what to switch and the trade-off. Menu locations change, so name the control and let the user find it. Locations are T (S47, S57).

| Toggle | Use it when | Trade-off |
|---|---|---|
| Account memory off, per project ("Use account memory" in the project's Memory section) | client, team or sensitive work | the project's memory stays separate, personal context does not enter (V S47) |
| Memory off for one chat ("+" menu, then Memory) | one clean focused chat | applies to that chat only (V S47) |
| Search and reference chats off | past chats must not leak into this task | Claude cannot pull earlier work |
| Incognito chat | a one-off sensitive topic | not saved, and reported as unavailable inside Projects (T S63) |
| Web search on | facts may be newer than June 2026, or cited sources are wanted | more tokens and time. Keep it off when every fact comes from the user |
| Research on | multi-source cited work | much heavier usage. Paid plans only (V S50) |
| Effort higher | a measured quality gain on hard work | cost. Lower effort first to get less thinking (V S44) |
| Code execution and file creation on | the task creates files, or a skill runs scripts | required for Skills in claude.ai (V S15, S48) |
| Fresh thread or session | context is stale, the topic changed, or two corrections failed | earlier context is lost, so carry the decisions in Project knowledge or a short summary |
| Follow-ups inside the same Project | the same work continues | classic Projects share only instructions and knowledge. The new Projects beta threads also share memory (T S18) |
| Project knowledge instead of re-pasting | the same reference is used again | retrieval mode may apply near the context limit (V S46) |
| Subagent in Claude Code | noisy exploration or large reads | separate context and a summary back, at its own token cost |
| Prompt caching on the API | a long fixed system prompt reused within minutes | the first write costs more, later reads cost far less (T S60) |
| /clear or /compact in Claude Code | /clear between unrelated tasks, /compact to keep going | /clear is U on an official page |
