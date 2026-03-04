"""Fastn Linkedin connector — auto-generated type stubs.

Do not edit manually. Regenerate with `fastn connector sync`.
"""
from __future__ import annotations

from typing import Any, Dict, List, Optional, TypedDict


class _LinkedinCreateCommentMessage(TypedDict, total=False):
    text: str

class _LinkedinCreatePostSpecificcontent(TypedDict, total=False):
    com_linkedin_ugc_ShareContent: Dict[str, Any]

class _LinkedinCreatePostVisibility(TypedDict, total=False):
    com_linkedin_ugc_MemberNetworkVisibility: str

class LinkedinConnector:
    """Linkedin connector ().

    Provides 16 tools.
    """

    def linkedin_close_job(
        self,
        jobId: str,
        jobPostingState: str,
    ) -> Dict[str, Any]:
        """Closes an existing job listing on LinkedIn by updating its status via a PATCH request. Use this when you need to mark a job posting as closed or inactive. This action modifies the job record and is not easily reversible — the job will no longer be visible to applicants once closed. Do not use this to delete a job or to update other job fields.

        Args:
            jobId: The unique identifier of the job posting to be closed. (required)
            jobPostingState: The state of the job posting, indicating it will be closed. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def linkedin_create_basic_job(
        self,
        elements: List[Any],
    ) -> Dict[str, Any]:
        """Creates a new standard on-site job listing on LinkedIn. Use this when posting a job that does not have remote or hybrid work arrangements. This action creates a new record on LinkedIn and the posting will be publicly visible to job seekers. Do not use this for remote jobs (use linkedin_create_remote_job) or hybrid roles (use linkedin_create_hybrid_job).

        Args:
            elements: List of job posting elements to create. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def linkedin_create_comment(
        self,
        actor: str,
        message: _LinkedinCreateCommentMessage,
        postId: str,
    ) -> Dict[str, Any]:
        """Creates a new comment on a specific LinkedIn UGC post identified by its post ID. Use this when you need to programmatically add a comment to a post on behalf of a user or organization. This action writes a new comment record and is visible to other LinkedIn users. Do not use this to create a new post — use linkedin_create_post instead.

        Args:
            actor: URN of the actor (user or organization) creating the comment. (required)
            message: Content of the comment message. (required)
            postId: Identifier of the LinkedIn post to comment on. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def linkedin_create_hybrid_job(
        self,
        elements: List[Any],
    ) -> Dict[str, Any]:
        """Creates a new hybrid job listing on LinkedIn that combines remote and on-site work arrangements. Use this when posting a job that allows both remote and in-office work. This action creates a new record on LinkedIn and the posting will be publicly visible to job seekers. Do not use this for fully remote jobs (use linkedin_create_remote_job) or standard on-site jobs (use linkedin_create_basic_job).

        Args:
            elements: List of hybrid job postings to create. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def linkedin_create_post(
        self,
        author: str,
        lifecycleState: str,
        specificContent: _LinkedinCreatePostSpecificcontent,
        visibility: _LinkedinCreatePostVisibility,
    ) -> Dict[str, Any]:
        """Creates a new UGC post on LinkedIn. Use this when you need to publish content to LinkedIn on behalf of a user or organization. This action writes a new post record that will be visible to LinkedIn users. Do not use this to add a comment to an existing post — use linkedin_create_comment instead.

        Args:
            author: Identifier of the post author. (required)
            lifecycleState: The lifecycle state of the post. (required)
            specificContent: Specific content details for the post. (required)
            visibility: Visibility settings for the post. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def linkedin_create_remote_job(
        self,
        elements: List[Any],
    ) -> Dict[str, Any]:
        """Creates a new fully remote job listing on LinkedIn. Use this when posting a job that requires no physical office presence. This action creates a new record on LinkedIn and the posting will be publicly visible to job seekers. Do not use this for hybrid roles (use linkedin_create_hybrid_job) or standard on-site jobs (use linkedin_create_basic_job).

        Args:
            elements: A list of job elements describing each remote job posting. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def linkedin_delete_post(
        self,
        postUrn: str,
    ) -> Dict[str, Any]:
        """Permanently deletes an existing LinkedIn post identified by its post URN. Use this when a post needs to be removed from LinkedIn. This action is irreversible — the post and its associated comments cannot be recovered after deletion. Do not use this to close a job posting — use linkedin_close_job instead.

        Args:
            postUrn: The URN of the LinkedIn post. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def linkedin_get_job(
        self,
        jobId: str,
    ) -> Dict[str, Any]:
        """Retrieves detailed information about a single LinkedIn job listing identified by its job ID. Use this when you need the full details of one specific job, such as its title, description, location, or status. Do not use this to retrieve multiple jobs — use linkedin_list_org_jobs instead.

        Args:
            jobId: The unique identifier of the job to retrieve details for. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def linkedin_get_organization(
        self,
        orgId: str,
    ) -> Dict[str, Any]:
        """Retrieves detailed information about a specific LinkedIn organization identified by its organization ID. Use this when you need data such as the organizations name, description, logo, or industry. Do not use this to search for organizations by keyword — use linkedin_search_company_by_keyword instead.

        Args:
            orgId: The unique identifier of the LinkedIn organization to retrieve. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def linkedin_get_person(
        self,
        id: str,
    ) -> Dict[str, Any]:
        """Retrieves detailed profile information about a specific LinkedIn member identified by their person ID. Use this when you need professional data for a known individual, such as their name, headline, or work history. Do not use this to retrieve the currently authenticated users own profile — use linkedin_get_user_info instead.

        Args:
            id: The unique identifier of the LinkedIn member to retrieve. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def linkedin_get_user_info(
        self,
    ) -> Dict[str, Any]:
        """Retrieves profile information for the currently authenticated LinkedIn user, including their name, email, profile picture, and professional data. Use this when you need details about the logged-in user. Do not use this to retrieve information about another specific person — use linkedin_get_person instead.
        Returns:
            API response as a dictionary.
        """
        ...

    def linkedin_list_comments(
        self,
        urn: str,
        count: Optional[str] = None,
        start: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Lists all comments associated with a specific LinkedIn post or social action identified by its URN. Use this when you need to retrieve all comments on a given post. Returns a collection of comment records. Do not use this to create a comment — use linkedin_create_comment instead.

        Args:
            urn: Uniform Resource Name (URN) for the requested resource in the Linkedin Linkedin API. (required)
            count: The number of results to return in the Linkedin Linkedin API response.
            start: The starting index for pagination in the Linkedin Linkedin API response.
        Returns:
            API response as a dictionary.
        """
        ...

    def linkedin_list_org_jobs(
        self,
        company: str,
    ) -> Dict[str, Any]:
        """Lists all job listings associated with a specific LinkedIn organization. Use this when you need to retrieve all active or posted jobs for a given organization. Returns a collection of job records. Do not use this to retrieve details about a single job — use linkedin_get_job instead.

        Args:
            company: The unique identifier or name of the company to get job listings from. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def linkedin_list_org_posts(
        self,
        q: str,
        authors: Optional[str] = None,
        count: Optional[str] = None,
        start: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Lists all UGC posts associated with a specific LinkedIn organization. Use this when you need to retrieve all posts published by an organization. Returns a collection of post records. Do not use this to retrieve a single post or to list posts for an individual user.

        Args:
            q: The search query parameter specifying the type of query for organization posts. (required)
            authors: Filter posts by the specified authors.
            count: The number of organization posts to retrieve.
            start: The starting index from which to retrieve posts (for pagination).
        Returns:
            API response as a dictionary.
        """
        ...

    def linkedin_search_company(
        self,
        query: str,
        filtercompanySize: Optional[str] = None,
        filterfollowersSize: Optional[str] = None,
        filterfortune: Optional[str] = None,
        filterindustry: Optional[str] = None,
        filterindustryV2: Optional[str] = None,
        filternetworkDegree: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Searches for LinkedIn company profiles using query parameters. Use this when you need to look up companies without a specific keyword filter. Returns a list of matching company records. Do not use this when you already have a company ID — use linkedin_get_organization instead. Use linkedin_search_company_by_keyword when a keyword is available.

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

    def linkedin_search_company_by_keyword(
        self,
        query: str,
    ) -> Dict[str, Any]:
        """Searches for LinkedIn company profiles using a specific keyword. Use this when you need to find companies whose names or descriptions match a search term. Returns a list of matching company records. Do not use this when you already have a company ID — use linkedin_get_organization instead. Prefer this over linkedin_search_company when a keyword filter is needed.

        Args:
            query: The keyword string used to search for companies. (required)
        Returns:
            API response as a dictionary.
        """
        ...

