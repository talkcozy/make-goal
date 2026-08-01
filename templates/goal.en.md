# {{PROJECT_OR_OBJECTIVE_NAME}} Goal

## Objective

{{Describe the final outcome. Write this so a fresh AI agent can understand what must exist when the work is complete.}}

## Output Location

Primary workspace:

`{{ABSOLUTE_OR_REPOSITORY_PATH}}`

Goal file:

`{{PATH_TO_GOAL_MD}}`

## Background

{{Summarize the user's context, existing work, prior decisions, reference files, links, and why the goal matters.}}

## References to Inspect

- `{{path-or-link}}`: {{why it matters}}

## Scope

In scope:

- {{included work}}

Out of scope:

- {{excluded work}}

Assumptions:

- {{assumption}}

## Constraints

- Technology/platform: {{constraints}}
- Quality/style: {{constraints}}
- Safety/privacy/legal/licensing: {{constraints}}
- Budget/timeline/autonomy: {{constraints}}

## Execution Harness and Environment

Expected executor:

- {{Codex / Claude Code / generic agent / human + agent}}

Runtime:

- OS/shell: {{expected environment}}
- Working directory: `{{path}}`
- Required runtimes: {{Node/Python/Go/etc. and versions}}

Required tools:

- {{tool}}: {{why needed}}; verify with `{{command}}`

Dependency setup:

```bash
{{install or bootstrap commands}}
```

Secrets and external services:

- `{{ENV_VAR_OR_SERVICE}}`: {{purpose}}; verify presence without printing secret values.

Permissions:

- Allowed: {{actions}}
- Ask before: {{risky actions}}
- Forbidden: {{actions}}

Baseline harness check:

```bash
{{commands that prove the environment is ready}}
```

Fallback rules:

- If {{tool/service/credential}} is missing, {{fallback behavior}}.
- If validation cannot run, record why in `{{progress/validation.md}}` and run {{replacement check}}.

## Deliverables

- {{deliverable}}

## Milestones

### M0: {{Milestone name}}

Tasks:

- {{task}}

Acceptance criteria:

- {{check}}

### M1: {{Milestone name}}

Tasks:

- {{task}}

Acceptance criteria:

- {{check}}

## Agent Work Loop

Every agent cycle must:

1. Read this `goal.md`.
2. Read progress records listed below.
3. Inspect the current workspace state.
4. Run the baseline harness check and bootstrap missing required dependencies when documented.
5. Run the quickest relevant baseline validation.
6. Choose the highest-priority unfinished task.
7. Implement a small, verifiable increment.
8. Run relevant validation.
9. Fix failures caused by the increment.
10. Update progress records, including harness notes when environment state changes.
11. Continue while budget remains and no blocking condition exists.

Do not stop after planning when implementation is possible. Do not claim completion without validation.

## Progress Tracking

Maintain:

- `{{progress/worklog.md}}`: completed work, changed files, next task, risks.
- `{{progress/validation.md}}`: commands/checks run, pass/fail status, failures, skipped checks.
- `{{progress/decisions.md}}`: durable decisions and rationale.
- `{{progress/harness.md}}`: environment status, dependency setup, missing tools, fallbacks used.

## Validation Plan

Required checks:

- `{{command-or-review}}`

Manual checks:

- {{manual QA}}

Artifact checks:

- {{files/screenshots/reports/deployments}}

## Risk and Blocking Rules

Ask the user before:

- {{risky operation}}

Treat as blocked when:

- {{blocking condition}}

When blocked:

1. Record the blocker in `{{progress/worklog.md}}`.
2. Record validation status in `{{progress/validation.md}}`.
3. Continue with independent non-blocked work if available.
4. If no meaningful work remains, report the exact blocker and needed user action.

## Quality Bar

- Correctness: {{standard}}
- Maintainability: {{standard}}
- User experience: {{standard}}
- Performance/reliability: {{standard}}
- Documentation: {{standard}}

## Completion Definition

This goal is complete only when:

- {{condition}}
