---
name: agent-cost-tracker
version: 2.0.0
description: Track LLM API spending per agent/session with budget alerts and CSV export
tags: ["cost", "tracking", "llm", "budget", "cli", "finance"]
---

# Agent Cost Tracker v2 🚀

Track LLM API spending per agent/session with budget alerts and CSV export

Zero dependencies (Python stdlib only). Works on Windows, macOS, Linux.

## ✨ What's New in v2

| Feature | Description |
|---------|-------------|
| Per-agent cost tracking | Per-agent cost tracking |
| Session-level attribution | Session-level attribution |
| Budget alerts | Budget alerts |
| CSV export | CSV export |
| Daily/weekly rollups | Daily/weekly rollups |
| JSON output | JSON output |

## Install

```bash
# Requires Python 3.8+. No pip install needed.
curl -O https://raw.githubusercontent.com/itsPremkumar/agent-cost-tracker/main/agent_cost_tracker.py

# Or copy the file anywhere — it's self-contained.
```

## Commands

| Command | Description |
|---------|-------------|
| `python agent_cost_tracker.py track <agent> <cost>` | Log a cost event |
| `python agent_cost_tracker.py report` | Generate cost report |
| `python agent_cost_tracker.py budget <agent> <limit>` | Set budget |
| `python agent_cost_tracker.py alerts` | Show budget alerts |
| `python agent_cost_tracker.py export` | Export to CSV |
| `python agent_cost_tracker.py self-test` | Run built-in tests |

## Features

- **Per-agent cost tracking**
- **Session-level attribution**
- **Budget alerts**
- **CSV export**
- **Daily/weekly rollups**
- **JSON output**

## Example

```bash
python agent_cost_tracker.py self-test
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
        run: python agent_cost_tracker.py self-test
```

## Why

Agent Cost Tracker is built for agent-native workflows: zero dependencies, offline-first, CI-ready.
Part of the Hermes autonomous product stack (31 agent-native tools, all CI-tested).

## Support

Free + MIT. Sponsor if useful:
- GitHub Sponsors: https://github.com/sponsors/itsPremkumar
- Buy Me a Coffee: https://buymeacoffee.com/itsPremkumar

⭐ Star on [GitHub](https://github.com/itsPremkumar/agent-cost-tracker)
