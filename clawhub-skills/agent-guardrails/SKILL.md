---
name: agent-guardrails
version: 2.0.0
description: Enforce safety guardrails on agent actions: permission gates, allowlists, audit
tags: ["guardrails", "safety", "agent", "cli", "security", "policy"]
---

# Agent Guardrails v2 🚀

Enforce safety guardrails on agent actions: permission gates, allowlists, audit

Zero dependencies (Python stdlib only). Works on Windows, macOS, Linux.

## ✨ What's New in v2

| Feature | Description |
|---------|-------------|
| Permission gating | Permission gating |
| Allowlist/denylist | Allowlist/denylist |
| Policy definition | Policy definition |
| Violation audit | Violation audit |
| JSON output | JSON output |
| CI integration | CI integration |

## Install

```bash
# Requires Python 3.8+. No pip install needed.
curl -O https://raw.githubusercontent.com/itsPremkumar/agent-guardrails/main/agent_guardrails.py

# Or copy the file anywhere — it's self-contained.
```

## Commands

| Command | Description |
|---------|-------------|
| `python agent_guardrails.py check <action>` | Check if action is allowed |
| `python agent_guardrails.py policy <agent>` | Show agent policy |
| `python agent_guardrails.py audit <agent>` | Audit violations |
| `python agent_guardrails.py self-test` | Run built-in tests |

## Features

- **Permission gating**
- **Allowlist/denylist**
- **Policy definition**
- **Violation audit**
- **JSON output**
- **CI integration**

## Example

```bash
python agent_guardrails.py self-test
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
        run: python agent_guardrails.py self-test
```

## Why

Agent Guardrails is built for agent-native workflows: zero dependencies, offline-first, CI-ready.
Part of the Hermes autonomous product stack (31 agent-native tools, all CI-tested).

## Support

Free + MIT. Sponsor if useful:
- GitHub Sponsors: https://github.com/sponsors/itsPremkumar
- Buy Me a Coffee: https://buymeacoffee.com/itsPremkumar

⭐ Star on [GitHub](https://github.com/itsPremkumar/agent-guardrails)
