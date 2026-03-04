"""Fastn QuintaDB connector — auto-generated type stubs.

Do not edit manually. Regenerate with `fastn connector sync`.
"""
from __future__ import annotations

from typing import Any, Dict, List, Optional, TypedDict


class QuintadbConnector:
    """QuintaDB connector ().

    Provides 9 tools.
    """

    def quintadb_create_database(
        self,
        database_name: str,
        form_name: str,
    ) -> Dict[str, Any]:
        """Creates a new database in the authenticated QuintaDB account. Use this tool when you need to provision a new top-level database before adding forms to it. Do not use this tool to create a form within an existing database — use quintadb_create_form instead.

        Args:
            database_name: The name of the database to interact with. (required)
            form_name: The name of the form within the specified database. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def quintadb_create_form(
        self,
        databaseId: str,
        name: str,
    ) -> Dict[str, Any]:
        """Creates a new form within an existing QuintaDB database, identified by its database ID. Use this tool when you need to add a new web form to an existing database. Do not use this tool to create a new database — use quintadb_create_database instead.

        Args:
            databaseId: The ID of the QuintaDB database. (required)
            name: Name of the resource. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def quintadb_delete_database(
        self,
        databaseId: str,
    ) -> Dict[str, Any]:
        """Permanently deletes an existing QuintaDB database, identified by its database ID, along with all forms and data contained within it. Use this tool only when you intend to irreversibly remove the entire database. This action cannot be undone. Do not use this tool to delete a single form within a database — use quintadb_delete_form instead.

        Args:
            databaseId: The ID of the QuintaDB database. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def quintadb_delete_form(
        self,
        databaseId: str,
        formId: str,
    ) -> Dict[str, Any]:
        """Permanently deletes an existing form from a QuintaDB database, identified by both the database ID and the form ID. Use this tool only when you intend to irreversibly remove the form and all of its associated configuration. This action cannot be undone. Do not use this tool to delete a database — use quintadb_delete_database instead.

        Args:
            databaseId:  (required)
            formId:  (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def quintadb_get_database(
        self,
        databaseId: str,
    ) -> Dict[str, Any]:
        """Retrieves the details of a specific QuintaDB database by its database ID. Use this tool when you already know the database ID and need its full metadata or configuration. Do not use this tool to list all databases — use quintadb_list_databases instead.

        Args:
            databaseId: The unique identifier of the QuintaDB database. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def quintadb_get_form(
        self,
        databaseId: str,
        formId: str,
    ) -> Dict[str, Any]:
        """Retrieves the details of a specific form within a QuintaDB database, identified by both the database ID and the form ID. Use this tool when you need metadata or configuration details for a single known form. Do not use this tool to list all forms in a database — use quintadb_list_database_forms instead.

        Args:
            databaseId: The ID of the database to interact with. (required)
            formId: The ID of the form within the database. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def quintadb_list_database_forms(
        self,
        databaseId: str,
    ) -> Dict[str, Any]:
        """Retrieves a list of all forms associated with a specific QuintaDB database, identified by its database ID. Use this tool when you need to discover which forms exist within a database or find a specific form ID. Do not use this tool to retrieve a single forms details — use quintadb_get_form instead.

        Args:
            databaseId: The ID of the QuintaDB database to interact with. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def quintadb_list_databases(
        self,
        page: int,
    ) -> Dict[str, Any]:
        """Retrieves a list of all databases available in the authenticated QuintaDB account. Use this tool when you need to discover available databases or find a specific database ID. Do not use this tool to retrieve a single database by ID — use quintadb_get_database instead.

        Args:
            page: Specifies the page number for pagination. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def quintadb_update_database(
        self,
        databaseId: str,
        name: str,
    ) -> Dict[str, Any]:
        """Updates the name or settings of an existing QuintaDB database identified by its database ID. Use this tool when you need to rename or modify the properties of an existing database. Do not use this tool to update forms, records, or fields within a database — use the appropriate form or record tools instead. This operation overwrites the existing database metadata.

        Args:
            databaseId: The ID of the QuintaDB database. (required)
            name: Name of the resource. (required)
        Returns:
            API response as a dictionary.
        """
        ...

