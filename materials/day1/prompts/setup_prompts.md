# Day 1 Setup Prompts — Copy-Paste Library

> Use these prompts in the **Agent** side panel during the Day 1 sprint. Replace `[TOPIC]` and bracketed placeholders with your project-specific text.

---

## Project Structure

### 1. Create Project Structure

```
Create a project structure for an economics research project on [TOPIC]. Include:
- src/ for Python modules
- scripts/ for runnable pipelines
- data/raw/ and data/processed/ (with .gitkeep)
- docs/ for project brief and design memo
- references/ for bibliography.bib
- output/ for figures and tables
- tests/ for pytest
- replication/ for README and run instructions
Add a minimal README.md and requirements.txt with pandas, numpy, statsmodels.
```

### 2. Minimal Python Skeleton

```
Add a minimal Python structure for an economics project: src/__init__.py, 
scripts/run_analysis.py (stub that prints "Analysis not yet implemented"), 
and a pyproject.toml or requirements.txt with pandas, numpy, statsmodels, pytest.
```

---

## Cursor Rules

### 3. Generate Python Rules

```
Generate Cursor rules for an economics research project that uses Python and LaTeX.
Create .cursor/rules/python-economics.mdc with:
- globs: ["**/*.py"]
- alwaysApply: false
- Instructions: PEP 8, max line length 120, type hints on public functions, 
  Google-style docstrings, prefer pandas for tabular data, numpy for arrays, 
  include unit tests for estimation functions.
```

### 4. Generate LaTeX Rules

```
Create .cursor/rules/latex-conventions.mdc for an economics paper:
- globs: ["**/*.tex", "**/*.bib"]
- Use natbib with \citet and \citep
- Figures in figures/, tables in tables/
- Use booktabs and siunitx for tables
- Descriptive labels (fig:..., tab:...)
```

### 5. Generate Citation Rule

```
Create .cursor/rules/citation-standards.mdc for economics papers:
- Use natbib; \citet for narrative, \citep for parenthetical
- Cite working papers as "Author (Year), working paper."
- Abbreviate journal names (e.g., AER, QJE, Econometrica)
- globs: ["**/*.tex", "**/*.bib"]
```

---

## AGENTS.md

### 6. Create AGENTS.md

```
Create an AGENTS.md file for my economics research project. Include:
- Project context: [1–2 sentences on research question and approach]
- Code standards: Python 3.10+, Ruff for formatting, pytest for tests
- Key paths: src/, data/, outputs/, references/
- What to avoid: hardcoded paths, commit raw data, modify bibliography without instruction
- Workflow: one branch per issue, PR before merge, consistency check before merge
Keep it under 40 lines.
```

### 7. AGENTS.md from Brief

```
Read docs/project_brief.md and create an AGENTS.md that summarizes:
1. Research question in one sentence
2. Code standards (Python, formatter, test framework)
3. Key directories and their purpose
4. Two things agents should never do
```

---

## .cursorignore

### 8. Set Up .cursorignore (General)

```
Generate a .cursorignore file for an economics research project. Include patterns for:
- .env and credentials (*.pem, credentials/, api_keys/)
- data/, data_raw/, outputs/, results/
- Common economics file types: *.csv, *.parquet, *.dta, *.sav
- Python cache and venv: __pycache__/, .venv/, venv/
- Large files: *.pdf, *.zip
Use # comments to organize sections.
```

### 9. .cursorignore for Sensitive Survey Data

```
Set up .cursorignore patterns for an economics project with sensitive survey data.
Exclude: data/, *_microdata*, *_individual*, *_confidential*, *_restricted*,
proprietary/, .env, credentials/, intermediate/, temp/, cache/.
Add a comment explaining why each section is excluded.
```

### 10. Verify Exclusions

```
I added data/ to .cursorignore. Confirm: can you access or summarize the contents 
of any file under data/? If not, say so clearly. If yes, list which files you can see.
```

---

## Project Brief

### 11. Write 1-Page Project Brief

```
Write a 1-page project brief for a research project on [TOPIC]. Include:
- Project title
- Research question (1–2 sentences, testable)
- Expected contribution (2–4 sentences)
- Data sources table (columns: Source, URL, Format, Coverage, Notes)
- Method approach (panel regression, event study, IV, etc.)
- Key deliverables and 4-day timeline
- Acceptance criteria
Use the structure in templates/project_brief.md.
```

### 12. Refine Research Question

```
My research question is: "[YOUR DRAFT QUESTION]". 
Make it more testable and specific. Suggest one main outcome variable and one key 
treatment or policy variable. Keep it to 1–2 sentences.
```

### 13. Fill Data Sources Table

```
I need to document data sources for [TOPIC]. Suggest 2–3 public data sources 
(FRED, World Bank, Eurostat, national statistics) with:
- Source name and URL
- Format (API, CSV, Stata)
- Key variables
- Time and geographic coverage
Format as a markdown table.
```

---

## Combined Setup

### 14. Full Day 1 Setup in One Go

```
I'm starting an economics research project on [TOPIC]. Do the following:
1. Create docs/project_brief.md with research question, contribution, data table, method
2. Create .cursor/rules/python-economics.mdc with globs for *.py
3. Create .cursorignore with data/, .env, outputs/, *.csv, *.dta, __pycache__/, .venv/
4. Create AGENTS.md with project context, code standards, key paths, what to avoid
Keep each artifact concise. Use templates/ structure where applicable.
```

---

## Context and Usage

- **Ask mode**: Use prompts 10, 12, 13 for research and verification (no file edits).
- **Agent mode**: Use prompts 1–9, 11, 14 for implementation (creates/edits files).
- **Context**: Attach **folders/files** to keep work scoped to the repo; ask the agent to **search the web** for literature or formulas; attach **data files** for data-aware tasks. Exact @ menu items differ by Cursor version—see [Prompting agents](https://www.cursor.com/docs/agent/prompting).
