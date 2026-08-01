# goal.md Structure / goal.md 结构规范

Use this as the default structure for a high-quality executable goal document. Adapt headings to the task domain.

以下是高质量可执行 `goal.md` 的默认结构。根据任务领域调整标题，不要生搬硬套。

## Required Sections

1. Title
   - Name the objective clearly.
   - 清楚命名目标。

2. Objective
   - Describe the final outcome, not just the next step.
   - 描述最终结果，而不只是下一步。

3. Background and Context
   - Include why this matters, existing materials, prior decisions, and relevant paths/links.
   - 写明背景、已有资料、既定决策、相关路径和链接。

4. Scope
   - In scope, out of scope, and assumptions.
   - 包含范围、排除范围和假设。

5. Target Users or Consumers
   - Who uses the result and what quality bar they expect.
   - 谁会使用结果，以及他们期待什么质量。

6. Constraints
   - Tools, platforms, stack, style, budget, deadlines, safety, privacy, licensing.
   - 工具、平台、技术栈、风格、预算、时间、安全、隐私、许可等。

7. Execution Harness and Environment
   - Expected executor, runtime, tools, dependency setup, permissions, secrets, services, baseline checks, and fallbacks.
   - 执行者、运行环境、工具、依赖安装、权限、密钥、外部服务、基线检查和降级方案。

8. Deliverables
   - Files, features, reports, deployments, docs, tests, examples.
   - 文件、功能、报告、部署、文档、测试、示例等。

9. Milestones or Phases
   - Break work into verifiable stages. Each stage must include acceptance criteria.
   - 把工作拆成可验证阶段。每个阶段必须有验收标准。

10. Work Loop for Agents
    - Tell agents how to check harness readiness, resume, choose work, implement, verify, log progress, and continue.
    - 告诉 agent 如何检查环境就绪、恢复上下文、选择任务、实现、验证、记录进度并继续。

11. Validation Plan
    - Commands, checks, reviews, screenshots, benchmarks, manual QA, source citations, or artifact inspections.
    - 命令、检查、评审、截图、基准测试、人工 QA、引用来源或产物检查。

12. Progress Tracking
    - Worklog, decisions, validation logs, checklists, status file locations.
    - 工作日志、决策记录、验证记录、清单和状态文件位置。

13. Risk and Blocking Rules
    - What to do when missing access, tests fail, requirements conflict, or destructive actions are needed.
    - 遇到缺少权限、测试失败、需求冲突或危险操作时怎么处理。

14. Quality Bar
    - Maintainability, user experience, correctness, performance, security, documentation.
    - 可维护性、用户体验、正确性、性能、安全、文档标准。

15. Completion Definition
    - The exact conditions under which the goal is complete.
    - 明确什么条件下才算完成。

## Optional Sections

- Repository or workspace map
- Data model or architecture
- Design direction
- Release or deployment plan
- Testing matrix
- Rollback plan
- Open questions
- Glossary
- Examples
- Non-goals

## Agent Work Loop Pattern

Use this pattern in most software and artifact-building goals:

```text
Each work cycle:
1. Read goal.md.
2. Read progress files.
3. Inspect current state.
4. Run harness readiness checks and bootstrap missing required dependencies when documented.
5. Run quick validation to establish baseline.
6. Select the highest-priority unfinished task.
7. Implement a small verifiable increment.
8. Run relevant validation.
9. Fix failures introduced by the increment.
10. Update worklog, decisions, validation records, and harness notes when environment state changed.
11. Continue if budget remains and no blocking condition exists.
```

## Anti-Patterns

- A goal that only says "build X" without validation.
- A goal that depends on conversation context not written into the file.
- A goal that has milestones but no acceptance criteria.
- A goal that tells agents to continue forever with no completion definition.
- A goal that lets agents overwrite unrelated user changes.
- A goal that omits where progress should be recorded.
- A goal that assumes tools, secrets, browsers, services, or network access without a harness readiness plan.
