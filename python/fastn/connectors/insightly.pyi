"""Fastn Insightly connector — auto-generated type stubs.

Do not edit manually. Regenerate with `fastn connector sync`.
"""
from __future__ import annotations

from typing import Any, Dict, List, Optional, TypedDict


class InsightlyConnector:
    """Insightly connector ().

    Provides 11 tools.
    """

    def insightly_create_contact(
        self,
        EMAIL_ADDRESS: str,
        FIRST_NAME: str,
        LAST_NAME: str,
        PHONE: str,
    ) -> Dict[str, Any]:
        """Creates a new contact record in Insightly CRM with the provided details such as name, email, and phone number. Use this when adding a new individual to the CRM. Do not use this to update an existing contact.

        Args:
            EMAIL_ADDRESS: The email address of the contact. (required)
            FIRST_NAME: The first name of the contact. (required)
            LAST_NAME: The last name of the contact. (required)
            PHONE: The phone number of the contact. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def insightly_create_organization(
        self,
        ADDRESS_BILLING_CITY: str,
        ADDRESS_BILLING_COUNTRY: str,
        ADDRESS_BILLING_POSTCODE: str,
        ADDRESS_BILLING_STATE: str,
        ADDRESS_BILLING_STREET: str,
        ADDRESS_SHIP_CITY: str,
        ADDRESS_SHIP_COUNTRY: str,
        ADDRESS_SHIP_POSTCODE: str,
        ADDRESS_SHIP_STATE: str,
        ADDRESS_SHIP_STREET: str,
        ORGANISATION_NAME: str,
        PHONE: str,
        WEBSITE: str,
    ) -> Dict[str, Any]:
        """Creates a new organization record in Insightly CRM with the provided details such as name, address, and custom fields. Use this when onboarding a new company or account into the CRM. Do not use this to update an existing organization.

        Args:
            ADDRESS_BILLING_CITY: Billing city of the organization. (required)
            ADDRESS_BILLING_COUNTRY: Billing country of the organization. (required)
            ADDRESS_BILLING_POSTCODE: Billing postal code of the organization. (required)
            ADDRESS_BILLING_STATE: Billing state or province of the organization. (required)
            ADDRESS_BILLING_STREET: Billing street address of the organization. (required)
            ADDRESS_SHIP_CITY: Shipping city of the organization. (required)
            ADDRESS_SHIP_COUNTRY: Shipping country of the organization. (required)
            ADDRESS_SHIP_POSTCODE: Shipping postal code of the organization. (required)
            ADDRESS_SHIP_STATE: Shipping state or province of the organization. (required)
            ADDRESS_SHIP_STREET: Shipping street address of the organization. (required)
            ORGANISATION_NAME: Name of the organization. (required)
            PHONE: Primary phone number of the organization. (required)
            WEBSITE: Website URL of the organization. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def insightly_delete_contact(
        self,
        contactId: str,
    ) -> Dict[str, Any]:
        """Permanently deletes a specific contact record from Insightly CRM using its contact ID. Use this to remove a contact that is no longer relevant. This action is irreversible. Do not use this if you only want to update the contacts details.

        Args:
            contactId: The ID of the contact. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def insightly_delete_organization(
        self,
        organizationId: str,
    ) -> Dict[str, Any]:
        """Permanently deletes a specific organization record from Insightly CRM using its organization ID. Use this to remove an organization that is no longer relevant. This action is irreversible and will remove the organization along with its associated CRM data. Do not use this if you only want to update the organizations details.

        Args:
            organizationId: The ID of the organization to target within the Insightly API. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def insightly_get_contact(
        self,
        contactId: str,
    ) -> Dict[str, Any]:
        """Retrieves detailed information about a single contact in Insightly CRM identified by its contact ID, including name, email, phone number, and associated organizations. Use this when you need full details for a specific contact. Do not use this to list all contacts or to modify contact data.

        Args:
            contactId:  (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def insightly_list_contacts(
        self,
    ) -> Dict[str, Any]:
        """Returns a list of all contact records stored in Insightly CRM. Use this to enumerate contacts when you do not have a specific contact ID, or to browse all individuals in the CRM. Do not use this to retrieve details of a single contact by ID.
        Returns:
            API response as a dictionary.
        """
        ...

    def insightly_list_organizations(
        self,
    ) -> Dict[str, Any]:
        """Returns a list of all organization records in Insightly CRM. Use this to enumerate organizations when you do not have a specific organization ID, or to browse all companies in the CRM. Do not use this to retrieve details of a single organization by ID.
        Returns:
            API response as a dictionary.
        """
        ...

    def insightly_list_users(
        self,
    ) -> Dict[str, Any]:
        """Returns a list of all user accounts in Insightly CRM. Use this to enumerate system users, audit team membership, or look up user IDs for assignment operations. Do not use this to retrieve contact or organization records.
        Returns:
            API response as a dictionary.
        """
        ...

    def insightly_update_contact(
        self,
        EMAIL_ADDRESS: str,
        FIRST_NAME: str,
        LAST_NAME: str,
    ) -> Dict[str, Any]:
        """Updates the details of an existing contact record in Insightly CRM, such as name, email, phone number, or custom fields. Use this to keep contact information current. Do not use this to create a new contact or delete an existing one.

        Args:
            EMAIL_ADDRESS: The email address of the contact. (required)
            FIRST_NAME: The first name of the contact. (required)
            LAST_NAME: The last name of the contact. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def insightly_update_organization(
        self,
        ADDRESS_BILLING_CITY: str,
        ADDRESS_BILLING_COUNTRY: str,
        ADDRESS_BILLING_POSTCODE: str,
        ADDRESS_BILLING_STATE: str,
        ADDRESS_BILLING_STREET: str,
        ADDRESS_SHIP_CITY: str,
        ADDRESS_SHIP_COUNTRY: str,
        ADDRESS_SHIP_POSTCODE: str,
        ADDRESS_SHIP_STATE: str,
        ADDRESS_SHIP_STREET: str,
        ORGANISATION_ID: int,
        ORGANISATION_NAME: str,
        PHONE: str,
        WEBSITE: str,
    ) -> Dict[str, Any]:
        """Updates the information of an existing organization record in Insightly CRM, such as name, address, or custom fields. Use this to keep organization data current. Do not use this to create a new organization or delete an existing one.

        Args:
            ADDRESS_BILLING_CITY: Billing city for the organization. (required)
            ADDRESS_BILLING_COUNTRY: Billing country for the organization. (required)
            ADDRESS_BILLING_POSTCODE: Billing postal code for the organization. (required)
            ADDRESS_BILLING_STATE: Billing state/province for the organization. (required)
            ADDRESS_BILLING_STREET: Billing street address for the organization. (required)
            ADDRESS_SHIP_CITY: Shipping city for the organization. (required)
            ADDRESS_SHIP_COUNTRY: Shipping country for the organization. (required)
            ADDRESS_SHIP_POSTCODE: Shipping postal code for the organization. (required)
            ADDRESS_SHIP_STATE: Shipping state/province for the organization. (required)
            ADDRESS_SHIP_STREET: Shipping street address for the organization. (required)
            ORGANISATION_ID: Unique identifier for the organization (if updating an existing organization). (required)
            ORGANISATION_NAME: Name of the organization. (required)
            PHONE: Phone number for the organization. (required)
            WEBSITE: Website URL for the organization. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def minimax_chat_completion(
        self,
        messages: List[Any],
        model: str,
    ) -> Dict[str, Any]:
        """Sends a chat completion request to the MiniMax AI API and returns a generated text response. Use this tool when you need to generate conversational AI responses, complete prompts, or interact with the MiniMax large language model. Do not use this tool for accounting, tax management, or any non-AI tasks. This tool makes a POST request to the MiniMax chat API and may incur usage costs per call.

        Args:
            messages:  (required)
            model: Model related to the request. (required)
        Returns:
            API response as a dictionary.
        """
        ...

