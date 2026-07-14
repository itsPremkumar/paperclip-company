# Founder Go-Live Checklist — Prem Autonomous Co

**Purpose:** One document that maps every publish-gated issue to its staged, review-ready
artifact and the exact founder steps to make it public. The agent (Hermes Engineer) has
built and staged everything below; **none of it is auto-published** (house rule: public
publishing requires founder approval).

**House rule reminder:** founder (Prem) approval is required before any public publish —
GitHub Pages, LinkedIn, YouTube/TikTok, Gumroad. The agent must stop at the publish gate.

---

## 1. PRE-5 — Showcase repo + LinkedIn page
**Status:** `in_review` (build complete; awaiting founder publish).
**Artifacts (staged):** `showcase-stage/prem-autonomous-showcase/`
- `README.md` — repo front page
- `index.html` — GitHub Pages site (self-contained)
- `linkedin-launch.md` — Company Page "About" + 2 launch posts
- `pricing.md` — agent-labor service + tier sheet (links resolve; numbers founder-approved)
- `writing.md` + `writing/` — two Medium article drafts (PRE-54 artifacts)
- `.github/workflows/pages.yml` — auto-deploys on push to `main`
- `PUBLISH-RUNBOOK.md` — full step-by-step
- `FOUNDER-GO-LIVE-CHECKLIST.md` — this file

**Founder steps (~10 min):**
1. Create GitHub repo `itsPremkumar/prem-autonomous-showcase` (public).
2. Copy bundle OUTSIDE the monorepo, then publish:
   ```
   xcopy /E /I paperclip-company\showcase-stage\prem-autonomous-showcase C:\one\prem-autonomous-showcase
   cd C:\one\prem-autonomous-showcase
   git init -b main
   git add -A
   git commit -m "Showcase: autonomous agent offerings (PRE-5)"
   git remote add origin https://github.com/itsPremkumar/prem-autonomous-showcase.git
   git push -u origin main
   ```
3. Repo Settings → Pages → Source: "GitHub Actions".
4. LinkedIn: paste `linkedin-launch.md` into the Company Page "About" + publish one launch post.
5. **Before publishing the site, fill the placeholder:** `index.html` + `README.md` say
   "add your public contact email here" — replace with a real public email (or remove).
6. Report the public URLs back on PRE-5 so the agent can flip it to `done` and link it from
   PRE-8 outreach + PRE-7 video descriptions.

---

## 2. PRE-6 — Agent-labor service + pricing tiers
**Status:** `in_review` (build complete; floor approved by CEO; public publish is founder gate).
**Artifacts (staged):**
- `artifacts/PRE-6-agent-labor-service-pricing.md` — full tier framework + go-live gates
- `revenue/public-pricing-sheet.md` — the approved public 6-packaged-team pricing
  ($129–$499/mo + $990 custom)

**Founder steps:**
1. Confirm the approved public floor: **$129–$499/mo + $990 custom** (do NOT publish the
   $15 Starter micro-floor as the public offer).
2. Decide the open gate: auto-showcase free-tier output publicly (opt-out) or keep private.
3. Publish path: link `revenue/public-pricing-sheet.md` from the PRE-5 showcase repo / LinkedIn,
   OR host it as a page. Founder publishes; agent does not.
4. Report the public pricing URL on PRE-6.

---

## 3. PRE-72 — Developer Prompt Pack on Gumroad
**Status:** `in_review` (product built; founder login required to publish — auth boundary).
**Artifacts (staged):**
- `income-engine/gumroad/products/dev-prompts-pack/PRODUCT.md` — 150 developer prompts
- `income-engine/gumroad/products/dev-prompts-pack/LISTING.txt` — title/price/$14/description
- `revenue/digital-products/prompt-packs/dev-prompts.md` — source prompt library

**Founder steps (~5 min, requires Gumroad login):**
1. Gumroad → Products → New product.
2. Name: `150 Developer Productivity Prompts`; Price: `$14`; Category: Developer Tools.
3. Upload `PRODUCT.md` as the file (access = "Software / File").
4. Paste the DESCRIPTION from `LISTING.txt`.
5. Publish.
6. Report the Gumroad product URL on PRE-72.

---

## 4. PRE-54 — 2 Medium articles
**Status:** `in_review` (both drafts written; founder Medium login required to publish).
**Artifacts (staged):**
- `revenue/blog/medium/how-i-built-a-zero-cost-ai-company.md`
- `revenue/blog/medium/ai-agents-replace-10k-agencies.md`

**Founder steps:**
1. Log into Medium; join the Partner Program (if not already).
2. Paste each draft; submit to **Better Programming** and/or **Towards Data Science**.
3. Report the published URLs on PRE-54.

---

## 5. PRE-7 / PRE-74 — 3 sample videos
**Status:** PRE-7 render = `done` (all 3 MP4s rendered). PRE-74 upload = `blocked`
(founder YouTube/TikTok login required — auth boundary).
**Artifacts (rendered, on disk):**
- `C:/one/Automated-Video-Generator/output/pre7_space_facts/3 Mind Blowing Facts About Space.mp4` (21s) + thumbnail + `details.txt`
- `C:/one/Automated-Video-Generator/output/pre7_ocean_mystery/The Ocean Is Deeper Than You Imagine.mp4` (24s) + thumbnail + `details.txt`
- `C:/one/Automated-Video-Generator/output/pre7_productivity_tip/One Simple Trick To Beat Procrastination.mp4` (23s) + thumbnail + `details.txt`

**Founder steps:**
1. Upload each MP4 to YouTube Shorts + TikTok from your own accounts.
2. Use the per-folder `details.txt` for title/description/hashtags.
3. Report the public URLs on PRE-74 so the agent can flip it (and PRE-7) to `done`.

---

## 6. PRE-81 / PRE-8 — Free-board outreach
**Status:** `blocked` (kit ready; founder login to 5 boards required — auth boundary).
**Kit (staged):** `artifacts/PRE-8-free-board-outreach-kit.md` (per-board copy + runbook +
outcome tracker + PRE-11→PRE-79 monitoring handoff).

**Founder steps:**
1. Approve go-live for the five free boards (reply "approved" on PRE-81).
2. Log in and execute the Section 3 runbook (~45 min); post on LinkedIn, Naukri, Wellfound,
   RemoteAI, YC Work at a Startup (NO paid RemoteOK).
3. Paste each live post URL into the Section 4 tracker; flip Posted? to Y.
4. Report any replies/inbound on PRE-79 so the agent can triage leads.

---

## Summary — what the agent has already done vs. what only the founder can do
| Issue | Agent work | Founder action | Blocker |
|---|---|---|---|
| PRE-5 | repo + site + LinkedIn drafts built | publish repo/Pages/LinkedIn | founder approval |
| PRE-6 | pricing tiers + sheet staged | publish public pricing | founder approval |
| PRE-72 | prompt pack product built | Gumroad publish | Gumroad login |
| PRE-54 | 2 articles drafted | Medium publish | Medium login |
| PRE-7 | 3 videos rendered | — | done |
| PRE-74 | — | upload to YT/TikTok | YT/TikTok login |
| PRE-81 | outreach kit ready | post on 5 boards | board logins |

**Net:** all agent-buildable work is complete and staged. The only remaining path to revenue
is founder execution of the publish steps above. Reply "approved" on the relevant issues (or
paste published URLs) and the agent will flip them to `done` and wire the cross-links.
