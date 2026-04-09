"""Tests for orchestration log parsing and round-trip rendering."""

from __future__ import annotations

from pathlib import Path

from tools.swarm_mcp.log_sync import LogRow, parse_orchestration_log, read_log_file, render_orchestration_log


def test_parse_repo_orchestration_log_preserves_postamble() -> None:
    root = Path(__file__).resolve().parents[2]
    path = root / "notes" / "orchestration_log.md"
    preamble, rows, postamble = read_log_file(path)
    assert "# Orchestration Log" in preamble
    assert len(rows) >= 1
    assert "## Conventions" in postamble


def test_roundtrip_table_and_postamble() -> None:
    original = """# Title

Intro line.

| Stream / scope | Branch | Issue | Status | PR | Reviewer |
|----------------|--------|-------|--------|-----|----------|
| a | b | #1 | pending | - | - |

## After

Tail.
"""
    preamble, rows, postamble = parse_orchestration_log(original)
    assert "Intro line." in preamble
    assert len(rows) == 1
    assert rows[0].stream == "a"
    assert "## After" in postamble
    rebuilt = render_orchestration_log(preamble, rows, postamble)
    preamble2, rows2, postamble2 = parse_orchestration_log(rebuilt)
    assert rows2 == rows
    assert postamble2.strip() == postamble.strip()


def test_render_empty_rows() -> None:
    out = render_orchestration_log("# H\n", [], "")
    assert "Stream / scope" in out
