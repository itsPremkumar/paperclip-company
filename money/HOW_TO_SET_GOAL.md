# 🎯 HOW TO SET THE AUTONOMOUS MONEY GOAL — Step by Step

This file gives you the EXACT text to paste and the exact steps. No guessing.

================================================================
## STEP 0 — Raise the loop turn budget (one time, in terminal or chat)
================================================================

Run this once so the goal loop doesn't stop at 20 turns:

    hermes config set agent.goal_max_turns 120

(If that key errors, try: `hermes config set goal.max_turns 120`
 or check available keys with: `hermes config | grep -i goal`)

================================================================
## STEP 1 — Paste this as a slash command to DRAFT the contract
================================================================

Copy the ENTIRE block below and paste it into your Hermes chat input,
then press Enter:

/goal draft Build the complete zero-to-revenue autonomous money system inside the Hermes-Full-Autonomous-Company repo at C:\one\paperclip-company. Build the 7 remaining pipelines (#6–#12) listed in money/MONEY_AUTOMATION_IDEAS.md: lead-enrichment SaaS, RAG-KB builder, affiliate farm, invoice automation, security scanner, proposal generator, social auto-poster. Each pipeline must follow the proven shape of pipeline1..5 (a data dict + build_package + self-test + --list + --out, stdlib-only, zero external dependencies). Wire every pipeline into money/run_all.py and regenerate money/INCOME_DASHBOARD.md (target: 12 pipelines, ~50 packages). Replace n8n stub manifests with working workflow JSON containing real executable code nodes (no TODO/placeholder). Build infra/docker-compose.yml for n8n + Chatwoot + Stirling-PDF + Listmonk, plus infra/SETUP.md. Generate platform-ready Fiverr and Upwork listing copy for every package under listings/. Schedule the acquisition loop (Moltbook already runs 3-min cadence; add affiliate-farm and cold-email sequences). STOP and pause only at these 3 human gates: (1) marketplace account creation, (2) payment linkage, (3) first live gig approval.

================================================================
## STEP 2 — Activate the goal (after the draft returns a contract)
================================================================

Hermes will return a structured 5-field completion contract
(outcome / verification / constraints / boundaries / stop_when).
Review it, then paste:

    /goal <paste the exact contract text Hermes returned in Step 1>

The judge loop now runs autonomously, turn after turn, until verification
is proven OR it hits a human gate.

================================================================
## STEP 3 — Walk away. The loop handles Phases A–F.
================================================================

It will:
  A. Build pipelines #6–#12 (each self-test must pass)
  B. Unify in run_all.py → `python money/run_all.py self-test` = 12 pipelines, ~50 packages
  C. Real n8n workflows (executable, not stubs)
  D. Infra stack (docker-compose + SETUP.md)
  E. Listing copy for every package
  F. Acquisition loop scheduling
  G. PAUSE at gate #1 with your 3-action checklist

================================================================
## STEP 4 — At each human gate, do the ~5-min action, then resume
================================================================

When the loop pauses, you:
  1. Create Fiverr/Upwork accounts (ID verify)  → then type:  /goal resume
  2. Link PayPal/Stripe                        → then type:  /goal resume
  3. Click Publish on first gig                → then type:  /goal resume

After gate #3 the system is live and earning.

================================================================
## CONTROLS YOU CAN USE ANYTIME
================================================================

  /goal status     → see current goal + progress
  /goal pause      → stop the loop (keep goal)
  /goal resume     → restart the loop
  /goal clear      → delete the goal
  /subgoal <text>  → add extra success criteria mid-loop

Your real message always preempts the loop and pauses it for that turn.

================================================================
## HONEST LIMIT
================================================================

The loop builds, verifies, deploys-ready, and schedules everything.
It CANNOT: create marketplace accounts, link payment, or click Publish
— those 3 points are legally/UI gated to a human. Your total manual
effort = ~15 minutes across the 3 gates.
