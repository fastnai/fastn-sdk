"""Fastn Front connector — auto-generated type stubs.

Do not edit manually. Regenerate with `fastn connector sync`.
"""
from __future__ import annotations

from typing import Any, Dict, List, Optional, TypedDict


class FrontConnector:
    """Front connector ().

    Provides 12 tools.
    """

    def front_add_contact_to_account(
        self,
        accountId: str,
        contact_ids: List[Any],
    ) -> Dict[str, Any]:
        """Associates one or more existing contacts with a specific Front account, identified by the account ID. Use this to link contacts to an account for organizational purposes. Do not use this to create a new contact or account — use front_create_contact or front_create_account instead.

        Args:
            accountId: The ID of the account. (required)
            contact_ids: An array of contact IDs. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def front_create_account(
        self,
        description: str,
        name: str,
        domains: Optional[List[Any]] = None,
        logo_url: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Creates a new account in Front with details such as name and domain. Use this when a new company or organization needs to be added to Front for contact management and communication tracking. Do not use this to update an existing account — use front_update_account instead.

        Args:
            description: Description of the entity. (required)
            name: Name of the entity. (required)
            domains: Array of domains.
            logo_url: URL of the logo.
        Returns:
            API response as a dictionary.
        """
        ...

    def front_create_contact(
        self,
        description: str,
        handles: List[Any],
        name: str,
    ) -> Dict[str, Any]:
        """Creates a new contact in Front with details such as name, email, phone, and custom attributes. Use this when a new individual needs to be added to the Front contact directory. Do not use this to update an existing contact — use front_update_contact instead.

        Args:
            description: Description of the request. (required)
            handles:  (required)
            name: Name associated with the request. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def front_delete_account(
        self,
        accountId: str,
    ) -> Dict[str, Any]:
        """Permanently deletes a specific account from Front, identified by the account ID. Use this only when an account record must be fully removed from the system. This action is irreversible — the account and its associated data cannot be recovered after deletion. Do not use this to update an account — use front_update_account instead.

        Args:
            accountId: Account ID for the Front platform Front endpoint. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def front_delete_contact(
        self,
        contactId: str,
    ) -> Dict[str, Any]:
        """Permanently deletes a specific contact from Front, identified by their contact ID. Use this when a contact record must be fully removed from the system. This action is irreversible — the contact and all associated data cannot be recovered after deletion. Do not use this to simply update or merge a contact — use front_update_contact instead.

        Args:
            contactId: ID of the contact. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def front_get_account(
        self,
        accountId: str,
    ) -> Dict[str, Any]:
        """Retrieves detailed information about a single account in Front, identified by the account ID. Returns fields such as account name, domain, and linked contacts. Use this when you have a specific account ID and need full account details. Do not use this to browse all accounts — use front_list_accounts instead.

        Args:
            accountId: Account ID for the Front platform. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def front_get_contact(
        self,
        contactId: str,
    ) -> Dict[str, Any]:
        """Retrieves detailed information about a single contact in Front, identified by their contact ID. Returns fields such as name, email addresses, phone numbers, and linked accounts. Use this when you have a specific contact ID and need full contact details. Do not use this to browse all contacts — use front_list_contacts instead.

        Args:
            contactId: ID of the contact. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def front_list_accounts(
        self,
    ) -> Dict[str, Any]:
        """Retrieves a paginated list of all accounts in Front. Use this to enumerate or browse all company or organization records in the system. Do not use this when you need details for a specific account — use front_get_account with an account ID instead.
        Returns:
            API response as a dictionary.
        """
        ...

    def front_list_contacts(
        self,
    ) -> Dict[str, Any]:
        """Retrieves a paginated list of all contacts in Front. Use this to enumerate or browse the full contact directory. Do not use this when you need details for a specific contact — use front_get_contact with a contact ID instead.
        Returns:
            API response as a dictionary.
        """
        ...

    def front_remove_contact_from_account(
        self,
        accountId: str,
        contact_ids: List[Any],
    ) -> Dict[str, Any]:
        """Removes the association between one or more contacts and a specific Front account, identified by the account ID. Use this to unlink contacts from an account without deleting the contact or account records themselves. Do not use this to permanently delete a contact — use front_delete_contact instead.

        Args:
            accountId: Account ID for the request. (required)
            contact_ids: Array of contact IDs. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def front_update_account(
        self,
        accountId: str,
        description: str,
        name: str,
        domains: Optional[List[Any]] = None,
        logo_url: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Updates information for an existing account in Front, identified by the account ID. Use this to modify account fields such as name, domain, or custom attributes. Do not use this to create a new account — use front_create_account instead. This operation modifies the account record in place.

        Args:
            accountId: ID of the account. (required)
            description: Description of the resource. (required)
            name: Name of the resource. (required)
            domains: Array of domains associated with the resource.
            logo_url: URL of the logo for the resource.
        Returns:
            API response as a dictionary.
        """
        ...

    def front_update_contact(
        self,
        contactId: str,
        description: str,
        handles: List[Any],
        name: str,
    ) -> Dict[str, Any]:
        """Updates information for an existing contact in Front, identified by their contact ID. Use this to modify contact fields such as name, email, phone, or custom attributes. Do not use this to create a new contact — use front_create_contact instead. This operation modifies the contact record in place.

        Args:
            contactId: The ID of the contact. (required)
            description: The description. (required)
            handles:  (required)
            name: The name. (required)
        Returns:
            API response as a dictionary.
        """
        ...

