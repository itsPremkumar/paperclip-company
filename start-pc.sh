#!/bin/bash
cd /c/one/paperclip-company/paperclip/server
export PORT=3100 HOST=0.0.0.0 SERVE_UI=true
export BETTER_AUTH_SECRET=paperclip-dev-secret-change-me
export PAPERCLIP_DEPLOYMENT_MODE=authenticated
export PAPERCLIP_DEPLOYMENT_EXPOSURE=private
export PAPERCLIP_PUBLIC_URL=http://localhost:3100
export PAPERCLIP_HOME=C:/one/paperclip-company/data/paperclip
export PAPERCLIP_MIGRATION_AUTO_APPLY=true
export DATABASE_URL=postgres://paperclip:***@localhost:5432/paperclip
export NODE_OPTIONS=--max-old-space-size=4096
if [ -z "$OPENROUTER_API_KEY" ]; then
  OR=$(grep -E '^OPENROUTER_API_KEY=' "C:/Users/PREM KUMAR/AppData/Local/hermes/.env" 2>/dev/null | head -1 | cut -d= -f2-)
  [ -n "$OR" ] && export OPENROUTER_API_KEY="$OR"
fi
exec /c/one/paperclip-company/paperclip/node_modules/.bin/tsx src/index.ts
