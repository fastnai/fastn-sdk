"""Basic Fastn SDK usage — send a Slack message.

Update the credentials below and run:
    python examples/basic_usage.py
"""

from fastn import FastnClient

# --- Configuration (update these) ----------------------------------------
API_KEY = "your-api-key"
PROJECT_ID = "your-project-id"
# --------------------------------------------------------------------------

def main() -> None:
    fastn = FastnClient(
        api_key=API_KEY,
        project_id=PROJECT_ID,
        verbose=True,
    )

    result = fastn.slack.send_message(
        channel="general",
        text="Hello from Fastn SDK!",
    )
    print("Result:", result)


if __name__ == "__main__":
    main()
