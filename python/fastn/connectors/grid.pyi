"""Fastn Grid connector — auto-generated type stubs.

Do not edit manually. Regenerate with `fastn connector sync`.
"""
from __future__ import annotations

from typing import Any, Dict, List, Optional, TypedDict


class GridConnector:
    """Grid connector ().

    Provides 3 tools.
    """

    def grid_advanced_data_query(
        self,
        apply: Optional[List[Any]] = None,
        read: Optional[List[Any]] = None,
        workbookId: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Executes an advanced data query against a specific Grid workbook, returning complex data sets filtered by the criteria you provide. Use this tool when you need to run structured or formula-based queries against workbook data and require more control than a simple cell-value lookup. Do not use this tool to retrieve raw cell values by range — use grid_get_cell_values instead. This tool sends a POST request and may consume API quota.

        Args:
            apply: 
            read: 
            workbookId: 
        Returns:
            API response as a dictionary.
        """
        ...

    def grid_get_cell_values(
        self,
        apply: Optional[Dict[str, Any]] = None,
        read: Optional[List[Any]] = None,
        workbookId: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Retrieves values from specific cells in a Grid workbook by posting a cell range or reference specification. Use this tool when you need to read raw cell data from a known workbook and cell location. Do not use this tool for complex filtered queries — use grid_advanced_data_query instead. This tool sends a POST request to the workbook values endpoint.

        Args:
            apply: 
            read: 
            workbookId: 
        Returns:
            API response as a dictionary.
        """
        ...

    def grid_list_workbooks(
        self,
        next_cursor: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Returns a list of all workbooks available in the Grid account. Use this tool when you need to discover existing workbooks, retrieve their IDs, or enumerate available data sources before performing cell reads or queries. Do not use this tool to read data from inside a workbook — use grid_get_cell_values or grid_advanced_data_query for that. This tool is read-only and has no side effects.

        Args:
            next_cursor: 
        Returns:
            API response as a dictionary.
        """
        ...

