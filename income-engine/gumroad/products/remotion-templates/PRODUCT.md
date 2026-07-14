# 🎬 Remotion Short-Form Video Template Pack — 12 Production-Ready Video Templates

*The exact template pack we use to run the Automated Video Generator (AVG) — a Remotion-based pipeline that produces short-form videos on autopilot. 12 done-for-you templates across 12 niches, plus full voice, styling, and timing configs so you can render real MP4s the same day.*

---

## 🧭 What This Is

A complete template pack for the AVG (Automated Video Generator). These are the actual templates Prem Autonomous Co uses to publish short-form content at zero cost — no camera, no editor, no monthly SaaS. Point Remotion at `input-scripts.json` and render.

---

## 📦 What's Inside

| File | What it does |
|------|--------------|
| `input-scripts.json` | The full 12-template database — hook, full script, orientation, voice, text overlay flag for each. |
| `voices-config.json` | 7 free Edge-TTS voices (no API key), orientation presets (1080×1920 / 1920×1080), text style, transition timing, and royalty-free music pointers. |

### 🎬 The 12 Templates

| # | Template | Niche | Style |
|---|----------|-------|-------|
| 1 | Space Facts | Science | Educate + Amaze |
| 2 | Ocean Mysteries | Nature | Curiosity Hook |
| 3 | Productivity Hacks | Self-Improvement | Actionable Tips |
| 4 | AI News Flash | Tech | Timely Updates |
| 5 | Coding Tips | Developer | Quick Wins |
| 6 | Startup Stories | Business | Narrative |
| 7 | Book Summaries | Education | Value in 60s |
| 8 | Fitness Tips | Health | Quick Workouts |
| 9 | Language Lessons | Education | Daily Practice |
| 10 | History Shorts | Education | Surprising Facts |
| 11 | Tech Reviews | Tech | Honest Opinions |
| 12 | Motivation | Self-Help | Inspirational |

---

## 🔧 Technical Specs

- **Format:** JSON + Markdown (drop-in for AVG v5.x / Remotion 4.x)
- **Output:** MP4 (H.264), 1080×1920 portrait or 1920×1080 landscape
- **Audio:** Edge-TTS — free, no API key required
- **Stock media:** Pexels / Pixabay / Openverse free tiers

### Sample Template Structure
```json
{
  "id": "template-space-facts",
  "title": "3 Space Facts That Blow Minds",
  "script": "Space is stranger than you think... [Visual: ...]",
  "orientation": "portrait",
  "voice": "en-US-GuyNeural",
  "showText": true,
  "defaultVideo": "default.mp4"
}
```

---

## 🛡️ Notes

- Every script ships with a `[Visual: ...]` cue so you can map stock clips without guessing.
- Voices are free Edge-TTS presets — swap any one for your brand voice in seconds.
- Built and used in production by Prem Autonomous Co. Marginal cost to deliver: zero — it's a file.

*Free template outline lives on GitHub. This pack is the filled-in, ready-to-render kit — same system, cleaned up and deployable today.*
