"""AWS Bedrock agent integration — tool use with Converse API.

Demonstrates how to use Fastn tools with AWS Bedrock's Converse API,
which provides a unified interface for tool use across models like
Claude, Llama, and Mistral on AWS.

Prerequisites:
    pip install boto3 fastn
    # AWS credentials configured via aws configure or environment variables

Update the credentials below and run:
    python examples/bedrock_agent.py
"""

import json

from fastn import FastnClient

# --- Configuration (update these) ----------------------------------------
API_KEY = "your-api-key"
PROJECT_ID = "your-project-id"
CONNECTOR = "slack"
PROMPT = "Send 'Hello from Bedrock!' to #general on Slack"
MODEL_ID = "anthropic.claude-3-5-sonnet-20241022-v2:0"
# --------------------------------------------------------------------------


def main() -> None:
    fastn = FastnClient(api_key=API_KEY, project_id=PROJECT_ID)

    # ── 1. Get tools in Bedrock format ───────────────────────────────
    tools = fastn.get_tools_for(CONNECTOR, format="bedrock")
    print(f"Got {len(tools)} tools in Bedrock format")
    print(f"Tool config preview: {json.dumps(tools[0], indent=2)[:200]}...")

    # ── 2. Call Bedrock Converse API ─────────────────────────────────
    try:
        import boto3
    except ImportError:
        print("\nboto3 not installed. Run: pip install boto3")
        print("Showing tool format only.")
        print(json.dumps(tools[:2], indent=2))
        return

    bedrock = boto3.client("bedrock-runtime", region_name="us-east-1")

    response = bedrock.converse(
        modelId=MODEL_ID,
        messages=[{"role": "user", "content": [{"text": PROMPT}]}],
        toolConfig={"tools": tools},
    )

    # ── 3. Process tool use ──────────────────────────────────────────
    output = response["output"]["message"]
    for block in output["content"]:
        if "toolUse" in block:
            tool_use = block["toolUse"]
            tool_name = tool_use["name"]
            tool_input = tool_use["input"]

            print(f"\nBedrock calls: {tool_name}")
            print(f"Input: {json.dumps(tool_input, indent=2)}")

            # ── 4. Execute via Fastn ─────────────────────────────────
            result = fastn.execute(
                action_id=tool_name,
                params=tool_input,
            )
            print(f"Result: {json.dumps(result, indent=2)}")
        elif "text" in block:
            print(f"\nModel response: {block['text']}")

    fastn.close()


if __name__ == "__main__":
    main()
