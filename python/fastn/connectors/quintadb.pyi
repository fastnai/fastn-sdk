"""Fastn QuintaDB connector — auto-generated type stubs.

Do not edit manually. Regenerate with `fastn connector sync`.
"""
from __future__ import annotations

from typing import Any, Dict, List, Optional


class QuintadbConnector:
    """QuintaDB connector ().

    Provides 9 tools.
    """

    def create_database(
        self,
        database_name: str,
        form_name: str,
    ) -> Dict[str, Any]:
        """Creates a new database in the specified database connector.

        Args:
            database_name: The name of the database to interact with. (required)
            form_name: The name of the form within the specified database. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def create_form(
        self,
        name: str,
    ) -> Dict[str, Any]:
        """Creates a new form in the specified form connector.

        Args:
            name: Name of the resource. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def delete_database(
        self,
        databaseId: str,
    ) -> Dict[str, Any]:
        """Deletes an existing database from the specified database connector.

        Args:
            databaseId: The ID of the QuintaDB database. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def delete_form(
        self,
        databaseId: str,
        formId: str,
    ) -> Dict[str, Any]:
        """Deletes an existing form from the specified form connector.

        Args:
            databaseId:  (required)
            formId:  (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def get_database_by_id(
        self,
        databaseId: str,
    ) -> Dict[str, Any]:
        """Retrieves a specific database by its ID from the specified database connector.

        Args:
            databaseId: The unique identifier of the QuintaDB database. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def get_database_forms(
        self,
        databaseId: str,
    ) -> Dict[str, Any]:
        """Fetches all forms associated with a specific database from the specified database connector.

        Args:
            databaseId: The ID of the QuintaDB database to interact with. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def get_databases(
        self,
        page: int,
    ) -> Dict[str, Any]:
        """Retrieves a list of all databases from the specified database connector.

        Args:
            page: Specifies the page number for pagination. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def get_form_by_id(
        self,
        databaseId: str,
        formId: str,
    ) -> Dict[str, Any]:
        """Fetches a specific form by its ID from the specified form connector.

        Args:
            databaseId: The ID of the database to interact with. (required)
            formId: The ID of the form within the database. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def update_database(
        self,
        name: str,
    ) -> Dict[str, Any]:
        """Updates an existing database in the specified database connector.

        Args:
            name: Name of the resource. (required)
        Returns:
            API response as a dictionary.
        """
        ...

