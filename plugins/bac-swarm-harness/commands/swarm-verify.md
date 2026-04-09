---
name: swarm-verify
description: Run PR review and verifier gates before merge in a swarm workflow.
---

Follow `docs/swarm-harness.md` **Review / verify gates**:

1. **pr-reviewer** on each open PR (readonly first).
2. **replication-verifier** when replication paths or run instructions changed.
3. **artifact-coherence-auditor** when paper / outputs / replication must align.
4. Domain reviewers if `domain:*` labels apply (`hank-model-auditor`, `game-theory-referee`, `microeconometrics-identification-reviewer`).
5. **integration-coordinator** for merge order and conflicts.
6. Open **new GitHub issues** for verifier blockers; do not silently expand merged PR scope.
