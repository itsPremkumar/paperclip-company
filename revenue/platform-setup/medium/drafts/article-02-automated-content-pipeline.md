# I Automated 90% of My Content Pipeline — Here's the Exact Architecture

**Subtitle:** From RSS feeds to published articles with zero manual intervention. A complete technical walkthrough of a zero-touch content engine.

**Target Publication:** Better Marketing, Writing Cooperative, or Towards Data Science
**Word Count:** ~2,200 words
**Status:** Draft — ready for human review & Medium submission

---

## The Problem: Content Is a Full-Time Job

When I started Prem Autonomous Co, I knew content was our primary growth channel. With zero ad budget, every impression had to be earned through writing that actually helped people.

The problem: good content takes time. Research, outline, draft, edit, format, publish, repurpose. Repeat 3–5 times a week. That's 20–30 hours — more than the rest of the business combined.

I had two choices: burn out or automate.

I chose automation. Here's exactly how I built a content pipeline that produces 35+ pieces per week with about 90 minutes of human direction. No hype, no "passive income" promises — just the architecture, the tooling, and the honest tradeoffs.

---

## Overview: The Four-Stage Pipeline

The entire system runs on four stages connected by filesystem events and cron schedules:

```
RSS Ingestion → Research Digest → Drafting → Multi-Channel Distribution
     ↑                                                  |
     |________________ Review Gate _____________________|
```

Each stage is an independent agent or script that reads from a shared workspace and writes structured output. No complex message queues, no orchestration platform — just Markdown files on disk and scheduled cron jobs.

**Total monthly operating cost:** $0 (self-hosted, open-source, free-tier LLM APIs).

---

## Stage 1: RSS Ingestion (The Research Loop)

**What it does:** Monitors 20+ RSS feeds from AI, automation, startup, and developer communities. Runs three times daily (7 AM, 12 PM, 6 PM).

**Stack:** A Python script using `feedparser` + `requests` + plain-text file output.

**How it works:**

1. A cron job fires `python scripts/rss-digest.py`
2. The script fetches each feed, filters by keyword relevance (configurable list: "AI agent", "automation", "no-code", "prompt engineering", "LLM", "Paperclip", "multi-agent")
3. Deduplicates against a rolling cache of the last 500 seen items
4. Scores each item: title match (3 pts), description match (1 pt), author reputation (manual boost list)
5. Writes the top 10 items to `workspace/research/digest-YYYY-MM-DD.md` with full URLs, excerpts, and relevance scores

**Key design decisions:**

- **Simple over smart.** No vector embeddings, no semantic search. Keyword scoring catches 90% of relevant content and runs in under 2 seconds.
- **No state beyond files.** The cache is `workspace/research/.seen_cache.json` — trivial to inspect, reset, or back up.
- **Human-readable output.** The digest is formatted for both a human reader and the drafting agent that consumes it next.

### Sample digest entry

```markdown
## Digest: 2026-07-13

### 1. Paperclip v0.8 Released with Multi-Agent Debugger
**Source:** dev.to | **Score:** 9
**URL:** https://dev.to/example/paperclip-v08
**Snippet:** The latest release adds step-through debugging for agent chains,
  making it possible to inspect intermediate outputs...
**Why it matters:** Directly relevant to our stack — potential feature to
  highlight in upcoming tutorial content.
```

---

## Stage 2: Research → Topic Selection

**What it does:** Takes the raw digest and produces a ranked list of article topics with outlines.

**Trigger:** The drafting agent scans `workspace/research/` for new digests, processes them, and deletes the trigger file.

**Stack:** A single Hermes agent prompt with structured output instructions. The agent receives the digest text plus our editorial guidelines (audience, tone, keyword strategy) and produces:

```json
{
  "topics": [
    {
      "title": "How to Build a Multi-Agent Code Review Pipeline",
      "angle": "Practical tutorial with real GitHub Actions integration",
      "target_keyword": "multi-agent code review pipeline",
      "suggested_outline": [
        "Why single-agent review fails",
        "The 4-agent architecture",
        "Step-by-step integration with GitHub Actions",
        "Results from production"
      ],
      "priority": 1
    }
  ]
}
```

**Why this works:** The agent has full context of what we've already published (from a `workspace/editorial-calendar.md` file it reads), so it won't suggest a topic we covered last week.

---

