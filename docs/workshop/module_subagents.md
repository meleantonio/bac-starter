# Module: Subagents — Specialized Agents for Research Workflows

## Objectives

By the end of this module, participants will:

1. Understand what subagents are and when they differ from the main agent or skills.
2. Create at least one custom subagent in `.cursor/agents/*.md` format.
3. Use a subagent (e.g., reviewer) on a real PR from their capstone project.
4. Choose the right abstraction: main agent vs subagent vs skill vs slash command.

## Prerequisites

- Day 1–2 complete: project repo, issue board, rules, `AGENTS.md`.
- At least one open PR on the capstone project (or a branch ready for review).
- Cursor v2.4+ (or latest stable with subagent support).
- Basic familiarity with YAML frontmatter in markdown.

## Demo Script

### Setup

1. Ensure `.cursor/agents/` exists; create if needed.
2. Have a sample PR open in the repo (e.g., a small fix or feature branch).
3. Open the Agent panel in **Agent** mode.

### Steps (numbered, instructor-facing)

1. **Introduce subagents**  
   "Subagents are specialized AI assistants with their own context window. They get a prompt, tools, and optionally a different model. Use them when you need context isolation, parallel work, or role specialization."

2. **Show the `.cursor/agents/` directory**  
   "Each subagent is a `.md` file with YAML frontmatter (`name`, `description`, optional `model`, `readonly`, `background`) and a prompt body."

3. **Create the reviewer subagent**  
   Create `.cursor/agents/pr-reviewer.md` with the template below. Walk through each field:
   - `name`: how you invoke it (`/pr-reviewer` or "use the pr-reviewer subagent")
   - `description`: when Agent delegates to it—be specific
   - `model`: `fast` for cheaper/faster review, `inherit` for same as main

4. **Invoke the reviewer on the sample PR**  
   Type:  
   > Use the pr-reviewer subagent to review this PR for consistency, correctness, and style.  
   Show the PR branch/URL in context (e.g., `@PR-123` or paste the diff).

5. **Read the subagent output**  
   Show where the subagent writes its findings (chat reply, or `~/.cursor/subagents/` if background).

6. **Explain when to use subagents vs alternatives**  
   - Subagent: multi-step review, long exploration, parallel streams.  
   - Skill: single-purpose quick task (e.g., "generate changelog").  
   - Main agent: general orchestration, decisions, merging.

### Key Points to Emphasize

- **Description drives delegation.** Vague descriptions → Agent rarely uses the subagent. Be explicit: "Use when reviewing PRs for econometric code consistency, statistical correctness, and citation style."
- **One clear role per subagent.** Avoid generic "helper" agents.
- **Project vs user scope:** `.cursor/agents/` = project-only; `~/.cursor/agents/` = all projects.
- **Explicit invocation:** `/pr-reviewer review this PR` or "Use the pr-reviewer subagent to..."

## Hands-On Exercise

### Minimum Viable Path

1. Create `.cursor/agents/pr-reviewer.md` using the template below (or the reviewer template in this module).
2. Open a PR from your capstone (or create a small branch and PR).
3. Invoke the subagent:  
   > Use the pr-reviewer subagent to review PR #X for consistency, correctness, and style. Focus on: coefficient interpretations, unit labels, missingness handling, and citation format.
4. Apply at least one suggested change from the review.
5. Commit the subagent definition to the repo.

### Extension Challenge

- Add a second subagent: **replicator** (validates clean-room runs) or **bibliographer** (standardizes bib entries).
- Invoke two subagents in parallel: "Have pr-reviewer review the code changes and bibliographer check the references section."
- Refine the `description` so the main Agent delegates automatically when you say "Review this PR."

## When You Get Stuck

- **Subagent not found:** Ensure the file is in `.cursor/agents/` and has valid YAML. Restart Cursor or reload the window.
- **Agent doesn't delegate:** Make the description more specific. Include phrases like "Use when reviewing econometric code" or "Use proactively for PR reviews."
- **Wrong model:** Set `model: fast` for cheaper runs; use `inherit` to match main.
- **Subagent returns generic output:** Tighten the prompt body. Add economist-specific criteria (e.g., "Check that standard errors are reported; verify treatment effect interpretation").

