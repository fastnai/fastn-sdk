from __future__ import annotations

import json
from typing import Optional

import click

from fastn import __version__
from fastn.cli import cli, EXECUTE_URL, SOURCE_COMMUNITY
from fastn.cli._helpers import (
    _ensure_fresh_token,
    _extract_input_fields,
    _handle_execute_error,
    _parse_extra_args,
    _prompt_for_params,
    _to_snake_case,
    _verbose_post,
)
from fastn.cli._registry import _fetch_connector_tools, _parse_tool_node
from fastn.config import find_fastn_dir, load_config, load_manifest, load_registry, save_registry


@cli.command(
    context_settings=dict(
        ignore_unknown_options=True,
        allow_extra_args=True,
    ),
)
@click.argument("connector_name")
@click.argument("action_name", required=False, default=None)
@click.argument("tenant_id", required=False, default=None)
@click.option("--connection-id", default=None, help="Connection ID for multi-connection tools")
@click.option("--tenant", default=None, help="Tenant ID (overrides config)")
@click.pass_context
def run(ctx: click.Context, connector_name: str, action_name: Optional[str], tenant_id: Optional[str], connection_id: Optional[str], tenant: Optional[str]) -> None:
    """Execute a tool action directly from the command line.

    \b
    Usage:
      fastn run <tool>                              Show available actions
      fastn run <tool> <action> [--key value]        Execute with inline params
      fastn run <tool> <action> <tenant_id>          Execute for a specific tenant
      fastn run <tool> <action>                      Execute with interactive prompts

    \b
    Examples:
      fastn run slack                                Show available Slack actions
      fastn run slack send_message --channel general --text "Hello!"
      fastn run slack send_message 3ab9d640-...      Execute as specific tenant
      fastn run slack send_message             Prompts for each field
      fastn run flows my_flow --input '{"key": "value"}'
    """
    config = load_config()
    if not config.auth_token and not config.api_key:
        raise click.ClickException("Not authenticated. Run `fastn login` first.")

    _ensure_fresh_token(config)

    fastn_dir = find_fastn_dir()
    registry = load_registry(fastn_dir)
    connectors = registry.get("connectors", {})

    if not connectors:
        raise click.ClickException(
            "Registry is empty. Run `fastn sync` first."
        )

    if connector_name not in connectors:
        raise click.ClickException(
            f"Tool '{connector_name}' not found. Run `fastn list` to see available tools."
        )

    connector_data = connectors[connector_name]
    connector_id = connector_data.get("id", "")

    if not connector_id:
        raise click.ClickException(
            f"No ID for '{connector_name}'. Run `fastn sync`."
        )

    # Ensure tools are loaded
    tools = connector_data.get("tools", {})
    if not tools:
        source = connector_data.get("source", SOURCE_COMMUNITY)
        click.echo(f"Fetching tools for {connector_name}...")
        tool_nodes = _fetch_connector_tools(config, connector_id, source)
        tools = {}
        for node in tool_nodes:
            parsed = _parse_tool_node(node)
            tools[parsed["key"]] = parsed["data"]

        connector_data["tools"] = tools
        connector_data["tool_count"] = len(tools)
        save_registry(registry, fastn_dir)

    # If no action given, list available actions
    if not action_name:
        display_name = connector_data.get("display_name", connector_name)
        click.echo()
        click.echo(f"  {display_name} — available actions:")
        click.echo()
        for key in sorted(tools.keys()):
            tdata = tools[key]
            display_key = _to_snake_case(key)
            desc = tdata.get("description", "")
            if desc:
                click.echo(f"    {display_key:<30} {desc}")
            else:
                click.echo(f"    {display_key}")
        click.echo()
        click.echo(f"  Run: fastn run {connector_name} <action> [--key value ...]")
        click.echo()
        return

    # Resolve the action
    tool_info = tools.get(action_name)
    # Fallback: try without underscores (send_message -> sendmessage)
    if tool_info is None and "_" in action_name:
        tool_info = tools.get(action_name.replace("_", ""))
    if tool_info is None:
        available = ", ".join(
            _to_snake_case(k) for k in sorted(tools.keys())
        )
        raise click.ClickException(
            f"Action '{action_name}' not found in '{connector_name}'. "
            f"Available: {available}"
        )

    action_id = tool_info.get("actionId", "")
    if not action_id:
        raise click.ClickException(
            f"No actionId for '{action_name}'. Run `fastn sync` and `fastn add {connector_name}`."
        )

    # Extract input fields from schema for interactive prompting
    input_schema = tool_info.get("inputSchema", {})
    _pk, fields, required_fields = _extract_input_fields(input_schema)

    # Parse extra --key value args into params
    params = _parse_extra_args(ctx.args)

    # If no args were passed and there are fields, prompt interactively
    if not params and fields:
        desc = tool_info.get("description", "")
        click.echo()
        click.echo(f"  {connector_name}.{action_name}")
        if desc:
            click.echo(f"  {desc}")
        params = _prompt_for_params(fields, required_fields)

    # Build execute payload — dynamically route params based on the schema
    from fastn.client import _build_params_from_schema

    workspace_id = config.resolve_project_id()
    parameters = _build_params_from_schema(tool_info, params)
    payload: dict = {
        "input": {
            "actionId": action_id,
            "connectorId": connector_id,
            "agentId": workspace_id,
            "toolName": action_name,
            "parameters": parameters,
        }
    }
    if connection_id:
        payload["input"]["connectionId"] = connection_id

    effective_tenant = tenant_id or tenant
    if effective_tenant:
        config.tenant_id = effective_tenant
    headers = config.get_headers()

    click.echo()
    click.echo(f"Running {connector_name}.{action_name}...")
    resp = _verbose_post(EXECUTE_URL, headers, payload)

    _handle_execute_error(resp, f"{connector_name}.{action_name}", workspace_id)

    data = resp.json()
    # Unwrap: API returns {body, statusCode, rawBody} — show the body
    if isinstance(data, dict) and "body" in data:
        result = data["body"]
    else:
        result = data

    click.echo(json.dumps(result, indent=2))


