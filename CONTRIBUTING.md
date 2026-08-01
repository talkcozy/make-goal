# Contributing / 贡献指南

Thanks for improving `make-goal`.

感谢你改进 `make-goal`。

## Principles

- Keep prompts and skill instructions portable across AI agents.
- Keep the Codex `SKILL.md` concise; move detailed guidance into `references/`.
- Maintain English and Chinese versions together when changing user-facing instructions.
- Prefer concrete examples over abstract theory.
- Do not make the skill domain-specific. It should work for software, writing, research, operations, design, and other long-running goals.

## Validation

Validate the Codex skill before opening a PR:

```bash
python3 -m venv /tmp/make-goal-validate
/tmp/make-goal-validate/bin/pip install PyYAML
/tmp/make-goal-validate/bin/python /path/to/skill-creator/scripts/quick_validate.py packages/codex/skills/make-goal
```

Also check for unfinished task markers:

```bash
rg "T""ODO|\\[T""ODO" .
```

## Bilingual Updates

If you change:

- `templates/goal.en.md`, update `templates/goal.zh-CN.md`.
- `packages/generic-agent/make-goal.md`, update `packages/generic-agent/make-goal.zh-CN.md`.
- `packages/claude-code/commands/make-goal.md`, update `packages/claude-code/commands/make-goal.zh-CN.md`.
