"""Fastn Rows connector — auto-generated type stubs.

Do not edit manually. Regenerate with `fastn connector sync`.
"""
from __future__ import annotations

from typing import Any, Dict, List, Optional


class RowsConnector:
    """Rows connector ().

    Provides 18 tools.
    """

    def append_values(
        self,
        values: List[Any],
    ) -> Dict[str, Any]:
        """Appends new values to the specified cells in a spreadsheet through the connector.

        Args:
            values: A list of arrays representing the rows of data to write. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def create_page(
        self,
        name: str,
    ) -> Dict[str, Any]:
        """Creates a new page within the selected workspace using the connector.

        Args:
            name: Name of the row. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def create_spreadsheet(
        self,
        name: str,
        pages: List[Any],
    ) -> Dict[str, Any]:
        """Creates a new spreadsheet within the active connector's context.

        Args:
            name: Name of the data set. (required)
            pages:  (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def create_table(
        self,
        name: str,
    ) -> Dict[str, Any]:
        """Creates a new table within the active spreadsheet via the connector.

        Args:
            name: Name of the entity. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def delete_page(
        self,
        pageId: str,
        spreadsheetId: str,
    ) -> Dict[str, Any]:
        """Deletes a specified page from the workspace using the connector.

        Args:
            pageId: The ID of the specific page within the spreadsheet. (required)
            spreadsheetId: The unique identifier for the Google Sheet. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def delete_spreadsheet(
        self,
        spreadsheetId: str,
    ) -> Dict[str, Any]:
        """Deletes a specified spreadsheet from the connector's environment.

        Args:
            spreadsheetId: The ID of the Google Sheet to access. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def delete_table(
        self,
        spreadsheetId: str,
        tableId: str,
    ) -> Dict[str, Any]:
        """Deletes a specified table from the connected spreadsheet environment.

        Args:
            spreadsheetId: The unique identifier of the Google Sheet. (required)
            tableId: The unique identifier of the table within the spreadsheet. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def execute_computation(
        self,
        datetime_render_option: Optional[str] = None,
        value_render_option: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Executes a computation or formula within a spreadsheet context through the connector.

        Args:
            datetime_render_option: How dates, times, and durations should be presented in the response.
            value_render_option: How values should be presented in the response.
        Returns:
            API response as a dictionary.
        """
        ...

    def get_cell(
        self,
        datetime_render_option: Optional[str] = None,
        limit: Optional[str] = None,
        major_dimension: Optional[str] = None,
        page_token: Optional[str] = None,
        value_render_option: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Fetches the value of a specific cell in a spreadsheet facilitated by the connector.

        Args:
            datetime_render_option: Controls how dates, times, and durations are represented in the response.
            limit: Limits the number of rows returned.
            major_dimension: Indicates whether rows or columns should be the major dimension of the response.
            page_token: Token for pagination; used to retrieve the next page of results.
            value_render_option: Controls how values are represented in the response (e.g., 'FORMATTED_VALUE', 'UNFORMATTED_VALUE').
        Returns:
            API response as a dictionary.
        """
        ...

    def get_folders_(
        self,
        limit: str,
        offset: str,
    ) -> Dict[str, Any]:
        """Fetches all folders within a specified workspace using the relevant connector.

        Args:
            limit: The maximum number of rows to return. (required)
            offset: The number of rows to skip before returning results. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def get_spreadsheet(
        self,
        spreadsheetId: str,
    ) -> Dict[str, Any]:
        """Fetches details of a specific spreadsheet using its identifier in the connector's environment.

        Args:
            spreadsheetId: The unique identifier of the Google Sheet. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def get_spreadsheets(
        self,
        folder_id: Optional[str] = None,
        limit: Optional[str] = None,
        offset: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Retrieves a list of spreadsheets available in the current connector's environment.

        Args:
            folder_id: The ID of the folder containing the rows to retrieve.
            limit: The maximum number of rows to return.
            offset: The number of rows to skip before returning the results.
        Returns:
            API response as a dictionary.
        """
        ...

    def get_values(
        self,
        datetime_render_option: Optional[str] = None,
        limit: Optional[str] = None,
        major_dimension: Optional[str] = None,
        page_token: Optional[str] = None,
        value_render_option: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Retrieves values from specified cells or ranges in a spreadsheet using the connector.

        Args:
            datetime_render_option: Controls how dates and times are rendered in the response. Options might include 'SERIAL_NUMBER', 'FORMATTED_STRING'.
            limit: The maximum number of rows to return.
            major_dimension: Indicates whether the data is arranged by rows or columns.  Typically 'ROWS' or 'COLUMNS'.
            page_token: A token to retrieve the next page of results in paginated responses.
            value_render_option: Specifies how values should be rendered in the response.  Options might include 'FORMATTED_VALUE', 'UNFORMATTED_VALUE', or 'FORMULA'.
        Returns:
            API response as a dictionary.
        """
        ...

    def get_workspaces(
        self,
    ) -> Dict[str, Any]:
        """Retrieves a list of workspaces from the appropriate connector.
        Returns:
            API response as a dictionary.
        """
        ...

    def overwrite_cells_(
        self,
        cells: List[Any],
    ) -> Dict[str, Any]:
        """Overwrites specified cells with new data in a spreadsheet using the connector.

        Args:
            cells:  (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def update_page(
        self,
        name: str,
    ) -> Dict[str, Any]:
        """Updates the content or properties of a specified page in the connector's context.

        Args:
            name: The name associated with the request. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def update_spreadsheet(
        self,
        name: str,
    ) -> Dict[str, Any]:
        """Updates an existing spreadsheet with new data or configurations through the connector.

        Args:
            name: The name of the row. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def update_table(
        self,
        name: str,
    ) -> Dict[str, Any]:
        """Updates an existing table in the spreadsheet using the relevant connector settings.

        Args:
            name: Name of the row or element. (required)
        Returns:
            API response as a dictionary.
        """
        ...

