#!/usr/bin/env bash
# RAM-safe Paperclip server launcher (verified per infra/paperclip-control-guide.md)
# Forward slashes only (git-bash pitfall). No exec (avoids detach). DB uses trust auth on localhost.
set -u
cd /c/one/paperclip-company/paperclip/server

export PORT=3100
export HOST=0.0.0.0
export SERVE_UI=true
export PAPERCLIP_DEPLOYMENT_MODE=authenticated
export PAPERCLIP_DEPLOYMENT_EXPOSURE=private
export PAPERCLIP_PUBLIC_URL=http://localhost:3100
export PAPERCLIP_HOME=/c/one/paperclip-company/data/paperclip
export PAPERCLIP_MIGRATION_AUTO_APPLY=true
# Trust auth on localhost => password value is irrelevant for connection
export DATABASE_URL="postgres://paperclip:paperclip@localhost:5432/paperclip"
export BETTER_AUTH_SECRET=paperclip-dev-secret-change-me
export NODE_OPTIONS="--max-old-space-size=1500"
export PATH="/c/Users/PREM KUMAR/AppData/Local/Programs/Python/Python312:$PATH"

# Pull OPENROUTER_API_KEY from Hermes env if not already in environment
if [ -z "${OPENROUTER_API_KEY:-}" ]; then
  OR=$(grep -E '^OPENROUTER_API_KEY=' "/c/Users/PREM KUMAR/AppData/Local/hermes/.env" 2>/dev/null | head -1 | cut -d= -f2-)
  [ -n "$OR" ] && export OPENROUTER_API_KEY="$OR"
fi

echo "[start-pc-now] launching at $(date)"
echo "[start-pc-now] node: $(command -v node) ; OPENROUTER_API_KEY set: ${OPENROUTER_API_KEY:+yes}${OPENROUTER_API_KEY:-no}"
exec node node_modules/tsx/dist/cli.mjs src/index.ts
