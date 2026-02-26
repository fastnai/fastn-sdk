"""Fastn Insightly connector — auto-generated type stubs.

Do not edit manually. Regenerate with `fastn connector sync`.
"""
from __future__ import annotations

from typing import Any, Dict, List, Optional


class InsightlyConnector:
    """Insightly connector ().

    Provides 11 tools.
    """

    def chat_completion(
        self,
        messages: List[Any],
        model: str,
    ) -> Dict[str, Any]:
        """Generates chat completions based on provided prompts through the specified connector.

        Args:
            messages:  (required)
            model: Model related to the request. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def create_contact(
        self,
        EMAIL_ADDRESS: str,
        FIRST_NAME: str,
        LAST_NAME: str,
        PHONE: str,
    ) -> Dict[str, Any]:
        """Creates a new contact entry in the system using the specified API connector.

        Args:
            EMAIL_ADDRESS: The email address of the contact. (required)
            FIRST_NAME: The first name of the contact. (required)
            LAST_NAME: The last name of the contact. (required)
            PHONE: The phone number of the contact. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def create_organization(
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
        """Creates a new organization in the system using the specified API connector.

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

    def delete_contact(
        self,
        contactId: str,
    ) -> Dict[str, Any]:
        """Deletes a specific contact from the system using its identifier via the API connector.

        Args:
            contactId: The ID of the contact. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def delete_organization(
        self,
        organizationId: str,
    ) -> Dict[str, Any]:
        """Deletes a specific organization from the system using its identifier via the API connector.

        Args:
            organizationId: The ID of the organization to target within the Insightly API. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def get_contact(
        self,
        contactId: str,
    ) -> Dict[str, Any]:
        """Retrieves detailed information about a specific contact in the system using its unique identifier via the connector.

        Args:
            contactId:  (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def get_contacts(
        self,
    ) -> Dict[str, Any]:
        """Fetches all contacts stored in the system through the designated connector.
        Returns:
            API response as a dictionary.
        """
        ...

    def get_organizations(
        self,
    ) -> Dict[str, Any]:
        """Retrieves a list of organizations in the system using the appropriate API connector.
        Returns:
            API response as a dictionary.
        """
        ...

    def get_users(
        self,
    ) -> Dict[str, Any]:
        """Retrieves a list of users in the system using the appropriate API connector.
        Returns:
            API response as a dictionary.
        """
        ...

    def update_contact(
        self,
        EMAIL_ADDRESS: str,
        FIRST_NAME: str,
        LAST_NAME: str,
    ) -> Dict[str, Any]:
        """Updates the details of an existing contact in the system through the connector.

        Args:
            EMAIL_ADDRESS: The email address of the contact. (required)
            FIRST_NAME: The first name of the contact. (required)
            LAST_NAME: The last name of the contact. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def update_organization(
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
        """Updates the information of an existing organization in the system using the designated API connector.

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

