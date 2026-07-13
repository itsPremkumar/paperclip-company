# Markdown Linter 🚀

[![Python 3.8+](https://img.shields.io/badge/python-3.8%2B-blue.svg)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)
![markdown](https://img.shields.io/badge/tag-markdown-blue) ![lint](https://img.shields.io/badge/tag-lint-blue) ![format](https://img.shields.io/badge/tag-format-blue) ![toc](https://img.shields.io/badge/tag-toc-blue) ![cli](https://img.shields.io/badge/tag-cli-blue) ![docs](https://img.shields.io/badge/tag-docs-blue)

Lint and auto-format Markdown: trailing whitespace, frontmatter validation, TOC generation

Zero dependencies (Python stdlib only). Works on Windows, macOS, Linux.

## ✨ Features

- Trailing whitespace detection (CI-friendly exit 1)
- Frontmatter validation
- TOC generation with nesting
- Format with dry-run
- TOC insertion
- Multiple rule sets

## Commands

| Command | Description |
|---------|-------------|
| `check <file>` | Lint a Markdown file |
| `frontmatter <file>` | Validate YAML frontmatter |
| `toc <file>` | Generate table of contents |
| `format <file>` | Auto-format (dry-run by default) |
| `toc --insert <file>` | Insert TOC into file |
| `self-test` | Run built-in tests |

## Quick Start

```bash
# Download (no pip needed)
curl -O https://raw.githubusercontent.com/itsPremkumar/md-linter/main/md_linter.py

# Run
python md_linter.py self-test
```

## Why Markdown Linter?

- **Zero deps** — runs in any Python 3.8+ environment
- **Offline-first** — no telemetry, no uploads, fully private
- **CI-ready** — JSON output + self-tests for pipelines
- **Cross-platform** — identical output on Windows/macOS/Linux

---

📦 Also on [ClawHub](https://clawhub.ai/skills/skills/md-linter)  
⭐ Star on [GitHub](https://github.com/itsPremkumar/md-linter)  
☕ [Buy Me a Coffee](https://buymeacoffee.com/itsPremkumar)
