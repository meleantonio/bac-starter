"""Tests for issue dependency graph helpers."""

from __future__ import annotations

from tools.swarm_mcp.github_state import (
    build_issue_nodes,
    detect_cycle,
    merge_ready_issues,
)


def _issue(num: int, labels: list[str]) -> dict:
    return {"number": num, "labels": [{"name": lb} for lb in labels], "title": ""}


def test_merge_ready_respects_blocked_by() -> None:
    raw = [_issue(1, ["parallel"]), _issue(2, ["blocked-by:1"])]
    nodes = build_issue_nodes(raw)
    assert merge_ready_issues(nodes, set()) == [1]
    assert merge_ready_issues(nodes, {1}) == [1, 2]


def test_detect_cycle_two_node() -> None:
    raw = [_issue(1, ["blocked-by:2"]), _issue(2, ["blocked-by:1"])]
    nodes = build_issue_nodes(raw)
    cyc = detect_cycle(nodes)
    assert cyc is not None
    assert set(cyc) >= {1, 2}


def test_acyclic_no_cycle() -> None:
    raw = [_issue(1, []), _issue(2, ["blocked-by:1"]), _issue(3, ["blocked-by:2"])]
    nodes = build_issue_nodes(raw)
    assert detect_cycle(nodes) is None
