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
4. Run the quickest relevant baseline validation.
5. Choose the highest-priority unfinished task.
6. Implement a small, verifiable increment.
7. Run relevant validation.
8. Fix failures caused by the increment.
9. Update progress records.
10. Continue while budget remains and no blocking condition exists.

Do not stop after planning when implementation is possible. Do not claim completion without validation.

## Progress Tracking

Maintain:

- `{{progress/worklog.md}}`: completed work, changed files, next task, risks.
- `{{progress/validation.md}}`: commands/checks run, pass/fail status, failures, skipped checks.
- `{{progress/decisions.md}}`: durable decisions and rationale.

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

