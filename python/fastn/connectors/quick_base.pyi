"""Fastn Quick Base connector — auto-generated type stubs.

Do not edit manually. Regenerate with `fastn connector sync`.
"""
from __future__ import annotations

from typing import Any, Dict, List, Optional


class QuickBaseConnector:
    """Quick Base connector ().

    Provides 12 tools.
    """

    def create_field(
        self,
        tableId: str,
    ) -> Dict[str, Any]:
        """Creates a new field within a specified table in the database connector.

        Args:
            tableId:  (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def create_table(
        self,
        appId: str,
    ) -> Dict[str, Any]:
        """Creates a new table in the database connector.

        Args:
            appId: The ID of the Quick Base application. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def delete_fields(
        self,
        tableId: str,
    ) -> Dict[str, Any]:
        """Deletes specified fields from a table in the database connector.

        Args:
            tableId: The ID of the Quick Base table. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def delete_records(
        self,
        from: str,
        where: str,
    ) -> Dict[str, Any]:
        """Deletes specified records from a specified table in the database connector.

        Args:
            from: Specifies the table from which to retrieve data. (required)
            where: A condition to filter the retrieved data. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def delete_table(
        self,
        appId: str,
    ) -> Dict[str, Any]:
        """Deletes an existing table from the database connector.

        Args:
            appId: The ID of the Quick Base application. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def get_field(
        self,
        tableId: str,
        includeFieldPerms: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Fetches details of a specific field from a table in the database connector.

        Args:
            tableId: The ID of the Quick Base table. (required)
            includeFieldPerms: Indicates whether to include field permissions in the response.
        Returns:
            API response as a dictionary.
        """
        ...

    def get_fields(
        self,
        tableId: str,
        includeFieldPerms: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Retrieves a list of fields from a specified table in the database connector.

        Args:
            tableId: The ID of the Quick Base table. (required)
            includeFieldPerms: Indicates whether to include field permissions in the response (optional).
        Returns:
            API response as a dictionary.
        """
        ...

    def get_table(
        self,
        appId: str,
    ) -> Dict[str, Any]:
        """Fetches details of a specific table from the database connector.

        Args:
            appId: The ID of the Quick Base application. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def get_tables(
        self,
        appId: str,
    ) -> Dict[str, Any]:
        """Retrieves a list of tables from the database connector.

        Args:
            appId: The ID of the Quick Base application. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def insert_record(
        self,
        data: List[Any],
        to: str,
        fieldsToReturn: Optional[List[Any]] = None,
    ) -> Dict[str, Any]:
        """Inserts a new record into a specified table in the database connector.

        Args:
            data:  (required)
            to: Target Quick Base table or database. (required)
            fieldsToReturn: List of field IDs to be returned in the response.
        Returns:
            API response as a dictionary.
        """
        ...

    def update_field(
        self,
        tableId: str,
    ) -> Dict[str, Any]:
        """Updates the details of a specific field in a table in the database connector.

        Args:
            tableId: The ID of the Quick Base table. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def update_table(
        self,
        appId: str,
    ) -> Dict[str, Any]:
        """Updates the schema or structure of an existing table in the database connector.

        Args:
            appId: ID of the Quick Base application. (required)
        Returns:
            API response as a dictionary.
        """
        ...

