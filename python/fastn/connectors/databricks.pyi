"""Fastn Databricks connector — auto-generated type stubs.

Do not edit manually. Regenerate with `fastn connector sync`.
"""
from __future__ import annotations

from typing import Any, Dict, List, Optional


class DatabricksConnector:
    """Databricks connector ().

    Provides 1 tools.
    """

    def execute_query(
        self,
        query: str,
    ) -> Dict[str, Any]:
        """Executes a query in the specified database connector, allowing for the retrieval or manipulation of data based on the provided query parameters.

        Args:
            query: The query to be executed on the Databricks cluster. (required)
        Returns:
            API response as a dictionary.
        """
        ...

