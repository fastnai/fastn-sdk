"""Fastn CLI package — init, login, logout, whoami, sync, add, remove, list, run, schema, version."""

from __future__ import annotations

import json
import os
import shutil
import sys
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Dict, List, Optional, Tuple

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
_SDK_ROOT = Path(__file__).resolve().parent.parent.parent.parent
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
        connectorType
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


GET_ORGANIZATIONS_QUERY = """
query getOrganizations($userId: String) {
  getOrganizations(userId: $userId) {
    id
    name
    deletable
    packageType
    __typename
  }
}
"""

COMMUNITY_CONNECTOR_ID = "community"

# Connector source categories
SOURCE_WORKSPACE = "workspace"
SOURCE_ORG = "org"
SOURCE_COMMUNITY = "community"

EXECUTE_URL = "https://live.fastn.ai/api/ucl/executeTool"
FASTN_APP_BASE = "https://app.ucl.dev"

GET_TOOLS_URL = "https://live.fastn.ai/api/ucl/getTools"


@click.group()
@click.version_option(version=__version__, prog_name="fastn")
@click.option("-v", "--verbose", is_flag=True, default=False, help="Show API calls and responses")
@click.pass_context
def cli(ctx: click.Context, verbose: bool) -> None:
    """Fastn SDK — The fastest way to add enterprise integrations to any AI agent or app."""
    ctx.ensure_object(dict)
    ctx.obj["verbose"] = verbose


# Import all submodule commands so they register with the cli group
# (these imports must come after ``cli`` is defined)
from fastn.cli import auth_commands as _auth  # noqa: F401,E402
from fastn.cli import registry_commands as _registry  # noqa: F401,E402
from fastn.cli import run_command as _run  # noqa: F401,E402
from fastn.cli import agent_command as _agent  # noqa: F401,E402


def main() -> None:
    """Entry point for the fastn CLI."""
    cli()


if __name__ == "__main__":
    main()
