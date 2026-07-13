---
name: agent-health
version: 2.0.0
description: Monitor agent endpoints, check liveness, collect metrics, alert on failures
tags: ["health", "monitor", "agent", "cli", "observability", "alerts"]
---

# Agent Health Monitor v2 🚀

Monitor agent endpoints, check liveness, collect metrics, alert on failures

Zero dependencies (Python stdlib only). Works on Windows, macOS, Linux.

## ✨ What's New in v2

| Feature | Description |
|---------|-------------|
| Endpoint liveness checks | Endpoint liveness checks |
| Metric collection | Metric collection |
| Failure alerting | Failure alerting |
| Watch mode | Watch mode |
| JSON output | JSON output |
| Multi-agent support | Multi-agent support |

## Install

```bash
# Requires Python 3.8+. No pip install needed.
curl -O https://raw.githubusercontent.com/itsPremkumar/agent-health/main/agent_health.py

# Or copy the file anywhere — it's self-contained.
```

## Commands

| Command | Description |
|---------|-------------|
| `python agent_health.py check <endpoint>` | Health check an agent |
| `python agent_health.py metrics <agent>` | Collect metrics |
| `python agent_health.py watch <agent>` | Continuous monitoring |
| `python agent_health.py alerts` | Show active alerts |
| `python agent_health.py self-test` | Run built-in tests |

## Features

- **Endpoint liveness checks**
- **Metric collection**
- **Failure alerting**
- **Watch mode**
- **JSON output**
- **Multi-agent support**

## Example

```bash
python agent_health.py self-test
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
        run: python agent_health.py self-test
```

## Why

Agent Health Monitor is built for agent-native workflows: zero dependencies, offline-first, CI-ready.
Part of the Hermes autonomous product stack (31 agent-native tools, all CI-tested).

## Support

Free + MIT. Sponsor if useful:
- GitHub Sponsors: https://github.com/sponsors/itsPremkumar
- Buy Me a Coffee: https://buymeacoffee.com/itsPremkumar

⭐ Star on [GitHub](https://github.com/itsPremkumar/agent-health)
