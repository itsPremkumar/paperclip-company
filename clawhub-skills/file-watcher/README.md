# File Watcher 🚀

[![Python 3.8+](https://img.shields.io/badge/python-3.8%2B-blue.svg)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)
![file](https://img.shields.io/badge/tag-file-blue) ![watch](https://img.shields.io/badge/tag-watch-blue) ![monitor](https://img.shields.io/badge/tag-monitor-blue) ![diff](https://img.shields.io/badge/tag-diff-blue) ![cli](https://img.shields.io/badge/tag-cli-blue) ![automation](https://img.shields.io/badge/tag-automation-blue)

Monitor directories for changes: snapshots, diffs, glob filtering, event detection

Zero dependencies (Python stdlib only). Works on Windows, macOS, Linux.

## ✨ Features

- Snapshot capture
- Hash/MD5 tracking
- Glob filtering
- Create/delete/modify detection
- Diff between snapshots
- Watch mode

## Commands

| Command | Description |
|---------|-------------|
| `once <dir>` | Take a snapshot |
| `once <dir> --output FILE` | Save snapshot to file |
| `diff <a> <b>` | Diff two snapshots |
| `watch <dir>` | Watch for changes (long-running) |
| `--glob PATTERN` | Filter by glob |
| `self-test` | Run built-in tests |

## Quick Start

```bash
# Download (no pip needed)
curl -O https://raw.githubusercontent.com/itsPremkumar/file-watcher/main/file_watcher.py

# Run
python file_watcher.py self-test
```

## Why File Watcher?

- **Zero deps** — runs in any Python 3.8+ environment
- **Offline-first** — no telemetry, no uploads, fully private
- **CI-ready** — JSON output + self-tests for pipelines
- **Cross-platform** — identical output on Windows/macOS/Linux

---

📦 Also on [ClawHub](https://clawhub.ai/skills/skills/file-watcher)  
⭐ Star on [GitHub](https://github.com/itsPremkumar/file-watcher)  
☕ [Buy Me a Coffee](https://buymeacoffee.com/itsPremkumar)
