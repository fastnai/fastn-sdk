"""Fastn Microsoft Dynamics 365 Sales Hub connector — auto-generated type stubs.

Do not edit manually. Regenerate with `fastn connector sync`.
"""
from __future__ import annotations

from typing import Any, Dict, List, Optional, TypedDict


class MicrosoftDynamics365SalesHubConnector:
    """Microsoft Dynamics 365 Sales Hub connector ().

    Provides 2 tools.
    """

    def microsoft_dynamics_365_sales_hub_create_contact(
        self,
        address1_city: str,
        address1_country: str,
        allow_duplicates: bool,
        emailaddress1: str,
        firstname: str,
        lastname: str,
        mobilephone: str,
        salutation: str,
        telephone1: str,
        jobtitle: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Creates a new contact record in Microsoft Dynamics 365 Sales Hub. Use this tool when you need to add a new person or organization contact to the CRM for sales tracking, communication history, or customer relationship management. Do not use this tool to update an existing contact — use the update contact tool instead. This operation persists a new contact record and cannot be undone without a separate delete operation.

        Args:
            address1_city: The city of the contact's address. (required)
            address1_country: The country of the contact's address. (required)
            allow_duplicates: Flag indicating whether duplicate entries are allowed. (required)
            emailaddress1: The email address of the contact. (required)
            firstname: The first name of the contact. (required)
            lastname: The last name of the contact. (required)
            mobilephone: The mobile phone number of the contact. (required)
            salutation: The salutation for the contact (e.g., Mr., Ms.). (required)
            telephone1: The telephone number of the contact. (required)
            jobtitle: The job title of the contact.
        Returns:
            API response as a dictionary.
        """
        ...

    def microsoft_dynamics_365_sales_hub_generate_auth_token(
        self,
        clientId: str,
        client_id: str,
        password: str,
        scope: str,
        tenant_id: str,
        username: str,
    ) -> Dict[str, Any]:
        """Generates an OAuth 2.0 access token using username and password credentials (Resource Owner Password Credentials grant) against the Microsoft identity platform. Use this tool when you need to authenticate with Microsoft Dynamics 365 Sales Hub APIs and obtain a bearer token for subsequent API calls. Do not use this tool for interactive user login flows or when client credentials or authorization code grants are more appropriate. The generated token is temporary and will expire based on the configured token lifetime.

        Args:
            clientId: The client ID associated with the application making the request. (required)
            client_id: The identifier for the client application requesting authentication. (required)
            password: The password of the user for authentication. (required)
            scope: The scope of the authorization request, defining access levels. (required)
            tenant_id: The unique identifier for the tenant in string format. (required)
            username: The username of the user for authentication. (required)
        Returns:
            API response as a dictionary.
        """
        ...

