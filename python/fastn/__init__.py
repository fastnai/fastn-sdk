"""Fastn SDK — Typed access to 250+ integrations for apps and AI agents.

Provides two clients (sync and async) that give attribute-based access to
connectors like Slack, Jira, GitHub, Salesforce, and more.

Setup:
    pip install fastn
    fastn init          # or: fastn login
    fastn sync
    fastn add slack

Quick start:
    from fastn import FastnClient

    fastn = FastnClient(api_key="...", project_id="...")
    fastn.slack.send_message(channel="general", text="Hello!")

Async:
    from fastn import AsyncFastnClient

    async with AsyncFastnClient(api_key="...", project_id="...") as fastn:
        await fastn.slack.send_message(channel="general", text="Hello!")

LLM agent integration:
    fastn = FastnClient(api_key="...", project_id="...")

    # Get tools in OpenAI/Anthropic/Gemini/Bedrock format
    tools = fastn.get_tools_for("slack", format="openai")

    # Feed tools to your LLM, get back a tool call, then execute:
    result = fastn.execute(action_id="act_slack_send_message", params={...})

Multi-connection / multi-tenant:
    # Per-call overrides
    fastn.slack.send_message(connection_id="conn_abc", tenant_id="acme", ...)

    # Bound proxy
    slack = fastn.connect("conn_abc")
    slack.send_message(channel="general", text="Hi")

Environments (LIVE / STAGING / DEV):
    fastn = FastnClient(api_key="...", project_id="...", stage="DEV")
    # Or: FASTN_STAGE=DEV

Configuration priority:
    constructor params > environment variables > .fastn/config.json

Environment variables:
    FASTN_API_KEY, FASTN_PROJECT_ID, FASTN_AUTH_TOKEN,
    FASTN_TENANT_ID, FASTN_STAGE

Exceptions (all inherit from FastnError):
    AuthError, ConfigError, APIError, ConnectorNotFoundError,
    ToolNotFoundError, ConnectionNotFoundError, OAuthError, RegistryError
"""

from __future__ import annotations

from fastn.client import AsyncFastnClient, FastnClient
from fastn.exceptions import (
    APIError,
    AuthError,
    ConfigError,
    ConnectionNotFoundError,
    ConnectorNotFoundError,
    FastnError,
    OAuthError,
    RegistryError,
    ToolNotFoundError,
)

__version__ = "0.1.0"

__all__ = [
    "APIError",
    "AsyncFastnClient",
    "AuthError",
    "ConfigError",
    "ConnectionNotFoundError",
    "ConnectorNotFoundError",
    "FastnClient",
    "FastnError",
    "OAuthError",
    "RegistryError",
    "ToolNotFoundError",
    "__version__",
]
