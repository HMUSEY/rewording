# Rewording Guard

Claude Code add-on for the rewording plugin. When you type /rewording:rewording, a local Python script reads only that request, estimates its size in tokens, flags deletes, publishing and requests for recent facts, and blocks the request if it holds an API key, password, card number or IBAN. It runs nowhere else, makes no network calls and calls no model. Requires Python 3.

## Install

```
/plugin install rewording-guard --marketplace HMUSEY/rewording
```
