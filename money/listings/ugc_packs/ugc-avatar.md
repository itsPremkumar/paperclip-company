# I will generate AI UGC avatar ad videos (no actors, no studio)

**Price:** $300/gig
**Margin:** —%
**Tags:** ugc ads, ai video, facebook ads, tiktok ads, ai avatar, remotion, cogvideox, ad creative

## What you get
A done-for-you, automated solution built on 100% free/open-source tooling.
No recurring SaaS fees — the system runs on your own infrastructure.

## Delivery process
- **Basic** ($75, 3 days): 1 video; 1 workflow; Email support
- **Standard** ($300, 5 days): Up to 5 videos; Setup + test; Loom walkthrough; 7-day support
- **Premium** ($600, 7 days): Unlimited videos; Full system; Monthly retainer option; Priority support

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
 "name": "deliver-ugc-ugc-avatar",
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
 "note": "Tools: Remotion + Edge-TTS + CogVideoX + Flowise (local) \u2014 all free/self-hosted. Replace code node with your render logic."
}
```
