"""Agent API examples — LLM tool-use workflows with Fastn.

Covers:
  1. LLM agent (OpenAI)    — single-turn function calling
  2. LLM agent (Anthropic) — single-turn Claude tool use
  3. LLM agent (Gemini)    — single-turn Google function calling
  4. Bedrock agent          — AWS Bedrock Converse API tool use
  5. Multi-step agent       — agentic loop chaining multiple tool calls

Update the credentials below and run:
    python examples/sdk/agents.py
"""

from __future__ import annotations

import json

from fastn import FastnClient

# --- Configuration (update these) ----------------------------------------
API_KEY = "your-api-key"
PROJECT_ID = "your-project-id"
CONNECTOR = "slack"
PROMPT = "Send 'Hello from AI agent!' to #general-test on Slack"
# --------------------------------------------------------------------------


# ===================================================================
# 1. OpenAI function-calling
# ===================================================================

def openai_agent() -> None:
    """Describe what you need -> Fastn discovers tools -> OpenAI calls them."""
    print("\n" + "=" * 60)
    print("1. OPENAI AGENT")
    print("=" * 60)

    fastn = FastnClient(api_key=API_KEY, project_id=PROJECT_ID)

    # Describe what you need — Fastn finds the right tools
    tools = fastn.get_tools_for(PROMPT, format="openai")
    print(f"Got {len(tools)} tools in OpenAI format\n")

    try:
        import openai
    except ImportError:
        print("openai not installed. Run: pip install openai")
        print("\nTool format preview:")
        print(json.dumps(tools[:2], indent=2))
        fastn.close()
        return

    client = openai.OpenAI()
    response = client.chat.completions.create(
        model="gpt-4o",
        messages=[{"role": "user", "content": PROMPT}],
        tools=tools,
    )

    choice = response.choices[0]
    if choice.message.tool_calls:
        for tool_call in choice.message.tool_calls:
            print(f"LLM calls: {tool_call.function.name}")
            print(f"Arguments: {tool_call.function.arguments}")
            result = fastn.execute(
                tool=tool_call.function.name,
                params=json.loads(tool_call.function.arguments),
            )
            print(f"Result: {result}")
    else:
        print("LLM did not make a tool call:", choice.message.content)

    fastn.close()


# ===================================================================
# 2. Anthropic Claude tool use
# ===================================================================

def anthropic_agent() -> None:
    """Describe what you need -> Fastn discovers tools -> Claude calls them."""
    print("\n" + "=" * 60)
    print("2. ANTHROPIC AGENT")
    print("=" * 60)

    fastn = FastnClient(api_key=API_KEY, project_id=PROJECT_ID)

    tools = fastn.get_tools_for(PROMPT, format="anthropic")
    print(f"Got {len(tools)} tools in Anthropic format\n")

    try:
        import anthropic
    except ImportError:
        print("anthropic not installed. Run: pip install anthropic")
        print("\nTool format preview:")
        print(json.dumps(tools[:2], indent=2))
        fastn.close()
        return

    client = anthropic.Anthropic()
    response = client.messages.create(
        model="claude-sonnet-4-20250514",
        max_tokens=1024,
        messages=[{"role": "user", "content": PROMPT}],
        tools=tools,
    )

    for block in response.content:
        if block.type == "tool_use":
            print(f"Claude calls: {block.name}")
            print(f"Input: {block.input}")
            result = fastn.execute(tool=block.name, params=block.input)
            print(f"Result: {result}")

    fastn.close()


# ===================================================================
# 3. Google Gemini function calling
# ===================================================================

def gemini_agent() -> None:
    """Describe what you need -> Fastn discovers tools -> Gemini calls them."""
    print("\n" + "=" * 60)
    print("3. GEMINI AGENT")
    print("=" * 60)

    fastn = FastnClient(api_key=API_KEY, project_id=PROJECT_ID)

    tools = fastn.get_tools_for(PROMPT, format="gemini")
    print(f"Got {len(tools)} tools in Gemini format\n")

    try:
        from google import genai
    except ImportError:
        print("google-genai not installed. Run: pip install google-genai")
        print("\nTool format preview:")
        print(json.dumps(tools[:2], indent=2))
        fastn.close()
        return

    client = genai.Client()
    response = client.models.generate_content(
        model="gemini-2.0-flash",
        contents=PROMPT,
        config=genai.types.GenerateContentConfig(tools=tools),
    )

    for part in response.candidates[0].content.parts:
        if fn := part.function_call:
            print(f"Gemini calls: {fn.name}")
            print(f"Args: {dict(fn.args)}")
            result = fastn.execute(tool=fn.name, params=dict(fn.args))
            print(f"Result: {result}")

    fastn.close()


