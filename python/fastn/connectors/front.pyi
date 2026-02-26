"""Fastn Front connector — auto-generated type stubs.

Do not edit manually. Regenerate with `fastn connector sync`.
"""
from __future__ import annotations

from typing import Any, Dict, List, Optional


class FrontConnector:
    """Front connector ().

    Provides 12 tools.
    """

    def add_contact_to_account(
        self,
        contact_ids: List[Any],
    ) -> Dict[str, Any]:
        """Adds a contact to an existing account in the connected service.

        Args:
            contact_ids: An array of contact IDs. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def create_account(
        self,
        description: str,
        name: str,
        domains: Optional[List[Any]] = None,
        logo_url: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Creates a new account in the connected service.

        Args:
            description: Description of the entity. (required)
            name: Name of the entity. (required)
            domains: Array of domains.
            logo_url: URL of the logo.
        Returns:
            API response as a dictionary.
        """
        ...

    def create_contact(
        self,
        description: str,
        handles: List[Any],
        name: str,
    ) -> Dict[str, Any]:
        """Creates a new contact in the connected service.

        Args:
            description: Description of the request. (required)
            handles:  (required)
            name: Name associated with the request. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def delete_account(
        self,
        accountId: str,
    ) -> Dict[str, Any]:
        """Deletes a specified account from the connected service.

        Args:
            accountId: Account ID for the Front platform Front endpoint. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def delete_contact(
        self,
        contactId: str,
    ) -> Dict[str, Any]:
        """Deletes a specified contact from the connected service.

        Args:
            contactId: ID of the contact. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def get_account(
        self,
        accountId: str,
    ) -> Dict[str, Any]:
        """Fetches detailed information about a specific account from the connected service.

        Args:
            accountId: Account ID for the Front platform. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def get_accounts(
        self,
    ) -> Dict[str, Any]:
        """Retrieves a list of all accounts from the connected service.
        Returns:
            API response as a dictionary.
        """
        ...

    def get_contact(
        self,
        contactId: str,
    ) -> Dict[str, Any]:
        """Fetches detailed information about a specific contact from the connected service.

        Args:
            contactId: ID of the contact. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def get_contacts(
        self,
    ) -> Dict[str, Any]:
        """Retrieves a list of all contacts from the connected service.
        Returns:
            API response as a dictionary.
        """
        ...

    def remove_contactfrom_account(
        self,
        contact_ids: List[Any],
    ) -> Dict[str, Any]:
        """Removes a contact from an existing account in the connected service.

        Args:
            contact_ids: Array of contact IDs. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def update_account(
        self,
        description: str,
        name: str,
        domains: Optional[List[Any]] = None,
        logo_url: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Updates information for an existing account in the connected service.

        Args:
            description: Description of the resource. (required)
            name: Name of the resource. (required)
            domains: Array of domains associated with the resource.
            logo_url: URL of the logo for the resource.
        Returns:
            API response as a dictionary.
        """
        ...

    def update_contact(
        self,
        description: str,
        handles: List[Any],
        name: str,
    ) -> Dict[str, Any]:
        """Updates information for an existing contact in the connected service.

        Args:
            description: The description. (required)
            handles:  (required)
            name: The name. (required)
        Returns:
            API response as a dictionary.
        """
        ...

