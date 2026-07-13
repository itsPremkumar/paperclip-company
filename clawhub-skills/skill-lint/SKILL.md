---
name: skill-lint
version: 2.0.0
description: Lint ClawHub SKILL.md files: frontmatter, structure, command docs, thin-content detection
tags: ["lint", "skill", "clawhub", "cli", "docs", "quality"]
---

# Skill Linter v2 🚀

Lint ClawHub SKILL.md files: frontmatter, structure, command docs, thin-content detection

Zero dependencies (Python stdlib only). Works on Windows, macOS, Linux.

## ✨ What's New in v2

| Feature | Description |
|---------|-------------|
| Frontmatter validation | Frontmatter validation |
| Structure checks | Structure checks |
| Command doc verification | Command doc verification |
| Thin-content detection | Thin-content detection |
| Auto-fix mode | Auto-fix mode |
| JSON output | JSON output |

## Install

```bash
# Requires Python 3.8+. No pip install needed.
curl -O https://raw.githubusercontent.com/itsPremkumar/skill-lint/main/skill_lint.py

# Or copy the file anywhere — it's self-contained.
```

## Commands

| Command | Description |
|---------|-------------|
| `python skill_lint.py lint <skill>` | Lint a SKILL.md |
| `python skill_lint.py fix <skill>` | Auto-fix issues |
| `python skill_lint.py audit <dir>` | Audit a skill directory |
| `python skill_lint.py self-test` | Run built-in tests |

## Features

- **Frontmatter validation**
- **Structure checks**
- **Command doc verification**
- **Thin-content detection**
- **Auto-fix mode**
- **JSON output**

## Example

```bash
python skill_lint.py self-test
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
        run: python skill_lint.py self-test
```

## Why

Skill Linter is built for agent-native workflows: zero dependencies, offline-first, CI-ready.
Part of the Hermes autonomous product stack (31 agent-native tools, all CI-tested).

## Support

Free + MIT. Sponsor if useful:
- GitHub Sponsors: https://github.com/sponsors/itsPremkumar
- Buy Me a Coffee: https://buymeacoffee.com/itsPremkumar

⭐ Star on [GitHub](https://github.com/itsPremkumar/skill-lint)
