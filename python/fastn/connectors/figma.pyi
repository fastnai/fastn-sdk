"""Fastn Figma connector — auto-generated type stubs.

Do not edit manually. Regenerate with `fastn connector sync`.
"""
from __future__ import annotations

from typing import Any, Dict, List, Optional


class FigmaConnector:
    """Figma connector ().

    Provides 14 tools.
    """

    def delete_comment(
        self,
        commentId: str,
        fileId: str,
    ) -> Dict[str, Any]:
        """Deletes a comment from a specific file in the document management system.

        Args:
            commentId: The ID of the comment to be accessed. (required)
            fileId: The ID of the Figma file containing the comment. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def get_file(
        self,
        branch_data: Optional[str] = None,
        depth: Optional[str] = None,
        geometry: Optional[str] = None,
        ids: Optional[str] = None,
        plugin_data: Optional[str] = None,
        version: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Retrieves a file from the file storage system based on the provided file ID.

        Args:
            branch_data: Branch data for the request.
            depth: Depth of the request.
            geometry: Geometry data for the request.
            ids: Ids for the request.
            plugin_data: Plugin data for the request.
            version: Version for the request.
        Returns:
            API response as a dictionary.
        """
        ...

    def get_file_comments(
        self,
        as_md: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Fetches all comments associated with a specific file in the document management system.

        Args:
            as_md: Parameter to specify markdown format.
        Returns:
            API response as a dictionary.
        """
        ...

    def get_file_meta_data(
        self,
        fileId: str,
    ) -> Dict[str, Any]:
        """Obtains metadata for a particular file in the file storage system, providing details such as size, type, and creation date.

        Args:
            fileId: The ID of the Figma file. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def get_file_versions(
        self,
        fileId: str,
    ) -> Dict[str, Any]:
        """Fetches all versions of a specific file from the file storage system, allowing you to see edit history.

        Args:
            fileId: The unique identifier of the Figma file. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def get_files_nodes(
        self,
        ids: str,
        depth: Optional[str] = None,
        geometry: Optional[str] = None,
        plugin_data: Optional[str] = None,
        version: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Retrieves all nodes related to files in the workspace of the document management system, useful for understanding the file structure.

        Args:
            ids: Specifies the IDs of the objects to be retrieved. (required)
            depth: Specifies the depth of the response data.
            geometry: Specifies the geometry to be included in the response.
            plugin_data: Specifies any plugin-specific data to be included.
            version: Specifies the version of the API to use.
        Returns:
            API response as a dictionary.
        """
        ...

    def get_image(
        self,
        contents_only: Optional[str] = None,
        format: Optional[str] = None,
        ids: Optional[str] = None,
        scale: Optional[str] = None,
        svg_include_id: Optional[str] = None,
        svg_include_node_id: Optional[str] = None,
        svg_outline_text: Optional[str] = None,
        svg_simplify_stroke: Optional[str] = None,
        use_absolute_bounds: Optional[str] = None,
        version: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Gets an image from the file storage system using the image ID, providing the necessary data for display or further processing.

        Args:
            contents_only: Specifies whether to only return the contents of the image.
            format: Specifies the desired format of the exported image (e.g., PNG, SVG).
            ids: Comma-separated list of node IDs to export.
            scale: Scaling factor for the exported image.
            svg_include_id: Whether to include IDs in the SVG export.
            svg_include_node_id: Whether to include node IDs in the SVG export.
            svg_outline_text: Whether to outline text in the SVG export.
            svg_simplify_stroke: Whether to simplify strokes in the SVG export.
            use_absolute_bounds: Whether to use absolute bounds for the export.
            version: Specifies the version of the file to export.
        Returns:
            API response as a dictionary.
        """
        ...

    def get_me(
        self,
    ) -> Dict[str, Any]:
        """Retrieves current user information from the user management system, including details like username and contact info.
        Returns:
            API response as a dictionary.
        """
        ...

    def get_project_files(
        self,
        projectId: str,
    ) -> Dict[str, Any]:
        """Fetches files associated with a specific project in the project management system.

        Args:
            projectId: The ID of the Figma project. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def get_team_component_sets(
        self,
        after: Optional[str] = None,
        before: Optional[str] = None,
        page_size: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Fetches sets of components that are part of the team’s projects in the collaborative project management system.

        Args:
            after: Cursor to start pagination from.
            before: Cursor to end pagination at.
            page_size: Number of results per page.
        Returns:
            API response as a dictionary.
        """
        ...

    def get_team_components(
        self,
        after: Optional[str] = None,
        before: Optional[str] = None,
        page_size: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Retrieves components used by a team within the collaborative project management system.

        Args:
            after: Cursor to fetch results after a specific item.
            before: Cursor to fetch results before a specific item.
            page_size: Number of results per page.
        Returns:
            API response as a dictionary.
        """
        ...

    def get_team_projects(
        self,
        teamId: str,
    ) -> Dict[str, Any]:
        """Obtains a list of projects that belong to the team in the project management system.

        Args:
            teamId: The ID of the Figma team. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def get_team_styles(
        self,
        after: Optional[str] = None,
        before: Optional[str] = None,
        page_size: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Retrieves style guides and design styles utilized by the team in the collaborative project management system.

        Args:
            after: Cursor to start pagination from.
            before: Cursor to end pagination at.
            page_size: Number of results per page.
        Returns:
            API response as a dictionary.
        """
        ...

    def post_comment_on_file(
        self,
        client_meta: Dict[str, Any],
        message: str,
    ) -> Dict[str, Any]:
        """Posts a comment on a specific file within the document management system, allowing collaboration and feedback.

        Args:
            client_meta: Metadata about the client making the request. (required)
            message: A message associated with the request. (required)
        Returns:
            API response as a dictionary.
        """
        ...

