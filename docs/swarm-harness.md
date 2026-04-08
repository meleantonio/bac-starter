# GitHub Swarm Harness

Operator guide for running multi-agent work with **GitHub issues, branches, and PRs** as the control plane. Cursor skills and subagents implement the same structure the workshop describes in `materials/day3/` and the `github-swarm-orchestration` skill.

## Lifecycle

1. **Plan** — If starting from SDD: run `sdd-orchestrator` / `spec/` until `spec/tasks.md` is approved.
2. **Export** — Use the `spec-tasks-to-github` skill to draft issues (or create manually with the Swarm task template).
3. **Label** — Apply concurrency and dependency labels (see below).
4. **Branch** — One issue → one branch → one PR by default: `feat/issue-<N>-short-slug`.
5. **Implement** — Worker agents commit; cite the creative worker name in commits and PR title/body when used.
6. **Review** — `pr-reviewer` + optional domain reviewers + `replication-verifier` / `artifact-coherence-auditor` as needed.
7. **Merge** — `integration-coordinator` or human decides order; use `automerge-ok` only when gates are explicit.
8. **Follow-on** — Verifier findings → **new linked issues**, not silent scope creep on the same PR.

## Labels (canonical)

| Label | Meaning |
|-------|---------|
| `parallel` | Safe to run in parallel; no merge dependency on other open work |
| `sequential` | Must land after another issue/PR |
| `blocked-by:<N>` | Blocked until issue `#N` is merged (use the numeric id) |
| `phase:verify` | Verification / audit work |
| `automerge-ok` | Allowed to auto-merge after CI + review gates pass |
| `domain:hank` | Invoke `hank-model-auditor` when relevant |
| `domain:game-theory` | Invoke `game-theory-referee` when relevant |
| `domain:micro` | Invoke `microeconometrics-identification-reviewer` when relevant |

Create these labels once per repo (GitHub UI or `gh label create`).

## Multi-stream milestones

For explicit pipeline splits (data → analysis → paper), you may use `rig/<stream>` branches **only** if recorded in `notes/orchestration_log.md`. Do not mix `feat/issue-*` and `rig/*` in the same milestone without documenting the mapping.

## State mirror

Keep **`notes/orchestration_log.md`** updated: stream (or issue), branch, issue, status, PR, reviewer. This is the audit trail when chat context is gone.

## Skills and agents

| Asset | Role |
|-------|------|
| `github-swarm-orchestration` skill | End-to-end swarm checklist |
| `spec-tasks-to-github` skill | Export spec tasks to issue bodies |
| `pr-reviewer` | PR consistency and economics-aware review |
| `replication-verifier` | Rerunnability and handoff |
| `artifact-coherence-auditor` | Paper / replication / outputs coherence |
| `integration-coordinator` | Merge order, rebase, conflicts |
| Plugin `bac-swarm-harness` | Commands + optional MCP sync for log/GitHub state |

## Plugin / MCP

See `plugins/bac-swarm-harness/README.md` and `docs/swarm-harness-dry-run.md`. The repo-local `.cursor/` assets remain the source of truth; the plugin adds commands and optional automation.
