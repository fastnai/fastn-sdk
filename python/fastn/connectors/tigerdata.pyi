"""Fastn TigerData connector — auto-generated type stubs.

Do not edit manually. Regenerate with `fastn connector sync`.
"""
from __future__ import annotations

from typing import Any, Dict, List, Optional


class TigerdataConnector:
    """TigerData connector ().

    Provides 1 tools.
    """

    def execute_query(
        self,
        query: str,
    ) -> Dict[str, Any]:
        """Executes a query in the context of the specified database connector, allowing users to retrieve or manipulate data based on the SQL commands provided.

        Args:
            query: The TigerData query string. (required)
        Returns:
            API response as a dictionary.
        """
        ...

