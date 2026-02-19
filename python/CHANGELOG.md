# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

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
