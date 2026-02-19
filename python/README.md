# Fastn SDK for Python

Typed, deterministic access to 250+ integrations — Slack, Jira, GitHub, Salesforce, and more. Works for both traditional applications and AI agent workflows.

[![PyPI version](https://img.shields.io/pypi/v/fastn-sdk.svg)](https://pypi.org/project/fastn-sdk/)
[![Python](https://img.shields.io/pypi/pyversions/fastn-sdk.svg)](https://pypi.org/project/fastn-sdk/)
[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](https://opensource.org/licenses/MIT)

## Installation

```bash
pip install fastn-sdk
```

## Quick Start

### 1. Initialize credentials

```bash
fastn init
```

Prompts for your API key and project ID, then saves them to `.fastn/config.json` (automatically gitignored).

Alternatively, log in with your browser:

```bash
fastn login
```

### 2. Sync the connector registry

```bash
fastn sync
```

Downloads all available connector metadata (names, tools, schemas).

### 3. Add connectors you need

```bash
fastn add slack jira github
```

Generates typed stubs so your IDE shows full autocomplete with parameter names and types.

### 4. Use in code

```python
from fastn import FastnClient

fastn = FastnClient()
response = fastn.slack.send_message(channel="general", text="Hello from Fastn!")
print(response)
```

**Async:**

```python
from fastn import AsyncFastnClient

async def main():
    async with AsyncFastnClient() as fastn:
        response = await fastn.slack.send_message(channel="general", text="Hello!")
        print(response)
```

## Explicit Configuration

Pass credentials directly instead of using the config file:

```python
fastn = FastnClient(
    api_key="your-api-key",
    project_id="your-project-id",
)
```

Or use environment variables:

```bash
export FASTN_API_KEY="your-api-key"
export FASTN_PROJECT_ID="your-project-id"
```

## Multi-Connection Support

When you have multiple connections for the same connector (e.g. two Slack workspaces):

```python
# Per-call connection_id
fastn.slack.send_message(
    connection_id="conn_workspace_a",
    channel="general",
    text="Hello workspace A!",
)

# Or bind once with connect()
slack_a = fastn.connect("conn_workspace_a")
slack_a.send_message(channel="general", text="Hello!")
slack_a.create_channel(name="new-channel")
```

## Environments

The Fastn API supports three environments: `LIVE` (production), `STAGING`, and `DEV`. The environment is controlled via the `stage` header — all environments use the same base URL.

```python
# Via constructor parameter
dev = FastnClient(stage="DEV")
staging = FastnClient(stage="STAGING")
prod = FastnClient()  # defaults to LIVE
```

Via environment variable:

```bash
export FASTN_STAGE=DEV
```

Via config file (`.fastn/config.json`):

```json
{"stage": "DEV"}
```

**Priority:** constructor param > `FASTN_STAGE` env var > config file > `"LIVE"`

Combine with connection and tenant overrides:

```python
dev = FastnClient(stage="DEV")
dev.slack.send_message(
    connection_id="conn_dev_slack",
    tenant_id="dev_tenant",
    channel="general",
    text="DEV environment message",
)
```

## LLM Agent Integration

The SDK provides first-class support for LLM agent workflows. Get tool schemas in your LLM provider's native format, feed them to the model, and execute the result — all through the SDK.

### Workflow

```python
# 1. Get tools in your LLM's format
tools = fastn.get_tools_for("slack", format="openai")

# 2. Send to your LLM
response = openai.chat.completions.create(
    model="gpt-4o",
    messages=[{"role": "user", "content": "Send hello to #general on Slack"}],
    tools=tools,
)

# 3. Execute the LLM's tool call
tool_call = response.choices[0].message.tool_calls[0]
result = fastn.execute(
    action_id=tool_call.function.name,
    params=json.loads(tool_call.function.arguments),
)
```

### Supported Formats

| Format | Provider | Method |
|--------|----------|--------|
| `"openai"` | OpenAI, Azure OpenAI | `get_tools_for("slack", format="openai")` |
| `"anthropic"` | Anthropic Claude | `get_tools_for("slack", format="anthropic")` |
| `"gemini"` | Google Gemini / Vertex AI | `get_tools_for("slack", format="gemini")` |
| `"bedrock"` | AWS Bedrock Converse API | `get_tools_for("slack", format="bedrock")` |
| `"raw"` | Any (raw Fastn schemas) | `get_tools_for("slack", format="raw")` |

### OpenAI Example

```python
import json
import openai
from fastn import FastnClient

fastn = FastnClient()
tools = fastn.get_tools_for("slack", format="openai")

response = openai.chat.completions.create(
    model="gpt-4o",
    messages=[{"role": "user", "content": "Post 'Deploy complete' to #releases"}],
    tools=tools,
)

for tool_call in response.choices[0].message.tool_calls or []:
    result = fastn.execute(
        action_id=tool_call.function.name,
        params=json.loads(tool_call.function.arguments),
    )
    print(result)
```

### Anthropic Example

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

### Raw Schema Access

For custom integrations or unsupported LLM providers:

```python
# Get raw schemas with actionId, inputSchema, outputSchema
raw_tools = fastn.get_tools_for("slack", format="raw")

# Or access individual tools
tool = fastn.get_tool("slack", "sendmessage")
print(tool["actionId"])      # "act_slack_sendmessage"
print(tool["inputSchema"])   # JSON Schema for parameters
print(tool["outputSchema"])  # JSON Schema for response
```

## AI-Powered Mode

For quick prototyping, use natural language to discover and execute tools:

```python
result = fastn.run("Send hello to #general on Slack")
```

## Control Plane

Inspect the connector registry programmatically:

```python
# List all available connectors
connectors = fastn.admin.connectors.list()

# Get details for a specific connector
slack = fastn.admin.connectors.get("slack")

# Get all tools for a connector (raw schemas)
tools = fastn.get_tools("slack")

# Get a single tool's schema
tool = fastn.get_tool("slack", "sendmessage")
```

## CLI Reference

| Command | Description |
|---------|-------------|
| `fastn init` | Interactive setup — prompts for API key and project ID |
| `fastn login` | Authenticate via browser (OAuth device flow) |
| `fastn logout` | Clear stored authentication tokens |
| `fastn whoami` | Show current authenticated user |
| `fastn sync` | Download/update the connector registry |
| `fastn add <name> [...]` | Add connector stubs for IDE autocomplete |
| `fastn remove <name>` | Remove connector stubs |
| `fastn list` | Show all available connectors |
| `fastn list -v` | Show connectors with tool details |
| `fastn schema <connector> <tool>` | Print a tool's input/output schema |
| `fastn version` | Show SDK and registry versions |

## IDE Autocomplete Setup

After running `fastn sync` and `fastn add <connector>`, your IDE will provide full autocomplete:

- **PyCharm / IntelliJ**: Works automatically with `.pyi` stubs
- **VS Code (Pylance)**: Add to `python.analysis.extraPaths` in settings:
  ```json
  {
    "python.analysis.extraPaths": [".fastn/python"]
  }
  ```
- **mypy**: Add to `mypy.ini`:
  ```ini
  [mypy]
  mypy_path = .fastn/python
  ```

## Error Handling

All exceptions inherit from `FastnError`:

```python
from fastn import (
    FastnClient,
    FastnError,
    AuthError,
    ConfigError,
    APIError,
    ConnectorNotFoundError,
    ToolNotFoundError,
    ConnectionNotFoundError,
    OAuthError,
    RegistryError,
)

try:
    fastn = FastnClient()
    fastn.slack.send_message(channel="general", text="Hello!")
except AuthError:
    print("Invalid credentials — check your API key")
except ConnectorNotFoundError as e:
    print(f"Run: fastn sync && fastn add {e.connector_name}")
except ToolNotFoundError as e:
    print(f"Tool '{e.tool_name}' not found in '{e.connector_name}'")
except APIError as e:
    print(f"HTTP {e.status_code}: {e}")
except ConfigError:
    print("Run: fastn init")
```

| Exception | When |
|-----------|------|
| `FastnError` | Base class for all SDK errors |
| `AuthError` | Invalid or expired credentials |
| `ConfigError` | Missing API key or project ID |
| `APIError` | HTTP error from the Fastn API (has `.status_code`, `.response_body`) |
| `ConnectorNotFoundError` | Connector not in registry |
| `ToolNotFoundError` | Tool not found in connector |
| `ConnectionNotFoundError` | Connection ID not recognized |
| `OAuthError` | OAuth flow failed (has `.error_code`) |
| `RegistryError` | Registry sync or parse failure |

## API Reference

### `FastnClient`

```python
FastnClient(
    api_key: str = None,        # Fastn API key (or set FASTN_API_KEY)
    project_id: str = None,     # Fastn project ID (or set FASTN_PROJECT_ID)
    auth_token: str = None,     # JWT from `fastn login` (or set FASTN_AUTH_TOKEN)
    tenant_id: str = None,      # Tenant ID (default: "organization", or set FASTN_TENANT_ID)
    stage: str = None,          # Environment: "LIVE", "STAGING", "DEV" (or set FASTN_STAGE)
    config_path: str = None,    # Path to config.json (default: .fastn/config.json)
    timeout: float = 30.0,      # HTTP timeout in seconds
    max_retries: int = 3,       # Retry count for transient failures
    verbose: bool = False,      # Enable debug logging
)
```

**Methods:**

| Method | Description |
|--------|-------------|
| `fastn.<connector>.<tool>(**params)` | Execute a tool on a connector |
| `fastn.connect(connection_id)` | Bind a connection and return a proxy |
| `fastn.execute(action_id, params, ...)` | Execute a tool by action ID (for LLM agents) |
| `fastn.get_tools(connector_name)` | Get all tools with raw schemas |
| `fastn.get_tool(connector_name, tool_name)` | Get one tool's schema |
| `fastn.get_tools_for(connector_name, format)` | Get tools in LLM provider format |
| `fastn.run(prompt)` | AI-powered tool discovery and execution |
| `fastn.admin.connectors.list()` | List all connectors in registry |
| `fastn.admin.connectors.get(name)` | Get connector details |

### `AsyncFastnClient`

Same API as `FastnClient`, but all tool calls and `execute()` are `async`/`await`. Use as an async context manager:

```python
async with AsyncFastnClient() as fastn:
    result = await fastn.slack.send_message(channel="general", text="Hi")
```

## Examples

See the [`examples/`](examples/) directory for runnable scripts:

| Script | Description |
|--------|-------------|
| [`basic_usage.py`](examples/basic_usage.py) | Send a Slack message using the default connection |
| [`multi_tenant.py`](examples/multi_tenant.py) | Connection IDs, tenant overrides, bound proxies |
| [`llm_agent.py`](examples/llm_agent.py) | Full LLM agent workflow (OpenAI, Anthropic, Gemini) |
| [`environments.py`](examples/environments.py) | Switch between DEV, STAGING, and LIVE |

## License

MIT
