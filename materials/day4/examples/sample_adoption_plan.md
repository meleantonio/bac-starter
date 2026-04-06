# 30-Day Post-Workshop Adoption Plan — Sample Completed Example

> A completed 30-day adoption plan for an economist integrating agentic workflows. Use as reference during Day 4.

---

# 30-Day Post-Workshop Adoption Plan

> Integrate Cursor-first agent workflows into my main empirical project (labor economics / minimum wage).

---

## Overview

**Goal:** Apply the agentic workflow from the capstone to my ongoing minimum-wage paper. By Day 30, I want: rules and AGENTS.md in place, one real task completed via Agent, one subagent (reviewer) used on a PR, and a weekly "agent sprint" slot established.

---

## Week 1 — Consolidate

**Goal:** Lock in personal setup and project governance.

- [x] Set up Cursor rules for my main research project (`.cursor/rules/economics.mdc` for coefficient interpretation, units, citation style)
- [x] Add `.cursorignore` for `data/`, `.env`, `*.pem`, `credentials*`
- [x] Create `AGENTS.md` in my main project repo with: run command, replication path, "use Agent for data cleaning and spec exploration"
- [x] Document preferred mode usage: Agent for multi-file changes and PRs; Ask for quick lookups and explanations
- [ ] Other: Add `.cursor/rules/replication.mdc` with checklist for clean-run verification

---

## Week 2 — Apply

**Goal:** Use the agent workflow on one real research task.

- [x] Pick one concrete task: Add a placebo specification (different time window) to the robustness section
- [x] Run it with Agent mode: "Implement a placebo regression using 2005–2009 as placebo period; add to results/placebo_estimates.csv"
- [x] Document what worked: Agent created script, ran it; I had to fix one path. Logged in `notes/agent_sprint_log.md`
- [ ] Create at least one issue and close it via PR (e.g., "Add placebo robustness check" → branch → PR → merge)
- [ ] Other: Try one data-cleaning task (e.g., "Standardize state FIPS codes in panel.csv")

---

## Week 3 — Expand

**Goal:** Add subagents, skills, or parallel execution.

- [x] Create one subagent: `pr-reviewer` at `.cursor/agents/pr-reviewer.md` (from workshop template)
- [ ] Add or adopt one skill: `replication-checker` — verify pipeline runs from clean state before each submission draft
- [ ] Try one parallel execution: Use worktree for "robustness branch" while main branch gets paper edits
- [ ] Other: Invoke reviewer on my next PR before asking a colleague

---

## Week 4 — Sustain

**Goal:** Make routines stick and share with colleagues.

- [ ] Establish a weekly "agent sprint" slot: Fridays 2–3 pm — one focused Agent task (refactor, docstrings, robustness check)
- [ ] Share one workflow tip with coauthor: "Use pr-reviewer subagent before sending me a PR"
- [ ] Update this adoption plan based on what worked (retrospective bullets)
- [ ] Other: Present the agentic workflow at a 15-min lab meeting

---

## Check-in Notes

| Week | Done? | Wins | Blockers |
|------|-------|------|----------|
| 1 | [x] | Rules + AGENTS.md in place; .cursorignore clean | None |
| 2 | [ ] | Placebo spec implemented | Haven't closed an issue via PR yet — will do in Week 3 |
| 3 | [ ] | pr-reviewer created | Skill creation took longer than expected |
| 4 | [ ] | | |

---

## Resources to Revisit

- [x] Cursor docs: Modes, Rules, Subagents, Skills
- [x] Workshop materials: `materials/day3/README.md`, `docs/workshop/module_subagents.md`
- [x] Review log template: `templates/review_log.md`
- [x] Replication README template: `templates/replication_README.md`

---

*Guidance: Check off items as you go. Adjust actions to fit your workload. Quality over quantity.*
