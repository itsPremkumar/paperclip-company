---
name: agent-caps
version: 2.0.0
description: Define, validate, and audit agent capability manifests for safe skill installation
tags: ["agent", "caps", "security", "manifest", "cli", "safety"]
---

# Agent Capability Manifest v2 🚀

Define, validate, and audit agent capability manifests for safe skill installation

Zero dependencies (Python stdlib only). Works on Windows, macOS, Linux.

## ✨ What's New in v2

| Feature | Description |
|---------|-------------|
| Manifest schema validation | Manifest schema validation |
| Skill audit before install | Skill audit before install |
| Capability diffing | Capability diffing |
| Risk scoring | Risk scoring |
| JSON output | JSON output |
| CI integration | CI integration |

## Install

```bash
# Requires Python 3.8+. No pip install needed.
curl -O https://raw.githubusercontent.com/itsPremkumar/agent-caps/main/agent_caps.py

# Or copy the file anywhere — it's self-contained.
```

## Commands

| Command | Description |
|---------|-------------|
| `python agent_caps.py validate <manifest>` | Validate capability manifest |
| `python agent_caps.py audit <skill>` | Audit a skill folder |
| `python agent_caps.py diff <a> <b>` | Compare manifests |
| `python agent_caps.py report <agent>` | Generate capability report |
| `python agent_caps.py self-test` | Run built-in tests |

## Features

- **Manifest schema validation**
- **Skill audit before install**
- **Capability diffing**
- **Risk scoring**
- **JSON output**
- **CI integration**

## Example

```bash
python agent_caps.py self-test
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
        run: python agent_caps.py self-test
```

## Why

Agent Capability Manifest is built for agent-native workflows: zero dependencies, offline-first, CI-ready.
Part of the Hermes autonomous product stack (31 agent-native tools, all CI-tested).

## Support

Free + MIT. Sponsor if useful:
- GitHub Sponsors: https://github.com/sponsors/itsPremkumar
- Buy Me a Coffee: https://buymeacoffee.com/itsPremkumar

⭐ Star on [GitHub](https://github.com/itsPremkumar/agent-caps)
