"""Fastn Ninox connector — auto-generated type stubs.

Do not edit manually. Regenerate with `fastn connector sync`.
"""
from __future__ import annotations

from typing import Any, Dict, List, Optional


class NinoxConnector:
    """Ninox connector ().

    Provides 13 tools.
    """

    def create_record(
        self,
    ) -> Dict[str, Any]:
        """Creates a new record in the specified database using the relevant connector.
        Returns:
            API response as a dictionary.
        """
        ...

    def delete_record(
        self,
        databaseID: str,
        recordID: str,
        tableID: str,
        teamID: str,
    ) -> Dict[str, Any]:
        """Deletes a specific record from the specified database using the relevant connector.

        Args:
            databaseID: The unique identifier for the target database. (required)
            recordID: The unique identifier for the target record. (required)
            tableID: The unique identifier for the target table. (required)
            teamID: The unique identifier for the team owning the database. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def delete_records(
        self,
    ) -> Dict[str, Any]:
        """Deletes multiple records from the specified database using the relevant connector.
        Returns:
            API response as a dictionary.
        """
        ...

    def execute_read_only_get_query(
        self,
        query: str,
    ) -> Dict[str, Any]:
        """Executes a read-only GET query to retrieve data from the specified database using the relevant connector.

        Args:
            query: The query string for the Ninox API request. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def execute_read_only_post_query(
        self,
        query: str,
    ) -> Dict[str, Any]:
        """Executes a read-only POST query to retrieve data from the specified database using the relevant connector.

        Args:
            query: The query to be executed on the Ninox database. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def execute_writeable_query(
        self,
        query: str,
    ) -> Dict[str, Any]:
        """Executes a writable query to modify data in the specified database using the relevant connector.

        Args:
            query: The Ninox query string. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def get_database(
        self,
        databaseID: str,
        teamID: str,
    ) -> Dict[str, Any]:
        """Retrieves details of a specific database using the relevant connector.

        Args:
            databaseID: The unique identifier for the target Ninox database. (required)
            teamID: The unique identifier for the team accessing the database. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def get_databases(
        self,
        teamID: str,
    ) -> Dict[str, Any]:
        """Retrieves a list of all databases available in the connector.

        Args:
            teamID: The ID of the Ninox team. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def get_record(
        self,
        choiceStyle: Optional[str] = None,
        style: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Retrieves a specific record from the specified database using the relevant connector.

        Args:
            choiceStyle: Specifies the style of choices (e.g., dropdown, radio buttons).
            style: Specifies the style of the element (e.g., text field, number field).
        Returns:
            API response as a dictionary.
        """
        ...

    def get_records(
        self,
        choiceStyle: Optional[str] = None,
        style: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Retrieves all records from the specified database using the relevant connector.

        Args:
            choiceStyle: Specifies the style for choice fields.
            style: Specifies the style for the request.
        Returns:
            API response as a dictionary.
        """
        ...

    def get_workspace(
        self,
        teamID: str,
    ) -> Dict[str, Any]:
        """Retrieves details of a specific workspace using the relevant connector.

        Args:
            teamID: The ID of the Ninox team. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def get_workspaces(
        self,
    ) -> Dict[str, Any]:
        """Retrieves a list of all workspaces available in the connector.
        Returns:
            API response as a dictionary.
        """
        ...

    def update_record(
        self,
    ) -> Dict[str, Any]:
        """Updates an existing record in the specified database using the relevant connector.
        Returns:
            API response as a dictionary.
        """
        ...

