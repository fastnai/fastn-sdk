"""Fastn Linkedin connector — auto-generated type stubs.

Do not edit manually. Regenerate with `fastn connector sync`.
"""
from __future__ import annotations

from typing import Any, Dict, List, Optional


class LinkedinConnector:
    """Linkedin connector ().

    Provides 16 tools.
    """

    def close_job(
        self,
        jobPostingState: str,
    ) -> Dict[str, Any]:
        """Closes an existing job listing in the job database.

        Args:
            jobPostingState: The state of the job posting, indicating it will be closed. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def create_basic_job(
        self,
        elements: List[Any],
    ) -> Dict[str, Any]:
        """Creates a basic job listing in the job database.

        Args:
            elements: List of job posting elements to create. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def create_comment(
        self,
        actor: str,
        message: Dict[str, Any],
    ) -> Dict[str, Any]:
        """Creates a new comment on a specific post.

        Args:
            actor: URN of the actor (user or organization) creating the comment. (required)
            message: Content of the comment message. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def create_hybrid_job(
        self,
        elements: List[Any],
    ) -> Dict[str, Any]:
        """Creates a hybrid job listing (combining remote and on-site) in the job database.

        Args:
            elements: List of hybrid job postings to create. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def create_post(
        self,
        author: str,
        lifecycleState: str,
        specificContent: Dict[str, Any],
        visibility: Dict[str, Any],
    ) -> Dict[str, Any]:
        """Creates a new post in the platform.

        Args:
            author: Identifier of the post author. (required)
            lifecycleState: The lifecycle state of the post. (required)
            specificContent: Specific content details for the post. (required)
            visibility: Visibility settings for the post. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def create_remote_job(
        self,
        elements: List[Any],
    ) -> Dict[str, Any]:
        """Creates a remote job listing in the job database.

        Args:
            elements: A list of job elements describing each remote job posting. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def delete_post(
        self,
        postUrn: str,
    ) -> Dict[str, Any]:
        """Deletes an existing post from the platform.

        Args:
            postUrn: The URN of the LinkedIn post. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def get_comments(
        self,
        count: Optional[str] = None,
        start: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Fetches comments associated with a specific post.

        Args:
            count: The number of results to return in the Linkedin Linkedin API response.
            start: The starting index for pagination in the Linkedin Linkedin API response.
        Returns:
            API response as a dictionary.
        """
        ...

    def get_job(
        self,
        jobId: str,
    ) -> Dict[str, Any]:
        """Retrieves detailed information about a specific job.

        Args:
            jobId: The unique identifier of the job to retrieve details for. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def get_org_jobs(
        self,
        company: str,
    ) -> Dict[str, Any]:
        """Fetches job listings related to a specific organization.

        Args:
            company: The unique identifier or name of the company to get job listings from. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def get_org_posts(
        self,
        q: str,
        authors: Optional[str] = None,
        count: Optional[str] = None,
        start: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Fetches posts related to a specific organization.

        Args:
            q: The search query parameter specifying the type of query for organization posts. (required)
            authors: Filter posts by the specified authors.
            count: The number of organization posts to retrieve.
            start: The starting index from which to retrieve posts (for pagination).
        Returns:
            API response as a dictionary.
        """
        ...

    def get_organization(
        self,
        orgId: str,
    ) -> Dict[str, Any]:
        """Retrieves detailed information about a specific organization.

        Args:
            orgId: The unique identifier of the LinkedIn organization to retrieve. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def get_person(
        self,
        id: str,
    ) -> Dict[str, Any]:
        """Retrieves detailed information about a specific person.

        Args:
            id: The unique identifier of the LinkedIn member to retrieve. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def get_user_info(
        self,
    ) -> Dict[str, Any]:
        """Retrieves user information from the system.
        Returns:
            API response as a dictionary.
        """
        ...

    def seach_company(
        self,
        query: str,
        filtercompanySize: Optional[str] = None,
        filterfollowersSize: Optional[str] = None,
        filterfortune: Optional[str] = None,
        filterindustry: Optional[str] = None,
        filterindustryV2: Optional[str] = None,
        filternetworkDegree: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Searches for a company in the database.

        Args:
            query: The search term or company name to find relevant companies. (required)
            filtercompanySize: Filter companies based on their size (number of employees).
            filterfollowersSize: Filter companies based on the size of their follower base.
            filterfortune: Filter companies based on their Fortune 500 status.
            filterindustry: Filter companies by industry category.
            filterindustryV2: An alternative or updated industry filter for searching companies.
            filternetworkDegree: Filter companies based on network degree relevance.
        Returns:
            API response as a dictionary.
        """
        ...

    def seach_company_by_keyword(
        self,
        query: str,
    ) -> Dict[str, Any]:
        """Searches for companies using a specific keyword.

        Args:
            query: The keyword string used to search for companies. (required)
        Returns:
            API response as a dictionary.
        """
        ...

