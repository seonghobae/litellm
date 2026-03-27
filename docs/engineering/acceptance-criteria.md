# Engineering Acceptance Criteria

This file is the repository-canonical completion checklist for focused engineering work.

## General

- A task is not done until code, focused tests, PR state, and linked issue state agree on the same outcome.
- Follow existing LiteLLM patterns in `litellm/`, `tests/`, `.github/pull_request_template.md`, `AGENTS.md`, and `CLAUDE.md` instead of inventing a new delivery flow.
- Keep issue-scoped fixes isolated. Unrelated cleanup stays out of the canonical PR unless it is required to unblock CI for that same branch.
- New behavior must preserve backward compatibility unless the linked issue or PR explicitly calls for a breaking change.

## Bug Fixes

- Reproduce the reported failure with a focused regression test or equivalent CI-visible reproduction before changing production code.
- Fix the root cause, not only the downstream symptom. If retries, fallbacks, or logging amplify the error, the original invalid input path still needs to fail fast.
- For provider plus proxy bugs, verify both the provider-side path and the proxy ingress path when user input can reach both.
- If malformed input should be rejected, return a user-facing validation error before transport dispatch whenever the code path allows it.

## Tests

- Add at least one test in `tests/test_litellm/` or the most specific existing test suite covering the changed behavior.
- Keep the minimal focused verification command in the PR description and issue notes when the full repo suite is too large for quick iteration.
- Run the targeted regression suite after each functional change and before creating or updating a PR.
- If branch CI fails for a reason directly connected to the branch, fix that branch-level failure before opening or promoting the upstream PR.

## PR And Issue State

- Every fix branch must link to its canonical upstream issue in the PR body using `Fixes BerriAI/litellm#<issue>` when applicable.
- The active PR must follow `.github/pull_request_template.md` and record the latest branch CI links and the current targeted verification evidence.
- Resolve or explicitly answer AI review findings that question correctness, missing coverage, or unintended scope changes.
- The linked upstream issue stays open until the canonical upstream PR exists or the fix is otherwise merged upstream.

## Current Canonical Example

- Issue `BerriAI/litellm#23959` is complete only when lone surrogate Unicode is rejected before Azure transport, proxy parsing rejects escaped lone surrogates, retry/fallback does not loop on the malformed request, branch CI is green, and an upstream PR exists.
