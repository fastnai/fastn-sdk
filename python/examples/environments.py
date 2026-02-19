"""Environment switching — DEV, STAGING, LIVE.

The Fastn API uses the `stage` header to route requests to different
environments. All environments use the same base URL.

Set the environment via:
    1. Constructor parameter:  FastnClient(stage="DEV")
    2. Environment variable:   FASTN_STAGE=DEV
    3. Config file:            .fastn/config.json -> {"stage": "DEV"}

Priority: constructor param > env var > config file > default ("LIVE")

Update the credentials below and run:
    python examples/environments.py
"""

from fastn import FastnClient

# --- Configuration (update these) ----------------------------------------
API_KEY = "your-api-key"
PROJECT_ID = "your-project-id"
STAGE = "LIVE"                             # "LIVE", "STAGING", or "DEV"
CHANNEL = "general"
CONNECTION_ID = None                       # optional, e.g. "conn_slack_dev"
TENANT_ID = None                           # optional, e.g. "dev_tenant"
# --------------------------------------------------------------------------


def main() -> None:
    fastn = FastnClient(
        api_key=API_KEY,
        project_id=PROJECT_ID,
        stage=STAGE,
        verbose=True,
    )

    print(f"=== Sending to {STAGE} environment ===")

    kwargs = {
        "channel": CHANNEL,
        "text": f"Hello from {STAGE} environment!",
    }
    if CONNECTION_ID:
        kwargs["connection_id"] = CONNECTION_ID
    if TENANT_ID:
        kwargs["tenant_id"] = TENANT_ID

    result = fastn.slack.send_message(**kwargs)
    print("Result:", result)

    fastn.close()


if __name__ == "__main__":
    main()
