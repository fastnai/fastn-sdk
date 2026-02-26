"""Fastn Timetonic connector — auto-generated type stubs.

Do not edit manually. Regenerate with `fastn connector sync`.
"""
from __future__ import annotations

from typing import Any, Dict, List, Optional


class TimetonicConnector:
    """Timetonic connector ().

    Provides 8 tools.
    """

    def add_table_row(
        self,
        b_c: str,
        b_o: str,
        catId: str,
        fieldValues: str,
    ) -> Dict[str, Any]:
        """Adds a new row to a specified table associated with a book in the library system.

        Args:
            b_c: Description for b_c field. (required)
            b_o: Description for b_o field. (required)
            catId: Category ID for the request. (required)
            fieldValues: Field values for the request. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def compute_table_operation(
        self,
        b_o: str,
        catId: str,
        operation: str,
    ) -> Dict[str, Any]:
        """Performs a specified mathematical operation (such as sum, average, etc.) on the values of a table in the library system.

        Args:
            b_o: Description of the b_o parameter. (required)
            catId: ID of the category. (required)
            operation: Type of operation to perform. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def delete_table_row(
        self,
        b_c: str,
        b_o: str,
        catId: str,
        rowId: str,
    ) -> Dict[str, Any]:
        """Deletes a row from a specified table related to a book in the library system.

        Args:
            b_c: Description for b_c field. (required)
            b_o: Description for b_o field. (required)
            catId: Category ID. (required)
            rowId: Row ID. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def get_all_books(
        self,
    ) -> Dict[str, Any]:
        """Retrieves a list of all books available in the library system.
        Returns:
            API response as a dictionary.
        """
        ...

    def get_book_info(
        self,
        b_c: str,
        b_o: str,
    ) -> Dict[str, Any]:
        """Fetches detailed information about a specific book in the library system using its unique identifier.

        Args:
            b_c: Description of the b_c parameter. (required)
            b_o: Description of the b_o parameter. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def get_book_tables(
        self,
        b_c: str,
        b_o: str,
        includeFields: Optional[bool] = None,
    ) -> Dict[str, Any]:
        """Obtains the tables associated with the specified book in the library system.

        Args:
            b_c: Description for b_c field. (required)
            b_o: Description for b_o field. (required)
            includeFields: Indicates whether to include fields.
        Returns:
            API response as a dictionary.
        """
        ...

    def get_table_values(
        self,
        b_o: str,
        catId: str,
        maxRows: Optional[str] = None,
        offset: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Fetches the values contained within a specified table related to a book in the library system.

        Args:
            b_o: Description needed for b_o field. (required)
            catId: ID of the category. (required)
            maxRows: Maximum number of rows to retrieve.
            offset: Offset for pagination.
        Returns:
            API response as a dictionary.
        """
        ...

    def update_table_row(
        self,
        b_c: str,
        b_o: str,
        catId: str,
        fieldValues: str,
        rowId: str,
    ) -> Dict[str, Any]:
        """Updates an existing row in a specified table associated with a book in the library system.

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

