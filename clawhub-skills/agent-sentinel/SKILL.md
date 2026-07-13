---
name: agent-sentinel
version: 2.0.0
description: Scan OpenClaw/Hermes skills for risky permission patterns before installation
tags: ["security", "audit", "skill", "openclaw", "hermes", "vetting"]
---

# Agent Sentinel v2 🚀

Scan OpenClaw/Hermes skills for risky permission patterns before installation

Zero dependencies (Python stdlib only). Works on Windows, macOS, Linux.

## ✨ What's New in v2

| Feature | Description |
|---------|-------------|
| Simple-named skill requesting  | Simple-named skill requesting shell → HIGH |
| Shell/exec capability requeste | Shell/exec capability requested → MEDIUM |
| Hardcoded secret detection → H | Hardcoded secret detection → HIGH |
| No human approval gate → LOW | No human approval gate → LOW |
| Network egress without reason | Network egress without reason |
| Offline, private, no telemetry | Offline, private, no telemetry |

## Install

```bash
# Requires Python 3.8+. No pip install needed.
curl -O https://raw.githubusercontent.com/itsPremkumar/agent-sentinel/main/agent_sentinel.py

# Or copy the file anywhere — it's self-contained.
```

## Commands

| Command | Description |
|---------|-------------|
| `python agent_sentinel.py scan <skill-folder>` | Risk report for a skill |
| `python agent_sentinel.py self-test` | Run built-in tests |

## Features

- **Simple-named skill requesting shell → HIGH**
- **Shell/exec capability requested → MEDIUM**
- **Hardcoded secret detection → HIGH**
- **No human approval gate → LOW**
- **Network egress without reason**
- **Offline, private, no telemetry**

## Example

```bash
python agent_sentinel.py self-test
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
        run: python agent_sentinel.py self-test
```

## Why

Agent Sentinel is built for agent-native workflows: zero dependencies, offline-first, CI-ready.
Part of the Hermes autonomous product stack (31 agent-native tools, all CI-tested).

## Support

Free + MIT. Sponsor if useful:
- GitHub Sponsors: https://github.com/sponsors/itsPremkumar
- Buy Me a Coffee: https://buymeacoffee.com/itsPremkumar

⭐ Star on [GitHub](https://github.com/itsPremkumar/agent-sentinel)
