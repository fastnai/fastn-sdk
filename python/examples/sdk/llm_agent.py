"""LLM agent integration — describe what you need, get tools, execute.

Demonstrates the full agent workflow:
    1. Describe what you need — Fastn discovers the right tools
    2. Send tools + user prompt to the LLM
    3. Execute the LLM's tool call via fastn.execute()

Update the credentials below and run:
    python examples/sdk/llm_agent.py
"""

import json

from fastn import FastnClient

# --- Configuration (update these) ----------------------------------------
API_KEY = "your-api-key"
PROJECT_ID = "your-project-id"
PROMPT = "Send 'Hello from AI agent!' to #general on Slack"
# --------------------------------------------------------------------------


def openai_example(fastn: FastnClient) -> None:
    """OpenAI function-calling workflow."""
    # Describe what you need — Fastn finds the right tools
    tools = fastn.get_tools_for(PROMPT, format="openai")
    print(f"Got {len(tools)} tools in OpenAI format\n")

    try:
        import openai
    except ImportError:
        print("openai not installed. Run: pip install openai")
        print("\nTool format preview:")
        print(json.dumps(tools[:2], indent=2))
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
                action_id=tool_call.function.name,
                params=json.loads(tool_call.function.arguments),
            )
            print(f"Result: {result}")
    else:
        print("LLM did not make a tool call:", choice.message.content)


def anthropic_example(fastn: FastnClient) -> None:
    """Anthropic Claude tool-use workflow."""
    tools = fastn.get_tools_for(PROMPT, format="anthropic")
    print(f"Got {len(tools)} tools in Anthropic format\n")

    try:
        import anthropic
    except ImportError:
        print("anthropic not installed. Run: pip install anthropic")
        print("\nTool format preview:")
        print(json.dumps(tools[:2], indent=2))
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
            result = fastn.execute(action_id=block.name, params=block.input)
            print(f"Result: {result}")


def gemini_example(fastn: FastnClient) -> None:
    """Google Gemini function-calling workflow."""
    tools = fastn.get_tools_for(PROMPT, format="gemini")
    print(f"Got {len(tools)} tools in Gemini format\n")

    try:
        from google import genai
    except ImportError:
        print("google-genai not installed. Run: pip install google-genai")
        print("\nTool format preview:")
        print(json.dumps(tools[:2], indent=2))
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
            result = fastn.execute(action_id=fn.name, params=dict(fn.args))
            print(f"Result: {result}")


def main() -> None:
    fastn = FastnClient(
        api_key=API_KEY,
        project_id=PROJECT_ID,
    )

    # Uncomment the provider you want to test:
    openai_example(fastn)
    # anthropic_example(fastn)
    # gemini_example(fastn)


if __name__ == "__main__":
    main()
