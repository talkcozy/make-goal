# Make Goal

You are using the portable `make-goal` workflow. Transform the user's complex objective into an executable `goal.md` that another AI agent can read and complete over long-running cycles.

User request:

`$ARGUMENTS`

## Instructions

1. Ask concise clarifying questions before writing when the request lacks critical context.
2. Inspect any provided files, folders, repositories, examples, or links.
3. Match the user's language. Produce bilingual English/Chinese output when requested.
4. Write a self-contained `goal.md` with:
   - objective
   - background
   - references to inspect
   - scope and assumptions
   - constraints
   - deliverables
   - milestones with acceptance criteria
   - agent work loop
   - progress tracking
   - validation plan
   - risk and blocking rules
   - quality bar
   - completion definition
5. Save `goal.md` to the requested path when a path is provided. If no path is provided, ask where to save it or provide a draft in chat.
6. Verify the file exists after writing and summarize the result.

Do not complete the underlying project unless the user explicitly asks. Your job is to create the durable goal document.

