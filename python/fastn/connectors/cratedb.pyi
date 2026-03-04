"""Fastn CrateDB connector — auto-generated type stubs.

Do not edit manually. Regenerate with `fastn connector sync`.
"""
from __future__ import annotations

from typing import Any, Dict, List, Optional, TypedDict


class CratedbConnector:
    """CrateDB connector ().

    Provides 1 tools.
    """

    def cratedb_execute_query(
        self,
        query: str,
    ) -> Dict[str, Any]:
        """Executes a SQL query against a CrateDB distributed database. Use this to retrieve, insert, update, or delete data stored in CrateDB. Write queries (INSERT, UPDATE, DELETE, DROP) will modify or permanently remove data and cannot be automatically reversed — verify the query before execution. Do not use this tool for schema-level administration outside of SQL DDL statements.

        Args:
            query: The SQL query string. (required)
        Returns:
            API response as a dictionary.
        """
        ...

