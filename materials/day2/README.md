# Day 2 Sprint Guide — Research Pipeline

> Complete runnable guide for the second day of the Agentic Coding for Economists workshop.
> Use this document as your primary sprint playbook; follow timeboxes and check deliverables.

---

## Sprint Objective

Turn your topic and research question into a **testable execution path**:

1. **Literature mapping**: Core references (empirical, theoretical, or macro as relevant), hypothesis refinement, contribution framing
2. **SDD artifacts**: Intent, **EARS-style** requirements, design, and tasks --- in `docs/research_design_memo.md` and/or separate `docs/requirements.md`, `docs/design.md`, with the memo linking to heavier files as needed
3. **Data/method plan**: Data source map (or simulation/calibration inputs for theory/macro), implementation issues with acceptance criteria
4. **Context control**: Notes on what to include/exclude, @mentions plan, verification loop patterns

By end of day you will have a prioritised implementation backlog and clear specs for Days 3–4.

---

## Pre-Sprint Reading (Do Before Day 2)

Read these **before** the session. Paths from repo root:

| Document | Purpose |
|----------|---------|
| [setup_guide.md](../../docs/workshop/setup_guide.md) | Context control section (tool setup and verification) |
| [module_modes_and_context.md](../../docs/workshop/module_modes_and_context.md) | @mentions, tight vs wide context (recap) |
| Day 1 `notes/modes_playbook.md` (if created) | Your personal Ask vs Agent vs Plan choices |

**Verification loop patterns** (recap from demo): acceptance criteria per issue → implement → consistency check → fail-fix-rerun. Ask the agent to **search the web** for literature; attach **folders** or ask to **search the codebase** to stay in-repo (exact @ menu varies by Cursor version).

---

## Detailed Sprint Schedule (4 hours)

| Time | Block | Focus |
|------|-------|-------|
| 0:00–0:20 | Demo | Literature → hypothesis → method path; context control depth |
| 0:20–1:40 | Sprint A | Literature map, research design memo, bibliography |
| 1:40–1:50 | Checkpoint | Hypothesis clarity, data access blockers |
| 1:50–2:50 | Sprint B | Data/method plan, implementation issues, workflow_state.md |
| 2:50–3:30 | Context Control | Notes, prompt scaffolds, @mentions plan |
| 3:30–4:00 | Wrap-up | Verify deliverables, Day 3 prep |

---

## Sprint Block A: Literature Mapping + Research Design (0:20–1:40)

### Timebox Warning

- **0:50**: If you don't have 5+ core references yet, cap scope: pick 5–8 and note gaps.
- **1:10**: If your research design memo isn't drafted, use the template and fill at least Research Question, Hypothesis, Data Description.
- **1:30**: If bibliography isn't in BibTeX, export from Google Scholar/Zotero or manually add 5 entries.

---

### Step-by-Step Walkthrough

#### 1. Literature Mapping (25–35 min)

1. **Identify** 5–8 core papers for your topic. Use:
   - Google Scholar, EconLit, NBER, RePEc
   - Instructor-provided reading list (if any)
   - Web search from the Agent panel: "Search the web: key papers on [TOPIC] 2020–2024"

2. **Create** or extend `references/bibliography.bib` with BibTeX entries.

3. **Map** each reference to your contribution:
   - What does it find?
   - How does your question differ (data, method, sample)?
   - One-line relevance for your design memo.

4. **Document** in `docs/research_design_memo.md` under "Key references (3–5)".

**Prompts**: Use `materials/day2/prompts/research_prompts.md` — literature mapping section.

#### 2. Research Design Memo (35–45 min)

5. **Open** `docs/research_design_memo.md` (copy from `templates/research_design_memo.md` if missing).

6. **Fill in** all sections:
   - Research Question (1–2 sentences)
   - Motivation and Literature Context (2–4 paragraphs + key references)
   - Hypothesis / Hypotheses (H1, H2, …)
   - Data Description (table: source, access, variables, sample, unit of observation)
   - Empirical / Theoretical Strategy (spec, model, software)
   - Identification Strategy (if applicable: policy change, instrument, RDD)
   - Expected Results
   - Limitations and Robustness
   - References (link to `references/bibliography.bib`)

7. **Verify**: Hypotheses are testable; data is described with access notes.

**Example**: See `materials/day2/examples/sample_research_design.md`.

#### 3. Bibliography (15–20 min)

8. **Add** 8–10 BibTeX entries to `references/bibliography.bib`.

9. **Ensure** entries have: author, title, journal/year (or type), doi or url when available.

10. **Cross-check**: All key references in the design memo are in the bib file.

**Example**: See `materials/day2/examples/sample_bibliography.bib`.

---

### If You Get Stuck (Block A)

| Symptom | Solution |
|---------|----------|
| Too many sources | Cap to 8–10 core references; note gaps in design memo |
| Data access uncertain | Document access constraints and fallback datasets in data description |
| Method unclear | Write two alternative approaches and decide in checkpoint |
| Hypothesis too vague | Use "If X, then Y; measured by Z" structure |
| BibTeX format errors | Use `@article`, `@inproceedings`, `@misc`; check commas and braces |

