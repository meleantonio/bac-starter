---
name: applied-microeconometrics
description: Guides applied microeconometrics workflows for estimands, identification, specification, inference, and robustness. Use when working on DiD, IV, RD, panel regressions, treatment effects, or empirical design questions.
---

# Applied Microeconometrics

## Trigger

Use when the task involves:
- identifying an estimand or empirical strategy
- deciding between specifications or inference choices
- assessing threats to identification or robustness
- interpreting regression, event-study, IV, RD, or panel results

## Workflow

1. State the estimand, unit of observation, sample, and treatment timing.
2. Spell out the identification strategy and the assumptions required for interpretation.
3. Map variables, sample restrictions, specification choices, and inference choices.
4. Report the main result, robustness evidence, and limitations separately.

## Guardrails

- Do not confuse predictive fit with identification.
- Make sample restrictions, missing-data handling, and treatment coding explicit.
- Use inference choices that match the design, and say why they do.
- Separate the preferred specification from robustness or placebo specifications.

## Output

Return:
- the estimand and empirical design
- the key identifying assumptions
- the main specification and inference choices
- the most important robustness gaps or threats
- the interpretation, with clear limits

## Additional Resources

- For identification and reporting checklists, see [reference.md](reference.md).
