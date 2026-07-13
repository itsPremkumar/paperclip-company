# Secret Scanner 🚀

[![Python 3.8+](https://img.shields.io/badge/python-3.8%2B-blue.svg)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)
![security](https://img.shields.io/badge/tag-security-blue) ![secret](https://img.shields.io/badge/tag-secret-blue) ![scan](https://img.shields.io/badge/tag-scan-blue) ![audit](https://img.shields.io/badge/tag-audit-blue) ![cli](https://img.shields.io/badge/tag-cli-blue) ![credentials](https://img.shields.io/badge/tag-credentials-blue)

Detect API keys, tokens, and credentials in code with 50+ patterns, entropy analysis, and multiple report formats

Zero dependencies (Python stdlib only). Works on Windows, macOS, Linux.

## ✨ Features

- 50+ detection patterns
- Context display (surrounding lines)
- .gitignore-aware
- Multiple report formats (text/json/csv/html)
- Entropy detection for random keys
- GitHub PAT, OpenAI, JWT, MongoDB, Stripe, SSH

## Commands

| Command | Description |
|---------|-------------|
| `scan <path>` | Scan directory for secrets |
| `check <file>` | Deep-scan single file |
| `list-patterns` | List all detection patterns |
| `validate-line <text>` | Test a single line |
| `export-report <path>` | Export report (text/json/csv/html) |
| `watch <dir>` | Watch directory for new secrets |
| `self-test` | Run built-in tests |

## Quick Start

```bash
# Download (no pip needed)
curl -O https://raw.githubusercontent.com/itsPremkumar/secret-scanner/main/secret_scanner.py

# Run
python secret_scanner.py self-test
```

## Why Secret Scanner?

- **Zero deps** — runs in any Python 3.8+ environment
- **Offline-first** — no telemetry, no uploads, fully private
- **CI-ready** — JSON output + self-tests for pipelines
- **Cross-platform** — identical output on Windows/macOS/Linux

---

📦 Also on [ClawHub](https://clawhub.ai/skills/skills/secret-scanner)  
⭐ Star on [GitHub](https://github.com/itsPremkumar/secret-scanner)  
☕ [Buy Me a Coffee](https://buymeacoffee.com/itsPremkumar)
