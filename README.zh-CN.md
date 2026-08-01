# make-goal

**make-goal** 是一个通用 AI agent skill，用来把复杂目标整理成可执行的 `goal.md`。

它不是针对某一个项目的专用 prompt，而是一套通用工作流：先向用户提问补齐上下文，再把目标、约束、里程碑、验证方式、进度记录和阻塞规则写进一个持久化文件，让其他 AI agent 可以进入 goal 模式长期执行。

**你必须非常努力，才会看起来毫不费力。** `make-goal` 的努力发生在目标整理阶段，之后 agent 执行 goal 才会顺滑、稳定、像是毫不费力。

官网：[talkcozy.github.io/make-goal](https://talkcozy.github.io/make-goal/)

## 适用场景

- 重构软件项目
- 创建开源库
- 搭建产品 MVP
- 写书或整理长文档
- 做研究报告
- 迁移系统
- 清理知识库
- 长期运营项目

## 目录

```text
make-goal/
  packages/
    codex/skills/make-goal/        # Codex skill
    claude-code/commands/          # Claude Code slash command
    generic-agent/                 # 其他 agent 可复制的通用指令
  templates/
    goal.en.md
    goal.zh-CN.md
  docs/
    goal-md-spec.md
```

## Codex 安装

```bash
mkdir -p ~/.codex/skills
ln -s "$(pwd)/packages/codex/skills/make-goal" ~/.codex/skills/make-goal
```

使用方式：

```text
Use $make-goal 帮我把这个长期项目整理成 goal.md。
```

## Claude Code 安装

```bash
mkdir -p .claude/commands
cp packages/claude-code/commands/make-goal.md .claude/commands/make-goal.md
```

使用方式：

```text
/make-goal 帮我把这个项目整理成可长期执行的 goal.md。
```

## 其他 AI Agent

把下面任意一个文件复制到 agent 的项目指令或系统指令中：

- `packages/generic-agent/make-goal.md`
- `packages/generic-agent/make-goal.zh-CN.md`

## 核心原则

生成的 `goal.md` 必须：

- 自包含
- 可执行
- 可验证
- 可长期恢复
- 明确执行 harness：运行环境、工具、依赖、权限、密钥、外部服务、就绪检查和降级方案
- 明确完成定义
- 明确 agent 工作循环
- 明确进度记录方式
- 明确风险和阻塞处理

## 许可证

MIT
