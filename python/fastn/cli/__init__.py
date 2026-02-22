"""Fastn CLI package — init, login, logout, whoami, sync, add, remove, list, run, schema, version."""

from __future__ import annotations

import click

from fastn import __version__


API_BASE_URL = "https://live.fastn.ai/api/ucl"
GRAPHQL_URL = "https://live.fastn.ai/api/graphql"

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


@click.group()
@click.version_option(version=__version__, prog_name="fastn")
@click.option("-v", "--verbose", is_flag=True, default=False, help="Show API calls and responses")
@click.pass_context
def cli(ctx: click.Context, verbose: bool) -> None:
    """Fastn SDK — The integration infrastructure for AI agents."""
    ctx.ensure_object(dict)
    ctx.obj["verbose"] = verbose


# Import all submodule commands so they register with the cli group
# (these imports must come after ``cli`` is defined)
from fastn.cli import auth_commands as _auth  # noqa: F401,E402
from fastn.cli import registry_commands as _registry  # noqa: F401,E402
from fastn.cli import run_command as _run  # noqa: F401,E402
from fastn.cli import agent_command as _agent  # noqa: F401,E402
from fastn.cli import skills_command as _skills  # noqa: F401,E402


def main() -> None:
    """Entry point for the fastn CLI."""
    cli()


if __name__ == "__main__":
    main()
