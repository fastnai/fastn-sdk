"""Fastn Google Sheets connector — auto-generated type stubs.

Do not edit manually. Regenerate with `fastn connector sync`.
"""
from __future__ import annotations

from typing import Any, Dict, List, Optional, TypedDict


class _GoogleSheetsCreateSpreadsheetProperties(TypedDict, total=False):
    title: str

class GoogleSheetsConnector:
    """Google Sheets connector ().

    Provides 8 tools.
    """

    def google_sheets_append_sheet(
        self,
        range: str,
        spreadsheet: str,
        values: List[Any],
        valueInputOption: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Appends one or more rows of data to the end of an existing range in a Google Sheets worksheet without overwriting existing content. Use this when you need to add new records to a sheet, such as logging entries, inserting rows into a database-like sheet, or accumulating data over time. Do not use this to overwrite specific cells; use google_sheets_update_cell instead. Do not use this to create a new sheet tab; use google_sheets_create_sheet_tab instead. This operation permanently adds rows to the sheet; appended data must be deleted manually and cannot be undone programmatically.

        Args:
            range: Range of cells to update within the Google Sheet (e.g., 'Sheet1!A1:B2'). When appending, the range can be the sheet name only (e.g., 'Sheet1'). (required)
            spreadsheet: ID of the Google Sheet to update. (required)
            values: An array of rows, where each row is an array of cell values to be appended to the Google Sheet. (required)
            valueInputOption: Option to specify how the input data should be interpreted (e.g., 'RAW', 'USER_ENTERED').
        Returns:
            API response as a dictionary.
        """
        ...

    def google_sheets_create_sheet_tab(
        self,
        requests: Optional[List[Any]] = None,
        sheetId: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Creates a new sheet tab within an existing spreadsheet in the specified connector. Use this tool when you need to add a new worksheet to a Google Sheet, such as organizing data by category or creating a dedicated tab for a specific dataset. Do not use this tool if you only need to add data to an existing sheet tab; use google_sheets_update_cell instead.

        Args:
            requests: 
            sheetId: 
        Returns:
            API response as a dictionary.
        """
        ...

    def google_sheets_create_spreadsheet(
        self,
        properties: _GoogleSheetsCreateSpreadsheetProperties,
        dataSources: Optional[List[Any]] = None,
        developerMetadata: Optional[List[Any]] = None,
        namedRanges: Optional[List[Any]] = None,
        sheets: Optional[List[Any]] = None,
        spreadsheetId: Optional[str] = None,
        spreadsheetUrl: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Creates a new spreadsheet in the specified connector environment. Use this when you need to create a blank spreadsheet or a new spreadsheet with initial properties such as title and locale. This action cannot be undone; the spreadsheet will be created and persist until manually deleted. Do not use this to modify an existing spreadsheet (use update tools instead) or to retrieve spreadsheet data (use google_sheets_get_spreadsheet instead).

        Args:
            properties: Additional properties related to the request body. (required)
            dataSources: List of data sources used by the Google Sheet.
            developerMetadata: List of developer metadata entries.
            namedRanges: List of named ranges in the Google Sheet.
            sheets: List of sheet names to process in Google Sheets.
            spreadsheetId: ID of the Google Sheet.
            spreadsheetUrl: URL of the Google Sheet.
        Returns:
            API response as a dictionary.
        """
        ...

    def google_sheets_get_data_from_sheet(
        self,
        sheetId: str,
        sheetRange: str,
        sheetName: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Retrieves cell values from a specific range in a Google Sheet by sheet name and range coordinates. Use this when you need to read existing spreadsheet data, such as pulling values from a specific range (e.g., A1:C10) to analyze, display, or process them in your application. Do not use this to write or modify data; use google_sheets_append_sheet or update operations instead.

        Args:
            sheetId: The unique identifier for the Google Sheet. (required)
            sheetRange: The range of cells to access within the Google Sheet (e.g., A1:B10). (required)
            sheetName: The Sheet Tab Name of the Google Sheet. Found at the bottom of the Google sheets.
        Returns:
            API response as a dictionary.
        """
        ...

    def google_sheets_get_spreadsheet(
        self,
        includeGridData: str,
        ranges: str,
        spreadsheetId: str,
    ) -> Dict[str, Any]:
        """Retrieves the metadata and structural properties of a single Google Sheets spreadsheet by its spreadsheet ID, including sheet tab names, dimensions, and settings. Use this when you have a spreadsheet ID and need to inspect its structure before reading or writing data. Do not use this to list all available spreadsheets; use google_sheets_list_sheets instead. Do not use this to read cell values; use google_sheets_get_data_from_sheet instead. Do not use this to create a new spreadsheet; use google_sheets_create_spreadsheet instead.

        Args:
            includeGridData: Indicates whether to include grid data in the response.  (true/false or similar) (required)
            ranges: Specifies the ranges of data to retrieve from the Google Sheet. (required)
            spreadsheetId: The unique identifier of the Google Sheet. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def google_sheets_list_sheet_tabs(
        self,
        sheetId: str,
        fields: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Lists all sheet tabs (worksheets) within a specific Google Sheets spreadsheet identified by its spreadsheet ID. Use this when you need to discover the names or properties of all tabs in a spreadsheet before reading or writing data. Do not use this to read cell data from within a sheet; use google_sheets_get_data_from_sheet instead. Do not use this to list all spreadsheets; use google_sheets_list_sheets instead.

        Args:
            sheetId: The Google Sheets spreadsheet ID identifying the target spreadsheet. (required)
            fields: A comma-separated list of fields to include in the response.
        Returns:
            API response as a dictionary.
        """
        ...

    def google_sheets_list_sheets(
        self,
        nextPageToken: Optional[str] = None,
        pageSize: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Lists all spreadsheets accessible in the connected Google Drive environment. Use this when you need to discover available spreadsheets without knowing their IDs. Do not use this to list the tabs within a single spreadsheet; use google_sheets_list_sheet_tabs instead. Do not use this to retrieve the content or structure of a specific spreadsheet; use google_sheets_get_spreadsheet instead.

        Args:
            nextPageToken: 
            pageSize: Page size for My connectors endpoint.
        Returns:
            API response as a dictionary.
        """
        ...

    def google_sheets_update_cell(
        self,
        majorDimension: str,
        range: str,
        sheetId: str,
        sheetTabName: str,
        valueInputOption: str,
        values: List[Any],
        includeValuesInResponse: Optional[bool] = None,
    ) -> Dict[str, Any]:
        """Updates the value of a specific cell or a range of cells in an existing Google Sheets worksheet. Use this when you need to overwrite or set values in one or more cells, such as updating a number, changing text, or entering a formula. Do not use this to add new rows of data without overwriting; use google_sheets_append_sheet instead. Do not use this to create a new sheet tab; use google_sheets_create_sheet_tab instead. This operation overwrites existing cell values immediately and cannot be undone programmatically.

        Args:
            majorDimension: Indicates whether the data is arranged in rows ('ROWS') or columns ('COLUMNS'). (required)
            range: The A1 notation of the range to which the data should be written (e.g., 'Sheet1!A1:B2'). (required)
            sheetId: The ID of the Google Sheet. (required)
            sheetTabName: The name of the sheet tab. (required)
            valueInputOption: Specifies how values are interpreted (e.g., 'RAW', 'USER_ENTERED'). (required)
            values: A two-dimensional array of values to write to the sheet. (required)
            includeValuesInResponse: Whether to include values in the API response.
        Returns:
            API response as a dictionary.
        """
        ...

