"""Fastn Contentful connector — auto-generated type stubs.

Do not edit manually. Regenerate with `fastn connector sync`.
"""
from __future__ import annotations

from typing import Any, Dict, List, Optional


class ContentfulConnector:
    """Contentful connector ().

    Provides 23 tools.
    """

    def create_asset(
        self,
        fields: Optional[Dict[str, Any]] = None,
        metadata: Optional[Dict[str, Any]] = None,
    ) -> Dict[str, Any]:
        """Creates a new asset in the specified content management system.

        Args:
            fields: Content fields for the entry.
            metadata: Metadata associated with the content.
        Returns:
            API response as a dictionary.
        """
        ...

    def create_content_type(
        self,
        fields: Optional[List[Any]] = None,
        name: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Creates a new content type in the specified content management system.

        Args:
            fields: 
            name: Name of the content entry.
        Returns:
            API response as a dictionary.
        """
        ...

    def create_entry(
        self,
        contentful_content_type: str,
    ) -> Dict[str, Any]:
        """Creates a new entry in the specified content management system.

        Args:
            contentful_content_type: Content type for the Contentful API request. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def delete_asset(
        self,
        xContentfulVersion: str,
    ) -> Dict[str, Any]:
        """Deletes an asset from the specified content management system.

        Args:
            xContentfulVersion: Contentful version for the API request. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def delete_entry(
        self,
        entryId: str,
        environmentId: str,
        spaceId: str,
    ) -> Dict[str, Any]:
        """Deletes an entry in the specified content management system.

        Args:
            entryId: ID of the Contentful entry. (required)
            environmentId: ID of the Contentful environment. (required)
            spaceId: ID of the Contentful space. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def generate_token(
        self,
        client_id: str,
        client_secret: str,
        code: str,
        redirect_uri: str,
    ) -> Dict[str, Any]:
        """Generates a new access token for authentication in the specified content management system.

        Args:
            client_id: Client ID for Contentful API authentication. (required)
            client_secret: Client secret for Contentful API authentication. (required)
            code: Authorization code for Contentful API. (required)
            redirect_uri: Redirect URI for Contentful API authentication. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def get_asset(
        self,
        assetId: Optional[str] = None,
        environmentId: Optional[str] = None,
        spaceId: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Retrieves a specific asset from the specified content management system.

        Args:
            assetId: 
            environmentId: 
            spaceId: 
        Returns:
            API response as a dictionary.
        """
        ...

    def get_assets(
        self,
        environmentId: str,
        spaceId: str,
    ) -> Dict[str, Any]:
        """Retrieves assets from the specified content management system.

        Args:
            environmentId: ID of the Contentful environment. (required)
            spaceId: ID of the Contentful space. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def get_content_type(
        self,
        contentTypeId: Optional[str] = None,
        environmentId: Optional[str] = None,
        spaceId: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Retrieves a specific content type from the specified content management system.

        Args:
            contentTypeId: 
            environmentId: 
            spaceId: 
        Returns:
            API response as a dictionary.
        """
        ...

    def get_content_types(
        self,
        environmentId: str,
        spaceId: str,
    ) -> Dict[str, Any]:
        """Retrieves available content types from the specified content management system.

        Args:
            environmentId: ID of the Contentful environment. (required)
            spaceId: ID of the Contentful space. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def get_delivery_api_keys(
        self,
        spaceId: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Retrieves delivery API keys for accessing the specified content management system.

        Args:
            spaceId: 
        Returns:
            API response as a dictionary.
        """
        ...

    def get_entries(
        self,
    ) -> Dict[str, Any]:
        """Retrieves entries from the specified content management system.
        Returns:
            API response as a dictionary.
        """
        ...

    def get_entry(
        self,
        entryId: str,
        environmentId: str,
        spaceId: str,
    ) -> Dict[str, Any]:
        """Retrieves a specific entry from the specified content management system.

        Args:
            entryId: The ID of the Contentful entry. (required)
            environmentId: The ID of the Contentful environment. (required)
            spaceId:  (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def get_environments(
        self,
        limit: Optional[str] = None,
        skip: Optional[str] = None,
        total: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Retrieves available environments in the specified content management system.

        Args:
            limit: 
            skip: 
            total: 
        Returns:
            API response as a dictionary.
        """
        ...

    def get_spaces(
        self,
        limit: Optional[str] = None,
        skip: Optional[str] = None,
        total: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Retrieves available spaces in the specified content management system.

        Args:
            limit: 
            skip: 
            total: 
        Returns:
            API response as a dictionary.
        """
        ...

    def process_asset(
        self,
        XContentfulVersion: str,
    ) -> Dict[str, Any]:
        """Processes an asset within the specified content management system.

        Args:
            XContentfulVersion: Contentful version header for optimistic locking. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def publish_asset(
        self,
        XContentfulVersion: str,
    ) -> Dict[str, Any]:
        """Publishes an asset in the specified content management system.

        Args:
            XContentfulVersion: The Contentful version for the request. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def publish_content_type(
        self,
        x_contentful_version: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Publishes a content type in the specified content management system.

        Args:
            x_contentful_version: 
        Returns:
            API response as a dictionary.
        """
        ...

    def publish_entry(
        self,
        x_contentful_version: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Publishes an entry in the specified content management system.

        Args:
            x_contentful_version: 
        Returns:
            API response as a dictionary.
        """
        ...

    def refresh_token(
        self,
        client_id: str,
        client_secret: str,
        redirect_uri: str,
        refresh_token: str,
    ) -> Dict[str, Any]:
        """Refreshes an existing access token in the specified content management system.

        Args:
            client_id: Client ID for Contentful API authentication. (required)
            client_secret: Client secret for Contentful API authentication. (required)
            redirect_uri: Redirect URI for Contentful API authentication. (required)
            refresh_token: Refresh token for Contentful API authentication. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def update_asset(
        self,
        xContentfulVersion: str,
    ) -> Dict[str, Any]:
        """Updates an existing asset in the specified content management system.

        Args:
            xContentfulVersion: Contentful version header. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def update_content_type(
        self,
        fields: Optional[List[Any]] = None,
        name: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Updates an existing content type in the specified content management system.

        Args:
            fields: 
            name: Name of the content entry.
        Returns:
            API response as a dictionary.
        """
        ...

    def update_entry(
        self,
        contentful_content_type: str,
    ) -> Dict[str, Any]:
        """Updates an existing entry in the specified content management system.

        Args:
            contentful_content_type: Content type for the Contentful request. (required)
        Returns:
            API response as a dictionary.
        """
        ...

