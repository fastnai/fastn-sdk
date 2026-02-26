"""Fastn Ragic connector — auto-generated type stubs.

Do not edit manually. Regenerate with `fastn connector sync`.
"""
from __future__ import annotations

from typing import Any, Dict, List, Optional


class RagicConnector:
    """Ragic connector ().

    Provides 5 tools.
    """

    def create_record(
        self,
        v: str,
        api: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Creates a new record in the specified connector, enabling the addition of new entries to the database.

        Args:
            v: API version. (required)
            api: 
        Returns:
            API response as a dictionary.
        """
        ...

    def delete_record(
        self,
        v: str,
    ) -> Dict[str, Any]:
        """Deletes a specified record from the connector, removing the entry completely from the database.

        Args:
            v: Version of the API being called. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def get_single_record(
        self,
        v: str,
    ) -> Dict[str, Any]:
        """Retrieves a single record from the specified connector, providing detailed information about a particular entry.

        Args:
            v: API version. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def list_records(
        self,
        v: str,
        limit: Optional[str] = None,
        offset: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Lists all records in the specified connector, allowing for retrieval of multiple entries at once.

        Args:
            v: Specifies the API version. (required)
            limit: Limit the number of results.
            offset: Offset for pagination.
        Returns:
            API response as a dictionary.
        """
        ...

    def update_record(
        self,
        v: str,
        doLinkLoad: Optional[bool] = None,
    ) -> Dict[str, Any]:
        """Updates an existing record in the specified connector, allowing for modifications to be made to current entries.

        Args:
            v: API version. (required)
            doLinkLoad: Indicates whether to load links.
        Returns:
            API response as a dictionary.
        """
        ...

