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

## Install for Codex

Copy or symlink the Codex skill into your Codex skills directory:

```bash
mkdir -p ~/.codex/skills
ln -s "$(pwd)/packages/codex/skills/make-goal" ~/.codex/skills/make-goal
```

Or run:

```bash
bash scripts/install-codex.sh
```

Then invoke it in Codex:

```text
Use $make-goal to turn this project idea into a goal.md.
```

## Install for Claude Code

Copy the command file into a project or user-level Claude command directory:

```bash
mkdir -p .claude/commands
cp packages/claude-code/commands/make-goal.md .claude/commands/make-goal.md
```

Or run:

```bash
bash scripts/install-claude-code.sh
```

Then use:

```text
/make-goal Create a goal.md for refactoring this repo into a modular architecture.
```

中文命令模板也在：

```text
packages/claude-code/commands/make-goal.zh-CN.md
```

## Use with Any Agent

Paste one of these files into your agent's system/project instructions:

- `packages/generic-agent/make-goal.md`
- `packages/generic-agent/make-goal.zh-CN.md`

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
