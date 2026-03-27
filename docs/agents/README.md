# Agents README

This file is the repository-canonical guide for agent-driven work in LiteLLM.

## Primary Sources

- `AGENTS.md` remains the broad repository instruction file.
- `docs/engineering/acceptance-criteria.md` defines when a task is actually done.
- `docs/engineering/harness-engineering.md` defines the canonical verification commands.
- `docs/workflow/one-day-delivery-plan.md` and `docs/workflow/pr-continuity.md` define branch and PR handling.

## Working Rules

- Use the narrowest existing tests for issue-scoped fixes before running broader suites.
- Keep branch-specific CI unblockers separate from the main functional fix when possible.
- Reuse the existing branch and canonical PR for the task instead of creating duplicates.
- Treat AI review findings as actionable inputs to resolve or explicitly defer in the PR conversation.
