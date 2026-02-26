"""Fastn Grid connector — auto-generated type stubs.

Do not edit manually. Regenerate with `fastn connector sync`.
"""
from __future__ import annotations

from typing import Any, Dict, List, Optional


class GridConnector:
    """Grid connector ().

    Provides 3 tools.
    """

    def advanced_data_query(
        self,
        apply: Optional[List[Any]] = None,
        read: Optional[List[Any]] = None,
    ) -> Dict[str, Any]:
        """Performs advanced data queries within the connector, allowing users to extract complex data sets based on specific criteria.

        Args:
            apply: 
            read: 
        Returns:
            API response as a dictionary.
        """
        ...

    def get_cell_values(
        self,
        apply: Optional[Dict[str, Any]] = None,
        read: Optional[List[Any]] = None,
    ) -> Dict[str, Any]:
        """Fetches values from specific cells in a workbook, enabling data retrieval and analysis through the specified connector.

        Args:
            apply: 
            read: 
        Returns:
            API response as a dictionary.
        """
        ...

    def get_workbooks(
        self,
        next_cursor: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Retrieves a list of workbooks from the application, allowing for easy access to workbook details and manipulation within the specified connector.

        Args:
            next_cursor: 
        Returns:
            API response as a dictionary.
        """
        ...

