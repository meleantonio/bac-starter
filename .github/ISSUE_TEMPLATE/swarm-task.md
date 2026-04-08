---
name: Swarm task
about: Unit of work for parallel/sequential agent execution with clear acceptance criteria and GitHub links.
title: "[scope] Short description"
labels: []
assignees: []
---

## Summary

One sentence describing the deliverable.

## Spec trace (optional)

- Link to `spec/tasks.md` checkbox or task ID: <!-- e.g. Task 3.2 -->
- Related requirement IDs (if any):

## Acceptance criteria

- [ ] Criterion 1
- [ ] Criterion 2

## Execution

- **Branch convention:** `feat/issue-<N>-short-slug` (replace `<N>` with this issue number after creation), unless milestone uses `rig/<stream>` (document in `notes/orchestration_log.md`).
- **Worker name (optional):** Creative subagent label for commits/PRs, e.g. `Gauss` for descriptive stats.

## Dependencies

- [ ] None — label: `parallel`
- [ ] Depends on issue #___ — add label `sequential` and `blocked-by:<N>` (use the blocking issue number for `N`)

## Review / verify gates

- [ ] PR will request: `pr-reviewer` (and domain reviewer if `domain:*` label applies)
- [ ] Post-merge or on PR: `replication-verifier` / `artifact-coherence-auditor` as needed
- [ ] **Automerge:** only if label `automerge-ok` is applied and CI + review gates pass

## Handoffs

- Reads: `notes/handoff_*.md` (list paths)
- Writes: `notes/handoff_*.md` (list paths)

## Paths touched (expected)

- <!-- e.g. `analysis/`, `replication/` -->
