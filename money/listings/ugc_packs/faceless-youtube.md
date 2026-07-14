# I will produce faceless YouTube/TikTok automation videos

**Price:** $120/gig
**Margin:** —%
**Tags:** faceless youtube, tiktok automation, ai video, edge tts, remotion, content creator, passive income, shorts

## What you get
A done-for-you, automated solution built on 100% free/open-source tooling.
No recurring SaaS fees — the system runs on your own infrastructure.

## Delivery process
- **Basic** ($30, 3 days): 1 video; 1 workflow; Email support
- **Standard** ($120, 5 days): Up to 5 videos; Setup + test; Loom walkthrough; 7-day support
- **Premium** ($240, 7 days): Unlimited videos; Full system; Monthly retainer option; Priority support

## Why this works
- Self-hosted stack (n8n + free tools) → 90–99% profit margin
- Every deliverable is generated and delivered automatically
- You own the system; scale to unlimited clients

## FAQ
**Q: Do I need to pay for software?**
A: No. Everything runs on free open-source tools (n8n, Chatwoot, Stirling-PDF, Listmonk).

**Q: Is this a one-time build or ongoing?**
A: Both. One-time setup + optional monthly retainer for monitoring/optimization.

**Q: Can you customize for my niche?**
A: Yes — every package is generated from a template and tuned to your vertical.

## Technical spec (for the build)
```json
{
 "name": "deliver-ugc-faceless-youtube",
 "nodes": [
  {
   "parameters": {},
   "name": "Webhook (intake)",
   "type": "n8n-nodes-base.webhook",
   "typeVersion": 1,
   "position": [
    0,
    0
   ]
  },
  {
   "parameters": {},
   "name": "Render video (Remotion/CogVideoX)",
   "type": "n8n-nodes-base.code",
   "typeVersion": 1,
   "position": [
    300,
    0
   ]
  },
  {
   "parameters": {},
   "name": "Deliver + notify",
   "type": "n8n-nodes-base.emailSend",
   "typeVersion": 1,
   "position": [
    600,
    0
   ]
  }
 ],
 "connections": {
  "Webhook (intake)": {
   "main": [
    [
     {
      "node": "Render video (Remotion/CogVideoX)",
      "type": "main",
      "index": 0
     }
    ]
   ]
  },
  "Render video (Remotion/CogVideoX)": {
   "main": [
    [
     {
      "node": "Deliver + notify",
      "type": "main",
      "index": 0
     }
    ]
   ]
  }
 },
 "note": "Tools: Edge-TTS + Remotion + your youtube-content skill \u2014 all free/self-hosted. Replace code node with your render logic."
}
```
