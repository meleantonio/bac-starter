# Day 3 Sprint Guide — Parallel Agent Execution and Swarm Orchestration

> **Objective:** Execute implementation issues in parallel, keep outputs consistent, and use subagents and skills in a structured swarm workflow.

---

## Pre-Sprint Reading

Complete *before* the Day 3 session. Estimated time: 30–45 minutes.

| Document | Path | Focus |
|----------|------|-------|
| **Subagents** | [module_subagents.md](../../docs/workshop/module_subagents.md) | Role specialization, `.cursor/agents/` format, when to delegate |
| **Skills & Skillcraft** | [module_skills_skillcraft.md](../../docs/workshop/module_skills_skillcraft.md) | SKILL.md structure, triggers, progressive disclosure |
| **Cloud Agents & Safety** | [module_background_agents_safety.md](../../docs/workshop/module_background_agents_safety.md) | Branch handoff, review-before-merge, prompt injection awareness (read before swarm lab) |
| **Swarms & Orchestration** | [module_swarms_github_cloud.md](../../docs/workshop/module_swarms_github_cloud.md) | GitHub issues/labels, parallel vs sequential Cloud Agents, orchestration log, HANK-style example |
| **MCP Intro** | [module_mcp_intro.md](../../docs/workshop/module_mcp_intro.md) | MCP basics, FRED/filesystem setup, when MCP adds value (slides + demo on Day 3) |

**Key concepts to absorb:**
- Subagents = specialized context; one role per subagent.
- Skills = reusable workflows triggered by description; augment the main agent.
- Swarms = multiple coordinated agents; **GitHub issues + labels** express parallel vs sequential work; **Cloud Agents** can run one issue per branch when tasks are large enough to isolate.
- Handoff files (`notes/handoff_*.md`) and `notes/orchestration_log.md` reduce integration risk.
- Never merge without review; branch isolation is your safety boundary.

---

## Detailed Sprint Schedule

| Block | Time | Duration | Activity |
|-------|------|----------|----------|
| **Demo** | 0:00–0:20 | 20 min | Issue decomposition, subagents, skills, swarm setup |
| **Sprint A** | 0:20–1:40 | **80 min** | Parallel implementation on 3 branches |
| **Checkpoint** | 1:40–1:50 | 10 min | Integration risks, review assignments |
| **Sprint B** | 1:50–2:50 | **60 min** | PRs, consistency pass, merges |
| **Skill/Subagent Lab** | 2:50–3:30 | 40 min | Create 1 subagent + 1 skill, use them |
| **Wrap-up** | 3:30–4:00 | 30 min | Verify deliverables, Day 4 prep |

**Total:** 4 hours.

---

## Sprint Block A — Parallel Implementation (0:20–1:40)

### Walkthrough

#### Step 0: Label issues (≈5 min)

Add GitHub labels (or project columns) so dependencies are explicit: e.g. `parallel`, `sequential`, `blocked-by:#N`. Independent issues can run **Cloud Agents** (or foreground Agent) in parallel; dependent issues wait until prerequisite PRs merge. See [module_swarms_github_cloud.md](../../docs/workshop/module_swarms_github_cloud.md).

#### Step 1: Assign Branches per Issue (≈10 min)

Map your issues to up to three parallel streams (or more if your team can handle it). Typical mapping:

| Stream | Branch | Issue | Deliverable | Depends on |
|--------|--------|-------|-------------|------------|
| **Data** | `rig/data-loader` | #X | Data loader + `notes/handoff_data_to_analysis.md` | — |
| **Analysis** | `rig/analysis` | #Y | Analysis script + handoff to paper | Data handoff |
| **Paper** | `rig/paper-skeleton` | #Z | Paper skeleton, intro–conclusion | Analysis handoff |

**Commands to create branches:**
```bash
git checkout main
git pull origin main

git checkout -b rig/data-loader main
git push -u origin rig/data-loader

git checkout main
git checkout -b rig/analysis main
git push -u origin rig/analysis

git checkout main
git checkout -b rig/paper-skeleton main
git push -u origin rig/paper-skeleton

git checkout main
```

#### Step 2: Create Orchestration Log (≈5 min)

Create `notes/orchestration_log.md`:

```markdown
# Orchestration Log — [Project Name]

| Stream | Branch | Issue | Status | PR | Reviewer |
|--------|--------|-------|--------|-----|----------|
| data   | rig/data-loader    | #X | pending | - | - |
| analysis | rig/analysis     | #Y | pending | - | - |
| paper  | rig/paper-skeleton | #Z | pending | - | - |
```

#### Step 3: Run Parallel Coding Agents (≈55 min)

**Option A — Single machine, sequential (simplest):**  
Work on one branch at a time. Switch branches between streams. Use Agent to implement each stream's deliverable.