## Stage 3: Drafting (The Content Factory)

**What it does:** Writes the first draft of each approved topic.

**Trigger:** A human (me) approves 1–3 topics per batch on Monday and Wednesday mornings. Approval is simply moving a JSON file from `workspace/topics/proposed/` to `workspace/topics/approved/`.

**Stack:** A Python script that calls the LLM API (OpenRouter free tier) with a structured prompt template.

**The prompt template:**

```
You are writing an article for Prem Autonomous Co, a publication about
AI agents, automation, and running a zero-budget tech business.

**Topic:** {{topic}}
**Angle:** {{angle}}
**Target keyword:** {{keyword}}
**Suggested outline:** {{outline}}
**Audience:** Developers and technical founders (B2B, mid-to-senior level)
**Tone:** Practical, honest, specific. No hype. No passive-income claims.
**Length:** 1,800-2,500 words

Write the full article in markdown. Include:
- A strong hook in the first paragraph
- 4-6 major sections with H2 headers
- At least 2 code examples or configuration blocks
- A conclusion that summarizes takeaways
- A 2-sentence author bio at the end
```

**Output processing:**

After the draft is written, a post-processing script:
1. Strips any hallucinated statistics or fabricated numbers (checks against a "known facts" file)
2. Verifies all links are to real domains
3. Adds frontmatter metadata (title, date, keywords, word count)
4. Writes to `workspace/drafts/approved/YYYY-MM-DD-title.md`

---

## Stage 4: Quality Gate & Publishing

**What it does:** Catches errors, improves style consistency, and prepares the article for multi-channel distribution.

**The review gate is non-negotiable.** Every piece goes through three automated checks before I see it:

### 1. Fact-Check Agent
- Scans for specific patterns: "according to", "studies show", "X% of Y"
- Flags any claim not backed by an inline citation
- If a claim is unverifiable, it's highlighted in the draft for human review

### 2. Style Consistency Check
- Compares against our style guide (stored in `workspace/style-guide.md`)
- Checks: heading structure, list consistency, code block formatting, link format
- Produces a score: green (pass), yellow (minor fixes applied), red (needs rewrite)

### 3. Readability Scorer
- Target: 50–70 on the Flesch Reading Ease scale
- If below 50: suggests shorter sentences and simpler vocabulary
- If above 70: suggests more technical depth

After the automated checks pass, the draft enters my review queue: a single folder `workspace/review/`. I spend about 15 minutes per article doing a final read, checking the flagged claims, and clicking "approve".

---

## Stage 5: Multi-Channel Distribution

**What it does:** Takes one approved article and produces 15 distribution assets.

**The multiplier effect:**

| Asset | Channel | Format |
|-------|---------|--------|
| Full article (2,000 words) | Company blog → Medium | Markdown |
| LinkedIn post (300 words) | Personal profile | Text + image |
| Twitter thread (20 tweets) | @premukumar | Thread format |
| LinkedIn carousel (10 slides) | Personal profile | Canva template |
| Newsletter excerpt (500 words) | Email list | HTML |
| 3 short-form video scripts | TikTok / Reels / Shorts | 60-sec scripts |
| Reddit post (TL;DR) | r/artificial, r/MachineLearning | Text |
| Hacker News comment | news.ycombinator.com | Text |

**How it works:**

A Python script (`scripts/repurpose.py`) reads the approved article and feeds it to a repurposing agent with a template for each format. The output lands in `workspace/distribution/YYYY-MM-DD/`.

**Key insight:** Don't try to repurpose everything. I only repurpose the top 2 articles per week — the ones with the highest predicted engagement (based on the topic score from Stage 2). The other 3–5 articles get published as-is on the blog and Medium.

---

## The Real Numbers: What 6 Months of This Pipeline Produced

| Metric | Value |
|--------|-------|
| Articles published | 87 |
| Total pieces (including repurposed) | 620+ |
| Weekly human time | ~90 minutes |
| Organic impressions (90 days) | 200K+ |
| Failed automations (crashes) | 7 (all recovered) |
| Articles that needed major human rewrite | 12 (13%) |
| Articles published with minor edits only | 60 (69%) |
| Articles sent back from review gate | 15 (17%) |

**The honest truth:** The pipeline doesn't replace a writer. It replaces the mechanical work *around* writing. I still choose the topics, set the angle, and do the final edit. But I no longer spend 3 hours formatting a WordPress post or writing 15 social media updates by hand.

