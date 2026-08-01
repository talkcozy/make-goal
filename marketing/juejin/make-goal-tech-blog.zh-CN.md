# make-goal：把长期 AI 任务从聊天记录里解放出来

> 适合发布平台：稀土掘金
> 建议标签：AI Agent、Codex、Claude Code、工程效率、开源

## 摘要

很多 AI agent 的短任务表现很好，但一旦任务变成长周期项目，质量就容易开始漂移：计划散落在聊天记录里，环境依赖没有写清楚，验证方式靠临时记忆，下一轮 agent 接手时又要重新理解上下文。

`make-goal` 想解决的不是“让 AI 写一个更漂亮的计划”，而是把复杂目标整理成一个可执行、可恢复、可验证的 `goal.md`。它把目标、约束、运行环境、里程碑、验收标准和进度记录放进同一个文件，让 Codex、Claude Code 或其他 agent 可以直接进入长期执行模式。

**你必须非常努力，才会看起来毫不费力。** `make-goal` 的努力发生在目标整理阶段。前面多问清楚一点，后面交给 agent 跑起来才会顺。

## 长任务真正缺的不是计划，而是可执行上下文

我们通常会这样使用 AI agent：

1. 在聊天里描述一个目标
2. 让 agent 给出计划
3. 让它开始修改代码或整理资料
4. 中途不断补充上下文
5. 下一次会话重新解释一遍

这个流程在十分钟内有效，但对几小时、几天甚至更长的任务并不可靠。原因不是 agent 不会拆任务，而是“任务状态”没有变成稳定资产。

聊天记录的问题是：

- 上下文太长，后续 agent 不一定能完整读取
- 用户的口头约束很容易被遗漏
- 环境依赖经常只存在于某一轮对话里
- 验证方式不明确，完成标准会越来越模糊
- 进度没有结构化记录，恢复成本很高

所以 `make-goal` 的核心判断是：长期任务需要的不是一次性 plan，而是一份可以被 agent 反复读取和执行的目标合约。

## goal.md 应该包含什么

一个好的 `goal.md` 至少要回答这些问题：

- 最终要交付什么
- 哪些文件、仓库、链接或参考资料必须先读
- 哪些约束不能破坏
- 哪些事情明确不做
- 当前运行环境需要什么
- 缺少依赖时 agent 应该怎么办
- 如何分阶段推进
- 每个阶段怎样验收
- 每次循环之后如何记录进度
- 什么条件下可以认为任务完成

`make-goal` 会引导 agent 先问问题，再生成文档。它不会急着写任务清单，而是先把缺失信息补齐，尤其是执行环境这一层。

## Harness：长期任务最容易被低估的一层

很多任务目标本身很清楚，但 agent 仍然会卡住，常见原因是 harness 没设计好。

这里的 harness 指的是 agent 真正执行任务时需要依赖的一切：

- runtime，比如 Node、Python、Godot、LayaAir、浏览器
- package manager，比如 npm、pnpm、uv、pip
- CLI 工具，比如 gh、git、ffmpeg、Playwright
- MCP server、插件或外部连接器
- 环境变量和密钥名称
- 本地服务、数据库、第三方 API
- 文件系统权限和网络权限
- 基线检查命令
- 依赖缺失时的降级方案

如果这些没有写进 `goal.md`，后续 agent 就会靠猜。它可能猜对，也可能在环境缺失时直接停下，或者用一个错误的替代方案继续推进。

因此 `make-goal` 在目标整理阶段会明确要求写出 harness：

```md
## Execution Harness

- Runtime:
- Package manager:
- Required CLI tools:
- Required services:
- Environment variables:
- Permissions:
- Readiness checks:
- Fallbacks:
```

这部分看起来不如“功能列表”兴奋，但它决定了任务能不能长期自动跑下去。

## Agent 工作循环

`make-goal` 生成的 `goal.md` 不只是给人看的文档，它还会定义 agent 的工作循环：

```text
Read goal.md
Read progress log
Inspect current repo state
Pick the next smallest useful increment
Implement
Validate
Record progress
Continue
```

这个循环有两个好处。

第一，它减少漂移。agent 每一轮都回到同一个目标文件，而不是依赖当前聊天上下文。

第二，它方便恢复。如果任务中断，下一个 agent 可以先读 `goal.md` 和 progress log，再继续从当前状态推进。

## 为什么做成通用 skill

`make-goal` 不是为某一个项目写的 prompt，而是一个通用 skill。

它可以用于：

- 软件重构
- 开源项目初始化
- 产品 MVP
- 研究报告
- 文档迁移
- 游戏开发
- 知识库清理
- 长期运营任务

它也不绑定单一 agent。当前仓库提供了三类入口：

- Codex skill package
- Claude Code slash command
- Generic agent prompt

更重要的是，用户不需要先下载仓库再手动跑安装脚本。更自然的入口是一段给 agent 的提示词：

```text
Open https://github.com/talkcozy/make-goal. Read the repo, install make-goal for this Codex environment, verify the skill is available, then use $make-goal to create a goal.md for this project.
```

也就是说，安装这件事本身也可以交给 agent 去完成。用户只需要表达意图，agent 负责读仓库、安装、验证和使用。

## 一个 goal.md 的质量标准

我认为一个合格的 `goal.md` 至少要满足这些标准：

- 自包含：脱离原始聊天记录也能理解
- 可执行：下一步做什么足够明确
- 可验证：每个阶段有检查方式
- 可恢复：中断后能继续
- 有边界：写清楚不做什么
- 有 harness：环境依赖和缺失处理写清楚
- 有进度记录：每轮工作能留下状态
- 有完成定义：知道什么时候该停

如果只有任务清单，它只是 plan。如果包含了上下文、harness、循环和验收标准，它才更接近长期任务合约。

## 适合在什么时候使用

当你的需求可以在一次对话里完成时，不一定需要 `make-goal`。

但如果出现以下情况，就很适合先生成 `goal.md`：

- 任务会持续很久
- 涉及多个目录或多个仓库
- 需要反复验证
- 中途可能换 agent 或换会话
- 环境依赖比较复杂
- 用户希望 agent 尽量自主推进
- 完成标准不止一个截图或一个函数

换句话说，`make-goal` 适合那些“开始写代码之前值得认真想清楚”的任务。

## 结语

AI agent 越强，越需要清晰的执行边界。

好的 `goal.md` 不是在束缚 agent，而是在给它一个可以长期工作的地基。目标越复杂，前置整理越重要。

`make-goal` 的核心理念可以浓缩成一句话：

> 你必须非常努力，才会看起来毫不费力。

项目地址：

```text
https://github.com/talkcozy/make-goal
```

官网：

```text
https://talkcozy.github.io/make-goal/
```
