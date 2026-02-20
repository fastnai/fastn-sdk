"""Fastn SDK — The fastest way to add enterprise integrations to any AI agent or app.

Provides two clients (sync and async) that give attribute-based access to
250+ integrations like Slack, Jira, GitHub, Salesforce, and more.

Setup:
    pip install fastn-sdk
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

    # Describe what you need — Fastn discovers the right tools
    tools = fastn.get_tools_for("Send a message on Slack", format="openai")

    # Feed tools to your LLM, get back a tool call, then execute:
    result = fastn.execute(action_id="send_message", params={"channel": "general", "text": "Hi"})

CLI agent mode:
    # AI-powered tool discovery and execution from the command line
    fastn agent "Send hello to #general on Slack"
    fastn agent --connector slack "Post deploy status to #releases"
    fastn agent --eval "Create a Jira ticket for the login bug"

Multi-connection / multi-tenant:
    # Per-call overrides
    fastn.slack.send_message(connection_id="conn_abc", tenant_id="acme", ...)

    # Bound proxy
    slack = fastn.connect("conn_abc")
    slack.send_message(channel="general", text="Hi")

    # Constructor-level tenant
    fastn = FastnClient(tenant_id="acme")

CLI tool execution:
    fastn run slack send_message --channel general --text "Hello!"
    fastn run slack send_message acme-tenant-id    # with tenant

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

__version__ = "0.2.3"

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
