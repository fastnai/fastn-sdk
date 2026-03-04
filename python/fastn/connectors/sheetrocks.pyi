"""Fastn SheetRocks connector — auto-generated type stubs.

Do not edit manually. Regenerate with `fastn connector sync`.
"""
from __future__ import annotations

from typing import Any, Dict, List, Optional, TypedDict


class SheetrocksConnector:
    """SheetRocks connector ().

    Provides 7 tools.
    """

    def sheetrocks_append_cell_in_sheet(
        self,
        Cells: List[Any],
        sheetId: str,
        workbookId: str,
    ) -> Dict[str, Any]:
        """Appends a new cell or row of data to the end of a specific sheet within a SheetRocks workbook, identified by workbook ID and sheet ID. Use this tool when you need to add new data without overwriting existing content. Do not use this tool if you need to update or overwrite an existing cell. This operation modifies sheet data and cannot be automatically undone.

        Args:
            Cells: An array of cell data to be updated or added. Each inner array represents a row. (required)
            sheetId: The ID of the sheet to interact with. (required)
            workbookId: The ID of the workbook containing the sheet. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def sheetrocks_export_sheet_as_csv(
        self,
        sheetId: str,
        workbookId: str,
    ) -> Dict[str, Any]:
        """Exports a specific sheet from a SheetRocks workbook as a CSV file, identified by workbook ID and sheet ID. Use this tool when you need a portable, comma-separated representation of sheet data for download or further processing. Does not apply to or reference Google Sheets. Read-only; no data is modified.

        Args:
            sheetId: The unique identifier for the target sheet. (required)
            workbookId: The unique identifier for the target workbook. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def sheetrocks_get_cells_from_sheet(
        self,
        sheetId: str,
        workbookId: str,
    ) -> Dict[str, Any]:
        """Retrieves the content of cells from a specific sheet within a SheetRocks workbook, identified by workbook ID and sheet ID. Use this tool when you need to read cell values or data from a sheet. Does not apply to or reference Google Sheets. Read-only; no data is modified.

        Args:
            sheetId: The unique identifier for the target sheet. (required)
            workbookId: The unique identifier for the target workbook. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def sheetrocks_get_constraint_for_sheet(
        self,
        sheetId: str,
        workbookId: str,
    ) -> Dict[str, Any]:
        """Retrieves the data constraints (such as validation rules) defined for a specific sheet within a SheetRocks workbook, identified by workbook ID and sheet ID. Use this tool when you need to inspect what values or formats are permitted in a sheet before writing data. Does not apply to or reference Google Sheets. Read-only; no data is modified.

        Args:
            sheetId:  (required)
            workbookId:  (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def sheetrocks_get_format_of_sheet(
        self,
        sheetId: str,
        workbookId: str,
    ) -> Dict[str, Any]:
        """Retrieves the formatting details (such as column widths, cell styles, and number formats) of a specific sheet within a SheetRocks workbook, identified by workbook ID and sheet ID. Use this tool when you need to inspect the visual or structural formatting of a sheet before rendering or transforming data. Does not apply to or reference Google Sheets. Read-only; no data is modified.

        Args:
            sheetId:  (required)
            workbookId:  (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def sheetrocks_list_files(
        self,
        workbookId: str,
    ) -> Dict[str, Any]:
        """Lists all files attached to or associated with a specific SheetRocks workbook, identified by its workbook ID. Use this tool when you need to discover files linked to a workbook. Does not return workbook or cell data. Read-only; no data is modified.

        Args:
            workbookId: The unique identifier for the workbook. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def sheetrocks_list_workbooks(
        self,
    ) -> Dict[str, Any]:
        """Lists all workbooks available in your SheetRocks account. Use this tool when you need an overview of all workbooks or want to retrieve workbook IDs for use in subsequent calls. Does not return sheet-level or cell-level data. Read-only; no data is modified.
        Returns:
            API response as a dictionary.
        """
        ...

