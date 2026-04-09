---
name: swarm-kickoff
description: Start a GitHub-backed swarm milestone using spec tasks, issues, and orchestration log.
---

Read `docs/swarm-harness.md` and invoke the **github-swarm-orchestration** skill.

1. If `spec/tasks.md` is not approved yet, use **sdd-orchestrator** first.
2. Export tasks to GitHub issues with **spec-tasks-to-github** (or use `.github/ISSUE_TEMPLATE/swarm-task.md`).
3. Apply labels (`parallel`, `sequential`, `blocked-by:<N>`).
4. Initialize or update `notes/orchestration_log.md`.
5. Create branches `feat/issue-<N>-short-slug` and open PRs with `.github/pull_request_template.md`.
