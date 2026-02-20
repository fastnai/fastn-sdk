"""Multi-tenant and multi-connection usage.

Demonstrates how connection_id and tenant_id work:
  - No connection_id/tenant_id → uses the workspace default
  - connection_id → routes to a specific connected account
  - tenant_id → overrides the tenant for that call
  - fastn.connect() → binds a connection_id for repeated use

Update the credentials below and run:
    python examples/multi_tenant.py
"""

from fastn import FastnClient

# --- Configuration (update these) ----------------------------------------
API_KEY = "your-api-key"
PROJECT_ID = "your-project-id"
CONNECTION_ID = "your-connection-id"       # e.g. "conn_slack_workspace_a"
TENANT_ID = ""                              # e.g. "customer_acme"
CHANNEL = "general"
# --------------------------------------------------------------------------


def main() -> None:
    fastn = FastnClient(
        api_key=API_KEY,
        project_id=PROJECT_ID,
        verbose=False,
    )

    # ----------------------------------------------------------------
    # 1. Default — no connection_id, no tenant_id
    #    Uses the workspace/organization default connection
    # ----------------------------------------------------------------
    print("=== Default (workspace level) ===")
    result = fastn.slack.send_message(
        channel=CHANNEL,
        text="Message via default workspace connection",
    )
    print("Result:", result)

    # ----------------------------------------------------------------
    # 2. Specific connection_id — per-call override
    #    Routes to a specific Slack workspace connection
    # ----------------------------------------------------------------
    print("\n=== Specific connection (per-call) ===")
    result = fastn.slack.send_message(
        connection_id=CONNECTION_ID,
        channel=CHANNEL,
        text=f"Message via connection {CONNECTION_ID}",
    )
    print("Result:", result)

    # ----------------------------------------------------------------
    # 3. Bound connection — bind once, reuse for multiple calls
    #    All calls through this proxy use the bound connection_id
    # ----------------------------------------------------------------
    print("\n=== Bound connection ===")
    slack = fastn.connect(CONNECTION_ID)
    result = slack.send_message(
        channel=CHANNEL,
        text="Message via bound connection proxy",
    )
    print("Result:", result)

    # ----------------------------------------------------------------
    # 4. Tenant override — per-call tenant_id
    #    Changes the x-tenant header for a single call
    # ----------------------------------------------------------------
    print("\n=== Tenant override ===")
    result = fastn.slack.send_message(
        tenant_id=TENANT_ID,
        channel=CHANNEL,
        text=f"Message on behalf of tenant {TENANT_ID}",
    )
    print("Result:", result)

    # ----------------------------------------------------------------
    # 5. Both connection_id and tenant_id together
    # ----------------------------------------------------------------
    print("\n=== Connection + Tenant ===")
    result = fastn.slack.send_message(
        connection_id=CONNECTION_ID,
        tenant_id=TENANT_ID,
        channel=CHANNEL,
        text="Message with both connection and tenant override",
    )
    print("Result:", result)

    # ----------------------------------------------------------------
    # 6. Using execute() — same connection_id/tenant_id support
    # ----------------------------------------------------------------
    print("\n=== execute() with connection + tenant ===")
    result = fastn.execute(
        action_id="act_slack_send_message",
        params={"channel": CHANNEL, "text": "Via execute()"},
        connection_id=CONNECTION_ID,
        tenant_id=TENANT_ID,
    )
    print("Result:", result)


if __name__ == "__main__":
    main()
