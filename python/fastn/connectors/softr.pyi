"""Fastn Softr connector — auto-generated type stubs.

Do not edit manually. Regenerate with `fastn connector sync`.
"""
from __future__ import annotations

from typing import Any, Dict, List, Optional, TypedDict


class SoftrConnector:
    """Softr connector ().

    Provides 9 tools.
    """

    def softr_create_database(
        self,
        name: str,
        workspaceId: str,
        description: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Creates a new database in Softr. Use this tool when you need to provision a new database to store structured data within your Softr application. Do NOT use this tool to update an existing database — use softr_update_database instead. Side effect: a new database is created and will persist until explicitly deleted.

        Args:
            name: Name of the item. (required)
            workspaceId: ID of the workspace. (required)
            description: Description of the item.
        Returns:
            API response as a dictionary.
        """
        ...

    def softr_create_user(
        self,
        SoftrDomain: str,
        email: str,
        full_name: str,
        generate_magic_link: bool,
        password: str,
    ) -> Dict[str, Any]:
        """Creates a new user account in Softr. Use this tool when you need to register a new user and grant them access to your Softr application. Do NOT use this tool to update an existing users details or to bulk-import users — use softr_sync_users for bulk operations. Side effect: a new user account is created and the user may receive an invitation or welcome email depending on your Softr application settings.

        Args:
            SoftrDomain: Your Softr domain. (required)
            email: User's email address. (required)
            full_name: User's full name. (required)
            generate_magic_link: Whether to generate a magic link for login. (required)
            password: User's password. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def softr_delete_database(
        self,
        databaseId: str,
        force_: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Permanently deletes a specific database from Softr by its database ID. Use this tool when you need to remove a database and all its associated data from Softr. Do NOT use this tool if you only want to update or clear the database contents — this action is irreversible and cannot be undone. Side effect: all data stored in the deleted database is permanently lost.

        Args:
            databaseId: The ID of the database to interact with. (required)
            force_: 
        Returns:
            API response as a dictionary.
        """
        ...

    def softr_delete_user(
        self,
        SoftrDomain: str,
        userEmail: str,
    ) -> Dict[str, Any]:
        """Permanently deletes a Softr user account identified by their email address. Use this tool when you need to remove a user and revoke their access to the Softr application. Do NOT use this tool if you only want to update user details — use softr_update_user instead. This action is irreversible; the deleted user account cannot be recovered. Side effect: the user loses all access to the Softr application immediately upon deletion.

        Args:
            SoftrDomain: The Softr domain associated with your application. (required)
            userEmail: The email address of the user. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def softr_generate_magic_link(
        self,
        SoftrDomain: str,
        userEmail: str,
    ) -> Dict[str, Any]:
        """Generates a one-time magic link for passwordless authentication for a specific Softr user identified by their email address. Use this tool when you need to grant a user secure, temporary access to a Softr app without requiring a password. Do NOT use this tool to create a new user account — use softr_create_user instead. Side effect: a time-limited authentication token is generated and associated with the users account.

        Args:
            SoftrDomain: The Softr domain associated with your application. (required)
            userEmail: The email address of the user. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def softr_get_database(
        self,
        databaseId: str,
    ) -> Dict[str, Any]:
        """Retrieves the details of a specific Softr database by its database ID, including its name, configuration, and metadata. Use this tool when you need to inspect a single known database. Do NOT use this tool to list all available databases — use softr_list_databases instead. This tool is read-only and has no side effects.

        Args:
            databaseId: The ID of the Airtable database. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def softr_list_databases(
        self,
    ) -> Dict[str, Any]:
        """Retrieves a list of all databases available in the Softr account. Use this tool when you need an overview of all existing databases or to find a specific database ID before performing further operations. Do NOT use this tool to get detailed information about a single database — use softr_get_database instead. This tool is read-only and has no side effects.
        Returns:
            API response as a dictionary.
        """
        ...

    def softr_sync_users(
        self,
        SoftrDomain: str,
        body: List[Any],
    ) -> Dict[str, Any]:
        """Synchronizes user data between Softr and an external data source or platform. Use this tool when you need to ensure that user records in Softr are aligned with an external system, such as after a bulk import or an external user update. Do NOT use this tool to create a single new user — use softr_create_user instead. Side effect: existing Softr user records may be updated or overwritten to match the source data during synchronization.

        Args:
            SoftrDomain: The domain associated with your Softr application. (required)
            body: An array of strings representing the request body. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def softr_update_database(
        self,
        databaseId: str,
        description: str,
        name: str,
    ) -> Dict[str, Any]:
        """Updates the configuration or metadata of an existing Softr database identified by its database ID. Use this tool when you need to rename a database or modify its settings. Do NOT use this tool to delete a database or to update records within the database tables — use the appropriate delete or record-level tools instead. Side effect: the existing database configuration is overwritten with the new values provided.

        Args:
            databaseId: The ID of the database to interact with. (required)
            description: Description of the item. (required)
            name: Name of the item. (required)
        Returns:
            API response as a dictionary.
        """
        ...

