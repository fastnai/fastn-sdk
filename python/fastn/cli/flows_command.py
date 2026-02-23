"""CLI commands: fastn flow — manage integration flows."""

from __future__ import annotations

import json

import click

from fastn.cli import cli, OrderedGroup, GRAPHQL_URL
from fastn.cli._helpers import _ensure_fresh_token, _verbose_post
from fastn.config import load_config
from fastn._constants import FLOWS_API_URL, LIST_FLOWS_QUERY


# ---------------------------------------------------------------------------
# Shared helpers
# ---------------------------------------------------------------------------

def _require_auth():
    """Load config, check auth, refresh token, return (config, headers, project_id)."""
    config = load_config()
    if not config.auth_token and not config.api_key:
        raise click.ClickException("Not authenticated. Run `fastn login` first.")

    _ensure_fresh_token(config)

    project_id = config.resolve_project_id()
    if not project_id:
        raise click.ClickException("No project configured. Run `fastn login` first.")

    return config, config.get_headers(), project_id


def _flows_api_post(headers, endpoint, payload):
    """POST to the flows REST API and handle common errors."""
    url = f"{FLOWS_API_URL}/{endpoint}"
    resp = _verbose_post(url, headers=headers, payload=payload)

    if resp.status_code == 401:
        raise click.ClickException(
            "Authentication failed. Run `fastn login` to re-authenticate."
        )

    body = None
    try:
        body = resp.json()
    except (ValueError, RuntimeError):
        pass

    if resp.status_code >= 400:
        error_code = (body or {}).get("error", "")
        if error_code == "FLOW_NOT_FOUND":
            raise click.ClickException(
                f"Flow not found. Run `fastn flow ls` to see available flows."
            )
        if error_code == "RUN_NOT_FOUND":
            raise click.ClickException(
                f"Run not found. Check the run_id and try again."
            )
        raise click.ClickException(f"API error ({resp.status_code}): {resp.text[:200]}")

    # Unwrap {body: ...} envelope
    if isinstance(body, dict) and "body" in body:
        return body["body"]
    return body


# ---------------------------------------------------------------------------
# fastn flow  (group)
# ---------------------------------------------------------------------------

@cli.group(
    cls=OrderedGroup,
    command_order=["ls", "create", "run", "get-run", "update", "delete"],
)
@click.pass_context
def flow(ctx):
    """Build and run automated workflows between your connected apps.

    \b
    Usage:
      fastn flow ls                  List all flows
      fastn flow ls --status active  List only active flows
      fastn flow create              Create a new flow
      fastn flow run <flow_id>       Trigger a flow run
      fastn flow get-run <run_id>    Check run status
      fastn flow delete <flow_id>    Delete a flow
      fastn flow update <flow_id>    Update a flow
    """
    pass


@flow.command(name="ls")
@click.option("--status", default=None, type=click.Choice(["active", "paused", "draft"]),
              help="Filter flows by status")
def flow_ls(status):
    """List all flows in the current project."""
    _list_flows(status)


def _list_flows(status):
    """Fetch and display flows."""
    config, headers, project_id = _require_auth()

    variables = {
        "input": {
            "clientId": project_id,
            "first": 500,
            "after": None,
            "query": '{"input":{"limit":500,"offset":0,"sort":"desc","query":"","filter":{}}}',
        }
    }
    payload = {"query": LIST_FLOWS_QUERY, "variables": variables}

    resp = _verbose_post(GRAPHQL_URL, headers=headers, payload=payload)

    if resp.status_code == 401:
        raise click.ClickException(
            "Authentication failed. Run `fastn login` to re-authenticate."
        )
    if resp.status_code >= 400:
        raise click.ClickException(f"API error ({resp.status_code}): {resp.text[:200]}")

    data = resp.json().get("data", {})
    errors = resp.json().get("errors")
    if errors:
        raise click.ClickException(
            f"GraphQL error: {errors[0].get('message', 'Unknown error')}"
        )

    edges = (data.get("apis") or {}).get("edges") or []

    items = []
    for edge in edges:
        node = (edge or {}).get("node") or {}
        items.append(node)

    # Client-side status filter
    if status:
        items = [f for f in items if f.get("status") == status]

    if not items:
        click.echo("No flows found in this project.")
        return

    click.echo()
    click.echo(f"  {'Name':<25} {'Status':<10} {'Version':<10} {'ID'}")
    click.echo(f"  {'─' * 25} {'─' * 10} {'─' * 10} {'─' * 36}")
    for f in items:
        name = (f.get("name") or "")[:25]
        fstatus = (f.get("status") or "")[:10]
        version = (f.get("version") or "")[:10]
        fid = f.get("id", "")
        click.echo(f"  {name:<25} {fstatus:<10} {version:<10} {fid}")
    click.echo()
    click.echo(f"  {len(items)} flow(s) found.")


# ---------------------------------------------------------------------------
# fastn flow create
# ---------------------------------------------------------------------------

