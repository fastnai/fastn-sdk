"""Fastn Google Sheets connector — auto-generated type stubs.

Do not edit manually. Regenerate with `fastn connector sync`.
"""
from __future__ import annotations

from typing import Any, Dict, List, Optional


class GoogleSheetsConnector:
    """Google Sheets connector ().

    Provides 8 tools.
    """

    def append_sheet(
        self,
        valueInputOption: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Appends a new sheet to an existing spreadsheet in the specified connector.

        Args:
            valueInputOption: Option to specify how the input data should be interpreted (e.g., 'RAW', 'USER_ENTERED').
        Returns:
            API response as a dictionary.
        """
        ...

    def create_sheet_tab(
        self,
        requests: Optional[List[Any]] = None,
    ) -> Dict[str, Any]:
        """Creates a new sheet tab within an existing spreadsheet in the specified connector.

        Args:
            requests: 
        Returns:
            API response as a dictionary.
        """
        ...

    def create_spreadsheet(
        self,
        properties: Dict[str, Any],
        dataSources: Optional[List[Any]] = None,
        developerMetadata: Optional[List[Any]] = None,
        namedRanges: Optional[List[Any]] = None,
        sheets: Optional[List[Any]] = None,
        spreadsheetId: Optional[str] = None,
        spreadsheetUrl: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Creates a new spreadsheet in the specified connector environment.

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

    def get_data_from_sheet(
        self,
        sheetId: str,
        sheetRange: str,
        sheetName: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Fetches data from a specific sheet within a spreadsheet in the specified connector.

        Args:
            sheetId: The unique identifier for the Google Sheet. (required)
            sheetRange: The range of cells to access within the Google Sheet (e.g., A1:B10). (required)
            sheetName: The Sheet Tab Name of the Google Sheet. Found at the bottom of the Google sheets.
        Returns:
            API response as a dictionary.
        """
        ...

    def get_sheet_tabs(
        self,
        fields: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Retrieves the tabs of a specific sheet within a spreadsheet in the specified connector environment.

        Args:
            fields: A comma-separated list of fields to include in the response.
        Returns:
            API response as a dictionary.
        """
        ...

    def get_sheets(
        self,
        nextPageToken: Optional[str] = None,
        pageSize: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Lists all sheets within a given spreadsheet in the specified connector environment.

        Args:
            nextPageToken: 
            pageSize: Page size for My connectors endpoint.
        Returns:
            API response as a dictionary.
        """
        ...

    def get_spreadsheet(
        self,
        includeGridData: str,
        ranges: str,
    ) -> Dict[str, Any]:
        """Retrieves an existing spreadsheet from the specified connector environment.

        Args:
            includeGridData: Indicates whether to include grid data in the response.  (true/false or similar) (required)
            ranges: Specifies the ranges of data to retrieve from the Google Sheet. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def update_cell(
        self,
        valueInputOption: str,
        includeValuesInResponse: Optional[bool] = None,
    ) -> Dict[str, Any]:
        """Updates a specific cell's content in a sheet within a spreadsheet in the specified connector environment.

        Args:
            valueInputOption: Specifies how values are interpreted (e.g., 'RAW', 'USER_ENTERED'). (required)
            includeValuesInResponse: Whether to include values in the API response.
        Returns:
            API response as a dictionary.
        """
        ...

