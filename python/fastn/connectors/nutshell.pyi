"""Fastn Nutshell connector — auto-generated type stubs.

Do not edit manually. Regenerate with `fastn connector sync`.
"""
from __future__ import annotations

from typing import Any, Dict, List, Optional


class NutshellConnector:
    """Nutshell connector ().

    Provides 14 tools.
    """

    def create_contact(
        self,
        contacts: Optional[List[Any]] = None,
    ) -> Dict[str, Any]:
        """Creates a new contact in the system.

        Args:
            contacts: 
        Returns:
            API response as a dictionary.
        """
        ...

    def create_lead(
        self,
        leads: Optional[List[Any]] = None,
    ) -> Dict[str, Any]:
        """Creates a new lead in the system.

        Args:
            leads: 
        Returns:
            API response as a dictionary.
        """
        ...

    def create_tag(
        self,
        tags: Optional[List[Any]] = None,
    ) -> Dict[str, Any]:
        """Creates a new tag for organization or categorization in the system.

        Args:
            tags: 
        Returns:
            API response as a dictionary.
        """
        ...

    def get_activities(
        self,
    ) -> Dict[str, Any]:
        """Retrieves a list of activities associated with a specific entity in the system.
        Returns:
            API response as a dictionary.
        """
        ...

    def get_audiences(
        self,
    ) -> Dict[str, Any]:
        """Fetches a list of audiences available in the system.
        Returns:
            API response as a dictionary.
        """
        ...

    def get_competitors(
        self,
    ) -> Dict[str, Any]:
        """Retrieves information about competitors in the system.
        Returns:
            API response as a dictionary.
        """
        ...

    def get_contact(
        self,
        contactId: str,
    ) -> Dict[str, Any]:
        """Fetches details of a specific contact from the system.

        Args:
            contactId:  (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def get_contacts(
        self,
    ) -> Dict[str, Any]:
        """Retrieves a list of contacts in the system.
        Returns:
            API response as a dictionary.
        """
        ...

    def get_lead(
        self,
        leadId: str,
    ) -> Dict[str, Any]:
        """Fetches details of a specific lead from the system.

        Args:
            leadId: ID of the lead. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def get_leads(
        self,
    ) -> Dict[str, Any]:
        """Retrieves a list of leads in the system.
        Returns:
            API response as a dictionary.
        """
        ...

    def get_products(
        self,
    ) -> Dict[str, Any]:
        """Fetches a list of products available in the system.
        Returns:
            API response as a dictionary.
        """
        ...

    def get_tags(
        self,
        filtertagType: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Retrieves a list of tags in the system.

        Args:
            filtertagType: Type of filter tag to apply.
        Returns:
            API response as a dictionary.
        """
        ...

    def get_territories(
        self,
    ) -> Dict[str, Any]:
        """Fetches a list of territories defined in the system.
        Returns:
            API response as a dictionary.
        """
        ...

    def get_users(
        self,
    ) -> Dict[str, Any]:
        """Retrieves a list of users in the system.
        Returns:
            API response as a dictionary.
        """
        ...

