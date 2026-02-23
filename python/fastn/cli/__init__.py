"""Fastn CLI package — connectors, flows, skills, agent, auth, and system commands."""

from __future__ import annotations

from typing import List, Optional

import click

from fastn import __version__


API_BASE_URL = "https://live.fastn.ai/api/ucl"
GRAPHQL_URL = "https://live.fastn.ai/api/graphql"


class OrderedGroup(click.Group):
    """Click group that displays commands in an explicit order instead of alphabetically."""

    def __init__(self, *args, command_order: Optional[List[str]] = None, **kwargs):
        super().__init__(*args, **kwargs)
        self._command_order = command_order or []

    def list_commands(self, ctx: click.Context) -> List[str]:
        all_cmds = set(super().list_commands(ctx))
        ordered = [c for c in self._command_order if c in all_cmds]
        # Append any commands not in the explicit list (safety net)
        ordered += sorted(all_cmds - set(ordered))
        return ordered

SEARCH_TOOLS_QUERY = """
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
        connectorType
      }
    }
  }
}
"""

TOOL_ACTIONS_QUERY = """
query callCoreProjectFlow($input: CoreProjectFlowProxyInput!) {
  callCoreProjectFlow(input: $input) {
    data
    statusCode
    message
  }
}
"""


COMMUNITY_CONNECTOR_ID = "community"

# Connector source categories
SOURCE_WORKSPACE = "workspace"
SOURCE_ORG = "org"
SOURCE_COMMUNITY = "community"

EXECUTE_URL = "https://live.fastn.ai/api/ucl/executeTool"

GET_TOOLS_URL = "https://live.fastn.ai/api/ucl/getTools"


@click.group(
    cls=OrderedGroup,
    command_order=[
        "login", "logout", "whoami",
        "connector", "flow", "skill",
        "agent",
        "version",
    ],
)
@click.version_option(version=__version__, prog_name="fastn")
@click.option("-v", "--verbose", is_flag=True, default=False, help="Show API calls and responses")
@click.pass_context
def cli(ctx: click.Context, verbose: bool) -> None:
    """Fastn \u2014 The fastest way to add enterprise integrations to any AI agent or app."""
    ctx.ensure_object(dict)
    ctx.obj["verbose"] = verbose


# ---------------------------------------------------------------------------
# Connector subgroup — ls, add, remove, sync, run, schema
# ---------------------------------------------------------------------------

@cli.group(
    cls=OrderedGroup,
    command_order=["ls", "add", "remove", "sync", "run", "schema"],
)
@click.pass_context
def connector(ctx: click.Context) -> None:
    """Install and run tools from Slack, Jira, HubSpot, and 250+ more.

    \b
    Usage:
      fastn connector ls                       List all available connectors
      fastn connector ls slack               Show tools for a connector
      fastn connector add slack hubspot        Download type stubs
      fastn connector remove slack             Remove stubs
      fastn connector sync                     Refresh the registry
      fastn connector run slack send_message   Execute a tool
      fastn connector schema slack             Show JSON schemas
    """
    pass


# Import all submodule commands so they register with the cli/connectors groups
# (these imports must come after ``cli`` and ``connectors`` are defined)
from fastn.cli import auth_commands as _auth  # noqa: F401,E402
from fastn.cli import registry_commands as _registry  # noqa: F401,E402
from fastn.cli import run_command as _run  # noqa: F401,E402
from fastn.cli import agent_command as _agent  # noqa: F401,E402
from fastn.cli import skills_command as _skills  # noqa: F401,E402
from fastn.cli import flows_command as _flows_cmd  # noqa: F401,E402


def main() -> None:
    """Entry point for the fastn CLI."""
    cli()


if __name__ == "__main__":
    main()
