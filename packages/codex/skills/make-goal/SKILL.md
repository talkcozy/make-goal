---
name: make-goal
description: Create high-quality executable goal.md files for long-running AI agent work. Use when a user wants to turn a complex idea, project, refactor, research effort, product build, migration, writing task, or open-ended objective into a self-contained goal document that other AI agents can read, execute in goal mode, validate, and continue over many cycles. Trigger when the user says make goal, create goal.md, goal mode, long task plan for agents, or asks to prepare instructions for Codex, Claude Code, or other AI coding/work agents.
---

# Make Goal

## Purpose

Turn an ambiguous or complex user objective into an executable `goal.md`: a durable task contract that an AI agent can read, decompose, implement, verify, document, and continue across long-running sessions.

This skill creates the goal document. It does not itself complete the user's underlying project unless explicitly asked after `goal.md` is created.

## Workflow

1. Clarify the objective before writing. Ask concise questions when critical context is missing.
2. Inspect any files, folders, repos, examples, or links the user provides.
3. Decide the goal document language: match the user by default; produce bilingual English/Chinese when requested or when the target agents/users are multilingual.
4. Write a self-contained `goal.md` with enough context for a fresh agent to continue without the conversation.
5. Include an execution harness: required runtime, tools, permissions, dependency setup, credentials, external services, validation commands, and fallbacks.
6. Include an execution loop, validation commands, progress logs, completion definition, and blocking rules.
7. Save the file to the user-specified path when provided. If no path is provided, ask for one or draft inline.
8. Verify that the file exists and briefly summarize what was created.

## Clarifying Questions

Ask only what materially improves the goal. For small requests, 3-5 questions are enough. For high-stakes or long-running work, ask up to 8.

Always try to learn:

- Final outcome: What should exist when the work is done?
- Output location: Where should `goal.md` and resulting work live?
- Existing context: What repos, files, docs, links, examples, or prior attempts should agents inspect?
- Target executor: Codex, Claude Code, another AI agent, humans, or mixed?
- Harness and environment: What OS, runtime, tools, package managers, services, credentials, permissions, or plugins must be available?
- Constraints: Tech stack, tools, platform, style, legal/security limits, budget, timeline.
- Definition of done: How should agents know the objective is complete?
- Validation: What commands, tests, reviews, screenshots, metrics, or acceptance checks are required?
- Autonomy: Should agents keep going automatically, ask before risky changes, or stop at milestones?

If the user says to proceed without questions, infer responsibly and write assumptions into `goal.md`.

For a fuller questionnaire, read `references/questionnaire.md`.

## Required goal.md Qualities

A good `goal.md` must be:

- Self-contained: include enough background, paths, constraints, and assumptions for a new agent.
- Executable: describe concrete steps and phases, not just aspirations.
- Verifiable: every major phase has acceptance checks.
- Persistent: define progress files or status records for future sessions.
- Harness-aware: define how agents check and bootstrap the environment before doing the main work.
- Agent-safe: include non-destructive rules, user-change preservation, and blocking behavior.
- Domain-neutral: fit the user's task instead of forcing a software-project shape when the task is research, writing, operations, data work, or design.
- Iterative: tell agents how to choose the next task, implement, verify, record, and continue.

For the canonical section structure, read `references/goal-md-structure.md`.

For environment and harness design details, read `references/harness-design.md`.

## Output Patterns

Use these patterns depending on the request:

- **Create file**: write `goal.md` at the requested path and verify it.
- **Draft only**: provide the goal document in chat when no filesystem output is wanted.
- **Bilingual**: include paired English/Chinese headings or create `goal.md` plus `goal.zh-CN.md` / `goal.en.md` if the user requests separate files.
- **Cross-agent package**: include instructions for Codex, Claude Code, and generic agents when the user wants portability.

Bundled templates:

- `templates/goal.en.md`
- `templates/goal.zh-CN.md`

These live at the repository root when using the open-source package. If unavailable, recreate the structure from `references/goal-md-structure.md`.

## Writing Rules

- Use clear imperative instructions for future agents.
- Prefer concrete paths, commands, artifacts, and acceptance criteria.
- Put assumptions in a dedicated section.
- Include a "do not" section for risky behaviors.
- Include a "harness" or "environment readiness" section before the work loop.
- Include a "work loop" section that tells agents to read progress, inspect state, pick the next task, implement, verify, update logs, and continue.
- Include "blocked handling" so agents do not spin forever on missing access or impossible constraints.
- Include "completion definition" that is stricter than "the plan exists".
- Keep the document practical; avoid motivational filler.

## Validation

After creating or editing a Codex skill package, validate the skill folder with:

```bash
python3 /Users/orange/.codex/skills/.system/skill-creator/scripts/quick_validate.py <path-to-skill-folder>
```

For ordinary `goal.md` outputs, verify:

- The file exists at the requested path.
- It names the final objective.
- It includes execution harness, execution loop, phases, validation, progress logging, blocking rules, and completion definition.
- It references all provided input files or explicitly states why they were not used.
