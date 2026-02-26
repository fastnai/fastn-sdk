"""Fastn MotherDuck connector — auto-generated type stubs.

Do not edit manually. Regenerate with `fastn connector sync`.
"""
from __future__ import annotations

from typing import Any, Dict, List, Optional


class MotherduckConnector:
    """MotherDuck connector ().

    Provides 1 tools.
    """

    def execute_query(
        self,
        database: Optional[str] = None,
        query: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Executes a database query using the specified database connector, allowing retrieval and manipulation of data within the database.

        Args:
            database: 
            query: 
        Returns:
            API response as a dictionary.
        """
        ...

