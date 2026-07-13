"use strict";
/* ClawHub Studio SPA — talks to the local REST API. No framework. */

const State = { token: null, skills: [], current: null };

const $ = (id) => document.getElementById(id);
const api = {
  async req(method, path, body) {
    const opts = { method, headers: {} };
    if (body !== undefined) {
      opts.headers["Content-Type"] = "application/json";
      opts.body = JSON.stringify(body);
    }
    if (State.token) opts.headers["Authorization"] = "Bearer " + State.token;
    const r = await fetch(path, opts);
    const text = await r.text();
    let json = {};
    try { json = text ? JSON.parse(text) : {}; } catch (e) { json = { raw: text }; }
    return { status: r.status, data: json };
  },
  health: () => api.req("GET", "/api/health"),
  login: () => api.req("POST", "/api/login"),
  listSkills: () => api.req("GET", "/api/skills"),
  createSkill: (s) => api.req("POST", "/api/skills", s),
  versions: (slug) => api.req("GET", `/api/skills/${slug}/versions`),
  test: (slug, ver) => api.req("POST", `/api/skills/${slug}/${ver}/test`),
  publish: (slug, ver) => api.req("POST", `/api/skills/${slug}/${ver}/publish`, { dry_run: true }),
};

function toast(msg) {
  const t = $("toast");
  t.textContent = msg;
  t.classList.remove("hidden");
  clearTimeout(toast._t);
  toast._t = setTimeout(() => t.classList.add("hidden"), 2600);
}

function showView(name) {
  document.querySelectorAll(".view").forEach((v) => v.classList.add("hidden"));
  document.querySelectorAll(".nav-item").forEach((n) => n.classList.remove("active"));
  const map = { skills: "view-skills", new: "view-new", runs: "view-runs" };
  if (map[name]) $(map[name]).classList.remove("hidden");
  const nav = document.querySelector(`.nav-item[data-view="${name}"]`);
  if (nav) nav.classList.add("active");
  const titles = { skills: "Skills", new: "New Skill", runs: "Runs" };
  $("view-title").textContent = titles[name] || "ClawHub Studio";
}

async function ensureAuth() {
  if (State.token) return true;
  const { data } = await api.login();
  if (data.token) { State.token = data.token; $("btn-login").textContent = "● Authed"; return true; }
  toast("Login failed");
  return false;
}

async function loadSkills() {
  if (!await ensureAuth()) return;
  const { status, data } = await api.listSkills();
  if (status !== 200) { toast("Failed to load skills"); return; }
  State.skills = data || [];
  renderSkills();
}

function renderSkills() {
  const grid = $("skill-grid");
  grid.innerHTML = "";
  $("empty-skills").style.display = State.skills.length ? "none" : "block";
  for (const s of State.skills) {
    const el = document.createElement("div");
    el.className = "card skill-card";
    el.innerHTML = `<h3>${esc(s.name)}</h3><div class="meta">@${esc(s.slug)}</div>`;
    el.onclick = () => openSkill(s.slug);
    grid.appendChild(el);
  }
}

function esc(t) { return String(t).replace(/[&<>"]/g, (c) => ({ "&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;" }[c])); }

async function openSkill(slug) {
  if (!await ensureAuth()) return;
  const { data: vers } = await api.versions(slug);
  State.current = { slug, versions: vers || [] };
  $("view-title").textContent = "@" + slug;
  $("detail-title").textContent = "@" + slug;
  const latest = vers && vers.length ? vers[0] : null;
  $("detail-manifest").textContent = latest ? latest.manifest : "(no versions)";

  const ul = $("detail-versions");
  ul.innerHTML = "";
  for (const v of vers || []) {
    const li = document.createElement("li");
    li.innerHTML = `<span>${esc(v.version)}</span><span class="badge ${v.status}">${esc(v.status)}</span>`;
    ul.appendChild(li);
  }
  $("view-skills").classList.add("hidden");
  $("view-detail").classList.remove("hidden");
  document.querySelectorAll(".nav-item").forEach((n) => n.classList.remove("active"));
  $("view-title").textContent = "@" + slug;
}

async function createSkill() {
  const slug = $("in-slug").value.trim();
  const name = $("in-name").value.trim();
  const desc = $("in-desc").value.trim();
  const version = $("in-version").value.trim() || "0.1.0";
  if (!slug || !name) { toast("Slug and name required"); return; }
  if (!await ensureAuth()) return;
  const { status, data } = await api.createSkill({ slug, name });
  if (status !== 201) { $("new-result").textContent = "Error: " + JSON.stringify(data); return; }
  // add first version with a minimal manifest
  await api.req("POST", `/api/skills/${slug}/versions`, {
    version,
    manifest: { name, version, description: desc },
  });
  $("new-result").textContent = "Created " + slug + " v" + version;
  toast("Skill created");
  showView("skills");
  await loadSkills();
}

async function runTest() {
  if (!State.current) return;
  const v = State.current.versions[0];
  if (!v) { toast("No version to test"); return; }
  $("detail-output").textContent = "Running self-test…";
  const { data } = await api.test(State.current.slug, v.version);
  $("detail-output").textContent = (data.passed ? "PASS ✅\n" : "FAIL ❌\n") + (data.output || "");
}

async function publish() {
  if (!State.current) return;
  const v = State.current.versions[0];
  if (!v) { toast("No version to publish"); return; }
  $("detail-output").textContent = "Publishing (dry-run)…";
  const { data } = await api.publish(State.current.slug, v.version);
  $("detail-output").textContent = (data.published ? "PUBLISHED ✅\n" : "DRY-RUN\n") + (data.output || "") + "\n" + (data.command || "");
}

async function checkHealth() {
  const { status } = await api.health();
  const ok = status === 200;
  $("health-dot").classList.toggle("ok", ok);
  $("health-text").textContent = ok ? "studio online" : "offline";
}

// wire up
document.querySelectorAll(".nav-item").forEach((n) => n.onclick = () => showView(n.dataset.view));
$("btn-new").onclick = () => showView("new");
$("btn-back").onclick = () => { showView("skills"); $("view-detail").classList.add("hidden"); $("view-skills").classList.remove("hidden"); };
$("btn-create").onclick = createSkill;
$("btn-test").onclick = runTest;
$("btn-publish").onclick = publish;
$("btn-login").onclick = async () => { if (await ensureAuth()) { toast("Authenticated"); await loadSkills(); } };

(async () => {
  await checkHealth();
  await loadSkills();
  setInterval(checkHealth, 15000);
})();
