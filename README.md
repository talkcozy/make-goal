<p align="right">
  <strong>Language:</strong>
  <a href="./README.md">English</a> |
  <a href="./README.zh-CN.md">简体中文</a>
</p>

# make-goal

**make-goal** turns an ambiguous or complex objective into an executable `goal.md` that AI agents can read, execute, validate, and continue across long-running sessions.

**make-goal** 可以把一个复杂目标整理成可执行的 `goal.md`，让 Codex、Claude Code 或其他 AI agent 能够读取、拆解、验证、记录进度，并长期循环完成任务。

**你必须非常努力，才会看起来毫不费力。** `make-goal` puts the effort up front so future agents can run the goal smoothly later.

Website: [talkcozy.github.io/make-goal](https://talkcozy.github.io/make-goal/)

## Why

Most long AI tasks fail because the "plan" lives in chat history. `make-goal` moves the important context into a durable file:

- final objective
- background and references
- constraints and assumptions
- execution harness: runtime, tools, dependencies, permissions, secrets, services, readiness checks, fallbacks
- milestones with acceptance criteria
- repeatable agent work loop
- validation plan
- progress logs
- blocking rules
- completion definition

很多长任务失败，是因为计划只存在于对话历史里。`make-goal` 的目标是把关键上下文沉淀到一个可复用、可恢复、可验证的 `goal.md`。

## Repository Layout

```text
make-goal/
  packages/
    codex/skills/make-goal/        # Codex skill package
    claude-code/commands/          # Claude Code slash command prompts
    generic-agent/                 # Portable prompts for other agents
  templates/
    goal.en.md
    goal.zh-CN.md
  docs/
    goal-md-spec.md
  examples/
```

## Install with Your Agent

You usually do not need to clone this repository yourself. Copy the matching prompt into the agent that should use `make-goal`, and let the agent read the repository, install the right package, and verify the result.

### Codex

```text
Open https://github.com/talkcozy/make-goal. Read the repo, install make-goal for this Codex environment, verify the skill is available, then use $make-goal to create a goal.md for this project.
```

### Claude Code

```text
Open https://github.com/talkcozy/make-goal. Read the repo, install make-goal for this Claude Code environment, verify /make-goal is available, then use it to create a goal.md for this project.
```

### Any Agent

```text
Open https://github.com/talkcozy/make-goal. Read the repo, adapt the generic agent instructions for this environment, verify how I should invoke make-goal, then use it to create a goal.md for this project.
```

The helper scripts under `scripts/` still exist for agents or users already working from a cloned checkout, but they are not the primary onboarding path.

## What the Skill Should Ask

Before writing `goal.md`, the agent should ask for missing critical context:

- What is the final outcome?
- Where should `goal.md` be saved?
- What existing files, repos, examples, or links should be inspected?
- Which agent or humans will execute it?
- What runtime, tools, package managers, plugins, credentials, services, and permissions will the agent need?
- What should the agent do if a required harness piece is missing?
- What constraints matter?
- What counts as done?
- How should work be validated?
- How should progress be recorded?
- How autonomous should the future agent be?

## License

MIT