# ===================================================================
# 4. AWS Bedrock Converse API
# ===================================================================

def bedrock_agent() -> None:
    """Fastn tools with AWS Bedrock's Converse API.

    Prerequisites:
        pip install boto3 fastn
        # AWS credentials configured via aws configure or environment variables
    """
    print("\n" + "=" * 60)
    print("4. BEDROCK AGENT")
    print("=" * 60)

    fastn = FastnClient(api_key=API_KEY, project_id=PROJECT_ID)
    model_id = "anthropic.claude-3-5-sonnet-20241022-v2:0"

    # Get tools in Bedrock format
    tools = fastn.get_tools_for(CONNECTOR, format="bedrock")
    print(f"Got {len(tools)} tools in Bedrock format")
    print(f"Tool config preview: {json.dumps(tools[0], indent=2)[:200]}...")

    try:
        import boto3
    except ImportError:
        print("\nboto3 not installed. Run: pip install boto3")
        print("Showing tool format only.")
        print(json.dumps(tools[:2], indent=2))
        fastn.close()
        return

    bedrock = boto3.client("bedrock-runtime", region_name="us-east-1")

    response = bedrock.converse(
        modelId=model_id,
        messages=[{"role": "user", "content": [{"text": PROMPT}]}],
        toolConfig={"tools": tools},
    )

    output = response["output"]["message"]
    for block in output["content"]:
        if "toolUse" in block:
            tool_use = block["toolUse"]
            tool_name = tool_use["name"]
            tool_input = tool_use["input"]

            print(f"\nBedrock calls: {tool_name}")
            print(f"Input: {json.dumps(tool_input, indent=2)}")

            result = fastn.execute(
                tool=tool_name,
                params=tool_input,
            )
            print(f"Result: {json.dumps(result, indent=2)}")
        elif "text" in block:
            print(f"\nModel response: {block['text']}")

    fastn.close()


# ===================================================================
# 5. Multi-step agentic loop
# ===================================================================

def multi_step_agent() -> None:
    """Chain multiple tool calls in an agentic loop.

    This is the programmatic equivalent of `fastn agent`, giving you
    full control over the loop and decision logic.
    """
    print("\n" + "=" * 60)
    print("5. MULTI-STEP AGENT")
    print("=" * 60)

    fastn = FastnClient(api_key=API_KEY, project_id=PROJECT_ID)

    # Get tools in OpenAI format
    tools = fastn.get_tools_for("slack", format="openai")
    print(f"Available tools: {[t['function']['name'] for t in tools]}")

    try:
        import openai
    except ImportError:
        print("\nopenai not installed. Run: pip install openai")
        print("Showing manual multi-step example instead.\n")
        _manual_multi_step(fastn)
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

    # Agentic loop
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
            print(f"\nAgent: {choice.message.content}")
            break

        messages.append(choice.message)

        for tool_call in choice.message.tool_calls:
            fn_name = tool_call.function.name
            fn_args = json.loads(tool_call.function.arguments)

            print(f"  Tool: {fn_name}({json.dumps(fn_args)})")

            try:
                result = fastn.execute(
                    tool=fn_name,
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


def _manual_multi_step(fastn: FastnClient) -> None:
    """Demonstrate manual multi-step without LLM."""
    # Step 1: List channels
    print("Step 1: Listing Slack channels...")
    try:
        channels = fastn.slack.get_channels()
        print(f"  Found channels: {json.dumps(channels)[:200]}")
    except Exception as e:
        print(f"  Error: {e}")
        return

    # Step 2: Send message
    print("\nStep 2: Sending message to #general...")
    try:
        result = fastn.slack.send_message(
            channel="general",
            text="Hello from multi-step agent!",
        )
        print(f"  Result: {json.dumps(result)}")
    except Exception as e:
        print(f"  Error: {e}")


# ===================================================================
# Main
# ===================================================================

if __name__ == "__main__":
    # Uncomment the example you want to run:
    openai_agent()
    # anthropic_agent()
    # gemini_agent()
    # bedrock_agent()
    # multi_step_agent()