@flow.command()
@click.option("--prompt", "-p", required=True, help="Plain-English description of the flow to create")
def create(prompt):
    """Create an integration flow from a plain-English prompt.

    \b
    Examples:
      fastn flow create -p "When a Jira ticket is created, post to Slack"
      fastn flow create --prompt "Sync new Hubspot contacts to Salesforce daily"
    """
    _config, headers, _project_id = _require_auth()

    result = _flows_api_post(headers, "create", {"prompt": prompt})

    if isinstance(result, dict) and result.get("questions"):
        click.echo()
        click.echo("  Fastn needs more information:")
        click.echo()
        for q in result["questions"]:
            click.echo(f"    - {q}")
        click.echo()
        click.echo("  Use the SDK to answer: fastn.flows.create(prompt=..., answers={...})")
        return

    click.echo()
    flow_id = result.get("flow_id", "") if isinstance(result, dict) else ""
    if flow_id:
        click.echo(f"  \u2713 Flow created: {flow_id}")
    else:
        click.echo(json.dumps(result, indent=2))


# ---------------------------------------------------------------------------
# fastn flow run
# ---------------------------------------------------------------------------

@flow.command()
@click.argument("flow_id")
@click.option("--user-id", default=None, help="End-user ID for multi-tenant flows")
def run(flow_id, user_id):
    """Trigger a flow run.

    \b
    Examples:
      fastn flow run testflow
      fastn flow run testflow --user-id user_42
    """
    _config, headers, _project_id = _require_auth()

    payload = {"flow_id": flow_id}
    if user_id:
        payload["user_id"] = user_id

    result = _flows_api_post(headers, "run", payload)

    click.echo()
    run_id = result.get("run_id", "") if isinstance(result, dict) else ""
    status = result.get("status", "") if isinstance(result, dict) else ""
    if run_id:
        click.echo(f"  \u2713 Flow run started: {run_id}  (status: {status})")
        click.echo(f"    Check status: fastn flow get-run {run_id}")
    else:
        click.echo(json.dumps(result, indent=2))


# ---------------------------------------------------------------------------
# fastn flow get-run
# ---------------------------------------------------------------------------

@flow.command(name="get-run")
@click.argument("run_id")
def get_run(run_id):
    """Check the status of a flow run.

    \b
    Examples:
      fastn flow get-run run_xyz123
    """
    _config, headers, _project_id = _require_auth()

    result = _flows_api_post(headers, "get_run", {"run_id": run_id})

    click.echo()
    if isinstance(result, dict):
        click.echo(f"  Run ID:    {result.get('run_id', run_id)}")
        click.echo(f"  Status:    {result.get('status', 'unknown')}")
        if result.get("started_at"):
            click.echo(f"  Started:   {result['started_at']}")
        if result.get("completed_at"):
            click.echo(f"  Completed: {result['completed_at']}")
        if result.get("result"):
            click.echo(f"  Result:    {json.dumps(result['result'], indent=2)}")
        if result.get("error"):
            click.echo(f"  Error:     {result['error']}")
    else:
        click.echo(json.dumps(result, indent=2))


# ---------------------------------------------------------------------------
# fastn flow delete
# ---------------------------------------------------------------------------

@flow.command()
@click.argument("flow_id")
@click.option("--yes", "-y", is_flag=True, help="Skip confirmation prompt")
def delete(flow_id, yes):
    """Delete a flow.

    \b
    Examples:
      fastn flow delete testflow
      fastn flow delete testflow -y
    """
    _config, headers, _project_id = _require_auth()

    if not yes:
        if not click.confirm(f"  Delete flow '{flow_id}'?"):
            click.echo("  Cancelled.")
            return

    result = _flows_api_post(headers, "delete", {"flow_id": flow_id})

    click.echo()
    click.echo(f"  \u2713 Flow '{flow_id}' deleted.")


# ---------------------------------------------------------------------------
# fastn flow update
# ---------------------------------------------------------------------------

@flow.command()
@click.argument("flow_id")
@click.option("--prompt", "-p", default=None, help="New prompt to regenerate the flow")
@click.option("--schedule", default=None, help='Cron schedule (e.g. "0 9 * * MON-FRI")')
@click.option("--enabled/--disabled", default=None, help="Enable or disable the flow")
def update(flow_id, prompt, schedule, enabled):
    """Update an existing flow.

    \b
    Examples:
      fastn flow update testflow --schedule "0 9 * * MON-FRI"
      fastn flow update testflow --disabled
      fastn flow update testflow -p "Also send a summary email"
    """
    _config, headers, _project_id = _require_auth()

    payload = {"flow_id": flow_id}
    if prompt is not None:
        payload["prompt"] = prompt
    if schedule is not None:
        payload["schedule"] = schedule
    if enabled is not None:
        payload["enabled"] = enabled

    if len(payload) == 1:
        raise click.ClickException(
            "Nothing to update. Pass --prompt, --schedule, or --enabled/--disabled."
        )

    result = _flows_api_post(headers, "update", payload)

    click.echo()
    click.echo(f"  \u2713 Flow '{flow_id}' updated.")
    if isinstance(result, dict):
        if result.get("questions"):
            click.echo()
            click.echo("  Fastn needs more information:")
            for q in result["questions"]:
                click.echo(f"    - {q}")
