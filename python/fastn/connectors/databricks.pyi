"""Fastn Databricks connector — auto-generated type stubs.

Do not edit manually. Regenerate with `fastn connector sync`.
"""
from __future__ import annotations

from typing import Any, Dict, List, Optional, TypedDict


class DatabricksConnector:
    """Databricks connector ().

    Provides 1 tools.
    """

    def databricks_execute_query(
        self,
        query: str,
    ) -> Dict[str, Any]:
        """Executes a SQL or programmatic query against a Databricks data warehouse or lakehouse. Use this to retrieve, transform, or manipulate data stored in Databricks. Write operations (INSERT, UPDATE, DELETE, DROP) will modify or permanently remove data and cannot be automatically reversed — verify the query carefully before execution. Do not use this tool for cluster lifecycle management or job orchestration.

        Args:
            query: The query to be executed on the Databricks cluster. (required)
        Returns:
            API response as a dictionary.
        """
        ...

