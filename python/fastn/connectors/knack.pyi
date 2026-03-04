"""Fastn Knack connector — auto-generated type stubs.

Do not edit manually. Regenerate with `fastn connector sync`.
"""
from __future__ import annotations

from typing import Any, Dict, List, Optional, TypedDict


class KnackConnector:
    """Knack connector ().

    Provides 6 tools.
    """

    def knack_create_record(
        self,
        object_name: str,
        body: Optional[Dict[str, Any]] = None,
    ) -> Dict[str, Any]:
        """Creates a new record in a specified Knack object (table) with the provided field data. Use this tool when you need to insert a new entry into the database. Do NOT use this tool to update an existing record — use knack_update_record instead. This action is irreversible without a subsequent delete operation.

        Args:
            object_name: The name of the Knack object to interact with. (required)
            body: Data to be sent to the Knack API.
        Returns:
            API response as a dictionary.
        """
        ...

    def knack_delete_record(
        self,
        object_name: str,
        recordId: str,
    ) -> Dict[str, Any]:
        """Permanently deletes a single record from a Knack object (table) identified by its unique record ID. Use this tool when you need to remove an existing record from the database. Do NOT use this tool if you only want to update or archive a record — deletion is irreversible and cannot be undone.

        Args:
            object_name: The name of the Knack object. (required)
            recordId: The ID of the specific record within the object. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def knack_get_record(
        self,
        object_name: str,
        recordId: str,
    ) -> Dict[str, Any]:
        """Retrieves a single record from a Knack object (table) by its unique record ID. Use this tool when you need the full details of one specific record and you already know its ID. Do NOT use this tool to retrieve multiple records or search by field values — use knack_list_records instead. This is a read-only operation with no side effects.

        Args:
            object_name: The name of the Knack object. (required)
            recordId: The ID of the Knack record. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def knack_list_records(
        self,
        object_name: str,
        format: Optional[str] = None,
        page: Optional[str] = None,
        rows_per_page: Optional[str] = None,
        sort_field: Optional[str] = None,
        sort_order: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Retrieves a list of records from a specified Knack object (table). Use this tool when you need to browse or paginate through multiple records in a Knack database object. Do NOT use this tool if you only need a single record by ID — use knack_get_record instead. This is a read-only operation with no side effects.

        Args:
            object_name: The name of the Knack object to interact with. (required)
            format: The format of the response (e.g., json).
            page: The page number to retrieve.
            rows_per_page: The number of rows to retrieve per page.
            sort_field: The field to sort by.
            sort_order: The sort order (e.g., asc, desc).
        Returns:
            API response as a dictionary.
        """
        ...

    def knack_update_record(
        self,
        object_name: str,
        recordId: str,
        body: Optional[Dict[str, Any]] = None,
    ) -> Dict[str, Any]:
        """Updates an existing record in a Knack object (table) identified by its unique record ID with the provided field data. Use this tool when you need to modify one or more fields of an existing record. Do NOT use this tool to create a new record — use knack_create_record instead. This action overwrites existing field values with the supplied data.

        Args:
            object_name: The name of the Knack object. (required)
            recordId: The ID of the Knack record. (required)
            body: The data to be sent in the request body (optional).
        Returns:
            API response as a dictionary.
        """
        ...

    def knack_upload_file(
        self,
        appID: str,
    ) -> Dict[str, Any]:
        """Uploads a file asset to a Knack application for storage and processing. Use this tool when you need to attach or store a file (e.g., image, document) in Knack before associating it with a record. Returns an asset reference that can be used when creating or updating records. This action is irreversible without a separate delete operation — the file will persist in Knack storage after upload.

        Args:
            appID: The ID of the Knack application. (required)
        Returns:
            API response as a dictionary.
        """
        ...

