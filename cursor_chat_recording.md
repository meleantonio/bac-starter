# Cursor Chat Recording

## 2026-04-08

### User
in `@/.cursor` create examples of rules, subagents and skills that can support the work on a HANK model, or a game theory project, or an applied microeconometrics project. Use standard conventions and best practices for skills, subagents and rules taken from Cursor docs and online sources. Also add a copy of `/sdd` skills and the `sdd-orchestrator`.

### Assistant
- Audited the repo and confirmed there is no existing project-local `.cursor` setup yet.
- Reviewed current Cursor conventions for rules (`.mdc` with frontmatter), skills (`skills/<name>/SKILL.md`), and agents (`agents/*.md` with frontmatter).
- Located the existing global `sdd` skill and `sdd-orchestrator` agent for local copying.
- Collected scope clarifications:
  - Packaging: live project setup in `.cursor/rules`, `.cursor/skills`, and `.cursor/agents`.
  - Target stack: mixed economics workflow spanning MATLAB, Python, and Markdown/docs.
- Proposed a domain-first live `.cursor` layout with shared research rules, domain skills, reviewer agents, and project-local SDD copies.
- After approval, wrote the design spec to `docs/superpowers/specs/2026-04-08-cursor-econ-research-assets-design.md`.
- Completed a quick self-review for structure, path consistency, and local SDD copy behavior before handing the spec back for review.
- After approval, wrote the implementation plan to `docs/superpowers/plans/2026-04-08-cursor-econ-research-assets.md`.
- Created the live project-local `.cursor` assets:
  - `.cursor/README.md`
  - `.cursor/rules/` with four economics research rules
  - `.cursor/skills/` with HANK, game theory, applied microeconometrics, replication, and local `sdd`
  - `.cursor/agents/` with four reviewer agents and local `sdd-orchestrator`
- Copied the global `sdd` templates and `sdd-orchestrator` into the repository and adapted the `sdd` skill path to `.cursor/skills/sdd/templates/`.
- Verified the resulting `.cursor` tree and checked workspace diagnostics; no linter errors were reported on the edited paths.
