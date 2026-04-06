# Replication README — Sample Completed Example

> A completed replication README for a minimum-wage employment effects project. Use as reference during Day 4.

---

# Replication README — Minimum Wage and Teen Employment

> Anyone with access to FRED and this repo should be able to reproduce our results.

---

## Project Title

**Minimum Wage Employment Effects: A State-Level Panel Analysis (2010–2023)**

---

## Overview

This project estimates the effect of state minimum wage changes on teen employment using a two-way fixed effects specification. We use state-level data from FRED (teen employment rate, minimum wage) and the CPI for deflation. The replication package contains the data fetch script, analysis pipeline, and output generation. Main output: coefficient on real minimum wage in a regression of teen employment on state and year fixed effects.

---

## Requirements

| Requirement | Version / Notes |
|-------------|-----------------|
| **OS** | macOS 14+, Linux, or Windows 11 |
| **Python** | 3.10+ |
| **Key packages** | pandas, numpy, matplotlib, fredapi; see `requirements.txt` |
| **Data access** | FRED API key (free at https://fredaccount.stlouisfed.org/apikeys) |
| **Other** | None |

---

## Directory Structure

```
min-wage-employment/
├── data/
│   ├── raw/           # Fetched from FRED (gitignored if large)
│   └── processed/     # panel.csv
├── src/
│   ├── fetch_data.py
│   ├── run_analysis.py
│   └── generate_figures.py
├── results/
│   ├── estimates.csv
│   └── figures/
├── replication/       # This README and run scripts
├── docs/
├── requirements.txt
└── README.md
```

---

## Setup Instructions

1. **Clone the repository**
   ```bash
   git clone https://github.com/your-org/min-wage-employment.git
   cd min-wage-employment
   ```

2. **Create virtual environment**
   ```bash
   python -m venv .venv
   source .venv/bin/activate   # On Windows: .venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Configure data access**
   - Obtain a FRED API key from https://fredaccount.stlouisfed.org/apikeys
   - Set the key: `export FRED_API_KEY=your_key_here` (or add to `.env` and load with python-dotenv)
   - Add `.env` to `.gitignore` (do not commit the key)

5. **Verify setup**
   ```bash
   python -c "import pandas, fredapi; print('OK')"
   ```

---

## Running the Pipeline

Run in order. Exact commands:

```bash
# Step 1: Fetch data from FRED
python src/fetch_data.py

# Step 2: Run analysis (builds panel, estimates model)
python src/run_analysis.py

# Step 3: Generate figures
python src/generate_figures.py
```

**One-liner (if you have a master script):**
```bash
python src/run_all.py
```

**Approximate runtime:** ~3 minutes on a standard laptop (fetch ~1 min, analysis ~1 min, figures ~30 s).

---

## Expected Outputs

| File / artifact | Description |
|-----------------|-------------|
| `data/processed/panel.csv` | State-year panel with employment rate, real min wage, CPI |
| `results/estimates.csv` | Regression coefficients, SEs, R² |
| `results/figures/fig1_effect.pdf` | Coefficient plot with 95% CI |
| `results/figures/fig2_trends.pdf` | Teen employment and min wage over time |

---

## Troubleshooting

| Issue | Solution |
|-------|----------|
| FRED API rate limit | Add short delay between requests; or use cached data in `data/raw/` if provided |
| Missing FRED_API_KEY | Ensure `export FRED_API_KEY=...` before running; or check `.env` is loaded |
| ModuleNotFoundError | Run `pip install -r requirements.txt` from activated venv |
| Version mismatch | Pin versions in requirements.txt; we tested with pandas 2.0+, fredapi 0.5+ |
| No data/raw/ directory | `fetch_data.py` creates it; ensure write permission in project root |

---

## Known Limitations

- Sample: 2010–2023, US states only (no DC). Some states have missing min wage in early years; we use last-observed carryforward.
- FRED series used: `LASST*` (state employment), `STTMINWG*` (state min wage), `CPIAUCSL` (national CPI). See `src/fetch_data.py` for exact series IDs.
- Robustness: No placebo tests or alternative specifications in this package; see paper for full set.

---

## Contact

[Jane Doe](mailto:jane.doe@university.edu) — Replication questions.

---

*Tested: Clean run on 2025-03-17. Fresh clone, new venv, FRED API key in env.*
