"""Parse and render `notes/orchestration_log.md` markdown tables."""

from __future__ import annotations

import re
from dataclasses import dataclass
from pathlib import Path
from typing import Any


@dataclass
class LogRow:
    """One row of the orchestration log table."""

    stream: str
    branch: str
    issue: str
    status: str
    pr: str
    reviewer: str

    def as_dict(self) -> dict[str, str]:
        return {
            "stream": self.stream,
            "branch": self.branch,
            "issue": self.issue,
            "status": self.status,
            "pr": self.pr,
            "reviewer": self.reviewer,
        }


HEADER_CELLS = ["stream / scope", "branch", "issue", "status", "pr", "reviewer"]


def _split_table_row(line: str) -> list[str]:
    raw = line.strip()
    if not raw.startswith("|"):
        return []
    parts = [p.strip() for p in raw.strip("|").split("|")]
    return parts


def _is_separator_row(cells: list[str]) -> bool:
    if not cells:
        return False
    return all(re.match(r"^:?-{3,}:?$", c) for c in cells)


def parse_orchestration_log(content: str) -> tuple[str, list[LogRow], str]:
    """Split file into preamble, table rows, and postamble (content after the table).

    Finds the first markdown table whose header matches the orchestration columns.
    """
    lines = content.splitlines()
    i = 0
    while i < len(lines):
        row = _split_table_row(lines[i])
        if len(row) >= 6:
            normalized = [c.lower() for c in row[:6]]
            if normalized == HEADER_CELLS:
                if i + 1 < len(lines):
                    sep = _split_table_row(lines[i + 1])
                    if _is_separator_row(sep):
                        preamble = "\n".join(lines[:i]).rstrip() + "\n"
                        data_start = i + 2
                        rows: list[LogRow] = []
                        j = data_start
                        while j < len(lines):
                            cells = _split_table_row(lines[j])
                            if len(cells) < 6:
                                break
                            if _is_separator_row(cells):
                                j += 1
                                continue
                            rows.append(
                                LogRow(
                                    stream=cells[0],
                                    branch=cells[1],
                                    issue=cells[2],
                                    status=cells[3],
                                    pr=cells[4],
                                    reviewer=cells[5],
                                )
                            )
                            j += 1
                        rest = lines[j:]
                        postamble = "\n".join(rest).rstrip()
                        if postamble:
                            postamble += "\n"
                        return preamble, rows, postamble
        i += 1
    return content.rstrip() + ("\n" if content and not content.endswith("\n") else ""), [], ""


def render_orchestration_log(preamble: str, rows: list[LogRow], postamble: str = "") -> str:
    """Rebuild markdown file with a single standard table between preamble and postamble."""
    header = (
        "| Stream / scope | Branch | Issue | Status | PR | Reviewer |\n"
        "|----------------|--------|-------|--------|-----|----------|\n"
    )
    body_lines = []
    for r in rows:
        body_lines.append(
            f"| {r.stream} | {r.branch} | {r.issue} | {r.status} | {r.pr} | {r.reviewer} |"
        )
    body = "\n".join(body_lines)
    if body:
        body += "\n"
    pre = preamble if preamble.endswith("\n") else preamble + "\n"
    post = postamble
    if post and not post.endswith("\n"):
        post += "\n"
    mid = header + body
    if post:
        return pre + mid + "\n" + post
    return pre + mid


def read_log_file(path: Path) -> tuple[str, list[LogRow], str]:
    text = path.read_text(encoding="utf-8")
    return parse_orchestration_log(text)


def write_log_file(path: Path, preamble: str, rows: list[LogRow], postamble: str = "") -> None:
    path.write_text(render_orchestration_log(preamble, rows, postamble), encoding="utf-8")


def rows_to_jsonable(rows: list[LogRow]) -> list[dict[str, str]]:
    return [r.as_dict() for r in rows]


def rows_from_jsonable(data: list[dict[str, Any]]) -> list[LogRow]:
    out: list[LogRow] = []
    for item in data:
        out.append(
            LogRow(
                stream=str(item.get("stream", "")),
                branch=str(item.get("branch", "")),
                issue=str(item.get("issue", "")),
                status=str(item.get("status", "")),
                pr=str(item.get("pr", "")),
                reviewer=str(item.get("reviewer", "")),
            )
        )
    return out
