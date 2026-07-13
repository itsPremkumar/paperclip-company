# Excalidraw CLI 🚀

[![Python 3.8+](https://img.shields.io/badge/python-3.8%2B-blue.svg)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)
![excalidraw](https://img.shields.io/badge/tag-excalidraw-blue) ![diagrams](https://img.shields.io/badge/tag-diagrams-blue) ![flowchart](https://img.shields.io/badge/tag-flowchart-blue) ![architecture](https://img.shields.io/badge/tag-architecture-blue) ![cli](https://img.shields.io/badge/tag-cli-blue) ![drawing](https://img.shields.io/badge/tag-drawing-blue)

Generate Excalidraw diagrams (flowcharts, sequences, architecture) as valid .excalidraw JSON

Zero dependencies (Python stdlib only). Works on Windows, macOS, Linux.

## ✨ Features

- Valid Excalidraw JSON output
- Multiple diagram types (flowchart, sequence, arch, gantt)
- Colored elements
- Text labels
- Compatible with excalidraw.com
- Zero dependencies

## Commands

| Command | Description |
|---------|-------------|
| `create flowchart` | Generate a flowchart |
| `create sequence` | Generate a sequence diagram |
| `create arch` | Generate architecture diagram |
| `create gantt` | Generate a Gantt chart |
| `render <file>` | Render to SVG/PNG |
| `export <file>` | Export diagram |
| `list` | List templates |
| `show <file>` | Show diagram JSON |
| `self-test` | Run built-in tests |

## Quick Start

```bash
# Download (no pip needed)
curl -O https://raw.githubusercontent.com/itsPremkumar/excalidraw-cli/main/excalidraw_cli.py

# Run
python excalidraw_cli.py self-test
```

## Why Excalidraw CLI?

- **Zero deps** — runs in any Python 3.8+ environment
- **Offline-first** — no telemetry, no uploads, fully private
- **CI-ready** — JSON output + self-tests for pipelines
- **Cross-platform** — identical output on Windows/macOS/Linux

---

📦 Also on [ClawHub](https://clawhub.ai/skills/skills/excalidraw-cli)  
⭐ Star on [GitHub](https://github.com/itsPremkumar/excalidraw-cli)  
☕ [Buy Me a Coffee](https://buymeacoffee.com/itsPremkumar)
