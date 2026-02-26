"""Fastn Workday connector — auto-generated type stubs.

Do not edit manually. Regenerate with `fastn connector sync`.
"""
from __future__ import annotations

from typing import Any, Dict, List, Optional


class WorkdayConnector:
    """Workday connector ().

    Provides 4 tools.
    """

    def get_person(
        self,
    ) -> Dict[str, Any]:
        """Retrieves detailed information about an individual from the database, enabling users to access personal data stored in the system.
        Returns:
            API response as a dictionary.
        """
        ...

    def get_person_additional_names(
        self,
    ) -> Dict[str, Any]:
        """Fetches all additional names associated with a specific person from the database, allowing users to view alternate names or aliases linked to that individual.
        Returns:
            API response as a dictionary.
        """
        ...

    def get_person_home_addresses(
        self,
    ) -> Dict[str, Any]:
        """Obtains all home addresses listed for a particular person in the database, providing users with comprehensive address details for the individual.
        Returns:
            API response as a dictionary.
        """
        ...

    def get_person_personal_information(
        self,
    ) -> Dict[str, Any]:
        """Accesses personal information of an individual from the database, including key details such as birth date, contact information, and background data.
        Returns:
            API response as a dictionary.
        """
        ...

