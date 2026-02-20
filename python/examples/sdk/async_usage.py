"""Async Fastn SDK usage — non-blocking tool calls with AsyncFastnClient.

Demonstrates the async client for high-throughput scenarios where you
need to call multiple tools concurrently.

Update the credentials below and run:
    python examples/async_usage.py
"""

import asyncio

from fastn import AsyncFastnClient

# --- Configuration (update these) ----------------------------------------
API_KEY = "your-api-key"
PROJECT_ID = "your-project-id"
# --------------------------------------------------------------------------


async def main() -> None:
    async with AsyncFastnClient(
        api_key=API_KEY,
        project_id=PROJECT_ID,
    ) as fastn:
        # ── Single call ──────────────────────────────────────────────
        result = await fastn.slack.send_message(
            channel="general",
            text="Hello from async SDK!",
        )
        print("Single call:", result)

        # ── Concurrent calls ─────────────────────────────────────────
        results = await asyncio.gather(
            fastn.slack.send_message(channel="general", text="Message 1"),
            fastn.slack.send_message(channel="random", text="Message 2"),
            fastn.slack.list_channels(),
        )
        for i, r in enumerate(results, 1):
            print(f"Concurrent call {i}:", r)

        # ── With connection_id ───────────────────────────────────────
        result = await fastn.slack.send_message(
            connection_id="conn_workspace_b",
            channel="general",
            text="From another workspace",
        )
        print("Connection override:", result)

        # ── execute() — raw action_id call ───────────────────────────
        result = await fastn.execute(
            action_id="act_slack_send_message",
            params={"channel": "general", "text": "Via execute()"},
        )
        print("Execute:", result)


if __name__ == "__main__":
    asyncio.run(main())
