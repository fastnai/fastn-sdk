"""Fastn Tabidoo connector — auto-generated type stubs.

Do not edit manually. Regenerate with `fastn connector sync`.
"""
from __future__ import annotations

from typing import Any, Dict, List, Optional


class TabidooConnector:
    """Tabidoo connector ().

    Provides 10 tools.
    """

    def create_data_record(
        self,
        fields: Optional[Dict[str, Any]] = None,
    ) -> Dict[str, Any]:
        """Creates a new data record in a specified table using the specified connector.

        Args:
            fields: The fields and their values to be updated or created.
        Returns:
            API response as a dictionary.
        """
        ...

    def delete_data_record(
        self,
        appId: str,
        recordId: str,
        tableId: str,
    ) -> Dict[str, Any]:
        """Deletes a specific data record from a specified table using the specified connector.

        Args:
            appId: The ID of the application. (required)
            recordId: The ID of the record. (required)
            tableId: The ID of the table. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def get_all_applications(
        self,
    ) -> Dict[str, Any]:
        """Retrieves a list of all applications using the specified connector.
        Returns:
            API response as a dictionary.
        """
        ...

    def get_all_tables(
        self,
        appId: str,
    ) -> Dict[str, Any]:
        """Obtains a list of all tables available within the database via the specified connector.

        Args:
            appId: The ID of the application. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def get_application(
        self,
        appId: str,
    ) -> Dict[str, Any]:
        """Fetches detailed information about a specific application using the specified connector.

        Args:
            appId: The ID of the application. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def get_records(
        self,
        filter: Optional[str] = None,
        limit: Optional[str] = None,
        skip: Optional[str] = None,
        sort: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Fetches records from a specific table using the specified connector.

        Args:
            filter: Filter criteria for the data.
            limit: Maximum number of records to return.
            skip: Number of records to skip.
            sort: Sorting criteria for the data.
        Returns:
            API response as a dictionary.
        """
        ...

    def get_records_count(
        self,
        appId: str,
        tableId: str,
    ) -> Dict[str, Any]:
        """Counts the total number of records in a specific table using the specified connector.

        Args:
            appId: Identifier for the application. (required)
            tableId: Identifier for the target table. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def get_single_record(
        self,
        appId: str,
        recordId: str,
        tableId: str,
    ) -> Dict[str, Any]:
        """Retrieves a single record from a specific table using the specified connector.

        Args:
            appId: Identifier for the application. (required)
            recordId: Identifier for the specific record. (required)
            tableId: Identifier for the data table. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def get_table(
        self,
        appId: str,
        tableId: str,
    ) -> Dict[str, Any]:
        """Retrieves detailed information about a specific table using the specified connector.

        Args:
            appId: The ID of the application. (required)
            tableId: The ID of the table. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def update_data_record(
        self,
        fields: Optional[Dict[str, Any]] = None,
    ) -> Dict[str, Any]:
        """Updates an existing data record in a specified table using the specified connector.

        Args:
            fields: An object containing the fields and their values to update or create.
        Returns:
            API response as a dictionary.
        """
        ...

