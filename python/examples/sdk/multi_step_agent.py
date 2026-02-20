"""Multi-step agent workflow — chain multiple tool calls in sequence.

Demonstrates how to build a manual agentic loop that chains tool calls:
    1. Search/list resources
    2. Use the result to make a follow-up action
    3. Handle errors gracefully

This is the programmatic equivalent of `fastn agent`, giving you full
control over the loop and decision logic.

Update the credentials below and run:
    python examples/multi_step_agent.py
"""

import json

from fastn import FastnClient

# --- Configuration (update these) ----------------------------------------
API_KEY = "your-api-key"
PROJECT_ID = "your-project-id"
# --------------------------------------------------------------------------


def main() -> None:
    fastn = FastnClient(api_key=API_KEY, project_id=PROJECT_ID)

    # ── Step 1: Get tools in OpenAI format ───────────────────────────
    tools = fastn.get_tools_for("slack", format="openai")
    print(f"Available tools: {[t['function']['name'] for t in tools]}")

    # ── Step 2: Build messages for OpenAI ────────────────────────────
    try:
        import openai
    except ImportError:
        print("\nopenai not installed. Run: pip install openai")
        print("Showing manual multi-step example instead.\n")
        _manual_example(fastn)
        return

    client = openai.OpenAI()
    messages = [
        {"role": "system", "content": (
            "You are a helpful assistant. Use the available tools to "
            "accomplish the user's request. You may need to call multiple "
            "tools in sequence."
        )},
        {"role": "user", "content": (
            "Find the #general channel on Slack and send 'Hello from "
            "multi-step agent!' to it."
        )},
    ]

    # ── Step 3: Agentic loop ─────────────────────────────────────────
    max_turns = 5
    for turn in range(max_turns):
        print(f"\n--- Turn {turn + 1} ---")

        response = client.chat.completions.create(
            model="gpt-4o",
            messages=messages,
            tools=tools,
        )

        choice = response.choices[0]

        if not choice.message.tool_calls:
            # LLM is done — print final response
            print(f"\nAgent: {choice.message.content}")
            break

        # Process each tool call
        messages.append(choice.message)

        for tool_call in choice.message.tool_calls:
            fn_name = tool_call.function.name
            fn_args = json.loads(tool_call.function.arguments)

            print(f"  Tool: {fn_name}({json.dumps(fn_args)})")

            try:
                result = fastn.execute(
                    action_id=fn_name,
                    params=fn_args,
                )
                print(f"  Result: {json.dumps(result)[:200]}")
            except Exception as e:
                result = {"error": str(e)}
                print(f"  Error: {e}")

            messages.append({
                "role": "tool",
                "tool_call_id": tool_call.id,
                "content": json.dumps(result, default=str),
            })
    else:
        print(f"\nReached max turns ({max_turns})")

    fastn.close()


def _manual_example(fastn: FastnClient) -> None:
    """Demonstrate manual multi-step without LLM."""
    # Step 1: List channels
    print("Step 1: Listing Slack channels...")
    try:
        channels = fastn.slack.list_channels()
        print(f"  Found channels: {json.dumps(channels)[:200]}")
    except Exception as e:
        print(f"  Error: {e}")
        return

    # Step 2: Send message (using channel name directly)
    print("\nStep 2: Sending message to #general...")
    try:
        result = fastn.slack.send_message(
            channel="general",
            text="Hello from multi-step agent!",
        )
        print(f"  Result: {json.dumps(result)}")
    except Exception as e:
        print(f"  Error: {e}")


if __name__ == "__main__":
    main()
