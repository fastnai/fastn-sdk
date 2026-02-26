"""Fastn Starburst Galaxy connector — auto-generated type stubs.

Do not edit manually. Regenerate with `fastn connector sync`.
"""
from __future__ import annotations

from typing import Any, Dict, List, Optional


class StarburstGalaxyConnector:
    """Starburst Galaxy connector ().

    Provides 1 tools.
    """

    def execute_query(
        self,
        query: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Executes a query in the associated database using the executeQuery tool.

        Args:
            query: 
        Returns:
            API response as a dictionary.
        """
        ...

