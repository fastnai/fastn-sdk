"""Connector examples — direct connector access, tool execution, and SDK features.

Covers:
  1. Basic usage           — send a Slack message, send a Gmail email
  2. Async usage           — concurrent tool calls with AsyncFastnClient
  3. Cross-connector       — read last unread Gmail and forward to Slack
  4. Environments          — DEV / STAGING / LIVE switching
  5. Error handling        — exception hierarchy and retry patterns
  6. Multiple connections  — route calls to different connected accounts
  7. Multi-tenant          — route calls on behalf of end-user tenants

Update the credentials below and run:
    python examples/sdk/connectors.py
"""

from __future__ import annotations

import asyncio
import json
import time

from fastn import (
    AsyncFastnClient,
    FastnClient,
    FastnError,
    AuthError,
    ConfigError,
    APIError,
    ConnectorNotFoundError,
    ToolNotFoundError,
)

# --- Configuration (update these) ----------------------------------------
API_KEY = "your-api-key"
PROJECT_ID = "your-project-id"
# --------------------------------------------------------------------------


def _header(title: str) -> None:
    print(f"\n{'=' * 60}\n{title}\n{'=' * 60}")


# ===================================================================
# 1. Basic usage
# ===================================================================

def basic_usage() -> None:
    """Send a Slack message and a Gmail email."""
    _header("1. BASIC USAGE")

    with FastnClient(api_key=API_KEY, project_id=PROJECT_ID) as fastn:
        # Slack — send a channel message
        result = fastn.slack.send_message(channel="general-test", text="Hello from Fastn SDK")
        print("Slack:", result)

        # Gmail — send an email
        result = fastn.gmail.send_mail(
            subject="Weekly update",
            to="team@example.com",
            content="Here are this week's highlights...",
        )
        print("Gmail:", result)


# ===================================================================
# 2. Async usage
# ===================================================================

async def async_usage() -> None:
    """Non-blocking tool calls with AsyncFastnClient."""
    _header("2. ASYNC USAGE")

    async with AsyncFastnClient(api_key=API_KEY, project_id=PROJECT_ID) as fastn:
        # Single call
        result = await fastn.slack.send_message(channel="general-test", text="Hello async!")
        print("Single call:", result)

        # Concurrent calls across connectors
        results = await asyncio.gather(
            fastn.slack.send_message(channel="general-test", text="Update from SDK"),
            fastn.slack.get_channels(),
            fastn.gmail.get_mails(q="is:unread", maxResults="5"),
        )
        for i, r in enumerate(results, 1):
            print(f"Concurrent call {i}:", r)



# ===================================================================
# 3. Cross-connector
# ===================================================================

def gmail_to_slack() -> None:
    """Read the last unread email from Gmail and forward it to Slack."""
    _header("3. CROSS-CONNECTOR — Gmail to Slack")

    with FastnClient(api_key=API_KEY, project_id=PROJECT_ID) as fastn:
        # Step 1: Get unread emails
        emails = fastn.gmail.get_mails(q="is:unread", maxResults="1")
        messages = emails.get("messages", [])

        if not messages:
            print("No unread emails found.")
            return

        # Step 2: Get the full email content
        message_id = messages[0]["id"]
        email = fastn.gmail.get_mail(messageId=message_id, format="full")
        print(f"Email: {json.dumps(email, default=str)[:200]}")

        # Step 3: Extract subject and snippet
        subject = email.get("subject", "(no subject)")
        snippet = email.get("snippet", email.get("body", ""))[:300]

        # Step 4: Forward to Slack
        result = fastn.slack.send_message(
            channel="general-test",
            text=f"*New email:* {subject}\n>{snippet}",
        )
        print(f"Forwarded to Slack: {result.get('ok')}")


# ===================================================================
# 4. Environments
# ===================================================================

def environments(stage: str = "LIVE") -> None:
    """DEV, STAGING, LIVE — environment switching via the stage header.

    Set the environment via:
        1. Constructor parameter:  FastnClient(stage="DEV")
        2. Environment variable:   FASTN_STAGE=DEV
        3. Config file:            .fastn/config.json -> {"stage": "DEV"}

    Priority: constructor param > env var > config file > default ("LIVE")
    """
    _header("4. ENVIRONMENTS")

    with FastnClient(api_key=API_KEY, project_id=PROJECT_ID, stage=stage) as fastn:
        print(f"Sending to {stage} environment")
        result = fastn.slack.send_message(
            channel="general-test",
            text=f"Hello from {stage} environment!",
        )
        print("Result:", result)


# ===================================================================
# 5. Error handling
# ===================================================================

