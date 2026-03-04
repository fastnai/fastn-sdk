"""Fastn Contentful connector — auto-generated type stubs.

Do not edit manually. Regenerate with `fastn connector sync`.
"""
from __future__ import annotations

from typing import Any, Dict, List, Optional, TypedDict


class _ContentfulCreateAssetFields(TypedDict, total=False):
    file: Dict[str, Any]
    title: Dict[str, Any]

class _ContentfulCreateAssetMetadata(TypedDict, total=False):
    tags: List[Any]

class _ContentfulCreateEntryFields(TypedDict, total=False):
    name: Dict[str, Any]

class _ContentfulCreateEntryMetadata(TypedDict, total=False):
    tags: List[Any]

class _ContentfulUpdateAssetFields(TypedDict, total=False):
    file: Dict[str, Any]
    title: Dict[str, Any]

class _ContentfulUpdateAssetMetadata(TypedDict, total=False):
    tags: List[Any]

class _ContentfulUpdateEntryFields(TypedDict, total=False):
    name: Dict[str, Any]

class _ContentfulUpdateEntryMetadata(TypedDict, total=False):
    tags: List[Any]

class ContentfulConnector:
    """Contentful connector ().

    Provides 25 tools.
    """

    def contentful_create_asset(
        self,
        environmentId: str,
        spaceId: str,
        fields: Optional[_ContentfulCreateAssetFields] = None,
        metadata: Optional[_ContentfulCreateAssetMetadata] = None,
    ) -> Dict[str, Any]:
        """Creates a new asset record in a specified Contentful space and environment. Use this to register a new asset with its metadata and file references before processing and publishing it. Do not use this to update an existing asset — use contentful_update_asset instead. After creation, the asset must be processed and published before it is publicly available. This operation creates a new persistent record in Contentful.

        Args:
            environmentId: Environment ID for the Contentful environment. (required)
            spaceId: Space ID for the Contentful space. (required)
            fields: Content fields for the entry.
            metadata: Metadata associated with the content.
        Returns:
            API response as a dictionary.
        """
        ...

    def contentful_create_content_type(
        self,
        environmentId: str,
        spaceId: str,
        fields: Optional[List[Any]] = None,
        name: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Creates a new content type with a defined field schema in a specified Contentful space and environment. Use this when you need to define a new structured content model for entries. Do not use this to update an existing content type — use contentful_update_content_type instead. After creation, the content type must be published via contentful_publish_content_type before it can be used for entries. This operation creates a new persistent content model record.

        Args:
            environmentId: ID of the Contentful environment. (required)
            spaceId: ID of the Contentful space. (required)
            fields: 
            name: Name of the content entry.
        Returns:
            API response as a dictionary.
        """
        ...

    def contentful_create_entry(
        self,
        contentful_content_type: str,
        environmentId: str,
        spaceId: str,
        fields: Optional[_ContentfulCreateEntryFields] = None,
        metadata: Optional[_ContentfulCreateEntryMetadata] = None,
    ) -> Dict[str, Any]:
        """Creates a new entry of a specified content type in a Contentful space and environment. Use this when you need to add a new content record with field values. Do not use this to update an existing entry — use contentful_update_entry instead. After creation, the entry must be published via contentful_publish_entry before it is publicly available. This operation creates a new persistent record in Contentful.

        Args:
            contentful_content_type: Content type for the Contentful API request. (required)
            environmentId: Environment ID for the Contentful API request. (required)
            spaceId: Space ID for the Contentful API request. (required)
            fields: Fields of the Contentful entry.
            metadata: Metadata associated with the Contentful entry.
        Returns:
            API response as a dictionary.
        """
        ...

    def contentful_delete_asset(
        self,
        assetId: str,
        environmentId: str,
        spaceId: str,
        xContentfulVersion: str,
    ) -> Dict[str, Any]:
        """Permanently deletes a Contentful asset by asset ID from a specified space and environment. Use this only when you intend to remove an asset entirely. Do not use this to unpublish an asset — unpublishing is a separate action. This operation is irreversible; the asset file and all its metadata will be permanently lost.

        Args:
            assetId: Asset ID for the Contentful API request. (required)
            environmentId: Environment ID for the Contentful API request. (required)
            spaceId: Space ID for the Contentful API request. (required)
            xContentfulVersion: Contentful version for the API request. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def contentful_delete_entry(
        self,
        entryId: str,
        environmentId: str,
        spaceId: str,
    ) -> Dict[str, Any]:
        """Permanently deletes a Contentful entry by entry ID from a specified space and environment. Use this only when you intend to remove an entry entirely. Do not use this to unpublish an entry — unpublishing is a separate action. This operation is irreversible; the entry and all its field data will be permanently lost.

        Args:
            entryId: ID of the Contentful entry. (required)
            environmentId: ID of the Contentful environment. (required)
            spaceId: ID of the Contentful space. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def contentful_generate_token(
        self,
        client_id: str,
        client_secret: str,
        code: str,
        redirect_uri: str,
    ) -> Dict[str, Any]:
        """Generates a new Contentful OAuth access token using client credentials or an authorization code. Use this for initial authentication when no valid token exists. Do not use this to renew an existing token — use contentful_refresh_token instead. This operation issues a new access token that grants API access based on the provided credentials.

        Args:
            client_id: Client ID for Contentful API authentication. (required)
            client_secret: Client secret for Contentful API authentication. (required)
            code: Authorization code for Contentful API. (required)
            redirect_uri: Redirect URI for Contentful API authentication. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def contentful_get_asset(
        self,
        assetId: Optional[str] = None,
        environmentId: Optional[str] = None,
        spaceId: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Retrieves a single Contentful asset by asset ID from a specified space and environment. Use this when you need the metadata and file details of one specific asset. Do not use this to list multiple assets — use contentful_list_assets instead. This is a read-only operation with no side effects.

        Args:
            assetId: 
            environmentId: 
            spaceId: 
        Returns:
            API response as a dictionary.
        """
        ...

    def contentful_get_content_type(
        self,
        contentTypeId: Optional[str] = None,
        environmentId: Optional[str] = None,
        spaceId: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Retrieves a single Contentful content type by content type ID from a specified space and environment. Use this when you need the field schema and configuration of one specific content type. Do not use this to list all content types — use contentful_list_content_types instead. This is a read-only operation with no side effects.

        Args:
            contentTypeId: 
            environmentId: 
            spaceId: 
        Returns:
            API response as a dictionary.
        """
        ...

    def contentful_get_entry(
        self,
        entryId: str,
        environmentId: str,
        spaceId: str,
    ) -> Dict[str, Any]:
        """Retrieves a single Contentful entry by entry ID from a specified space and environment using the Content Delivery API. Use this when you need the full field data for one specific entry. Do not use this to retrieve multiple entries — use contentful_list_entries instead. This is a read-only operation with no side effects.

        Args:
            entryId: The ID of the Contentful entry. (required)
            environmentId: The ID of the Contentful environment. (required)
            spaceId:  (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def contentful_list_assets(
        self,
        environmentId: str,
        spaceId: str,
    ) -> Dict[str, Any]:
        """Lists all assets in a specified Contentful space and environment. Use this when you need to retrieve multiple assets, optionally filtered by query parameters. Do not use this to fetch a single asset by ID — use contentful_get_asset instead. This is a read-only operation with no side effects.

        Args:
            environmentId: ID of the Contentful environment. (required)
            spaceId: ID of the Contentful space. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def contentful_list_content_types(
        self,
        environmentId: str,
        spaceId: str,
    ) -> Dict[str, Any]:
        """Lists all content types available in a specified Contentful space and environment. Use this when you need to discover available content models and their field schemas. Do not use this to retrieve a single content type by ID — use contentful_get_content_type instead. This is a read-only operation with no side effects.

        Args:
            environmentId: ID of the Contentful environment. (required)
            spaceId: ID of the Contentful space. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def contentful_list_delivery_api_keys(
        self,
        spaceId: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Lists all Content Delivery API keys for a specified Contentful space. Use this when you need to retrieve available API keys for read-only content delivery access. Do not use this to generate new tokens or manage authentication — use contentful_generate_token or contentful_refresh_token for that. This is a read-only operation with no side effects.

        Args:
            spaceId: 
        Returns:
            API response as a dictionary.
        """
        ...

    def contentful_list_entries(
        self,
        environmentId: str,
        spaceId: str,
        params: Optional[List[Any]] = None,
    ) -> Dict[str, Any]:
        """Lists all entries in a specified Contentful space and environment using the Content Management API. Use this when you need to retrieve multiple entries, optionally filtered by content type or other query parameters. Do not use this to fetch a single entry by ID — use contentful_get_entry instead. This is a read-only operation with no side effects.

        Args:
            environmentId: The ID of the Contentful environment. (required)
            spaceId: The ID of the Contentful space. (required)
            params: 
        Returns:
            API response as a dictionary.
        """
        ...

    def contentful_list_environments(
        self,
        limit: Optional[str] = None,
        skip: Optional[str] = None,
        spaceId: Optional[str] = None,
        total: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Lists all environments within a specified Contentful space. Use this when you need to discover available environments and their IDs before performing environment-specific operations. Do not use this to list spaces — use contentful_list_spaces instead. This is a read-only operation with no side effects.

        Args:
            limit: 
            skip: 
            spaceId: 
            total: 
        Returns:
            API response as a dictionary.
        """
        ...

    def contentful_list_spaces(
        self,
        limit: Optional[str] = None,
        skip: Optional[str] = None,
        total: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Lists all Contentful spaces accessible to the authenticated account. Use this when you need to discover available spaces and their IDs before performing space-specific operations. Do not use this to retrieve environments within a space — use contentful_list_environments instead. This is a read-only operation with no side effects.

        Args:
            limit: 
            skip: 
            total: 
        Returns:
            API response as a dictionary.
        """
        ...

    def contentful_process_asset(
        self,
        XContentfulVersion: str,
        assetId: str,
        environmentId: str,
        spaceId: str,
    ) -> Dict[str, Any]:
        """Triggers processing of a Contentful asset file for the en-US locale by asset ID in a specified space and environment. Use this after uploading an asset to initiate Contentfuls file processing pipeline before the asset can be published. Do not use this to process assets for other locales — use the locale-specific process tool instead. This operation is a prerequisite for publishing and may take a moment to complete.

        Args:
            XContentfulVersion: Contentful version header for optimistic locking. (required)
            assetId: ID of the Contentful asset. (required)
            environmentId: ID of the Contentful environment. (required)
            spaceId: ID of the Contentful space. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def contentful_process_asset_locale(
        self,
        assetId: Optional[str] = None,
        environmentId: Optional[str] = None,
        locale_code: Optional[str] = None,
        spaceId: Optional[str] = None,
        xContentfulVersion: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Triggers processing of a Contentful asset file for a specified locale by asset ID in a specified space and environment. Use this after uploading an asset when you need to process a locale other than en-US. Do not use this for the default en-US locale — use contentful_process_asset instead. This operation is a prerequisite for publishing and may take a moment to complete.

        Args:
            assetId: 
            environmentId: 
            locale_code: 
            spaceId: 
            xContentfulVersion: 
        Returns:
            API response as a dictionary.
        """
        ...

    def contentful_publish_asset(
        self,
        XContentfulVersion: str,
        assetId: str,
        environmentId: str,
        spaceId: str,
    ) -> Dict[str, Any]:
        """Publishes a Contentful asset by asset ID, making it publicly available via the Content Delivery API in the specified space and environment. Use this after an asset has been created and processed to make it live. Do not use this before processing the asset — use contentful_process_asset first. Publishing makes the asset visible to end users and cannot be silently undone without an explicit unpublish action.

        Args:
            XContentfulVersion: The Contentful version for the request. (required)
            assetId: The ID of the Contentful asset. (required)
            environmentId: The ID of the Contentful environment. (required)
            spaceId: The ID of the Contentful space. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def contentful_publish_asset_v2(
        self,
        assetId: Optional[str] = None,
        environmentId: Optional[str] = None,
        spaceId: Optional[str] = None,
        xContentfulVersion: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Publishes a Contentful asset by asset ID, making it publicly available via the Content Delivery API in the specified space and environment. This is a duplicate of contentful_publish_asset — verify which instance is intended and consolidate if possible. Publishing makes the asset visible to end users and cannot be silently undone without an explicit unpublish action.

        Args:
            assetId: 
            environmentId: 
            spaceId: 
            xContentfulVersion: 
        Returns:
            API response as a dictionary.
        """
        ...

    def contentful_publish_content_type(
        self,
        content_type_id: Optional[str] = None,
        environmentId: Optional[str] = None,
        spaceId: Optional[str] = None,
        x_contentful_version: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Publishes a Contentful content type by content type ID, activating it for use in entries within the specified space and environment. Use this after creating or updating a content type to make it available for entry creation. Do not use this to modify the content type schema — use contentful_update_content_type instead. Publishing a content type affects all future entries of that type and cannot be silently undone without an explicit unpublish action.

        Args:
            content_type_id: 
            environmentId: 
            spaceId: 
            x_contentful_version: 
        Returns:
            API response as a dictionary.
        """
        ...

    def contentful_publish_entry(
        self,
        entryId: Optional[str] = None,
        environmentId: Optional[str] = None,
        spaceId: Optional[str] = None,
        x_contentful_version: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Publishes a Contentful entry by entry ID, making it publicly available via the Content Delivery API in the specified space and environment. Use this after an entry has been created or updated to make it live. Do not use this to update entry field values — use contentful_update_entry instead. Publishing makes the entry visible to end users and cannot be silently undone without an explicit unpublish action.

        Args:
            entryId: 
            environmentId: 
            spaceId: 
            x_contentful_version: 
        Returns:
            API response as a dictionary.
        """
        ...

    def contentful_refresh_token(
        self,
        client_id: str,
        client_secret: str,
        redirect_uri: str,
        refresh_token: str,
    ) -> Dict[str, Any]:
        """Exchanges a refresh token for a new Contentful OAuth access token. Use this when an existing access token has expired and needs to be renewed without requiring user re-authentication. Do not use this to generate a brand-new token from scratch — use contentful_generate_token for initial token generation. This operation invalidates the previous token and issues a new one.

        Args:
            client_id: Client ID for Contentful API authentication. (required)
            client_secret: Client secret for Contentful API authentication. (required)
            redirect_uri: Redirect URI for Contentful API authentication. (required)
            refresh_token: Refresh token for Contentful API authentication. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def contentful_update_asset(
        self,
        assetId: str,
        environmentId: str,
        spaceId: str,
        xContentfulVersion: str,
        fields: Optional[_ContentfulUpdateAssetFields] = None,
        metadata: Optional[_ContentfulUpdateAssetMetadata] = None,
    ) -> Dict[str, Any]:
        """Updates the metadata or file references of an existing Contentful asset by asset ID in a specified space and environment. Use this when you need to modify an assets title, description, or file information. Do not use this to publish the asset — publishing requires a separate publish call. This operation overwrites the assets current metadata and cannot be undone without a manual restore.

        Args:
            assetId: Contentful asset ID. (required)
            environmentId: Contentful environment ID. (required)
            spaceId: Contentful space ID. (required)
            xContentfulVersion: Contentful version header. (required)
            fields: Content fields for the Contentful API.
            metadata: Metadata associated with the content.
        Returns:
            API response as a dictionary.
        """
        ...

    def contentful_update_content_type(
        self,
        contentTypeId: str,
        environmentId: str,
        spaceId: str,
        fields: Optional[List[Any]] = None,
        name: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Updates the schema or configuration of an existing Contentful content type by content type ID in a specified space and environment. Use this when you need to modify field definitions, validations, or display settings of a content type. Do not use this to create a new content type — use contentful_create_content_type instead. Changes must be published via contentful_publish_content_type to take effect. This operation can affect all existing entries of that content type.

        Args:
            contentTypeId: The ID of the Contentful content type. (required)
            environmentId: The ID of the Contentful environment. (required)
            spaceId:  (required)
            fields: 
            name: Name of the content entry.
        Returns:
            API response as a dictionary.
        """
        ...

    def contentful_update_entry(
        self,
        contentful_content_type: str,
        entryId: str,
        environmentId: str,
        spaceId: str,
        fields: Optional[_ContentfulUpdateEntryFields] = None,
        metadata: Optional[_ContentfulUpdateEntryMetadata] = None,
    ) -> Dict[str, Any]:
        """Updates the fields of an existing Contentful entry by entry ID within a specified space and environment. Use this when you need to modify the content of an already-created entry. Do not use this to create a new entry or to publish an entry — publishing requires a separate publish call. This operation overwrites the entrys current field values and cannot be undone without a manual restore.

        Args:
            contentful_content_type: Content type for the Contentful request. (required)
            entryId: Contentful Entry ID. (required)
            environmentId: Contentful Environment ID. (required)
            spaceId: The ID of the Contentful space. (required)
            fields: Fields of the Contentful entry.
            metadata: Metadata for the Contentful entry.
        Returns:
            API response as a dictionary.
        """
        ...

