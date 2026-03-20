# CodeRabbit Review Commands

This file records the repository-canonical CodeRabbit commands used in LiteLLM PRs.

## Commands

- `@coderabbitai review` - request or resume review on the active PR.
- `@coderabbitai full review` - request a fresh whole-PR review when incremental review is not enough.
- `@coderabbitai pause` - pause automatic review on a noisy PR.
- `@coderabbitai resume` - resume automatic review after a pause.

## Repo Usage Notes

- Put commands in PR comments, not commit messages.
- Re-run `@coderabbitai review` after meaningful follow-up commits on the same PR.
- Answer or resolve CodeRabbit findings that affect correctness, coverage, or PR scope before promoting the branch upstream.
- Keep the PR body in sync with the current CI links and canonical issue while review is active.
