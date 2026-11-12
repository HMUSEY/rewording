# Rewording

Turns a raw request, in Arabic or English, into a ready prompt for the right Claude surface. The reply names the surface, gives the prompt, the model and effort to pick, the settings to switch, what the request is missing, and a token warning when the request is heavy. It writes the prompt only and never does the task itself.

## Use it

Type `/` in a chat, pick rewording, then write your request. In Claude Code type `/rewording:rewording` followed by the request.

## Data

The plugin holds only Markdown files. It sends nothing anywhere and stores nothing. In Claude Code the optional rewording-guard plugin adds a local check for size and secrets before the request reaches the model.

## Install

```
/plugin install rewording --marketplace HMUSEY/rewording
```
