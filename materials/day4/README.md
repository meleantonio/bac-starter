# Day 4 Sprint Guide — Integration, Replication, Presentation

> **Objective:** Deliver a mini research package and communicate results clearly in a 5–7 minute capstone presentation.

---

## Pre-Sprint Reading

Complete *before* the Day 4 session. Estimated time: 25–35 minutes.

| Document | Path | Focus |
|----------|------|-------|
| **Cloud Agents & Safety** | [module_background_agents_safety.md](../../docs/workshop/module_background_agents_safety.md) | Review-before-merge, branch handoff, safety rules (Day 3 recap) |
| **Replication README Template** | [templates/replication_README.md](../../templates/replication_README.md) | Structure to fill during Sprint A |

**Note:** [MCP Introduction](../../docs/workshop/module_mcp_intro.md) is taught on **Day 3** (see [materials/day3/README.md](../day3/README.md)). Use it if you document `docs/mcp_setup.md` in your replication package.

**Key concepts:**
- Replication package = clone + deps + run = outputs.
- Clean run = fresh clone, new venv, no manual hacks.
- Presentation scope: problem, method, demo, next steps. One result beats many.

---

## Detailed Sprint Schedule

| Block | Time | Duration | Activity |
|-------|------|----------|----------|
| **Demo** | 0:00–0:20 | 20 min | Replication clean-run, package structure |
| **Sprint A** | 0:20–1:40 | **80 min** | Clean-run + replication README |
| **Checkpoint** | 1:40–1:50 | 10 min | Blockers in replication run |
| **Sprint B** | 1:50–2:50 | **60 min** | Finalize package + presentation draft |
| **30-Day Plan + Handoff** | 2:50–3:30 | 40 min | Adoption plan, handoff notes |
| **Wrap-up** | 3:30–4:00 | 30 min | Presentations + final review |

**Total:** 4 hours.

---

## Sprint Block A — Clean-Run + Replication (0:20–1:40)

### Walkthrough

#### Step 1: Freeze Project Scope (≈5 min)

- No new features. Lock deliverables to what exists from Day 3.
- Document any known limitations (missing data, environment-specific steps) in `notes/` or `replication/README.md`.

#### Step 2: Run Clean Replication (≈30 min)

**Clean state means:**
- Fresh clone of your repo (or use a clean directory)
- New virtual environment
- No cached data or outputs from prior runs (or document where they come from)

**Commands (adjust to your setup):**
```bash
# In a fresh directory
git clone [YOUR_REPO_URL] capstone-clean
cd capstone-clean

python -m venv .venv
source .venv/bin/activate   # Windows: .venv\Scripts\activate
pip install -r requirements.txt

# Configure data (API keys, paths) — document in replication README
export FRED_API_KEY=your_key   # if needed

# Run pipeline — document exact commands
python src/fetch_data.py
python src/run_analysis.py
```

**Record:**
- Exact commands that work
- Time to run (if >5 min, note it)
- Any manual steps (e.g., downloading a file, placing it in `data/`)

#### Step 3: Document Replication Steps (≈40 min)

Fill `replication/README.md` (or copy from `templates/replication_README.md`):

1. **Overview** — One paragraph: project, research question, what the package contains
2. **Requirements** — OS, Python version, key packages, data access
3. **Directory structure** — Match your project
4. **Setup instructions** — Clone, venv, install, configure data
5. **Running the pipeline** — Exact commands in order
6. **Expected outputs** — Tables, figures, paths
7. **Troubleshooting** — Common issues and solutions
8. **Contact** — Your name/email for replication questions

**See:** `examples/sample_replication_readme.md` for a completed example.

#### Step 4: Handle Blockers

| Blocker | Action |
|---------|--------|
| **Missing data** | Document required access; provide stub/mock dataset or download URL |
| **API key required** | Document in Requirements and Setup; never commit the key |
| **Clean run fails** | Isolate smallest failing step; add to Troubleshooting |
| **Platform-specific** | Note OS/versions in Requirements |

---

## Checkpoint (1:40–1:50)

- [ ] Clean run completed (or documented blockers)
- [ ] Replication README drafted with exact commands
- [ ] Known limitations listed
- [ ] Package structure frozen

**Timebox warning:** If clean run fails late, document the failure and provide a "partial replication" path (e.g., use provided sample data) so reviewers can still run something.

---

## Sprint Block B — Package + Presentation (1:50–2:50)

### Walkthrough

#### Step 1: Finalize Package (≈25 min)

