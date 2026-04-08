"""Minimal MCP stdio server for swarm orchestration helpers.

Implements newline-delimited JSON-RPC 2.0 suitable for Cursor MCP stdio transport.
Run from repository root: python -m tools.swarm_mcp.server
"""

from __future__ import annotations

import json
import logging
import sys
from pathlib import Path
from typing import Any

from tools.swarm_mcp.github_state import (
    build_issue_nodes,
    detect_cycle,
    merge_ready_issues,
)
from tools.swarm_mcp.log_sync import (
    read_log_file,
    rows_from_jsonable,
    rows_to_jsonable,
    write_log_file,
)

logger = logging.getLogger(__name__)

PROTOCOL_VERSION = "2024-11-05"
SERVER_NAME = "bac-swarm-harness"
SERVER_VERSION = "0.1.0"


def _repo_root() -> Path:
    return Path(__file__).resolve().parents[2]


def _tool_orchestration_log_parse(arguments: dict[str, Any]) -> dict[str, Any]:
    rel = arguments.get("relative_path", "notes/orchestration_log.md")
    path = _repo_root() / rel
    preamble, rows, postamble = read_log_file(path)
    return {
        "preamble": preamble,
        "rows": rows_to_jsonable(rows),
        "postamble": postamble,
        "path": str(path),
    }


def _tool_orchestration_log_write(arguments: dict[str, Any]) -> dict[str, Any]:
    rel = arguments.get("relative_path", "notes/orchestration_log.md")
    path = _repo_root() / rel
    preamble = str(arguments.get("preamble", ""))
    postamble = str(arguments.get("postamble", ""))
    rows = rows_from_jsonable(arguments.get("rows", []))
    write_log_file(path, preamble, rows, postamble)
    return {"ok": True, "path": str(path), "row_count": len(rows)}


def _tool_issue_graph_analyze(arguments: dict[str, Any]) -> dict[str, Any]:
    issues = arguments.get("issues", [])
    merged = set(int(x) for x in (arguments.get("merged_numbers") or []))
    nodes = build_issue_nodes(issues)
    cycle = detect_cycle(nodes)
    ready = merge_ready_issues(nodes, merged)
    return {
        "cycle": cycle,
        "merge_ready": ready,
        "node_count": len(nodes),
    }


TOOLS = [
    {
        "name": "orchestration_log_parse",
        "description": "Parse notes/orchestration_log.md into preamble + structured rows.",
        "inputSchema": {
            "type": "object",
            "properties": {
                "relative_path": {
                    "type": "string",
                    "description": "Path relative to repo root",
                    "default": "notes/orchestration_log.md",
                }
            },
        },
    },
    {
        "name": "orchestration_log_write",
        "description": "Write orchestration log markdown from preamble and rows.",
        "inputSchema": {
            "type": "object",
            "properties": {
                "relative_path": {"type": "string"},
                "preamble": {"type": "string"},
                "postamble": {
                    "type": "string",
                    "description": "Markdown after the table (e.g. ## Conventions)",
                },
                "rows": {
                    "type": "array",
                    "items": {
                        "type": "object",
                        "properties": {
                            "stream": {"type": "string"},
                            "branch": {"type": "string"},
                            "issue": {"type": "string"},
                            "status": {"type": "string"},
                            "pr": {"type": "string"},
                            "reviewer": {"type": "string"},
                        },
                    },
                },
            },
            "required": ["rows"],
        },
    },
    {
        "name": "issue_graph_analyze",
        "description": "Analyze issue objects for dependency cycles and merge-ready set.",
        "inputSchema": {
            "type": "object",
            "properties": {
                "issues": {"type": "array"},
                "merged_numbers": {
                    "type": "array",
                    "items": {"type": "integer"},
                    "description": "Issue numbers already merged",
                },
            },
            "required": ["issues"],
        },
    },
]


def _send(obj: dict[str, Any]) -> None:
    line = json.dumps(obj, ensure_ascii=False)
    sys.stdout.write(line + "\n")
    sys.stdout.flush()


def _handle(msg: dict[str, Any]) -> None:
    if msg.get("jsonrpc") != "2.0":
        return
    mid = msg.get("id")
    method = msg.get("method")
    params = msg.get("params") or {}

    if method == "initialize":
        _send(
            {
                "jsonrpc": "2.0",
                "id": mid,
                "result": {
                    "protocolVersion": PROTOCOL_VERSION,
                    "capabilities": {"tools": {}},
                    "serverInfo": {"name": SERVER_NAME, "version": SERVER_VERSION},
                },
            }
        )
        return

    if method == "notifications/initialized":
        return

    if method == "ping":
        if mid is not None:
            _send({"jsonrpc": "2.0", "id": mid, "result": {}})
        return

    if method == "tools/list":
        _send(
            {
                "jsonrpc": "2.0",
                "id": mid,
                "result": {"tools": TOOLS},
            }
        )
        return

    if method == "tools/call":
        name = params.get("name")
        arguments = params.get("arguments") or {}
        try:
            if name == "orchestration_log_parse":
                result = _tool_orchestration_log_parse(arguments)
            elif name == "orchestration_log_write":
                result = _tool_orchestration_log_write(arguments)
            elif name == "issue_graph_analyze":
                result = _tool_issue_graph_analyze(arguments)
            else:
                raise ValueError(f"Unknown tool: {name}")
            _send(
                {
                    "jsonrpc": "2.0",
                    "id": mid,
                    "result": {
                        "content": [{"type": "text", "text": json.dumps(result, indent=2)}],
                    },
                }
            )
        except Exception as exc:  # noqa: BLE001
            logger.exception("tools/call failed")
            _send(
                {
                    "jsonrpc": "2.0",
                    "id": mid,
                    "error": {"code": -32000, "message": str(exc)},
                }
            )
        return

    if mid is not None:
        _send(
            {
                "jsonrpc": "2.0",
                "id": mid,
                "error": {"code": -32601, "message": f"Method not found: {method}"},
            }
        )


def main() -> None:
    logging.basicConfig(level=logging.WARNING)
    for line in sys.stdin:
        line = line.strip()
        if not line:
            continue
        try:
            msg = json.loads(line)
        except json.JSONDecodeError:
            continue
        _handle(msg)


if __name__ == "__main__":
    main()
