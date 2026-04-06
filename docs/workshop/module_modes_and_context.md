# Module: Agent, Ask, Plan, Debug + Context Control

## Version note

Cursor’s **@** menu and feature names change between releases. Before the workshop, open the **Agent** side panel (**Cmd+I** / **Ctrl+I**), inspect which @ targets your build offers, and align demos with the current [Prompting agents](https://www.cursor.com/docs/agent/prompting) guide. **Switching modes may start a fresh context window**—note that for long threads.

## Objectives

By the end of this module, participants will:

- Distinguish **Agent**, **Ask**, **Plan**, and **Debug** modes and choose the right mode for each task type
- **Scope context** using **@ Files**, **@ Folders**, **@ Docs**, symbols/links as available, and plain-language instructions (“only edit this path…”, “search the repo for…”). Older materials used `@Codebase` / `@Web` chips; on Cursor 2.x you often **ask the agent to search the web or the codebase** without those exact @ items—verify on your version.
- Understand tight vs wide context: when to narrow scope vs when to allow broad search
- Explain how **customization** beyond the four modes is usually done with **rules, skills, subagents, and MCP**—not necessarily a separate “Custom mode” chip
- Produce a personal modes playbook for economics workflows

## Prerequisites

- Cursor installed and authenticated
- A local repo (or `examples/` folder) with at least one Python file (e.g., a stub or existing economics utility)
- Basic familiarity with the **Agent** side panel and the mode selector

## Demo Script

### Setup

1. Open Cursor with a clean project that has a simple economics example (e.g., `examples/gini_stub.py` or a minimal `src/utils/` with one file)
2. Ensure participants can see the **Agent** panel and the **mode** selector (**Shift+Tab** or the picker, depending on version)
3. Have the same task written in a visible place: *"Write a Python function to compute the Gini coefficient from a list of income values, with docstring and unit tests"*

### Steps (numbered, instructor-facing)

1. **Ask mode demo (5 min)**
   - Select **Ask** mode
   - Paste the Gini task prompt
   - Show that the AI responds with code, explanations, and suggestions—but does **not** apply edits to files
   - Point out: useful for research, verification, exploration; no risk of overwriting; requires manual copy-paste

2. **Agent mode demo (7 min)**
   - Select **Agent** mode
   - Paste the **same** task prompt
   - Show that the AI creates/edits files, runs commands, and iterates
   - Compare outputs: file creation, test execution, potential for more complete integration

3. **Side-by-side comparison (3 min)**
   - Open two threads or tabs: one with Ask output, one with Agent output
   - Highlight: Ask = research/reference; Agent = implementation and automation
   - Emphasize: both valid; choice depends on whether you want to "think" or "do"

4. **Plan mode (3 min)**
   - Switch to **Plan** mode
   - Same task: show that the AI first produces a plan (steps, files, dependencies) before implementation
   - Use case: complex multi-file changes, research design breakdowns

5. **Debug mode (2 min)**
   - Use **Debug** mode on a file with an intentional bug (e.g., off-by-one in Gini formula)
   - Show systematic debugging flow: hypothesis → test → fix

6. **Context scoping demo (8 min)**
   - **Repo-wide:** Ask: "Search this codebase: where do we load income data? Propose where to add a Gini call." Attach a **folder** or use @ Files if that fits your build.
   - **Web / literature:** Ask: "Search the web: what is the standard Gini formula for grouped data? Cite a standard reference." (If your Cursor build exposes **@Web** or web search in the @ menu, you may use it—optional.)
   - **@ Docs:** Attach library docs (e.g., pandas, numpy) when you have indexed them under **@ Docs**.
   - **Data file:** Attach `data/sample_incomes.csv` (or @ the file) and ask: "Compute and report the Gini."
   - Show how **narrowing** attachments and instructions changes focus and reduces drift

7. **Tight vs wide context (5 min)**
   - Tight: "Only edit `src/models/gini.py`: fix the edge case when input is empty."
   - Wide: "Search the repo and add Gini support across analysis scripts that use income data."
   - Explain: tight = precision, reproducibility; wide = consistency, integration

### Key Points to Emphasize

- **Ask = read-only, Agent = read-write**. Use Ask when you are learning or prototyping; use Agent when you want files changed and tasks automated.
- **Plan before building**. For multi-step research pipelines, Plan mode (or explicit planning prompts) reduces wasted edits.
- **Context is your quality lever**. Attach files/folders, name paths explicitly, and ask for web or repo search in plain language—match what your Cursor version supports.
- **Economists:** Use scoped folders/files for "stay in this codebase"; explicit web search for literature/formulas; attached files for data-aware tasks.

## Hands-On Exercise

### Minimum Viable Path

1. **Ask vs Agent (15 min)**
   - Pick one economics task from: "compute the mean and median of a numeric column", "write a function to standardize variables (z-score)", or "explain how to use `statsmodels` for OLS"
   - Run it in **Ask** mode first: get code + explanation
   - Run the **same** task in **Agent** mode: let it create a file and run it
   - Compare: which output is more useful for your workflow? When would you use each?

2. **Context practice (15 min)**
   - In a repo with 2–3 Python files and possibly a data file:
     - Ask: "Where do we load data, and what format is expected?" with the **`src/`** folder (or repo root) in context
     - Ask: "Search the web: what is the current recommended way to read Parquet in pandas?"
   - If you have a CSV: attach it and ask: "Summarize the column types and row count of this file"

3. **Document your findings (10 min)**
   - Create `notes/modes_playbook.md` with:
     - When you use Ask vs Agent vs Plan
     - Which context pattern you used (files, folders, web ask, docs) and why
     - One "tight context" and one "wide context" example from your work

### Extension Challenge

- **Multi-file consistency**: Use Agent mode with the relevant directory in context to add a new utility (e.g., Gini) and ensure it is called from existing analysis scripts. Verify no duplicate implementations.
- **Plan → Agent handoff**: Use Plan mode to break a research task (e.g., "build a simple IV pipeline") into steps; then switch to Agent and implement step 1 only, using tight path scope for that step.

## When You Get Stuck

| Symptom | Likely cause | Try |
|--------|---------------|-----|
| AI keeps editing wrong files | Too wide context; no path scope | Name the file or folder explicitly; attach only what is needed |
| AI hallucinates formulas | No grounding in your code/data | Attach data/code or ask for web search with explicit request |
| Agent makes too many changes | Task underspecified; Agent over-interprets | Use Ask first to refine; or switch to Plan mode |
| Can't find "Plan" or "Debug" | Cursor version or UI differs | Update Cursor; check Settings → Modes / Agent help |
| @ item missing | Product/UI change | Use natural language ("search the web…", "search the repo…") per [Prompting agents](https://www.cursor.com/docs/agent/prompting) |

## Expected Artifacts

- `notes/modes_playbook.md`: Personal reference with mode choices, context patterns, and tight/wide examples
- Optionally: `notes/context_patterns.md` linking to this module for future reference

## Key Prompts

**Ask mode – research / exploration**
```
Search the web: What is the formula for the Gini coefficient when income data is grouped into deciles?
Provide the formula and a simple numerical example.
```

**Ask mode – code comprehension**
```
Using this repository context, trace how we load survey data and compute summary statistics.
List the functions involved and their inputs/outputs.
```

**Agent mode – implementation**
```
Create a Python function `gini(values: list[float]) -> float` that computes the Gini coefficient
using the standard formula. Add a Google-style docstring, handle edge cases (empty list, single value),
and add 3 pytest tests in `tests/test_gini.py`. Place the function in `src/utils/inequality.py`.
```

**Agent mode – integration**
```
Find the main analysis script that loads income data. Add a call to our
`gini()` function (from src/utils/inequality.py) and print the result after loading.
Do not modify any other files.
```

**Context narrowing**
```
Only edit `src/utils/inequality.py`. Fix the edge case when the input list is empty.
Return 0.0 with no other changes to the function.
```

**Context widening**
```
Search the repo: we added `gini()` in src/utils/inequality.py`.
Find all analysis scripts that use income/wealth data and add a Gini computation
if they don't already have one. Keep changes minimal.
```

**Plan mode – breakdown**
```
Plan the implementation of a 2SLS IV estimator for a simple demand equation:
y = X*β + u, with instruments Z. List the steps, files to create/modify,
and dependencies. Do not implement yet.
```

## Further Reading

- Cursor — Agent overview: https://www.cursor.com/docs/agent/overview
- Cursor — Plan mode: https://www.cursor.com/docs/agent/plan-mode
- Cursor — Prompting agents: https://www.cursor.com/docs/agent/prompting
- Cursor help — [Ask](https://cursor.com/help/ai-features/ask-mode), [Agent](https://cursor.com/help/ai-features/agent), [Plan](https://cursor.com/help/ai-features/plan-mode), [Debug](https://cursor.com/help/ai-features/debug-mode)
