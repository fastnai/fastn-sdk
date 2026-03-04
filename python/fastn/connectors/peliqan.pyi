"""Fastn Peliqan connector — auto-generated type stubs.

Do not edit manually. Regenerate with `fastn connector sync`.
"""
from __future__ import annotations

from typing import Any, Dict, List, Optional, TypedDict


class PeliqanConnector:
    """Peliqan connector ().

    Provides 1 tools.
    """

    def peliqan_execute_query(
        self,
        query: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Executes a database query against a specified connector in the Peliqan data platform and returns the results. Use this to run SQL or platform-specific queries to read or manipulate data across connected SaaS apps and databases. This tool may have side effects if the query performs write, update, or delete operations — use with caution for non-SELECT statements. Do not use this for triggering workflow automations; use dedicated workflow tools instead.

        Args:
            query: 
        Returns:
            API response as a dictionary.
        """
        ...

