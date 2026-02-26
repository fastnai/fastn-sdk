"""Fastn test connector — auto-generated type stubs.

Do not edit manually. Regenerate with `fastn connector sync`.
"""
from __future__ import annotations

from typing import Any, Dict, List, Optional


class TestConnector:
    """test connector ().

    Provides 14 tools.
    """

    def calculate_user_count(
        self,
    ) -> Dict[str, Any]:
        """Returns the total count of users in the database. Example: GET /users/count
        Returns:
            API response as a dictionary.
        """
        ...

    def execute_query(
        self,
    ) -> Dict[str, Any]:
        """Execute a custom SQL query on the database. Use with caution.
        Returns:
            API response as a dictionary.
        """
        ...

    def get_all_users(
        self,
    ) -> Dict[str, Any]:
        """This endpoint retrieves a paginated list of all users. Example: GET /users?offset=0&limit=10
        Returns:
            API response as a dictionary.
        """
        ...

    def get_databases(
        self,
    ) -> Dict[str, Any]:
        """Get list of all databases in PostgreSQL
        Returns:
            API response as a dictionary.
        """
        ...

    def get_role_permissions(
        self,
    ) -> Dict[str, Any]:
        """Fetches all permissions associated with a role by its ID. Example: GET /roles/1/permissions
        Returns:
            API response as a dictionary.
        """
        ...

    def get_schemas(
        self,
    ) -> Dict[str, Any]:
        """Get list of all schemas in the database
        Returns:
            API response as a dictionary.
        """
        ...

    def get_table_schema(
        self,
    ) -> Dict[str, Any]:
        """Get detailed schema information for a specific table including columns, types, and constraints
        Returns:
            API response as a dictionary.
        """
        ...

    def get_tables(
        self,
    ) -> Dict[str, Any]:
        """Get list of all tables in the database
        Returns:
            API response as a dictionary.
        """
        ...

    def get_total_user_count(
        self,
    ) -> Dict[str, Any]:
        """This endpoint retrieves the total count of users in the system. Example: GET /users/count
        Returns:
            API response as a dictionary.
        """
        ...

    def get_user_by_id(
        self,
    ) -> Dict[str, Any]:
        """Fetches a single user from the database based on the provided user ID. Example: GET /users/1
        Returns:
            API response as a dictionary.
        """
        ...

    def get_user_count(
        self,
    ) -> Dict[str, Any]:
        """Returns the total number of users in the database. Example: GET /users/count
        Returns:
            API response as a dictionary.
        """
        ...

    def get_user_details(
        self,
    ) -> Dict[str, Any]:
        """This endpoint retrieves the details of a user identified by userId. Example: GET /users/1
        Returns:
            API response as a dictionary.
        """
        ...

    def get_user_roles(
        self,
    ) -> Dict[str, Any]:
        """Fetches all roles associated with a user by their ID. Example: GET /users/1/roles
        Returns:
            API response as a dictionary.
        """
        ...

    def get_users(
        self,
    ) -> Dict[str, Any]:
        """Fetches a list of users from the database with optional pagination. Example: GET /users?offset=0&limit=10
        Returns:
            API response as a dictionary.
        """
        ...

