"""Fastn CLI — init, login, logout, whoami, sync, add, remove, list, schema, version.

Provides the ``fastn`` command-line interface for managing
SDK configuration, connector registry, and type stubs.

Commands:
    fastn init              Interactive setup — prompts for API key + project ID.
    fastn login             Authenticate via browser (OAuth device flow).
    fastn logout            Clear stored authentication tokens.
    fastn whoami            Show current authenticated user.
    fastn sync              Download/update the connector registry from the API.
    fastn add <name> [...]  Generate typed .pyi stubs for IDE autocomplete.
    fastn remove <name>     Remove connector stubs.
    fastn list              Show all available connectors.
    fastn list -v           Show connectors with tool details.
    fastn schema <c> <t>    Print input/output schema for a tool.
    fastn version           Show SDK and registry versions.

The CLI entry point is registered in pyproject.toml:
    [project.scripts]
    fastn = "fastn.cli:main"
"""

from __future__ import annotations

import json
import sys
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Dict, List, Optional

import click
import httpx

from fastn import __version__
from fastn.auth import mask_key

API_BASE_URL = "https://live.fastn.ai/api/ucl"
from fastn.config import (
    DEFAULT_STAGE,
    FASTN_DIR,
    FastnConfig,
    add_connector_to_manifest,
    ensure_gitignore,
    find_fastn_dir,
    get_installed_connectors,
    load_config,
    load_manifest,
    load_migrations,
    load_registry,
    remove_connector_from_manifest,
    save_config,
    save_manifest,
    save_migrations,
    save_registry,
)


# Import the generator (it lives in the sibling generator package)
# At runtime, we add the parent dir to path so the generator is importable
_SDK_ROOT = Path(__file__).resolve().parent.parent.parent
if str(_SDK_ROOT) not in sys.path:
    sys.path.insert(0, str(_SDK_ROOT))

try:
    from generator.generate import StubGenerator, parse_registry
    from generator.diff import (
        build_migrations,
        compute_schema_hash,
        diff_registries,
        merge_migrations,
    )
except ImportError:
    # If generator is not available (e.g. installed via pip without generator),
    # stub generation and diff detection will be skipped
    StubGenerator = None  # type: ignore[assignment,misc]
    parse_registry = None  # type: ignore[assignment]
    compute_schema_hash = None  # type: ignore[assignment]
    diff_registries = None  # type: ignore[assignment]
    build_migrations = None  # type: ignore[assignment]
    merge_migrations = None  # type: ignore[assignment]


def _to_snake_case(name: str) -> str:
    """Convert a camelCase or PascalCase name to snake_case.

    Examples:
        sendMessage   -> send_message
        SendMessage   -> send_message
        getUsers      -> get_users
        getUserByEmail -> get_user_by_email
        testauth      -> testauth  (no-op for already lowercase)
    """
    import re
    # Insert underscore before uppercase letters that follow a lowercase letter or digit
    s = re.sub(r"([a-z0-9])([A-Z])", r"\1_\2", name)
    # Insert underscore before uppercase letters followed by lowercase (for runs of caps)
    s = re.sub(r"([A-Z]+)([A-Z][a-z])", r"\1_\2", s)
    # Replace spaces and hyphens with underscores
    s = s.replace(" ", "_").replace("-", "_")
    return s.lower()


GRAPHQL_URL = "https://live.fastn.ai/api/graphql"

SEARCH_CONNECTORS_QUERY = """
query searchDataSourceGroups($input: SearchDataModelInput!) {
  searchDataSourceGroups(input: $input) {
    pageInfo {
      totalCount
    }
    edges {
      node {
        id
        clientId
        name
      }
    }
  }
}
"""

CONNECTOR_TOOLS_QUERY = """
query callCoreProjectFlow($input: CoreProjectFlowProxyInput!) {
  callCoreProjectFlow(input: $input) {
    data
    statusCode
    message
  }
}
"""


COMMUNITY_CONNECTOR_ID = "community"


