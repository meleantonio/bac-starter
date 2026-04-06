# Consistency and Verification Review Log — Example

> A completed example review log showing findings from a PR review. Use as reference during Day 3 Sprint B.

---

## Review Metadata

| Field | Value |
|-------|-------|
| **Date** | 2025-03-17 |
| **Reviewer** | pr-reviewer subagent + A. Smith |
| **Branch / PR** | `rig/analysis` / #8 |
| **Scope** | Analysis script (run_analysis.py), results output, handoff to paper |

---

## Consistency Checks

| Check | Pass? | Notes |
|-------|-------|-------|
| Code runs without errors | ✓ | `python src/run_analysis.py` succeeds in venv |
| Outputs match description in docs | ✓ | estimates.csv and figures/ produced as in handoff |
| No hardcoded paths (use config/env) | ✗ | Line 42: `/Users/authors/data/` — must use relative path or env |
| Dependencies documented (`requirements.txt`, etc.) | ✓ | pandas, numpy, matplotlib listed |
| Data access instructions present | ✓ | replication/README.md describes data/ placement |
| Reproducible from clean clone | ✗ | Blocked by hardcoded path above |

---

## Correctness Checks

| Check | Pass? | Notes |
|-------|-------|-------|
| Methodology aligns with research design | ✓ | OLS regression as in docs/research_design_memo.md |
| Results plausible (sanity checks) | ✓ | Coefficients in reasonable range; R² ~0.35 |
| Edge cases considered (missing, zeros) | ✓ | dropna() used with warning logged |
| Units and definitions consistent | ✓ | Matches handoff_data_to_analysis.md |

---

## Style Checks

| Check | Pass? | Notes |
|-------|-------|-------|
| Naming conventions followed | ✓ | snake_case, descriptive names |
| Functions/classes documented | ✗ | `estimate_model()` missing docstring |
| Code structure readable | ✓ | Clear sections for load, estimate, export |

---

## Findings

| Severity | File | Issue | Suggested Fix |
|----------|------|-------|---------------|
| High | src/run_analysis.py:42 | Hardcoded path `/Users/authors/data/raw/` | Use `Path(__file__).parent.parent / "data" / "raw"` or env var `DATA_PATH` |
| Medium | src/run_analysis.py | Missing docstring on `estimate_model()` | Add Google-style docstring with Args, Returns |
| Low | src/run_analysis.py:87 | Magic number `0.05` for alpha | Define `SIGNIFICANCE_LEVEL = 0.05` at module top |

---

## Verdict

- [ ] **Pass** — Ready to merge; no blocking issues
- [x] **Revise** — Address findings above, then re-review
- [ ] **Fail** — Significant issues; do not merge

**Reviewer signature / note:** Fix the hardcoded path (High) and add docstring (Medium) before merge. Low-priority items can be follow-up. Re-run replication-checker after fix.

---

*This example shows a typical mix of blockers and suggestions. Address High/Medium before merge.*
