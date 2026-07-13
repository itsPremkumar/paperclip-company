---
name: file-watcher
version: 2.0.0
description: Monitor directories for changes: snapshots, diffs, glob filtering, event detection
tags: ["file", "watch", "monitor", "diff", "cli", "automation"]
---

# File Watcher v2 🚀

Monitor directories for changes: snapshots, diffs, glob filtering, event detection

Zero dependencies (Python stdlib only). Works on Windows, macOS, Linux.

## ✨ What's New in v2

| Feature | Description |
|---------|-------------|
| Snapshot capture | Snapshot capture |
| Hash/MD5 tracking | Hash/MD5 tracking |
| Glob filtering | Glob filtering |
| Create/delete/modify detection | Create/delete/modify detection |
| Diff between snapshots | Diff between snapshots |
| Watch mode | Watch mode |

## Install

```bash
# Requires Python 3.8+. No pip install needed.
curl -O https://raw.githubusercontent.com/itsPremkumar/file-watcher/main/file_watcher.py

# Or copy the file anywhere — it's self-contained.
```

## Commands

| Command | Description |
|---------|-------------|
| `python file_watcher.py once <dir>` | Take a snapshot |
| `python file_watcher.py once <dir> --output FILE` | Save snapshot to file |
| `python file_watcher.py diff <a> <b>` | Diff two snapshots |
| `python file_watcher.py watch <dir>` | Watch for changes (long-running) |
| `python file_watcher.py --glob PATTERN` | Filter by glob |
| `python file_watcher.py self-test` | Run built-in tests |

## Features

- **Snapshot capture**
- **Hash/MD5 tracking**
- **Glob filtering**
- **Create/delete/modify detection**
- **Diff between snapshots**
- **Watch mode**

## Example

```bash
python file_watcher.py self-test
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
        run: python file_watcher.py self-test
```

## Why

File Watcher is built for agent-native workflows: zero dependencies, offline-first, CI-ready.
Part of the Hermes autonomous product stack (31 agent-native tools, all CI-tested).

## Support

Free + MIT. Sponsor if useful:
- GitHub Sponsors: https://github.com/sponsors/itsPremkumar
- Buy Me a Coffee: https://buymeacoffee.com/itsPremkumar

⭐ Star on [GitHub](https://github.com/itsPremkumar/file-watcher)
