# PR Continuity

This file defines the repository-canonical PR continuity rules for the current contribution flow.

## Canonical PR Selection

- Prefer the existing PR for the current branch over opening a new PR from the same head.
- For fork-based work, the fork PR is canonical until an upstream PR is opened from the same branch head.
- Always link the fork PR back to the upstream issue, not only to the fork repository.

## Current Branch State

- Branch: `fix-23959-azure-surrogate-local`
- Canonical fork PR: `https://github.com/seonghobae/litellm/pull/1`
- Canonical upstream issue: `https://github.com/BerriAI/litellm/issues/23959`
- Upstream PR status: none yet

## Promotion Rules

- Update the existing fork PR body and checks instead of replacing it.
- Open the upstream PR only after the fork PR state is coherent: linked issue, current CI links, latest commit pushed, and review findings addressed or answered.
- Do not open a second upstream PR for the same branch head unless the first one is closed or superseded with explicit continuity notes.