def _ensure_fresh_token(config: FastnConfig) -> None:
    """Auto-refresh the access token if it has expired.

    Mutates *config* in place and persists the new tokens to disk.
    """
    from fastn.oauth import is_token_expired

    if not config.refresh_token or not is_token_expired(config.token_expiry):
        return

    from fastn.oauth import compute_token_expiry, refresh_access_token

    try:
        tokens = refresh_access_token(config.refresh_token)
        config.auth_token = tokens.access_token
        config.refresh_token = tokens.refresh_token
        config.token_expiry = compute_token_expiry(tokens.expires_in)
        save_config(config)
    except Exception:
        raise click.ClickException(
            "Session expired. Run `fastn login` to re-authenticate."
        )


def _graphql_headers(config: FastnConfig) -> dict:
    """Build headers for the GraphQL API."""
    return config.get_headers()


def _fetch_registry_list(config: FastnConfig) -> dict:
    """Fetch all connectors from the GraphQL API."""
    headers = _graphql_headers(config)
    # Community connector listing requires x-fastn-space-id: community
    headers["x-fastn-space-id"] = COMMUNITY_CONNECTOR_ID

    resp = httpx.post(
        GRAPHQL_URL,
        headers=headers,
        json={
            "query": SEARCH_CONNECTORS_QUERY,
            "variables": {
                "input": {
                    "clientId": COMMUNITY_CONNECTOR_ID,
                    "first": 500,
                    "connectorId": COMMUNITY_CONNECTOR_ID,
                    "query": '{"input":{"limit":500,"offset":0,"sort":"asc","query":"","filter":{}}}',
                    "isCommunity": True,
                    "offset": 0,
                }
            },
        },
        timeout=30.0,
    )
    if resp.status_code != 200:
        raise click.ClickException(f"Failed to fetch registry: {resp.status_code} {resp.text}")

    data = resp.json() or {}

    # Check for GraphQL errors
    if data.get("errors"):
        error_msg = data["errors"][0].get("message", "Unknown GraphQL error")
        raise click.ClickException(f"Registry sync failed: {error_msg}")

    search_result = (data.get("data") or {}).get("searchDataSourceGroups") or {}
    edges = search_result.get("edges") or []

    connectors: dict = {}
    for edge in edges:
        node = edge.get("node", {})
        connector_id = node.get("id", "")
        name = node.get("name", "")
        key = name.lower().replace(" ", "_").replace("-", "_")
        connectors[key] = {
            "id": connector_id,
            "display_name": name,
            "category": "",
            "tools": {},
            "tool_count": 0,
        }

    return {"version": "1.0.0", "connectors": connectors}


def _fetch_connector_tools(config: FastnConfig, connector_id: str) -> list:
    """Fetch all tools/actions for a connector via callCoreProjectFlow."""
    headers = _graphql_headers(config)
    workspace_id = config.resolve_project_id()

    resp = httpx.post(
        GRAPHQL_URL,
        headers=headers,
        json={
            "query": CONNECTOR_TOOLS_QUERY,
            "variables": {
                "input": {
                    "operationName": "getConnectorRegisteredTools_v1",
                    "input": {
                        "connectorId": connector_id,
                        "orgId": COMMUNITY_CONNECTOR_ID,
                        "workspaceId": workspace_id,
                        "gatewayId": workspace_id,
                    },
                }
            },
        },
        timeout=30.0,
    )
    if resp.status_code != 200:
        raise click.ClickException(
            f"Failed to fetch connector tools: {resp.status_code} {resp.text}"
        )

    data = resp.json()

    # Check for GraphQL errors
    if data.get("errors"):
        error_msg = data["errors"][0].get("message", "Unknown GraphQL error")
        raise click.ClickException(f"GraphQL error: {error_msg}")

    result = data.get("data", {}).get("callCoreProjectFlow") or {}
    tools = result.get("data") or []
    return tools


