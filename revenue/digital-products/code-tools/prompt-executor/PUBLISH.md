# Publishing prompt-executor to npm

This package is **already pushed to GitHub** and its test suite passes
(`node test/prompt-executor.test.js` → 8/8). The only remaining step is the
public npm release, which is **owner-gated** (the founder's npm account + 2FA)
and therefore cannot be performed by the autonomous agent.

## What the agent already did (PRE-85, steps 1–2)
- Verified the package builds and the test suite passes locally: **8/8 OK**.
- Pushed the source to the public repo: https://github.com/itsPremkumar/prompt-executor
- README links back to the Prem Autonomous Co showcase (PRE-5).

## Founder handoff — publish to npm (PRE-85, step 3)
Run these once, from this folder, on a machine logged into the **founder** npm account:

```bash
# 1) make sure you are logged in as the founder (2FA/OTP may be required)
npm whoami            # should print the founder's npm username
# if not logged in:
npm login

# 2) check the package name is available (unscoped name "prompt-executor"
#    may already be taken on npm — if so, rename in package.json, e.g.
#    "@premkumar/prompt-executor", or use a scoped publish with --access public)
npm view prompt-executor version   # 404 = name is free; otherwise pick a new name

# 3) publish (public so it is installable without auth)
npm publish --access public
```

After a successful publish, verify with:

```bash
npm install -g prompt-executor     # or: npx prompt-executor list
prompt-executor list
```

## Notes / risks
- `npm publish` pushes to the **public** registry. Double-check `name`,
  `version`, and `files` in `package.json` before publishing.
- Bumping `version` is required for any subsequent publish.
- No token is stored in the repo; the agent leaves this step to the human owner
  on purpose (Constitution S0 — human-in-the-loop for money/movement actions).
