---
name: economics-literature-review
description: Finds and synthesizes recent economics literature for a research question, prioritizing top economics journals and strong working-paper venues, resolving paywalled links through IDEAS/RePEc or author webpages, and writing a markdown review. Use when the user asks for a literature search, literature review, related-work scan, paper shortlist, bibliography, or economics article review.
---

# Economics Literature Review

## Trigger

Use when the task involves:
- finding recent economics papers for a research question
- building a top-10 reading list or related-work shortlist
- writing a markdown literature review or paper scan
- handling paywalled journal articles by locating open versions

## Defaults

- Read the research question from `spec/intent.md`, under `## Research Question`, unless the user points to another file.
- Write the review to `docs/literature-review.md` unless the user requests another path.
- Start with the last 5 years. Widen to roughly the last 10 years if the recent pool is too thin.
- Prioritize top economics journals first, then strong theory or field journals, then leading working-paper series if needed.

## Workflow

1. Read the research question and extract the core topic, model terms, equilibrium concept, and likely synonym phrases.
2. Search recent economics literature with a journal-first pass, then widen to IDEAS/RePEc and major working-paper venues.
3. Build a candidate set larger than 10 papers, then screen for fit, recency, economics relevance, and venue quality.
4. For each shortlisted paper, verify the abstract and metadata, then capture citation, year, venue or status, and a usable access link.
5. If the journal page is paywalled, look for a free version on IDEAS/RePEc, the authors' webpages, NBER, CEPR, SSRN, arXiv, or an institutional repository.
6. Rank the 10 strongest matches, explain why each matters for the research question, and separate published papers from working papers.
7. Write the markdown review and tell the user about any unresolved access issues or thin-coverage areas.

## Guardrails

- Prefer economics papers over adjacent math or control papers unless the adjacent paper is clearly necessary for the economics question.
- Do not imply publication status when the paper is still a working paper or the status is unclear.
- If top-journal matches are sparse, say so directly and explain why lower-tier journals or working papers were included.
- Record access status explicitly: open version found, journal page paywalled but free version found, or no free version located.
- Do not include a paper you have not verified at least through abstract-level evidence.

## Output

Return:
- the extracted research question
- the search scope and selection logic
- a ranked top-10 list with citation, venue or status, year, access link, and a short relevance note
- a short synthesis of common themes, open gaps, and next-search directions
- an access-issues section listing paywalled or unresolved papers

## Additional Resources

- For venue priorities, access fallback order, and a markdown template, see [reference.md](reference.md).
