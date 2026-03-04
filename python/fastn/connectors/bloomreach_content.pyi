"""Fastn Bloomreach Content connector — auto-generated type stubs.

Do not edit manually. Regenerate with `fastn connector sync`.
"""
from __future__ import annotations

from typing import Any, Dict, List, Optional, TypedDict


class _BloomreachEngagementTrackEventCustomerIds(TypedDict, total=False):
    email: str

class _BloomreachEngagementTrackEventProperties(TypedDict, total=False):
    price: float
    product_id: str
    product_name: str

class BloomreachContentConnector:
    """Bloomreach Content connector ().

    Provides 12 tools.
    """

    def bloomreach_content_create_page(
        self,
        channelId: str,
        pagePath: str,
        projectId: str,
        container: Optional[Dict[str, Any]] = None,
        contentType: Optional[str] = None,
        displayName: Optional[str] = None,
        fields: Optional[Dict[str, Any]] = None,
        layout: Optional[str] = None,
        pageName: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Creates a new page at the specified path within a Bloomreach Content channel and project. Use this tool when you need to add a brand-new page to a channel. If a page already exists at the given path, this call will overwrite it (idempotent PUT). Do not use this tool to update an existing pages content — use bloomreach_content_update_page instead. This action persists changes to the project and may affect live content depending on publish state.

        Args:
            channelId:  (required)
            pagePath:  (required)
            projectId:  (required)
            container: 
            contentType: 
            displayName: 
            fields: 
            layout: 
            pageName: 
        Returns:
            API response as a dictionary.
        """
        ...

    def bloomreach_content_create_project(
        self,
        name: str,
        description: Optional[str] = None,
        includeContentTypes: Optional[bool] = None,
    ) -> Dict[str, Any]:
        """Creates a new Bloomreach Content project. Use this tool when you need to provision a fresh project to organize channels, pages, and documents. Do not use this tool to update an existing project — use the appropriate update tool instead. This action persists a new project in the Bloomreach environment.

        Args:
            name: Name of the content. (required)
            description: Description of the content.
            includeContentTypes: Flag indicating whether to include content types in the response.
        Returns:
            API response as a dictionary.
        """
        ...

    def bloomreach_content_delete_document(
        self,
        documentPath: str,
        projectId: str,
    ) -> Dict[str, Any]:
        """Permanently deletes a content document from a Bloomreach Content project using its document path. Use this tool only when you intend to irreversibly remove the document. This action is destructive and cannot be undone. Do not use this tool to delete pages or projects — use bloomreach_content_delete_page or bloomreach_content_delete_project instead.

        Args:
            documentPath:  (required)
            projectId:  (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def bloomreach_content_delete_page(
        self,
        channelId: str,
        pagePath: str,
        projectId: str,
    ) -> Dict[str, Any]:
        """Permanently deletes a page at the specified path from a Bloomreach Content channel and project. Use this tool only when you intend to irreversibly remove the page. This action is destructive and cannot be undone, and may immediately affect live content depending on publish state. Do not use this tool to delete documents or projects — use bloomreach_content_delete_document or bloomreach_content_delete_project instead.

        Args:
            channelId:  (required)
            pagePath:  (required)
            projectId:  (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def bloomreach_content_delete_project(
        self,
        projectId: str,
    ) -> Dict[str, Any]:
        """Permanently deletes a Bloomreach Content project identified by its project ID. Use this tool only when you intend to irreversibly remove the project and all its associated content, channels, pages, and documents. This action is destructive and cannot be undone. Do not use this tool to delete individual pages or documents — use bloomreach_content_delete_page or bloomreach_content_delete_document instead.

        Args:
            projectId:  (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def bloomreach_content_get_document(
        self,
        documentPath: str,
        projectId: str,
    ) -> Dict[str, Any]:
        """Retrieves a single content document from a Bloomreach Content project using its document path. Use this tool when you need to read the content, fields, or metadata of a specific document. Does not modify any data. Do not use this tool to list multiple documents or to retrieve pages — use the appropriate list or get page tools instead.

        Args:
            documentPath:  (required)
            projectId:  (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def bloomreach_content_get_page(
        self,
        Environment_name: str,
        Preview_Token: str,
        channel_id: str,
        page: str,
    ) -> Dict[str, Any]:
        """Retrieves the details of a specific page from a Bloomreach Content channel using its page path. Use this tool when you need to read or inspect the current content, metadata, or structure of a single page in a given channel. Supports an optional preview token to fetch unpublished draft content. Does not modify any data.

        Args:
            Environment_name:  (required)
            Preview_Token:  (required)
            channel_id:  (required)
            page:  (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def bloomreach_content_get_project(
        self,
        projectId: str,
    ) -> Dict[str, Any]:
        """Retrieves the details of a single Bloomreach Content project by its unique project ID. Use this tool when you need to inspect the configuration, metadata, or status of a specific project. Does not modify any data. Do not use this tool to list all projects — use bloomreach_content_list_projects instead.

        Args:
            projectId:  (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def bloomreach_content_list_projects(
        self,
    ) -> Dict[str, Any]:
        """Returns a list of all Bloomreach Content projects available in the environment. Use this tool when you need to enumerate projects, for example to find a project ID before performing further operations. Does not modify any data. Do not use this tool to retrieve details of a single project — use bloomreach_content_get_project instead.
        Returns:
            API response as a dictionary.
        """
        ...

    def bloomreach_content_update_page(
        self,
        channelId: str,
        pagePath: str,
        projectId: str,
        containers: Optional[str] = None,
        contentType: Optional[str] = None,
        displayName: Optional[str] = None,
        documentFields: Optional[Dict[str, Any]] = None,
        layout: Optional[str] = None,
        pageName: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Updates the content or configuration of an existing page at the specified path within a Bloomreach Content channel and project. Use this tool when you need to modify a page that already exists. If the page does not exist at the given path, a new one may be created (idempotent PUT). Do not use this tool to delete a page — use bloomreach_content_delete_page instead. This action persists changes and may affect live content depending on publish state.

        Args:
            channelId:  (required)
            pagePath:  (required)
            projectId:  (required)
            containers: 
            contentType: 
            displayName: 
            documentFields: 
            layout: 
            pageName: 
        Returns:
            API response as a dictionary.
        """
        ...

    def bloomreach_content_upsert_document(
        self,
        contentType: str,
        displayName: str,
        documentPath: str,
        fields: List[Any],
        name: str,
        path: str,
        projectId: str,
    ) -> Dict[str, Any]:
        """Creates or fully replaces a content document at the specified path within a Bloomreach Content project (upsert via HTTP PUT). Use this tool when you need to publish new document content or overwrite existing document content entirely. If the document does not exist it will be created; if it does exist it will be replaced. Do not use this tool for partial updates or to delete documents — use the appropriate delete tool instead. This action persists changes and may affect live content depending on publish state.

        Args:
            contentType: The content type of the document. (required)
            displayName: The display name of the document. (required)
            documentPath:  (required)
            fields:  (required)
            name: The name of the document. (required)
            path: The path of the document within the Bloomreach Content project. (required)
            projectId:  (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def bloomreach_engagement_track_event(
        self,
        customer_ids: _BloomreachEngagementTrackEventCustomerIds,
        event_type: str,
        properties: _BloomreachEngagementTrackEventProperties,
        timestamp: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Tracks a new customer event in Bloomreach Engagement by sending event data to the platform. Use this to record customer actions or interactions (e.g., purchases, page views, clicks) associated with a specific customer profile. This writes data to the platform and cannot be automatically undone. Do not use this to retrieve event history; use bloomreach_engagement_export_events instead.

        Args:
            customer_ids: Identifiers for the customer associated with the event (required)
            event_type: Type of event (e.g., purchase, page view) (required)
            properties: Additional properties related to the event (required)
            timestamp: Timestamp of the event
        Returns:
            API response as a dictionary.
        """
        ...

