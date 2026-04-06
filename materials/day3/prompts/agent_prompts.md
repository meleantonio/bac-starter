# Day 3 Agent Prompts — Copy-Paste Ready

> Use these prompts in Cursor Agent mode during the Day 3 sprint. Replace placeholders (e.g., `#X`, `scripts/run_analysis.py`) with your actual values.

---

## Subagent Creation Prompts

### PR Reviewer Subagent

```
Create a subagent at .cursor/agents/pr-reviewer.md that reviews pull requests for econometric and empirical economics projects. Include:
- YAML frontmatter: name, description (include "Use when reviewing PRs for consistency, statistical correctness, and style"), model: fast, readonly: true
- Prompt body covering: (1) Consistency with project rules, (2) Correctness (coefficients, SEs, missingness, units), (3) Style (docstrings, type hints, citations), (4) Output format: Summary (pass / needs changes), Blockers, Suggestions, Reproducibility check

Make the description specific so the main Agent delegates to it when I say "Review this PR."
```

### Replicator Subagent

```
Create a subagent at .cursor/agents/replicator.md that validates replication readiness. Include:
- YAML: name, description ("Use when verifying that a pipeline or script runs from clean state, has no hardcoded paths, and produces reproducible output"), model: fast
- Prompt body: identify main entry point, check for hardcoded paths/secrets, verify dependencies in requirements.txt, run dry-run if possible
- Output: Reproducibility readiness (green/yellow/red), Blockers, Recommendations

Focus on "can a colleague run this from scratch?"
```

### Bibliographer Subagent

```
Create a subagent at .cursor/agents/bibliographer.md that standardizes bibliography files. Include:
- YAML: name, description ("Use when standardizing .bib files, checking citation-key format, fixing missing fields, or aligning in-text citations with the bibliography"), model: fast
- Prompt body: standardize .bib entries (key format, required fields), fix journal abbreviations, cross-check in-text citations vs bib, ensure DOIs/URLs
- Output: Number of entries checked/fixed, orphan citations, suggested key renames
```

---

## Skill Creation Prompts

### Replication-Checker Skill

```
Create a skill at .cursor/skills/replication-checker/SKILL.md with:
- Description: "Verifies that research pipelines run from clean state with no hardcoded paths, declared dependencies, and reproducible output. Use when checking replication readiness, validating run instructions, or before sharing code."
- Workflow: (1) Identify main entry point, (2) Check for hardcoded paths (absolute, localhost), (3) Verify dependencies declared, (4) Report status (green/yellow/red), blockers, recommendations, minimal run command
- Optional: references/replication_checklist.md or scripts/check_paths.py
```

### Literature-Mapper Skill

```
Create a skill at .cursor/skills/literature-mapper/SKILL.md with:
- Description: "Standardizes references, maps literature to research design, and produces relevance summaries. Use when standardizing bib, mapping literature, or summarizing cited papers."
- Workflow: (1) Standardize .bib entries, (2) Cross-reference with docs/research_design.md, (3) Produce one-paragraph relevance summary per cited paper
```

---

## Swarm Orchestration Prompts

### Planner — create labeled issues (parallel vs sequential)

```
You are helping plan the next milestone. Create or update GitHub issues with:
(1) acceptance criteria per issue,
(2) labels: use `parallel` for tasks with no cross-dependencies; use `sequential` or `blocked-by:#N` when task B needs A merged first,
(3) a one-line note on whether each issue is a good fit for a Cloud Agent (isolated branch, clear scope) vs foreground Agent.
```

### Cloud Agent — one issue, one branch

```
Start a Cloud Agent for issue #K only. Branch: feat/issue-K. Implement the acceptance criteria in the issue; do not modify unrelated paths. Open a PR when done.
```

### Assign Work to Data Stream

```
On branch rig/data-loader, implement the data loader per issue #X. Input: raw data in data/raw/. Output: data/processed/panel.csv. Create notes/handoff_data_to_analysis.md with column names, units, and sample stats (count, mean for key vars).
```

### Assign Work to Analysis Stream

```
On branch rig/analysis, implement the analysis script per issue #Y. Read data from data/processed/panel.csv (see notes/handoff_data_to_analysis.md for schema). Output: results/estimates.csv and results/figures/. Create notes/handoff_analysis_to_paper.md with key results to report (coefficients, interpretation).
```

### Assign Work to Paper Stream

```
On branch rig/paper-skeleton, create the paper skeleton per issue #Z. Use notes/handoff_analysis_to_paper.md for results. Structure: intro, data, methods, results, conclusion. Use the paper-polisher skill before finalizing if available.
```

### Consistency Pass Before Merge

```
Use the pr-reviewer subagent to review all open PRs for rig/data-loader, rig/analysis, and rig/paper-skeleton. Check cross-stream consistency (paths, units, variable labels). Report: ready to merge / needs changes with specific line numbers.
```

### HANK-style monetary policy (illustrative decomposition)

```
Draft GitHub issues for a HANK project: (1) steady state + calibration module, (2) monetary shock IRFs blocked on (1), (3) heterogeneity aggregation / welfare blocked on (2), (4) literature + BibTeX in parallel with early code, (5) policy figures + narrative blocked on (3). Add labels parallel/sequential/blocked-by as appropriate.
```

---

## Cloud Agent task prompts (formerly “Background Agents”)

### Generate Documentation

```
Generate docstrings for all Python files in scripts/. Use Google-style (Args, Returns, Raises). Preserve existing logic. Work on branch bg/docstrings. Do not modify function bodies, only add docstrings.
```

### Add Type Hints

```
Add type hints to all functions in src/. Use standard library typing (Optional, List, Dict, etc.). Preserve behavior. Work on branch bg/type-hints.
```

### Review Cloud Agent PR (after PR is open)

```
Review this PR from a Cloud Agent. Check: (1) no logic changes unless requested, (2) docstrings/type hints match the code, (3) no hardcoded paths or secrets. Report: ready to merge / needs changes with specific line numbers.
```

---

## Review and Consistency Check Prompts

### Invoke Reviewer on a PR

```
Use the pr-reviewer subagent to review [this PR | PR #42] for:
1. Consistency with project coding standards
2. Statistical/econometric correctness (coefficients, SEs, interpretation)
3. Style (naming, docstrings, citation format)

Report: passed / needs changes, with specific line-level suggestions.
```

### Invoke Replicator

```
Use the replicator subagent to verify that the pipeline in scripts/run_analysis.py runs from a clean state. Check: (1) no hardcoded paths, (2) all dependencies in requirements.txt, (3) reproducible output hash for sample data.
```

### Invoke Bibliographer

```
Use the bibliographer subagent to standardize all references in references/bibliography.bib. Ensure: consistent key format, no missing fields, correct journal abbreviations, and alignment with the in-text citations in paper/main.tex.
```

### Invoke Replication-Checker Skill

```
Use the replication-checker skill to verify that scripts/run_analysis.py can run from a clean state. Report: blockers, recommendations, and a minimal run command.
```

### Invoke Literature-Mapper Skill

```
Use the literature-mapper skill to standardize references/bibliography.bib and produce a one-paragraph relevance summary for each paper cited in docs/research_design.md.
```

---

## Parallel Invocation (Two Subagents)

```
Have the pr-reviewer subagent review the code changes and the bibliographer subagent check the references section. Report both findings together.
```

---

*Tip: Bookmark this file and @mention it in chat when you need a prompt.*
