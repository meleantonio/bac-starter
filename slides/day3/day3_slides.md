---
marp: true
theme: default
paginate: true
header: "Agentic Coding for Economists"
footer: "Antonio Mele | Universita di Milano-Bicocca | April 2026"
---

# Day 3: Parallel Agent Execution Sprint

https://agentic-coding-for-economists.vercel.app/i/bac

## Agentic Coding for Economists
### Antonio Mele | Università di Milano-Bicocca | April 7–10, 2026

---

# Day 2 Recap

**What we built:**
- Spec-driven development: research question → design → pipeline
- Literature map, hypothesis refinement, data plan, method choice
- One-page research design with full specs (requirements, tasks, intent)
- Bibliography file and prioritized implementation task list

**Context discipline:** Tight vs wide context, @mentions, codebase queries

---

# Day 3 Goals

1. **MCP:** Model Context Protocol — FRED API, filesystem, Stata/MATLAB/R on your machine, when it adds value
2. **Subagents:** Specialized agents for recurring roles (reviewer, replicator, bibliographer)
3. **Agent Skills:** Reusable workflows with SKILL.md and skill-creator principles
4. **Cloud Agents:** Remote execution, branch handoff, review-before-merge
5. **Swarm Orchestration:** Multiple coordinated agents — GitHub issues, labels, parallel vs sequential Cloud Agent runs

**Definition of Done (Day 3):** Full harness (skills + subagents + swarms), working prototype, consistency log, merged PRs

---

# What is MCP?

**MCP** = Model Context Protocol

- A standard for connecting AI models to **external tools** (APIs, databases, filesystems)
- Cursor invokes MCP servers; the AI then "sees" tools and resources they expose
- Use case for economists: pull FRED series, read data from controlled folders, search the web — all within a single chat
- **Local statistical software:** MCP can bridge to **Stata**, **MATLAB**, or **R** on your machine (via appropriate servers), so the agent can run batch jobs, scripts, or pull outputs in your environment—with your approval

**MCP = bridges to real tools.** The AI gains structured access instead of hallucinating data.

---

# mcp.json Configuration

**Locations:**
- **Global:** `~/.cursor/mcp.json` — applies to all projects
- **Project:** `.cursor/mcp.json` — shared with team via git (ideal for course repos)

**Security:** Never put API keys in `mcp.json` in git. Use `env` with `${VAR}`.

---

# FRED API Example

```json
{
  "mcpServers": {
    "mcp-fredapi": {
      "command": "uv",
      "args": [
        "--directory", "~/mcp-fredapi",
        "run", "--with", "mcp", "--with", "httpx",
        "mcp", "run", "server.py"
      ],
      "env": {
        "FRED_API_KEY": "${FRED_API_KEY}"
      }
    }
  }
}
```

**Key from:** https://fredaccount.stlouisfed.org/apikeys

---

# When MCP Adds Value vs Overkill

| Adds value | Overkill |
|------------|----------|
| Recurring data pulls (FRED, ECB, BIS) | One-off data download (browser + save) |
| Scoped filesystem access (e.g. `data/` only) | Single analysis (manual run) |
| Web search for literature | Heavy custom tooling |
| Local Stata/MATLAB/R workflows (MCP bridge to your machine) | — |

**Economists:** FRED is the obvious win. Start with one MCP.

---

# What Are Subagents?

**Subagents** are specialized AI assistants with their own context window.

- Each gets its own **prompt**, **tools**, and optionally a different **model**
- Use when you need: **context isolation**, **parallel work**, or **role specialization**
- Differ from main agent: focused on one job; from skills: separate context

**Economics example:** "Have pr-reviewer review the code changes and bibliographer check the references section" — two subagents in parallel.

---

# Subagent Format: `.cursor/agents/*.md`

Each subagent is a markdown file with **YAML frontmatter** and a prompt body:

| Frontmatter | Purpose |
|-------------|---------|
| `name` | Invocation (e.g. `/pr-reviewer`) |
| `description` | When Agent delegates — *be specific* |
| `model` | `fast` or `inherit` |
| `readonly` | `true` for reviewers |

**Scope:** `.cursor/agents/` = project-only | `~/.cursor/agents/` = all projects

**Description drives delegation.** Vague → Agent rarely uses it.

*Verify field names and UI labels in your Cursor version.* Docs: https://www.cursor.com/docs/agent/subagents

---

# Subagent Example: PR Reviewer

```markdown
---
name: pr-reviewer
description: PR review specialist for econometric code.
  Use when reviewing pull requests for consistency,
  statistical correctness, and style.
model: fast
readonly: true
---

You are a rigorous code reviewer for econometric projects.

When invoked on a PR:
1. **Consistency**: Project rules, naming, patterns
2. **Correctness**: Coefficients, SEs, missingness, units
3. **Style**: Docstrings, citations, README

Report: pass / needs changes + line-level suggestions.
```

