# Day 4 Delivery Prompts — Copy-Paste Ready

> Use these prompts during the Day 4 sprint for replication, packaging, presentation, and adoption planning.

---

## Replication Documentation Prompts

### Generate Replication README from Current State

```
Review our project structure and scripts. Create a complete replication/README.md that includes:
1. Overview (one paragraph: project, research question, what the package contains)
2. Requirements (OS, Python version, key packages, data access)
3. Directory structure (match our layout)
4. Setup instructions (clone, venv, pip install, data config)
5. Running the pipeline (exact commands in order)
6. Expected outputs (tables, figures, paths)
7. Troubleshooting (common issues and solutions)
8. Contact

Use templates/replication_README.md as structure. Document any known limitations.
```

### Document Clean-Run Steps

```
I just ran the full pipeline from a fresh clone. Document the exact steps that worked:
- Clone command
- Venv creation and activation
- pip install
- Any env vars or config (redact secrets)
- Run commands in order
- Approximate runtime
- Any manual steps (e.g., placing a file in data/)

Format for replication/README.md.
```

### Add Troubleshooting Section

```
Our replication sometimes fails due to: [list issues, e.g., API rate limits, missing data path]. Add a Troubleshooting section to replication/README.md with: Issue | Solution for each. Be specific.
```

---

## MCP Configuration Prompts

### Document MCP Setup

```
Create docs/mcp_setup.md documenting our MCP configuration. Include:
- Which MCP servers we use (e.g., FRED, filesystem)
- mcp.json snippet with secrets redacted
- One working prompt that uses the MCP
- Notes (restart required, path format, etc.)
```

### FRED Data Integration Note

```
Add a note to replication/README.md: "For FRED data, set FRED_API_KEY in environment. See docs/mcp_setup.md for MCP configuration." Place it in the Setup / Configure data access section.
```

---

## Presentation Drafting Prompts

### Draft Presentation Outline

```
Using our project brief, research design memo, and key results, draft a 5–7 minute presentation outline. Use templates/presentation_outline.md structure:
- Slide 1: Title + research question
- Slide 2: Motivation + contribution
- Slide 3: Method + data
- Slide 4: Key results (highlight one main finding)
- Slide 5: Workflow + tools (modes, subagents, skills)
- Slide 6: Next steps + 30-day plan

One idea per slide. Include suggested bullet points for each.
```

### Create Slide Content from Results

```
Our main result is [describe: e.g., coefficient of 0.42 on treatment, SE 0.08]. Create slide content for Slide 4 (Key Results) that:
- States the main finding in one sentence
- Suggests one figure or table to show
- Includes a 30-second demo script if we run the pipeline live
- Has a backup: "If demo fails, show [screenshot/figure]"
```

### Refine Presentation for Time

```
Our presentation draft is [X] minutes. Tighten it to 5–7 minutes. Cut the least essential content. Prioritize: research question, one result, workflow mention, next steps.
```

---

## 30-Day Plan Generation Prompts

### Generate Adoption Plan from Template

```
Fill templates/adoption_plan_30d.md with concrete actions for our project. Use our actual repo paths, AGENTS.md, and context:
- Week 1: Specific rules to add, .cursorignore entries, AGENTS.md updates
- Week 2: One real task (name it), one issue to open and close via PR
- Week 3: Which subagent to create, which skill, what parallel execution
- Week 4: When is our weekly agent sprint slot, who to share with

Be specific. No generic placeholder text.
```

### Customize 30-Day Plan for Research Workflow

```
I'm an economist with [describe: e.g., teaching load, paper deadlines]. Adapt the 30-day adoption plan so Week 1–2 are lighter and Week 3–4 align with [specific date or milestone]. Keep the same structure but adjust scope.
```

---

## Final Cleanup and Packaging Prompts

### Finalize Package Structure

```
Review our repo for the final package. Ensure:
1. README.md (root) has project title, quick start, link to replication/README.md
2. Remove temp files, __pycache__, stray .ipynb_checkpoints
3. .cursorignore excludes data/, .env, secrets
4. AGENTS.md has final run command and project notes
5. requirements.txt is complete and pinned if needed

Report what you changed or would change.
```

### Create Minimal .cursorignore for Package

```
Create or update .cursorignore so we can share the repo: exclude data/raw (if large), .env, *.pem, credentials*, __pycache__, .venv. Keep source, config templates, and docs. List what you added.
```

### Verify Replication README Commands

```
Read replication/README.md and run the documented setup and run commands. Report: do they work as written? Any missing steps? Update the README with corrections.
```

---

## End-of-Day Summary Prompt

```
Summarize our Day 4 deliverables for a handoff note: replication README status, clean-run result, presentation scope, 30-day plan location. One paragraph. For docs/handoff.md.
```

---

*Tip: @mention this file in chat when you need a delivery prompt.*
