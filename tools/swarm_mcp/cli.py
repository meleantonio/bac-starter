"""CLI entry points for swarm log and issue-graph utilities (no MCP)."""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

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


def _cmd_parse_log(args: argparse.Namespace) -> int:
    path = Path(args.path)
    preamble, rows, postamble = read_log_file(path)
    out = {"preamble": preamble, "rows": rows_to_jsonable(rows), "postamble": postamble}
    print(json.dumps(out, indent=2))
    return 0


def _cmd_render_log(args: argparse.Namespace) -> int:
    payload = json.loads(Path(args.input).read_text(encoding="utf-8"))
    preamble = str(payload.get("preamble", ""))
    postamble = str(payload.get("postamble", ""))
    rows = rows_from_jsonable(payload.get("rows", []))
    write_log_file(Path(args.path), preamble, rows, postamble)
    return 0


def _cmd_issue_graph(args: argparse.Namespace) -> int:
    raw = json.loads(Path(args.input).read_text(encoding="utf-8"))
    nodes = build_issue_nodes(raw)
    cycle = detect_cycle(nodes)
    merged = set(args.merged) if args.merged else set()
    result = {
        "nodes": [{"number": n.number, "labels": n.labels, "title": n.title} for n in nodes],
        "cycle": cycle,
        "merge_ready": merge_ready_issues(nodes, merged),
    }
    print(json.dumps(result, indent=2))
    return 0


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(prog="swarm-mcp")
    sub = parser.add_subparsers(dest="command", required=True)

    p_parse = sub.add_parser("parse-log", help="Parse orchestration_log.md to JSON")
    p_parse.add_argument("path", type=str)
    p_parse.set_defaults(func=_cmd_parse_log)

    p_render = sub.add_parser("render-log", help="Write orchestration_log.md from JSON file")
    p_render.add_argument("path", type=str)
    p_render.add_argument("input", type=str, help="JSON file with preamble + rows")
    p_render.set_defaults(func=_cmd_render_log)

    p_graph = sub.add_parser("issue-graph", help="Analyze issue list JSON for cycles and readiness")
    p_graph.add_argument("input", type=str, help="JSON file: list of GitHub issue objects")
    p_graph.add_argument(
        "--merged",
        type=int,
        nargs="*",
        default=[],
        help="Issue numbers already merged/closed",
    )
    p_graph.set_defaults(func=_cmd_issue_graph)

    args = parser.parse_args(argv)
    return int(args.func(args))


if __name__ == "__main__":
    sys.exit(main())
