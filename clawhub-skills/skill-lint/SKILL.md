---
name: skill-lint
version: 1.0.0
description: Validate a ClawHub/OpenClaw skill folder before publishing (frontmatter, shape, size). Stdlib.
tags: [skill, lint, publish, openclaw, hermes, quality]
---

# skill-lint — lint your skill before you publish

Catches the rejections ClawHub throws: missing SKILL.md, missing YAML frontmatter
(name/version/description), non-semver version, nested skill dirs, oversized files.
Zero deps.

## Usage
```bash
python skill_lint.py check <folder> [--json]
```

## Why
A rejected publish wastes a cycle. Run this locally first. Free + MIT.

## Support
Free + MIT. Sponsor if useful:
- GitHub Sponsors: https://github.com/sponsors/itsPremkumar  *(add your link)*
- Buy Me a Coffee: https://buymeacoffee.com/itsPremkumar      *(add your link)*
