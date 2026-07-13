---
name: company-ops
version: 2.0.0
description: Operate the autonomous AI company: 24/7 cron loop, task management, revenue tracking
tags: ["company", "ops", "autonomous", "cron", "automation", "ai"]
---

# Company Ops v2 🚀

Operate the autonomous AI company: 24/7 cron loop, task management, revenue tracking

Zero dependencies (Python stdlib only). Works on Windows, macOS, Linux.

## ✨ What's New in v2

| Feature | Description |
|---------|-------------|
| 24/7 autonomy loop | 24/7 autonomy loop |
| Task queue management | Task queue management |
| Revenue channel tracking | Revenue channel tracking |
| Constitution-as-OS | Constitution-as-OS |
| GitHub source of truth | GitHub source of truth |
| Human-in-the-loop gates | Human-in-the-loop gates |

## Install

```bash
# Requires Python 3.8+. No pip install needed.
curl -O https://raw.githubusercontent.com/itsPremkumar/company-ops/main/autonomy-loop.py

# Or copy the file anywhere — it's self-contained.
```

## Commands

| Command | Description |
|---------|-------------|
| `python autonomy-loop.py loop` | Run autonomy loop tick |
| `python autonomy-loop.py tasks` | List pending tasks |
| `python autonomy-loop.py revenue` | Show revenue dashboard |
| `python autonomy-loop.py status` | Company status report |

## Features

- **24/7 autonomy loop**
- **Task queue management**
- **Revenue channel tracking**
- **Constitution-as-OS**
- **GitHub source of truth**
- **Human-in-the-loop gates**

## Example

```bash
python autonomy-loop.py self-test
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
        run: python autonomy-loop.py self-test
```

## Why

Company Ops is built for agent-native workflows: zero dependencies, offline-first, CI-ready.
Part of the Hermes autonomous product stack (31 agent-native tools, all CI-tested).

## Support

Free + MIT. Sponsor if useful:
- GitHub Sponsors: https://github.com/sponsors/itsPremkumar
- Buy Me a Coffee: https://buymeacoffee.com/itsPremkumar

⭐ Star on [GitHub](https://github.com/itsPremkumar/company-ops)
