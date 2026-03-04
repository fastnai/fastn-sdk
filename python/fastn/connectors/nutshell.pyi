"""Fastn Nutshell connector — auto-generated type stubs.

Do not edit manually. Regenerate with `fastn connector sync`.
"""
from __future__ import annotations

from typing import Any, Dict, List, Optional, TypedDict


class NutshellConnector:
    """Nutshell connector ().

    Provides 14 tools.
    """

    def nutshell_create_contact(
        self,
        contacts: Optional[List[Any]] = None,
    ) -> Dict[str, Any]:
        """Creates a new contact record in Nutshell CRM. Use this tool when a new person or company needs to be added to the CRM. Requires contact details such as name, email, and phone number. This action modifies data by adding a new contact to the system.

        Args:
            contacts: 
        Returns:
            API response as a dictionary.
        """
        ...

    def nutshell_create_lead(
        self,
        leads: Optional[List[Any]] = None,
    ) -> Dict[str, Any]:
        """Creates a new lead record in Nutshell CRM. Use this tool when a new sales opportunity needs to be tracked. Requires lead details such as associated contacts, value, and pipeline stage. This action modifies data by adding a new lead to the system.

        Args:
            leads: 
        Returns:
            API response as a dictionary.
        """
        ...

    def nutshell_create_tag(
        self,
        tags: Optional[List[Any]] = None,
    ) -> Dict[str, Any]:
        """Creates a new tag in Nutshell CRM for use in categorizing and organizing records such as leads and contacts. Use this tool when a required tag does not already exist. To view existing tags before creating a new one, use nutshell_list_tags first. This action modifies data by adding a new tag to the system.

        Args:
            tags: 
        Returns:
            API response as a dictionary.
        """
        ...

    def nutshell_get_contact(
        self,
        contactId: str,
    ) -> Dict[str, Any]:
        """Retrieves full details of a single contact from Nutshell CRM by their contact ID, including name, email, phone, and associated leads. Use this tool when you need complete information about one specific contact. To list all contacts, use nutshell_list_contacts instead. Does not modify any data.

        Args:
            contactId:  (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def nutshell_get_lead(
        self,
        leadId: str,
    ) -> Dict[str, Any]:
        """Retrieves full details of a single lead from Nutshell CRM by its lead ID, including status, assigned users, associated contacts, and pipeline stage. Use this tool when you need complete information about one specific lead. To list all leads, use nutshell_list_leads instead. Does not modify any data.

        Args:
            leadId: ID of the lead. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def nutshell_list_activities(
        self,
    ) -> Dict[str, Any]:
        """Retrieves a list of activities logged in Nutshell CRM, such as calls, meetings, and tasks. Use this tool to review activity history across CRM entities. Does not modify any data.
        Returns:
            API response as a dictionary.
        """
        ...

    def nutshell_list_audiences(
        self,
    ) -> Dict[str, Any]:
        """Retrieves a list of all audiences defined in Nutshell CRM. Use this tool to view audience segments used for targeting and marketing purposes. Does not modify any data.
        Returns:
            API response as a dictionary.
        """
        ...

    def nutshell_list_competitors(
        self,
    ) -> Dict[str, Any]:
        """Retrieves a list of all competitors tracked in Nutshell CRM. Use this tool to view competitor records used in sales analysis and lead tracking. Does not modify any data.
        Returns:
            API response as a dictionary.
        """
        ...

    def nutshell_list_contacts(
        self,
    ) -> Dict[str, Any]:
        """Retrieves a list of all contacts in Nutshell CRM. Use this tool to browse or enumerate contact records. For detailed information about a single contact, use nutshell_get_contact with a specific contact ID. Does not modify any data.
        Returns:
            API response as a dictionary.
        """
        ...

    def nutshell_list_leads(
        self,
    ) -> Dict[str, Any]:
        """Retrieves a list of all leads in Nutshell CRM. Use this tool when you need an overview of pipeline leads. For detailed information about a single lead, use nutshell_get_lead with a specific lead ID. Does not modify any data.
        Returns:
            API response as a dictionary.
        """
        ...

    def nutshell_list_products(
        self,
    ) -> Dict[str, Any]:
        """Retrieves a list of all products available in Nutshell CRM. Use this tool to view product catalog entries used in leads and sales processes. Does not modify any data.
        Returns:
            API response as a dictionary.
        """
        ...

    def nutshell_list_tags(
        self,
        filtertagType: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Retrieves a list of all tags available in Nutshell CRM. Use this tool to view existing tags used for categorization and organization of records. To create a new tag, use nutshell_create_tag instead. Does not modify any data.

        Args:
            filtertagType: Type of filter tag to apply.
        Returns:
            API response as a dictionary.
        """
        ...

    def nutshell_list_territories(
        self,
    ) -> Dict[str, Any]:
        """Retrieves a list of all sales territories defined in Nutshell CRM. Use this tool to view territory assignments and configurations. Does not modify any data.
        Returns:
            API response as a dictionary.
        """
        ...

    def nutshell_list_users(
        self,
    ) -> Dict[str, Any]:
        """Retrieves a list of all users in the Nutshell CRM system. Use this tool to obtain user records including names, roles, and identifiers. For a single users details, filter results from this list. Does not modify any data.
        Returns:
            API response as a dictionary.
        """
        ...