@cli.command()
@click.argument("connector_name")
@click.argument("tool_name", required=False, default=None)
def schema(connector_name: str, tool_name: Optional[str]) -> None:
    """Show raw JSON schema for a tool's actions.

    \b
    Usage:
      fastn schema slack                  Show schemas for all Slack actions
      fastn schema slack send_message     Show schema for a specific action
    """
    fastn_dir = find_fastn_dir()
    registry = load_registry(fastn_dir)
    connectors = registry.get("connectors", {})

    if connector_name not in connectors:
        raise click.ClickException(
            f"Tool '{connector_name}' not found. Run `fastn add {connector_name}` first."
        )

    connector_data = connectors[connector_name]
    tools = connector_data.get("tools", {})

    if not tools:
        raise click.ClickException(
            f"No tools cached for '{connector_name}'. Run `fastn add {connector_name}` first."
        )

    if tool_name:
        tool = tools.get(tool_name)
        # Fallback: try without underscores (send_message -> sendmessage)
        if tool is None and "_" in tool_name:
            tool = tools.get(tool_name.replace("_", ""))
        if tool is None:
            available = ", ".join(
                _to_snake_case(k) for k in sorted(tools.keys())
            )
            raise click.ClickException(
                f"Tool '{tool_name}' not found in {connector_name}. Available: {available}"
            )
        output = {
            "name": tool_name,
            "description": tool.get("description", ""),
            "actionId": tool.get("actionId", ""),
            "inputSchema": tool.get("inputSchema", {}),
            "outputSchema": tool.get("outputSchema", {}),
        }
        click.echo(json.dumps(output, indent=2))
    else:
        output = []
        for name, tool in sorted(tools.items()):
            output.append({
                "name": _to_snake_case(name),
                "description": tool.get("description", ""),
                "actionId": tool.get("actionId", ""),
                "inputSchema": tool.get("inputSchema", {}),
                "outputSchema": tool.get("outputSchema", {}),
            })
        click.echo(json.dumps(output, indent=2))


@cli.command()
def version() -> None:
    """Show SDK and registry version."""
    fastn_dir = find_fastn_dir()
    manifest = load_manifest(fastn_dir)

    click.echo(f"Fastn SDK v{__version__}")
    reg_version = manifest.get("registry_version", "not synced")
    click.echo(f"Registry version: {reg_version}")
    last_synced = manifest.get("last_synced", "never")
    click.echo(f"Last synced: {last_synced}")
