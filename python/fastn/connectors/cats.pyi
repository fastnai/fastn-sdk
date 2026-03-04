"""Fastn CATS connector — auto-generated type stubs.

Do not edit manually. Regenerate with `fastn connector sync`.
"""
from __future__ import annotations

from typing import Any, Dict, List, Optional, TypedDict


class _CatsUpdateCandidateEmails(TypedDict, total=False):
    primary: str

class _CatsUpdateCandidatePhones(TypedDict, total=False):
    home: str

class CatsConnector:
    """CATS connector ().

    Provides 13 tools.
    """

    def cats_create_candidate(
        self,
        first_name: str,
        last_name: str,
        emails: Optional[List[Any]] = None,
        phones: Optional[List[Any]] = None,
        title: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Creates a new candidate record in CATS. Use this when onboarding a new applicant into the ATS for the first time. Do not use this to update an existing candidate — use cats_update_candidate instead. This action is reversible via cats_delete_candidate.

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

    def cats_create_company_list(
        self,
        name: str,
        notes: str,
    ) -> Dict[str, Any]:
        """Creates a new company list in CATS for grouping and organizing companies within recruiting workflows. Use this when you need a named collection to associate multiple companies together. Do not use this to modify an existing list.

        Args:
            name: The name associated with the request. (required)
            notes: Additional notes or information. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def cats_delete_activity(
        self,
        activitieId: str,
    ) -> Dict[str, Any]:
        """Permanently deletes a specific activity record from CATS by activity ID. Use this to remove erroneous or duplicate activity entries. This action is irreversible — the activity cannot be recovered after deletion.

        Args:
            activitieId: ID of the activity. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def cats_delete_candidate(
        self,
        candidateId: str,
    ) -> Dict[str, Any]:
        """Permanently deletes a specific candidate record from CATS by candidate ID. Use this to remove a duplicate or invalid candidate entry. This action is irreversible — all data associated with the candidate will be lost.

        Args:
            candidateId: ID of the candidate.  Used to identify the specific candidate within the CATS CATS endpoint. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def cats_delete_company_list(
        self,
        listId: str,
    ) -> Dict[str, Any]:
        """Permanently deletes a specific company list from CATS by its list ID. Use this to remove an obsolete or erroneous company grouping. This action is irreversible — the list and its associations cannot be recovered after deletion.

        Args:
            listId: ID of the list. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def cats_get_activity(
        self,
        activitieId: str,
    ) -> Dict[str, Any]:
        """Retrieves detailed information about a single activity record in CATS by activity ID, such as its type, associated candidate or company, and notes. Use this when you need full details for one known activity. To retrieve multiple activities, use cats_list_activities instead.

        Args:
            activitieId: ID of the activity. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def cats_get_candidate(
        self,
        candidateId: str,
    ) -> Dict[str, Any]:
        """Retrieves detailed information about a single candidate in CATS by candidate ID, including contact information, status, and associated records. Use this when you need full details for one known candidate. To browse multiple candidates, use cats_list_candidates instead.

        Args:
            candidateId: ID of the candidate. This parameter is used to identify the candidate in the CATS system. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def cats_get_company_list(
        self,
        listId: str,
    ) -> Dict[str, Any]:
        """Retrieves details of a single company list from CATS by its list ID, including its name and associated companies. Use this when you need to inspect or verify one specific company list. To retrieve all company lists, use cats_list_company_lists instead.

        Args:
            listId: ID of the list. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def cats_list_activities(
        self,
    ) -> Dict[str, Any]:
        """Returns a list of all activity records in CATS, such as calls, emails, and meetings logged against candidates or companies. Use this to enumerate or review recruiting activities across the system. To retrieve details for a single activity, use cats_get_activity instead.
        Returns:
            API response as a dictionary.
        """
        ...

    def cats_list_candidates(
        self,
    ) -> Dict[str, Any]:
        """Returns a paginated list of all candidate records in CATS. Use this to enumerate or search across candidates in the system. To retrieve full details for a single known candidate, use cats_get_candidate instead.
        Returns:
            API response as a dictionary.
        """
        ...

    def cats_list_company_lists(
        self,
    ) -> Dict[str, Any]:
        """Returns a collection of all company lists defined in CATS. Use this to browse or enumerate available company groupings. To retrieve details of a single specific list, use cats_get_company_list instead.
        Returns:
            API response as a dictionary.
        """
        ...

    def cats_update_activity(
        self,
        activitieId: str,
        date: str,
        notes: str,
        regarding_id: int,
        type: str,
    ) -> Dict[str, Any]:
        """Updates the details of an existing activity record in CATS by activity ID. Use this to correct or modify an activitys attributes such as type, notes, or associated entities. Do not use this to create a new activity.

        Args:
            activitieId: ID of the activity. (required)
            date: Date related to the activity. (required)
            notes: Notes or description of the activity. (required)
            regarding_id: ID of the object this activity relates to. (required)
            type: Type of activity. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def cats_update_candidate(
        self,
        candidateId: str,
        emails: _CatsUpdateCandidateEmails,
        first_name: str,
        last_name: str,
        custom_fields: Optional[List[Any]] = None,
        phones: Optional[_CatsUpdateCandidatePhones] = None,
        title: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Updates one or more fields on an existing candidate record in CATS by candidate ID. Use this to modify contact details, status, or other candidate attributes. Do not use this to create a new candidate — use cats_create_candidate instead.

        Args:
            candidateId: ID of the candidate. (required)
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

