---
name: prompt-lint
version: 2.0.0
description: Lint AI prompts: clarity, safety, injection risks, template validity
tags: ["lint", "prompt", "ai", "cli", "safety", "quality"]
---

# Prompt Linter v2 🚀

Lint AI prompts: clarity, safety, injection risks, template validity

Zero dependencies (Python stdlib only). Works on Windows, macOS, Linux.

## ✨ What's New in v2

| Feature | Description |
|---------|-------------|
| Clarity scoring | Clarity scoring |
| Safety checks | Safety checks |
| Injection detection | Injection detection |
| Template validation | Template validation |
| Auto-suggestions | Auto-suggestions |
| JSON output | JSON output |

## Install

```bash
# Requires Python 3.8+. No pip install needed.
curl -O https://raw.githubusercontent.com/itsPremkumar/prompt-lint/main/prompt_lint.py

# Or copy the file anywhere — it's self-contained.
```

## Commands

| Command | Description |
|---------|-------------|
| `python prompt_lint.py lint <prompt>` | Lint a prompt |
| `python prompt_lint.py fix <prompt>` | Suggest fixes |
| `python prompt_lint.py scan <dir>` | Scan prompt files |
| `python prompt_lint.py self-test` | Run built-in tests |

## Features

- **Clarity scoring**
- **Safety checks**
- **Injection detection**
- **Template validation**
- **Auto-suggestions**
- **JSON output**

## Example

```bash
python prompt_lint.py self-test
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
        run: python prompt_lint.py self-test
```

## Why

Prompt Linter is built for agent-native workflows: zero dependencies, offline-first, CI-ready.
Part of the Hermes autonomous product stack (31 agent-native tools, all CI-tested).

## Support

Free + MIT. Sponsor if useful:
- GitHub Sponsors: https://github.com/sponsors/itsPremkumar
- Buy Me a Coffee: https://buymeacoffee.com/itsPremkumar

⭐ Star on [GitHub](https://github.com/itsPremkumar/prompt-lint)
