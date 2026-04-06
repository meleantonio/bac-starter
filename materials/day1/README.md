# Day 1 Sprint Guide — Setup + GitHub + Capstone Start

> Complete runnable guide for the first day of the Agentic Coding for Economists workshop.
> Use this document as your primary sprint playbook; follow timeboxes and check deliverables.

---

## Sprint Objective

Launch both tracks in parallel:

1. **Tooling stack**: Cursor-first workflow, modes, context control, rules/memories
2. **Research project**: Repository, issue board, project brief, first PR

By end of day you will have a structured repo, a scoped research question, and guardrails (rules, AGENTS.md, .cursorignore) that keep AI assistance consistent and safe.

---

## Pre-Sprint Reading (Do Before Day 1)

Read these **before** the session. Paths from repo root `docs/workshop/`:

| Document | Purpose |
|----------|---------|
| [module_modes_and_context.md](../../docs/workshop/module_modes_and_context.md) | Agent vs Ask vs Plan modes; @mentions; tight vs wide context |
| [module_rules_memories_agentsmd.md](../../docs/workshop/module_rules_memories_agentsmd.md) | Project rules (.cursor/rules/), AGENTS.md, Memories |
| [module_cursorignore_privacy.md](../../docs/workshop/module_cursorignore_privacy.md) | .cursorignore patterns, privacy, exclusions for data |
| [github_bootcamp_en.md](../../docs/workshop/github_bootcamp_en.md) | Repo, branch, PR, issue, labels, agentic workflow pattern |

**Quick check**: Can you explain when to use Ask vs Agent mode? Do you know what `.cursorignore` excludes and why?

---

## Detailed Sprint Schedule (4 hours)

| Time | Block | Focus |
|------|-------|-------|
| 0:00–0:20 | Demo | Cursor-first workflow, modes, context control basics |
| 0:20–1:40 | Sprint A | Repo creation, issue board, labels, first branch/commit/PR/merge |
| 1:40–1:50 | Checkpoint | Unblockers, priorities, quick wins |
| 1:50–2:50 | Sprint B | Project brief, rules, .cursorignore, AGENTS.md |
| 2:50–3:40 | Guardrails | Refine and verify rules, memories, exclusions |
| 3:40–4:00 | Wrap-up | Verify deliverables, Day 2 prep |

---

## Sprint Block A: Repo + Issue Board + First PR (0:20–1:40)

### Timebox Warning

- **0:40**: If you haven't created your repo and cloned it locally, ask the instructor for help.
- **1:10**: If you don't have ≥8 issues on your board yet, simplify scope and create smaller issues.
- **1:30**: If your first PR isn't open yet, focus on getting one small issue merged—defer perfection.

---

### Step-by-Step Walkthrough

#### 1. Create Your Project Repository (15–20 min)

1. **Create** a new repository on GitHub (or fork the course starter repo).
   - Name: `[your-topic]-capstone` (e.g., `minimum-wage-youth-capstone`).
   - Initialize with README only, or use starter if provided.

2. **Clone** to your machine:
   ```bash
   git clone git@github.com:YOUR_USER/YOUR_REPO.git
   cd YOUR_REPO
   ```

3. **Verify**: `git status` runs, `main` branch exists.

#### 2. Set Up Issue Board and Labels (20–25 min)

4. **Create labels** (Settings → Labels) with these suggested names and colors:

   | Label | Color | Use |
   |-------|-------|-----|
   | `research-question` | Blue | Core question, scope |
   | `literature` | Light blue | Literature mapping, references |
   | `data` | Green | Data acquisition, ETL |
   | `model` | Purple | Specification, estimation |
   | `estimation` | Purple | Code, scripts |
   | `writing` | Orange | Paper, figures, tables |
   | `consistency-check` | Red | Review, verification |
   | `doc` | Gray | Documentation |

