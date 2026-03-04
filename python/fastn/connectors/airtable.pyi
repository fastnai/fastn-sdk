"""Fastn Airtable connector — auto-generated type stubs.

Do not edit manually. Regenerate with `fastn connector sync`.
"""
from __future__ import annotations

from typing import Any, Dict, List, Optional, TypedDict


class _AirtableCreateWebhookSpecification(TypedDict, total=False):
    options: Dict[str, Any]

class _AirtableUpdateRecordFields(TypedDict, total=False):
    Address: str
    Name: str
    Visited: bool

class AirtableConnector:
    """Airtable connector ().

    Provides 11 tools.
    """

    def airtable_create_base(
        self,
        name: str,
        workspaceId: str,
        tables: Optional[List[Any]] = None,
    ) -> Dict[str, Any]:
        """Creates a new Airtable base in your account with a specified name and initial table configuration. Use this when you need to provision a new project workspace from scratch. Do not use this to add tables to an existing base — use airtable_create_table instead. This action creates a persistent base in your Airtable account.

        Args:
            name: The name of the workspace. (required)
            workspaceId: The ID of the workspace. (required)
            tables: 
        Returns:
            API response as a dictionary.
        """
        ...

    def airtable_create_row(
        self,
        baseId: str,
        tableNameOrId: str,
        records: Optional[List[Any]] = None,
    ) -> Dict[str, Any]:
        """Adds a single new record (row) to a specified table within an Airtable base, populating it with the provided field values. Use this to insert one new data entry into a table. Do not use this to update an existing record — use airtable_update_record instead. This action creates a new record and cannot be undone without explicitly deleting it.

        Args:
            baseId: ID of the Airtable base. (required)
            tableNameOrId: Name or ID of the Airtable table. (required)
            records: 
        Returns:
            API response as a dictionary.
        """
        ...

    def airtable_create_table(
        self,
        baseId: str,
        description: Optional[str] = None,
        fields: Optional[List[Any]] = None,
        name: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Creates a new table within a specified Airtable base, including defining its initial fields and configuration. Use this when you need to add a new table to an existing base. Do not use this to add records to an existing table — use airtable_create_row instead. This action modifies the base schema.

        Args:
            baseId: The ID of the Airtable base. (required)
            description: Description of the Airtable record or table.
            fields: 
            name: Name of the Airtable record or table.
        Returns:
            API response as a dictionary.
        """
        ...

    def airtable_create_webhook(
        self,
        baseId: str,
        notificationUrl: str,
        specification: Optional[_AirtableCreateWebhookSpecification] = None,
    ) -> Dict[str, Any]:
        """Registers a new webhook on a specified Airtable base to receive real-time event notifications when data changes occur. Use this to set up event-driven integrations that react to record creation, updates, or deletions. Do not use this for one-time data reads — use list or get tools instead. This action creates a persistent webhook subscription; remove it explicitly when no longer needed to avoid unnecessary notifications.

        Args:
            baseId: The ID of the Airtable base. (required)
            notificationUrl: URL to receive notifications. (required)
            specification: Specification for the notification.
        Returns:
            API response as a dictionary.
        """
        ...

    def airtable_delete_bulk_records(
        self,
        baseId: str,
        records: str,
        tableNameOrId: str,
    ) -> Dict[str, Any]:
        """Permanently deletes multiple records in a single request from a specified Airtable table. Use this for efficient bulk removal of records when you have multiple record IDs to delete. This action is irreversible — deleted records cannot be recovered. Do not use this to delete a single record — use airtable_delete_record instead.

        Args:
            baseId: ID of the Airtable base. (required)
            records: Records data to be processed by the Airtable API. (required)
            tableNameOrId: Name or ID of the Airtable table. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def airtable_delete_record(
        self,
        baseId: str,
        recordId: str,
        tableNameOrId: str,
    ) -> Dict[str, Any]:
        """Permanently deletes a single record from a specified Airtable table by its record ID. Use this when you need to remove one specific record from a table. This action is irreversible — deleted records cannot be recovered. Do not use this to delete multiple records at once — use airtable_delete_bulk_records instead.

        Args:
            baseId: ID of the Airtable base. (required)
            recordId: ID of the specific record in Airtable. (required)
            tableNameOrId: Name or ID of the Airtable table. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def airtable_list_bases(
        self,
        offset: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Returns a list of all Airtable bases accessible in your account, including their names and IDs. Use this to discover available bases before performing table or record operations. Do not use this to list tables within a base — use airtable_list_tables instead. This action is read-only and has no side effects.

        Args:
            offset: 
        Returns:
            API response as a dictionary.
        """
        ...

    def airtable_list_records(
        self,
        baseId: str,
        tableNameOrId: str,
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
        """Returns a list of records from a specified table within an Airtable base, including all field values. Use this to read or browse the contents of a table. Do not use this to retrieve a single known record by ID — use a targeted get approach if available. This action is read-only and has no side effects.

        Args:
            baseId: The ID of the Airtable base. (required)
            tableNameOrId: The name or ID of the Airtable table. (required)
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

    def airtable_list_tables(
        self,
        baseId: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Returns a list of all tables within a specified Airtable base, including their names and IDs. Use this to discover available tables before reading or writing records. Do not use this to retrieve records within a table — use airtable_list_records instead. This action is read-only and has no side effects.

        Args:
            baseId: 
        Returns:
            API response as a dictionary.
        """
        ...

    def airtable_update_bulk(
        self,
        baseId: str,
        tableNameOrId: str,
        records: Optional[List[Any]] = None,
    ) -> Dict[str, Any]:
        """Updates multiple records simultaneously in a specified Airtable table in a single API call. Use this for efficient batch updates when you need to modify fields across several records at once. Do not use this to update a single record — use airtable_update_record instead. This action modifies existing data for all provided record IDs.

        Args:
            baseId: The unique identifier for the Airtable base. (required)
            tableNameOrId: The name or ID of the Airtable table. (required)
            records: 
        Returns:
            API response as a dictionary.
        """
        ...

    def airtable_update_record(
        self,
        baseId: str,
        fields: _AirtableUpdateRecordFields,
        recordId: str,
        tableNameOrId: str,
    ) -> Dict[str, Any]:
        """Updates a single record in a specified Airtable table by its record ID, modifying only the fields provided in the request (partial update). Use this when you need to change specific fields on one known record. Do not use this to update multiple records at once — use airtable_update_bulk instead. This action modifies existing data.

        Args:
            baseId: ID of the Airtable base containing the table. (required)
            fields: Fields to be updated in the Airtable record. (required)
            recordId: ID of the record to be updated. (required)
            tableNameOrId: Name or ID of the table containing the record. (required)
        Returns:
            API response as a dictionary.
        """
        ...

