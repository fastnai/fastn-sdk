# Fastn SDK

Typed, deterministic access to 250+ integrations — Slack, Jira, GitHub, Salesforce, and more.

No AI interpretation at runtime. Full IDE autocomplete. One unified interface. First-class LLM agent support.

## Installation

### Python

```bash
pip install fastn
```

## Quick Start

### 1. Initialize credentials

```bash
fastn init
```

Prompts for your API key and project ID, then saves them to `.fastn/config.json` (automatically gitignored).

Or authenticate via browser:

```bash
fastn login
```

### 2. Sync the connector registry

```bash
fastn sync
```

Downloads all available connector metadata.

### 3. Add connectors you need

```bash
fastn add slack jira github
```

Generates typed stubs for IDE autocomplete.

### 4. Use in code

**Python:**

```python
from fastn import FastnClient

fastn = FastnClient()
response = fastn.slack.send_message(channel="general", text="Hello from Fastn!")
print(response)
```

**Python (async):**

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

Or via environment variables:

```bash
export FASTN_API_KEY="your-api-key"
export FASTN_PROJECT_ID="your-project-id"
```

## Environments

Switch between `LIVE`, `STAGING`, and `DEV` environments:

```python
dev = FastnClient(stage="DEV")
staging = FastnClient(stage="STAGING")
prod = FastnClient()  # defaults to LIVE
```

Or via environment variable: `FASTN_STAGE=DEV`

## LLM Agent Integration

Get tool schemas in your LLM provider's native format, feed them to the model, and execute the result:

```python
import json
from fastn import FastnClient

fastn = FastnClient()

# 1. Get tools in OpenAI format (also supports: anthropic, gemini, bedrock, raw)
tools = fastn.get_tools_for("slack", format="openai")

# 2. Send to your LLM
response = openai.chat.completions.create(
    model="gpt-4o",
    messages=[{"role": "user", "content": "Send hello to #general on Slack"}],
    tools=tools,
)

# 3. Execute the tool call
tool_call = response.choices[0].message.tool_calls[0]
result = fastn.execute(
    action_id=tool_call.function.name,
    params=json.loads(tool_call.function.arguments),
)
```

Supported formats: `openai`, `anthropic`, `gemini`, `bedrock`, `raw`

## Multi-Connection Support

```python
# Per-call
fastn.slack.send_message(connection_id="conn_abc", channel="general", text="Hi!")

# Or bind once
slack = fastn.connect("conn_abc")
slack.send_message(channel="general", text="Hi!")
```

## AI-Powered Mode

Use natural language to discover and execute tools:

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
| `fastn sync` | Download/update the connector registry |
| `fastn add <name> [...]` | Add connector stubs for IDE autocomplete |
| `fastn remove <name>` | Remove connector stubs |
| `fastn list` | Show all available connectors |
| `fastn list -v` | Show connectors with tool details |
| `fastn schema <connector> <tool>` | Print a tool's input/output schema |
| `fastn version` | Show SDK and registry versions |

## How It Works

The SDK is a thin dynamic proxy. When you write:

```python
fastn.slack.send_message(channel="general", text="Hello")
```

It translates to an API call with the correct `actionId` from the locally cached registry. You never see raw HTTP calls, action IDs, or agent IDs.

## Project Structure

```
.fastn/
├── config.json          # Credentials (gitignored)
├── manifest.json        # Registry version + installed connectors
├── registry.json        # Cached connector metadata
└── python/
    ├── index.pyi        # Root client stubs
    └── connectors/
        ├── slack.pyi    # Full stubs for installed connectors
        └── _placeholders.pyi
```

## Error Handling

The SDK provides typed exceptions for granular error handling:

| Exception | When |
|-----------|------|
| `FastnError` | Base class for all SDK errors |
| `AuthError` | Invalid or expired credentials |
| `ConfigError` | Missing API key or project ID |
| `APIError` | HTTP error from the API (`.status_code`, `.response_body`) |
| `ConnectorNotFoundError` | Connector not in registry |
| `ToolNotFoundError` | Tool not found in connector |
| `ConnectionNotFoundError` | Connection ID not recognized |
| `OAuthError` | OAuth flow failure (`.error_code`) |
| `RegistryError` | Registry sync or parse failure |

```python
from fastn import FastnClient, ConnectorNotFoundError

try:
    fastn.unknown_connector.some_tool()
except ConnectorNotFoundError as e:
    print(f"Run: fastn sync && fastn add {e.connector_name}")
```

## License

MIT
