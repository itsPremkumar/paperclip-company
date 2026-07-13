# Skill Linter 🚀

[![Python 3.8+](https://img.shields.io/badge/python-3.8%2B-blue.svg)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)
![lint](https://img.shields.io/badge/tag-lint-blue) ![skill](https://img.shields.io/badge/tag-skill-blue) ![clawhub](https://img.shields.io/badge/tag-clawhub-blue) ![cli](https://img.shields.io/badge/tag-cli-blue) ![docs](https://img.shields.io/badge/tag-docs-blue) ![quality](https://img.shields.io/badge/tag-quality-blue)

Lint ClawHub SKILL.md files: frontmatter, structure, command docs, thin-content detection

Zero dependencies (Python stdlib only). Works on Windows, macOS, Linux.

## ✨ Features

- Frontmatter validation
- Structure checks
- Command doc verification
- Thin-content detection
- Auto-fix mode
- JSON output

## Commands

| Command | Description |
|---------|-------------|
| `lint <skill>` | Lint a SKILL.md |
| `fix <skill>` | Auto-fix issues |
| `audit <dir>` | Audit a skill directory |
| `self-test` | Run built-in tests |

## Quick Start

```bash
# Download (no pip needed)
curl -O https://raw.githubusercontent.com/itsPremkumar/skill-lint/main/skill_lint.py

# Run
python skill_lint.py self-test
```

## Why Skill Linter?

- **Zero deps** — runs in any Python 3.8+ environment
- **Offline-first** — no telemetry, no uploads, fully private
- **CI-ready** — JSON output + self-tests for pipelines
- **Cross-platform** — identical output on Windows/macOS/Linux

---

📦 Also on [ClawHub](https://clawhub.ai/skills/skills/skill-lint)  
⭐ Star on [GitHub](https://github.com/itsPremkumar/skill-lint)  
☕ [Buy Me a Coffee](https://buymeacoffee.com/itsPremkumar)
