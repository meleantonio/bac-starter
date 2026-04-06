# Agent Instructions — Minimum Wage / Youth Employment Capstone

This file guides AI agents working on this economics research project. Update it as you refine scope and conventions.

---

## Project Context

This project examines the causal effect of minimum wage increases on youth (ages 15–24) employment across EU countries. We use Eurostat data, a difference-in-differences design with staggered adoption, and heterogeneity by institutional context. Data: Eurostat LFS and minimum wage series; OECD institutional indicators. Method: TWFE and Callaway-Sant’Anna; Python (pandas, linearmodels).

---

## Coding Standards

- **Python**: PEP 8, max line length 120, type hints on public functions, Google-style docstrings.
- **Structure**: `src/` for modules, `scripts/` for pipelines; no hardcoded paths or machine-specific config.
- **Dependencies**: Declared in `requirements.txt`; no undeclared imports.
- **Testing**: pytest for critical logic; aim for reproducibility over coverage.

---

## LaTeX Standards

- Use `natbib` for citations; `\citet{}` and `\citep{}` as appropriate.
- Tables: `booktabs` (`\toprule`, `\midrule`, `\bottomrule`).
- Figures and tables: descriptive labels (`fig:...`, `tab:...`), captions above tables, below figures.
- Compilation: pdflatex or equivalent; document engine in README if non-standard.

---

## Key Paths

| Path | Purpose |
|------|---------|
| `src/` | Core Python modules |
| `scripts/` | Runnable pipelines and analysis |
| `data/raw/` | Raw inputs (not committed) |
| `data/processed/` | Processed datasets |
| `output/` | Figures, tables, results |
| `references/` | bibliography.bib |
| `docs/` | project_brief.md, research_design_memo.md, data_source_map.md |
| `replication/` | README and run instructions |

---

## Workflow Rules

- **Branching**: One branch per issue; names like `issue-N-short-description`.
- **Merge**: PR required; no direct push to `main`.
- **Before merge**: Consistency pass (rules, docs, code aligned) and replication sanity check.

---

## What to Avoid

- Do not hardcode paths or API keys; use `.env` and path helpers.
- Do not commit raw data or confidential microdata.
- Do not modify `references/bibliography.bib` without explicit instruction.
- Do not skip verification: run scripts and check compilation before claiming completion.

---

## Agent Guidelines

- **Ask mode**: Use for research, literature lookup, debugging, and exploratory questions.
- **Agent mode**: Use for implementation, file edits, and multi-step coding tasks.
- **Verification**: Always verify outputs (run scripts, check compilation) before claiming completion.
- **Transparency**: Document assumptions and data sources; cite external references.
