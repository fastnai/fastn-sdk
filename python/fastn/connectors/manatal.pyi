"""Fastn Manatal connector — auto-generated type stubs.

Do not edit manually. Regenerate with `fastn connector sync`.
"""
from __future__ import annotations

from typing import Any, Dict, List, Optional, TypedDict


class ManatalConnector:
    """Manatal connector ().

    Provides 16 tools.
    """

    def manatal_create_job(
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
        """Creates a new job opening in Manatal. Use this when starting recruitment for a new position. Provide job details such as title, department, description, and requirements. Use manatal_update_job to modify an existing job instead. This action creates a persistent record in the recruitment pipeline.

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

    def manatal_delete_job(
        self,
        jobId: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Permanently deletes a job opening from Manatal by job ID. Use this to remove positions that are no longer relevant, have been filled, or were created in error. WARNING: This action is irreversible — the job record, along with its associated pipeline data, cannot be recovered after deletion. Do not use this to temporarily hide a job; use manatal_update_job to change its status instead.

        Args:
            jobId: 
        Returns:
            API response as a dictionary.
        """
        ...

    def manatal_get_candidate(
        self,
        candidateId: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Retrieves detailed profile information for a single candidate in Manatal by candidate ID. Use this when you need full details (contact info, skills, experience, status) for one specific candidate. Use manatal_list_candidates instead when you need to browse or search multiple candidates. Does not modify any data.

        Args:
            candidateId: 
        Returns:
            API response as a dictionary.
        """
        ...

    def manatal_get_job(
        self,
        jobId: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Retrieves full details of a single job opening in Manatal by job ID, including title, department, status, description, and requirements. Use this when you need complete information for one known job. Use manatal_list_jobs to browse or search multiple jobs when you do not have a specific job ID. Does not modify any data.

        Args:
            jobId: 
        Returns:
            API response as a dictionary.
        """
        ...

    def manatal_get_job_activity(
        self,
        activityId: Optional[str] = None,
        jobId: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Retrieves the details of a single activity record associated with a specific job in Manatal, identified by both job ID and activity ID. Use this to inspect a known activity event such as a status change, interview scheduled, or note added. Use manatal_list_job_activities to browse all activities for a job. Does not modify any data.

        Args:
            activityId: 
            jobId: 
        Returns:
            API response as a dictionary.
        """
        ...

    def manatal_get_job_attachment(
        self,
        attachmentId: Optional[str] = None,
        jobId: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Retrieves the details of a single attachment associated with a specific job in Manatal, identified by both job ID and attachment ID. Use this to access a known document (e.g., job description PDF, intake form) linked to a job posting. Use manatal_list_job_attachments to browse all attachments for a job. Does not modify any data.

        Args:
            attachmentId: 
            jobId: 
        Returns:
            API response as a dictionary.
        """
        ...

    def manatal_get_job_match(
        self,
        jobId: Optional[str] = None,
        matchId: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Retrieves the details of a single candidate-to-job match record in Manatal, identified by both job ID and match ID. Use this to inspect the match score, status, or metadata for one specific match. Use manatal_list_job_matches to browse all matches for a job. Does not modify any data.

        Args:
            jobId: 
            matchId: 
        Returns:
            API response as a dictionary.
        """
        ...

    def manatal_get_job_note(
        self,
        jobId: Optional[str] = None,
        noteId: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Retrieves the full details of a single note attached to a specific job in Manatal, identified by both job ID and note ID. Use this when you need the complete content of one known note. Use manatal_list_job_notes to browse all notes for a job when you do not have a specific note ID. Does not modify any data.

        Args:
            jobId: 
            noteId: 
        Returns:
            API response as a dictionary.
        """
        ...

    def manatal_list_candidate_attachments(
        self,
        candidate_pk: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Returns all attachments associated with a specific candidate in Manatal, identified by candidate ID. Use this to discover documents linked to a candidate profile, such as resumes, cover letters, or certifications. Does not modify any data.

        Args:
            candidate_pk: 
        Returns:
            API response as a dictionary.
        """
        ...

    def manatal_list_candidates(
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
        """Returns a list of candidates in Manatal. Use this to browse the candidate pool, search for candidates by name or status, or retrieve candidate IDs for use with other candidate-specific tools. Use manatal_get_candidate when you already have a specific candidate ID and need full profile details. Does not modify any data.

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

    def manatal_list_job_activities(
        self,
        jobId: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Returns all activity records associated with a specific job in Manatal, identified by job ID. Use this to review the full audit trail or event history for a job opening, such as status changes, interviews, and notes. Use manatal_get_job_activity when you need details for a single known activity. Does not modify any data.

        Args:
            jobId: 
        Returns:
            API response as a dictionary.
        """
        ...

    def manatal_list_job_attachments(
        self,
        jobId: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Returns all attachments associated with a specific job in Manatal, identified by job ID. Use this to discover documents linked to a job posting, such as job descriptions, scorecards, or intake forms. Use manatal_get_job_attachment when you already have a specific attachment ID. Does not modify any data.

        Args:
            jobId: 
        Returns:
            API response as a dictionary.
        """
        ...

    def manatal_list_job_matches(
        self,
        jobId: Optional[str] = None,
        page: Optional[str] = None,
        page_size: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Returns a list of all candidate matches associated with a specific job in Manatal, identified by job ID. Use this to review which candidates have been matched or recommended for a job opening. Use manatal_get_job_match when you need full details for a single known match. Does not modify any data.

        Args:
            jobId: 
            page: 
            page_size: 
        Returns:
            API response as a dictionary.
        """
        ...

    def manatal_list_job_notes(
        self,
        jobId: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Returns all notes associated with a specific job in Manatal, identified by job ID. Use this to review the full annotation history or comments for a job opening. Use manatal_get_job_note when you already have a specific note ID and need its full details. Does not modify any data.

        Args:
            jobId: 
        Returns:
            API response as a dictionary.
        """
        ...

    def manatal_list_jobs(
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
        """Returns a list of all job openings in Manatal. Use this to browse available positions, filter by status or department, or identify job IDs for use with other job-specific tools. Use manatal_get_job when you already have a specific job ID and need full details. Does not modify any data.

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

    def manatal_update_job(
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
        jobId: Optional[str] = None,
        owner: Optional[int] = None,
        position_name: Optional[str] = None,
        salary_max: Optional[str] = None,
        salary_min: Optional[str] = None,
        status: Optional[str] = None,
        zipcode: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Updates one or more fields of an existing job opening in Manatal by job ID. Use this to modify job details such as title, description, status, requirements, or hiring team. Only fields provided in the request body will be changed (partial update). Use manatal_create_job to create a new job instead. This action overwrites existing field values.

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
            jobId: 
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

