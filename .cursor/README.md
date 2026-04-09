# Project Cursor Assets

This repository includes live project-local Cursor assets for economics research workflows.

## Layout

- `.cursor/rules/`: shared research and writing rules
- `.cursor/skills/`: domain workflows and the local `sdd` copy
- `.cursor/agents/`: specialized reviewer agents and subagents

## Included Assets

- `research-reproducibility`: cross-cutting rule for paths, assumptions, and traceability
- `python-econ-research`: Python conventions for research code
- `matlab-econ-research`: MATLAB conventions for model and numerical code
- `economic-writing-and-tables`: writing guidance for notes, tables, and result summaries
- `hank-modeling`, `game-theory-analysis`, `applied-microeconometrics`, `replication-and-research-hygiene`: project-local research skills
- `github-swarm-orchestration`, `spec-tasks-to-github`: GitHub issue/branch/PR swarm workflow and spec-to-issue export
- `hank-model-auditor`, `game-theory-referee`, `microeconometrics-identification-reviewer`, `replication-verifier`: reviewer agents
- `pr-reviewer`, `artifact-coherence-auditor`, `integration-coordinator`: PR review, artifact coherence, and merge-order coordination for swarm workflows
- `sdd`, `sdd-orchestrator`: project-local copies of the existing SDD skill and agent

## Notes

- Skills keep core guidance in `SKILL.md` and use one-level-deep reference files only where extra detail helps.
- The local `sdd` copy uses project-local paths under `.cursor/skills/sdd/` so it is self-contained in this repository.
- These files are examples meant to be directly usable here and easy to adapt in future research projects.