5. **Create ≥8 issues** for your capstone. Each issue = one concrete deliverable. Examples:

   - "Define research question and project brief"
   - "Add bibliography with 5 core references"
   - "Create data source map"
   - "Implement data loading script"
   - "Run baseline regression"
   - "Create summary statistics table"
   - "Add replication README"
   - "Review and consistency pass"

6. **Assign labels** to each issue. Add a short acceptance criterion in the description where possible.

#### 3. Complete One Issue End-to-End (25–35 min)

7. **Pick** the simplest issue (e.g., "Add project brief skeleton" or "Create .cursorignore").

8. **Create a branch**:
   ```bash
   git checkout -b feature/issue-N-short-description
   # e.g. git checkout -b feature/issue-1-project-brief
   ```

9. **Make changes** (manually or with Cursor Agent).

10. **Commit and push**:
    ```bash
    git add .
    git commit -m "Add project brief skeleton (issue #N)"
    git push -u origin feature/issue-N-short-description
    ```

11. **Open a Pull Request** on GitHub. Link to the issue: `Closes #N`.

12. **Merge** the PR (after self-review or instructor check). Delete the branch if prompted.

13. **Update local** `main`:
    ```bash
    git checkout main
    git pull
    ```

---

### If You Get Stuck (Block A)

| Symptom | Solution |
|---------|----------|
| Git auth fails | Re-check SSH key at https://github.com/settings/keys or use HTTPS + token |
| Can't create repo | Use instructor's shared org or a pre-made template fork |
| Too many/few issues | Aim for 8–12; each issue should be completable in 30–90 min |
| Branch/PR workflow unclear | Follow [github_bootcamp_en.md](../../docs/workshop/github_bootcamp_en.md) command cheatsheet |
| First PR feels too big | Pick a 1-file, 1-output issue (e.g., add README section) |

---

## Sprint Block B: Project Brief, Rules, .cursorignore, AGENTS.md (1:50–2:50)

### Timebox Warning

- **2:10**: If your project brief isn't drafted yet, use the template and fill in at least Research Question + one data source.
- **2:35**: If rules/AGENTS.md aren't in progress, copy from `materials/day1/examples/` and adapt.

---

### Step-by-Step Walkthrough

#### 1. Project Brief (25–30 min)

14. **Create** `docs/project_brief.md` using the template in `templates/project_brief.md`.

15. **Fill in**:
    - Project title (one line)
    - Research question (1–2 sentences, testable)
    - Expected contribution (2–4 sentences)
    - Data sources table (≥1 row with URL, format, notes)
    - Method approach (panel regression, event study, IV, etc.)
    - Key deliverables (checkboxes)
    - Timeline (4-day sprint table)

16. **Verify**: Research question is clear and data is accessible (or obtainable during sprint).

**Prompts**: Use `materials/day1/prompts/setup_prompts.md` — "Write a 1-page project brief for a research project on [TOPIC]..."

#### 2. Cursor Rules (15–20 min)

17. **Create** `.cursor/rules/` if missing:
    ```bash
    mkdir -p .cursor/rules
    ```

18. **Add** at least one rule file:
    - `python-economics.mdc` for Python (globs: `**/*.py`)
    - `latex-conventions.mdc` for LaTeX (globs: `**/*.tex`, `**/*.bib`)

19. **Structure** each rule:
    ```markdown
    ---
    description: Python style for economics projects
    globs: ["**/*.py"]
    alwaysApply: false
    ---
    # Python Economics Style
    - Use type hints for function signatures.
    - Use Google-style docstrings.
    - Prefer pandas for tabular data; numpy for arrays.
    - Include unit tests for estimation and utility functions.
    ```

**Example**: See `materials/day1/examples/sample_rules.mdc`.

#### 3. .cursorignore (10–15 min)