def _parse_tool_node(node: dict) -> dict:
    """Parse a single tool node from callCoreProjectFlow into registry format."""
    tool_name = node.get("name", "")
    action_id = node.get("id", "")
    description = node.get("description", "")

    # Extract params from inputSchema (already a dict)
    params = {}
    input_schema = node.get("inputSchema") or {}
    if isinstance(input_schema, dict):
        props = input_schema.get("properties", {})
        required_fields = input_schema.get("required", [])
        for pname, pdata in props.items():
            params[pname] = {
                "type": pdata.get("type", "string"),
                "description": pdata.get("description", ""),
                "required": pname in required_fields,
            }

    key = _to_snake_case(tool_name)
    return {
        "key": key,
        "data": {
            "actionId": action_id,
            "name": tool_name,
            "description": description,
            "params": params,
            "inputSchema": node.get("inputSchema") or {},
            "outputSchema": node.get("outputSchema") or {},
        },
    }


def _check_and_migrate(
    fastn_dir: Path,
    old_registry: Dict,
    new_registry: Dict,
    connector_names: Optional[list] = None,
) -> bool:
    """Detect breaking changes, prompt user, and save migration records.

    When breaking changes are found:
        1. Shows the diff summary
        2. Asks the user to confirm
        3. If confirmed, generates migration records so old code keeps
           working at runtime with deprecation warnings
        4. Saves migrations to .fastn/migrations.json

    Returns True if stubs should be regenerated, False to skip.
    """
    if diff_registries is None:
        return True

    result = diff_registries(old_registry, new_registry, connector_names)
    if not result.changes:
        return True

    summary = result.summary()
    if summary:
        click.echo()
        click.echo(summary)

    if result.has_breaking_changes:
        click.echo()
        click.echo("  Your existing code will continue to work with deprecation warnings.")
        if not click.confirm("  Update stubs with these breaking changes?"):
            click.echo("  Stubs not updated. Your existing stubs are unchanged.")
            return False

        # Generate and save migration records for runtime backward compat
        if build_migrations is not None:
            new_migrations = build_migrations(result, old_registry)
            existing_migrations = load_migrations(fastn_dir)
            if existing_migrations and merge_migrations is not None:
                merged = merge_migrations(existing_migrations, new_migrations)
            else:
                merged = new_migrations
            save_migrations(merged, fastn_dir)
            click.echo("  \u2713 Migration records saved. Old code will still work.")

    return True


def _update_schema_hashes(fastn_dir: Path, registry: Dict, installed: list) -> None:
    """Store schema hashes in manifest for each installed connector."""
    if compute_schema_hash is None:
        return

    manifest = load_manifest(fastn_dir)
    installed_data = manifest.get("installed", {})
    for name in installed:
        if name in installed_data:
            installed_data[name]["schema_hash"] = compute_schema_hash(registry, name)
    save_manifest(manifest, fastn_dir)


def _regenerate_stubs(
    fastn_dir: Path,
    language: str = "python",
    old_registry: Optional[Dict] = None,
    _skip: Optional[bool] = None,
) -> bool:
    """Regenerate type stubs based on current registry and installed connectors.

    If old_registry is provided, performs breaking change detection
    before regenerating. The user is prompted to confirm when breaking
    changes are found. Migration records are saved for runtime backward
    compatibility.

    Returns False if the user declined the update, True otherwise.
    """
    if StubGenerator is None:
        return True

    registry = load_registry(fastn_dir)
    installed = get_installed_connectors(fastn_dir)
    output_dir = fastn_dir / language
    output_dir.mkdir(parents=True, exist_ok=True)

    # Detect breaking changes before regenerating (only once, on first language)
    if _skip is None and old_registry is not None and language == "python":
        if not _check_and_migrate(fastn_dir, old_registry, registry, installed):
            return False

    if _skip:
        return False

    generator = StubGenerator(language=language)
    parsed = parse_registry(registry)
    generator.generate_all(registry, installed, str(output_dir))

    # Update schema hashes after successful generation
    if language == "python":
        _update_schema_hashes(fastn_dir, registry, installed)

    return True


@click.group()
@click.version_option(version=__version__, prog_name="fastn")
def cli() -> None:
    """Fastn SDK — Typed access to 250+ integrations."""
    pass


