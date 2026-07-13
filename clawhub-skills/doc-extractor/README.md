# Document Text Extractor 🚀

[![Python 3.8+](https://img.shields.io/badge/python-3.8%2B-blue.svg)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)
![pdf](https://img.shields.io/badge/tag-pdf-blue) ![docx](https://img.shields.io/badge/tag-docx-blue) ![extract](https://img.shields.io/badge/tag-extract-blue) ![text](https://img.shields.io/badge/tag-text-blue) ![cli](https://img.shields.io/badge/tag-cli-blue) ![documents](https://img.shields.io/badge/tag-documents-blue)

Extract text from PDF, DOCX, and TXT with encoding detection and page/paragraph structure

Zero dependencies (Python stdlib only). Works on Windows, macOS, Linux.

## ✨ Features

- PDF extraction (pymupdf optional)
- DOCX via zipfile + xml
- TXT with encoding detection
- Page/paragraph structure
- Metadata extraction
- Batch processing

## Commands

| Command | Description |
|---------|-------------|
| `extract <file>` | Extract text from document |
| `pages <file>` | List pages (PDF) |
| `metadata <file>` | Extract metadata |
| `--format txt|md|json` | Output format |
| `--json` | JSON output |
| `self-test` | Run built-in tests |

## Quick Start

```bash
# Download (no pip needed)
curl -O https://raw.githubusercontent.com/itsPremkumar/doc-extractor/main/doc_extractor.py

# Run
python doc_extractor.py self-test
```

## Why Document Text Extractor?

- **Zero deps** — runs in any Python 3.8+ environment
- **Offline-first** — no telemetry, no uploads, fully private
- **CI-ready** — JSON output + self-tests for pipelines
- **Cross-platform** — identical output on Windows/macOS/Linux

---

📦 Also on [ClawHub](https://clawhub.ai/skills/skills/doc-extractor)  
⭐ Star on [GitHub](https://github.com/itsPremkumar/doc-extractor)  
☕ [Buy Me a Coffee](https://buymeacoffee.com/itsPremkumar)
