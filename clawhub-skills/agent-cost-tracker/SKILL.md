---
name: agent-cost-tracker
version: 1.0.0
description: Estimate LLM token usage + cost from agent run logs (gpt/claude/gemini pricing). Stdlib, offline.
tags: [cost, tokens, finance, openclaw, hermes, agent]
---

# agent-cost-tracker — know what your agent spends

Agents burn tokens silently. agent-cost-tracker tallies `prompt_tokens`/`completion_tokens`
from any run log and prices it against gpt-4o / claude / gemini rates. Zero deps.

## Usage
```bash
python agent_cost_tracker.py tally <logfile> [--model gpt-4o] [--json]
python agent_cost_tracker.py estimate --prompt 10000 --completion 2000 --model claude-3-5-sonnet
```

## Why
Cost visibility is the difference between a $0 agent and a $200/month surprise. Free + MIT.
A premium "live spend dashboard" bundle is on Gumroad.

## Support
Free + MIT. Sponsor if useful:
- GitHub Sponsors: https://github.com/sponsors/itsPremkumar  *(add your link)*
- Buy Me a Coffee: https://buymeacoffee.com/itsPremkumar      *(add your link)*
