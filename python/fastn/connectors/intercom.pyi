"""Fastn Intercom connector — auto-generated type stubs.

Do not edit manually. Regenerate with `fastn connector sync`.
"""
from __future__ import annotations

from typing import Any, Dict, List, Optional, TypedDict


class IntercomConnector:
    """Intercom connector ().

    Provides 5 tools.
    """

    def intercom_create_contact(
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
        """Creates a new contact record in Intercom. Use this tool when onboarding a new user or customer who does not yet exist in Intercom. Do not use this tool to update an existing contact — use intercom_update_contact instead. Check for duplicate contacts before calling this tool to avoid creating redundant records. This action creates a persistent contact entry in Intercom.

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

    def intercom_delete_contact(
        self,
        contactId: str,
    ) -> Dict[str, Any]:
        """Permanently deletes a specific contact from Intercom by their unique contact ID. Use this tool only when a contact record must be fully removed from the system, such as for GDPR erasure requests or data cleanup. Do not use this tool to simply deactivate or archive a contact. This action is irreversible — the contact and all associated data will be permanently deleted and cannot be recovered.

        Args:
            contactId: The ID of the contact in Intercom. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def intercom_get_contact(
        self,
        contactId: str,
    ) -> Dict[str, Any]:
        """Retrieves detailed information about a single Intercom contact by their unique contact ID. Use this tool when you need full profile data for a specific contact, such as name, email, and interaction history. Requires a valid contactId; use intercom_list_contacts first if you need to discover contact IDs. This is a read-only operation with no side effects.

        Args:
            contactId: ID of the contact in Intercom. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def intercom_list_contacts(
        self,
        per_page: Optional[str] = None,
        starting_after: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Retrieves a list of all contacts from Intercom. Use this tool when you need to browse, filter, or process multiple contacts at once. For detailed information about a single specific contact, use intercom_get_contact instead. This is a read-only operation with no side effects.

        Args:
            per_page: 
            starting_after: 
        Returns:
            API response as a dictionary.
        """
        ...

    def intercom_update_contact(
        self,
        contactId: str,
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
        """Updates the details of an existing Intercom contact by their unique contact ID. Use this tool when you need to modify contact attributes such as name, email, phone, or custom fields. Requires a valid contactId and the fields to update; it will overwrite the provided fields on the existing record. Do not use this tool to create new contacts — use intercom_create_contact instead. This action modifies the contact record in place.

        Args:
            contactId: The ID of the contact. (required)
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

