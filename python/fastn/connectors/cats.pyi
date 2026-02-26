"""Fastn CATS connector — auto-generated type stubs.

Do not edit manually. Regenerate with `fastn connector sync`.
"""
from __future__ import annotations

from typing import Any, Dict, List, Optional


class CatsConnector:
    """CATS connector ().

    Provides 13 tools.
    """

    def create_candidate(
        self,
        first_name: str,
        last_name: str,
        emails: Optional[List[Any]] = None,
        phones: Optional[List[Any]] = None,
        title: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Creates a new candidate in the specified connector.

        Args:
            first_name: First name of the individual. (required)
            last_name: Last name of the individual. (required)
            emails: 
            phones: 
            title: Title of the individual (e.g., Mr., Ms.).
        Returns:
            API response as a dictionary.
        """
        ...

    def create_company_list(
        self,
        name: str,
        notes: str,
    ) -> Dict[str, Any]:
        """Creates a new company list in the connector.

        Args:
            name: The name associated with the request. (required)
            notes: Additional notes or information. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def delete_activities(
        self,
        activitieId: str,
    ) -> Dict[str, Any]:
        """Deletes specified activities from the connector's system.

        Args:
            activitieId: ID of the activity. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def delete_candidate(
        self,
        candidateId: str,
    ) -> Dict[str, Any]:
        """Deletes a specific candidate from the connector's system.

        Args:
            candidateId: ID of the candidate.  Used to identify the specific candidate within the CATS CATS endpoint. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def delete_company_list(
        self,
        listId: str,
    ) -> Dict[str, Any]:
        """Deletes a specific company list from the connector's system.

        Args:
            listId: ID of the list. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def get_activitie(
        self,
        activitieId: str,
    ) -> Dict[str, Any]:
        """Retrieves detailed information about a specific activity from the specified connector.

        Args:
            activitieId: ID of the activity. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def get_activities(
        self,
    ) -> Dict[str, Any]:
        """Retrieves a list of activities from the specified connector.
        Returns:
            API response as a dictionary.
        """
        ...

    def get_candidate(
        self,
        candidateId: str,
    ) -> Dict[str, Any]:
        """Retrieves detailed information about a specific candidate from the specified connector.

        Args:
            candidateId: ID of the candidate. This parameter is used to identify the candidate in the CATS system. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def get_candidates(
        self,
    ) -> Dict[str, Any]:
        """Fetches a list of candidates from the specified connector.
        Returns:
            API response as a dictionary.
        """
        ...

    def get_company_list(
        self,
        listId: str,
    ) -> Dict[str, Any]:
        """Retrieves detailed information about a specific company list from the specified connector.

        Args:
            listId: ID of the list. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def get_company_lists(
        self,
    ) -> Dict[str, Any]:
        """Retrieves a list of company lists from the specified connector.
        Returns:
            API response as a dictionary.
        """
        ...

    def update_activity(
        self,
        date: str,
        notes: str,
        regarding_id: int,
        type: str,
    ) -> Dict[str, Any]:
        """Updates the details of an existing activity in the connector.

        Args:
            date: Date related to the activity. (required)
            notes: Notes or description of the activity. (required)
            regarding_id: ID of the object this activity relates to. (required)
            type: Type of activity. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def update_candidate(
        self,
        emails: Dict[str, Any],
        first_name: str,
        last_name: str,
        custom_fields: Optional[List[Any]] = None,
        phones: Optional[Dict[str, Any]] = None,
        title: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Updates information for an existing candidate in the connector.

        Args:
            emails: Email addresses for the candidate. (required)
            first_name: First name of the candidate. (required)
            last_name: Last name of the candidate. (required)
            custom_fields: 
            phones: Phone numbers for the candidate.
            title: Title of the candidate.
        Returns:
            API response as a dictionary.
        """
        ...