---

# Role Specialization: Reviewer, Replicator, Bibliographer

- **pr-reviewer:** Consistency, correctness, style on PRs. Check coefficient interpretations, unit labels, citation format.
- **replicator:** Verify pipeline runs from clean state; no hardcoded paths; reproducible output hash.
- **bibliographer:** Standardize .bib entries, fix journal abbreviations, cross-check in-text citations.

**One clear role per subagent.** Avoid generic "helper" agents.

---

# When to Use Subagents vs Main Agent vs Skills

| Use | When |
|-----|------|
| **Subagent** | Multi-step review, long exploration, parallel streams |
| **Skill** | Single-purpose quick task (e.g. generate changelog) |
| **Main agent** | General orchestration, decisions, merging |

**Invoke explicitly:** "Use the pr-reviewer subagent to review PR #42" or `/pr-reviewer review this PR`

---

# What Are Skills?

**Skills** extend the agent with reusable workflows.

- Loaded when the **description** matches the user request
- Unlike subagents: **no separate context** — they augment the main agent
- Same pattern: Cursor-native vs folderized (Claude Code, Codex)

**Example trigger:** "Verify that my pipeline in `scripts/run_analysis.py` is reproducible" → replication-checker skill loads

---

# SKILL.md Structure

**Anatomy:**
- **Frontmatter:** `name`, `description` (required). Description is the primary trigger.
- **Body:** instructions, workflows, when to read `references/` or `scripts/`
- **Optional:** `references/`, `scripts/`, `assets/` for progressive disclosure

**Progressive disclosure:** Keep SKILL.md under ~500 lines. Move detailed checklists to `references/`.

---

# Skill-Creator Principles

1. **Concise is key:** Context window is shared. Only add what the agent doesn't already have.
2. **Degrees of freedom:** Low (scripts, strict steps) for fragile ops; high (text guidance) for variable decisions.
3. **Progressive disclosure:** SKILL.md stays lean; load `references/` or `scripts/` only when needed.

**Validate-iterate:** Use the skill on a real task. Fix what breaks.

---

# Building the Replication-Checker Skill

```markdown
---
name: replication-checker
description: Verifies that research pipelines run from clean
  state with no hardcoded paths, declared dependencies,
  and reproducible output. Use when checking replication
  readiness or validating run instructions.
---

# Replication Checker

When invoked:
1. Identify main entry point (script, notebook, Make target)
2. Check for hardcoded paths — see references/replication_checklist.md
3. Verify dependencies: requirements.txt, environment.yml
4. Run minimal/dry-run; report success or failure

Output: green/yellow/red, blockers, recommendations, run command
```

---

# Skill Taxonomy

| Skill | Trigger phrases | Degree of freedom |
|-------|-----------------|-------------------|
| replication-checker | verify replication, check pipeline | Medium |
| literature-mapper | standardize bib, map references | Medium |
| data-contract-enforcer | validate data, check units | Low (script-heavy) |
| paper-polisher | polish paper, citation hygiene | High |

**Cursor vs folderized skills:** Same pattern. Cursor-native under Cursor paths; pattern transfers to Claude Code, Codex.

---

# What Are Cloud Agents?

**Cloud Agents** (formerly Background Agents) run in the cloud on isolated VMs.

- They **clone your repo**, work on a **branch**, and produce a **PR**
- You can continue working locally while they run
- Use for: doc generation, refactors, multi-file changes

**Handoff flow:** Task → Agent runs remotely → PR created → **You review, then merge**

Official docs: https://www.cursor.com/docs/background-agent

---

# Branch Handoff Protocol

1. **Before launch:** Create or specify the branch; ensure it's based on current `main`
2. **Task description:** Clear scope, file paths, "work on branch X"
3. **During run:** Agent clones, checks out branch, executes. You keep working.
4. **On completion:** Agent pushes branch, opens PR
5. **Review:** Open PR, read diff, run tests. Use pr-reviewer subagent.
6. **Decision:** Merge, request changes, or close

---

# Safety and Prompt Injection Awareness

**Safety rules:**
- **No merge without review** — agent output can be wrong or off-scope
- **Branch isolation** — work stays on branch until you merge
- **No secrets in prompts** — use env vars; add `.env` to `.cursorignore`
- **Sanitize external input** — avoid piping raw user text into agent prompts

**Prompt injection:** Malicious content in inputs that steers the agent. Lower risk when you control inputs (your code).

---

# Review-Before-Merge Protocol

**Checklist before merging a Cloud Agent PR:**
- Run tests
- Spot-check 3 random files
- Verify no logic changes unless requested
- No hardcoded paths or secrets in diff

**Key prompt:** "Generate docstrings for all Python files in `scripts/`. Use Google-style. Work on branch `bg/docstrings`. Do not modify function bodies."

---

# What Is a Swarm?

A **swarm** is **several agents coordinated** toward one project outcome — not a single prescribed toolchain.