def error_handling() -> None:
    """Exception hierarchy and common error scenarios.

    FastnError
    +-- AuthError              — invalid credentials or expired token
    +-- ConfigError            — missing config fields
    +-- APIError               — HTTP errors from the Fastn API
    +-- ConnectorNotFoundError — connector not in registry
    +-- ToolNotFoundError      — tool not found in connector
    +-- ConnectionNotFoundError— connection_id not valid
    +-- OAuthError             — device login failures
    +-- RegistryError          — registry sync issues
    """
    _header("5. ERROR HANDLING")

    # ConfigError — missing credentials
    try:
        FastnClient(api_key="", project_id="")
    except ConfigError as e:
        print(f"ConfigError: {e}")

    with FastnClient(api_key=API_KEY, project_id=PROJECT_ID) as fastn:
        # ConnectorNotFoundError
        try:
            _ = fastn.nonexistent_connector
        except ConnectorNotFoundError as e:
            print(f"ConnectorNotFoundError: {e}")

        # ToolNotFoundError
        try:
            fastn.slack.nonexistent_tool(param="value")
        except ToolNotFoundError as e:
            print(f"ToolNotFoundError: {e}")

        # APIError / AuthError
        try:
            fastn.gmail.send_mail(subject="test", to="bad", content="test")
        except AuthError as e:
            print(f"AuthError: {e}")
        except APIError as e:
            print(f"APIError (status {e.status_code}): {e}")

        # Retry pattern
        print("\n=== Retry pattern ===")
        for attempt in range(1, 4):
            try:
                result = fastn.slack.send_message(channel="general-test", text="Hello with retry!")
                print(f"  Attempt {attempt}: Success")
                break
            except APIError as e:
                wait = 2 ** attempt
                print(f"  Attempt {attempt}: APIError, retrying in {wait}s...")
                time.sleep(wait)
            except AuthError:
                print(f"  Attempt {attempt}: Auth error, cannot retry.")
                break


# ===================================================================
# 6. Multiple connections
# ===================================================================

def multiple_connections() -> None:
    """Route calls to different connected accounts.

    Use connection_id to target a specific connected account when you have
    multiple accounts for the same connector (e.g. two Slack workspaces,
    a personal and work Gmail).

    - Per-call:       fastn.slack.send_message(connection_id="conn_...", ...)
    - Bound proxy:    slack = fastn.connect("conn_..."); slack.send_message(...)
    """
    _header("6. MULTIPLE CONNECTIONS")

    with FastnClient(api_key=API_KEY, project_id=PROJECT_ID) as fastn:
        # Default — uses the workspace-level connection
        print("=== Default connection ===")
        result = fastn.slack.send_message(channel="general-test", text="Default workspace")
        print("Result:", result)

        # Per-call connection_id — target a specific Slack workspace
        print("\n=== Per-call connection_id (Slack workspace B) ===")
        result = fastn.slack.send_message(
            connection_id="conn_slack_workspace_b",
            channel="general-test",
            text="Hello from workspace B",
        )
        print("Result:", result)

        # Per-call connection_id — target a specific Gmail account
        print("\n=== Per-call connection_id (Gmail support account) ===")
        result = fastn.gmail.send_mail(
            connection_id="conn_gmail_support",
            subject="Hello",
            to="user@example.com",
            content="Sent from the support Gmail account",
        )
        print("Result:", result)

        # Bound proxy — bind once, reuse for multiple calls
        print("\n=== Bound proxy ===")
        slack_b = fastn.connect("conn_slack_workspace_b")
        slack_b.send_message(channel="general-test", text="First message via proxy")
        slack_b.send_message(channel="random", text="Second message via proxy")
        print("Sent two messages through the bound proxy")


# ===================================================================
# 7. Multi-tenant
# ===================================================================

def multi_tenant() -> None:
    """Route calls on behalf of end-user tenants.

    Use tenant_id when your platform serves multiple customers and each
    customer has their own connected accounts managed through Fastn.

    - tenant_id routes to that tenant's connections
    - Can be combined with connection_id for precise routing
    """
    _header("7. MULTI-TENANT")

    with FastnClient(api_key=API_KEY, project_id=PROJECT_ID) as fastn:
        # Send a Slack message on behalf of tenant "acme"
        print("=== Tenant: acme ===")
        result = fastn.slack.send_message(
            tenant_id="customer_acme",
            channel="general-test",
            text="Hello from Acme's Slack",
        )
        print("Result:", result)

        # Send a Gmail on behalf of tenant "globex"
        print("\n=== Tenant: globex ===")
        result = fastn.gmail.send_mail(
            tenant_id="customer_globex",
            subject="Partnership update",
            to="partner@example.com",
            content="Sent on behalf of Globex Corp",
        )
        print("Result:", result)

        # Combine tenant_id + connection_id for precise routing
        print("\n=== Tenant + connection ===")
        result = fastn.slack.send_message(
            tenant_id="customer_acme",
            connection_id="conn_slack_acme_eng",
            channel="engineering",
            text="Routed to Acme's engineering Slack workspace",
        )
        print("Result:", result)


# ===================================================================
# Main
# ===================================================================

if __name__ == "__main__":
    # Uncomment the examples you want to run:
    basic_usage()
    # asyncio.run(async_usage())
    # gmail_to_slack()
    # environments(stage="LIVE")
    # error_handling()
    # multiple_connections()
    # multi_tenant()