def _run_device_login() -> Optional[FastnConfig]:
    """Run the Keycloak device authorization flow.

    Returns a partial FastnConfig with auth tokens set, or None if login fails.
    """
    import webbrowser

    from fastn.oauth import (
        compute_token_expiry,
        poll_for_token,
        request_device_code,
    )

    try:
        with httpx.Client(timeout=30.0) as client:
            device = request_device_code(client)

            click.echo()
            click.echo(f"  Visit: {device.verification_uri}")
            click.echo(f"  Enter code: {device.user_code}")
            click.echo()

            # Try to auto-open browser
            try:
                webbrowser.open(device.verification_uri_complete)
                click.echo("  (Browser opened automatically)")
            except Exception:
                click.echo("  Open the URL above in your browser.")

            click.echo()
            click.echo("  Waiting for authorization", nl=False)

            tokens = poll_for_token(
                device.device_code,
                interval=device.interval,
                expires_in=device.expires_in,
                client=client,
            )

            click.echo()
            click.echo("  \u2713 Login successful!")

            return FastnConfig(
                auth_token=tokens.access_token,
                refresh_token=tokens.refresh_token,
                token_expiry=compute_token_expiry(tokens.expires_in),
            )
    except Exception as e:
        click.echo()
        click.echo(f"  \u2717 Login failed: {e}")
        click.echo()
        click.echo("  If this persists, use `fastn init` with a manual API key instead.")
        return None


@cli.command()
def login() -> None:
    """Authenticate with Fastn via browser-based device login."""
    click.echo()
    click.echo("  Fastn Login")

    result = _run_device_login()
    if result is None:
        raise SystemExit(1)

    # Merge with existing config (preserve space_id, etc.)
    existing = load_config()
    existing.auth_token = result.auth_token
    existing.refresh_token = result.refresh_token
    existing.token_expiry = result.token_expiry

    filepath = save_config(existing)
    ensure_gitignore()

    click.echo(f"  \u2713 Tokens saved to {filepath}")
    click.echo()


@cli.command()
def logout() -> None:
    """Clear stored authentication tokens."""
    config = load_config()
    config.auth_token = ""
    config.refresh_token = ""
    config.token_expiry = ""

    filepath = save_config(config)
    click.echo("  \u2713 Logged out successfully.")
    click.echo(f"  Tokens cleared from {filepath}")


@cli.command()
def whoami() -> None:
    """Show current authenticated user info."""
    config = load_config()

    if not config.auth_token:
        click.echo("  Not logged in. Run `fastn login` to authenticate.")
        return

    _ensure_fresh_token(config)

    from fastn.oauth import fetch_userinfo

    try:
        user_info = fetch_userinfo(config.auth_token)
        click.echo()
        name = user_info.get("name", user_info.get("preferred_username", "Unknown"))
        email = user_info.get("email", "")
        sub = user_info.get("sub", "")
        click.echo(f"  Logged in as: {name}")
        if email:
            click.echo(f"  Email: {email}")
        if sub:
            click.echo(f"  User ID: {sub}")
        click.echo()
    except Exception as e:
        click.echo(f"  Failed to fetch user info: {e}")
        click.echo("  Try running `fastn login` to re-authenticate.")


@cli.command()
def init() -> None:
    """Interactive setup — prompts for credentials, saves to .fastn/config.json."""
    click.echo()
    click.echo("  Welcome to Fastn SDK Setup")
    click.echo()

    # Offer browser-based login
    use_browser = click.confirm("  Log in via browser?", default=True)

    auth_token = ""
    refresh_token = ""
    token_expiry = ""
    api_key = ""

    if use_browser:
        result = _run_device_login()
        if result:
            auth_token = result.auth_token
            refresh_token = result.refresh_token
            token_expiry = result.token_expiry
        else:
            click.echo("  Falling back to manual API key entry.")
            api_key = click.prompt("  API Key", hide_input=False)
    else:
        api_key = click.prompt("  API Key", hide_input=False)

    click.echo()
    project_id = click.prompt("  Project ID")

    config = FastnConfig(
        api_key=api_key,
        project_id=project_id,
        stage=DEFAULT_STAGE,
        auth_token=auth_token,
        refresh_token=refresh_token,
        token_expiry=token_expiry,
    )

    filepath = save_config(config)
    ensure_gitignore()

    click.echo()
    click.echo(f"  \u2713 Config saved to {filepath}")
    click.echo("  \u2713 Added .fastn/config.json to .gitignore")
    click.echo()
    click.echo("  Run `fastn sync` to download the connector registry.")
    click.echo()


