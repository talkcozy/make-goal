# Example: Software Refactor Goal

## Objective

Refactor an existing application into a modular, tested, maintainable architecture without changing user-facing behavior.

## Execution Harness and Environment

Expected executor:

- AI coding agent with filesystem and terminal access.

Runtime:

- Working directory: project repository root.
- Required runtimes: infer from lockfiles and README before installing anything.

Baseline harness check:

```bash
pwd
git status --short
ls
```

Fallback rules:

- If dependencies are missing, inspect the repo's README and lockfiles, then install with the existing package manager.
- If tests cannot run, record the missing dependency in `progress/validation.md` and add the smallest available static check.

## Agent Work Loop

1. Read this goal.
2. Read `progress/worklog.md`, `progress/validation.md`, and `progress/decisions.md`.
3. Run the harness readiness checks.
4. Inspect current git status and existing tests.
5. Select the smallest refactor that can be validated.
6. Implement without reverting unrelated user changes.
7. Run tests and type checks.
8. Update progress files.
9. Continue until all completion criteria are met.

## Completion Definition

Complete only when behavior is preserved, tests pass, documentation is updated, and no planned refactor milestone remains open.
