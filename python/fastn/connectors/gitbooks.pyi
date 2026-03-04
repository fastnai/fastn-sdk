"""Fastn GitBooks connector — auto-generated type stubs.

Do not edit manually. Regenerate with `fastn connector sync`.
"""
from __future__ import annotations

from typing import Any, Dict, List, Optional, TypedDict


class GitbooksConnector:
    """GitBooks connector ().

    Provides 8 tools.
    """

    def gitbooks_get_organization(
        self,
        organizationId: str,
    ) -> Dict[str, Any]:
        """Retrieves details for a specific GitBooks organization by its organization ID, including its name, members, and associated spaces. Use this when you need metadata about a known organization. Use gitbooks_list_organizations to discover all organizations associated with your account. Does not modify any data.

        Args:
            organizationId: The unique identifier for the organization. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def gitbooks_get_page(
        self,
        pageId: str,
        spaceId: str,
        computed: Optional[str] = None,
        evaluated: Optional[str] = None,
        format: Optional[str] = None,
        metadata: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Retrieves metadata and content for a single page within a GitBooks space using its page ID. Use this when you have a specific page ID and need its details. Use gitbooks_get_page_content instead if you only have the pages URL path. Does not modify any data.

        Args:
            pageId: The unique identifier for the GitBook page. (required)
            spaceId: The unique identifier for the GitBook space containing the page. (required)
            computed: A computed value related to the page.
            evaluated: An evaluated value related to the page.
            format: Specifies the desired output format for the page.
            metadata: Metadata associated with the page.
        Returns:
            API response as a dictionary.
        """
        ...

    def gitbooks_get_page_content(
        self,
        pagePath: str,
        spaceId: str,
    ) -> Dict[str, Any]:
        """Retrieves the full text content of a specific page by its path within a GitBooks space. Use this when you need to read or display the body/content of a known page using its URL path. Use gitbooks_get_page instead if you are referencing the page by its page ID rather than its path. Does not modify any data.

        Args:
            pagePath: The path component of the Bilal API endpoint. (required)
            spaceId: The identifier of the Bilal space or workspace. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def gitbooks_get_space(
        self,
        spaceId: str,
        shareKey: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Retrieves metadata and attributes for a single GitBooks space by its space ID, including its title, visibility, and configuration. Use this when you need details about a specific known space. Use gitbooks_list_spaces to discover all spaces under an organization. Does not modify any data.

        Args:
            spaceId: The unique identifier for the GitBook space. (required)
            shareKey: Share key for accessing the space.
        Returns:
            API response as a dictionary.
        """
        ...

    def gitbooks_list_organizations(
        self,
        limit: Optional[str] = None,
        page: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Returns a list of all GitBooks organizations associated with the authenticated account. Use this when you need to discover which organizations are available before fetching spaces or pages. Use gitbooks_get_organization to retrieve details for a single known organization. Does not modify any data.

        Args:
            limit: The maximum number of organizations to return.
            page: The page number of results to retrieve.
        Returns:
            API response as a dictionary.
        """
        ...

    def gitbooks_list_pages(
        self,
        spaceId: str,
        computed: Optional[str] = None,
        metadata: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Returns a list of all pages within a specific GitBooks space. Use this when you need an overview of all documentation pages available in a space. Use gitbooks_get_page to retrieve full details for a single page by ID. Does not modify any data.

        Args:
            spaceId: The unique identifier for the GitBook space. (required)
            computed: Specifies which computed properties to include in the response.
            metadata: Specifies whether to include metadata in the response.
        Returns:
            API response as a dictionary.
        """
        ...

    def gitbooks_list_spaces(
        self,
        organizationId: str,
        limit: Optional[str] = None,
        page: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Returns a list of all spaces belonging to a specific GitBooks organization. Use this when you need to discover or enumerate available documentation spaces within an organization. Use gitbooks_get_space to retrieve full details for a single known space. Does not modify any data.

        Args:
            organizationId: The ID of the organization whose spaces are to be retrieved. (required)
            limit: The maximum number of spaces to return.
            page: The page number to retrieve.
        Returns:
            API response as a dictionary.
        """
        ...

    def gitbooks_search_space(
        self,
        spaceId: str,
        limit: Optional[str] = None,
        page: Optional[str] = None,
        query: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Searches for content within a specific GitBooks space using a query string and returns matching documents or sections. Use this when you need to find relevant pages or content within a known space. Use gitbooks_list_spaces if you first need to discover available spaces. Does not modify any data.

        Args:
            spaceId: The unique identifier of the GitBooks space to search within. (required)
            limit: The maximum number of results to return.
            page: The page number for pagination.
            query: The search query string.
        Returns:
            API response as a dictionary.
        """
        ...

