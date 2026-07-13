---
name: secret-scanner
version: 2.0.0
description: Detect API keys, tokens, and credentials in code with 50+ patterns, entropy analysis, and multiple report formats
tags: ["security", "secret", "scan", "audit", "cli", "credentials"]
---

# Secret Scanner v2 🚀

Detect API keys, tokens, and credentials in code with 50+ patterns, entropy analysis, and multiple report formats

Zero dependencies (Python stdlib only). Works on Windows, macOS, Linux.

## ✨ What's New in v2

| Feature | Description |
|---------|-------------|
| 50+ detection patterns | 50+ detection patterns |
| Context display (surrounding l | Context display (surrounding lines) |
| .gitignore-aware | .gitignore-aware |
| Multiple report formats (text/ | Multiple report formats (text/json/csv/html) |
| Entropy detection for random k | Entropy detection for random keys |
| GitHub PAT, OpenAI, JWT, Mongo | GitHub PAT, OpenAI, JWT, MongoDB, Stripe, SSH |

## Install

```bash
# Requires Python 3.8+. No pip install needed.
curl -O https://raw.githubusercontent.com/itsPremkumar/secret-scanner/main/secret_scanner.py

# Or copy the file anywhere — it's self-contained.
```

## Commands

| Command | Description |
|---------|-------------|
| `python secret_scanner.py scan <path>` | Scan directory for secrets |
| `python secret_scanner.py check <file>` | Deep-scan single file |
| `python secret_scanner.py list-patterns` | List all detection patterns |
| `python secret_scanner.py validate-line <text>` | Test a single line |
| `python secret_scanner.py export-report <path>` | Export report (text/json/csv/html) |
| `python secret_scanner.py watch <dir>` | Watch directory for new secrets |
| `python secret_scanner.py self-test` | Run built-in tests |

## Features

- **50+ detection patterns**
- **Context display (surrounding lines)**
- **.gitignore-aware**
- **Multiple report formats (text/json/csv/html)**
- **Entropy detection for random keys**
- **GitHub PAT, OpenAI, JWT, MongoDB, Stripe, SSH**

## Example

```bash
python secret_scanner.py self-test
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
        run: python secret_scanner.py self-test
```

## Why

Secret Scanner is built for agent-native workflows: zero dependencies, offline-first, CI-ready.
Part of the Hermes autonomous product stack (31 agent-native tools, all CI-tested).

## Support

Free + MIT. Sponsor if useful:
- GitHub Sponsors: https://github.com/sponsors/itsPremkumar
- Buy Me a Coffee: https://buymeacoffee.com/itsPremkumar

⭐ Star on [GitHub](https://github.com/itsPremkumar/secret-scanner)