**Option B — Git worktrees (parallel):**  
Create separate directories per branch. Open each in a different Cursor window and run Agent in parallel.

```bash
# Example: create worktrees
git worktree add ../capstone-data rig/data-loader
git worktree add ../capstone-analysis rig/analysis
git worktree add ../capstone-paper rig/paper-skeleton
```

**Agent prompts per stream** (copy from `prompts/agent_prompts.md`):

- **Data stream:** Implement data loader per issue #X. Output handoff file with column names, units, sample stats.
- **Analysis stream:** Implement analysis script per issue #Y. Read handoff from notes/. Output estimates and handoff to paper.
- **Paper stream:** Create paper skeleton per issue #Z. Use handoff for results. Structure: intro, data, methods, results, conclusion.

#### Step 4: Create Handoff Files

Where streams depend on each other, create explicit handoff files in `notes/`:

- `notes/handoff_data_to_analysis.md` — from data stream: paths, columns, units, sample counts.
- `notes/handoff_analysis_to_paper.md` — from analysis stream: key results, variable labels, figures/tables to cite.

#### Step 5: Open PRs with Clear Scope

For each stream, open a PR targeting `main`. PR title/description should:

- Reference the issue (e.g., "Closes #X")
- List changed files and deliverables
- Note any dependencies (e.g., "merge data PR first")

---

## Checkpoint (1:40–1:50)

- [ ] All 3 streams have code committed and PRs opened (or nearly ready)
- [ ] Orchestration log updated with PR links
- [ ] Integration risks identified (e.g., shared paths, order of merge)
- [ ] Assign reviewer: self, partner, or pr-reviewer subagent

**Timebox warning:** If Sprint A is behind, reduce scope for one stream rather than eating into Sprint B.

---

## Sprint Block B — PRs, Review, Merges (1:50–2:50)

### Walkthrough

#### Step 1: Run Consistency / Review Pass (≈20 min)

Use the **pr-reviewer subagent** (create in Skill/Subagent Lab if needed):

> Use the pr-reviewer subagent to review all open PRs for rig/data-loader, rig/analysis, and rig/paper-skeleton. Check cross-stream consistency (paths, units, labels). Report: ready to merge / needs changes.

Document findings in `notes/review_log.md` (or `replication/review_log.md`). Use the template at `templates/review_log.md`.

#### Step 2: Resolve Integration Blockers (≈20 min)

- **Conflicting branches:** Pause merges. Merge in dependency order: data → analysis → paper.
- **Path mismatches:** Align on a single convention (e.g., `data/processed/panel.csv`).
- **Missing handoffs:** Add or fix handoff files so streams can run in sequence.

#### Step 3: Merge PRs (≈15 min)

Merge order (if dependencies exist):

1. `rig/data-loader` → main
2. `rig/analysis` → main (rebase on main first if needed)
3. `rig/paper-skeleton` → main

If conflicts arise: create an integration branch, resolve, then merge.

#### Step 4: Run Replication Check

After merges:

> Use the replication-checker skill to verify the combined pipeline runs from a clean state.

Fix any blockers. Document the minimal run command in `replication/README.md`.

#### Step 5: Finalize Orchestration Log

Update `notes/orchestration_log.md` with:

- PR links
- Merge status
- Final run command for end-to-end pipeline

---

## Skill / Subagent Lab (2:50–3:30)

### Step-by-Step: Create 1 Subagent + 1 Skill

#### Create PR Reviewer Subagent (≈10 min)

1. Ensure `.cursor/agents/` exists.
2. Create `.cursor/agents/pr-reviewer.md` — see `examples/sample_subagent.md` for a complete template.
3. Invoke: *"Use the pr-reviewer subagent to review [this PR / PR #X] for consistency, correctness, and style."*
4. Apply at least one suggested change.

**Alternative subagents:** replicator (clean-run validation), bibliographer (bib standardization). Prompts in `prompts/agent_prompts.md`.

#### Create One Skill (≈15 min)

1. Choose one: **replication-checker** (recommended), **literature-mapper**, **data-contract-enforcer**, **paper-polisher**.
2. Create `.cursor/skills/<skill-name>/SKILL.md` with:
   - YAML: `name`, `description` (include trigger phrases)
   - Body: core workflow, 3–5 steps
3. Add at least one `references/` or `scripts/` file if helpful.
4. Invoke on a real artifact:
   - Replication-checker: *"Use the replication-checker skill to verify that scripts/run_analysis.py runs from a clean state."*

#### Validate and Iterate (≈10 min)

- If the skill never triggers: broaden the description, add exact phrases users might say.
- If the agent ignores steps: make the body more imperative; use numbered lists.

---

## Swarm Lab Protocol — 3-Stream Parallel Execution

Follow these exact steps when running the swarm lab.

### Phase 1: Setup (15 min)

