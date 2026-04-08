---
name: game-theory-analysis
description: Structures game-theory analysis across normal-form and extensive-form settings. Use when defining players, actions, information, equilibrium concepts, or comparative statics in strategic interaction problems.
---

# Game Theory Analysis

## Trigger

Use when the task involves:
- strategic interaction with explicit players and payoffs
- best responses, incentives, or equilibrium selection
- normal-form, extensive-form, or repeated-game reasoning
- mechanism design or credibility questions at a lightweight project level

## Workflow

1. Restate the primitives: players, actions, payoffs, timing, and information.
2. Name the equilibrium concept before solving.
3. Check best-response logic, beliefs, and incentive constraints explicitly.
4. Distinguish the formal result from intuition, welfare discussion, or extensions.

## Guardrails

- Do not switch equilibrium concepts mid-analysis.
- Keep off-path beliefs explicit in sequential games.
- State how multiplicity, tie-breaking, or equilibrium selection is handled.
- Separate existence, uniqueness, and comparative-statics claims.

## Output

Return:
- the game primitives
- the equilibrium concept being used
- the core argument or solution
- open ambiguities or multiple-equilibrium issues
- the interpretation, clearly labeled as intuition or implication

## Additional Resources

- For checklists and common mistakes, see [reference.md](reference.md).
