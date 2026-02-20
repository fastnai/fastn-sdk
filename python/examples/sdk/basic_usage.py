"""Basic Fastn SDK usage — send a Slack message.

Update the credentials below and run:
    python examples/basic_usage.py
"""

from fastn import FastnClient

# --- Configuration (update these) ----------------------------------------
API_KEY = "9cbb710d583e17b370042825fee33a2bb7aaaa61"
PROJECT_ID = "c1653d47-6242-4a71-ac34-9fc59d01b97e"
# --------------------------------------------------------------------------

def main() -> None:
    fastn = FastnClient(
        api_key=API_KEY,
        project_id=PROJECT_ID,
        verbose=False,
    )

    result = fastn.slack.send_message(
        channel="general",
        text="Hello from Fastn SDK",
    )
    print("Result:", result)


if __name__ == "__main__":
    main()
