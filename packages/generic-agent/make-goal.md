# make-goal for Generic AI Agents

Use this instruction when a user wants a long-running AI agent to complete a complex task later. Your output is a durable `goal.md`.

## Process

1. Understand the user's final objective.
2. Ask for missing critical context:
   - final outcome
   - output path
   - references to inspect
   - executor agent/tooling
   - execution harness: runtime, tools, dependency setup, permissions, credentials, services, baseline checks, fallbacks
   - constraints
   - definition of done
   - validation method
   - autonomy and safety rules
3. Inspect referenced materials when available.
4. Write `goal.md` in the user's language unless they request bilingual output.
5. Make `goal.md` self-contained and executable.

## Required Sections

- Objective
- Output Location
- Background
- References to Inspect
- Scope
- Constraints
- Execution Harness and Environment
- Deliverables
- Milestones with Acceptance Criteria
- Agent Work Loop
- Progress Tracking
- Validation Plan
- Risk and Blocking Rules
- Quality Bar
- Completion Definition

## Key Rule

A plan is not enough. The `goal.md` must tell future agents exactly how to check and bootstrap the environment, resume, choose work, implement, verify, record progress, handle blockers, and know when the goal is complete.
