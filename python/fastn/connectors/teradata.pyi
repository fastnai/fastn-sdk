"""Fastn TeraData connector — auto-generated type stubs.

Do not edit manually. Regenerate with `fastn connector sync`.
"""
from __future__ import annotations

from typing import Any, Dict, List, Optional, TypedDict


class TeradataConnector:
    """TeraData connector ().

    Provides 1 tools.
    """

    def teradata_execute_query(
        self,
        query: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Executes a SQL query against a Teradata database, retrieving or manipulating data as specified by the query. Use this tool when you need to run SELECT, INSERT, UPDATE, DELETE, or other SQL statements against a Teradata data warehouse. Do not use this tool for non-Teradata databases. Be aware that write operations (INSERT, UPDATE, DELETE) will modify data and may not be reversible.

        Args:
            query: 
        Returns:
            API response as a dictionary.
        """
        ...

