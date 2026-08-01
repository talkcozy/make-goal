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

## 让 agent 自己安装

一般不需要你先下载这个仓库。把下面对应的一段话复制给 agent，让 agent 自己读取 GitHub 仓库、安装正确的包，并验证结果。

### Codex

```text
请打开 https://github.com/talkcozy/make-goal，先阅读仓库，把 make-goal 安装到当前 Codex 环境中，验证 skill 可用，然后使用 $make-goal 帮我把当前项目整理成 goal.md。
```

### Claude Code

```text
请打开 https://github.com/talkcozy/make-goal，先阅读仓库，把 make-goal 安装到当前 Claude Code 环境中，验证 /make-goal 可用，然后用它帮我把当前项目整理成可长期执行的 goal.md。
```

### 其他 AI Agent

```text
请打开 https://github.com/talkcozy/make-goal，先阅读仓库，根据通用 agent 指令适配当前环境，验证我应该如何调用 make-goal，然后用它帮我把当前项目整理成 goal.md。
```

`scripts/` 下的辅助脚本仍然保留，适合已经在 clone 后仓库里的 agent 或高级用户使用，但它不再是默认入口。

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