@cli.command()
def sync() -> None:
    """Download/update registry and refresh installed connector stubs."""
    config = load_config()
    if not config.auth_token and not config.api_key:
        raise click.ClickException("Not authenticated. Run `fastn login` first.")

    _ensure_fresh_token(config)

    click.echo("Syncing connector registry...")

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
    click.echo(f"\u2713 Registry synced: {connector_count} connectors available.")

    # Regenerate stubs for installed connectors (with breaking change detection)
    installed = get_installed_connectors(fastn_dir)
    if installed:
        updated = _regenerate_stubs(fastn_dir, "python", old_registry=old_registry)
        _regenerate_stubs(fastn_dir, "typescript", old_registry=old_registry, _skip=not updated)
        if updated:
            click.echo(f"\u2713 Refreshed stubs for {len(installed)} installed connector(s).")

    click.echo()
    click.echo("Run `fastn add <connector>` to enable autocomplete for specific connectors.")


@cli.command()
@click.argument("connectors", nargs=-1, required=True)
def add(connectors: tuple) -> None:
    """Download full type stubs for specific connectors."""
    config = load_config()
    try:
        config.validate()
    except Exception as e:
        raise click.ClickException(str(e))

    _ensure_fresh_token(config)

    fastn_dir = find_fastn_dir()
    registry = load_registry(fastn_dir)

    # Capture old registry for breaking change detection
    import copy
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
            click.echo(f"  ✗ Connector '{connector_name}' not found in registry.")
            click.echo(f"    Run `fastn sync` to refresh, then try again.")
            continue

        connector_data = reg_connectors[connector_name]
        connector_id = connector_data.get("id", "")

        if not connector_id:
            click.echo(f"  ✗ No connector ID for '{connector_name}'. Run `fastn sync`.")
            continue

        # Fetch tools for this connector
        click.echo(f"  Fetching tools for {connector_name}...")
        tool_nodes = _fetch_connector_tools(config, connector_id)
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
    updated = _regenerate_stubs(fastn_dir, "python", old_registry=old_registry)
    _regenerate_stubs(fastn_dir, "typescript", old_registry=old_registry, _skip=not updated)
    if updated:
        click.echo("✓ Type stubs generated.")


@cli.command()
@click.argument("connector_name")
def remove(connector_name: str) -> None:
    """Remove connector stubs."""
    fastn_dir = find_fastn_dir()

    if remove_connector_from_manifest(connector_name, fastn_dir):
        # Remove stub files
        for lang in ("python", "typescript"):
            ext = "pyi" if lang == "python" else "d.ts"
            stub_file = fastn_dir / lang / "connectors" / f"{connector_name}.{ext}"
            if stub_file.exists():
                stub_file.unlink()

        _regenerate_stubs(fastn_dir, "python")
        _regenerate_stubs(fastn_dir, "typescript")
        click.echo(f"\u2713 Removed {connector_name}.")
    else:
        click.echo(f"Connector '{connector_name}' is not installed.")


