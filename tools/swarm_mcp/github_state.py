"""Issue dependency helpers for swarm milestones (blocked-by labels)."""

from __future__ import annotations

import re
from dataclasses import dataclass, field


_BLOCKED_BY = re.compile(r"^blocked-by:(\d+)$", re.IGNORECASE)


@dataclass
class IssueNode:
    """GitHub issue as a node in a dependency graph."""

    number: int
    labels: list[str] = field(default_factory=list)
    title: str = ""

    def blocked_by_numbers(self) -> list[int]:
        found: list[int] = []
        for lab in self.labels:
            m = _BLOCKED_BY.match(lab.strip())
            if m:
                found.append(int(m.group(1)))
        return found


def build_issue_nodes(raw: list[dict]) -> list[IssueNode]:
    """Build nodes from GitHub-style dicts: {\"number\": 1, \"labels\": [{\"name\": ...}], \"title\": ...}."""
    nodes: list[IssueNode] = []
    for item in raw:
        num = int(item["number"])
        labels_data = item.get("labels") or []
        label_names: list[str] = []
        for lb in labels_data:
            if isinstance(lb, str):
                label_names.append(lb)
            elif isinstance(lb, dict) and "name" in lb:
                label_names.append(str(lb["name"]))
        title = str(item.get("title", ""))
        nodes.append(IssueNode(number=num, labels=label_names, title=title))
    return nodes


def build_adjacency(nodes: list[IssueNode]) -> dict[int, list[int]]:
    """Return adjacency map: blocker_issue -> list of dependent issues (A blocks B => A -> B)."""
    numbers = {n.number for n in nodes}
    adj: dict[int, list[int]] = {n.number: [] for n in nodes}
    for n in nodes:
        for b in n.blocked_by_numbers():
            if b in numbers:
                adj.setdefault(b, []).append(n.number)
    return adj


def detect_cycle(nodes: list[IssueNode]) -> list[int] | None:
    """Return a cycle as a list of issue numbers if one exists, else None."""
    adj = build_adjacency(nodes)
    finished: set[int] = set()

    def visit(u: int, stack: list[int]) -> list[int] | None:
        if u in stack:
            idx = stack.index(u)
            return stack[idx:] + [u]
        if u in finished:
            return None
        stack.append(u)
        for v in adj.get(u, []):
            cyc = visit(v, stack)
            if cyc:
                return cyc
        stack.pop()
        finished.add(u)
        return None

    for n in nodes:
        if n.number in finished:
            continue
        cyc = visit(n.number, [])
        if cyc:
            return cyc
    return None


def merge_ready_issues(nodes: list[IssueNode], merged_numbers: set[int]) -> list[int]:
    """Issues whose every in-repo blocked-by predecessor is in merged_numbers."""
    all_nums = {n.number for n in nodes}
    ready: list[int] = []
    for n in nodes:
        blockers = n.blocked_by_numbers()
        needed = [b for b in blockers if b in all_nums]
        if all(b in merged_numbers for b in needed):
            ready.append(n.number)
    return sorted(ready)
