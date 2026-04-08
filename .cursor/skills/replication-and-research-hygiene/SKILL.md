---
name: replication-and-research-hygiene
description: Supports replication, result handoff, and canonical research pipelines. Use when organizing empirical or quantitative research code, preparing tables and figures, or making work rerunnable by someone else.
---

# Replication And Research Hygiene

## Trigger

Use when the task involves:
- making results rerunnable by someone else
- deciding which scripts or notebooks are canonical
- packaging tables, figures, simulations, or model outputs for handoff
- checking for hidden path, seed, dependency, or environment assumptions

## Workflow

1. Inventory inputs, outputs, environment assumptions, and any required secrets or credentials.
2. Distinguish exploratory artifacts from canonical pipelines.
3. Verify paths, seeds, configuration values, and result-generation steps.
4. Write a short replication note with commands, dependencies, expected outputs, and remaining blockers.

## Guardrails

- Do not claim a result is reproducible if it depends on undocumented manual edits.
- Avoid absolute paths and hidden local dependencies.
- Keep raw data immutable.
- Name the canonical script or entry point that regenerates each table, figure, or model output.

## Output

Return:
- the canonical entry points
- required inputs and environment assumptions
- commands or steps to regenerate outputs
- unresolved reproducibility gaps

## Replication Note Template

```markdown
## Replication Note
- Entry point: `path/to/script.py`
- Inputs: `data/raw/...`
- Environment: Python 3.11, MATLAB R2025a
- Outputs: `results/tables/table_1.csv`, `results/figures/figure_2.png`
- Remaining blockers: none / [list blockers]
```
