## 6. Scheduled task

Read cowork-task.md first. This file adds to it.

Everything in Cowork task except the checkpoint, because no one is there to approve during a run. Plus these.

Paste targets:
- Task prompt: (Required) It must stand alone, because each run starts a new session.
- Schedule: (Required) frequency, day, time, time zone.
- Output location and name pattern: (Required)

Add to the task prompt:

```
<unattended_run>
This runs unattended. Do only reversible work. Write results to a new file named [pattern with date].
If an input is missing, stop and write a short note saying what was missing.
End each run with a summary of what was done and what needs me.
</unattended_run>
```

Notes: paid plans (V S50). Runs remotely by default, unless it needs local files or apps (V S17).
