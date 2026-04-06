# Research Design Memo — Minimum Wage / Youth Employment

> Completed example for the Agentic Coding for Economists capstone. Use as reference.

---

## Research Question

What is the causal effect of minimum wage increases on youth (ages 15–24) employment and hours worked across EU member states, and does the effect differ by country institutional context (e.g., collective bargaining coverage, labor market flexibility)?

---

## Motivation and Literature Context

Minimum wage policy remains contentious. Standard theory predicts employment losses for low-skill workers; monopsony and search models predict smaller or zero effects. Empirical evidence is mixed. US evidence (Card-Krueger, Dube, Cengiz et al.) focuses on state-level variation; EU evidence is sparser and often country-specific. Youth are a key group: they are over-represented among minimum-wage workers and may experience larger employment elasticities.

This project contributes by: (1) using harmonized Eurostat data for multiple EU countries; (2) exploiting staggered minimum wage changes in a difference-in-differences design; (3) testing heterogeneity by collective bargaining coverage and employment protection. Policy relevance: EU debates on fair wages and youth employment.

**Key references (5):**

1. Neumark & Wascher (2008) — Classic review; highlights identification challenges.
2. Cengiz et al. (2019) — Event study with staggered adoption; finds small employment effects.
3. Dube (2019) — Contiguous-county design; questions negative employment effects.
4. Eurostat — LFS and minimum wage series; our data source.
5. OECD ICTWSS — Institutional indicators for heterogeneity.

---

## Hypothesis / Hypotheses

- **H1:** An increase in the real minimum wage reduces youth employment rate, ceteris paribus (negative elasticity).
- **H2:** The employment effect is smaller (less negative) in countries with higher collective bargaining coverage.
- **H3:** The employment effect is larger (more negative) in countries with stricter employment protection legislation (EPL).

---

## Data Description

| Field | Description |
|-------|-------------|
| **Source** | Eurostat (minimum wages, LFS employment/hours); OECD (bargaining coverage, EPL) |
| **Access** | Public (Eurostat bulk download or API; OECD stats); Eurostat microdata may require application |
| **Key Variables** | Minimum wage (nominal, real); youth employment rate; hours worked; country, year; collective bargaining coverage; EPL index |
| **Sample** | EU countries, 2000–2024 (or latest); annual; N ≈ 25 countries × 25 years |
| **Unit of observation** | Country-year |

---

## Empirical / Theoretical Strategy

- **Main specification**: Two-way fixed effects (TWFE) difference-in-differences.
  - Outcome: Youth employment rate (or log hours); alternatively, employment-to-population ratio.
  - Treatment: Log real minimum wage (deflated by CPI) or ratio of minimum to median wage.
  - Controls: GDP growth, unemployment rate, youth share of population.
  - FEs: Country, year. SEs clustered by country.

- **Heterogeneity**: Interact treatment with (1) collective bargaining coverage tertile, (2) EPL tertile.

- **Software**: Python (pandas, linearmodels PanelOLS, statsmodels for robustness).

---

## Identification Strategy

- **Source of variation**: Within-country changes in nominal minimum wage over time; cross-country variation in timing and magnitude.
- **Assumptions**: Parallel trends in outcomes absent treatment; no anticipatory employment changes; treatment timing exogenous to country-specific shocks.
- **Threats**: Composition effects (migration, schooling); measurement error in minimum wage (subnational vs national); staggered adoption may bias TWFE (Callaway-Sant’Anna as robustness).
- **Robustness**: Callaway-Sant’Anna estimator; placebo pre-period; alternative age groups (25–34); alternative outcomes (hours, part-time share).

---

## Expected Results

- **H1**: We expect a negative but modest coefficient on log minimum wage (elasticity in the range -0.1 to -0.3 based on prior meta-analyses). Null effect would also be informative.
- **H2**: Smaller (less negative) effect in high bargaining-coverage countries.
- **H3**: More negative effect in high-EPL countries (wage floor binds more when adjustment costs are higher).

---

## Limitations and Robustness

- **Limitations**: Eurostat aggregates may mask within-country heterogeneity; measurement of effective minimum wage (coverage, compliance) may vary; sample excludes some EU countries with limited data.
- **Robustness checks**: (1) Callaway-Sant’Anna for staggered adoption; (2) subsample by region (e.g., Western vs Eastern EU); (3) alternative treatment definitions (Kaitz index); (4) placebo in pre-period.

---

## References

See `references/bibliography.bib` for full BibTeX. Key entries: NeumarkWascher2008, Cengiz2019, Dube2019, Eurostat, OECD_ICTWSS.

---

*Guidance: This memo becomes the basis for requirements spec, task breakdown, and implementation backlog.*
