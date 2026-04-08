# Venue And Output Reference

## Venue Priority

Use this order by default:

1. Top general-interest economics journals:
   - `American Economic Review`
   - `Quarterly Journal of Economics`
   - `Journal of Political Economy`
   - `Econometrica`
   - `Review of Economic Studies`
2. Strong field or theory journals when the question is specialized:
   - `RAND Journal of Economics`
   - `Theoretical Economics`
   - `Journal of Economic Theory`
   - `AEJ: Microeconomics`
   - `Games and Economic Behavior`
   - other clearly high-quality economics field journals that fit the question
3. Leading working-paper venues when published recent matches are thin or lagging:
   - `NBER Working Papers`
   - `CEPR Discussion Papers`
   - `IZA Discussion Papers`
   - department or author working-paper series with clear metadata

If the research question is highly specialized, explain any deviation from this ordering.

## Access Fallback Order

When the journal landing page is paywalled, look for a free version in this order:

1. `IDEAS/RePEc`
2. author webpage
3. `NBER`
4. `CEPR`
5. `SSRN`
6. `arXiv`
7. institutional repository or accepted-manuscript page

Keep both links when useful:
- journal or canonical landing page
- free access link actually used for review

## Review Template

Use this structure unless the user asks for something else:

```markdown
# Literature Review

## Research Question
[Quoted or paraphrased from `spec/intent.md`]

## Search Scope
- Date window:
- Venue priority:
- Search terms:
- Inclusion rule:
- Access strategy:

## Top 10 Papers

| Rank | Paper | Venue or Status | Year | Access |
| --- | --- | --- | --- | --- |
| 1 | Author, Title | Journal / Working paper | 2025 | [Open link](...) |

### 1. Author, "Title"
- Venue or status:
- Year:
- Access link:
- Why it fits:
- Core model, method, or setting:
- Key takeaway for this project:
- Access notes:

<!-- Repeat through 10 -->

## Synthesis
- Main theme 1
- Main theme 2
- Main theme 3

## Gaps And Next Search Directions
- Gap 1
- Gap 2

## Access Issues
- Paper:
  Status:
  Note:
```

## Selection Heuristics

- Prefer papers that match the economic question, not just the mathematics.
- Favor papers with clear equilibrium objects, welfare implications, or comparative statics if those are central to the question.
- Keep foundational older papers out of the top 10 unless they are necessary for framing the recent literature. If included, label them as foundational exceptions.
- When two papers are close substitutes, keep the one with stronger economics relevance or better accessibility.
