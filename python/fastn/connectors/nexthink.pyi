"""Fastn Nexthink connector — auto-generated type stubs.

Do not edit manually. Regenerate with `fastn connector sync`.
"""
from __future__ import annotations

from typing import Any, Dict, List, Optional, TypedDict


class _NexthinkExecuteNqlQueryParameters(TypedDict, total=False):
    type: str

class _NexthinkRequestNqlQueryExecutionParameters(TypedDict, total=False):
    type: str

class NexthinkConnector:
    """Nexthink connector ().

    Provides 8 tools.
    """

    def nexthink_create_enrichment(
        self,
        domain: str,
        enrichments: Optional[List[Any]] = None,
    ) -> Dict[str, Any]:
        """Creates a new data enrichment field definition in the connected Nexthink instance, allowing additional custom data to be associated with Nexthink entities. Use this tool when you need to extend Nexthink data models with new enrichment fields. Do not use this tool to update existing enrichment fields. This operation modifies the Nexthink data schema.

        Args:
            domain: Domain name. (required)
            enrichments: 
        Returns:
            API response as a dictionary.
        """
        ...

    def nexthink_execute_nql_query(
        self,
        parameters: _NexthinkExecuteNqlQueryParameters,
        queryId: str,
    ) -> Dict[str, Any]:
        """Synchronously executes a NQL (Nexthink Query Language) query against the connected Nexthink instance and returns the results immediately. Use this tool when you need real-time query results from Nexthink data. Do not use this tool for large data exports that require asynchronous processing — use nexthink_request_nql_query_execution instead. Note: NQL stands for Nexthink Query Language, not Nexoss Query Language.

        Args:
            parameters: Additional parameters for the request. (required)
            queryId: The ID of the query. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def nexthink_generate_auth_token(
        self,
        instanceName: str,
        region: str,
    ) -> Dict[str, Any]:
        """Generates an authentication token for accessing the Nexthink API securely. Use this tool to obtain a bearer token required before making authenticated API calls to Nexthink. Do not use this tool if a valid token is already available. The generated token has a limited lifespan and must be refreshed periodically.

        Args:
            instanceName: Name of the Nexthink instance. (required)
            region: Region of the Nexthink instance. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def nexthink_get_remote_action(
        self,
        nqlid: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Retrieves the details of a specific remote action in the connected Nexthink instance, identified by its unique identifier. Use this tool when you need to inspect the configuration or parameters of a single remote action. Do not use this tool to list all available remote actions — use nexthink_list_remote_actions instead.

        Args:
            nqlid: The ID of the NQL query.
        Returns:
            API response as a dictionary.
        """
        ...

    def nexthink_get_workflow(
        self,
        nqlid: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Retrieves the details of a specific Nexthink workflow identified by its unique identifier. Use this tool when you need to inspect the configuration or status of a single workflow. Do not use this tool to list all available workflows — use nexthink_list_workflows instead.

        Args:
            nqlid: The ID of the Nexthink Query Language (NQL) query.
        Returns:
            API response as a dictionary.
        """
        ...

    def nexthink_list_remote_actions(
        self,
    ) -> Dict[str, Any]:
        """Lists all remote actions available within the connected Nexthink instance. Use this tool when you need an overview of all executable remote actions, for example to find an action ID before retrieving its details or triggering it. Do not use this tool to retrieve details of a single remote action — use nexthink_get_remote_action instead.
        Returns:
            API response as a dictionary.
        """
        ...

    def nexthink_list_workflows(
        self,
        apiEnabled: Optional[str] = None,
        status: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Lists all workflows available and configured within the connected Nexthink instance. Use this tool when you need an overview of all workflows, for example to find a workflow ID before fetching its details. Do not use this tool to retrieve details of a single workflow — use nexthink_get_workflow instead.

        Args:
            apiEnabled: Indicates if the API is enabled.
            status: The status of the request.
        Returns:
            API response as a dictionary.
        """
        ...

    def nexthink_request_nql_query_execution(
        self,
        parameters: Optional[_NexthinkRequestNqlQueryExecutionParameters] = None,
        queryId: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Submits an asynchronous export request to execute a NQL (Nexthink Query Language) query and retrieve the resulting data from the Nexthink instance. Use this tool when you need to export large datasets via NQL asynchronously. Do not use this tool for synchronous query execution — use nexthink_execute_nql_query instead. This operation initiates a background export job.

        Args:
            parameters: 
            queryId: 
        Returns:
            API response as a dictionary.
        """
        ...

