## Summary

What this PR does (one short paragraph).

## Issue

- Closes #<!-- issue number -->
- Or Refs #<!-- issue numbers if partial -->

## Spec / task trace

- `spec/tasks.md` (task ID or checkbox): <!-- optional -->

## Worker / subagent

- **Worker name:** <!-- e.g. Diogenes — cite in commit messages -->

## Checklist

- [ ] Acceptance criteria in the issue are met
- [ ] No absolute machine paths; follows [research reproducibility](.cursor/rules/research-reproducibility.mdc)
- [ ] Handoff files updated if this PR crosses streams (`notes/handoff_*.md`)
- [ ] `notes/orchestration_log.md` updated (PR link, status)

## Merge order

- [ ] No ordering constraint
- [ ] Merge after: #<!-- prerequisite PR or issue -->
- [ ] Base branch is up to date with `main` (rebase if dependency merged first)

## Reviewers / verifiers

- [ ] `pr-reviewer` subagent (or human) — consistency, correctness, style
- [ ] `replication-verifier` — if replication paths or run instructions changed
- [ ] Domain reviewer — if labeled `domain:hank` | `domain:game-theory` | `domain:micro`
- [ ] `artifact-coherence-auditor` — if paper / outputs / replication coherence is in scope

## Automerge

- [ ] Label `automerge-ok` applied **and** all gates green — then merge allowed
- [ ] Otherwise: human or `integration-coordinator` merges after approval
