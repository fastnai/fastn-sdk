"""Fastn Azure Table Storage connector — auto-generated type stubs.

Do not edit manually. Regenerate with `fastn connector sync`.
"""
from __future__ import annotations

from typing import Any, Dict, List, Optional


class AzureTableStorageConnector:
    """Azure Table Storage connector ().

    Provides 3 tools.
    """

    def add_records(
        self,
        PartitionKey: Optional[str] = None,
        RowKey: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Adds new records to the existing table in the specified database using the connector.

        Args:
            PartitionKey: 
            RowKey: 
        Returns:
            API response as a dictionary.
        """
        ...

    def create_table(
        self,
        TableName: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Creates a new table in the specified database using the connector.

        Args:
            TableName: 
        Returns:
            API response as a dictionary.
        """
        ...

    def get_records(
        self,
        NextPartitionKey: Optional[str] = None,
        NextRowKey: Optional[str] = None,
        filter: Optional[str] = None,
        select: Optional[str] = None,
        top: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Retrieves records from the specified table in the database using the connector.

        Args:
            NextPartitionKey: 
            NextRowKey: 
            filter: 
            select: 
            top: 
        Returns:
            API response as a dictionary.
        """
        ...

