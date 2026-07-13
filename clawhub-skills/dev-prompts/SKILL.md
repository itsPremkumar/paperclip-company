---
name: dev-prompts
version: 2.0.0
description: Curated collection of engineering prompts: code review, debugging, architecture, refactoring
tags: ["prompts", "dev", "engineering", "templates", "ai", "productivity"]
---

# Developer Prompts Pack v2 🚀

Curated collection of engineering prompts: code review, debugging, architecture, refactoring

Zero dependencies (Python stdlib only). Works on Windows, macOS, Linux.

## ✨ What's New in v2

| Feature | Description |
|---------|-------------|
| 30+ engineering prompt templat | 30+ engineering prompt templates |
| Code review prompts | Code review prompts |
| Debugging workflows | Debugging workflows |
| Architecture decision prompts | Architecture decision prompts |
| Refactoring guides | Refactoring guides |
| Copy-paste ready | Copy-paste ready |

## Install

```bash
# Requires Python 3.8+. No pip install needed.
curl -O https://raw.githubusercontent.com/itsPremkumar/dev-prompts/main/SKILL.md

# Or copy the file anywhere — it's self-contained.
```

## Commands

| Command | Description |
|---------|-------------|
| `list` | List available prompts |
| `show <name>` | Show a prompt template |
| `search <query>` | Find relevant prompts |

## Features

- **30+ engineering prompt templates**
- **Code review prompts**
- **Debugging workflows**
- **Architecture decision prompts**
- **Refactoring guides**
- **Copy-paste ready**

## Example

```bash
python None self-test
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
        run: python None self-test
```

## Why

Developer Prompts Pack is built for agent-native workflows: zero dependencies, offline-first, CI-ready.
Part of the Hermes autonomous product stack (31 agent-native tools, all CI-tested).

## Support

Free + MIT. Sponsor if useful:
- GitHub Sponsors: https://github.com/sponsors/itsPremkumar
- Buy Me a Coffee: https://buymeacoffee.com/itsPremkumar

⭐ Star on [GitHub](https://github.com/itsPremkumar/dev-prompts)
