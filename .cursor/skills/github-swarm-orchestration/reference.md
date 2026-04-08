# GitHub swarm orchestration — reference

## Label glossary

| Label | When to use |
|-------|-------------|
| `parallel` | No dependency on other in-flight merges |
| `sequential` | Ordering matters |
| `blocked-by:<N>` | Replace `N` with blocking issue number |
| `phase:verify` | Audit / verifier work |
| `automerge-ok` | Merge only after CI + review gates |
| `domain:hank` | HANK-touched code or calib |
| `domain:game-theory` | Theory / equilibrium text or code |
| `domain:micro` | Empirical ID or estimation |

## Branch naming

- Default: `feat/issue-<N>-short-slug`
- Multi-stream (document in `notes/orchestration_log.md`): `rig/<stream>`

## Phase checklist (captain)

1. **Planner** — Confirm `spec/tasks.md` approved OR issues already defined; list DAG of issues.
2. **Dispatch** — For each ready issue (no unmerged `blocked-by`), open branch, assign worker name, implement.
3. **Review gate** — `pr-reviewer`; add domain reviewer per labels.
4. **Verifier gate** — `replication-verifier` if run paths change; `artifact-coherence-auditor` if paper/output/replication alignment is in scope.
5. **Merge gate** — `integration-coordinator` or human; respect merge order; `automerge-ok` only if explicit.
6. **Follow-on** — New issues for verifier blockers; link from audit comment.

## `gh` snippets (non-interactive)

```bash
gh issue create --title "..." --body-file /tmp/issue.md --label parallel
gh pr create --base main --head feat/issue-12-slug --title "feat: ..." --body "Closes #12"
gh pr checks <PR_NUMBER>
gh pr merge <PR_NUMBER> --squash  # only when policy allows
```

## Files

- Log: `notes/orchestration_log.md`
- Operator doc: `docs/swarm-harness.md`
- Templates: `.github/ISSUE_TEMPLATE/swarm-task.md`, `.github/pull_request_template.md`
