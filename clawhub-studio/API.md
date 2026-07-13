# API

Base URL: `http://127.0.0.1:<port>`. All responses are JSON. Mutating endpoints require
`Authorization: Bearer <token>`.

## Auth
```
POST /api/login                  → { "token": "<signed>" }
```
No credentials — mints a local signed token (12h TTL).

## Health
```
GET  /api/health                → { "ok": true, "product": "clawhub-studio" }
```

## Skills
```
GET    /api/skills              → [ {id, slug, name, created_at, updated_at}, ... ]
POST   /api/skills              { "slug": str, "name": str }
                                  → 201 { "id": int, "slug": str }
GET    /api/skills/<slug>       → {id, slug, name, created_at, updated_at}
GET    /api/skills/<slug>/versions
                                  → [ {id, skill_id, version, manifest, status,
                                        published, created_at}, ... ]
POST   /api/skills/<slug>/versions
                                  { "version": "x.y.z",
                                    "manifest": {name, version, description, ...} }
                                  → 201 { "id": int, "version": str }
```

## Test (per version)
```
POST   /api/skills/<slug>/<version>/test
                                  → { "passed": bool, "rc": int, "output": str }
```
Runs the skill's self-test (from `data_dir/skills/<slug>` on disk) and records a run.

## Publish
```
POST   /api/skills/<slug>/<version>/publish
                                  { "dry_run": true }   # default true
                                  → { "published": bool, "rc": int,
                                      "output": str, "command": str }
```
Wraps `clawhub publish <folder>`. Set `dry_run: false` to actually publish (requires the
`clawhub` CLI authenticated as the target account).

## Errors
- `401` — missing/invalid token.
- `404` — unknown route or missing skill/version.
- `409` — skill slug already exists.
- `400` — bad request body.