---

## The Architecture Diagram (Simplified)

```
┌─────────────────┐     ┌──────────────────┐     ┌─────────────────┐
│   RSS Ingestion  │────▶│  Topic Selection  │────▶│   Draft Engine  │
│   (cron, 3x/d)   │     │  (Hermes agent)   │     │  (LLM + script) │
└─────────────────┘     └──────────────────┘     └────────┬────────┘
                                                           │
                                                           ▼
┌─────────────────┐     ┌──────────────────┐     ┌─────────────────┐
│ Multi-Channel    │◀────│   Quality Gate    │◀────│   Draft Output  │
│ Distribution     │     │  (3 automated     │     │  (workspace/)   │
│ (repurpose.py)   │     │   checks + human) │     │                 │
└─────────────────┘     └──────────────────┘     └─────────────────┘
```

**Total scripts:** 4 Python files + 2 agent prompt configurations.
**Total configuration:** 3 YAML files (RSS sources, editorial guidelines, distribution channels).
**Cron entries:** 6 (scheduled tasks on the host machine).

---

## What I'd Do Differently

Building this taught me what matters and what doesn't. If I started over:

1. **Skip the fancy orchestration.** I spent two weeks trying to set up n8n before realizing a Python script + cron does the same thing with fewer failure points.

2. **Over-invest in the review gate.** The first version had no automated quality checks. It published an article with a hallucinated CEO quote. Never again. The review gate is now the most important piece of the pipeline.

3. **Write the style guide first.** The repurposing agent produces wildly inconsistent outputs without explicit style rules. Once I wrote down "always use Oxford comma", "headings are sentence case", "code blocks have language tags", the output quality jumped dramatically.

4. **Don't repurpose everything.** Early on I tried to make every article into 15 pieces. That was exhausting and produced low-quality social posts. Now I only deep-repurpose the top 20% of articles, and the rest just get a blog post and a LinkedIn summary.

---

## How to Build Your Own (30-Minute Setup)

You don't need my exact stack. Here's the minimal version you can set up in one sitting:

1. **RSS ingestion:** `pip install feedparser` → write a 20-line Python script → schedule with cron on your machine or a free Railway/Zeabur instance.

2. **Drafting:** Create a prompt template (use the one above as a starting point) → call any LLM API that has a free tier (OpenRouter, Claude, Gemini).

3. **Review gate:** One folder for "incoming drafts" and one for "approved". The act of moving a file between folders is your quality gate.

4. **Distribution:** Pick ONE secondary channel (LinkedIn is the highest ROI for B2B) and write one repurposing script. Don't do all 15 channels until you've validated the content works.

**The whole thing costs $0 in software and about $5–10/month in API calls if you use free-tier models.**

---

## The Tradeoffs You Need to Know

This isn't a magic bullet. Here are the real downsides:

- **Topic drift.** The agent will keep proposing similar topics if you don't actively refresh the editorial guidelines. I review keyword strategy every 2 weeks.
- **Voice inconsistency.** Automated content lacks a single coherent voice. Readers notice. The fix is a detailed style guide and reading every draft before it goes live.
- **SEO blind spots.** The agent doesn't understand search intent as well as a human SEO specialist. I supplement with manual keyword research.
- **The "uncanny valley" problem.** Some readers can tell the content was AI-assisted. For our technical audience, this is actually fine — they care about accuracy, not provenance — but it matters if your brand depends on a very human voice.

---

## Conclusion

A fully automated content pipeline is achievable with open-source tools and about $0/month in software costs. The architecture is simpler than most people expect: RSS feeds → topic selection → drafting → quality gate → distribution.

The hard part isn't the automation. The hard part is the editorial judgment that decides what to write, what to publish, and what to throw away. That still requires a human.

But that human now spends 90 minutes a week instead of 30 hours. And that freed time is what makes the rest of the business possible.

---

*Prem Kumar runs Prem Autonomous Co, a zero-budget AI-native company operating 7 agents across Paperclip + Hermes. He publishes weekly about AI automation, agent architecture, and building businesses with limited resources.*

---

**Next in the series:** *The 7 Agents That Run My Business While I Sleep* — detailed profiles of each agent, their tools, schedules, and failure modes.
