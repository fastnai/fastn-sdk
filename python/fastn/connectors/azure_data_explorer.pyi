"""Fastn Azure Data Explorer connector — auto-generated type stubs.

Do not edit manually. Regenerate with `fastn connector sync`.
"""
from __future__ import annotations

from typing import Any, Dict, List, Optional


class AzureDataExplorerConnector:
    """Azure Data Explorer connector ().

    Provides 1 tools.
    """

    def execute_kql_query(
        self,
        csl: str,
        db: str,
        properties: str,
    ) -> Dict[str, Any]:
        """Executes a KQL (Kusto Query Language) query within the context of the specified Azure Data Explorer connector, allowing users to retrieve and analyze large datasets.

        Args:
            csl: The CSL (Common Schema Language) query string. (required)
            db: The name of the database to query. (required)
            properties: Additional properties for the request. (required)
        Returns:
            API response as a dictionary.
        """
        ...

