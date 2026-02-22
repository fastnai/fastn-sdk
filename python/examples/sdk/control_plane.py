"""Control plane — inspect connectors, tools, and schemas programmatically.

Demonstrates the connectors API for introspecting the connector registry without
making any tool calls.

Update the credentials below and run:
    python examples/control_plane.py
"""

import json

from fastn import FastnClient

# --- Configuration (update these) ----------------------------------------
API_KEY = "your-api-key"
PROJECT_ID = "your-project-id"
CONNECTOR = "slack"           # connector to inspect
# --------------------------------------------------------------------------


def main() -> None:
    fastn = FastnClient(api_key=API_KEY, project_id=PROJECT_ID)

    # -- 1. List all connectors --------------------------------------------
    print("=== All Connectors ===")
    connectors = fastn.connectors.list()
    for c in connectors:
        tool_count = c.get("tool_count", len(c.get("tools", {})))
        print(f"  {c['name']:<25} {tool_count} tools")

    # -- 2. Get a specific connector ---------------------------------------
    print(f"\n=== Connector: {CONNECTOR} ===")
    connector = fastn.connectors.get(CONNECTOR)
    print(f"  Name: {connector['name']}")
    print(f"  Display: {connector.get('display_name', connector['name'])}")
    print(f"  Tools: {len(connector.get('tools', {}))}")

    # -- 3. List tools for a connector -------------------------------------
    print(f"\n=== Tools in {CONNECTOR} ===")
    tools = fastn.get_tools(CONNECTOR)
    for tool in tools:
        print(f"  {tool['name']:<30} {tool.get('description', '')}")

    # -- 4. Get a specific tool's schema -----------------------------------
    if tools:
        tool_name = tools[0]["name"]
        print(f"\n=== Schema: {CONNECTOR}.{tool_name} ===")
        tool = fastn.get_tool(CONNECTOR, tool_name)
        print(f"  actionId: {tool['actionId']}")
        print(f"  inputSchema:")
        print(json.dumps(tool.get("inputSchema", {}), indent=4))

    # -- 5. Get tools in LLM format ----------------------------------------
    print(f"\n=== OpenAI format ===")
    openai_tools = fastn.get_tools_for("slack tools", connector=CONNECTOR, format="openai")
    print(f"  {len(openai_tools)} tools ready for OpenAI function calling")
    if openai_tools:
        print(f"  First tool: {openai_tools[0]['function']['name']}")

    print(f"\n=== Anthropic format ===")
    anthropic_tools = fastn.get_tools_for("slack tools", connector=CONNECTOR, format="anthropic")
    print(f"  {len(anthropic_tools)} tools ready for Claude tool use")

    print(f"\n=== Gemini format ===")
    gemini_tools = fastn.get_tools_for("slack tools", connector=CONNECTOR, format="gemini")
    print(f"  {len(gemini_tools)} tools ready for Gemini function calling")

    print(f"\n=== Bedrock format ===")
    bedrock_tools = fastn.get_tools_for("slack tools", connector=CONNECTOR, format="bedrock")
    print(f"  {len(bedrock_tools)} tools ready for AWS Bedrock")

    print(f"\n=== Raw format ===")
    raw_tools = fastn.get_tools_for("slack tools", connector=CONNECTOR, format="raw")
    print(f"  {len(raw_tools)} tools with raw schemas + actionIds")

    fastn.close()


if __name__ == "__main__":
    main()
