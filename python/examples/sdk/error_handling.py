"""Error handling patterns — catch and handle Fastn SDK exceptions.

Demonstrates the exception hierarchy and common error scenarios:
    FastnError
    ├── AuthError              — invalid credentials or expired token
    ├── ConfigError            — missing config fields
    ├── APIError               — HTTP errors from the Fastn API
    ├── ConnectorNotFoundError — connector not in registry
    ├── ToolNotFoundError      — action not found in connector
    ├── ConnectionNotFoundError— connection_id not valid
    ├── OAuthError             — device login failures
    └── RegistryError          — registry sync issues

Update the credentials below and run:
    python examples/error_handling.py
"""

from fastn import (
    FastnClient,
    FastnError,
    AuthError,
    ConfigError,
    APIError,
    ConnectorNotFoundError,
    ToolNotFoundError,
    ConnectionNotFoundError,
)

# --- Configuration (update these) ----------------------------------------
API_KEY = "your-api-key"
PROJECT_ID = "your-project-id"
# --------------------------------------------------------------------------


def main() -> None:
    # ── 1. ConfigError — missing credentials ─────────────────────────
    print("=== ConfigError ===")
    try:
        bad_client = FastnClient(api_key="", project_id="")
    except ConfigError as e:
        print(f"  Caught ConfigError: {e}")

    # ── 2. Normal client setup ───────────────────────────────────────
    fastn = FastnClient(api_key=API_KEY, project_id=PROJECT_ID)

    # ── 3. ConnectorNotFoundError — unknown connector ────────────────
    print("\n=== ConnectorNotFoundError ===")
    try:
        _ = fastn.nonexistent_connector
    except ConnectorNotFoundError as e:
        print(f"  Caught ConnectorNotFoundError: {e}")

    # ── 4. ToolNotFoundError — unknown action ────────────────────────
    print("\n=== ToolNotFoundError ===")
    try:
        fastn.slack.nonexistent_action(param="value")
    except ToolNotFoundError as e:
        print(f"  Caught ToolNotFoundError: {e}")

    # ── 5. APIError — server error ───────────────────────────────────
    print("\n=== APIError ===")
    try:
        # This will fail if the tool isn't connected
        fastn.slack.send_message(channel="invalid", text="test")
    except APIError as e:
        print(f"  Caught APIError (status {e.status_code}): {e}")
    except AuthError as e:
        print(f"  Caught AuthError: {e}")

    # ── 6. Catch-all with FastnError ─────────────────────────────────
    print("\n=== FastnError (catch-all) ===")
    try:
        fastn.execute(action_id="act_invalid", params={})
    except FastnError as e:
        print(f"  Caught FastnError ({type(e).__name__}): {e}")

    # ── 7. Retry pattern ─────────────────────────────────────────────
    print("\n=== Retry pattern ===")
    import time

    max_retries = 3
    for attempt in range(1, max_retries + 1):
        try:
            result = fastn.slack.send_message(
                channel="general",
                text="Hello with retry!",
            )
            print(f"  Attempt {attempt}: Success — {result}")
            break
        except APIError as e:
            if attempt < max_retries:
                wait = 2 ** attempt
                print(f"  Attempt {attempt}: APIError, retrying in {wait}s...")
                time.sleep(wait)
            else:
                print(f"  Attempt {attempt}: Failed after {max_retries} retries: {e}")
        except AuthError:
            print("  Auth error — cannot retry, fix credentials first.")
            break

    fastn.close()


if __name__ == "__main__":
    main()
