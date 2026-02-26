"""Fastn Bloomreach Content connector — auto-generated type stubs.

Do not edit manually. Regenerate with `fastn connector sync`.
"""
from __future__ import annotations

from typing import Any, Dict, List, Optional


class BloomreachContentConnector:
    """Bloomreach Content connector ().

    Provides 12 tools.
    """

    def add_event(
        self,
        customer_ids: Dict[str, Any],
        event_type: str,
        properties: Dict[str, Any],
        timestamp: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Adds a new event to the calendar or system using the addEvent tool.

        Args:
            customer_ids: Identifiers for the customer associated with the event (required)
            event_type: Type of event (e.g., purchase, page view) (required)
            properties: Additional properties related to the event (required)
            timestamp: Timestamp of the event
        Returns:
            API response as a dictionary.
        """
        ...

    def create_page(
        self,
        container: Optional[Dict[str, Any]] = None,
        contentType: Optional[str] = None,
        displayName: Optional[str] = None,
        fields: Optional[Dict[str, Any]] = None,
        layout: Optional[str] = None,
        pageName: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Creates a new page within the system using the createPage tool.

        Args:
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

    def create_project(
        self,
        name: str,
        description: Optional[str] = None,
        includeContentTypes: Optional[bool] = None,
    ) -> Dict[str, Any]:
        """Creates a new project within the system using the createProject tool.

        Args:
            name: Name of the content. (required)
            description: Description of the content.
            includeContentTypes: Flag indicating whether to include content types in the response.
        Returns:
            API response as a dictionary.
        """
        ...

    def delete_document(
        self,
        documentPath: str,
        projectId: str,
    ) -> Dict[str, Any]:
        """Removes a document from the system with the deleteDocument tool.

        Args:
            documentPath:  (required)
            projectId:  (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def delete_page(
        self,
        channelId: str,
        pagePath: str,
        projectId: str,
    ) -> Dict[str, Any]:
        """Deletes a page using the deletePage tool.

        Args:
            channelId:  (required)
            pagePath:  (required)
            projectId:  (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def delete_project(
        self,
        projectId: str,
    ) -> Dict[str, Any]:
        """Deletes a specified project using the deleteProject tool.

        Args:
            projectId:  (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def get_all_projects(
        self,
    ) -> Dict[str, Any]:
        """Retrieves a list of all projects using the getAllProjects tool.
        Returns:
            API response as a dictionary.
        """
        ...

    def get_document(
        self,
        documentPath: str,
        projectId: str,
    ) -> Dict[str, Any]:
        """Retrieves a single document using the getDocument tool.

        Args:
            documentPath:  (required)
            projectId:  (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def get_page(
        self,
    ) -> Dict[str, Any]:
        """Fetches a specific page's details using the getPage tool.
        Returns:
            API response as a dictionary.
        """
        ...

    def get_project_by_id(
        self,
        projectId: str,
    ) -> Dict[str, Any]:
        """Fetches details of a specific project by its ID using the getProjectById tool.

        Args:
            projectId:  (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def put_document(
        self,
        contentType: str,
        displayName: str,
        fields: List[Any],
        name: str,
        path: str,
    ) -> Dict[str, Any]:
        """Uploads or updates a document using the putDocument tool.

        Args:
            contentType: The content type of the document. (required)
            displayName: The display name of the document. (required)
            fields:  (required)
            name: The name of the document. (required)
            path: The path of the document within the Bloomreach Content project. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def update_page(
        self,
        containers: Optional[str] = None,
        contentType: Optional[str] = None,
        displayName: Optional[str] = None,
        documentFields: Optional[Dict[str, Any]] = None,
        layout: Optional[str] = None,
        pageName: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Updates an existing page with new content using the updatePage tool.

        Args:
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

