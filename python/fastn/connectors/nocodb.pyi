"""Fastn NocoDB connector — auto-generated type stubs.

Do not edit manually. Regenerate with `fastn connector sync`.
"""
from __future__ import annotations

from typing import Any, Dict, List, Optional


class NocodbConnector:
    """NocoDB connector ().

    Provides 8 tools.
    """

    def count_record(
        self,
        viewId: Optional[str] = None,
        where: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Counts the number of records in the specified database using the database connector.

        Args:
            viewId: ID of the view to be used for the request.
            where: A WHERE clause to filter the data.
        Returns:
            API response as a dictionary.
        """
        ...

    def create_record(
        self,
    ) -> Dict[str, Any]:
        """Creates a new record in the specified database using the database connector.
        Returns:
            API response as a dictionary.
        """
        ...

    def delete_record(
        self,
    ) -> Dict[str, Any]:
        """Deletes an existing record from the specified database using the database connector.
        Returns:
            API response as a dictionary.
        """
        ...

    def get_linked_records(
        self,
        fields: Optional[str] = None,
        limit: Optional[str] = None,
        offset: Optional[str] = None,
        sort: Optional[str] = None,
        where: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Retrieves linked records associated with a specific record in the database using the database connector.

        Args:
            fields: Comma-separated list of fields to retrieve.
            limit: Maximum number of records to return.
            offset: Number of records to skip.
            sort: Field to sort by (e.g., 'name ASC', 'date DESC').
            where: SQL WHERE clause for filtering records.
        Returns:
            API response as a dictionary.
        """
        ...

    def get_record(
        self,
        fields: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Fetches details of a specific record from the database using the database connector.

        Args:
            fields: Specifies which fields to include in the response.
        Returns:
            API response as a dictionary.
        """
        ...

    def get_tables_records(
        self,
        fields: Optional[str] = None,
        limit: Optional[str] = None,
        offset: Optional[str] = None,
        sort: Optional[str] = None,
        viewId: Optional[str] = None,
        where: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Gets all records from the specified tables in the database using the database connector.

        Args:
            fields: Comma-separated list of fields to include in the result.
            limit: Number of records to return.
            offset: Number of records to skip.
            sort: Comma-separated list of fields to sort by.
            viewId: ID of the view to use for data retrieval.
            where: WHERE clause for filtering the data.
        Returns:
            API response as a dictionary.
        """
        ...

    def link_records(
        self,
    ) -> Dict[str, Any]:
        """Links two records together in the database using the database connector.
        Returns:
            API response as a dictionary.
        """
        ...

    def update_record(
        self,
    ) -> Dict[str, Any]:
        """Updates an existing record in the specified database using the database connector.
        Returns:
            API response as a dictionary.
        """
        ...

