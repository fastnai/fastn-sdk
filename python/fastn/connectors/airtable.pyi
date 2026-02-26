"""Fastn Airtable connector — auto-generated type stubs.

Do not edit manually. Regenerate with `fastn connector sync`.
"""
from __future__ import annotations

from typing import Any, Dict, List, Optional


class AirtableConnector:
    """Airtable connector ().

    Provides 11 tools.
    """

    def create_base(
        self,
        name: str,
        workspaceId: str,
        tables: Optional[List[Any]] = None,
    ) -> Dict[str, Any]:
        """Creates a new base in the system using the specified connector.

        Args:
            name: The name of the workspace. (required)
            workspaceId: The ID of the workspace. (required)
            tables: 
        Returns:
            API response as a dictionary.
        """
        ...

    def create_row(
        self,
        records: Optional[List[Any]] = None,
    ) -> Dict[str, Any]:
        """Adds a new row to a specified table within a base using the connector.

        Args:
            records: 
        Returns:
            API response as a dictionary.
        """
        ...

    def create_table(
        self,
        description: Optional[str] = None,
        fields: Optional[List[Any]] = None,
        name: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Creates a new table within a base through the designated connector.

        Args:
            description: Description of the Airtable record or table.
            fields: 
            name: Name of the Airtable record or table.
        Returns:
            API response as a dictionary.
        """
        ...

    def create_webhook(
        self,
        notificationUrl: str,
        specification: Optional[Dict[str, Any]] = None,
    ) -> Dict[str, Any]:
        """Sets up a webhook to listen for events from the connector, allowing for real-time notifications.

        Args:
            notificationUrl: URL to receive notifications. (required)
            specification: Specification for the notification.
        Returns:
            API response as a dictionary.
        """
        ...

    def delete_bulk_records(
        self,
        records: str,
    ) -> Dict[str, Any]:
        """Deletes multiple records from a specified table in the connector at once.

        Args:
            records: Records data to be processed by the Airtable API. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def delete_record(
        self,
        baseId: str,
        recordId: str,
        tableNameOrId: str,
    ) -> Dict[str, Any]:
        """Removes a single record from a specified table in the connector.

        Args:
            baseId: ID of the Airtable base. (required)
            recordId: ID of the specific record in Airtable. (required)
            tableNameOrId: Name or ID of the Airtable table. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def get_bases(
        self,
        offset: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Retrieves a list of all bases available in the connector.

        Args:
            offset: 
        Returns:
            API response as a dictionary.
        """
        ...

    def get_records(
        self,
        cellFormat: Optional[str] = None,
        fields: Optional[str] = None,
        filterByFormula: Optional[str] = None,
        maxRecords: Optional[str] = None,
        offset: Optional[str] = None,
        pageSize: Optional[str] = None,
        recordMetadata: Optional[str] = None,
        returnFieldsByFieldId: Optional[str] = None,
        sort: Optional[str] = None,
        timeZone: Optional[str] = None,
        userLocale: Optional[str] = None,
        view: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Fetches records from a specified table within a base using the connector.

        Args:
            cellFormat: 
            fields: 
            filterByFormula: 
            maxRecords: 
            offset: 
            pageSize: 
            recordMetadata: 
            returnFieldsByFieldId: 
            sort: 
            timeZone: 
            userLocale: 
            view: 
        Returns:
            API response as a dictionary.
        """
        ...

    def get_tables(
        self,
        baseId: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Retrieves a list of all tables available in a specified base of the connector.

        Args:
            baseId: 
        Returns:
            API response as a dictionary.
        """
        ...

    def update_bulk(
        self,
        records: Optional[List[Any]] = None,
    ) -> Dict[str, Any]:
        """Updates multiple records within a table of the connector simultaneously.

        Args:
            records: 
        Returns:
            API response as a dictionary.
        """
        ...

    def update_record(
        self,
        fields: Dict[str, Any],
    ) -> Dict[str, Any]:
        """Modifies a single record in a specified table using the connector.

        Args:
            fields: Fields to be updated in the Airtable record. (required)
        Returns:
            API response as a dictionary.
        """
        ...

