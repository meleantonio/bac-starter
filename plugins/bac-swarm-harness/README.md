# bac-swarm-harness (Cursor plugin)

Thin packaging for the **GitHub Swarm Harness** in this repository. Canonical workflows live in:

- `.cursor/skills/github-swarm-orchestration/`
- `.cursor/skills/spec-tasks-to-github/`
- `docs/swarm-harness.md`
- `tools/swarm_mcp/` (CLI + optional MCP server)

## Install (Cursor)

1. Open **Cursor Settings → MCP / Plugins** (or your Cursor version’s plugin install flow).
2. **Install from folder:** point at this directory:

   `plugins/bac-swarm-harness`

   Cursor should read `.cursor-plugin/plugin.json`.

3. **Working directory:** the MCP server runs as `python3 -m tools.swarm_mcp.server` with `cwd` set to the workspace folder (the repo root). Use a machine where `python3` is on `PATH`.

## MCP tools

| Tool | Purpose |
|------|---------|
| `orchestration_log_parse` | Read `notes/orchestration_log.md` → JSON (preamble, rows, postamble) |
| `orchestration_log_write` | Write log from JSON |
| `issue_graph_analyze` | Detect `blocked-by:` cycles; list merge-ready issues given merged IDs |

## CLI (without MCP)

From the **repository root**:

```bash
python3 -m tools.swarm_mcp.cli parse-log notes/orchestration_log.md
python3 -m tools.swarm_mcp.cli issue-graph issues.json --merged 1 2
```

## Slash commands

See `commands/` — short prompts that point agents at the harness docs and skills.

## Copy to global plugins (optional)

To make the plugin available in all workspaces, copy this folder to:

`~/.cursor/plugins/local/bac-swarm-harness/`

See Cursor plugin documentation for discovery paths.
