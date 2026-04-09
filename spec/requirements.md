# Requirements

> **Format:** EARS (Easy Application Requirements Syntax)

## Core Requirements

1. **[REQ-001]** The research project shall define the baseline two-player continuous-time linear-quadratic differential game by stating players, state variable(s), control variable(s), law of motion, horizon, boundary conditions, and payoff functionals.
2. **[REQ-002]** The research project shall name one baseline equilibrium concept, defaulting to feedback Nash unless another choice is explicitly justified, and specify the admissible strategy class consistent with that concept.
3. **[REQ-003]** WHEN the baseline model is fully specified the research project shall derive the equilibrium conditions using a single formal solution method consistent with the chosen equilibrium concept.
4. **[REQ-004]** WHEN the research project claims existence or uniqueness the research project shall state the exact assumptions, parameter restrictions, and regularity conditions supporting the claim.
5. **[REQ-005]** WHEN the research project presents comparative statics the research project shall link each result to a named parameter change and state the predicted effect on equilibrium controls, state dynamics, and value functions or welfare objects.
6. **[REQ-006]** WHILE reporting main results, the research project shall separate formal derivations from intuition, economic interpretation, and extension discussion.
7. **[REQ-007]** IF a result depends on assumptions stronger than the baseline model THEN the research project shall label the result as conditional or extension-only.
8. **[REQ-008]** WHERE optional numeric or symbolic verification is included, the research project shall reproduce the analytic benchmark under the same primitives, assumptions, and equilibrium concept.
9. **[REQ-009]** The research project shall record canonical entry points, environment assumptions, and expected outputs for any verification artifact or exported result.
10. **[REQ-010]** IF manual intervention is required to regenerate an output THEN the research project shall document the exact sequence before that output is treated as canonical.
11. **[REQ-011]** The research project shall maintain traceability from the research question to assumptions, equilibrium results, comparative statics, and any optional extension slot.

## Properties (Invariants)

*Universal statements that must always hold true.*

1. **[PROP-001]** The baseline analysis uses one named equilibrium concept consistently from setup through interpretation.
2. **[PROP-002]** Every symbol, timing convention, and unit of interpretation remains consistent across the intent, requirements, design, and tasks.
3. **[PROP-003]** Every existence, uniqueness, or comparative-static claim is paired with the assumptions that justify it.
4. **[PROP-004]** No canonical output depends on an undocumented absolute path, hidden local state, or undocumented manual intervention.
5. **[PROP-005]** The baseline scope remains theory-first and does not silently expand into empirical estimation or dataset-driven calibration.
