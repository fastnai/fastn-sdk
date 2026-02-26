"""Fastn AITable connector — auto-generated type stubs.

Do not edit manually. Regenerate with `fastn connector sync`.
"""
from __future__ import annotations

from typing import Any, Dict, List, Optional


class AitableConnector:
    """AITable connector ().

    Provides 9 tools.
    """

    def create_datasheet(
        self,
        description: Optional[str] = None,
        fields: Optional[List[Any]] = None,
        name: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Creates a new datasheet in the specified connector environment.

        Args:
            description: 
            fields: 
            name: 
        Returns:
            API response as a dictionary.
        """
        ...

    def create_field(
        self,
        name: Optional[str] = None,
        property: Optional[Dict[str, Any]] = None,
        type: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Creates a new field in the specified connector's datasheet.

        Args:
            name: 
            property: 
            type: 
        Returns:
            API response as a dictionary.
        """
        ...

    def create_records(
        self,
        records: Optional[List[Any]] = None,
    ) -> Dict[str, Any]:
        """Adds new records to the specified connector's datasheet.

        Args:
            records: 
        Returns:
            API response as a dictionary.
        """
        ...

    def delete_records(
        self,
        commaSeparatedRecordIds: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Deletes specified records from the specified connector's datasheet.

        Args:
            commaSeparatedRecordIds: 
        Returns:
            API response as a dictionary.
        """
        ...

    def get_fields(
        self,
        datasheetId: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Fetches the available fields in the specified connector's datasheet.

        Args:
            datasheetId: 
        Returns:
            API response as a dictionary.
        """
        ...

    def get_records(
        self,
        viewId: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Fetches the records from the specified connector's datasheet.

        Args:
            viewId: 
        Returns:
            API response as a dictionary.
        """
        ...

    def get_spaces(
        self,
    ) -> Dict[str, Any]:
        """Retrieves a list of spaces in the specified connector environment.
        Returns:
            API response as a dictionary.
        """
        ...

    def get_views(
        self,
        dataSheetId: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Retrieves a list of views in the specified connector environment.

        Args:
            dataSheetId: 
        Returns:
            API response as a dictionary.
        """
        ...

    def update_record(
        self,
        records: Optional[List[Any]] = None,
    ) -> Dict[str, Any]:
        """Updates an existing record in the specified connector's datasheet.

        Args:
            records: 
        Returns:
            API response as a dictionary.
        """
        ...