1. Create `notes/orchestration_log.md` with Stream | Branch | Issue | Status | PR | Reviewer.
2. Create branches: `rig/data-loader`, `rig/analysis`, `rig/paper-skeleton`.
3. Create placeholder handoff files in `notes/` if streams depend on each other.

### Phase 2: Parallel Execution (≈60–90 min)

4. **Stream 1 (data):** Switch to `rig/data-loader`. Agent: *"Implement [data loader] per issue #X. Output handoff file to notes/."*
5. **Stream 2 (analysis):** Use worktree or second window on `rig/analysis`. Agent: *"Implement [analysis script] per issue #Y. Read handoff from notes/."*
6. **Stream 3 (paper):** Use worktree or third window on `rig/paper-skeleton`. Agent: *"Create [paper skeleton] per issue #Z. Use handoff for results."*
7. Update `orchestration_log.md` as each stream completes (status → PR opened).

### Phase 3: Review and Merge (≈45 min)

8. Open PRs: each branch → main.
9. Run pr-reviewer subagent on each PR.
10. Fix blocking issues. Re-run replication-checker if applicable.
11. Merge in order: data → analysis → paper.
12. If integration issues: create integration branch, fix, merge.
13. Finalize `orchestration_log.md`.

### Phase 4: Verification (≈15 min)

14. Run the pipeline from scratch: clone, install deps, run. Document in `replication/README.md`.
15. Sign off: all streams merged, log complete, one clean run verified.

---

## Timebox Warnings

| Block | Warning | Action |
|-------|---------|--------|
| Sprint A | Still coding at 1:35 | Stop; open PRs with partial work. Fix in Sprint B. |
| Checkpoint | No PRs opened | Reduce scope for one stream; get something mergeable. |
| Sprint B | Review taking too long | Use subagent for speed; fix only blockers. |
| Skill/Subagent Lab | Skill too broad | Narrow to one repetitive task (e.g., replication check only). |
| Wrap-up | Missing deliverables | Prioritize: working prototype > merged PRs > skill used once. |

---

## Extension Challenges

- **4–5 parallel streams:** Add a doc-generation stream or a visualization stream.
- **Cloud Agent:** Run one long task (e.g., docstrings for `src/`) via a Cloud Agent; review the PR before merge.
- **Second subagent:** Create replicator or bibliographer; invoke both reviewer and bibliographer on a PR.
- **Integration test:** Add a minimal pytest or script that runs the full pipeline and asserts outputs exist.

---

## If You Get Stuck

| Situation | Try |
|-----------|-----|
| **Conflicting branches** | Pause merges. Nominate an integrator. Merge in dependency order. Rebase in sequence. |
| **Agent output inconsistent** | Run review log checklist; align on conventions (paths, units, naming). |
| **Skill never triggers** | Broaden description. Add trigger phrases: "check replication," "validate pipeline," "standardize bib." |
| **Subagent not found** | Ensure file is in `.cursor/agents/` with valid YAML. Restart Cursor or reload window. |
| **Review bottleneck** | Use pr-reviewer subagent. Don't block on human-only review for small changes. |
| **Merge conflicts** | Merge in dependency order (data → analysis → paper). Resolve as human integrator; don't let agents auto-merge. |
| **Clean run fails** | Isolate smallest failing step. Rerun with logs. Document as "Known Limitations" in replication README. |

---

## End-of-Day Deliverables Checklist

- [ ] Working prototype (scripts or notebook pipeline)
- [ ] `notes/orchestration_log.md` with streams, branches, PRs, merge status
- [ ] Consistency / review log (`notes/review_log.md` or equivalent)
- [ ] Merged PR set for core features (data, analysis, paper or equivalent)
- [ ] One subagent and one skill created and used at least once
- [ ] Handoff files in `notes/` where streams depend on each other
- [ ] One clean run documented (or blockers documented)

---

## Day 4 Prep Instructions

Before leaving Day 3:

1. **Freeze scope:** Decide what will be in the final package. No new features on Day 4.
2. **Identify replication blockers:** Missing data? Hardcoded paths? Document in `notes/` or `replication/README.md`.
3. **Review replication template:** Skim `templates/replication_README.md`. You will fill it during Day 4 Sprint A.
4. **Prepare presentation outline:** Glance at `templates/presentation_outline.md`. Day 4 Sprint B will flesh it out.
5. **Optional:** If you use MCP (FRED, filesystem), ensure config is stable and document it (`docs/mcp_setup.md`); Day 4 focuses on replication README and packaging.

---

## Prompts and Examples

- **Copy-pasteable prompts:** [prompts/agent_prompts.md](prompts/agent_prompts.md)
- **Sample subagent:** [examples/sample_subagent.md](examples/sample_subagent.md)
- **Sample review log:** [examples/sample_review_log.md](examples/sample_review_log.md)

---

*Guidance: Quality over quantity. One clean run and one merged PR set beat many half-finished streams.*
