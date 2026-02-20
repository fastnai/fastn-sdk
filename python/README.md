# Fastn SDK for Python

Pre-built tools for AI agents and apps — 250+ integrations including Slack, Jira, GitHub, Salesforce, HubSpot, Stripe, and more.

[![PyPI version](https://img.shields.io/pypi/v/fastn-sdk.svg)](https://pypi.org/project/fastn-sdk/)
[![Python](https://img.shields.io/pypi/pyversions/fastn-sdk.svg)](https://pypi.org/project/fastn-sdk/)
[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](https://opensource.org/licenses/MIT)

## Installation

```bash
pip install fastn-sdk
```

Installs the SDK and CLI. Requires Python 3.8+.

## Quick Start

```bash
# 1. Authenticate
fastn login

# 2. Download the tool registry
fastn sync

# 3. Enable autocomplete for the tools you need
fastn add slack jira github
```

```python
from fastn import FastnClient

fastn = FastnClient()
fastn.slack.send_message(channel="general", text="Hello from Fastn!")
```

Async:

```python
from fastn import AsyncFastnClient

async with AsyncFastnClient() as fastn:
    await fastn.slack.send_message(channel="general", text="Hello!")
```

## Configuration

Fastn reads credentials from three sources (highest priority first):

1. **Constructor parameters**: `FastnClient(api_key="...", project_id="...")`
2. **Environment variables**: `FASTN_API_KEY`, `FASTN_PROJECT_ID`
3. **Config file**: `.fastn/config.json` (created by `fastn init` or `fastn login`)

```python
# Explicit credentials (no config file needed)
fastn = FastnClient(api_key="your-api-key", project_id="your-project-id")
```

All environment variables:

| Variable | Description |
|----------|-------------|
| `FASTN_API_KEY` | API key |
| `FASTN_PROJECT_ID` | Project / workspace ID |
| `FASTN_AUTH_TOKEN` | JWT from `fastn login` |
| `FASTN_TENANT_ID` | Default tenant ID |
| `FASTN_STAGE` | Environment: `LIVE`, `STAGING`, or `DEV` |

## LLM Agent Integration

The SDK provides tool schemas in every major LLM provider's native format. The workflow is:

1. Get tools for a connector in your LLM's format
2. Send tools to the LLM with the user's prompt
3. Execute the LLM's tool call through Fastn

```python
import json
from fastn import FastnClient

fastn = FastnClient()

# 1. Get tools (supports: openai, anthropic, gemini, bedrock, raw)
tools = fastn.get_tools_for("slack", format="openai")

# 2. Send to LLM
response = openai.chat.completions.create(
    model="gpt-4o",
    messages=[{"role": "user", "content": "Send hello to #general on Slack"}],
    tools=tools,
)

# 3. Execute
tool_call = response.choices[0].message.tool_calls[0]
result = fastn.execute(
    action_id=tool_call.function.name,
    params=json.loads(tool_call.function.arguments),
)
```

### Supported LLM Providers

| Format | Provider | Example |
|--------|----------|---------|
| `"openai"` | OpenAI, Azure OpenAI | `get_tools_for("slack", format="openai")` |
| `"anthropic"` | Anthropic Claude | `get_tools_for("slack", format="anthropic")` |
| `"gemini"` | Google Gemini / Vertex AI | `get_tools_for("slack", format="gemini")` |
| `"bedrock"` | AWS Bedrock Converse API | `get_tools_for("slack", format="bedrock")` |
| `"raw"` | Any (raw Fastn schemas) | `get_tools_for("slack", format="raw")` |

### Anthropic Claude Example

```python
import anthropic
from fastn import FastnClient

fastn = FastnClient()
tools = fastn.get_tools_for("slack", format="anthropic")

client = anthropic.Anthropic()
response = client.messages.create(
    model="claude-sonnet-4-20250514",
    max_tokens=1024,
    messages=[{"role": "user", "content": "Send 'Build passed' to #ci"}],
    tools=tools,
)

for block in response.content:
    if block.type == "tool_use":
        result = fastn.execute(action_id=block.name, params=block.input)
        print(result)
```

### Google Gemini Example

```python
from google import genai
from fastn import FastnClient

fastn = FastnClient()
tools = fastn.get_tools_for("slack", format="gemini")

client = genai.Client()
response = client.models.generate_content(
    model="gemini-2.0-flash",
    contents="Send a greeting to #general on Slack",
    config=genai.types.GenerateContentConfig(tools=tools),
)

for part in response.candidates[0].content.parts:
    if fn := part.function_call:
        result = fastn.execute(action_id=fn.name, params=dict(fn.args))
        print(result)
```

### AWS Bedrock Example

```python
import boto3
from fastn import FastnClient

fastn = FastnClient()
tools = fastn.get_tools_for("slack", format="bedrock")

bedrock = boto3.client("bedrock-runtime")
response = bedrock.converse(
    modelId="anthropic.claude-sonnet-4-20250514-v1:0",
    messages=[{"role": "user", "content": [{"text": "Notify #ops that deploy is done"}]}],
    toolConfig={"tools": tools},
)

for block in response["output"]["message"]["content"]:
    if "toolUse" in block:
        tool_use = block["toolUse"]
        result = fastn.execute(action_id=tool_use["name"], params=tool_use["input"])
        print(result)
```

## Multi-Connection Support

When you have multiple connections for the same tool (e.g. two Slack workspaces):

```python
# Per-call
fastn.slack.send_message(connection_id="conn_workspace_a", channel="general", text="Hi!")

# Or bind once
slack_a = fastn.connect("conn_workspace_a")
slack_a.send_message(channel="general", text="Hello!")
```

## Multi-Tenant Support

Route requests to the correct tenant (customer, organization, or team):

```python
# Per-call override
fastn.slack.send_message(tenant_id="acme", channel="general", text="Hello!")

# Constructor-level default
fastn = FastnClient(tenant_id="acme")

# Environment variable
# export FASTN_TENANT_ID=acme

# CLI flag
# fastn run slack send_message --tenant acme --channel general --text "Hello!"
```

**Priority:** per-call `tenant_id` > CLI `--tenant` flag > constructor param > `FASTN_TENANT_ID` env var > config file > `"organization"`

## Environments

Switch between `LIVE`, `STAGING`, and `DEV`:

```python
dev = FastnClient(stage="DEV")
staging = FastnClient(stage="STAGING")
prod = FastnClient()  # defaults to LIVE
```

Or: `export FASTN_STAGE=DEV`

## AI-Powered Mode

For quick prototyping, use natural language:

```python
result = fastn.run("Send hello to #general on Slack")
```

## CLI Reference

| Command | Description |
|---------|-------------|
| `fastn init` | Interactive setup — prompts for API key and project ID |
| `fastn login` | Authenticate via browser (OAuth device flow) |
| `fastn logout` | Clear stored authentication tokens |
| `fastn whoami` | Show current authenticated user |
| `fastn sync` | Download/update the tool registry |
| `fastn add <name> [...]` | Add tool stubs for IDE autocomplete |
| `fastn remove <name>` | Remove tool stubs |
| `fastn list` | Show all available tools |
| `fastn list --active` | Show only active/enabled tools |
| `fastn list -v` | Show tools with action details |
| `fastn run <tool> <action>` | Execute a tool action (interactive or inline params) |
| `fastn agent "<prompt>"` | AI-powered tool execution via natural language |
| `fastn schema <tool> <action>` | Print an action's input/output schema |
| `fastn version` | Show SDK and registry versions |

## CLI: `fastn agent`

Agentic CLI — describe what you want in natural language and the agent discovers tools, sends them to your LLM via native function calling, and executes tool calls in a loop until the task is complete.

```bash
fastn agent "Send hello to #general on Slack"
fastn agent --connector slack "List all channels"
fastn agent --eval "Create a Jira ticket for the login bug"
```

| Option | Default | Description |
|--------|---------|-------------|
| `--connector` | — | Scope tool discovery to a specific connector |
| `--tool` | — | Scope discovery to a specific tool/action |
| `--max-turns` | `10` | Maximum agentic loop iterations |
| `--max-tools` | `5` | Maximum number of tools passed to the LLM |
| `--max-errors` | `2` | Stop after this many consecutive tool errors |
| `-y` / `--yes` | off | Skip confirmation prompts before each tool call |
| `--eval` | off | Run LLM-based evaluation after the agent finishes |
| `--connection-id` | — | Connection ID for multi-connection tools |
| `--tenant` | — | Tenant ID override |

## CLI: `fastn run`

Execute tool actions directly from the command line:

```bash
# List available actions
fastn run slack

# Interactive mode (prompts for each parameter)
fastn run slack send_message

# Inline parameters
fastn run slack send_message --channel general --text "Hello!"

# With tenant override
fastn run slack send_message --tenant acme --channel general --text "Hello!"
```

## API Reference

### `FastnClient`

```python
FastnClient(
    api_key: str = None,        # Fastn API key (or FASTN_API_KEY)
    project_id: str = None,     # Project ID (or FASTN_PROJECT_ID)
    auth_token: str = None,     # JWT from fastn login (or FASTN_AUTH_TOKEN)
    tenant_id: str = None,      # Tenant ID (or FASTN_TENANT_ID)
    stage: str = None,          # "LIVE", "STAGING", "DEV" (or FASTN_STAGE)
    config_path: str = None,    # Path to config.json
    timeout: float = 30.0,      # HTTP timeout in seconds
    max_retries: int = 3,       # Retry count for transient failures
    verbose: bool = False,      # Debug logging
)
```

**Methods:**

| Method | Description |
|--------|-------------|
| `fastn.<tool>.<action>(**params)` | Execute an action on a tool |
| `fastn.connect(connection_id)` | Bind a connection, return a proxy |
| `fastn.execute(action_id, params, ...)` | Execute by action ID (for LLM agents) |
| `fastn.get_tools(tool_name)` | Get all actions with raw schemas |
| `fastn.get_tool(tool_name, action_name)` | Get one action's schema |
| `fastn.get_tools_for(tool_name, format)` | Get actions in LLM provider format |
| `fastn.run(prompt)` | AI-powered action discovery and execution |
| `fastn.admin.connectors.list()` | List all tools in registry |
| `fastn.admin.connectors.get(name)` | Get tool details |

### `AsyncFastnClient`

Same API as `FastnClient`, but all tool calls and `execute()` are `async`/`await`:

```python
async with AsyncFastnClient() as fastn:
    result = await fastn.slack.send_message(channel="general", text="Hi")
```

## Error Handling

All exceptions inherit from `FastnError`:

```python
from fastn import (
    FastnClient, FastnError, AuthError, ConfigError, APIError,
    ConnectorNotFoundError, ToolNotFoundError, ConnectionNotFoundError,
    OAuthError, RegistryError,
)

try:
    fastn.slack.send_message(channel="general", text="Hello!")
except AuthError:
    print("Invalid credentials — check your API key")
except ConnectorNotFoundError as e:
    print(f"Run: fastn sync && fastn add {e.connector_name}")
except ToolNotFoundError as e:
    print(f"Action '{e.tool_name}' not found in '{e.connector_name}'")
except APIError as e:
    print(f"HTTP {e.status_code}: {e}")
except ConfigError:
    print("Run: fastn init")
```

| Exception | When | Key Attributes |
|-----------|------|----------------|
| `FastnError` | Base class for all SDK errors | — |
| `AuthError` | Invalid or expired credentials | — |
| `ConfigError` | Missing API key or project ID | — |
| `APIError` | HTTP error from the Fastn API | `.status_code`, `.response_body` |
| `ConnectorNotFoundError` | Tool not in registry | `.connector_name` |
| `ToolNotFoundError` | Action not found in tool | `.tool_name`, `.connector_name` |
| `ConnectionNotFoundError` | Connection ID not recognized | — |
| `OAuthError` | OAuth flow failed | `.error_code` |
| `RegistryError` | Registry sync or parse failure | — |

## IDE Autocomplete

After `fastn sync` and `fastn add <name>`, your IDE shows full autocomplete:

- **PyCharm / IntelliJ**: Works automatically with `.pyi` stubs
- **VS Code (Pylance)**: Add `".fastn/python"` to `python.analysis.extraPaths`
- **mypy**: Set `mypy_path = .fastn/python`

## Control Plane

Inspect the tool registry programmatically:

```python
connectors = fastn.admin.connectors.list()       # All tools
slack = fastn.admin.connectors.get("slack")       # Tool details
tools = fastn.get_tools("slack")                  # All actions (raw schemas)
tool = fastn.get_tool("slack", "sendmessage")     # Single action schema
```

## Examples

See [`examples/`](examples/) for runnable scripts:

| Directory | Contents |
|-----------|----------|
| [`examples/sdk/`](examples/sdk/) | SDK usage — basic, async, LLM agents, multi-tenant, environments, error handling |
| [`examples/cli/`](examples/cli/) | CLI usage — all commands with examples |

## Development

```bash
# Install in dev mode
pip install -e ".[dev]"

# Run all tests (375 tests, ~6s)
make test

# Run only SDK tests (129 tests, ~5s)
make test-sdk

# Run only CLI tests (246 tests, <1s)
make test-cli

# Run a single test file
make test-file F=tests/cli/test_cli_commands.py

# Or use pytest directly
python3 -m pytest tests/sdk/ -q       # SDK only
python3 -m pytest tests/cli/ -q       # CLI only
python3 -m pytest tests/ -q           # All
python3 -m pytest tests/ -m sdk -q    # By marker
python3 -m pytest tests/ -m cli -q    # By marker
```

### Test Structure

```
tests/
├── sdk/                           # SDK core tests (129 tests)
│   ├── test_client.py             # FastnClient, AsyncFastnClient
│   ├── test_connector.py          # DynamicConnector proxy
│   ├── test_config.py             # Config loading, env vars, validation
│   ├── test_exceptions.py         # Exception hierarchy
│   ├── test_auth.py               # Auth helpers
│   └── test_oauth.py              # OAuth device flow, token refresh
└── cli/                           # CLI command tests (246 tests)
    ├── test_cli_commands.py        # All CLI commands (sync, add, remove, list, run, agent, etc.)
    ├── test_cli_helpers.py         # CLI helper functions
    ├── test_agent_command.py       # fastn agent command
    ├── test_agent_helpers.py       # Agent helper functions
    ├── test_helpers_extended.py    # Extended helper tests (token, schema, parsing)
    ├── test_detect_api_error.py    # API error detection across providers
    └── test_detect_languages.py    # SDK language detection for stub generation
```

## License

MIT