def _format_schema_properties(schema: dict, indent: int = 6) -> list:
    """Extract and format properties from an input or output schema.

    For inputSchema the real fields are typically nested under a wrapper
    key like ``body`` or ``param``.  This helper unwraps one level when
    the top-level schema has a single object property so the user sees
    the actual fields.

    Returns a list of formatted lines ready for ``click.echo``.
    """
    props = schema.get("properties", {})
    required_fields = set(schema.get("required", []))

    # Unwrap single wrapper key (e.g. "body" or "param")
    if len(props) == 1:
        wrapper_key = list(props.keys())[0]
        wrapper = props[wrapper_key]
        if isinstance(wrapper, dict) and wrapper.get("type") == "object":
            props = wrapper.get("properties", {})
            required_fields = set(wrapper.get("required", []))

    if not props:
        return []

    pad = " " * indent
    lines = []
    for name, pdata in props.items():
        ptype = pdata.get("type", "string")
        req = " (required)" if name in required_fields else ""
        desc = pdata.get("description", "")
        if desc:
            lines.append(f"{pad}{name}: {ptype}{req} — {desc}")
        else:
            lines.append(f"{pad}{name}: {ptype}{req}")
    return lines


@cli.command(name="list")
@click.argument("connector_name", required=False, default=None)
@click.option("--installed", is_flag=True, help="Show only installed connectors")
@click.option("-v", "--verbose", is_flag=True, help="Show input/output schemas for each tool")
def list_connectors(connector_name: Optional[str], installed: bool, verbose: bool) -> None:
    """List connectors, or show details for a specific one.

    \b
    Usage:
      fastn list              Show all available connectors
      fastn list --installed  Show only installed connectors
      fastn list slack        Show tools for the 'slack' connector
      fastn list slack -v     Show tools with input/output schemas
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

        click.echo("Syncing connector registry...")
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
            click.echo("No connectors found in registry.")
            return

    # If a connector name is given, show its details (like `sdk list java`)
    if connector_name:
        config = load_config()
        if not config.auth_token and not config.api_key:
            raise click.ClickException("Not authenticated. Run `fastn login` first.")

        _ensure_fresh_token(config)

        if connector_name not in connectors:
            raise click.ClickException(
                f"Connector '{connector_name}' not found. Run `fastn list` to see available connectors."
            )

        connector_data = connectors[connector_name]
        connector_id = connector_data.get("id", "")

        if not connector_id:
            raise click.ClickException(
                f"No connector ID for '{connector_name}'. Run `fastn sync`."
            )

        # Check if tools are already cached in registry
        cached_tools = connector_data.get("tools", {})
        if cached_tools:
            tool_list = cached_tools
        else:
            click.echo(f"Fetching tools for {connector_name}...")
            tool_nodes = _fetch_connector_tools(config, connector_id)
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

    # No connector name — list all connectors
    installed_names = set(get_installed_connectors(fastn_dir))

    if installed and not installed_names:
        click.echo("No connectors installed. Run `fastn add <name>` to install.")
        return

    items = sorted(connectors.items())
    if installed:
        items = [(k, v) for k, v in items if k in installed_names]

    click.echo()
    total = len(connectors)
    showing = len(items)
    label = "Installed" if installed else "Available"
    click.echo(f"  {label} connectors ({showing}{'' if installed else f' of {total}'}):")
    click.echo()

    for name, data in items:
        marker = "\u2705" if name in installed_names else "  "
        click.echo(f"  {marker} {name}")

    click.echo()
    installed_count = len(installed_names)
    click.echo(f"  {installed_count} installed. Run `fastn add <name>` to enable autocomplete.")
    click.echo()


@cli.command()
@click.argument("connector_name")
@click.argument("tool_name", required=False, default=None)
def schema(connector_name: str, tool_name: Optional[str]) -> None:
    """Show raw JSON schema for a connector's tools.

    \b
    Usage:
      fastn schema slack                  Show schemas for all Slack tools
      fastn schema slack send_message     Show schema for a specific tool
    """
    fastn_dir = find_fastn_dir()
    registry = load_registry(fastn_dir)
    connectors = registry.get("connectors", {})

    if connector_name not in connectors:
        raise click.ClickException(
            f"Connector '{connector_name}' not found. Run `fastn add {connector_name}` first."
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


def main() -> None:
    """Entry point for the fastn CLI."""
    cli()


if __name__ == "__main__":
    main()
