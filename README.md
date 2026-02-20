# Fastn SDK

Pre-built tools for AI agents and apps — 250+ integrations including Slack, Jira, GitHub, Salesforce, HubSpot, Stripe, and more.

One SDK. One CLI. Every integration. Full IDE autocomplete. First-class LLM agent support.

## Why Fastn?

| Problem | Fastn Solution |
|---------|---------------|
| Each SaaS API has its own SDK, auth flow, and schema | One `FastnClient` with a unified interface for all 250+ integrations |
| LLM agents need tool schemas in provider-specific formats | `get_tools_for("slack", format="openai")` returns ready-to-use schemas |
| Managing OAuth tokens, API keys, and connections per-tenant is complex | Built-in multi-connection and multi-tenant support with `connection_id` and `tenant_id` |
| No type safety when calling integrations dynamically | Generated `.pyi` stubs give full IDE autocomplete with parameter names and types |

## SDKs

| Language | Package | Status |
|----------|---------|--------|
| **Python** | [`fastn-sdk`](https://pypi.org/project/fastn-sdk/) | Stable (v0.2.1) |
| **Node.js** | `@fastn/sdk` | Planned |

## Quick Start (Python)

```bash
pip install fastn-sdk
fastn login
fastn sync
fastn add slack
```

```python
from fastn import FastnClient

fastn = FastnClient()
fastn.slack.send_message(channel="general", text="Hello from Fastn!")
```

## LLM Agent Integration

Fastn provides tool schemas in native format for every major LLM provider. The workflow is three steps: get tools, send to LLM, execute the result.

```python
from fastn import FastnClient

fastn = FastnClient()

# Works with: openai, anthropic, gemini, bedrock, raw
tools = fastn.get_tools_for("slack", format="openai")

# Send tools to your LLM, get back tool_calls, then:
result = fastn.execute(action_id=tool_call.function.name, params=parsed_args)
```

Supported providers: **OpenAI**, **Anthropic Claude**, **Google Gemini**, **AWS Bedrock**, and any provider via `raw` format.

## CLI Agent Mode

Execute tools via natural language from the command line:

```bash
fastn agent "Send hello to #general on Slack"
fastn agent --connector slack "List all channels"
fastn agent --eval "Create a Jira ticket for the login bug"
```

## Documentation

- **[Python SDK Guide](python/README.md)** — full API reference, examples, error handling
- **[Changelog](python/CHANGELOG.md)** — release history
- **[fastn.ai](https://fastn.ai)** — product overview
- **[docs.fastn.ai](https://docs.fastn.ai)** — full documentation

## Repo Structure

```
fastn-sdk/
├── python/                  # Python SDK + CLI (PyPI: fastn)
│   ├── fastn/               # SDK source
│   │   ├── client.py        # FastnClient, AsyncFastnClient
│   │   ├── connector.py     # Dynamic connector proxy
│   │   ├── config.py        # Config management
│   │   ├── exceptions.py    # Typed exception hierarchy
│   │   ├── oauth.py         # OAuth device flow
│   │   ├── auth.py          # Auth helpers
│   │   └── cli/             # CLI commands (login, sync, add, run, agent)
│   ├── tests/
│   │   ├── sdk/             # SDK tests (129 tests)
│   │   └── cli/             # CLI tests (246 tests)
│   └── examples/
│       ├── sdk/             # SDK usage examples
│       └── cli/             # CLI usage examples
├── generator/               # Shared stub generation (.pyi / .d.ts)
└── node/                    # Node.js SDK (planned)
```

## Development

```bash
cd python
pip install -e ".[dev]"

# Run all tests (375 tests, ~6s)
make test

# Run only SDK tests (129 tests, ~5s)
make test-sdk

# Run only CLI tests (246 tests, <1s)
make test-cli

# Run a single test file
make test-file F=tests/cli/test_cli_commands.py

# Lint
make lint
```

## License

MIT
