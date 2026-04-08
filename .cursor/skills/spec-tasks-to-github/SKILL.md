---
name: spec-tasks-to-github
description: >
  Exports approved spec/tasks.md entries into GitHub issue drafts with labels, branch names,
  and acceptance criteria. Use when syncing SDD tasks to issues, creating a swarm milestone
  from spec, or generating labeled issue bodies for feat/issue-N branches.
---

# Spec Tasks To GitHub

## When to use

- `spec/tasks.md` exists and user wants GitHub issues that **trace** to task lines or IDs.
- Planning a swarm milestone after SDD approval.

## Preconditions

- User confirms `spec/tasks.md` is the approved source for scope.
- Issue labels exist or you document one-time `gh label create` commands.

## Workflow

1. **Parse** `spec/tasks.md` for `- [ ]` / `- [x]` items and any task IDs or requirement references.
2. **Group** into minimal set of issues (prefer one issue per mergeable unit, not one per checkbox micro-step).
3. **Infer DAG:**
   - Tasks that only depend on earlier sections → earlier issues block later ones (`blocked-by:<N>`).
   - Independent sections → `parallel` label.
4. **Draft one issue body per issue** using this template (copy to clipboard or file for `gh issue create --body-file`):

```markdown
## Spec trace
- spec/tasks.md: <!-- quote the task line or ID -->

## Acceptance criteria
- [ ] ...

## Branch
`feat/issue-<N>-short-slug` (fill N after issue is created)

## Dependencies
- Labels: <!-- parallel | sequential -->
- blocked-by: <!-- issue numbers, or none -->

## Review / verify
- [ ] pr-reviewer
- [ ] replication-verifier (if applicable)
- [ ] artifact-coherence-auditor (if paper/replication alignment)
```

5. **Ordering:** Create blocking issues first so you can reference their numbers in `blocked-by:` on dependent issues.
6. **Handoff:** Tell the user to run `github-swarm-orchestration` for execution, or continue in the same session following that skill's phases.

## Guardrails

- Do not change product scope: export what the spec says; flag ambiguities instead of inventing tasks.
- Keep issue bodies self-contained for workers who lack chat context.

## Output

- Numbered list of proposed issue titles + labels + dependency notes
- Ready-to-paste issue bodies (or paths to temp files) for `gh issue create`
