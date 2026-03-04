"""Fastn Tabidoo connector — auto-generated type stubs.

Do not edit manually. Regenerate with `fastn connector sync`.
"""
from __future__ import annotations

from typing import Any, Dict, List, Optional, TypedDict


class TabidooConnector:
    """Tabidoo connector ().

    Provides 10 tools.
    """

    def tabidoo_create_data_record(
        self,
        appId: str,
        tableId: str,
        fields: Optional[Dict[str, Any]] = None,
    ) -> Dict[str, Any]:
        """Creates a new data record in a specified table within a Tabidoo application, identified by app ID and table ID. Use this to add a new row or entry to an existing table. Do not use this to update an existing record; use tabidoo_update_data_record instead.

        Args:
            appId: The ID of the application. (required)
            tableId: The ID of the table. (required)
            fields: The fields and their values to be updated or created.
        Returns:
            API response as a dictionary.
        """
        ...

    def tabidoo_delete_data_record(
        self,
        appId: str,
        recordId: str,
        tableId: str,
    ) -> Dict[str, Any]:
        """Permanently deletes a specific data record from a table in a Tabidoo application, identified by app ID, table ID, and record ID. Use this when a record must be fully removed from a table. This action is irreversible — the record cannot be recovered after deletion. Do not use this to update or clear field values; use tabidoo_update_data_record instead.

        Args:
            appId: The ID of the application. (required)
            recordId: The ID of the record. (required)
            tableId: The ID of the table. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def tabidoo_get_application(
        self,
        appId: str,
    ) -> Dict[str, Any]:
        """Returns detailed information about a specific Tabidoo application by its app ID, including its configuration and metadata. Use this when you need details about one particular application. Do not use this to list all applications; use tabidoo_list_applications instead.

        Args:
            appId: The ID of the application. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def tabidoo_get_data_record(
        self,
        appId: str,
        recordId: str,
        tableId: str,
    ) -> Dict[str, Any]:
        """Returns the full details of a single data record from a specified Tabidoo table, identified by app ID, table ID, and record ID. Use this when you need the complete field values of one specific record. Do not use this to retrieve multiple records; use tabidoo_list_data_records instead.

        Args:
            appId: Identifier for the application. (required)
            recordId: Identifier for the specific record. (required)
            tableId: Identifier for the data table. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def tabidoo_get_data_records_count(
        self,
        appId: str,
        tableId: str,
    ) -> Dict[str, Any]:
        """Returns the total number of data records in a specified table within a Tabidoo application, identified by app ID and table ID. Use this to count entries without retrieving full record data. Do not use this to retrieve the actual records; use tabidoo_list_data_records instead.

        Args:
            appId: Identifier for the application. (required)
            tableId: Identifier for the target table. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def tabidoo_get_table(
        self,
        appId: str,
        tableId: str,
    ) -> Dict[str, Any]:
        """Returns detailed information about a specific table within a Tabidoo application, including its schema and field definitions, identified by app ID and table ID. Use this when you need metadata or structure details for a particular table. Do not use this to list all tables; use tabidoo_list_tables instead.

        Args:
            appId: The ID of the application. (required)
            tableId: The ID of the table. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def tabidoo_list_applications(
        self,
    ) -> Dict[str, Any]:
        """Returns a list of all applications available in the Tabidoo account. Use this to discover what applications exist and obtain their app IDs for use in subsequent calls. Do not use this to retrieve details of a single application; use tabidoo_get_application instead.
        Returns:
            API response as a dictionary.
        """
        ...

    def tabidoo_list_data_records(
        self,
        appId: str,
        tableId: str,
        filter: Optional[str] = None,
        limit: Optional[str] = None,
        skip: Optional[str] = None,
        sort: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Returns a list of data records from a specified table within a Tabidoo application, identified by app ID and table ID. Use this to retrieve multiple records from a table. Do not use this to retrieve a single specific record; use tabidoo_get_data_record instead.

        Args:
            appId: Identifier of the application. (required)
            tableId: Identifier of the table. (required)
            filter: Filter criteria for the data.
            limit: Maximum number of records to return.
            skip: Number of records to skip.
            sort: Sorting criteria for the data.
        Returns:
            API response as a dictionary.
        """
        ...

    def tabidoo_list_tables(
        self,
        appId: str,
    ) -> Dict[str, Any]:
        """Returns a list of all tables available within a specified Tabidoo application, identified by app ID. Use this to discover what tables exist in an application. Do not use this to retrieve details of a single table; use tabidoo_get_table instead.

        Args:
            appId: The ID of the application. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def tabidoo_update_data_record(
        self,
        appId: str,
        recordId: str,
        tableId: str,
        fields: Optional[Dict[str, Any]] = None,
    ) -> Dict[str, Any]:
        """Updates one or more fields of an existing data record in a specified Tabidoo table, identified by app ID, table ID, and record ID. Use this to modify the content of an existing record. Only the fields provided in the request body will be changed. Do not use this to create a new record; use tabidoo_create_data_record instead.

        Args:
            appId: The ID of the Tabidoo app. (required)
            recordId: The ID of the record to be accessed. (required)
            tableId: The ID of the table containing the record. (required)
            fields: An object containing the fields and their values to update or create.
        Returns:
            API response as a dictionary.
        """
        ...

