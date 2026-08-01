# goal.md Specification / goal.md 规范

`make-goal` produces executable goal documents for AI agents.

`make-goal` 用来生成可被 AI agent 执行的目标文档。

## What makes a goal executable?

An executable goal:

- contains the final outcome, not only the next step
- includes paths, references, assumptions, and constraints
- defines the execution harness: runtime, tools, dependency setup, permissions, secrets, services, readiness checks, and fallbacks
- decomposes work into milestones with acceptance criteria
- defines a repeatable agent work loop
- tells agents how to validate work
- tells agents where to record progress
- defines risks, blockers, and completion conditions

## What goal.md is not

`goal.md` is not:

- a vague project brief
- a motivational note
- a one-time checklist
- a hidden-context prompt that only works in the original chat
- a substitute for validation

## Recommended Progress Files

For project work, use:

- `progress/worklog.md`
- `progress/validation.md`
- `progress/decisions.md`
- `progress/harness.md`

For research or writing work, use equivalents such as:

- `progress/research-log.md`
- `progress/sources.md`
- `progress/review-notes.md`

The exact filenames can change, but `goal.md` must define them.

## Harness Readiness

Every serious `goal.md` should tell future agents how to verify the environment before doing the main work:

- required OS/shell assumptions
- working directory
- language runtimes and versions
- package managers and install commands
- browsers, CLIs, plugins, MCP servers, or local apps
- required env vars or external services, without secret values
- permissions and approval boundaries
- baseline readiness commands
- fallback behavior when optional or required pieces are missing

The goal should prevent agents from stopping just because one optional tool is absent. It should also prevent agents from pretending an unverified environment is ready.
