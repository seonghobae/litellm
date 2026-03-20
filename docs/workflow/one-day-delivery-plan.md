# One-Day Delivery Plan

This file defines the repository-canonical flow for a focused one-issue LiteLLM delivery.

## Flow

1. Confirm the canonical task from the user message, current branch, linked issue, and existing PR state.
2. Reproduce the failure with a narrow regression test or CI-visible reproduction.
3. Implement the minimal fix that follows existing LiteLLM patterns.
4. Run the focused verification suite locally.
5. Push the branch, update the fork PR body, and request AI review if available.
6. Keep fixing branch-specific CI until the canonical fork PR is healthy.
7. Open the upstream PR only after the fork PR is ready for maintainer review.

## Branch Rules

- Prefer one issue-scoped branch per canonical task, such as `fix-23959-azure-surrogate-local`.
- Keep issue-fixing commits and branch-only test harness cleanup in separate commits when both are needed.
- Reuse the same branch and PR instead of opening duplicates for the same issue.

## Current Canonical Task

- Canonical issue: `BerriAI/litellm#23959`
- Active fork PR: `seonghobae/litellm#1`
- Upstream PR: none yet
- Required upstream promotion condition: branch PR evidence is ready and branch CI is healthy enough for maintainer review.
