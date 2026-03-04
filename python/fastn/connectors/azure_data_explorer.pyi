"""Fastn Azure Data Explorer connector — auto-generated type stubs.

Do not edit manually. Regenerate with `fastn connector sync`.
"""
from __future__ import annotations

from typing import Any, Dict, List, Optional, TypedDict


class AzureDataExplorerConnector:
    """Azure Data Explorer connector ().

    Provides 1 tools.
    """

    def microsoft_fabric_execute_kql_query(
        self,
        csl: str,
        db: str,
        properties: str,
        queryServiceUrl: str,
    ) -> Dict[str, Any]:
        """Executes a KQL (Kusto Query Language) management or query command against an Azure Data Explorer cluster via the Microsoft Fabric query service REST endpoint. Use this tool when you need to run read queries, filter, aggregate, or analyze large datasets stored in Azure Data Explorer in real time, or when you need to issue management REST commands via the /v1/rest/mgmt endpoint. Do not use this tool for schema modification operations or data ingestion that require dedicated ingestion APIs. Requires a valid KQL query or management command string and a configured query service URL. This tool reads data and issues management commands; management commands may have side effects on the cluster.

        Args:
            csl: The CSL (Common Schema Language) query string. (required)
            db: The name of the database to query. (required)
            properties: Additional properties for the request. (required)
            queryServiceUrl: The URL of the query service. (required)
        Returns:
            API response as a dictionary.
        """
        ...

