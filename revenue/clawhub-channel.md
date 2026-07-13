# Channel: ClawHub + Moltbook (agent-native distribution)

Research: 2026-07-13. Sources: docs.openclaw.ai/clawhub, clawhub.ai, medium.com
ClawHub Skill Economy (0xmega, 2026-03), moltbook.com, arstechnica AP News.

## What these platforms are
- **ClawHub** — OpenClaw's native skill/plugin registry. `clawhub` CLI installed here;
  we are authenticated as **itsPremkumar** (`clawhub whoami` ✔). Publish = one command.
- **Moltbook** — "Reddit for AI agents": a social network where agents post/discuss.
  Discovery + distribution channel (agents can post autonomously).
- Both are **agent-native**: the audience IS AI agents / their operators.

## The real business model (the key insight)
ClawHub has **NO paid listings — everything is free**. It is a DISTRIBUTION channel,
not a storefront. Money is made *off* ClawHub, not through it:
  Tier 1 ($100–1k/mo): free skill → premium version on Gumroad / your site
  Tier 2: custom builds for businesses wanting the skill configured for their stack
  Tier 3 ($5k–20k/mo): setup-as-a-service / consulting

So the funnel is: **ClawHub (free skill = distribution) → Gumroad (premium = money)**.
We ALREADY have 7 Gumroad products + the clawhub CLI authed. This closes the loop.

## End-to-end automation reality check (Charter S0)
| Step | Automatable by agent? | Gate |
|------|----------------------|------|
| Build skill (SKILL.md + tool) | YES | none |
| Publish to ClawHub | YES (authed as itsPremkumar) | none |
| Post to Moltbook for visibility | YES (agent-native) | account |
| Link premium Gumroad version | YES (write the link) | Gumroad publish = human (PRE-52) |
| Receive money | NO | Gumroad payout = human |

→ This is the MOST end-to-end-automatable channel we have: the agent can build + publish
  the distribution asset with zero human action. Only the eventual money receipt is gated.

## Action plan (this turn)
1. Package `agent-caps` as a ClawHub skill (SKILL.md + tool + examples).
2. Publish it via `clawhub publish` (authed). Verify live on clawhub.ai.
3. Document the funnel in revenue-strategy.md update.
4. Push skill source to GitHub (source of truth).
5. Moltbook posting left as a documented next step (account + human comfort).

## Compliance
- Skill must be honest (no "guaranteed income"). Our agent-caps is a real, free tool.
- Disclose premium Gumroad link only after Gumroad publish (human step).
- Never store payout creds in the skill.
