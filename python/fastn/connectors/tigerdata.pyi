"""Fastn TigerData connector — auto-generated type stubs.

Do not edit manually. Regenerate with `fastn connector sync`.
"""
from __future__ import annotations

from typing import Any, Dict, List, Optional, TypedDict


class TigerdataConnector:
    """TigerData connector ().

    Provides 1 tools.
    """

    def tigerdata_execute_query(
        self,
        query: str,
    ) -> Dict[str, Any]:
        """Executes a SQL query against a TigerData PostgreSQL-compatible database, retrieving or manipulating data as specified by the query. Use this tool when you need to run SELECT, INSERT, UPDATE, DELETE, or other SQL statements against a TigerData instance. Do not use this tool for non-TigerData databases. Be aware that write operations (INSERT, UPDATE, DELETE) will modify data and may not be reversible.

        Args:
            query: The TigerData query string. (required)
        Returns:
            API response as a dictionary.
        """
        ...