- Combine **foreground Agent**, **subagents**, **skills**, and **Cloud Agents** as needed
- Orchestration can be **human-led**, **scripted**, or **agent-assisted** (planner creates issues; implementers execute)
- **GitHub + Cloud Agents** is one practical pattern; adapt labels and tools to your lab

---

# GitHub as the Control Plane

**Issues = units of work.** Make dependencies explicit:

- **Labels** (examples): `parallel`, `sequential`, `blocked-by:#12`, `ready`
- **Project columns** or milestones for waves: Wave A (parallel) → Wave B (after merge of #5)
- Planner (you or an agent) opens issues with **acceptance criteria**; sub-orchestrators triage and assign Cloud Agent runs

**Rule of thumb:** Independent tasks → parallel Cloud Agents; dependent tasks → sequential launches after prior PR merges.

---

# From Issues to PRs (Cloud Agents)

As in **Cloud Agents** above: each issue can drive one **branch** and one **Cloud Agent** run when the task is large enough to isolate.

`GitHub Issues` → `Labels / deps` → `Cloud Agent` → `PR → review`

Foreground Agent on your machine is still valid for short edits.

---

# Layered Orchestration

**Three layers** (illustrative):

- **Planner:** Creates or refines the issue graph (human or main Agent). Outputs: labeled issues, milestones.
- **Implementation swarm:** Cloud Agents (and humans) work issues in parallel or sequence per labels.
- **Review / consistency swarm:** Subagents + skills (`pr-reviewer`, `replicator`, replication-checker); optional “review lead” Agent pass across PRs

Sub-orchestrators can be **different chats** or **different Cloud Agent tasks** with narrow prompts.

---

# Handoffs and Ledger (Still Essential)

**Branches:** e.g. `feat/hank-ss`, `feat/hank-irf` — one coherent branch per issue when using Cloud Agents. Merge only after review; keep `main` stable.

**Handoff files:** `notes/handoff_*.md` — column names, units, steady-state outputs IRFs consume

**Orchestration log:** `notes/orchestration_log.md` — Stream | Branch | Issue | Status | PR | Reviewer

---

# Example: HANK + Monetary Policy (Issues)

**Parallel** (no ordering across these): literature & BibTeX hygiene; test harness / CI stub; data download + cleaning skeleton for macro time series.

**Sequential:** steady-state / calibration module → shock definitions & IRF computation → aggregation & welfare table → paper section.

| Issue (sketch) | Label | Cloud Agent? |
|----------------|-------|--------------|
| #1 SS solver + calibration | sequential / wave 1 | Yes |
| #2 Monetary shock IRFs | blocked-by #1 | Yes, after #1 merges |
| #3 Heterogeneity aggregation | blocked-by #2 | Often sequential |
| #4 Lit review + bib | parallel | Yes or foreground |
| #5 Figures + policy section | blocked-by #3 | Yes |

---

# Example: Branches and Commands

```bash
git checkout main && git pull
git checkout -b feat/hank-ss
# ... launch Cloud Agent on issue #1 for this branch; open PR when done.
```

**After #1 merges:** create `feat/hank-irf` from updated `main`; launch agent for issue #2.

**Optional further reading** (other orchestration metaphors): https://github.com/steveyegge/gastown

---

# Safety Rules: No Merge Without Review

**Before merging:**
1. Run **pr-reviewer subagent** on each PR
2. Run **replication-checker skill** on the combined pipeline
3. Merge in dependency order (e.g. data → equilibrium → IRFs → paper)

**Swarm lab protocol:** Phase 1 Setup (15 min) → Phase 2 Parallel (90 min) → Phase 3 Review & Merge (45 min) → Phase 4 Verification (15 min)

---

# Definition of Done for Day 3

1. Full harness: at least one subagent (e.g. pr-reviewer) and one skill (e.g. replication-checker)
2. Working prototype: scripts, notebook, or paper skeleton
3. Consistency / review log: `notes/orchestration_log.md`
4. Merged PRs for core pipeline components (data, analysis, paper)

**Artifacts:** `.cursor/agents/*.md`, `.cursor/skills/*`, `notes/handoff_*.md`

---

# Day 3 Deliverables

| Artifact | Location |
|----------|----------|
| Subagent(s) | `.cursor/agents/pr-reviewer.md` |
| Skill(s) | `.cursor/skills/replication-checker/` |
| Orchestration log | `notes/orchestration_log.md` |
| Handoff files | `notes/handoff_*.md` |
| Merged PRs | GitHub |

---

# Day 4 Preview: Integration, Replication, Presentation

**Tomorrow we cover:**
- Replication protocol: clean-run checklist, fail-fix-rerun cycle
- Packaging for reproducibility: README-first, dependency pinning
- 30-day adoption plan
- Course wrap-up and next steps

**Deliverables:** Mini replication package, replication README, 5–7 min presentation
