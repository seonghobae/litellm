# Harness Engineering

This file records the repository-canonical verification commands for focused engineering work.

## Baseline Commands

- Full unit baseline: `make test-unit`
- Fast lint baseline: `poetry run ruff check .`
- Python script execution: `poetry run python <script>.py`
- Proxy startup smoke: `poetry run litellm --config dev_config.yaml --port 4000`

## Environment Notes

- Some suites require extra local packages noted in `AGENTS.md`, including `psycopg-binary` and `openapi-core`.
- The proxy boot path may need PostgreSQL or the default embedded Neon setup from `litellm-proxy-extras`.
- CI is the final source of truth for broad suites when local environments are incomplete, but local targeted regressions should still run before PR updates.

## Focused Verification For Issue 23959

- Azure regression: `poetry run pytest tests/test_litellm/llms/azure/test_azure_exception_mapping.py -k surrogate -v`
- Proxy parsing regression: `poetry run pytest tests/test_litellm/proxy/common_utils/test_http_parsing_utils.py -k surrogate -v`
- Router retry regression: `poetry run pytest tests/test_litellm/test_router_retry_non_retryable_errors.py -k surrogate -v`
- Combined focused suite: `poetry run pytest tests/test_litellm/llms/azure/test_azure_exception_mapping.py tests/test_litellm/proxy/common_utils/test_http_parsing_utils.py tests/test_litellm/test_router_retry_non_retryable_errors.py -v`

## Branch CI Handling

- If a focused branch fails fork CI because of tests loaded from the same branch, fix the branch-level failure before opening the upstream PR.
- Record the latest actionable workflow URL in the PR body after each rerun so reviewers can follow the canonical branch evidence.
