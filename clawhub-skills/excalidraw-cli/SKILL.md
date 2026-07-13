---
name: excalidraw-cli
version: 2.0.0
description: Generate Excalidraw diagrams (flowcharts, sequences, architecture) as valid .excalidraw JSON
tags: ["excalidraw", "diagrams", "flowchart", "architecture", "cli", "drawing"]
---

# Excalidraw CLI v2 🚀

Generate Excalidraw diagrams (flowcharts, sequences, architecture) as valid .excalidraw JSON

Zero dependencies (Python stdlib only). Works on Windows, macOS, Linux.

## ✨ What's New in v2

| Feature | Description |
|---------|-------------|
| Valid Excalidraw JSON output | Valid Excalidraw JSON output |
| Multiple diagram types (flowch | Multiple diagram types (flowchart, sequence, arch, gantt) |
| Colored elements | Colored elements |
| Text labels | Text labels |
| Compatible with excalidraw.com | Compatible with excalidraw.com |
| Zero dependencies | Zero dependencies |

## Install

```bash
# Requires Python 3.8+. No pip install needed.
curl -O https://raw.githubusercontent.com/itsPremkumar/excalidraw-cli/main/excalidraw_cli.py

# Or copy the file anywhere — it's self-contained.
```

## Commands

| Command | Description |
|---------|-------------|
| `python excalidraw_cli.py create flowchart` | Generate a flowchart |
| `python excalidraw_cli.py create sequence` | Generate a sequence diagram |
| `python excalidraw_cli.py create arch` | Generate architecture diagram |
| `python excalidraw_cli.py create gantt` | Generate a Gantt chart |
| `python excalidraw_cli.py render <file>` | Render to SVG/PNG |
| `python excalidraw_cli.py export <file>` | Export diagram |
| `python excalidraw_cli.py list` | List templates |
| `python excalidraw_cli.py show <file>` | Show diagram JSON |
| `python excalidraw_cli.py self-test` | Run built-in tests |

## Features

- **Valid Excalidraw JSON output**
- **Multiple diagram types (flowchart, sequence, arch, gantt)**
- **Colored elements**
- **Text labels**
- **Compatible with excalidraw.com**
- **Zero dependencies**

## Example

```bash
python excalidraw_cli.py self-test
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
        run: python excalidraw_cli.py self-test
```

## Why

Excalidraw CLI is built for agent-native workflows: zero dependencies, offline-first, CI-ready.
Part of the Hermes autonomous product stack (31 agent-native tools, all CI-tested).

## Support

Free + MIT. Sponsor if useful:
- GitHub Sponsors: https://github.com/sponsors/itsPremkumar
- Buy Me a Coffee: https://buymeacoffee.com/itsPremkumar

⭐ Star on [GitHub](https://github.com/itsPremkumar/excalidraw-cli)
