# 小红书发布资料：make-goal

## 推荐标题

把复杂需求交给 AI 前，我会先做这一步

## 备选标题

- 别急着让 AI 开工，先让它写 goal.md
- 长任务总烂尾？可能缺的不是 prompt
- 我做了一个让 AI 跑长期任务的开源 skill

## 简介

很多 AI 长任务失败，不是因为目标不清楚，而是环境、验证、进度和阻塞处理没有写进一个稳定文件。`make-goal` 会先把复杂目标整理成可执行的 `goal.md`，再让 Codex、Claude Code 或其他 agent 长时间推进。

核心理念：你必须非常努力，才会看起来毫不费力。

项目地址：https://github.com/talkcozy/make-goal

## 成品图片

发布顺序：封面图 + 5 张正文竖图。

- `images/cover.jpg`
- `images/slide-01.jpg`
- `images/slide-02.jpg`
- `images/slide-03.jpg`
- `images/slide-04.jpg`
- `images/slide-05.jpg`

## 话题标签

#AI工具 #AIAgent #Codex #ClaudeCode #开源项目 #效率工具 #程序员 #项目管理 #PromptEngineering

## 图片规划

### Cover

主标题：复杂需求别直接丢给 AI

副标题：先生成一个能长期执行、可恢复、可验证的 goal.md

角标：make-goal

信息点：

- Context：目标、背景、资料、边界
- Harness：运行环境、工具、权限、fallback
- Validation：里程碑、验收、进度恢复

### 01

标题：长任务为什么会烂尾？

信息结构：表现 -> 结果

- 计划在聊天里 -> 换会话后上下文断片
- 依赖靠口头说 -> 缺工具时直接卡住
- 验收没写清 -> 做完也不知道对不对
- 进度没记录 -> 下一轮重复摸索

结论：长期任务需要可执行上下文，而不是一次性 plan。

### 02

标题：goal.md 不是待办清单

信息点：

- 目标：最终交付物、成功标准
- 边界：明确不做什么，避免漂移
- 上下文：必须阅读的仓库、文件、链接
- 里程碑：阶段任务和验收口径
- 验证：测试、截图、命令、人工检查
- 恢复：进度记录、阻塞规则、下一步

结构公式：goal.md = 目标 + 上下文 + Harness + 里程碑 + 验证 + 进度记录

### 03

标题：Harness：别让环境拖垮 Agent

信息点：

- 运行层：runtime、package manager、CLI 工具
- 连接层：API keys、MCP / 插件、本地服务
- 保障层：readiness checks、权限、fallback

结论：把 harness 写进 goal.md，agent 才能先检查、再执行、缺什么补什么。

### 04

标题：正确交给 Agent 的方式

信息点：

- 给 agent 一段提示词，而不是让用户手动下载仓库
- agent 自动完成：读仓库、安装、验证、生成 goal.md
- 图中包含可直接复制的英文提示词

### 05

标题：适合这些长期任务

信息点：

- 软件重构：多目录、多风险、要回归
- 产品 MVP：功能拆解、验收、迭代
- 研究报告：资料、假设、引用来源
- 游戏开发：玩法、资源、手感验证
- 文档迁移：结构、缺口、一致性
- 知识库清理：分类、去重、命名标准

结论：任务越长、环境越复杂，越要先做 goal.md。
