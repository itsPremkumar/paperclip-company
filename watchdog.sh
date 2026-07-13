#!/usr/bin/env bash
# Paperclip watchdog — restarts the server if down
# Called by Hermes cron every 5 minutes

HEALTH_URL="http://localhost:3100/api/health"

# Check if server is responding
if ! curl -sf "$HEALTH_URL" > /dev/null 2>&1; then
  echo "[$(date)] Paperclip server DOWN — restarting..."
  export OPENROUTER_API_KEY="${OPENROUTER_API_KEY:-}"
  # Key must come from the environment; never hardcode (GitHub secret scanning blocks it).
  export NODE_OPTIONS="--max-old-space-size=8192"
  cd /c/one/paperclip-company && cmd.exe /c "C:\one\paperclip-company\run-server.bat" > /dev/null 2>&1 &
  echo "[$(date)] Restart initiated — PID=$!"
else
  echo "[$(date)] Paperclip server UP — OK"
fi
