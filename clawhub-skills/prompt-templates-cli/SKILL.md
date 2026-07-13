---
name: prompt-templates-cli
version: 2.0.0
description: Manage reusable prompt templates: create, render, validate with variables
tags: ["prompts", "templates", "cli", "ai", "automation", "render"]
---

# Prompt Templates CLI v2 🚀

Manage reusable prompt templates: create, render, validate with variables

Zero dependencies (Python stdlib only). Works on Windows, macOS, Linux.

## ✨ What's New in v2

| Feature | Description |
|---------|-------------|
| Template library | Template library |
| Variable substitution | Variable substitution |
| Validation | Validation |
| Import/export | Import/export |
| JSON output | JSON output |
| Versioning | Versioning |

## Install

```bash
# Requires Python 3.8+. No pip install needed.
curl -O https://raw.githubusercontent.com/itsPremkumar/prompt-templates-cli/main/prompt_templates_cli.py

# Or copy the file anywhere — it's self-contained.
```

## Commands

| Command | Description |
|---------|-------------|
| `python prompt_templates_cli.py list` | List templates |
| `python prompt_templates_cli.py render <name> --vars x=y` | Render a template |
| `python prompt_templates_cli.py create <name>` | Create template |
| `python prompt_templates_cli.py validate <name>` | Validate syntax |
| `python prompt_templates_cli.py self-test` | Run built-in tests |

## Features

- **Template library**
- **Variable substitution**
- **Validation**
- **Import/export**
- **JSON output**
- **Versioning**

## Example

```bash
python prompt_templates_cli.py self-test
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
        run: python prompt_templates_cli.py self-test
```

## Why

Prompt Templates CLI is built for agent-native workflows: zero dependencies, offline-first, CI-ready.
Part of the Hermes autonomous product stack (31 agent-native tools, all CI-tested).

## Support

Free + MIT. Sponsor if useful:
- GitHub Sponsors: https://github.com/sponsors/itsPremkumar
- Buy Me a Coffee: https://buymeacoffee.com/itsPremkumar

⭐ Star on [GitHub](https://github.com/itsPremkumar/prompt-templates-cli)
