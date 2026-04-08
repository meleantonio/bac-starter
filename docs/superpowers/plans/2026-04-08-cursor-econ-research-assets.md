# Cursor Economics Research Assets Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Create a project-local `.cursor` setup with rules, skills, agents, and project-local SDD copies for economics research workflows.

**Architecture:** Add a small, live `.cursor` tree directly in the repository. Keep shared guidance in rules, domain workflows in skills with one-level-deep references, reviewer logic in agents, and vendored SDD files as a self-contained local copy.

**Tech Stack:** Markdown assets in `.cursor/`, copied SDD templates, project docs.

---

### Task 1: Scaffold The `.cursor` Tree

**Files:**
- Create: `.cursor/README.md`
- Create: `.cursor/rules/`
- Create: `.cursor/skills/`
- Create: `.cursor/agents/`

- [ ] **Step 1: Create the target directories**

```bash
mkdir -p .cursor/rules .cursor/skills .cursor/agents
```

- [ ] **Step 2: Add a short index describing the layout and intended use**

```markdown
# Project Cursor Assets

This repository contains live project-local Cursor assets for economics research workflows:
- rules in `.cursor/rules/`
- skills in `.cursor/skills/`
- agents in `.cursor/agents/`
```

### Task 2: Add Shared Research Rules

**Files:**
- Create: `.cursor/rules/research-reproducibility.mdc`
- Create: `.cursor/rules/python-econ-research.mdc`
- Create: `.cursor/rules/matlab-econ-research.mdc`
- Create: `.cursor/rules/economic-writing-and-tables.mdc`

- [ ] **Step 1: Write the four rule files with valid frontmatter**

```markdown
---
description: Keep economics research outputs reproducible and traceable
alwaysApply: true
---
```

- [ ] **Step 2: Use file globs for the language-specific rules**

```markdown
---
description: Python conventions for economics research code
globs: **/*.py
alwaysApply: false
---
```

### Task 3: Add Domain Skills

**Files:**
- Create: `.cursor/skills/hank-modeling/SKILL.md`
- Create: `.cursor/skills/hank-modeling/reference.md`
- Create: `.cursor/skills/game-theory-analysis/SKILL.md`
- Create: `.cursor/skills/game-theory-analysis/reference.md`
- Create: `.cursor/skills/applied-microeconometrics/SKILL.md`
- Create: `.cursor/skills/applied-microeconometrics/reference.md`
- Create: `.cursor/skills/replication-and-research-hygiene/SKILL.md`

- [ ] **Step 1: Write concise `SKILL.md` files with `name` and `description` frontmatter**

```markdown
---
name: hank-modeling
description: Guides HANK modeling workflows including calibration, equilibrium checks, and transition diagnostics. Use when working on heterogeneous-agent macro models or related numerical questions.
---
```

- [ ] **Step 2: Keep extended guidance in one-level-deep `reference.md` files where needed**

```markdown
## Additional Resources

- For detailed diagnostics and workflow checks, see [reference.md](reference.md).
```

### Task 4: Add Review Agents And Local SDD Copies

**Files:**
- Create: `.cursor/agents/hank-model-auditor.md`
- Create: `.cursor/agents/game-theory-referee.md`
- Create: `.cursor/agents/microeconometrics-identification-reviewer.md`
- Create: `.cursor/agents/replication-verifier.md`
- Create: `.cursor/agents/sdd-orchestrator.md`
- Create: `.cursor/skills/sdd/SKILL.md`
- Create: `.cursor/skills/sdd/reference.md`
- Create: `.cursor/skills/sdd/templates/spec/requirements.md`
- Create: `.cursor/skills/sdd/templates/spec/design.md`
- Create: `.cursor/skills/sdd/templates/spec/tasks.md`
- Create: `.cursor/skills/sdd/templates/steering/coding-standards.md`

- [ ] **Step 1: Copy the global `sdd` assets into the project-local `.cursor/skills/sdd/` directory**

```bash
cp ~/.cursor/skills/sdd/SKILL.md .cursor/skills/sdd/SKILL.md
cp ~/.cursor/skills/sdd/reference.md .cursor/skills/sdd/reference.md
cp ~/.cursor/skills/sdd/templates/spec/requirements.md .cursor/skills/sdd/templates/spec/requirements.md
cp ~/.cursor/skills/sdd/templates/spec/design.md .cursor/skills/sdd/templates/spec/design.md
cp ~/.cursor/skills/sdd/templates/spec/tasks.md .cursor/skills/sdd/templates/spec/tasks.md
cp ~/.cursor/skills/sdd/templates/steering/coding-standards.md .cursor/skills/sdd/templates/steering/coding-standards.md
```

- [ ] **Step 2: Replace the home-directory path in the copied `SKILL.md` with the project-local path**

```markdown
4. Copy templates from `.cursor/skills/sdd/templates/` into the project:
```

- [ ] **Step 3: Copy the global `sdd-orchestrator` into `.cursor/agents/` and add the four research review agents**

```markdown
---
name: hank-model-auditor
description: Reviews HANK model code and notes for calibration coherence, equilibrium logic, numerical diagnostics, and interpretation drift. Use when reviewing heterogeneous-agent macro model work.
model: inherit
---
```

### Task 5: Validate The Asset Tree

**Files:**
- Modify: `cursor_chat_recording.md`

- [ ] **Step 1: Verify the expected `.cursor` files exist**

```bash
rg --files .cursor
```

- [ ] **Step 2: Check edited files for workspace diagnostics**

```bash
# Use workspace lints/diagnostics for the changed markdown files if available
```

- [ ] **Step 3: Update the chat recording with the implementation summary**

```markdown
- Created the live project-local `.cursor` rules, skills, agents, and local SDD copy.
```
