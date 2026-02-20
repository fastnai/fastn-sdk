from __future__ import annotations

import copy
import json
from datetime import datetime, timezone
from typing import Any, Dict, List, Optional

import click

from fastn.cli import (
    cli,
    API_BASE_URL,
    COMMUNITY_CONNECTOR_ID,
    SOURCE_COMMUNITY,
    SOURCE_ORG,
    SOURCE_WORKSPACE,
)
from fastn.cli._helpers import (
    _ensure_fresh_token,
    _format_schema_properties,
    _to_snake_case,
    _verbose_post,
    _workspace_url,
)
from fastn.cli._registry import (
    _detect_languages,
    _extract_org_id,
    _fetch_connector_tools,
    _fetch_connectors_by_scope,
    _fetch_registry_list,
    _parse_tool_node,
    _regenerate_stubs,
)
from fastn.config import (
    add_connector_to_manifest,
    find_fastn_dir,
    get_installed_connectors,
    load_config,
    load_manifest,
    load_registry,
    remove_connector_from_manifest,
    save_manifest,
    save_registry,
)


@cli.command()
def sync() -> None:
    """Download/update the tool registry and refresh installed stubs."""
    config = load_config()
    if not config.auth_token and not config.api_key:
        raise click.ClickException("Not authenticated. Run `fastn login` first.")

    _ensure_fresh_token(config)

    click.echo("Syncing tool registry...")

    fastn_dir = find_fastn_dir()
    fastn_dir.mkdir(parents=True, exist_ok=True)

    # Capture old registry for breaking change detection
    old_registry = load_registry(fastn_dir)

    registry = _fetch_registry_list(config)
    save_registry(registry, fastn_dir)

    # Update manifest
    manifest = load_manifest(fastn_dir)
    manifest["registry_version"] = registry.get("version", "unknown")
    manifest["last_synced"] = datetime.now(timezone.utc).isoformat()
    save_manifest(manifest, fastn_dir)

    connector_count = len(registry.get("connectors", {}))
    click.echo(f"\u2713 Registry synced: {connector_count} tools available.")

    # Regenerate stubs for installed connectors (with breaking change detection)
    installed = get_installed_connectors(fastn_dir)
    if installed:
        languages = _detect_languages(fastn_dir)
        updated = False
        for lang in languages:
            result = _regenerate_stubs(
                fastn_dir, lang, old_registry=old_registry,
                _skip=not updated if updated else None,
            )
            updated = updated or result
        if updated:
            click.echo(f"\u2713 Refreshed stubs for {len(installed)} installed tool(s).")

    click.echo()
    click.echo("Run `fastn add <name>` to enable autocomplete for specific tools.")


@cli.command()
@click.argument("connectors", nargs=-1, required=True)
def add(connectors: tuple) -> None:
    """Download full type stubs for specific tools."""
    config = load_config()
    try:
        config.validate()
    except Exception as e:
        raise click.ClickException(str(e))

    _ensure_fresh_token(config)

    fastn_dir = find_fastn_dir()
    registry = load_registry(fastn_dir)

    # Capture old registry for breaking change detection
    old_registry = copy.deepcopy(registry)

    if not registry.get("connectors"):
        click.echo("Registry is empty. Running sync first...")
        registry = _fetch_registry_list(config)
        fastn_dir.mkdir(parents=True, exist_ok=True)
        save_registry(registry, fastn_dir)
        old_registry = {}  # No old data to compare against

    reg_connectors = registry.get("connectors", {})
    added_connectors: List[str] = []

    for connector_name in connectors:
        click.echo(f"Adding {connector_name}...")

        if connector_name not in reg_connectors:
            click.echo(f"  ✗ Tool '{connector_name}' not found in registry.")
            click.echo(f"    Run `fastn sync` to refresh, then try again.")
            continue

        connector_data = reg_connectors[connector_name]
        connector_id = connector_data.get("id", "")

        if not connector_id:
            click.echo(f"  ✗ No ID for '{connector_name}'. Run `fastn sync`.")
            continue

        # Fetch tools for this connector
        source = connector_data.get("source", SOURCE_COMMUNITY)
        click.echo(f"  Fetching tools for {connector_name}...")
        tool_nodes = _fetch_connector_tools(config, connector_id, source)
        tools = {}
        for node in tool_nodes:
            parsed = _parse_tool_node(node)
            tools[parsed["key"]] = parsed["data"]

        connector_data["tools"] = tools
        connector_data["tool_count"] = len(tools)
        save_registry(registry, fastn_dir)

        version = registry.get("version", "unknown")
        add_connector_to_manifest(connector_name, version, fastn_dir)
        added_connectors.append(connector_name)
        click.echo(f"  ✓ {connector_name} added ({len(tools)} tools).")

    # Regenerate stubs (with breaking change detection for re-added connectors)
    languages = _detect_languages(fastn_dir)
    updated = False
    for lang in languages:
        result = _regenerate_stubs(
            fastn_dir, lang, old_registry=old_registry,
            _skip=not updated if updated else None,
        )
        updated = updated or result
    if updated:
        click.echo("✓ Type stubs generated.")


