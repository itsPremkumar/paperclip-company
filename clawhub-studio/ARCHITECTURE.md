# Architecture

ClawHub Studio is a **local-first, single-binary** web app with no external services.

## Layers (top → bottom)
```
web/ (SPA)  ──HTTP/JSON──▶  server.py (REST + static host)
                                   │
              ┌────────────────────┼────────────────────┐
              ▼                    ▼                     ▼
        skills.py            testrunner.py          publish.py
     (domain logic)       (run self-test)        (clawhub CLI)
              │                                         │
              └──────────────▶ db.py ◀──────────────────┘
                            (SQLite repo)
                                  │
                              auth.py
                       (HMAC session tokens)
```

- **server.py** — `ThreadingHTTPServer`. Routes `/api/*` to JSON handlers, everything else
  to the SPA (with a path-traversal guard). No framework.
- **db.py** — thin SQLite repository. Schema is versioned (`PRAGMA user_version`) so
  migrations are explicit. Three tables: `skill`, `version`, `run`.
- **auth.py** — login mints a signed token (`<exp>.<nonce>.<hmac>`). The secret is a random
  file in the data dir (or `CLAWHUB_STUDIO_SECRET`). No password store.
- **skills.py** — pure domain logic: parse/serialize `SKILL.md` frontmatter, validate
  manifests, bump semver, derive status (`draft`/`ready`/`published`). No I/O.
- **testrunner.py** — runs `python <tool>.py self-test` (or the portfolio harness) and
  returns structured results. Subprocess only.
- **publish.py** — shells out to the local `clawhub` CLI. Dry-run by default.

## Invariants
- Every skill version carries a JSON manifest + a status.
- A run is recorded against a `(skill, version)` pair; the UI shows history.
- No secret ever leaves the data dir; `publish` uses the already-authed `clawhub` CLI.

## Why stdlib-only
Runs on the constrained host (low RAM, no pip installs). Zero CVE surface from third-party
web frameworks. Portable: copy the folder, run `python -m studio serve`.

## Testing
`tests/` is a real `unittest` suite (31 cases) exercising db, auth, skills, testrunner, and
the full server flow over localhost. `python -m studio self-test` runs it. CI runs the
matrix on Python 3.8 and 3.11.