20. **Create** `.cursorignore` at repo root with sections:
    - Environment and secrets: `.env`, `.env.*`, `credentials/`, `*.pem`
    - Data: `data/`, `data_raw/`, `outputs/`, `*.csv`, `*.dta`, `*.parquet`
    - Build/cache: `__pycache__/`, `.venv/`, `venv/`, `*.pyc`
    - Large files: `*.pdf`, `*.zip`

21. **Add** economics-specific patterns if needed: `*_confidential*`, `*_microdata*`, `proprietary/`.

22. **Verify**: Ask in Chat: "Can you summarize the contents of data/?" — AI should not access excluded paths.

**Prompts**: Use `materials/day1/prompts/setup_prompts.md` — "Set up .cursorignore patterns for an economics project with sensitive survey data..."

#### 4. AGENTS.md (10–15 min)

23. **Create** `AGENTS.md` at repo root. Include:
    - Project context (research question, main approach, key data)
    - Code standards (Python version, Ruff, pytest, structure)
    - Key paths: `src/`, `data/`, `outputs/`, `references/`
    - What to avoid (hardcoded paths, commit raw data, etc.)
    - Workflow rules (one branch per issue, PR before merge)

**Example**: See `materials/day1/examples/sample_agentsmd.md`.

**Prompts**: Use `materials/day1/prompts/setup_prompts.md` — "Create an AGENTS.md file for my economics research project..."

---

### If You Get Stuck (Block B)

| Symptom | Solution |
|---------|----------|
| Unsure about issue scope | Write smaller issues: one file, one output |
| Rule not applied | Check `globs` pattern; ensure file extension matches |
| AI still sees excluded file | Restart Cursor; verify `.cursorignore` at repo root |
| Project brief too vague | Use "who, what, when, where" — specific question + one data source |
| AGENTS.md too long | Keep under 40 lines; bullets only |

---

## Guardrails Block (2:50–3:40)

24. **Refine** rules: Test with "Add a function that computes X" — verify style matches.

25. **Refine** AGENTS.md: Ask "What is this project about?" — AI should cite AGENTS.md.

26. **Refine** .cursorignore: Confirm no sensitive data is indexed (test with a dummy file).

27. **Commit** all guardrails:
    ```bash
    git add .cursor/rules/ .cursorignore AGENTS.md docs/project_brief.md
    git commit -m "Add project guardrails: rules, .cursorignore, AGENTS.md, brief"
    git push
    ```

---

## Extension Challenges (For Fast Participants)

- **Second rule**: Add LaTeX or citation rule if you only did Python (or vice versa).
- **Modes playbook**: Create `notes/modes_playbook.md` with when you use Ask vs Agent vs Plan.
- **Context patterns**: Create `notes/context_patterns.md` with tight/wide examples from your work.
- **Extra issues**: Add 2–3 more implementation issues with acceptance criteria.

---

## End-of-Day Deliverables Checklist

- [ ] Project brief (v1) in `docs/project_brief.md`
- [ ] Issue board with ≥8 issues and labels
- [ ] First merged PR (any issue)
- [ ] `.cursor/rules/*.mdc` (≥1 file) committed
- [ ] `.cursorignore` at repo root committed
- [ ] `AGENTS.md` at repo root committed
- [ ] All changes pushed to `main`

---

## Day 2 Prep Instructions

1. **Read** before Day 2:
   - `docs/workshop/setup_guide.md` — Context control section (if present)
   - Verification loop patterns (brief recap in Day 2 demo)

2. **Prepare**:
   - Bring your research question and data source list.
   - Have `docs/project_brief.md` and `references/bibliography.bib` ready to extend.

3. **Expect** Day 2 focus: literature mapping, research design memo, data/method plan, implementation issues with acceptance criteria.

---

## Prompt Library

Copy-paste prompts are in `materials/day1/prompts/setup_prompts.md`.

Example outputs are in `materials/day1/examples/`:
- `sample_project_brief.md`
- `sample_rules.mdc`
- `sample_agentsmd.md`
