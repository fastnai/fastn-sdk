"""Fastn Workday connector — auto-generated type stubs.

Do not edit manually. Regenerate with `fastn connector sync`.
"""
from __future__ import annotations

from typing import Any, Dict, List, Optional, TypedDict


class WorkdayConnector:
    """Workday connector ().

    Provides 4 tools.
    """

    def workday_get_person(
        self,
        tenantHostname: str,
        authToken: Optional[str] = None,
        universal_ID: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Retrieves core profile information for a single person in Workday by their universal ID. Use this as the starting point to look up an individual before fetching more specific data such as personal information or home addresses. For richer personal detail, follow up with workday_get_person_personal_information.

        Args:
            tenantHostname:  (required)
            authToken: 
            universal_ID: 
        Returns:
            API response as a dictionary.
        """
        ...

    def workday_get_person_personal_information(
        self,
        person_Id: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Retrieves personal information for a specific person in Workday by their person ID, including birth date, contact details, and background data. Use this when you need demographic or personal profile data for a single individual. Do not use this to retrieve home addresses or additional names — use workday_list_person_home_addresses or workday_list_person_additional_names instead.

        Args:
            person_Id: 
        Returns:
            API response as a dictionary.
        """
        ...

    def workday_list_person_additional_names(
        self,
        tenantHostname: str,
        authToken: Optional[str] = None,
        person_Id: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Retrieves all additional names (e.g., aliases, preferred names, legal name variations) associated with a specific person in Workday by their person ID. Use this when alternate names for an individual are needed. For primary personal information, use workday_get_person_personal_information instead.

        Args:
            tenantHostname:  (required)
            authToken: 
            person_Id: 
        Returns:
            API response as a dictionary.
        """
        ...

    def workday_list_person_home_addresses(
        self,
        person_Id: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Retrieves all home addresses on file for a specific person in Workday by their person ID. Use this when you need to access or display a persons residential address information. For personal details such as birth date or contact info, use workday_get_person_personal_information instead.

        Args:
            person_Id: 
        Returns:
            API response as a dictionary.
        """
        ...