- **README.md** (root): Update with project title, quick start, link to `replication/README.md`
- **Directory cleanup:** Remove temp files, stray notebooks, unused scripts
- **.cursorignore:** Ensure data, secrets, large files are excluded
- **AGENTS.md:** Update with final run command and any project-specific notes

#### Step 2: Prepare 5–7 Minute Presentation (≈30 min)

Use `templates/presentation_outline.md` as structure:

| Slide | Content | Time |
|-------|---------|------|
| 1 | Title + research question | ~30 s |
| 2 | Motivation + contribution | ~60 s |
| 3 | Method + data | ~60 s |
| 4 | Key results / prototype demo | ~90 s |
| 5 | Workflow + tools (modes, subagents, skills) | ~60 s |
| 6 | Next steps + 30-day plan | ~30 s |

**Presentation guidelines:**
- One idea per slide
- Put the research question in bold on slide 1
- One main result > many; highlight one takeaway
- Optional: 30-second live demo (run script, show output) — rehearse; have screenshot backup
- Mention: design memo, pipeline, replication, agentic workflow

**See:** `prompts/delivery_prompts.md` for presentation drafting prompts.

---

## 30-Day Plan Session (2:50–3:30)

### Walkthrough

1. Copy `templates/adoption_plan_30d.md` to your repo (e.g., `docs/adoption_plan_30d.md` or root).
2. Fill each week:
   - **Week 1 — Consolidate:** Rules, .cursorignore, AGENTS.md, mode usage
   - **Week 2 — Apply:** One real task with Agent, one issue→PR cycle
   - **Week 3 — Expand:** One subagent, one skill, one parallel execution
   - **Week 4 — Sustain:** Weekly agent sprint slot, share with colleague
3. Update Check-in Notes as you go.
4. List Resources to Revisit (Cursor docs, workshop materials, your templates).

**See:** `examples/sample_adoption_plan.md` for a completed example.

### Handoff Notes

- Add to `docs/` or `notes/`: next owner, data access contacts, known TODOs
- If MCP is configured: document in `docs/mcp_setup.md` (see module_mcp_intro.md)

---

## Presentation Guidelines and Tips

- **Rehearse once with a timer** — Stay within 5–7 minutes
- **If demo fails** — Have a screenshot or pre-generated figure as backup
- **Point to repo** — "Full replication in replication/README.md"
- **Q&A:** Budget 2–3 minutes. Common questions: data access, method choices, agent workflow wins

---

## If You Get Stuck

| Situation | Try |
|-----------|-----|
| **Clean run fails** | Isolate smallest failing step. Rerun with verbose logs. Document in Troubleshooting. |
| **Missing data** | Document required access. Provide stub/mock dataset or download instructions. |
| **Presentation scope creep** | Limit to: problem, method, demo, next steps. Cut slides if needed. |
| **Replication README too long** | Focus on: Setup, Run Pipeline, Expected Outputs. Move details to separate docs. |
| **30-day plan feels generic** | Pick one concrete project. Name specific files, tasks, colleagues. |
| **MCP not working** | Skip for package; document as "optional" in replication README. |

---

## Final Deliverables Checklist (All 4 Days)

### From Day 1
- [ ] Project brief (1 page)
- [ ] Issue board (≥8 issues)
- [ ] First merged PR
- [ ] Rules, AGENTS.md, .cursorignore

### From Day 2
- [ ] Research design memo
- [ ] Data source map
- [ ] Prioritized implementation backlog
- [ ] Context control notes

### From Day 3
- [ ] Working prototype (scripts or notebook pipeline)
- [ ] Orchestration log
- [ ] Consistency/review log
- [ ] Merged PR set for core features
- [ ] One subagent and one skill used at least once

### From Day 4
- [ ] Mini research package (repo + instructions)
- [ ] Replication README with clean-run command
- [ ] Clean run verified (or blockers documented)
- [ ] 5–7 minute capstone presentation
- [ ] 30-day post-workshop adoption plan
- [ ] Handoff notes (if applicable)

---

## Prompts and Examples

- **Copy-pasteable prompts:** [prompts/delivery_prompts.md](prompts/delivery_prompts.md)
- **Sample replication README:** [examples/sample_replication_readme.md](examples/sample_replication_readme.md)
- **Sample adoption plan:** [examples/sample_adoption_plan.md](examples/sample_adoption_plan.md)

---

*Guidance: A runnable package and a clear presentation beat perfection. Ship it.*
