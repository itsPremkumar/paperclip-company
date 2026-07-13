---
name: skill-benchmark
version: 2.0.0
description: Benchmark ClawHub skills: performance, correctness, documentation quality
tags: ["benchmark", "skill", "quality", "cli", "testing", "metrics"]
---

# Skill Benchmark v2 🚀

Benchmark ClawHub skills: performance, correctness, documentation quality

Zero dependencies (Python stdlib only). Works on Windows, macOS, Linux.

## ✨ What's New in v2

| Feature | Description |
|---------|-------------|
| Performance benchmarking | Performance benchmarking |
| Correctness checks | Correctness checks |
| Doc quality scoring | Doc quality scoring |
| Comparison reports | Comparison reports |
| JSON output | JSON output |
| CI integration | CI integration |

## Install

```bash
# Requires Python 3.8+. No pip install needed.
curl -O https://raw.githubusercontent.com/itsPremkumar/skill-benchmark/main/skill_benchmark.py

# Or copy the file anywhere — it's self-contained.
```

## Commands

| Command | Description |
|---------|-------------|
| `python skill_benchmark.py run <skill>` | Run benchmark suite |
| `python skill_benchmark.py report <skill>` | Generate report |
| `python skill_benchmark.py compare <a> <b>` | Compare skills |
| `python skill_benchmark.py self-test` | Run built-in tests |

## Features

- **Performance benchmarking**
- **Correctness checks**
- **Doc quality scoring**
- **Comparison reports**
- **JSON output**
- **CI integration**

## Example

```bash
python skill_benchmark.py self-test
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
        run: python skill_benchmark.py self-test
```

## Why

Skill Benchmark is built for agent-native workflows: zero dependencies, offline-first, CI-ready.
Part of the Hermes autonomous product stack (31 agent-native tools, all CI-tested).

## Support

Free + MIT. Sponsor if useful:
- GitHub Sponsors: https://github.com/sponsors/itsPremkumar
- Buy Me a Coffee: https://buymeacoffee.com/itsPremkumar

⭐ Star on [GitHub](https://github.com/itsPremkumar/skill-benchmark)