@cli.command()
@click.argument("connector_name")
def remove(connector_name: str) -> None:
    """Remove tool stubs."""
    fastn_dir = find_fastn_dir()

    if remove_connector_from_manifest(connector_name, fastn_dir):
        # Remove stub files for detected languages only
        languages = _detect_languages(fastn_dir)
        for lang in languages:
            ext = "pyi" if lang == "python" else "d.ts"
            stub_file = fastn_dir / lang / "connectors" / f"{connector_name}.{ext}"
            if stub_file.exists():
                stub_file.unlink()

        for lang in languages:
            _regenerate_stubs(fastn_dir, lang)
        click.echo(f"\u2713 Removed {connector_name}.")
    else:
        click.echo(f"Tool '{connector_name}' is not installed.")


@cli.command(name="list")
@click.argument("connector_name", required=False, default=None)
@click.option("--active", is_flag=True, help="Show only active/enabled tools (workspace + org)")
@click.option("--installed", is_flag=True, help="Show only locally installed tools (fastn add)")
@click.option("-v", "--verbose", is_flag=True, help="Show input/output schemas for each tool")
def list_connectors(connector_name: Optional[str], active: bool, installed: bool, verbose: bool) -> None:
    """List tools, or show details for a specific one.

    \b
    Usage:
      fastn list              Show all available tools
      fastn list --active     Show only active/enabled tools
      fastn list --installed  Show only locally installed tools
      fastn list slack        Show actions for the 'slack' tool
      fastn list slack -v     Show actions with input/output schemas
    """
    fastn_dir = find_fastn_dir()
    registry = load_registry(fastn_dir)
    connectors = registry.get("connectors", {})

    if not connectors:
        # Auto-sync if registry is empty
        config = load_config()
        if not config.auth_token and not config.api_key:
            raise click.ClickException(
                "Not authenticated. Run `fastn login` first."
            )

        _ensure_fresh_token(config)

        click.echo("Syncing tool registry...")
        registry = _fetch_registry_list(config)
        fastn_dir.mkdir(parents=True, exist_ok=True)
        save_registry(registry, fastn_dir)

        # Update manifest
        manifest = load_manifest(fastn_dir)
        manifest["registry_version"] = registry.get("version", "unknown")
        manifest["last_synced"] = datetime.now(timezone.utc).isoformat()
        save_manifest(manifest, fastn_dir)

        connectors = registry.get("connectors", {})
        if not connectors:
            click.echo("No tools found in registry.")
            return

    # If a tool name is given, show its details (like `sdk list java`)
    if connector_name:
        config = load_config()
        if not config.auth_token and not config.api_key:
            raise click.ClickException("Not authenticated. Run `fastn login` first.")

        _ensure_fresh_token(config)

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

        # Check if tools are already cached in registry
        cached_tools = connector_data.get("tools", {})
        if cached_tools:
            tool_list = cached_tools
        else:
            source = connector_data.get("source", SOURCE_COMMUNITY)
            click.echo(f"Fetching tools for {connector_name}...")
            tool_nodes = _fetch_connector_tools(config, connector_id, source)
            tool_list = {}
            for node in tool_nodes:
                parsed = _parse_tool_node(node)
                tool_list[parsed["key"]] = parsed["data"]

            # Cache in registry
            connector_data["tools"] = tool_list
            connector_data["tool_count"] = len(tool_list)
            save_registry(registry, fastn_dir)

        display_name = connector_data.get("display_name", connector_name)
        click.echo()
        click.echo(f"  {display_name} ({len(tool_list)} tools):")
        click.echo()

        for key, tool in sorted(tool_list.items()):
            display_key = _to_snake_case(key) if key != _to_snake_case(key) else key
            usage = f"fastn.{connector_name}.{display_key}()"
            desc = tool.get("description", "")
            if verbose:
                click.echo(f"  {display_key}")
                click.echo(f"    Usage: {usage}")
                if desc:
                    click.echo(f"    {desc}")

                input_schema = tool.get("inputSchema", {})
                input_lines = _format_schema_properties(input_schema)
                if input_lines:
                    click.echo("    Input:")
                    for line in input_lines:
                        click.echo(line)

                output_schema = tool.get("outputSchema", {})
                output_lines = _format_schema_properties(output_schema)
                if output_lines:
                    click.echo("    Output:")
                    for line in output_lines:
                        click.echo(line)

                click.echo()
            else:
                if desc:
                    click.echo(f"    {display_key:<30} {desc}")
                else:
                    click.echo(f"    {display_key}")

        return

    # No tool name — list all tools
    installed_names = set(get_installed_connectors(fastn_dir))

    # --active: call getTools API with no prompt to get all enabled tools,
    # then fetch the workspace's selected connectors to include 0-tool entries.
    if active:
        config = load_config()
        if not config.auth_token and not config.api_key:
            raise click.ClickException("Not authenticated. Run `fastn login` first.")

        _ensure_fresh_token(config)

        headers = config.get_headers()
        workspace_id = config.resolve_project_id()

        # --- 1. Get all active/connected tools via the UCL getTools API ------
        active_payload: dict = {
            "input": {
                "agentId": workspace_id,
                "limit": 500,
            }
        }

        click.echo("Fetching active tools...")
        resp = _verbose_post(f"{API_BASE_URL}/getTools", headers, active_payload)

        if resp.status_code >= 400:
            raise click.ClickException(
                f"Failed to fetch active tools: {resp.status_code} {resp.text}"
            )

        data = resp.json()
        # Response is a plain array of tool objects
        tool_list = data if isinstance(data, list) else data.get("tools", data.get("data", []))
        if isinstance(tool_list, dict):
            tool_list = []

        # --- 2. Fetch selected connectors from the workspace ----------------
        # The UI's "Selected Tools" page shows connectors that are added to the
        # workspace's UCL.  We approximate this by re-fetching workspace and
        # org-scoped connectors, which includes both native connectors (flows,
        # test) and community connectors that have been selected.
        selected_connectors: dict = {}
        try:
            ws_selected = _fetch_connectors_by_scope(
                config, workspace_id, SOURCE_WORKSPACE
            )
            selected_connectors.update(ws_selected)
        except Exception:
            pass

        org_id = _extract_org_id(config)
        if org_id:
            try:
                org_selected = _fetch_connectors_by_scope(
                    config, org_id, SOURCE_ORG
                )
                for key, sdata in org_selected.items():
                    if key not in selected_connectors:
                        selected_connectors[key] = sdata
            except Exception:
                pass

        if not tool_list and not selected_connectors:
            app_url = _workspace_url(workspace_id)
            click.echo(f"No active tools. Enable tools at: {app_url}")
            return

        # --- 3. Build actionId → connector_name reverse lookup ---------------
        # The getTools API response doesn't include connector names — tools only
        # have actionId, type, and function.{name, description, parameters}.
        action_to_connector: Dict[str, str] = {}
        for cname, cdata in connectors.items():
            for _tkey, tinfo in cdata.get("tools", {}).items():
                aid = tinfo.get("actionId", "")
                if aid:
                    action_to_connector[aid] = cname

        # Collect the set of active actionIds that still need resolving
        active_action_ids = {
            t.get("actionId", "") for t in tool_list if t.get("actionId")
        }
        unresolved_ids = active_action_ids - set(action_to_connector.keys())

        # For connectors that haven't been `fastn add`-ed yet (tools dict is
        # empty), fetch their tool list so we can map actionIds.
        # Phase 1: workspace/org connectors (always fetched)
        # Phase 2: community connectors (only if unresolved IDs remain)
        unfetched_local = [
            (cname, cdata)
            for cname, cdata in connectors.items()
            if not cdata.get("tools")
            and cdata.get("id")
            and cdata.get("source") in (SOURCE_WORKSPACE, SOURCE_ORG)
        ]
        unfetched_community = [
            (cname, cdata)
            for cname, cdata in connectors.items()
            if not cdata.get("tools")
            and cdata.get("id")
            and cdata.get("source") == SOURCE_COMMUNITY
        ]

        registry_updated = False

        def _fetch_and_map(cname: str, cdata: dict) -> None:
            nonlocal registry_updated
            try:
                source = cdata.get("source", SOURCE_COMMUNITY)
                tool_nodes = _fetch_connector_tools(config, cdata["id"], source)
                tools_map: Dict[str, Any] = {}
                for node in tool_nodes:
                    parsed = _parse_tool_node(node)
                    aid = parsed["data"].get("actionId", "")
                    if aid:
                        action_to_connector[aid] = cname
                    tools_map[parsed["key"]] = parsed["data"]
                cdata["tools"] = tools_map
                cdata["tool_count"] = len(tools_map)
                registry_updated = True
            except Exception:
                pass  # Non-fatal — will show as "other"

        if unfetched_local or unresolved_ids:
            click.echo("  Resolving connector details...")

        # Always resolve workspace/org connectors
        for cname, cdata in unfetched_local:
            _fetch_and_map(cname, cdata)
            unresolved_ids -= set(action_to_connector.keys())

        # Resolve community connectors only while unresolved IDs remain.
        # Stop early once all active tools are mapped.
        if unresolved_ids:
            for cname, cdata in unfetched_community:
                if not unresolved_ids:
                    break
                _fetch_and_map(cname, cdata)
                unresolved_ids -= set(action_to_connector.keys())

        if registry_updated:
            save_registry(registry, fastn_dir)

        # --- 4. Group active tools by connector name -------------------------
        by_connector: dict = {}
        for tool in tool_list:
            action_id = tool.get("actionId", "")
            func = tool.get("function", {})
            tname = func.get("name", "") or action_id
            desc = func.get("description", "")

            # Look up connector name from our reverse map
            cname = action_to_connector.get(action_id, "")

            # Fallback: try matching by function name against cached registry
            if not cname:
                for reg_cname, cdata in connectors.items():
                    for _tkey, tinfo in cdata.get("tools", {}).items():
                        if tinfo.get("name") == tname or _tkey == _to_snake_case(tname):
                            cname = reg_cname
                            break
                    if cname:
                        break

            if not cname:
                cname = "other"

            by_connector.setdefault(cname, []).append({
                "name": tname,
                "description": desc,
                "actionId": action_id,
            })

        # --- 5. Include selected connectors with 0 active tools --------------
        # Workspace/org connectors that appear in searchDataSourceGroups but
        # have no tools in the getTools response are "selected but not connected"
        for cname, sdata in selected_connectors.items():
            if cname not in by_connector:
                by_connector[cname] = []
                # Merge display info into connectors dict so display names work
                if cname not in connectors:
                    connectors[cname] = sdata

        total_tools = len(tool_list)
        total_connectors = len(by_connector)
        click.echo()
        click.echo(f"  Active tools ({total_tools} actions across {total_connectors} connectors):")

        for cname in sorted(by_connector.keys()):
            tools_in_group = by_connector[cname]
            display = connectors.get(cname, {}).get("display_name", cname)
            marker = "\u2705" if cname.lower() in installed_names else "  "
            count_label = f"{len(tools_in_group)} actions"
            if not tools_in_group:
                count_label = "0 tools — not connected"
            click.echo()
            click.echo(f"  {marker} {display} ({count_label})")
            if verbose and tools_in_group:
                for t in sorted(tools_in_group, key=lambda x: x["name"]):
                    desc = t.get("description", "")
                    tname = _to_snake_case(t["name"]) if t["name"] else t["actionId"]
                    if desc:
                        click.echo(f"      {tname:<30} {desc}")
                    else:
                        click.echo(f"      {tname}")

        click.echo()
        app_url = _workspace_url(workspace_id)
        click.echo(f"  {total_connectors} connectors active. Manage at: {app_url}")
        click.echo(f"  Run `fastn add <name>` to enable autocomplete.")
        click.echo()
        return

    if installed and not installed_names:
        click.echo("No tools installed. Run `fastn add <name>` to install.")
        return

    if installed:
        items = [(k, v) for k, v in connectors.items() if k in installed_names]
        items.sort(key=lambda x: x[0])
        click.echo()
        click.echo(f"  Installed tools ({len(items)}):")
        click.echo()
        for name, data in items:
            click.echo(f"  \u2705 {name}")
        click.echo()
        click.echo(f"  {len(items)} installed. Run `fastn add <name>` to enable autocomplete.")
        click.echo()
        return

    # Group tools by source
    source_order = [
        (SOURCE_WORKSPACE, "My Workspace"),
        (SOURCE_ORG, "My Organization"),
        (SOURCE_COMMUNITY, "Marketplace"),
    ]

    click.echo()
    total = len(connectors)
    click.echo(f"  Available tools ({total}):")

    for source_key, source_label in source_order:
        group = [
            (k, v) for k, v in connectors.items()
            if v.get("source", SOURCE_COMMUNITY) == source_key
        ]
        if not group:
            continue

        group.sort(key=lambda x: x[0])

        click.echo()
        click.echo(f"  {source_label} ({len(group)}):")
        for name, data in group:
            marker = "\u2705" if name in installed_names else "  "
            ctype = data.get("connector_type", "GROUP")
            if ctype == "DATABASE":
                type_label = " [database]"
            elif ctype and ctype != "GROUP":
                type_label = f" [{ctype.lower()}]"
            else:
                type_label = ""
            click.echo(f"    {marker} {name}{type_label}")

    click.echo()
    installed_count = len(installed_names)
    click.echo(f"  {installed_count} installed. Run `fastn add <name>` to enable autocomplete.")
    click.echo()
