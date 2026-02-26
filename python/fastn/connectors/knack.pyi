"""Fastn Knack connector — auto-generated type stubs.

Do not edit manually. Regenerate with `fastn connector sync`.
"""
from __future__ import annotations

from typing import Any, Dict, List, Optional


class KnackConnector:
    """Knack connector ().

    Provides 6 tools.
    """

    def create_record(
        self,
    ) -> Dict[str, Any]:
        """Creates a new record in the database with the provided data using the configured connector.
        Returns:
            API response as a dictionary.
        """
        ...

    def delete_record(
        self,
        object_name: str,
        recordId: str,
    ) -> Dict[str, Any]:
        """Deletes a record from the database using its unique ID with the configured connector.

        Args:
            object_name: The name of the Knack object. (required)
            recordId: The ID of the specific record within the object. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def get_record(
        self,
        object_name: str,
        recordId: str,
    ) -> Dict[str, Any]:
        """Fetches a single record from the database identified by a unique ID using the configured connector.

        Args:
            object_name: The name of the Knack object. (required)
            recordId: The ID of the Knack record. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def get_records(
        self,
        format: Optional[str] = None,
        page: Optional[str] = None,
        rows_per_page: Optional[str] = None,
        sort_field: Optional[str] = None,
        sort_order: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Retrieves multiple records from the database using the configured connector.

        Args:
            format: The format of the response (e.g., json).
            page: The page number to retrieve.
            rows_per_page: The number of rows to retrieve per page.
            sort_field: The field to sort by.
            sort_order: The sort order (e.g., asc, desc).
        Returns:
            API response as a dictionary.
        """
        ...

    def update_record(
        self,
    ) -> Dict[str, Any]:
        """Updates an existing record in the database identified by a unique ID with the new data using the configured connector.
        Returns:
            API response as a dictionary.
        """
        ...

    def upload_file(
        self,
        appID: str,
    ) -> Dict[str, Any]:
        """Uploads a file to the server for storage and processing using the configured connector.

        Args:
            appID: The ID of the Knack application. (required)
        Returns:
            API response as a dictionary.
        """
        ...

