---
name: hank-modeling
description: Guides HANK modeling workflows including calibration review, equilibrium checks, and transition diagnostics. Use when working on heterogeneous-agent macro models, household distributions, policy experiments, or transition-path questions.
---

# HANK Modeling

## Trigger

Use when the task involves:
- calibration targets or parameter bookkeeping
- steady states, stationary distributions, or transition paths
- policy counterfactuals in heterogeneous-agent macro models
- debugging market-clearing or aggregation logic

## Workflow

1. Restate the economic environment, agents, frictions, shocks, and equilibrium object.
2. Inventory the states, controls, laws of motion, calibration targets, and outputs that matter for the task.
3. Check numerical objects before interpretation: grids, tolerances, initialization, residuals, convergence, and distribution mass.
4. Separate economic interpretation from numerical debugging in the final response.

## Guardrails

- Do not treat solver convergence as economic validation.
- Flag missing units, timing conventions, or normalization choices.
- When comparing calibrations or policies, state what is held fixed.
- If a result depends on interpolation, terminal conditions, or aggregation, name that dependency explicitly.

## Output

Return:
- the model block or question being analyzed
- the main calibration or equilibrium checks
- open numerical risks
- the economic interpretation, clearly separated from implementation details

## Additional Resources

- For diagnostics and common failure modes, see [reference.md](reference.md).