---

## Sprint Block B: Data/Method Plan + Implementation Issues (1:50–2:50)

### Timebox Warning

- **2:10**: If your data source map isn't filled, add at least 2 sources with access method.
- **2:30**: If you don't have ≥5 implementation issues with acceptance criteria, decompose one big task into 2–3 smaller ones.

---

### Step-by-Step Walkthrough

#### 4. Data Source Map (20–25 min)

11. **Open** `docs/data_source_map.md` (copy from `templates/data_source_map.md` if missing).

12. **Fill** one row per source:
    - Source Name, URL/Location
    - Access Method (public, restricted, API, request required)
    - Format (CSV, Stata, API)
    - Key Variables
    - Time Coverage, Geographic Coverage
    - Notes/Caveats (versioning, breaks, access steps)

13. **Add** access setup checklist items (e.g., FRED API key, Eurostat bulk download).

14. **Cross-check** with `research_design_memo.md` data description.

#### 5. Implementation Issues (25–30 min)

15. **Review** existing issues from Day 1. Ensure each has:
    - Clear title
    - Description with acceptance criteria (what "done" looks like)
    - Label (data, model, estimation, writing, consistency-check, etc.)
    - Priority (optional: P0, P1, P2)

16. **Add or refine** issues for:
    - Data acquisition (download, ETL script)
    - Data cleaning and merging
    - Baseline regression / main specification
    - Robustness checks (if time permits)
    - Tables and figures
    - Replication README
    - Consistency/review pass

17. **Prioritise**: Order issues so critical path (data → estimation → tables) is clear. Mark blocking issues.

#### 6. Workflow State (Optional, 10 min)

18. **Create** `notes/workflow_state.md` (or similar) as a lightweight plan/task log:
    - Current phase (e.g., "Data acquisition")
    - Next 3 tasks
    - Blockers
    - Last updated

19. **Use** this for agent handoffs and personal tracking. Update as you progress.

---

### If You Get Stuck (Block B)

| Symptom | Solution |
|---------|----------|
| Data source map empty | Start with FRED, World Bank, Eurostat; document access steps |
| Issues too coarse | Split: "Implement data loader" → "Download Eurostat CSV", "Write load script", "Add unit tests" |
| Acceptance criteria vague | Use "Script runs without error and produces X in output/" |
| workflow_state unclear | Keep it minimal: phase + next tasks + blockers |

---

## Context Control Block (2:50–3:30)

20. **Create** `notes/context_patterns.md` (or extend from Day 1) with:
    - When to **search the web** (literature, formulas, external APIs)
    - When to scope **repo/folder context** (stay in repo, refactor)
    - When to use `@Files` (specific data or config)
    - One "tight context" example (single file)
    - One "wide context" example (cross-file integration)

21. **Create** or extend `notes/modes_playbook.md`:
    - Ask: literature lookup, design refinement, debugging
    - Agent: implementation, file edits, pipeline scripts
    - Plan: complex multi-step breakdown before coding

22. **Document** prompt scaffolds: e.g., "Before implementing X, read docs/research_design_memo.md and docs/data_source_map.md."

23. **Commit** all Day 2 artifacts:
    ```bash
    git add docs/ references/ notes/
    git commit -m "Day 2: research design memo, bibliography, data map, context notes"
    git push
    ```

---

## Extension Challenges (For Fast Participants)

- **Deep literature**: Add 3–5 more references and a short "literature gap" paragraph.
- **Alternative specification**: Document a second empirical approach as robustness.
- **Stubs**: Create empty scripts for data load, estimation, table export (with docstrings).
- **workflow_state template**: Produce a reusable template for future projects.

---

## End-of-Day Deliverables Checklist

- [ ] Full SDD coverage (intent, requirements, design, tasks) in memo ± linked docs
- [ ] One-page hub memo in `docs/research_design_memo.md` (links or embeds the above)
- [ ] Bibliography with 8–10 entries in `references/bibliography.bib`
- [ ] Data source map in `docs/data_source_map.md` (or documented model/simulation inputs)
- [ ] Prioritised implementation backlog (≥8 issues, each with acceptance criteria)
- [ ] Context control notes (context_patterns.md and/or modes_playbook.md)
- [ ] All changes committed and pushed

---

## Day 3 Prep Instructions

1. **Read** before Day 3:
   - `docs/workshop/module_subagents.md` — Subagents for PR review, replication
   - `docs/workshop/module_skills_skillcraft.md` — Skills for replication checker, literature mapper

2. **Prepare**:
   - Have your implementation issues ready; expect to run parallel workstreams.
   - Know your blocking tasks (usually data access).

3. **Expect** Day 3 focus: parallel agent execution, subagents, skills, prototype build, consistency/review pass.

---

## Prompt Library

Copy-paste prompts are in `materials/day2/prompts/research_prompts.md`.

Example outputs are in `materials/day2/examples/`:
- `sample_research_design.md`
- `sample_bibliography.bib`
