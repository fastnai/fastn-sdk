"""Fastn Manatal connector — auto-generated type stubs.

Do not edit manually. Regenerate with `fastn connector sync`.
"""
from __future__ import annotations

from typing import Any, Dict, List, Optional


class ManatalConnector:
    """Manatal connector ().

    Provides 16 tools.
    """

    def create_job(
        self,
        address: Optional[str] = None,
        contract_details: Optional[str] = None,
        currency: Optional[int] = None,
        description: Optional[str] = None,
        external_id: Optional[str] = None,
        headcount: Optional[int] = None,
        is_pinned_in_career_page: Optional[bool] = None,
        is_published: Optional[bool] = None,
        is_remote: Optional[bool] = None,
        organization: Optional[int] = None,
        owner: Optional[int] = None,
        position_name: Optional[str] = None,
        salary_max: Optional[str] = None,
        salary_min: Optional[str] = None,
        status: Optional[str] = None,
        zipcode: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Creates a new job opening in the recruiting connector.

        Args:
            address: 
            contract_details: 
            currency: 
            description: 
            external_id: 
            headcount: 
            is_pinned_in_career_page: 
            is_published: 
            is_remote: 
            organization: 
            owner: 
            position_name: 
            salary_max: 
            salary_min: 
            status: 
            zipcode: 
        Returns:
            API response as a dictionary.
        """
        ...

    def delete_job(
        self,
        jobId: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Deletes a specified job opening from the recruiting connector.

        Args:
            jobId: 
        Returns:
            API response as a dictionary.
        """
        ...

    def get_candidate(
        self,
        candidateId: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Fetches detailed information about a specific candidate in the recruiting connector.

        Args:
            candidateId: 
        Returns:
            API response as a dictionary.
        """
        ...

    def get_candidate_attachments(
        self,
        candidate_pk: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Retrieves all attachments associated with a specific candidate in the recruiting connector.

        Args:
            candidate_pk: 
        Returns:
            API response as a dictionary.
        """
        ...

    def get_candidates(
        self,
        created_at__gte: Optional[str] = None,
        created_at__lte: Optional[str] = None,
        email: Optional[str] = None,
        external_id: Optional[str] = None,
        page: Optional[str] = None,
        page_size: Optional[str] = None,
        updated_at__gte: Optional[str] = None,
        updated_at__lte: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Fetches a list of candidates from the recruiting connector.

        Args:
            created_at__gte: 
            created_at__lte: 
            email: 
            external_id: 
            page: 
            page_size: 
            updated_at__gte: 
            updated_at__lte: 
        Returns:
            API response as a dictionary.
        """
        ...

    def get_job(
        self,
        jobId: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Fetches detailed information about a specific job from the recruiting connector.

        Args:
            jobId: 
        Returns:
            API response as a dictionary.
        """
        ...

    def get_job_activities(
        self,
        jobId: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Retrieves all activities related to a specific job in the recruiting connector.

        Args:
            jobId: 
        Returns:
            API response as a dictionary.
        """
        ...

    def get_job_activity(
        self,
        activityId: Optional[str] = None,
        jobId: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Fetches details about a specific job activity in the recruiting connector.

        Args:
            activityId: 
            jobId: 
        Returns:
            API response as a dictionary.
        """
        ...

    def get_job_attachment(
        self,
        attachmentId: Optional[str] = None,
        jobId: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Fetches information about a specific job attachment in the recruiting connector.

        Args:
            attachmentId: 
            jobId: 
        Returns:
            API response as a dictionary.
        """
        ...

    def get_job_attachments(
        self,
        jobId: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Retrieves all attachments associated with a specific job in the recruiting connector.

        Args:
            jobId: 
        Returns:
            API response as a dictionary.
        """
        ...

    def get_job_match(
        self,
        jobId: Optional[str] = None,
        matchId: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Fetches details about a specific job match in the recruiting connector.

        Args:
            jobId: 
            matchId: 
        Returns:
            API response as a dictionary.
        """
        ...

    def get_job_matches(
        self,
        page: Optional[str] = None,
        page_size: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Retrieves a list of candidates matched to a specific job in the recruiting connector.

        Args:
            page: 
            page_size: 
        Returns:
            API response as a dictionary.
        """
        ...

    def get_job_note(
        self,
        jobId: Optional[str] = None,
        noteId: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Fetches details about a specific job note in the recruiting connector.

        Args:
            jobId: 
            noteId: 
        Returns:
            API response as a dictionary.
        """
        ...

    def get_job_notes(
        self,
        jobId: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Retrieves all notes associated with a specific job in the recruiting connector.

        Args:
            jobId: 
        Returns:
            API response as a dictionary.
        """
        ...

    def get_jobs(
        self,
        address: Optional[str] = None,
        contract_details: Optional[str] = None,
        created_at__gte: Optional[str] = None,
        created_at__lte: Optional[str] = None,
        creator_id: Optional[str] = None,
        external_id: Optional[str] = None,
        headcount: Optional[str] = None,
        id: Optional[str] = None,
        is_published: Optional[str] = None,
        is_remote: Optional[str] = None,
        organization_id: Optional[str] = None,
        owner_id: Optional[str] = None,
        page: Optional[str] = None,
        page_size: Optional[str] = None,
        position_name: Optional[str] = None,
        status: Optional[str] = None,
        updated_at__gte: Optional[str] = None,
        updated_at__lte: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Obtains a list of job openings from the recruiting connector.

        Args:
            address: 
            contract_details: 
            created_at__gte: 
            created_at__lte: 
            creator_id: 
            external_id: 
            headcount: 
            id: 
            is_published: 
            is_remote: 
            organization_id: 
            owner_id: 
            page: 
            page_size: 
            position_name: 
            status: 
            updated_at__gte: 
            updated_at__lte: 
        Returns:
            API response as a dictionary.
        """
        ...

    def update_job(
        self,
        address: Optional[str] = None,
        contract_details: Optional[str] = None,
        currency: Optional[int] = None,
        description: Optional[str] = None,
        external_id: Optional[str] = None,
        headcount: Optional[int] = None,
        is_pinned_in_career_page: Optional[bool] = None,
        is_published: Optional[bool] = None,
        is_remote: Optional[bool] = None,
        owner: Optional[int] = None,
        position_name: Optional[str] = None,
        salary_max: Optional[str] = None,
        salary_min: Optional[str] = None,
        status: Optional[str] = None,
        zipcode: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Updates an existing job opening in the recruiting connector.

        Args:
            address: 
            contract_details: 
            currency: 
            description: 
            external_id: 
            headcount: 
            is_pinned_in_career_page: 
            is_published: 
            is_remote: 
            owner: 
            position_name: 
            salary_max: 
            salary_min: 
            status: 
            zipcode: 
        Returns:
            API response as a dictionary.
        """
        ...

