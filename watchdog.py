#!/usr/bin/env python3
"""
Paperclip Company Watchdog  (ZERO investment, zero LLM cost)

Runs on a schedule (Windows Task Scheduler, every 5 min + on boot).
What it does, every cycle, WITHOUT spending any API/token budget:
  1. Re-authenticates (sign-in) -> always-fresh session cookie.
  2. Checks /api/health. If the server is down or unhealthy, restarts it
     via run-server.bat (detached) and waits for it to come back.
  3. Pulls the company, its hermes_local worker agent, and open issues.
  4. If there is pending work and the agent is idle (no heartbeat running),
     nudges a heartbeat so the agent keeps executing.
  5. Detects "stuck / needs-disposition" issues and lists them.
  6. Writes company-status.json + company-report.md for the human to read.

No OpenAI/Hermes calls happen here -> the only cost is a few HTTP requests.
"""
import json
import os
import socket
import subprocess
import sys
import time
import urllib.request
import urllib.error
from datetime import datetime, timezone

BASE = "http://localhost:3100"
ORIGIN = "http://localhost:3100"
COMPANY_NAME = "Prem Autonomous Co"
HERE = os.path.dirname(os.path.abspath(__file__))
SERVER_BAT = os.path.join(HERE, "run-server.bat")
COOKIE = os.path.join(HERE, "watchdog-cj.txt")
STATUS_JSON = os.path.join(HERE, "company-status.json")
REPORT_MD = os.path.join(HERE, "company-report.md")
LOG = os.path.join(HERE, "watchdog.log")

EMAIL = "prem@local.dev"
PASSWORD = "LocalDevPass123!"

IDLE_NUDGE_SECS = 8 * 60      # only nudge if agent idle this long with pending work
HEALTH_WAIT_SECS = 60         # wait after (re)starting server
PORT = 3100


def log(msg):
    line = f"[{datetime.now(timezone.utc).isoformat()}] {msg}"
    print(line, flush=True)
    try:
        with open(LOG, "a", encoding="utf-8") as f:
            f.write(line + "\n")
    except Exception:
        pass


def http(method, path, body=None, cookie=None, as_json=True):
    url = BASE + path
    data = None
    headers = {"Origin": ORIGIN, "Content-Type": "application/json"}
    if body is not None:
        data = json.dumps(body).encode()
    if cookie and os.path.exists(cookie):
        with open(cookie, "r", encoding="utf-8") as f:
            for ln in f:
                if ln.startswith("#") or not ln.strip():
                    continue
                parts = ln.split("\t")
                if len(parts) >= 7 and parts[5].strip():
                    headers["Cookie"] = f"{parts[5].strip()}={parts[6].strip().rstrip(chr(10))}"
                    break
    req = urllib.request.Request(url, data=data, headers=headers, method=method)
    try:
        with urllib.request.urlopen(req, timeout=15) as r:
            raw = r.read().decode()
            set_cookie = r.headers.get("Set-Cookie")
            return (json.loads(raw) if as_json else raw), None, set_cookie
    except urllib.error.HTTPError as e:
        raw = e.read().decode(errors="replace")
        try:
            return (json.loads(raw) if as_json else raw), e.code, e.headers.get("Set-Cookie")
        except Exception:
            return raw, e.code, None
    except Exception as e:  # network / timeout
        return None, str(e), None


def save_cookie_from_header(set_cookie):
    """Parse a Set-Cookie header into the Netscape jar used by curl/python."""
    if not set_cookie:
        return False
    # take the first cookie pair
    first = set_cookie.split(",")[0] if ";" in set_cookie.split(",")[0] else set_cookie
    pair = first.split(";")[0]
    if "=" not in pair:
        return False
    name, _, val = pair.partition("=")
    with open(COOKIE, "w", encoding="utf-8") as f:
        f.write("# Netscape HTTP Cookie File\n")
        f.write(f"localhost\tFALSE\t/\tFALSE\t0\t{name.strip()}\t{val.strip()}\n")
    return True


def sign_in():
    res, err, set_cookie = http("POST", "/api/auth/sign-in/email",
                                {"email": EMAIL, "password": PASSWORD}, cookie=None)
    if err:
        log(f"sign-in failed: {err}")
        return False
    if not save_cookie_from_header(set_cookie):
        log("sign-in returned no Set-Cookie")
        return False
    log("re-authenticated OK")
    return True


def port_open():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(2)
    try:
        return s.connect_ex(("127.0.0.1", PORT)) == 0
    finally:
        s.close()


def restart_server():
    log("attempting to (re)start server via run-server.bat")
    if not os.path.exists(SERVER_BAT):
        log(f"ERROR: {SERVER_BAT} missing")
        return False
    try:
        subprocess.Popen(
            f'cmd.exe /c start "" "{SERVER_BAT}"',
            shell=True,
            stdout=subprocess.DEVNULL,
            stderr=subprocess.DEVNULL,
        )
        return True
    except Exception as e:
        log(f"restart failed: {e}")
        return False


