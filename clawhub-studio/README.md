# ClawHub Studio

A local-first studio to **author, test, version, and publish agent skills** — with a real
backend, auth, a test-runner UI, and one-click ClawHub publishing.

This is the production-grade successor to the one-off skill scripts: one cohesive app
instead of thirty fragments.

## Features
- **Skills registry** — create skills, manage semver versions, store manifests (SQLite).
- **Test runner** — run a skill's `self-test` from the UI; results are recorded per version.
- **Publish** — push a skill to ClawHub via the local `clawhub` CLI (dry-run first).
- **Auth** — signed session tokens (HMAC), no plaintext passwords.
- **Zero dependencies** — stdlib `http.server` + `sqlite3`. Runs anywhere Python 3.8+ runs.

## Quick start
```bash
cd clawhub-studio
python -m studio serve --port 8000 --open
# open http://127.0.0.1:8000
```
Login is automatic (mints a local token). Create a skill, add a version, hit
**Run self-test**, then **Publish (dry-run)**.

## Verify
```bash
python -m unittest discover -s tests        # 31 tests
python -m studio self-test                  # same suite, packaged
```

## Layout
```
clawhub-studio/
  studio/
    __main__.py   CLI: serve / self-test
    db.py         SQLite repository (skill / version / run)
    auth.py       signed session tokens (HMAC-SHA256)
    skills.py     manifest parse/validate/version-bump/serialize
    testrunner.py run a skill's self-test + portfolio harness
    publish.py    wrap `clawhub publish`
    server.py     REST API + static SPA host
  web/            single-page UI (index.html, app.js, styles.css)
  tests/          real unittest suite (db, auth, skills, testrunner, server)
```

See [ARCHITECTURE.md](ARCHITECTURE.md) and [API.md](API.md).
