"""Fastn Microsoft Dynamics 365 Business Central connector — auto-generated type stubs.

Do not edit manually. Regenerate with `fastn connector sync`.
"""
from __future__ import annotations

from typing import Any, Dict, List, Optional


class MicrosoftDynamics365BusinessCentralConnector:
    """Microsoft Dynamics 365 Business Central connector ().

    Provides 6 tools.
    """

    def create_contact(
        self,
        company: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Creates a new contact in the specified system via the API connector, allowing the addition of new individuals to the contact management database.

        Args:
            company: The name of the company.
        Returns:
            API response as a dictionary.
        """
        ...

    def create_journals(
        self,
        code: str,
        displayName: str,
    ) -> Dict[str, Any]:
        """Creates a new journal entry using the API connector, enabling users to add records and notes to the journal system.

        Args:
            code: Code related to the request body. (required)
            displayName: Display name related to the request body. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def generate_token(
        self,
        client_id: str,
        password: str,
        scope: str,
        username: str,
    ) -> Dict[str, Any]:
        """Generates an authentication token for use with the API connector, allowing access to secured endpoints.

        Args:
            client_id: Client ID for Microsoft Dynamics 365 Business Central authentication. (required)
            password: Password for Microsoft Dynamics 365 Business Central authentication. (required)
            scope: Scope of access for the Microsoft Dynamics 365 Business Central request. (required)
            username: Username for Microsoft Dynamics 365 Business Central authentication. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def get_companies(
        self,
        tenantId: str,
    ) -> Dict[str, Any]:
        """Retrieves a list of companies from the database using the appropriate API connector, providing information on each company available in the system.

        Args:
            tenantId: Tenant ID for accessing the Microsoft Dynamics 365 Business Central instance. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def get_contacts(
        self,
        company: Optional[str] = None,
        filter: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Retrieves a list of contacts from the database using the API connector, providing details on individuals stored in the contact management system.

        Args:
            company: The company ID or name.
            filter: Filter criteria for the request.
        Returns:
            API response as a dictionary.
        """
        ...

    def get_journals(
        self,
        companyId: str,
        tenantId: str,
    ) -> Dict[str, Any]:
        """Fetches a list of journals from the database via the API connector, providing access to entries and records stored in the journal system.

        Args:
            companyId: ID of the company. (required)
            tenantId: Tenant ID. (required)
        Returns:
            API response as a dictionary.
        """
        ...

