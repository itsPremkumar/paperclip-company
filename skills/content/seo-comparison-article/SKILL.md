---
name: seo-comparison-article
category: content
description: >-
  Repeatable skill for authoring evergreen "X vs Y vs Z" comparison articles
  into revenue/blog/ that the income-engine blog generator picks up
  automatically. Scan existing slugs for a missing comparison axis, reuse the
  canonical front-matter schema, then ship a 30-second verdict + side-by-side
  table + cross-links + product funnel. Zero human gate, no money movement.
state: active
---

# Author an Evergreen Comparison SEO Article

## When to use
You want continuous, low-risk, compounding SEO work that fills the content
funnel between heavier ticks. The autonomy loop has run this pattern 20+ times
across five axis families (automation tools, frameworks, models, channels/media,
and infra/dev-tooling). It is the safest agent-executable content task: it needs
no model inference, no money, and no human approval. See the **Coverage Matrix**
below for the live list of covered axes and the backlog of gaps to fill next.

## Inputs
- `revenue/blog/*.md` — the existing article corpus (the source of truth for
  what axes are already covered).
- The canonical front-matter schema (below) — the blog generator reads it to
  render the post, so matching it exactly is what makes the file publishable
  without manual edits.
- A list of paid products to funnel to (see `income-engine/gumroad/products/`
  and the catalog): e.g. `monetization-kit`, `zero-to-10k-ai-agents`,
  `ai-content-machine-blueprint`.

## Steps
1. **Scan for a missing comparison axis.** List existing slugs and group them by
   axis type. The loop has now covered 20+ comparison axes across five families
   (see **Coverage Matrix** below) — do NOT re-author a covered slug. Pick an
   Pick an UNSATISFIED axis from the backlog (e.g. a *landing-page builders* quartet
   (Unbounce vs Leadpages vs Instapage vs Carrd), a *community platforms* quartet
   (Circle vs Skool vs Mighty Networks vs Discord), a *form/survey tools* quartet
   (Typeform vs Tally vs Fillout vs Jotform), a *web analytics* quartet
   (Plausible vs Umami vs Fathom vs GA4), or an *API clients* quartet
   (Postman vs Insomnia vs Bruno vs Hoppscotch)) or propose a fresh high-intent axis.
   Prefer the gap with the highest
   search volume and lowest existing competition in the corpus.
   2. **Reuse the canonical front-matter block verbatim** (YAML between `---`
   fences). Required keys, in order:
   ```yaml
   ---
   title: "X vs Y vs Z: <question> in 2026"
   description: "<no-hype one-liner with the contenders and the payoff>"
   slug: x-vs-y-vs-z-2026
   date: "2026-07-14"
   niche: "<contender family + audience>"
   tags: ["x", "y", "z", "automation", "comparison"]
   author: "Prem Autonomous Co — Hermes Agent Team"
   ---
   ```
   The `slug` MUST equal the filename stem or the generator mis-links it.
3. **Open with a 30-second verdict.** 2–4 bullets, one per contender:
   "Pick X if … ; Pick Y if … ; Pick Z if …". This is the snippet search
   engines and LLMs lift for AEO/GEO answers.
4. **Add a side-by-side comparison table** (markdown `|` table) across the
   dimensions buyers actually care about: price/free tier, self-hosting, ease,
   best-fit use case, lock-in risk. Keep it skimmable.
