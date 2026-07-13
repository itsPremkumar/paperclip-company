@echo off
cd /d C:\one\paperclip-company\paperclip\server
set PORT=3100
set HOST=0.0.0.0
set SERVE_UI=true
set BETTER_AUTH_SECRET=paperclip-dev-secret-change-me
set PAPERCLIP_DEPLOYMENT_MODE=authenticated
set PAPERCLIP_DEPLOYMENT_EXPOSURE=private
set PAPERCLIP_PUBLIC_URL=http://localhost:3100
set PAPERCLIP_HOME=C:\one\paperclip-company\data\paperclip
set PAPERCLIP_MIGRATION_AUTO_APPLY=true
set DATABASE_URL=postgres://paperclip:paperclippw@localhost:5432/paperclip
REM Add Python to PATH so the hermes_local adapter probe finds python3 (Hermes still uses its own venv)
set OPENROUTER_API_KEY=%OPENROUTER_API_KEY%
REM Key injected from environment; never hardcode (GitHub secret scanning blocks it).
set NODE_OPTIONS=--max-old-space-size=8192
set PATH=C:\Users\PREM KUMAR\AppData\Local\Programs\Python\Python312;%PATH%
C:\one\paperclip-company\paperclip\node_modules\.bin\tsx src/index.ts >> C:\one\paperclip-company\tsx-out.log 2>&1
echo SERVER_EXIT=%ERRORLEVEL% >> C:\one\paperclip-company\tsx-out.log
