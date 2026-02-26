"""Fastn SheetRocks connector — auto-generated type stubs.

Do not edit manually. Regenerate with `fastn connector sync`.
"""
from __future__ import annotations

from typing import Any, Dict, List, Optional


class SheetrocksConnector:
    """SheetRocks connector ().

    Provides 7 tools.
    """

    def append_cell_in_sheet(
        self,
        Cells: List[Any],
    ) -> Dict[str, Any]:
        """Appends a new cell in the specified sheet using Google Sheets.

        Args:
            Cells: An array of cell data to be updated or added. Each inner array represents a row. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def export_sheet_as_csv(
        self,
        sheetId: str,
        workbookId: str,
    ) -> Dict[str, Any]:
        """Exports the specified sheet as a CSV file using Google Sheets.

        Args:
            sheetId: The unique identifier for the target sheet. (required)
            workbookId: The unique identifier for the target workbook. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def get_cells_from_sheet(
        self,
        sheetId: str,
        workbookId: str,
    ) -> Dict[str, Any]:
        """Fetches the content of specific cells from the specified sheet in Google Sheets.

        Args:
            sheetId: The unique identifier for the target sheet. (required)
            workbookId: The unique identifier for the target workbook. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def get_constraint_for_sheet(
        self,
        sheetId: str,
        workbookId: str,
    ) -> Dict[str, Any]:
        """Obtains the constraints (such as validation rules) for the specified sheet in Google Sheets.

        Args:
            sheetId:  (required)
            workbookId:  (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def get_files(
        self,
        workbookId: str,
    ) -> Dict[str, Any]:
        """Fetches a list of files available in the connected storage system.

        Args:
            workbookId: The unique identifier for the workbook. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def get_format_of_sheet(
        self,
        sheetId: str,
        workbookId: str,
    ) -> Dict[str, Any]:
        """Retrieves the formatting details of the specified sheet in Google Sheets.

        Args:
            sheetId:  (required)
            workbookId:  (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def get_workbooks(
        self,
    ) -> Dict[str, Any]:
        """Retrieves a list of workbooks from the specified API or service.
        Returns:
            API response as a dictionary.
        """
        ...

