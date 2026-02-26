"""Fastn Nexthink connector — auto-generated type stubs.

Do not edit manually. Regenerate with `fastn connector sync`.
"""
from __future__ import annotations

from typing import Any, Dict, List, Optional


class NexthinkConnector:
    """Nexthink connector ().

    Provides 8 tools.
    """

    def create_enrichment(
        self,
        domain: str,
        enrichments: Optional[List[Any]] = None,
    ) -> Dict[str, Any]:
        """Creates a new enrichment object in the specified connector for enhancing data.

        Args:
            domain: Domain name. (required)
            enrichments: 
        Returns:
            API response as a dictionary.
        """
        ...

    def execute_nql_query(
        self,
        parameters: Dict[str, Any],
        queryId: str,
    ) -> Dict[str, Any]:
        """Executes a NQL (Nexoss Query Language) query against the specified connector's database.

        Args:
            parameters: Additional parameters for the request. (required)
            queryId: The ID of the query. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def generate_auth_token(
        self,
        instanceName: str,
        region: str,
    ) -> Dict[str, Any]:
        """Generates an authentication token for accessing the API securely.

        Args:
            instanceName: Name of the Nexthink instance. (required)
            region: Region of the Nexthink instance. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def get_remote_action(
        self,
        nqlid: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Fetches the details of a specific remote action based on its identifier from the connector.

        Args:
            nqlid: The ID of the NQL query.
        Returns:
            API response as a dictionary.
        """
        ...

    def get_remote_actions(
        self,
    ) -> Dict[str, Any]:
        """Retrieves a list of available remote actions that can be performed within the specified connector.
        Returns:
            API response as a dictionary.
        """
        ...

    def get_workflow(
        self,
        nqlid: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Fetches the details of a specific workflow based on its identifier from the connector.

        Args:
            nqlid: The ID of the Nexthink Query Language (NQL) query.
        Returns:
            API response as a dictionary.
        """
        ...

    def get_workflows(
        self,
        apiEnabled: Optional[str] = None,
        status: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Retrieves a list of available workflows configured within the specified connector.

        Args:
            apiEnabled: Indicates if the API is enabled.
            status: The status of the request.
        Returns:
            API response as a dictionary.
        """
        ...

    def request_nql_query_execution(
        self,
        parameters: Optional[Dict[str, Any]] = None,
        queryId: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Requests the execution of a NQL query for retrieving specific data from the connector.

        Args:
            parameters: 
            queryId: 
        Returns:
            API response as a dictionary.
        """
        ...

