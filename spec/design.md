# Design Specification

> **Guidance followed:** keep the baseline tight, keep assumptions explicit, and make any optional verification traceable to the same analytic benchmark.

## Architecture

This project is a theory-first research pipeline centered on one canonical continuous-time linear-quadratic differential game. The architecture is intentionally narrow: a baseline model definition feeds one equilibrium-derivation path, which feeds a comparative-statics layer, which optionally feeds a lightweight verification-and-replication layer. The default baseline equilibrium concept is feedback Nash unless the project explicitly documents a different single-concept choice.

```text
intent -> model_definition -> equilibrium_derivation -> comparative_statics -> verification_and_replication
```

### Components

- `model_definition`
  - Owns the research question, players, controls, state dynamics, horizon, boundary conditions, payoff functionals, and notation.
  - Produces the baseline primitives plus a named assumption ledger.
- `equilibrium_derivation`
  - Owns the chosen equilibrium concept and one solution method that matches it.
  - Produces equilibrium conditions, control laws, and any existence or uniqueness results.
- `comparative_statics`
  - Owns parameter-by-parameter changes to equilibrium controls, state paths, and value or welfare objects.
  - Produces a result registry with explicit dependence on assumptions.
- `verification_and_replication`
  - Owns optional symbolic or numeric checks, canonical entry points, and rerun instructions.
  - Produces a short replication note and flags any mismatch between verification artifacts and the analytic benchmark.

## Data Models

```python
from dataclasses import dataclass


@dataclass(frozen=True)
class GamePrimitives:
    players: tuple[str, str]
    state_description: str
    control_descriptions: dict[str, str]
    dynamics: str
    horizon: str
    boundary_conditions: str
    payoffs: dict[str, str]


@dataclass(frozen=True)
class AssumptionSet:
    identifiers: tuple[str, ...]
    summary: str
    parameter_restrictions: tuple[str, ...]
    purpose: str


@dataclass(frozen=True)
class EquilibriumResult:
    equilibrium_concept: str
    solution_method: str
    control_laws: dict[str, str]
    state_path: str
    existence_claim: str
    uniqueness_claim: str


@dataclass(frozen=True)
class ComparativeStatic:
    parameter_name: str
    affected_object: str
    direction: str
    required_assumptions: tuple[str, ...]
    interpretation: str
```

These are conceptual models, not a commitment to immediate implementation. They define the minimum information that any note, script, or proof artifact must expose if it becomes canonical.

## Component Interfaces

### `define_baseline_game(intent) -> GamePrimitives`

- Input: research question, scope, and non-goals from `spec/intent.md`
- Output: complete baseline primitives and notation for the two-player LQ game

### `register_assumptions(primitives) -> AssumptionSet`

- Input: model primitives plus admissibility and regularity needs
- Output: named assumptions used for derivation, existence, uniqueness, and comparative statics

### `solve_baseline_equilibrium(primitives, assumptions, equilibrium_concept) -> EquilibriumResult`

- Input: primitives, named assumptions, and one baseline equilibrium concept
- Output: equilibrium conditions, control laws, state characterization, and existence or uniqueness statements

### `run_comparative_statics(result, parameter_changes) -> list[ComparativeStatic]`

- Input: baseline equilibrium result plus named parameter changes
- Output: a traceable registry of directional results and their required assumptions

### `write_replication_note(verification_artifacts) -> str`

- Input: optional symbolic or numeric checks, environment assumptions, and expected outputs
- Output: a short rerun guide that distinguishes canonical artifacts from exploratory ones

## Error Handling

- **Scope drift:** If an alternative equilibrium concept appears during the baseline derivation, move it into a clearly labeled extension instead of changing the baseline scope.
- **Assumption drift:** If a result needs stronger assumptions than previously stated, update the assumption ledger before accepting the result as canonical.
- **Proof mismatch:** If the derivation, notation, and stated result disagree, treat the result as unresolved and block downstream interpretation.
- **Verification mismatch:** If an optional symbolic or numeric check disagrees with the analytic benchmark, mark the check as exploratory until the discrepancy is resolved.
- **Reproducibility gap:** If an output lacks a canonical entry point or exact manual steps, do not treat it as a finished deliverable.

## Security Considerations

- The baseline design requires no secrets, credentials, or private data.
- If later tooling depends on external services, store secrets in environment variables rather than in code or notes.
- Use project-relative paths only.
- Treat any future raw data inputs as read-only.
- Keep exploratory notebooks, scratch algebra, or ad hoc scripts outside the canonical output path unless they are explicitly promoted and documented.

## Validation

- Check that the equilibrium concept is fixed once and reused consistently.
- Check that every result names the assumptions it depends on.
- Check limiting cases and admissibility conditions before reporting comparative statics.
- Check that every optional verification artifact points back to the same primitives and assumptions as the analytic baseline.
- Check that every canonical output can be regenerated from a documented entry point.
