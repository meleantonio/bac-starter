# Module: Rules & Memories + AGENTS.md

## Objectives

By the end of this module, participants will:

- Create and use Cursor project rules (`.cursor/rules/*.mdc`) for economics-specific standards
- Distinguish user rules (global) vs project rules (repo-specific)
- Apply rule types: **Always Apply**, **Apply to Specific Files** (e.g. via `globs`), **Apply Intelligently**, **Apply Manually** (per [Rules](https://www.cursor.com/docs/context/rules))
- Create and maintain an `AGENTS.md` as a team-facing instruction file
- Prefer **User Rules**, **Team Rules**, and **`AGENTS.md`** for stable, teachable governance; **Memories** behavior has changed across releases—verify in Cursor Settings before relying on it in class

## Prerequisites

- Cursor installed with a project opened (your capstone repo or a practice repo)
- Basic familiarity with Markdown and `.mdc` (Markdown with optional frontmatter)
- Understanding that rules constrain and guide AI behavior

## Demo Script

### Setup

1. Open a project with at least one Python file and ideally a `docs/` or `references/` folder
2. Create `.cursor/rules/` if it does not exist: `mkdir -p .cursor/rules`
3. Have the Cursor Rules UI visible (Settings → Rules, or the rules entry in the Agent panel)

### Steps (numbered, instructor-facing)

1. **Introduce rule types (3 min)** (current Cursor naming)
   - **Always Apply**: every request (use sparingly; e.g., "never expose API keys")
   - **Apply to Specific Files**: when `globs` match (e.g. `**/*.py`)
   - **Apply Intelligently**: when the agent infers relevance
   - **Apply Manually**: only when @-invoked or explicitly attached

2. **Create a project rule (7 min)**
   - Create `.cursor/rules/python-economics.mdc`:
   ```markdown
   ---
   description: Python style for economics projects
   globs: ["**/*.py"]
   alwaysApply: false
   ---

   # Python Economics Style

   - Use type hints for function signatures.
   - Use Google-style docstrings.
   - Prefer `pandas` for tabular data; `numpy` for arrays.
   - Log data loading and transformations with `structlog` or `logging`.
   - Include unit tests for estimation and utility functions.
   ```
   - Explain: `globs` makes this **Apply to Specific Files** when editing `.py`; `alwaysApply: false` avoids global bloat

3. **Create a LaTeX rule (5 min)**
   - Create `.cursor/rules/latex-conventions.mdc`:
   ```markdown
   ---
   description: LaTeX and citation conventions for economics papers
   globs: ["**/*.tex", "**/*.bib"]
   alwaysApply: false
   ---

   # LaTeX Conventions

   - Use `natbib` with `\citet` and `\citep`.
   - Place figures in `figures/`, tables in `tables/`.
   - Use `siunitx` for numbers in tables.
   - Cite working papers as "Author (Year), working paper."
   ```

4. **Show user vs project rules (3 min)**
   - User rules: apply across all projects (e.g., "use Ruff for Python formatting")
   - Project rules: apply only in this repo
   - Economics-specific standards belong in **project** rules; personal preferences in **user** rules

5. **Introduce AGENTS.md (5 min)**
   - Create `AGENTS.md` at repo root:
   ```markdown
   # Agent Instructions — [Project Name]

   ## Project context
   This repo implements a [brief description]. Research question: [one sentence].

   ## Code standards
   - Python 3.10+; Ruff for formatting.
   - See `.cursor/rules/` for detailed conventions.

   ## Key paths
   - `src/` — core code
   - `data/` — input data (never commit raw data)
   - `outputs/` — results, figures, tables

   ## What to avoid
   - Do not hardcode paths or API keys.
   - Do not modify `references/bibliography.bib` without explicit instruction.
   ```
   - Explain: AGENTS.md is the human-readable "project brief" for any agent (Cursor, cloud agents, future teammates)

6. **Memories (optional / verify in product) (3 min)**
   - If your Cursor build still exposes **Memories**, show adding one (e.g. Chicago-style references)
   - **Otherwise** teach the same preference as a **User Rule** line
   - Rules + `AGENTS.md` are the stable baseline for the workshop

### Key Points to Emphasize

- **Rules reduce rework**. A well-written rule means the AI follows your conventions without you repeating them.
- **Project rules > user rules** for team repos. Everyone gets the same standards.
- **AGENTS.md** is the "front door" for agents—concise, structured, actionable.
- **Economists:** Python style, LaTeX conventions, citation standards, and data-handling rules are high-value rule targets.

## Hands-On Exercise

### Minimum Viable Path

1. **Create one project rule (15 min)**
   - Choose one: Python style, LaTeX conventions, or citation standards
   - Create `.cursor/rules/<topic>.mdc` with `globs` and `alwaysApply: false`
   - Include at least 4–5 concrete instructions
   - Test: ask the AI to "add a new function to compute the mean" or "add a figure to the paper" and verify it follows your rule

2. **Create AGENTS.md (15 min)**
   - At repo root, create `AGENTS.md` with:
     - Project context (1–2 sentences)
     - Code standards (bullet list)
     - Key paths and their purpose
     - What to avoid (2–3 items)
   - Test: ask the AI "What is this project about?" and see if it references AGENTS.md

3. **Optional: second rule (10 min)**
   - Add a rule for the other domain (Python or LaTeX)
   - Or add a citation rule: e.g., "Use `\citet` for narrative, `\citep` for parenthetical; abbreviate journal names"

### Extension Challenge

- **Convert rules to AGENTS.md**: Create a prompt that asks the AI to read `.cursor/rules/*.mdc` and produce a consolidated summary for AGENTS.md. Compare with your manual version.
- **Apply Intelligently-style rule**: Create a rule the agent should pick up by description/context (per UI: often “Apply intelligently”). Test with a task that clearly requires that rule.

## When You Get Stuck

| Symptom | Likely cause | Try |
|--------|---------------|-----|
| Rule not applied | Wrong glob or path | Check `globs` pattern; ensure file extension matches |
| AI ignores rule | Rule too long or vague | Shorten; use bullet points; be explicit |
| AGENTS.md not used | Agent may not always load it | Reference it explicitly: "See AGENTS.md for project context" |
| Conflicting rules | User + project rules clash | Prefer project rules for repo; simplify user rules |
| Rule in wrong format | Invalid frontmatter | Use `---` delimiters; valid YAML; `globs` as array |

## Expected Artifacts

- `.cursor/rules/python-economics.mdc` (or equivalent)
- `.cursor/rules/latex-conventions.mdc` (or equivalent)
- `AGENTS.md` at repo root
- Optional: `.cursor/rules/citation-standards.mdc`

## Key Prompts

**Generate a project rule**
```
I need a Cursor rule file for [Python/LaTeX/citations] in an economics research project. 
Create `.cursor/rules/[name].mdc` with:
- globs for the relevant file types
- alwaysApply: false
- 5–7 concrete instructions that economists care about (type hints, docstrings, citation format, etc.)
```

**Test that a rule is applied**
```
Add a new Python function `compute_median_income(data: pd.DataFrame, column: str) -> float`. 
Verify it follows our project's Python conventions (check .cursor/rules).
```

**Convert rules to AGENTS.md**
```
Read all files in .cursor/rules/ and produce an AGENTS.md that:
1. Summarizes the project standards in 2–3 sentences
2. Lists key paths and their purpose
3. States 3 things agents should avoid
Keep it under 30 lines.
```

**Create AGENTS.md from scratch**
```
Create an AGENTS.md for this economics project. Include:
- One-sentence research question
- Code standards (Python version, formatter, test framework)
- Key directories: src/, data/, outputs/, references/
- Two things to never do (e.g., hardcode paths, commit raw data)
```

**Generate a citation rule**
```
Create .cursor/rules/citation-standards.mdc for economics papers. 
Rules: use natbib, \citet vs \citep, how to cite working papers and NBER drafts, 
journal abbreviation style. Set globs for .tex and .bib.
```

## Further Reading

- Cursor docs — Rules for AI: https://www.cursor.com/docs/context/rules
- SPEC.md §6.1 (Rules & Memories, AGENTS.md)
- `create-rule` skill (if available): guidance for writing effective rules
