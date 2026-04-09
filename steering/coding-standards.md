# Coding Standards

> **Purpose:** Steer the research specs and any later implementation toward clarity, reproducibility, and internally consistent game-theory reasoning.

## General

- Language: Markdown-first research specs; optional Python 3.10+ for later symbolic or numeric verification
- Framework: SDD workflow plus project-local reproducibility notes

## Patterns

- State the research question, game primitives, and equilibrium concept before any derivation.
- Keep one baseline equilibrium concept throughout the main analysis.
- Separate formal derivations, intuition, and extensions into distinct sections.
- Treat assumptions as named objects and link each result to the assumptions it needs.
- Use relative paths and canonical entry points for any code, notes, tables, or figures.
- Keep exploratory artifacts separate from canonical outputs.

## Forbidden Practices


- Mixing open-loop and feedback reasoning in the same baseline result without relabeling scope
- Using Perfect Bayesian equilibria
- Claiming existence or uniqueness without explicit parameter restrictions or regularity conditions
- Using absolute local paths or hidden manual steps
- Reporting interpretation that outruns the formal result
- Hard-coding credentials or secrets if external tooling is added later

## Examples

Good:

- "Under Assumptions A1-A4, the baseline feedback equilibrium exists and is unique."
- "Comparative Static CS-1 increases player 1's control intensity when q rises."

Bad:

- "The equilibrium should probably exist for standard parameter values."
- "We switched to another solution concept midway because it looked easier."
