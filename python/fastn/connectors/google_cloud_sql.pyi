"""Fastn Google Cloud SQL connector — auto-generated type stubs.

Do not edit manually. Regenerate with `fastn connector sync`.
"""
from __future__ import annotations

from typing import Any, Dict, List, Optional


class GoogleCloudSqlConnector:
    """Google Cloud SQL connector ().

    Provides 1 tools.
    """

    def execute_query(
        self,
        query: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Executes a SQL query in the specified database connector, allowing for data retrieval, manipulation, or management based on the query provided.

        Args:
            query: 
        Returns:
            API response as a dictionary.
        """
        ...

