"""Fastn TeraData connector — auto-generated type stubs.

Do not edit manually. Regenerate with `fastn connector sync`.
"""
from __future__ import annotations

from typing import Any, Dict, List, Optional


class TeradataConnector:
    """TeraData connector ().

    Provides 1 tools.
    """

    def execute_query(
        self,
        query: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Executes a query using the specified database connector, retrieving or manipulating data as needed.

        Args:
            query: 
        Returns:
            API response as a dictionary.
        """
        ...

