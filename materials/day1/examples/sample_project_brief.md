# Project Brief — Agentic Coding for Economists

> Completed example for the minimum wage youth employment capstone. Use as reference.

---

## Project Title

The Effect of Minimum Wage Increases on Youth Employment in EU Countries

---

## Research Question

What is the causal effect of minimum wage increases on youth (ages 15–24) employment and hours worked across EU member states, and does the effect differ by country institutional context (e.g., collective bargaining coverage, labor market flexibility)?

---

## Expected Contribution

This project contributes to the minimum wage literature by: (1) providing EU-wide evidence using harmonized Eurostat data and a difference-in-differences design with staggered policy adoption; (2) testing heterogeneous effects by institutional context; (3) producing a reproducible pipeline that can be extended to other subgroups and policy interventions. The results are policy-relevant for EU labor market reforms and youth employment initiatives.

---

## Data Sources

| Source Name | URL / Location | Format | Time Coverage | Notes |
|-------------|----------------|--------|---------------|-------|
| Eurostat — Annual minimum wages | https://ec.europa.eu/eurostat/databrowser | CSV, API | 2000–2024 | Harmonized gross minimum wage (national currency, monthly). Requires Eurostat bulk download or API. |
| Eurostat — LFS youth employment | https://ec.europa.eu/eurostat/databrowser | CSV, API | 2000–2024 | Employment rate, hours worked by age 15–24; annual and quarterly. LFS microdata access may require application. |
| OECD — Institutional indicators | https://stats.oecd.org | CSV, Excel | 2000–2023 | Collective bargaining coverage, EPL index. Good for heterogeneity. |
| ICTWSS database | https://ictwss.org | Stata, CSV | 1960–2022 | Union density, bargaining coverage; useful robustness. |

---

## Method Approach

- **Main specification**: Two-way fixed effects (TWFE) difference-in-differences with country and year FEs. Outcome: youth employment rate (or log hours). Treatment: real minimum wage (in logs or as ratio to median wage). Standard errors clustered by country.
- **Heterogeneity**: Interact treatment with institutional dummies (collective bargaining coverage, EPL).
- **Robustness**: Callaway-Sant’Anna estimator for staggered adoption; placebo pre-period; alternative age groups.
- **Software**: Python (pandas, linearmodels, statsmodels).

---

## Key Deliverables (4‑Day Sprint)

- [x] Project brief (1 page) — this document
- [ ] Issue board (≥8 issues)
- [ ] Research design memo
- [ ] Working prototype (code + docs)
- [ ] Replication package + README
- [ ] 5–7 minute presentation
- [ ] 30‑day adoption plan

---

## Timeline (4‑Day Sprint)

| Day | Focus | Key Outputs |
|-----|-------|-------------|
| Day 1 | Setup, project definition, governance | Brief, issues, rules, first PR |
| Day 2 | Research design, data plan, specs | Design memo, bib, data map |
| Day 3 | Parallel sprint, prototype, review | Prototype code, review log |
| Day 4 | Integration, replication, presentation | README, clean run, slides |

---

## Acceptance Criteria

- [x] Research question is clear and testable
- [x] Data sources are accessible or obtainable within the sprint
- [x] Method is feasible in 4 days (prototype-level)
- [ ] All deliverables listed above can be completed by Day 4 end

---

*Guidance: Update this brief as you refine scope. It should feed your issue board and AGENTS.md.*
