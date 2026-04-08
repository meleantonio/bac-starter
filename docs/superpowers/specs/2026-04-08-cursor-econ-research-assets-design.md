# Cursor Economics Research Assets Design

## Goal

Create a project-local `.cursor` setup that provides usable examples of:

- rules for research coding and writing hygiene
- skills for HANK modeling, game theory, applied microeconometrics, and replication
- agents that review domain-specific work
- a local copy of the existing `sdd` skill and `sdd-orchestrator`

The assets should follow current conventions already present in the local Cursor ecosystem:

- rules as `.cursor/rules/*.mdc` with YAML frontmatter
- skills as `.cursor/skills/<skill-name>/SKILL.md`
- agents as `.cursor/agents/*.md` with YAML frontmatter
- concise instructions with one-level-deep references where extra detail is needed

## Scope

This design covers a live project setup, not a passive example pack. The files should be directly usable by Cursor in this repository.

In scope:

- shared research rules
- mixed-stack support for Python, MATLAB, and Markdown
- three domain-specific skills
- one cross-cutting replication skill
- four domain/research review agents
- local copy of `sdd`
- local copy of `sdd-orchestrator`
- a short `.cursor/README.md` index

Out of scope:

- plugin packaging
- MCP-specific tooling for external economics APIs
- executable helper scripts
- automated tests for the `.cursor` content itself

## Design Principles

1. Keep each rule or skill focused on one concern.
2. Prefer concise operational guidance over textbook explanations.
3. Make domain assets specific enough to be useful, but generic enough to survive across projects.
4. Preserve progressive disclosure by putting extended material in referenced files rather than bloating `SKILL.md`.
5. Keep copied SDD assets locally usable by replacing home-directory assumptions with project-local paths where needed.

## Target Structure

```text
.cursor/
  README.md
  rules/
    research-reproducibility.mdc
    python-econ-research.mdc
    matlab-econ-research.mdc
    economic-writing-and-tables.mdc
  skills/
    hank-modeling/
      SKILL.md
      reference.md
    game-theory-analysis/
      SKILL.md
      reference.md
    applied-microeconometrics/
      SKILL.md
      reference.md
    replication-and-research-hygiene/
      SKILL.md
    sdd/
      SKILL.md
      reference.md
      templates/
        spec/design.md
        spec/requirements.md
        spec/tasks.md
        steering/coding-standards.md
  agents/
    hank-model-auditor.md
    game-theory-referee.md
    microeconometrics-identification-reviewer.md
    replication-verifier.md
    sdd-orchestrator.md
```

## Rules

### `research-reproducibility.mdc`

Always-apply rule for deterministic workflows and transparent outputs.

Core guidance:

- record assumptions and calibration choices
- do not overwrite raw inputs
- use stable relative paths
- note seeds, solver tolerances, and estimation settings
- keep tables/figures traceable to code that generated them

### `python-econ-research.mdc`

File-scoped rule for `**/*.py`.

Core guidance:

- type hints where practical
- clear separation between data loading, transformation, estimation, and reporting
- explicit error handling around I/O and estimation failures
- avoid notebook-style hidden state in scripts
- prefer functions returning data/results objects over scripts with side effects

### `matlab-econ-research.mdc`

File-scoped rule for `**/*.m`.

Core guidance:

- one clear purpose per script/function
- name parameters, calibration blocks, and grids clearly
- avoid hidden workspace dependencies
- document numerical assumptions, convergence checks, and fallback behavior
- keep plotting/export logic separate from model solution logic where practical

### `economic-writing-and-tables.mdc`

File-scoped rule for `**/*.md`.

Core guidance:

- state the question, identification logic, and limitations explicitly
- keep notation consistent
- write table/figure notes that define samples, units, and specifications
- separate results from interpretation and robustness commentary

## Skills

### `hank-modeling`

Purpose:

- support work on heterogeneous-agent macro models, calibration, equilibrium solution, and diagnostics

Main workflow:

1. clarify model block, equilibrium object, and outputs required
2. inspect state/control definitions and calibration targets
3. verify numerical method assumptions and convergence diagnostics
4. summarize economic interpretation separately from solver mechanics

Reference topics:

- calibration targets and parameter bookkeeping
- stationary equilibrium and transition-path checks
- distributional objects and market-clearing diagnostics

### `game-theory-analysis`

Purpose:

- support formal game specification, equilibrium reasoning, and comparative statics

Main workflow:

1. restate players, actions, information, timing, and payoffs
2. identify the equilibrium concept being used
3. check whether best-response logic and incentive constraints are explicit
4. separate formal conclusions from intuition and extensions

Reference topics:

- equilibrium concept checklist
- extensive-form vs normal-form handling
- comparative statics and sensitivity framing

### `applied-microeconometrics`

Purpose:

- support empirical design, identification, estimation, and robustness communication

Main workflow:

1. state the estimand and identification strategy
2. map variables, sample restrictions, and treatment timing
3. validate specification choices and inference assumptions
4. report robustness, threats to identification, and interpretation bounds

Reference topics:

- identification checklist
- common threats and robustness families
- reporting norms for tables, figures, and appendices

### `replication-and-research-hygiene`

Purpose:

- provide cross-project guidance for replication, auditability, and handoff quality

Main workflow:

1. inventory inputs, outputs, and environment assumptions
2. distinguish exploratory artifacts from canonical artifacts
3. verify that paths, seeds, and result-generation steps are reproducible
4. produce a short replication note when work is complete

## Agents

### `hank-model-auditor`

Role:

- review HANK-related code or notes for calibration coherence, equilibrium logic, numerical diagnostics, and interpretation drift

### `game-theory-referee`

Role:

- review game-theory work for internal consistency, equilibrium concept mismatch, missing off-path reasoning, and ambiguity in timing or information

### `microeconometrics-identification-reviewer`

Role:

- review empirical work with a referee-style emphasis on estimands, identification assumptions, inference choices, and robustness gaps

### `replication-verifier`

Role:

- review research workflows for reproducibility gaps, brittle paths, undocumented prerequisites, and output traceability

### `sdd-orchestrator`

Role:

- copied locally so the repository has an in-project SDD entry point alongside the copied `sdd` skill

## SDD Copy Policy

The local `sdd` and `sdd-orchestrator` copies should start from the existing global versions already available on the machine.

Required adaptation:

- replace references to `~/.cursor/skills/sdd/...` with `.cursor/skills/sdd/...` so the local copy is self-contained

No other behavioral changes should be made unless needed to keep references valid inside this repository.

## Validation

After implementation:

1. verify every rule has valid frontmatter with `description` and `alwaysApply`, plus `globs` where file-scoped
2. verify every skill has valid `name` and `description` frontmatter
3. verify every agent has valid `name` and `description` frontmatter
4. verify all referenced files exist and remain one level deep from each `SKILL.md`
5. verify copied SDD templates are present and path references are local
6. run lints/diagnostics on edited files if any are reported by the workspace

## Risks

- Overly generic economics guidance could become vague and low-value.
- Overly specific guidance could hard-code one research style and age poorly.
- Copying SDD verbatim without path fixes would leave broken references.

## Recommendation

Implement the domain-first layout above, keeping the skills concise and practical, and use project-local SDD copies so the repository is immediately usable without relying on personal global directories.
