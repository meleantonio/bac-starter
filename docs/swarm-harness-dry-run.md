# Swarm harness dry run

Walk through two scenarios to validate the **GitHub Swarm Harness** without relying on chat-native task IDs.

## Prerequisites

- `gh` authenticated (`gh auth status`).
- Python 3.10+ on `PATH`.
- From repo root (recommended): `python3 -m venv .venv && .venv/bin/pip install pytest` then `.venv/bin/python -m pytest`.

## Scenario A — Happy path (parallel issues)

1. Create two issues from **Swarm task** template (`.github/ISSUE_TEMPLATE/swarm-task.md`).
2. Label both `parallel`.
3. Update `notes/orchestration_log.md` with two rows (`pending`, no PR yet).
4. Branches: `feat/issue-<N>-slug-a` and `feat/issue-<M>-slug-b`.
5. Open two PRs using `.github/pull_request_template.md` (`Closes #N` / `Closes #M`).
6. Run **pr-reviewer** on each PR (readonly).
7. Merge in any order (no `blocked-by`).
8. Set rows to `merged` and paste PR URLs in the log.

**Check:** `python3 -m tools.swarm_mcp.cli parse-log notes/orchestration_log.md` returns valid JSON.

## Scenario B — Verifier follow-on (sequential + new issue)

1. Create issue **#A** (implementation) labeled `parallel`.
2. Create issue **#B** (coherence audit) labeled `sequential` and `blocked-by:<A>` (use A’s number).
3. Complete **#A**, merge PR, mark **#A** merged.
4. Start **#B** on a new branch; run **artifact-coherence-auditor**; if blockers exist, open **#C** (fix discrepancies) — do **not** expand **#B**’s scope silently.
5. Run **integration-coordinator** to order merges: **#C** before closing **#B** if **#C** blocks the audit.

**Check:** Save a sample `issues.json` (from `gh issue list --json number,title,labels`) and run:

```bash
python3 -m tools.swarm_mcp.cli issue-graph issues.json --merged <A>
```

Expect **#B** in `merge_ready` only after **#A** is listed in `--merged`.

**Cycle check:** If someone mis-labels mutual `blocked-by`, `issue_graph_analyze` / CLI should report a `cycle` array.

## Automated verification

```bash
pytest
```

## MCP smoke test (optional)

From repo root, with the **bac-swarm-harness** plugin enabled, confirm the MCP server starts (Cursor will spawn `python3 -m tools.swarm_mcp.server`). Invoke `orchestration_log_parse` on `notes/orchestration_log.md` and confirm JSON output.
