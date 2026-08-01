# Make Goal Questionnaire / Make Goal 提问清单

Use this when the user's objective is underspecified. Ask the smallest useful subset. Do not interrogate the user mechanically.

当用户目标不够清晰时使用本清单。只问真正有帮助的问题，不要机械地全部提问。

## Core Questions

1. What is the final outcome?
   - What should exist when the work is complete?
   - 完成后应该产出什么？

2. Where should the goal live?
   - Should I create `goal.md` in a folder, repo, workspace, or only draft it in chat?
   - `goal.md` 应该写到哪个目录/仓库，还是只在对话中草拟？

3. What context should future agents inspect?
   - Repos, files, folders, docs, tickets, screenshots, links, examples, prototypes, prior attempts.
   - 后续 agent 需要参考哪些仓库、文件、目录、文档、截图、链接、示例或旧方案？

4. Who or what will execute the goal?
   - Codex, Claude Code, another coding agent, a research agent, humans, or mixed.
   - 执行者是 Codex、Claude Code、其他 AI agent、人类，还是混合协作？

5. What constraints matter?
   - Tech stack, style, platform, budget, deadline, safety, data privacy, deployment, licensing.
   - 有哪些技术栈、风格、平台、预算、时间、安全、隐私、部署或许可约束？

6. What counts as done?
   - Tests passing, artifact created, user review, deployment, benchmarks, screenshots, docs.
   - 什么状态才算完成？测试、交付物、评审、部署、性能、截图、文档？

7. How should progress be recorded?
   - Worklog files, status docs, commits, issues, checklists, validation reports.
   - 进度应该记录在哪里？工作日志、状态文档、提交、issue、清单、验证报告？

8. How autonomous should the agent be?
   - Continue automatically, stop at milestones, ask before destructive/risky actions, or ask before spending money.
   - agent 应该自动持续推进、阶段暂停，还是遇到危险操作/花钱/外部发布前必须询问？

## Useful Follow-Ups

- Are there examples of "good" output or "bad" output?
- Should the goal prefer speed, quality, cost control, safety, or maintainability?
- Should the goal be bilingual?
- Should the agent create tests before implementation?
- Should the agent commit or push changes?
- Are there secrets, credentials, private data, or production systems to avoid?
- Should the agent use specific tools, plugins, MCP servers, CLIs, or apps?

## Question Strategy

- If the user already provided a path and objective, do not ask where to write the file.
- If references are local files, inspect them before asking questions that the files answer.
- If the user wants rapid progress, ask fewer questions and document assumptions.
- If the work may affect production, money, legal obligations, personal data, or irreversible state, ask explicit safety questions.
