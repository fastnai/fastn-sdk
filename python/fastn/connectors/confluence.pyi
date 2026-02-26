"""Fastn Confluence connector — auto-generated type stubs.

Do not edit manually. Regenerate with `fastn connector sync`.
"""
from __future__ import annotations

from typing import Any, Dict, List, Optional


class ConfluenceConnector:
    """Confluence connector ().

    Provides 12 tools.
    """

    def create_blog_post(
        self,
        private: Optional[bool] = None,
    ) -> Dict[str, Any]:
        """Creates a new blog post in the blogging platform.

        Args:
            private: Specifies whether the blog post should be private (true) or public (false).
        Returns:
            API response as a dictionary.
        """
        ...

    def create_page(
        self,
        embedded: Optional[bool] = None,
        private: Optional[bool] = None,
        rootlevel: Optional[bool] = None,
    ) -> Dict[str, Any]:
        """Creates a new page in the content management system.

        Args:
            embedded: Whether the page is embedded.
            private: Whether the page is private.
            rootlevel: Whether the page is at the root level.
        Returns:
            API response as a dictionary.
        """
        ...

    def delete_blog_post(
        self,
        draft: Optional[bool] = None,
        purge: Optional[bool] = None,
    ) -> Dict[str, Any]:
        """Deletes a specified blog post from the blogging platform.

        Args:
            draft: If true, deletes the blog post even if it is a draft.
            purge: If true, permanently deletes the blog post (may not be reversible).
        Returns:
            API response as a dictionary.
        """
        ...

    def delete_page(
        self,
        draft: Optional[bool] = None,
        purge: Optional[bool] = None,
    ) -> Dict[str, Any]:
        """Deletes a specified page from the content management system.

        Args:
            draft: If true, deletes the draft version of the page as well.
            purge: If true, completely purges the page, bypassing the recycle bin.
        Returns:
            API response as a dictionary.
        """
        ...

    def get_blog_post(
        self,
        bodyformat: Optional[str] = None,
        getdraft: Optional[str] = None,
        includecollaborators: Optional[str] = None,
        includefavoritedbycurrentuserstatus: Optional[str] = None,
        includelabels: Optional[str] = None,
        includelikes: Optional[str] = None,
        includeoperations: Optional[str] = None,
        includeproperties: Optional[str] = None,
        includeversion: Optional[str] = None,
        includeversions: Optional[str] = None,
        includewebresources: Optional[str] = None,
        status: Optional[str] = None,
        version: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Retrieves an existing blog post from the blogging platform based on its ID.

        Args:
            bodyformat: The format of the blog post body (e.g., "html", "storage").
            getdraft: Whether to retrieve a draft version of the blog post.
            includecollaborators: Whether to include collaborators information.
            includefavoritedbycurrentuserstatus: Whether to include the favorited status by the current user.
            includelabels: Whether to include labels associated with the blog post.
            includelikes: Whether to include like information.
            includeoperations: Whether to include operation information.
            includeproperties: Whether to include custom properties associated with the blog post.
            includeversion: Whether to include specific version information.
            includeversions: Whether to include all versions of the blog post.
            includewebresources: Whether to include associated web resources.
            status: The status of the blog post (e.g., "current", "draft").
            version: The specific version of the blog post to retrieve.
        Returns:
            API response as a dictionary.
        """
        ...

    def get_blog_posts(
        self,
        bodyformat: Optional[str] = None,
        cursor: Optional[str] = None,
        id: Optional[str] = None,
        limit: Optional[str] = None,
        sort: Optional[str] = None,
        spaceid: Optional[str] = None,
        status: Optional[str] = None,
        title: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Retrieves a list of all blog posts from the blogging platform.

        Args:
            bodyformat: The format of the blog post body (e.g., 'storage', 'view').
            cursor: A cursor for pagination.
            id: The ID of a specific blog post.
            limit: The maximum number of blog posts to return.
            sort: The order to sort blog posts (e.g., 'created asc', 'created desc').
            spaceid: The ID of the space containing the blog posts.
            status: The status of the blog posts (e.g., 'current', 'draft').
            title: The title of the blog post.
        Returns:
            API response as a dictionary.
        """
        ...

    def get_page(
        self,
        bodyformat: Optional[str] = None,
        getdraft: Optional[bool] = None,
        includecollaborators: Optional[bool] = None,
        includedirectchildren: Optional[bool] = None,
        includefavoritedbycurrentuserstatus: Optional[bool] = None,
        includelabels: Optional[bool] = None,
        includelikes: Optional[bool] = None,
        includeoperations: Optional[bool] = None,
        includeproperties: Optional[bool] = None,
        includeversion: Optional[bool] = None,
        includeversions: Optional[bool] = None,
        includewebresources: Optional[bool] = None,
        status: Optional[str] = None,
        version: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Retrieves a specific page from the content management system based on its ID.

        Args:
            bodyformat: Format of the page body (e.g., 'storage', 'view').
            getdraft: Whether to retrieve the draft version of the page (true/false).
            includecollaborators: Whether to include collaborator information (true/false).
            includedirectchildren: Whether to include direct child pages (true/false).
            includefavoritedbycurrentuserstatus: Whether to include favorited status for the current user (true/false).
            includelabels: Whether to include page labels (true/false).
            includelikes: Whether to include like information (true/false).
            includeoperations: Whether to include operation information (true/false).
            includeproperties: Whether to include page properties (true/false).
            includeversion: Whether to include specific version information (true/false).
            includeversions: Whether to include all versions information (true/false).
            includewebresources: Whether to include web resource information (true/false).
            status: Filter pages by status.
            version: Specific version number to retrieve.
        Returns:
            API response as a dictionary.
        """
        ...

    def get_pages(
        self,
        bodyformat: Optional[str] = None,
        cursor: Optional[str] = None,
        id: Optional[str] = None,
        limit: Optional[str] = None,
        sort: Optional[str] = None,
        spaceid: Optional[str] = None,
        status: Optional[str] = None,
        subtype: Optional[str] = None,
        title: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Retrieves a list of all pages in the content management system.

        Args:
            bodyformat: The format of the page body (e.g., storage, view).
            cursor: Cursor for pagination.
            id: The ID of a specific page to retrieve.
            limit: The maximum number of pages to return.
            sort: The sorting order for the results (e.g., created, updated).
            spaceid: The ID of the space to retrieve pages from.
            status: Filter pages by status (e.g., current, draft).
            subtype: Filter pages by subtype (e.g., page, blogpost).
            title: Filter pages by title.
        Returns:
            API response as a dictionary.
        """
        ...

    def get_space(
        self,
        descriptionformat: Optional[str] = None,
        includeicon: Optional[bool] = None,
        includelabels: Optional[bool] = None,
        includeoperations: Optional[bool] = None,
        includepermissions: Optional[bool] = None,
        includeproperties: Optional[bool] = None,
        includeroleassignments: Optional[bool] = None,
    ) -> Dict[str, Any]:
        """Retrieves a specific space from the content management system based on its ID.

        Args:
            descriptionformat: The format of the space description (e.g., 'plain', 'storage').
            includeicon: Whether to include the space icon in the response.
            includelabels: Whether to include space labels in the response.
            includeoperations: Whether to include space operations in the response.
            includepermissions: Whether to include space permissions in the response.
            includeproperties: Whether to include space properties in the response.
            includeroleassignments: Whether to include space role assignments in the response.
        Returns:
            API response as a dictionary.
        """
        ...

    def get_spaces(
        self,
        cursor: Optional[str] = None,
        descriptionformat: Optional[str] = None,
        favoritedby: Optional[str] = None,
        ids: Optional[str] = None,
        includeicon: Optional[bool] = None,
        keys: Optional[str] = None,
        labels: Optional[str] = None,
        limit: Optional[str] = None,
        notfavoritedby: Optional[str] = None,
        sort: Optional[str] = None,
        status: Optional[str] = None,
        type: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Retrieves a list of all spaces in the content management system.

        Args:
            cursor: Cursor for pagination.
            descriptionformat: Format of the space description (e.g., plain text, HTML).
            favoritedby: Filter spaces favorited by a specific user.
            ids: Comma-separated list of space IDs.
            includeicon: Whether to include space icons in the results.
            keys: Comma-separated list of space keys.
            labels: Filter spaces by labels.
            limit: Maximum number of spaces to return.
            notfavoritedby: Filter spaces not favorited by a specific user.
            sort: Sort order (e.g., name asc, name desc).
            status: Filter spaces by status (e.g., current, archived).
            type: Filter spaces by type (e.g., personal, global).
        Returns:
            API response as a dictionary.
        """
        ...

    def update_blog_post(
        self,
        id: str,
        status: str,
        title: str,
        body: Optional[Dict[str, Any]] = None,
        createdAt: Optional[str] = None,
        spaceId: Optional[str] = None,
        version: Optional[Dict[str, Any]] = None,
    ) -> Dict[str, Any]:
        """Updates the content or metadata of an existing blog post in the blogging platform.

        Args:
            id: The unique identifier for the blog post. (required)
            status: The status of the blog post (e.g., 'current', 'draft'). (required)
            title: The title of the blog post. (required)
            body: The content of the blog post.
            createdAt: Timestamp indicating when the blog post was created.
            spaceId: The ID of the space where the blog post resides.
            version: Version information for the blog post.
        Returns:
            API response as a dictionary.
        """
        ...

    def update_page(
        self,
        id: str,
        status: str,
        title: str,
        body: Optional[Dict[str, Any]] = None,
        version: Optional[Dict[str, Any]] = None,
    ) -> Dict[str, Any]:
        """Updates the content or metadata of an existing page in the content management system.

        Args:
            id: The ID of the Confluence page. (required)
            status: The status of the Confluence page (e.g., 'current', 'draft'). (required)
            title: The title of the Confluence page. (required)
            body: The content of the Confluence page.
            version: Version information for the page.
        Returns:
            API response as a dictionary.
        """
        ...

