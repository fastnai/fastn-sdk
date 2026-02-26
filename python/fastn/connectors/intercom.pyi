"""Fastn Intercom connector — auto-generated type stubs.

Do not edit manually. Regenerate with `fastn connector sync`.
"""
from __future__ import annotations

from typing import Any, Dict, List, Optional


class IntercomConnector:
    """Intercom connector ().

    Provides 5 tools.
    """

    def create_contact(
        self,
        email: str,
        avatar: Optional[str] = None,
        custom_attributes: Optional[Dict[str, Any]] = None,
        external_id: Optional[str] = None,
        last_seen_at: Optional[int] = None,
        name: Optional[str] = None,
        owner_id: Optional[int] = None,
        phone: Optional[str] = None,
        role: Optional[str] = None,
        signed_up_at: Optional[int] = None,
        unsubscribed_from_emails: Optional[bool] = None,
    ) -> Dict[str, Any]:
        """Creates a new contact in the contact management system.

        Args:
            email: The email address of the user. (required)
            avatar: URL of the user's avatar image.
            custom_attributes: Custom attributes associated with the user.
            external_id: An external identifier for the user.
            last_seen_at: Timestamp indicating when the user was last seen.
            name: The name of the user.
            owner_id: The ID of the user's owner within the Intercom application.
            phone: The phone number associated with the user.
            role: The role of the user within the Intercom application.
            signed_up_at: Timestamp indicating when the user signed up.
            unsubscribed_from_emails: Indicates whether the user has unsubscribed from email communications.
        Returns:
            API response as a dictionary.
        """
        ...

    def delete_contact(
        self,
        contactId: str,
    ) -> Dict[str, Any]:
        """Deletes a specified contact from the contact management system.

        Args:
            contactId: The ID of the contact in Intercom. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def get_contact(
        self,
        contactId: str,
    ) -> Dict[str, Any]:
        """Fetches detailed information about a specific contact in the contact management system.

        Args:
            contactId: ID of the contact in Intercom. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def get_contacts(
        self,
        per_page: Optional[str] = None,
        starting_after: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Retrieves a list of all contacts from the contact management system.

        Args:
            per_page: 
            starting_after: 
        Returns:
            API response as a dictionary.
        """
        ...

    def update_contact(
        self,
        avatar: Optional[str] = None,
        custom_attributes: Optional[Dict[str, Any]] = None,
        email: Optional[str] = None,
        external_id: Optional[str] = None,
        last_seen_at: Optional[int] = None,
        name: Optional[str] = None,
        owner_id: Optional[int] = None,
        phone: Optional[str] = None,
        role: Optional[str] = None,
        signed_up_at: Optional[int] = None,
        unsubscribed_from_emails: Optional[bool] = None,
    ) -> Dict[str, Any]:
        """Updates details for an existing contact in the contact management system.

        Args:
            avatar: URL of the user's avatar.
            custom_attributes: Custom attributes associated with the user.
            email: The user's email address.
            external_id: The user's external ID.
            last_seen_at: Timestamp indicating when the user was last seen.
            name: The user's name.
            owner_id: The ID of the user's owner.
            phone: The user's phone number.
            role: The user's role.
            signed_up_at: Timestamp indicating when the user signed up.
            unsubscribed_from_emails: Indicates if the user is unsubscribed from emails.
        Returns:
            API response as a dictionary.
        """
        ...

