"""Fastn Timetonic connector — auto-generated type stubs.

Do not edit manually. Regenerate with `fastn connector sync`.
"""
from __future__ import annotations

from typing import Any, Dict, List, Optional, TypedDict


class TimetonicConnector:
    """Timetonic connector ().

    Provides 8 tools.
    """

    def timetonic_add_table_row(
        self,
        b_c: str,
        b_o: str,
        catId: str,
        fieldValues: str,
    ) -> Dict[str, Any]:
        """Adds a new row to a specified table within a Timetonic book. Use this tool when you need to insert a new record into a table. Do not use this tool to update an existing row or delete a row. This action creates a new persistent record in the table.

        Args:
            b_c: Description for b_c field. (required)
            b_o: Description for b_o field. (required)
            catId: Category ID for the request. (required)
            fieldValues: Field values for the request. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def timetonic_compute_table_operation(
        self,
        b_o: str,
        catId: str,
        operation: str,
    ) -> Dict[str, Any]:
        """Performs a mathematical aggregation operation (such as sum, average, count, min, or max) on the values of a column within a Timetonic table. Use this tool when you need to calculate aggregate statistics on table data without retrieving raw rows. Do not use this tool to retrieve individual row values or modify table data. This is a read-only computation with no side effects.

        Args:
            b_o: Description of the b_o parameter. (required)
            catId: ID of the category. (required)
            operation: Type of operation to perform. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def timetonic_delete_table_row(
        self,
        b_c: str,
        b_o: str,
        catId: str,
        rowId: str,
    ) -> Dict[str, Any]:
        """Deletes a specific row from a table within a Timetonic book. Use this tool when you need to permanently remove a record from a table. Do not use this tool to update a row or delete an entire table. This action is destructive and irreversible; the deleted row cannot be recovered.

        Args:
            b_c: Description for b_c field. (required)
            b_o: Description for b_o field. (required)
            catId: Category ID. (required)
            rowId: Row ID. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def timetonic_get_book_info(
        self,
        b_c: str,
        b_o: str,
    ) -> Dict[str, Any]:
        """Retrieves detailed metadata and information about a specific book in Timetonic using its unique identifier. Use this tool when you need to look up properties of a book such as its name, owner, or configuration. Do not use this tool to retrieve a list of all books or to access table contents within the book. This is a read-only operation with no side effects.

        Args:
            b_c: Description of the b_c parameter. (required)
            b_o: Description of the b_o parameter. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def timetonic_list_all_books(
        self,
    ) -> Dict[str, Any]:
        """Retrieves a list of all books available in the Timetonic workspace. Use this tool when you need to discover all books accessible to the authenticated user. Do not use this tool to retrieve detailed information about a single book or to access table contents; use the get book info or list table values tools for those purposes. This is a read-only operation with no side effects.
        Returns:
            API response as a dictionary.
        """
        ...

    def timetonic_list_book_tables(
        self,
        b_c: str,
        b_o: str,
        includeFields: Optional[bool] = None,
    ) -> Dict[str, Any]:
        """Retrieves a list of all tables associated with a specified book in Timetonic. Use this tool when you need to discover what tables exist within a book before querying or modifying their contents. Do not use this tool to retrieve the row values within a table; use the list table values tool for that. This is a read-only operation with no side effects.

        Args:
            b_c: Description for b_c field. (required)
            b_o: Description for b_o field. (required)
            includeFields: Indicates whether to include fields.
        Returns:
            API response as a dictionary.
        """
        ...

    def timetonic_list_table_values(
        self,
        b_o: str,
        catId: str,
        maxRows: Optional[str] = None,
        offset: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Retrieves a list of all values contained within a specified table in a Timetonic book. Use this tool when you need to read the full contents of a table. Do not use this tool to add, update, or delete rows. This is a read-only operation with no side effects.

        Args:
            b_o: Description needed for b_o field. (required)
            catId: ID of the category. (required)
            maxRows: Maximum number of rows to retrieve.
            offset: Offset for pagination.
        Returns:
            API response as a dictionary.
        """
        ...

    def timetonic_update_table_row(
        self,
        b_c: str,
        b_o: str,
        catId: str,
        fieldValues: str,
        rowId: str,
    ) -> Dict[str, Any]:
        """Updates an existing row in a specified table within a Timetonic book. Use this tool when you need to modify the values of an existing record in a table. Do not use this tool to add a new row or delete an existing row. This action overwrites existing row data and the change is persisted immediately.

        Args:
            b_c: Description for b_c field. (required)
            b_o: Description for b_o field. (required)
            catId: ID of the category. (required)
            fieldValues: Values of the fields. (required)
            rowId: ID of the row. (required)
        Returns:
            API response as a dictionary.
        """
        ...