def main():
    log("=== watchdog cycle start ===")
    if not sign_in():
        log("CRITICAL: cannot authenticate; aborting cycle")
        return

    # 1) health / liveness
    if not port_open():
        log("server port closed -> restarting")
        restart_server()
        time.sleep(HEALTH_WAIT_SECS)
    health, err, _ = http("GET", "/api/health", cookie=COOKIE)
    if err or not isinstance(health, dict) or health.get("status") != "ok":
        log(f"health bad ({err or health}); restarting server")
        restart_server()
        time.sleep(HEALTH_WAIT_SECS)
        health, err, _ = http("GET", "/api/health", cookie=COOKIE)
        if err or not isinstance(health, dict) or health.get("status") != "ok":
            log("CRITICAL: server still down after restart")
            write_status(health=("down" if err else health), issues=[], agent=None,
                         nudged=False, critical="server unreachable")
            return
    log("server healthy")

    # 2) company + worker agent
    companies, _, _ = http("GET", "/api/companies", cookie=COOKIE)
    company = None
    if isinstance(companies, list):
        company = next((c for c in companies if c.get("name") == COMPANY_NAME), None)
    if not company:
        log("company not found")
        return
    cid = company["id"]
    agents, _, _ = http("GET", f"/api/companies/{cid}/agents", cookie=COOKIE)
    worker = None
    if isinstance(agents, list):
        worker = next((a for a in agents
                       if a.get("adapterType") == "hermes_local"
                       and a.get("role") == "cto"), None)
    if not worker:
        worker = next((a for a in (agents or []) if a.get("adapterType") == "hermes_local"), None)
    aid = worker["id"] if worker else None

    # 3) issues
    issues, _, _ = http("GET", f"/api/companies/{cid}/issues", cookie=COOKIE)
    issues = issues if isinstance(issues, list) else []
    open_issues = [i for i in issues if i.get("status") in ("todo", "in_progress")]
    pending_for_worker = [i for i in open_issues if i.get("assigneeAgentId") == aid]

    # 4) is a heartbeat currently running? Use the agent status + lastHeartbeatAt
    #    (the /heartbeat-runs list endpoint is not exposed on this build).
    agent_running = (worker or {}).get("status") == "running"
    last_hb = (worker or {}).get("lastHeartbeatAt")
    idle_too_long = True
    if last_hb:
        try:
            from datetime import datetime as _dt
            lt = _dt.fromisoformat(last_hb.replace("Z", "+00:00"))
            idle_too_long = (datetime.now(timezone.utc) - lt).total_seconds() > IDLE_NUDGE_SECS
        except Exception:
            idle_too_long = True
    nudged = False
    if aid and pending_for_worker and not agent_running and idle_too_long:
        # nudge only if work is pending, agent not mid-run, and idle a while
        res, e, _ = http("POST", f"/api/agents/{aid}/heartbeat/invoke", cookie=COOKIE)
        if not e:
            nudged = True
            log(f"nudged heartbeat for {worker.get('name')} ({len(pending_for_worker)} open issues)")

    # 5) stuck / needs-disposition detection
    stuck = [i for i in open_issues if i.get("status") == "in_progress"
             and not i.get("disposition")]

    write_status(health=health, issues=issues, agents=agents, worker=worker,
                 nudged=nudged, critical=None, stuck=stuck)
    log(f"cycle done: {len(open_issues)} open, {len(pending_for_worker)} for worker, "
        f"nudged={nudged}, stuck={len(stuck)}")
    log("=== watchdog cycle end ===")


def write_status(health, issues, agents, worker, nudged, critical, stuck=None):
    now = datetime.now(timezone.utc).isoformat()
    ags = agents if isinstance(agents, list) else []
    workers = [a for a in ags if a.get("adapterType") == "hermes_local"]
    summary = {
        "generatedAt": now,
        "server": "ok" if (isinstance(health, dict) and health.get("status") == "ok") else str(health),
        "agentsTotal": len(workers),
        "agentsRunning": len([a for a in workers if a.get("status") == "running"]),
        "agentsHeartbeatOn": len([a for a in workers
                                  if ((a.get("runtimeConfig") or {}).get("heartbeat") or {}).get("enabled")]),
        "worker": (worker or {}).get("name"),
        "workerStatus": (worker or {}).get("status"),
        "openIssues": len([i for i in issues if i.get("status") in ("todo", "in_progress")]),
        "nudgedThisCycle": nudged,
        "critical": critical,
        "agents": [
            {"name": a.get("name"), "role": a.get("role"), "status": a.get("status"),
             "heartbeat": ((a.get("runtimeConfig") or {}).get("heartbeat") or {}).get("enabled")}
            for a in workers
        ],
        "issues": [
            {"id": i.get("identifier"), "status": i.get("status"),
             "title": i.get("title"), "assignee": i.get("assigneeAgentId")}
            for i in issues
        ],
    }
    with open(STATUS_JSON, "w", encoding="utf-8") as f:
        json.dump(summary, f, indent=2)
    # human report
    lines = [f"# Paperclip Company — Status Report", "",
             f"_Generated: {now}_\n",
             f"- **Server:** {summary['server']}",
             f"- **Agents:** {summary['agentsRunning']}/{summary['agentsTotal']} running, "
             f"{summary['agentsHeartbeatOn']} heartbeat-on",
             f"- **Open issues:** {summary['openIssues']}",
             f"- **Watchdog nudged this cycle:** {nudged}", "\n",
             "## Agents (C-suite)"]
    lines.append("")
    lines.append("| Agent | Role | Status | Heartbeat |")
    lines.append("|-------|------|--------|-----------|")
    for a in sorted(summary["agents"], key=lambda x: x["role"]):
        lines.append(f"| {a['name']} | {a['role']} | {a['status']} | {'on' if a['heartbeat'] else 'off'} |")
    if critical:
        lines.append("")
        lines.append(f"## ⚠ CRITICAL: {critical}")
    lines.append("")
    lines.append("## Issues")
    lines.append("")
    lines.append("| ID | Status | Title |")
    lines.append("|----|--------|-------|")
    for i in sorted(summary["issues"], key=lambda x: (x["id"] or "")):
        lines.append(f"| {i['id']} | {i['status']} | {i['title']} |")
    lines.append("")
    lines.append("---")
    lines.append("Monitored zero-investment by watchdog.py (Task Scheduler, every 5 min).")
    with open(REPORT_MD, "w", encoding="utf-8") as f:
        f.write("\n".join(lines))


if __name__ == "__main__":
    main()
