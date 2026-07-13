---
name: md-linter
version: 2.0.0
description: Lint and auto-format Markdown: trailing whitespace, frontmatter validation, TOC generation
tags: ["markdown", "lint", "format", "toc", "cli", "docs"]
---

# Markdown Linter v2 🚀

Lint and auto-format Markdown: trailing whitespace, frontmatter validation, TOC generation

Zero dependencies (Python stdlib only). Works on Windows, macOS, Linux.

## ✨ What's New in v2

| Feature | Description |
|---------|-------------|
| Trailing whitespace detection  | Trailing whitespace detection (CI-friendly exit 1) |
| Frontmatter validation | Frontmatter validation |
| TOC generation with nesting | TOC generation with nesting |
| Format with dry-run | Format with dry-run |
| TOC insertion | TOC insertion |
| Multiple rule sets | Multiple rule sets |

## Install

```bash
# Requires Python 3.8+. No pip install needed.
curl -O https://raw.githubusercontent.com/itsPremkumar/md-linter/main/md_linter.py

# Or copy the file anywhere — it's self-contained.
```

## Commands

| Command | Description |
|---------|-------------|
| `python md_linter.py check <file>` | Lint a Markdown file |
| `python md_linter.py frontmatter <file>` | Validate YAML frontmatter |
| `python md_linter.py toc <file>` | Generate table of contents |
| `python md_linter.py format <file>` | Auto-format (dry-run by default) |
| `python md_linter.py toc --insert <file>` | Insert TOC into file |
| `python md_linter.py self-test` | Run built-in tests |

## Features

- **Trailing whitespace detection (CI-friendly exit 1)**
- **Frontmatter validation**
- **TOC generation with nesting**
- **Format with dry-run**
- **TOC insertion**
- **Multiple rule sets**

## Example

```bash
python md_linter.py self-test
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
        run: python md_linter.py self-test
```

## Why

Markdown Linter is built for agent-native workflows: zero dependencies, offline-first, CI-ready.
Part of the Hermes autonomous product stack (31 agent-native tools, all CI-tested).

## Support

Free + MIT. Sponsor if useful:
- GitHub Sponsors: https://github.com/sponsors/itsPremkumar
- Buy Me a Coffee: https://buymeacoffee.com/itsPremkumar

⭐ Star on [GitHub](https://github.com/itsPremkumar/md-linter)
