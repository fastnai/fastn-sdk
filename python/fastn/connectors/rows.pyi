"""Fastn Rows connector — auto-generated type stubs.

Do not edit manually. Regenerate with `fastn connector sync`.
"""
from __future__ import annotations

from typing import Any, Dict, List, Optional, TypedDict


class RowsConnector:
    """Rows connector ().

    Provides 18 tools.
    """

    def rows_append_values(
        self,
        range: str,
        spreadsheetId: str,
        tableId: str,
        values: List[Any],
    ) -> Dict[str, Any]:
        """Appends new data values to a specified range within a table in a Rows spreadsheet, adding rows below existing content. Use this when you need to add new records without overwriting existing data. Do not use this to replace existing cell values — use rows_overwrite_cells for full replacement.

        Args:
            range: The A1 notation of the values to update. (required)
            spreadsheetId: The ID of the spreadsheet to update. (required)
            tableId: The ID of the table to update. (required)
            values: A list of arrays representing the rows of data to write. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def rows_create_page(
        self,
        name: str,
        spreadsheetId: str,
    ) -> Dict[str, Any]:
        """Creates a new page within an existing Rows spreadsheet. Use this when you need to add a new sheet or tab to a spreadsheet by providing the spreadsheet ID. Do not use this to create a new spreadsheet — use rows_create_spreadsheet for that.

        Args:
            name: Name of the row. (required)
            spreadsheetId: The unique identifier of the Google Sheet. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def rows_create_spreadsheet(
        self,
        folderId: str,
        name: str,
        pages: List[Any],
    ) -> Dict[str, Any]:
        """Creates a new Rows spreadsheet inside a specified folder. Use this when you need to provision a new spreadsheet by providing the target folder ID. Do not use this to create pages or tables within an existing spreadsheet — use rows_create_page or rows_create_table for those.

        Args:
            folderId: The ID of the folder containing the rows. (required)
            name: Name of the data set. (required)
            pages:  (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def rows_create_table(
        self,
        name: str,
        pageId: str,
        spreadsheetId: str,
    ) -> Dict[str, Any]:
        """Creates a new table on a specified page within a Rows spreadsheet. Use this when you need to add a structured table to an existing page by providing the spreadsheet ID and page ID. Do not use this to create a new page — use rows_create_page for that.

        Args:
            name: Name of the entity. (required)
            pageId: The ID of the page within the spreadsheet. (required)
            spreadsheetId: The ID of the Google Sheet. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def rows_delete_page(
        self,
        pageId: str,
        spreadsheetId: str,
    ) -> Dict[str, Any]:
        """Permanently deletes a specified page from a Rows spreadsheet. Use this when you need to remove an entire page and all tables and data it contains. This action is irreversible — all content on the page will be lost and cannot be recovered.

        Args:
            pageId: The ID of the specific page within the spreadsheet. (required)
            spreadsheetId: The unique identifier for the Google Sheet. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def rows_delete_spreadsheet(
        self,
        spreadsheetId: str,
    ) -> Dict[str, Any]:
        """Permanently deletes a specified Rows spreadsheet and all of its pages, tables, and data. Use this when you need to completely remove a spreadsheet by its ID. This action is irreversible — all data within the spreadsheet will be permanently lost and cannot be recovered.

        Args:
            spreadsheetId: The ID of the Google Sheet to access. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def rows_delete_table(
        self,
        spreadsheetId: str,
        tableId: str,
    ) -> Dict[str, Any]:
        """Permanently deletes a specific table from a Rows spreadsheet. Use this when you need to remove an entire table and all its data from a spreadsheet by providing the spreadsheet ID and table ID. This action is irreversible — all data within the table will be lost and cannot be recovered.

        Args:
            spreadsheetId: The unique identifier of the Google Sheet. (required)
            tableId: The unique identifier of the table within the spreadsheet. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def rows_execute_computation(
        self,
        spreadsheetId: str,
        tables: List[Any],
        datetime_render_option: Optional[str] = None,
        value_render_option: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Executes a live computation or formula within a Rows spreadsheet and returns the result. Use this when you need to evaluate a formula or trigger a live data computation on a specific spreadsheet. Do not use this to read static cell values — use rows_get_cell or rows_get_values instead.

        Args:
            spreadsheetId: The ID of the Google Sheet to retrieve data from. (required)
            tables:  (required)
            datetime_render_option: How dates, times, and durations should be presented in the response.
            value_render_option: How values should be presented in the response.
        Returns:
            API response as a dictionary.
        """
        ...

    def rows_get_cell(
        self,
        range: str,
        spreadsheetId: str,
        tableId: str,
        datetime_render_option: Optional[str] = None,
        limit: Optional[str] = None,
        major_dimension: Optional[str] = None,
        page_token: Optional[str] = None,
        value_render_option: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Retrieves the value of a single cell or small range from a specific table in a Rows spreadsheet. Use this when you need to read the current content of a particular cell identified by its range address. Do not use this to retrieve multi-row value sets — use rows_get_values for broader range reads.

        Args:
            range: The A1 notation of the data range to retrieve (e.g., 'Sheet1!A1:B10'). (required)
            spreadsheetId: The ID of the Google Sheet. (required)
            tableId: The ID of the table within the spreadsheet (optional). (required)
            datetime_render_option: Controls how dates, times, and durations are represented in the response.
            limit: Limits the number of rows returned.
            major_dimension: Indicates whether rows or columns should be the major dimension of the response.
            page_token: Token for pagination; used to retrieve the next page of results.
            value_render_option: Controls how values are represented in the response (e.g., 'FORMATTED_VALUE', 'UNFORMATTED_VALUE').
        Returns:
            API response as a dictionary.
        """
        ...

    def rows_get_spreadsheet(
        self,
        spreadsheetId: str,
    ) -> Dict[str, Any]:
        """Retrieves the metadata and structure of a specific Rows spreadsheet by its ID, including its pages and tables. Use this when you need details about a single spreadsheet. To list all available spreadsheets, use rows_list_spreadsheets instead.

        Args:
            spreadsheetId: The unique identifier of the Google Sheet. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def rows_get_values(
        self,
        range: str,
        spreadsheetId: str,
        tableId: str,
        datetime_render_option: Optional[str] = None,
        limit: Optional[str] = None,
        major_dimension: Optional[str] = None,
        page_token: Optional[str] = None,
        value_render_option: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Retrieves the data values from a specified range within a table in a Rows spreadsheet. Use this when you need to read the contents of multiple cells or a range of rows and columns. Do not use this to retrieve table metadata or cell formatting — it returns raw data values only.

        Args:
            range: The A1 notation of the range of cells to retrieve. (required)
            spreadsheetId: The ID of the Google Sheet spreadsheet. (required)
            tableId: The ID of the table within the spreadsheet (optional, may not be needed depending on the API). (required)
            datetime_render_option: Controls how dates and times are rendered in the response. Options might include 'SERIAL_NUMBER', 'FORMATTED_STRING'.
            limit: The maximum number of rows to return.
            major_dimension: Indicates whether the data is arranged by rows or columns.  Typically 'ROWS' or 'COLUMNS'.
            page_token: A token to retrieve the next page of results in paginated responses.
            value_render_option: Specifies how values should be rendered in the response.  Options might include 'FORMATTED_VALUE', 'UNFORMATTED_VALUE', or 'FORMULA'.
        Returns:
            API response as a dictionary.
        """
        ...

    def rows_list_folders(
        self,
        limit: str,
        offset: str,
    ) -> Dict[str, Any]:
        """Returns a list of all folders available in the current Rows workspace. Use this when you need to discover folders and obtain their IDs, for example before creating a spreadsheet in a specific folder. Does not return the contents of each folder.

        Args:
            limit: The maximum number of rows to return. (required)
            offset: The number of rows to skip before returning results. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def rows_list_spreadsheets(
        self,
        folder_id: Optional[str] = None,
        limit: Optional[str] = None,
        offset: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Returns a list of all spreadsheets accessible in the current Rows account. Use this when you need to discover available spreadsheets and obtain their IDs. To retrieve details of a single specific spreadsheet, use rows_get_spreadsheet instead.

        Args:
            folder_id: The ID of the folder containing the rows to retrieve.
            limit: The maximum number of rows to return.
            offset: The number of rows to skip before returning the results.
        Returns:
            API response as a dictionary.
        """
        ...

    def rows_list_workspaces(
        self,
    ) -> Dict[str, Any]:
        """Returns a list of all workspaces accessible to the authenticated Rows account. Use this when you need to identify available workspaces and their IDs before operating on folders or spreadsheets within them.
        Returns:
            API response as a dictionary.
        """
        ...

    def rows_overwrite_cells(
        self,
        cells: List[Any],
        range: str,
        spreadsheetId: str,
        tableId: str,
    ) -> Dict[str, Any]:
        """Overwrites the content of a specified cell range in a Rows spreadsheet table with new data. Use this when you need to replace existing cell values entirely within a given range. This action overwrites all existing content in the targeted cells — use rows_append_values if you want to add data without overwriting.

        Args:
            cells:  (required)
            range:  (required)
            spreadsheetId:  (required)
            tableId:  (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def rows_update_page(
        self,
        name: str,
        pageId: str,
        spreadsheetId: str,
    ) -> Dict[str, Any]:
        """Updates the properties of a specified page within a Rows spreadsheet, such as its name or display settings. Use this when you need to modify page-level metadata. To update content within the page, use the appropriate table or cell tools instead.

        Args:
            name: The name associated with the request. (required)
            pageId: The ID of the page within the spreadsheet. (required)
            spreadsheetId: The ID of the Google Sheet. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def rows_update_spreadsheet(
        self,
        name: str,
        spreadsheetId: str,
    ) -> Dict[str, Any]:
        """Updates the metadata or configuration of an existing Rows spreadsheet, such as its name or settings. Use this when you need to modify spreadsheet-level properties without affecting page or cell content. To update cell data, use rows_overwrite_cells or rows_append_values instead.

        Args:
            name: The name of the row. (required)
            spreadsheetId: The ID of the Google Sheet where the row will be added. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def rows_update_table(
        self,
        name: str,
        spreadsheetId: str,
        tableId: str,
    ) -> Dict[str, Any]:
        """Updates the properties or configuration of an existing table within a Rows spreadsheet, such as its name or settings. Use this when you need to modify table-level metadata rather than cell content. To change cell data, use rows_overwrite_cells or rows_append_values instead.

        Args:
            name: Name of the row or element. (required)
            spreadsheetId: The unique identifier of the Google Sheet. (required)
            tableId: The unique identifier of the table within the spreadsheet. (required)
        Returns:
            API response as a dictionary.
        """
        ...

