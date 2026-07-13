---
name: codebase-inspection
version: 2.0.0
description: Advanced codebase analysis with HTML reports, git-aware diffs, trend tracking, SVG badges, CSV export, and CI/CD integration
tags: ["codebase", "analysis", "metrics", "devtools", "python", "cli", "ci", "reports"]
---

# Codebase Inspector v2 🚀

Advanced codebase analysis with HTML reports, git-aware diffs, trend tracking, SVG badges, CSV export, and CI/CD integration

Zero dependencies (Python stdlib only). Works on Windows, macOS, Linux.

## ✨ What's New in v2

| Feature | Description |
|---------|-------------|
| Automatic language detection ( | Automatic language detection (40+ extensions → 30+ languages) |
| Smart directory skipping (.git | Smart directory skipping (.git, node_modules, __pycache__, etc.) |
| Blank/comment/code line counti | Blank/comment/code line counting |
| HTML visual report with bar ch | HTML visual report with bar charts + summary cards |
| Historical trend tracking (sna | Historical trend tracking (snapshot-based) |
| Git-aware codebase diffing | Git-aware codebase diffing |
| SVG badge generation for READM | SVG badge generation for README |
| CSV export for dashboards | CSV export for dashboards |

## Install

```bash
# Requires Python 3.8+. No pip install needed.
curl -O https://raw.githubusercontent.com/itsPremkumar/codebase-inspection/main/codebase_inspector.py

# Or copy the file anywhere — it's self-contained.
```

## Commands

| Command | Description |
|---------|-------------|
| `python codebase_inspector.py analyze <dir>` | Analyze directory, print text report |
| `python codebase_inspector.py --json` | JSON output for pipelines |
| `python codebase_inspector.py --html FILE` | Generate visual HTML report with charts |
| `python codebase_inspector.py --csv` | CSV export for spreadsheets |
| `python codebase_inspector.py --badge` | Generate shields.io badge URL |
| `python codebase_inspector.py --snapshot` | Save as trend data point |
| `python codebase_inspector.py --trend` | Show historical trends |
| `python codebase_inspector.py --diff <dir2>` | Compare two codebases |
| `python codebase_inspector.py --exclude DIRS` | Skip custom directories |
| `python codebase_inspector.py self-test` | Run 13 built-in checks |

## Features

- **Automatic language detection (40+ extensions → 30+ languages)**
- **Smart directory skipping (.git, node_modules, __pycache__, etc.)**
- **Blank/comment/code line counting**
- **HTML visual report with bar charts + summary cards**
- **Historical trend tracking (snapshot-based)**
- **Git-aware codebase diffing**
- **SVG badge generation for README**
- **CSV export for dashboards**
- **JSON mode for CI/CD pipelines**
- **Cross-platform (Windows/macOS/Linux)**
- **13 built-in self-tests**

## Example

```bash
python codebase_inspector.py self-test
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
        run: python codebase_inspector.py self-test
```

## Why

Codebase Inspector is built for agent-native workflows: zero dependencies, offline-first, CI-ready.
Part of the Hermes autonomous product stack (31 agent-native tools, all CI-tested).

## Support

Free + MIT. Sponsor if useful:
- GitHub Sponsors: https://github.com/sponsors/itsPremkumar
- Buy Me a Coffee: https://buymeacoffee.com/itsPremkumar

⭐ Star on [GitHub](https://github.com/itsPremkumar/codebase-inspection)
