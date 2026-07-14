# I will automate your WhatsApp customer support with an AI agent

**Price:** $800/gig
**Margin:** —%
**Tags:** whatsapp support, ai chatbot, customer service automation, chatwoot, baileys, n8n, helpdesk automation, rag

## What you get
A done-for-you, automated solution built on 100% free/open-source tooling.
No recurring SaaS fees — the system runs on your own infrastructure.

## Delivery process
- **Basic** ($200, 3 days): Single flow; 1 workflow; Email support
- **Standard** ($800, 5 days): Setup + test; Up to 3 flows; Loom walkthrough; 7-day support
- **Premium** ($1600, 7 days): Full system; Unlimited flows; Monthly retainer option; Priority support

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
 "name": "deliver-wa-support-agent",
 "nodes": [
  {
   "parameters": {},
   "name": "Baileys (WhatsApp intake)",
   "type": "n8n-nodes-base.webhook",
   "typeVersion": 1,
   "position": [
    0,
    0
   ]
  },
  {
   "parameters": {},
   "name": "Agent / Chatwoot logic",
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
  "Baileys (WhatsApp intake)": {
   "main": [
    [
     {
      "node": "Agent / Chatwoot logic",
      "type": "main",
      "index": 0
     }
    ]
   ]
  },
  "Agent / Chatwoot logic": {
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
 "note": "Tools: Baileys + Chatwoot + n8n + local LLM + your doc-extractor skill \u2014 all free. Replace code node with your agent logic. Baileys repo: https://github.com/WhiskeySockets/Baileys"
}
```
