# HANK Modeling Reference

## Calibration Checklist

- Map each parameter to a target, citation, or modeling reason.
- Keep time units consistent across preferences, technology, fiscal policy, and transition horizons.
- Note which parameters are free, estimated, borrowed, or normalized.

## Stationary Equilibrium Checks

- Policy functions are defined on the full relevant state space.
- Distribution mass is non-negative and sums or integrates to one.
- Market-clearing residuals are explicitly reported.
- Euler equation or HJB/KFE residuals are small where accuracy matters.
- Aggregates implied by individual behavior match the reported aggregates.

## Transition-Path Checks

- Shock timing and policy timing are explicit.
- Initial and terminal conditions are documented.
- The terminal steady state is consistent with the policy experiment.
- The path is checked for implausible jumps caused by grid or interpolation issues.

## Common Failure Modes

- Frequency mismatch between calibration targets and model timing.
- Convergence in the outer loop while inner objects remain unstable.
- Distribution updates that lose mass or create negative density.
- Policy comparison that changes multiple objects at once without stating it.

## Reporting Pattern

- Start with the economic question.
- Then summarize calibration or equilibrium diagnostics.
- End with interpretation and remaining numerical caveats.