5. **Cross-link 6–13 existing articles** using relative `./slug.md` links in
   prose. Each link should be contextually motivated ("this pairs with our
   <topic> guide"), not a footer dump. Cross-links are what compound the
   funnel — never ship a standalone island.
6. **Funnel to at least one paid product** near the end ("if you want the
   done-for-you version, see <product>"). Name the product; do not embed buy
   links or price (publish/payout is human-gated).
7. **Save as** `revenue/blog/<slug>.md` and verify the file name == `slug`.
8. **Scan for secrets** before any commit (see guardrails).

## Guardrails
- Agent writes the article only. **Gumroad publish, pricing, and payouts stay
  HUMAN-GATED** (Constitution S0) — the loop never lists or moves money, and
  must never embed a checkout/price link in the body.
- Keep the front-matter schema EXACTLY as specified; a drifted key breaks the
  generator's parser and the post goes unpublished silently.
- No secrets, API keys, `.env`, or credentials ever belong in a blog article.
- Prefer extending the funnel (cross-links + product funnel) over inventing a
  brand-new angle — consistency beats novelty for SEO.

## Coverage Matrix (live as of 2026-07-16)

Covered comparison axes (slug == filename, all in `revenue/blog/`):

- **Automation tools:** `n8n-vs-make-vs-zapier-2026`
- **Frameworks:** `langgraph-vs-autogen-vs-crewai-vs-n8n-2026`
- **Models/LLMs:** `chatgpt-vs-claude-vs-gemini-vs-llama-2026`
- **Answer engines:** `perplexity-vs-google-ai-mode-vs-microsoft-copilot-vs-you-2026`
- **Inference/API gateways:** `openrouter-vs-together-vs-replicate-vs-groq-2026`
- **No-code agent builders:** `dify-vs-flowise-vs-langflow-vs-botpress-2026`
- **Coding assistants:** `cursor-vs-windsurf-vs-copilot-vs-claude-code-2026`
- **App builders (prompt-to-app):** `bolt-vs-lovable-vs-v0-vs-replit-2026`
- **Vector DBs:** `pinecone-vs-chroma-vs-qdrant-vs-weaviate-2026`
- **Image generators:** `midjourney-vs-dalle-vs-stable-diffusion-vs-flux-2026`
- **Video generators:** `runway-vs-pika-vs-synthesia-vs-heygen-2026`
- **TTS / voice generators:** `elevenlabs-vs-cartesia-vs-playht-vs-openai-tts-2026`
- **STT / speech-to-text:** `whisper-vs-assemblyai-vs-deepgram-vs-rev-ai-2026`
- **Music generators:** `suno-vs-udio-vs-aiva-vs-boomy-2026`
- **Presentation makers:** `gamma-vs-beautiful-ai-vs-tome-vs-slidesai-2026`
- **Writing assistants:** `jasper-vs-copy-ai-vs-writesonic-vs-rytr-2026`
- **Meeting assistants:** `otter-vs-fireflies-vs-fathom-vs-tldv-2026`
- **SEO content tools:** `surfer-seo-vs-clearscope-vs-frase-vs-marketmuse-2026`
- **Newsletter/creator-email platforms:** `beehiiv-vs-substack-vs-convertkit-vs-ghost-2026`
- **Channels/media:** `faceless-youtube-vs-tiktok-vs-newsletter-2026`
- **CRM / sales:** `hubspot-vs-salesforce-vs-pipedrive-vs-zoho-2026`
- **Customer-support helpdesk:** `zendesk-vs-freshdesk-vs-help-scout-vs-gorgias-2026`
- **Email marketing / ESP automation:** `mailchimp-vs-klaviyo-vs-activecampaign-vs-brevo-2026`
- **E-commerce platforms:** `shopify-vs-woocommerce-vs-bigcommerce-vs-squarespace-2026`
- **AI design tools:** `canva-vs-figma-vs-adobe-express-vs-designs-ai-2026`
- **No-code databases:** `airtable-vs-nocodb-vs-baserow-vs-supabase-2026`
- **Password / secrets managers:** `1password-vs-bitwarden-vs-dashlane-vs-keeper-2026`
- **Project management:** `linear-vs-asana-vs-clickup-vs-height-2026`
- **AI note / knowledge tools:** `notion-ai-vs-mem-vs-reflect-vs-capacities-2026`
- **Scheduling / calendar:** `calendly-vs-cal-com-vs-motion-vs-reclaim-2026`
- **Social media management:** `buffer-vs-hootsuite-vs-later-vs-sprout-social-2026`
- **Customer data / product analytics:** `segment-vs-rudderstack-vs-amplitude-vs-posthog-2026`
- **SEO keyword research:** `ahrefs-vs-semrush-vs-moz-vs-ubersuggest-2026`
- **Website builders:** `framer-vs-webflow-vs-wix-vs-10web-2026`
- **LLM observability / eval:** `langsmith-vs-langfuse-vs-phoenix-vs-helicone-2026`
- **Hosting / deploy:** `vercel-vs-netlify-vs-railway-vs-render-2026`
- **Course / digital-product platforms:** `kajabi-vs-teachable-vs-thinkific-vs-podia-2026`

Non-comparison blueprints (same funnel, different format) live alongside these,
e.g. `ai-agent-monetization-2026`, `build-ai-lead-generation-system-2026`,
`how-to-build-ai-voice-agent-2026`, and the vertical piece
`income-engine/content/ai-agents-for-appointment-scheduling-and-booking-automation.md`.

### Suggested next axes (backlog — not yet covered)
- ~~AI website builders: Framer vs Webflow vs Wix ADI vs 10Web~~ — COVERED → `framer-vs-webflow-vs-wix-vs-10web-2026` (2026-07-15, TICK-39)
- ~~AI design tools: Canva vs Figma vs Adobe Express vs Designs.ai~~ — COVERED → `canva-vs-figma-vs-adobe-express-vs-designs-ai-2026` (2026-07-16)
- ~~LLM observability / eval: LangSmith vs Langfuse vs Phoenix vs Helicone~~ — COVERED → `langsmith-vs-langfuse-vs-phoenix-vs-helicone-2026` (2026-07-16)
- ~~AI note / knowledge tools: Notion AI vs Mem vs Reflect vs Capacities~~ — COVERED → `notion-ai-vs-mem-vs-reflect-vs-capacities-2026` (2026-07-16)
- **Fine-tuning / ML platforms:** Together Fine-tune vs OpenAI Fine-tuning vs
  OctoAI vs Predibase (distinct from the inference-API axis already covered)

### Extended backlog (added 2026-07-16) — second wave of high-intent gaps
These are role/layer cuts that sit beside the first wave and keep the
"X vs Y vs Z" format inexhaustible. Pick by search volume × corpus-gap:

- ~~Customer data / product analytics: Segment vs RudderStack vs Amplitude vs PostHog~~ — COVERED → `segment-vs-rudderstack-vs-amplitude-vs-posthog-2026` (2026-07-16, TICK-53)
- ~~Social media management: Buffer vs Hootsuite vs Later vs Sprout Social~~ — COVERED → `buffer-vs-hootsuite-vs-later-vs-sprout-social-2026` (2026-07-16, TICK-52)
- **Translation / localization:** DeepL vs Google Translate vs Lilt vs Unbabel
- **AI spreadsheet / data analysis:** Rows vs GRID vs Equals vs Quadratic
- **Form / survey builders:** Typeform vs Jotform vs Fillout vs Formstack
- ~~Scheduling / calendar: Calendly vs Cal.com vs Motion vs Reclaim~~ — COVERED → `calendly-vs-cal-com-vs-motion-vs-reclaim-2026` (2026-07-16)
- **Project management:** Linear vs Asana vs ClickUp vs Height
- **Logo / brand design:** Looka vs Brandmark vs Tailor Brands vs LogoAI
- ~~No-code database: Airtable vs NocoDB vs Baserow vs Supabase~~ — COVERED → `airtable-vs-nocodb-vs-baserow-vs-supabase-2026` (2026-07-16)
- **Website chat / chatbot:** Intercom vs Drift vs Tidio vs Crisp

### Third-wave backlog (added 2026-07-16) — non-overlapping B2B SaaS cuts
These round out the comparison surface beside wave 1 + 2 so future healthy-RAM
ticks have a deep, non-duplicating bank of axes. Each is a distinct *cut* from the
email/newsletter, analytics, and chat waves above (different buyer job, not a
re-skin of an already-covered quartet):

- ~~Email marketing / ESP automation: Mailchimp vs Klaviyo vs ActiveCampaign vs Brevo~~ — COVERED → `mailchimp-vs-klaviyo-vs-activecampaign-vs-brevo-2026` (2026-07-16)
- ~~Cloud / edge hosting (dev infra): Vercel vs Netlify vs Railway vs Render~~ — COVERED → `vercel-vs-netlify-vs-railway-vs-render-2026` (2026-07-16)
- ~~AI customer-support helpdesk: Zendesk vs Freshdesk vs Help Scout vs Gorgias~~ — COVERED → `zendesk-vs-freshdesk-vs-help-scout-vs-gorgias-2026` (2026-07-16)
- ~~E-commerce platforms: Shopify vs WooCommerce vs BigCommerce vs Squarespace~~ — COVERED → `shopify-vs-woocommerce-vs-bigcommerce-vs-squarespace-2026` (2026-07-16)
- **Landing-page builders:** Unbounce vs Leadpages vs Instapage vs Systeme
- **Knowledge-base / docs tools:** Confluence vs GitBook vs Docusaurus vs Outline
- ~~Password / secrets managers: 1Password vs Bitwarden vs Dashlane vs Keeper~~ — COVERED → `1password-vs-bitwarden-vs-dashlane-vs-keeper-2026` (2026-07-16)
- **Video conferencing:** Zoom vs Google Meet vs Microsoft Teams vs Whereby
- **AI video editing / short-form:** Descript vs CapCut vs Opus Clip vs Veed
- **Webinar / live-event platforms:** WebinarJam vs Demio vs Livestorm vs BigMarker

When RAM is healthy (≥ 300 MB) pick a backlog axis and author the comparison.
When RAM is low, run this lightweight **self-improve** path instead (harden this
skill, add a lessons-learned entry) — never author under memory pressure.

## Why this matters
Comparison queries ("X vs Y") are high-intent, high-volume, and low-competition
relative to broad "how to" content. Because the loop already owns a deep,
cross-linked corpus, each new comparison article inherits link equity and routes
readers toward (human-gated) products. It is pure text, costs zero to produce,
and is fully reversible — the ideal autonomous-tick task.

## See also
- `skills/automation/package-digital-product.md` (turn the funnel into priced assets)
- `revenue/blog/n8n-vs-make-vs-zapier-2026.md` (reference implementation)
- `revenue/blog/chatgpt-vs-claude-vs-gemini-vs-llama-2026.md` (model-axis example)
- `knowledge-base/lessons-learned.md` (TICK-13/TICK-14/TICK-15 derivations)
