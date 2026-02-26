"""Fastn CockroachDB connector — auto-generated type stubs.

Do not edit manually. Regenerate with `fastn connector sync`.
"""
from __future__ import annotations

from typing import Any, Dict, List, Optional


class CockroachdbConnector:
    """CockroachDB connector ().

    Provides 6 tools.
    """

    def execute_query(
        self,
        query: str,
    ) -> Dict[str, Any]:
        """Executes a SQL query against the specified database through the database connector, returning the results of the query.

        Args:
            query: The SQL query to be executed. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def get_databases(
        self,
    ) -> Dict[str, Any]:
        """Retrieves a list of all available databases within the database management system using the database connector.
        Returns:
            API response as a dictionary.
        """
        ...

    def get_roles(
        self,
        database: str,
    ) -> Dict[str, Any]:
        """Fetches the roles defined within the database management system through the database connector, providing information on user permissions and access levels.

        Args:
            database: The name of the database to connect to. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def get_table_columns(
        self,
        table_name: str,
    ) -> Dict[str, Any]:
        """Obtains the columns of a specific table in a database via the database connector, detailing the structure and data types of the table.

        Args:
            table_name: The name of the table to interact with. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def get_tables(
        self,
    ) -> Dict[str, Any]:
        """Fetches the tables present in a specified database using the database connector, allowing users to see the structure of the database.
        Returns:
            API response as a dictionary.
        """
        ...

    def get_users(
        self,
    ) -> Dict[str, Any]:
        """Lists all users within the database management system as accessed through the database connector, enabling user management and oversight.
        Returns:
            API response as a dictionary.
        """
        ...

