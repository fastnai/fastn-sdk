"""Fastn Azure Table Storage connector — auto-generated type stubs.

Do not edit manually. Regenerate with `fastn connector sync`.
"""
from __future__ import annotations

from typing import Any, Dict, List, Optional, TypedDict


class AzureTableStorageConnector:
    """Azure Table Storage connector ().

    Provides 3 tools.
    """

    def azure_table_storage_add_record(
        self,
        PartitionKey: Optional[str] = None,
        RowKey: Optional[str] = None,
        tableName: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Inserts a new record (entity) into a specified table in Azure Table Storage. Use this tool when you need to persist a new structured data entry, such as a log event, configuration value, or user record. Do not use this tool to update an existing record — there is no update operation; inserting a duplicate PartitionKey and RowKey combination may result in an error or conflict. Requires the table name and the record data including PartitionKey and RowKey.

        Args:
            PartitionKey: 
            RowKey: 
            tableName: 
        Returns:
            API response as a dictionary.
        """
        ...

    def azure_table_storage_create_table(
        self,
        TableName: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Creates a new table in Azure Table Storage. Use this tool when you need to provision a new table before inserting records into it. Do not use this tool if the table already exists — Azure Table Storage will return a conflict error for duplicate table names. Do not use this tool to insert records — use azure_table_storage_add_record for that. Requires a unique table name.

        Args:
            TableName: 
        Returns:
            API response as a dictionary.
        """
        ...

    def azure_table_storage_list_records(
        self,
        NextPartitionKey: Optional[str] = None,
        NextRowKey: Optional[str] = None,
        filter: Optional[str] = None,
        select: Optional[str] = None,
        tableName: Optional[str] = None,
        top: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Lists records from a specified table in Azure Table Storage. Use this tool when you need to retrieve multiple rows of structured data from a table, for example to query all entries or apply OData filters. Do not use this tool to create tables or insert new records — use azure_table_storage_create_table or azure_table_storage_add_record for those. Requires the table name.

        Args:
            NextPartitionKey: 
            NextRowKey: 
            filter: 
            select: 
            tableName: 
            top: 
        Returns:
            API response as a dictionary.
        """
        ...

