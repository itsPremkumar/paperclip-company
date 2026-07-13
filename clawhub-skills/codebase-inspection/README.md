# Codebase Inspector 🚀

[![Python 3.8+](https://img.shields.io/badge/python-3.8%2B-blue.svg)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)
![codebase](https://img.shields.io/badge/tag-codebase-blue) ![analysis](https://img.shields.io/badge/tag-analysis-blue) ![metrics](https://img.shields.io/badge/tag-metrics-blue) ![devtools](https://img.shields.io/badge/tag-devtools-blue) ![python](https://img.shields.io/badge/tag-python-blue) ![cli](https://img.shields.io/badge/tag-cli-blue)

Advanced codebase analysis with HTML reports, git-aware diffs, trend tracking, SVG badges, CSV export, and CI/CD integration

Zero dependencies (Python stdlib only). Works on Windows, macOS, Linux.

## ✨ Features

- Automatic language detection (40+ extensions → 30+ languages)
- Smart directory skipping (.git, node_modules, __pycache__, etc.)
- Blank/comment/code line counting
- HTML visual report with bar charts + summary cards
- Historical trend tracking (snapshot-based)
- Git-aware codebase diffing
- SVG badge generation for README
- CSV export for dashboards
- JSON mode for CI/CD pipelines
- Cross-platform (Windows/macOS/Linux)
- 13 built-in self-tests

## Commands

| Command | Description |
|---------|-------------|
| `analyze <dir>` | Analyze directory, print text report |
| `--json` | JSON output for pipelines |
| `--html FILE` | Generate visual HTML report with charts |
| `--csv` | CSV export for spreadsheets |
| `--badge` | Generate shields.io badge URL |
| `--snapshot` | Save as trend data point |
| `--trend` | Show historical trends |
| `--diff <dir2>` | Compare two codebases |
| `--exclude DIRS` | Skip custom directories |
| `self-test` | Run 13 built-in checks |

## Quick Start

```bash
# Download (no pip needed)
curl -O https://raw.githubusercontent.com/itsPremkumar/codebase-inspection/main/codebase_inspector.py

# Run
python codebase_inspector.py self-test
```

## Why Codebase Inspector?

- **Zero deps** — runs in any Python 3.8+ environment
- **Offline-first** — no telemetry, no uploads, fully private
- **CI-ready** — JSON output + self-tests for pipelines
- **Cross-platform** — identical output on Windows/macOS/Linux

---

📦 Also on [ClawHub](https://clawhub.ai/skills/skills/codebase-inspection)  
⭐ Star on [GitHub](https://github.com/itsPremkumar/codebase-inspection)  
☕ [Buy Me a Coffee](https://buymeacoffee.com/itsPremkumar)
