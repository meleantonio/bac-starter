# Day 2 Research Prompts — Copy-Paste Library

> Use these prompts in the **Agent** side panel during the Day 2 sprint. Replace `[TOPIC]` and bracketed placeholders with your project-specific text.

---

## Literature Mapping

### 1. Key Papers on Topic

```
Search the web: what are the 5–8 most cited papers on [TOPIC] from 2018–2024? 
List author, year, title, journal, and one-sentence summary of main finding.
```

### 2. Literature Gap

```
I'm studying [TOPIC]. Search the web and identify the main empirical approaches in the 
recent literature and one gap that [YOUR ANGLE] could address. 
Give 3–4 references with short relevance notes.
```

### 3. Reference Summary for Design Memo

```
I have these papers in my bibliography: [LIST KEYS FROM .bib]. 
For each, write one sentence on how it relates to my research question: "[YOUR QUESTION]".
```

### 4. BibTeX from Paper List

```
I need BibTeX entries for these papers:
1. [Author, Year, Title, Journal]
2. [Author, Year, Title, Journal]
...
Format as @article or @inproceedings. Include doi if known.
```

---

## Research Design

### 5. Research Design Memo from Brief

```
Read docs/project_brief.md and create a full research design memo in 
docs/research_design_memo.md. Include:
- Research question (refined)
- Motivation and literature context (2–3 paragraphs)
- H1, H2 hypotheses (testable, specific)
- Data description table
- Empirical strategy (specification, software)
- Identification strategy (if applicable)
- Expected results, limitations, robustness
Use templates/research_design_memo.md structure.
```

### 6. Hypothesis Refinement

```
My hypothesis is: "[YOUR DRAFT HYPOTHESIS]". 
Refine it to be more testable. Specify: (1) treatment/exposure variable, 
(2) outcome variable, (3) expected sign/direction, (4) unit of observation.
```

### 7. Specification from Hypothesis

```
Given hypothesis: "[H1]". Suggest a baseline regression specification:
- Dependent variable
- Main regressor(s)
- Controls
- Fixed effects
- Standard error clustering
- Software (e.g., linearmodels PanelOLS, statsmodels)
```

---

## Data Plan

### 8. Data Source Suggestions

```
I need data for [TOPIC]. Search the web and suggest 3–5 public data sources 
(FRED, World Bank, Eurostat, national stats, etc.) with:
- Source name and URL
- Key variables for my analysis
- Access method (API, bulk download, registration)
- Time and geographic coverage
```

### 9. Data Source Map from Design

```
Read docs/research_design_memo.md (Data Description section) and 
docs/project_brief.md. Create or update docs/data_source_map.md with 
one row per source. Include: Source Name, URL, Access Method, Format, 
Key Variables, Time Coverage, Geographic Coverage, Notes/Caveats.
Add an Access Setup Checklist at the end.
```

### 10. Data Pipeline Plan

```
My data sources are: [LIST]. I need to merge them for analysis. 
Suggest a data pipeline: (1) download/load steps, (2) merge keys and units, 
(3) cleaning steps, (4) output format. List potential issues (missing years, 
different units, etc.).
```

---

## Issue Decomposition

### 11. Decompose Research into Issues

```
Read docs/research_design_memo.md and docs/data_source_map.md. 
Decompose the research pipeline into 8–12 GitHub issues with:
- Clear title
- 1–2 sentence description
- Acceptance criteria (what "done" looks like)
- Label (data, model, estimation, writing, consistency-check)
Order by dependency (data before estimation, etc.).
```

### 12. Add Acceptance Criteria to Issues

```
I have issues [#N1], [#N2], ... for my research project. 
For each, suggest concrete acceptance criteria: runnable checks or 
outputs that define "done". Format as bullet points per issue.
```

### 13. Prioritise Backlog

```
My implementation issues are: [LIST OR PASTE]. 
Prioritise them: P0 (blocking), P1 (core path), P2 (nice-to-have). 
Explain dependencies (e.g., "Data load must complete before regression").
```

---

## Context Control

### 14. Context control plan

```
For my research project on [TOPIC], when should I use:
- Web search (literature, formulas, external data docs) — ask explicitly: "Search the web for …"
- Repo-wide questions (implementation, refactoring) — attach `src/` or root folder; ask "search this codebase for …"
- Specific files (data or config) — attach the file in the Agent panel
- Library docs — @ Docs when indexed, or paste doc URLs
Give 2–3 example prompts for each. (Exact @ menu varies by Cursor version.)
```

### 15. Verification Loop Summary

```
Summarise the verification loop for my research pipeline: 
(1) acceptance criteria per issue, (2) implement, (3) consistency check, 
(4) fail-fix-rerun. Add one concrete example for a "data load" issue 
and one for an "estimation" issue.
```

---

## Combined

### 16. Full Day 2 Setup

```
I have docs/project_brief.md done. Do the following:
1. Create docs/research_design_memo.md with full design (hypotheses, data, method, identification)
2. Create references/bibliography.bib with 8–10 entries on [TOPIC]
3. Create docs/data_source_map.md from the design memo
4. Suggest 8–10 implementation issues with acceptance criteria
Keep each artifact aligned with the project brief.
```

---

## Context and Usage

- **Ask mode**: Use prompts 1, 2, 3, 4, 6, 8, 14, 15 for research (no file edits).
- **Agent mode**: Use prompts 5, 9, 11, 12, 16 for implementation (creates/edits files).
- **Web search**: Essential for prompts 1, 2, 4, 8 (literature and data discovery).
- **Repo / folder context**: Use when prompts refer to existing docs (5, 9, 11).