## Expected Artifacts

- `.cursor/agents/pr-reviewer.md` (or equivalent)
- Optionally: `.cursor/agents/replicator.md`, `.cursor/agents/bibliographer.md`
- At least one PR with a subagent-generated review applied

## Key Prompts

**Invoke reviewer on a PR:**
```
Use the pr-reviewer subagent to review [this PR | PR #42] for:
1. Consistency with project coding standards
2. Statistical/econometric correctness (coefficients, SEs, interpretation)
3. Style (naming, docstrings, citation format)

Report: passed / needs changes, with specific line-level suggestions.
```

**Invoke replicator (if you created it):**
```
Use the replicator subagent to verify that the pipeline in `scripts/run_analysis.py` runs from a clean state. Check: (1) no hardcoded paths, (2) all dependencies in requirements.txt, (3) reproducible output hash for sample data.
```

**Invoke bibliographer (if you created it):**
```
Use the bibliographer subagent to standardize all references in `references/bibliography.bib`. Ensure: consistent key format, no missing fields, correct journal abbreviations, and alignment with the in-text citations in `paper/main.tex`.
```

## Template Subagent Definitions

### 1. PR Reviewer (consistency, correctness, style)

```markdown
---
name: pr-reviewer
description: PR review specialist for econometric/research code. Use when reviewing pull requests for consistency, statistical correctness, and style. Use proactively for PR reviews.
model: fast
readonly: true
---

You are a rigorous code reviewer for econometric and empirical economics projects.

When invoked on a PR or diff:
1. **Consistency**: Align with project rules (`.cursor/rules`, `AGENTS.md`), naming conventions, and existing patterns.
2. **Correctness**: Check coefficient interpretations, standard errors, missingness handling, unit labels, and data assumptions. Flag potential endogeneity or selection issues if visible.
3. **Style**: Docstrings, type hints, citation format (e.g., author-year), README/run instructions.

Report:
- Summary: pass / needs changes
- By section: what is good, what must change, what to consider
- Line-level suggestions where actionable

Be concise. Economists care about reproducibility and interpretability.
```

### 2. Replicator (clean-room validation)

```markdown
---
name: replicator
description: Replication validator. Use when verifying that a pipeline or script runs from clean state, has no hardcoded paths, and produces reproducible output.
model: fast
---

You are a replication specialist. Your job is to verify that research code is reproducible.

When invoked:
1. Identify the main entry point (script, notebook, Makefile target).
2. Check: no hardcoded absolute paths, secrets, or local-only assumptions.
3. Verify dependencies are declared (requirements.txt, environment.yml).
4. If possible, run a dry-run or minimal run and report success/failure.

Report:
- Reproducibility readiness: green / yellow / red
- Blockers (must fix)
- Recommendations (nice to have)

Focus on "can a colleague run this from scratch?"
```

### 3. Bibliographer (bib standardization)

```markdown
---
name: bibliographer
description: Bibliography and citation specialist. Use when standardizing .bib files, checking citation-key format, fixing missing fields, or aligning in-text citations with the bibliography.
model: fast
---

You are a bibliography specialist for academic economics.

When invoked:
1. Standardize .bib entries: consistent key format (e.g., AuthorYear), no missing required fields.
2. Fix journal abbreviations (AER, QJE, Econometrica, etc.).
3. Cross-check in-text citations against the bib file; flag orphans or mismatches.
4. Ensure DOIs/URLs where appropriate.

Report:
- Number of entries checked/fixed
- List of orphan citations
- Suggested key renames if needed

Preserve existing semantics; improve consistency.
```

## Further Reading

- [Cursor Docs: Subagents](https://www.cursor.com/docs/agent/subagents)
- [Cursor Changelog v2.4 — Subagents + Skills](https://cursor.com/changelog)
- SPEC §6.1 (concept coverage matrix), §8 (skill-creator)
