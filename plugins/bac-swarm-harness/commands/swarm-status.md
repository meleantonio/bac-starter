---
name: swarm-status
description: Summarize swarm state from the orchestration log and optional issue graph JSON.
---

1. Open `notes/orchestration_log.md` and summarize each row (branch, issue, status, PR, reviewer).
2. Optionally run `python3 -m tools.swarm_mcp.cli parse-log notes/orchestration_log.md` to validate the table parses.
3. If the user provides a `gh issue list --json ...` export, run `python3 -m tools.swarm_mcp.cli issue-graph issues.json --merged ...` to report **merge-ready** issues and any **cycles** in `blocked-by:` labels.
