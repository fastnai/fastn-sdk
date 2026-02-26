"""Fastn Softr connector — auto-generated type stubs.

Do not edit manually. Regenerate with `fastn connector sync`.
"""
from __future__ import annotations

from typing import Any, Dict, List, Optional


class SoftrConnector:
    """Softr connector ().

    Provides 9 tools.
    """

    def create_database(
        self,
        name: str,
        workspaceId: str,
        description: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Creates a new database in the system.

        Args:
            name: Name of the item. (required)
            workspaceId: ID of the workspace. (required)
            description: Description of the item.
        Returns:
            API response as a dictionary.
        """
        ...

    def create_user(
        self,
        SoftrDomain: str,
    ) -> Dict[str, Any]:
        """Creates a new user in the system.

        Args:
            SoftrDomain: Your Softr domain. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def delete_database(
        self,
        force_: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Deletes a database from the system.

        Args:
            force_: 
        Returns:
            API response as a dictionary.
        """
        ...

    def delete_user(
        self,
        SoftrDomain: str,
    ) -> Dict[str, Any]:
        """Deletes a user from the system.

        Args:
            SoftrDomain: The Softr domain associated with your application. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def generate_magic_link(
        self,
        SoftrDomain: str,
    ) -> Dict[str, Any]:
        """Generates a magic link for user authentication.

        Args:
            SoftrDomain: The Softr domain associated with your application. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def get_database(
        self,
        databaseId: str,
    ) -> Dict[str, Any]:
        """Fetches details of a specific database.

        Args:
            databaseId: The ID of the Airtable database. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def get_databases(
        self,
    ) -> Dict[str, Any]:
        """Retrieves a list of databases in the system.
        Returns:
            API response as a dictionary.
        """
        ...

    def sync_users(
        self,
        SoftrDomain: str,
    ) -> Dict[str, Any]:
        """Synchronizes users across different platforms.

        Args:
            SoftrDomain: The domain associated with your Softr application. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def update_database(
        self,
        description: str,
        name: str,
    ) -> Dict[str, Any]:
        """Updates information for an existing database.

        Args:
            description: Description of the item. (required)
            name: Name of the item. (required)
        Returns:
            API response as a dictionary.
        """
        ...

