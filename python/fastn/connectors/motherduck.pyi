"""Fastn MotherDuck connector — auto-generated type stubs.

Do not edit manually. Regenerate with `fastn connector sync`.
"""
from __future__ import annotations

from typing import Any, Dict, List, Optional, TypedDict


class MotherduckConnector:
    """MotherDuck connector ().

    Provides 1 tools.
    """

    def motherduck_execute_query(
        self,
        database: Optional[str] = None,
        query: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Executes a SQL query against a MotherDuck (DuckDB-based) database and returns the results. Use this tool when you need to retrieve, aggregate, or manipulate data using SQL, including queries across local and cloud data sources. Do not use this tool for non-SQL operations or schema management outside of SQL DDL statements. Queries that modify data (INSERT, UPDATE, DELETE) will have permanent side effects on the target database.

        Args:
            database: 
            query: 
        Returns:
            API response as a dictionary.
        """
        ...

