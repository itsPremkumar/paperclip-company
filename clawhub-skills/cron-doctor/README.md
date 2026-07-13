# Cron Doctor 🚀

[![Python 3.8+](https://img.shields.io/badge/python-3.8%2B-blue.svg)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)
![cron](https://img.shields.io/badge/tag-cron-blue) ![doctor](https://img.shields.io/badge/tag-doctor-blue) ![diagnostics](https://img.shields.io/badge/tag-diagnostics-blue) ![cli](https://img.shields.io/badge/tag-cli-blue) ![scheduler](https://img.shields.io/badge/tag-scheduler-blue) ![debug](https://img.shields.io/badge/tag-debug-blue)

Diagnose and fix cron job issues: missed runs, overlapping jobs, silent failures

Zero dependencies (Python stdlib only). Works on Windows, macOS, Linux.

## ✨ Features

- Missed-run detection
- Overlap detection
- Silent-failure alerts
- Auto-fix suggestions
- Run history
- JSON output

## Commands

| Command | Description |
|---------|-------------|
| `diagnose` | Diagnose cron issues |
| `list` | List cron jobs |
| `fix <job>` | Attempt auto-fix |
| `history <job>` | Show run history |
| `self-test` | Run built-in tests |

## Quick Start

```bash
# Download (no pip needed)
curl -O https://raw.githubusercontent.com/itsPremkumar/cron-doctor/main/cron_doctor.py

# Run
python cron_doctor.py self-test
```

## Why Cron Doctor?

- **Zero deps** — runs in any Python 3.8+ environment
- **Offline-first** — no telemetry, no uploads, fully private
- **CI-ready** — JSON output + self-tests for pipelines
- **Cross-platform** — identical output on Windows/macOS/Linux

---

📦 Also on [ClawHub](https://clawhub.ai/skills/skills/cron-doctor)  
⭐ Star on [GitHub](https://github.com/itsPremkumar/cron-doctor)  
☕ [Buy Me a Coffee](https://buymeacoffee.com/itsPremkumar)
