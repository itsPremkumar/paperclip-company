# Prompt Templates CLI 🚀

[![Python 3.8+](https://img.shields.io/badge/python-3.8%2B-blue.svg)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)
![prompts](https://img.shields.io/badge/tag-prompts-blue) ![templates](https://img.shields.io/badge/tag-templates-blue) ![cli](https://img.shields.io/badge/tag-cli-blue) ![ai](https://img.shields.io/badge/tag-ai-blue) ![automation](https://img.shields.io/badge/tag-automation-blue) ![render](https://img.shields.io/badge/tag-render-blue)

Manage reusable prompt templates: create, render, validate with variables

Zero dependencies (Python stdlib only). Works on Windows, macOS, Linux.

## ✨ Features

- Template library
- Variable substitution
- Validation
- Import/export
- JSON output
- Versioning

## Commands

| Command | Description |
|---------|-------------|
| `list` | List templates |
| `render <name> --vars x=y` | Render a template |
| `create <name>` | Create template |
| `validate <name>` | Validate syntax |
| `self-test` | Run built-in tests |

## Quick Start

```bash
# Download (no pip needed)
curl -O https://raw.githubusercontent.com/itsPremkumar/prompt-templates-cli/main/prompt_templates_cli.py

# Run
python prompt_templates_cli.py self-test
```

## Why Prompt Templates CLI?

- **Zero deps** — runs in any Python 3.8+ environment
- **Offline-first** — no telemetry, no uploads, fully private
- **CI-ready** — JSON output + self-tests for pipelines
- **Cross-platform** — identical output on Windows/macOS/Linux

---

📦 Also on [ClawHub](https://clawhub.ai/skills/skills/prompt-templates-cli)  
⭐ Star on [GitHub](https://github.com/itsPremkumar/prompt-templates-cli)  
☕ [Buy Me a Coffee](https://buymeacoffee.com/itsPremkumar)
