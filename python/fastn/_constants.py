"""Fastn SDK constants — URLs, GraphQL queries, and format definitions."""

from __future__ import annotations

# ---------------------------------------------------------------------------
# HTTP / retry defaults
# ---------------------------------------------------------------------------

DEFAULT_TIMEOUT = 30.0
MAX_RETRIES = 3
BACKOFF_FACTOR = 0.5

# ---------------------------------------------------------------------------
# API URLs
# ---------------------------------------------------------------------------

API_BASE_URL = "https://live.fastn.ai/api/ucl"
FLOWS_API_URL = "https://live.fastn.ai/api/flows"
CONNECTIONS_API_URL = "https://live.fastn.ai/api/connections"
GRAPHQL_URL = "https://live.fastn.ai/api/graphql"

# ---------------------------------------------------------------------------
# GraphQL queries
# ---------------------------------------------------------------------------

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

CALL_CORE_PROJECT_FLOW_QUERY = """
query callCoreProjectFlow($input: CoreProjectFlowProxyInput!) {
  callCoreProjectFlow(input: $input) {
    data
    statusCode
    message
  }
}
"""

LIST_SKILLS_QUERY = """
query ListUCLAgents($input: ListUCLAgentsInput!) {
  listUCLAgents(input: $input) {
    id
    projectId
    name
    description
    createdAt
    updatedAt
    __typename
  }
}
"""

LIST_FLOWS_QUERY = """
query apis($input: SearchDataModelInput!) {
  apis(input: $input) {
    pageInfo {
      totalCount
      __typename
    }
    edges {
      node {
        id
        name
        description
        status
        version
        updatedAt
        deployedAt
        metaData {
          flowType
          architecture
          isAsync
          __typename
        }
        __typename
      }
      __typename
    }
    __typename
  }
}
"""

SEARCH_CONNECTORS_QUERY = """
query searchDataSourceGroups($input: SearchDataModelInput!) {
  searchDataSourceGroups(input: $input) {
    pageInfo { totalCount }
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

_UPDATE_RESOLVER_STEP_MUTATION = """
mutation updateResolverStep($input: CreateResolverStepInput!) {
  updateResolverStep(input: $input) {
    id
    type
    warnings
    __typename
  }
}
"""

# ---------------------------------------------------------------------------
# Supported LLM tool formats
# ---------------------------------------------------------------------------

_SUPPORTED_FORMATS = ("openai", "anthropic", "gemini", "bedrock", "raw")
