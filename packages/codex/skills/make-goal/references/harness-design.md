# Execution Harness Design / 执行环境设计

Many long-running agent goals fail even when the objective is clear because the executing agent lacks the right environment, tools, permissions, credentials, or fallback rules. Every serious `goal.md` should include an execution harness section.

很多长任务目标本身写得很清楚，但 agent 执行时缺少环境、工具、权限、密钥或降级规则，最后停住或做差。严肃的 `goal.md` 应包含执行环境设计。

## Required Harness Content

Include these when relevant:

1. Runtime environment
   - OS assumptions, shell, working directory, language runtimes, browser availability, GPU/CPU needs.
   - 操作系统、shell、工作目录、语言运行时、浏览器、GPU/CPU 等要求。

2. Tooling
   - CLIs, package managers, build tools, test tools, linters, formatters, IDE-only steps, MCP servers, plugins.
   - CLI、包管理器、构建工具、测试工具、lint/format 工具、IDE 步骤、MCP、插件等。

3. Dependency bootstrap
   - Exact install commands, cache expectations, lockfile policy, version checks, offline fallback.
   - 安装命令、缓存预期、lockfile 策略、版本检查、离线降级。

4. Permissions and sandbox
   - Filesystem scope, network access, approval rules, destructive commands, deploy/publish restrictions.
   - 文件系统范围、网络访问、审批规则、危险命令、部署/发布限制。

5. Secrets and external services
   - Required env vars, API keys, OAuth, cloud resources, databases, test accounts. Never write secret values into `goal.md`; write variable names and how to verify presence.
   - 所需环境变量、API key、OAuth、云资源、数据库、测试账号。不要把密钥值写进 `goal.md`，只写变量名和验证方式。

6. Baseline checks
   - Commands that prove the harness is ready before main work begins.
   - 开始主要工作前证明环境就绪的命令。

7. Fallbacks
   - What to do when a tool is missing, network is unavailable, credentials are absent, tests cannot run, or local services fail.
   - 工具缺失、网络不可用、无密钥、测试无法运行、本地服务失败时怎么处理。

8. Harness progress logging
   - Where to record environment status, setup failures, skipped checks, and assumptions.
   - 环境状态、安装失败、跳过验证、假设记录在哪里。

## Harness Section Template

```markdown
## Execution Harness and Environment

Expected executor:

- {{Codex / Claude Code / generic agent / human + agent}}

Runtime:

- OS/shell: {{expected}}
- Working directory: `{{path}}`
- Required runtimes: {{Node/Python/Go/etc. with versions}}

Required tools:

- {{tool}}: {{why needed}}; verify with `{{command}}`

Dependency setup:

```bash
{{install commands}}
```

Secrets and services:

- `{{ENV_VAR}}`: {{purpose}}; verify presence only, never print value.

Permissions:

- Allowed: {{actions}}
- Ask before: {{risky actions}}
- Forbidden: {{actions}}

Baseline harness check:

```bash
{{commands}}
```

Fallback rules:

- If {{tool}} is missing, {{fallback}}.
- If {{credential}} is missing, continue with {{offline/local/mock mode}} and record the limitation.
- If validation cannot run, record why in `{{progress/validation.md}}` and add the smallest replacement check.
```

## Harness Work Loop Addition

Add this near the start of the agent work loop:

```text
Before selecting feature work, run the harness readiness checks. If the environment is incomplete, first try the documented bootstrap steps. If setup fails, record the exact missing dependency and either use the documented fallback or continue with independent work.
```

## Anti-Patterns

- Saying "run tests" without saying how dependencies are installed.
- Requiring a cloud service without naming the env vars or test account needs.
- Assuming network or browser access without recording it.
- Letting agents stop permanently when one optional tool is missing.
- Printing or committing secret values.
- Treating an unverified environment as ready.
