---
name: prompt-lint
version: 1.0.0
description: Lint prompts/SKILL.md for quality (role, goal, output format, vague verbs, jailbreak phrases). Stdlib.
tags: [prompt, lint, quality, openclaw, hermes, agent]
---

# prompt-lint — ship crisp agent instructions

Scores a prompt on the basics agents actually need: clear role, explicit goal, stated
output format, no vague verbs ("help somehow"), no jailbreak phrases. Returns 0-100.
Zero deps.

## Usage
```bash
python prompt_lint.py check <file.md> [--json]
```

## Why
Weak prompts = weak agents. This is the cheap pre-flight check. Free + MIT. A premium
"prompt fixer" bundle is on Gumroad.

## Support
Free + MIT. Sponsor if useful:
- GitHub Sponsors: https://github.com/sponsors/itsPremkumar  *(add your link)*
- Buy Me a Coffee: https://buymeacoffee.com/itsPremkumar      *(add your link)*
