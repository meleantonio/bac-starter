# Orchestration Log

Mirror of swarm execution state. Update when branches are created, PRs opened, reviewers assigned, and merges complete.

| Stream / scope | Branch | Issue | Status | PR | Reviewer |
|----------------|--------|-------|--------|-----|----------|
| _example_ | `feat/issue-1-short-slug` | #1 | pending | - | - |

## Conventions

- **Status:** `pending` | `in_progress` | `pr_open` | `in_review` | `merged` | `blocked`
- **Branch:** Default `feat/issue-<N>-<slug>`; `rig/<stream>` only for declared multi-stream milestones (see `docs/swarm-harness.md`).
- **Reviewer:** Human handle or subagent name (e.g. `pr-reviewer`).

## Handoff files

When streams depend on each other, use `notes/handoff_<from>_to_<to>.md` and reference them in the issue and PR template.
