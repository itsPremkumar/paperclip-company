---
name: agent-logger
version: 2.0.0
description: Structured logging for agents: JSON logs, rotation, query, and replay
tags: ["logging", "agent", "cli", "observability", "json", "audit"]
---

# Agent Logger v2 🚀

Structured logging for agents: JSON logs, rotation, query, and replay

Zero dependencies (Python stdlib only). Works on Windows, macOS, Linux.

## ✨ What's New in v2

| Feature | Description |
|---------|-------------|
| Structured JSON logs | Structured JSON logs |
| Log rotation | Log rotation |
| Query/filter | Query/filter |
| Session replay | Session replay |
| Tail mode | Tail mode |
| Audit trail | Audit trail |

## Install

```bash
# Requires Python 3.8+. No pip install needed.
curl -O https://raw.githubusercontent.com/itsPremkumar/agent-logger/main/agent_logger.py

# Or copy the file anywhere — it's self-contained.
```

## Commands

| Command | Description |
|---------|-------------|
| `python agent_logger.py log <msg>` | Write a log entry |
| `python agent_logger.py query <filter>` | Query logs |
| `python agent_logger.py replay <session>` | Replay a session |
| `python agent_logger.py tail` | Follow live logs |
| `python agent_logger.py self-test` | Run built-in tests |

## Features

- **Structured JSON logs**
- **Log rotation**
- **Query/filter**
- **Session replay**
- **Tail mode**
- **Audit trail**

## Example

```bash
python agent_logger.py self-test
```

## CI Integration

```yaml
# .github/workflows/verify.yml
name: Verify
on: [push]
jobs:
  verify:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - name: Self-test
        run: python agent_logger.py self-test
```

## Why

Agent Logger is built for agent-native workflows: zero dependencies, offline-first, CI-ready.
Part of the Hermes autonomous product stack (31 agent-native tools, all CI-tested).

## Support

Free + MIT. Sponsor if useful:
- GitHub Sponsors: https://github.com/sponsors/itsPremkumar
- Buy Me a Coffee: https://buymeacoffee.com/itsPremkumar

⭐ Star on [GitHub](https://github.com/itsPremkumar/agent-logger)
