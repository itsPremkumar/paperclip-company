---
name: cron-doctor
version: 2.0.0
description: Diagnose and fix cron job issues: missed runs, overlapping jobs, silent failures
tags: ["cron", "doctor", "diagnostics", "cli", "scheduler", "debug"]
---

# Cron Doctor v2 🚀

Diagnose and fix cron job issues: missed runs, overlapping jobs, silent failures

Zero dependencies (Python stdlib only). Works on Windows, macOS, Linux.

## ✨ What's New in v2

| Feature | Description |
|---------|-------------|
| Missed-run detection | Missed-run detection |
| Overlap detection | Overlap detection |
| Silent-failure alerts | Silent-failure alerts |
| Auto-fix suggestions | Auto-fix suggestions |
| Run history | Run history |
| JSON output | JSON output |

## Install

```bash
# Requires Python 3.8+. No pip install needed.
curl -O https://raw.githubusercontent.com/itsPremkumar/cron-doctor/main/cron_doctor.py

# Or copy the file anywhere — it's self-contained.
```

## Commands

| Command | Description |
|---------|-------------|
| `python cron_doctor.py diagnose` | Diagnose cron issues |
| `python cron_doctor.py list` | List cron jobs |
| `python cron_doctor.py fix <job>` | Attempt auto-fix |
| `python cron_doctor.py history <job>` | Show run history |
| `python cron_doctor.py self-test` | Run built-in tests |

## Features

- **Missed-run detection**
- **Overlap detection**
- **Silent-failure alerts**
- **Auto-fix suggestions**
- **Run history**
- **JSON output**

## Example

```bash
python cron_doctor.py self-test
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
        run: python cron_doctor.py self-test
```

## Why

Cron Doctor is built for agent-native workflows: zero dependencies, offline-first, CI-ready.
Part of the Hermes autonomous product stack (31 agent-native tools, all CI-tested).

## Support

Free + MIT. Sponsor if useful:
- GitHub Sponsors: https://github.com/sponsors/itsPremkumar
- Buy Me a Coffee: https://buymeacoffee.com/itsPremkumar

⭐ Star on [GitHub](https://github.com/itsPremkumar/cron-doctor)
