# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [0.2.0] - 2026-02-19

### Added

- `fastn agent` command: AI-powered agentic tool execution with native function calling
  - OpenAI function-calling integration with automatic tool discovery
  - Prompt-based tool routing via `getTools(prompt, limit)` — sends only top-N tools to LLM
  - Configurable tool limit (`--max-tools`, default 5) to reduce hallucination
  - Benchmark summary table with token counts, cost estimation ($), and timing
  - Error recovery with consecutive error tracking (`--max-errors`, default 2)
  - Evaluation mode (`--eval`) — LLM judge assesses if agent called correct tools
  - Confirmation gates for tool calls (default on, `-y` to skip)
  - LLM diagnosis on persistent failures with debug context dump
  - Schema unwrapping for LLM consumption, re-wrapping for API execution
- `fastn run` command for direct tool execution from CLI
  - Interactive parameter prompting when no args provided
  - Inline parameters via `--key value`
  - Tenant ID as positional argument: `fastn run slack send_message <tenant_id>`
- `--tenant` option on `fastn run` and `fastn agent` for multi-tenant testing
- `fastn list --active` to show only enabled tools in workspace and org
- Generic error detection (`_detect_api_error`) for diverse API response formats
  - Handles Slack, GitHub, Stripe, GraphQL, generic REST, HTTP status codes in body
  - Preserves original error messages for LLM diagnosis
- Interactive LLM provider setup (OpenAI, Anthropic, Gemini) on first `fastn agent` run
- Workspace selection during `fastn login` and `fastn init`
- CLI split into `cli/` package for maintainability

### Changed

- Registry sync fetches from three scopes: workspace, organization, community
- `fastn list` groups connectors by source category
- Tenant header corrected to `x-fastn-space-tenantid`
- Tool schemas unwrapped for LLM (flat params) and re-wrapped for API execution

### Fixed

- Version alignment between pyproject.toml and __init__.py
- Error value preservation in API responses (Slack `channel_not_found` no longer overwritten)
- Agent summary table totals now include the final LLM response turn

## [0.1.0] - 2025-02-19

### Added

- `FastnClient` and `AsyncFastnClient` for sync and async workflows
- Dynamic connector proxy with attribute-based tool access (`fastn.slack.send_message()`)
- Multi-connection support via `connect()` and per-call `connection_id`
- LLM agent integration:
  - `get_tools_for(connector, format)` — returns tools in OpenAI, Anthropic, Gemini, Bedrock, or raw format
  - `execute(action_id, params)` — execute tools by action ID with LLM-generated parameters
- AI-powered mode via `run(prompt)` for natural language tool discovery
- Control plane: `admin.connectors.list()`, `admin.connectors.get()`, `get_tools()`, `get_tool()`
- Schema-aware migrations with deprecation warnings for smooth upgrades
- OAuth device authorization flow (`fastn login`) with automatic token refresh
- CLI commands: `init`, `login`, `logout`, `whoami`, `sync`, `add`, `remove`, `list`, `schema`, `version`
- IDE autocomplete via generated `.pyi` type stubs
- Automatic retry with exponential backoff for transient failures
- Config file security (owner-only permissions)
- PEP 561 `py.typed` marker for type checker support
- 9 typed exceptions for granular error handling
