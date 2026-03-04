"""Fastn Figma connector — auto-generated type stubs.

Do not edit manually. Regenerate with `fastn connector sync`.
"""
from __future__ import annotations

from typing import Any, Dict, List, Optional, TypedDict


class _FigmaPostCommentOnFileClientMeta(TypedDict, total=False):
    x: int
    y: int

class FigmaConnector:
    """Figma connector ().

    Provides 14 tools.
    """

    def figma_delete_comment(
        self,
        commentId: str,
        fileId: str,
    ) -> Dict[str, Any]:
        """Permanently deletes a specific comment from a Figma file, identified by file ID and comment ID. This action is irreversible — the comment cannot be recovered after deletion. Use this tool to remove outdated or incorrect feedback from a design file. Do not use this tool to delete all comments on a file at once; each comment must be deleted individually.

        Args:
            commentId: The ID of the comment to be accessed. (required)
            fileId: The ID of the Figma file containing the comment. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def figma_get_file(
        self,
        fileId: str,
        branch_data: Optional[str] = None,
        depth: Optional[str] = None,
        geometry: Optional[str] = None,
        ids: Optional[str] = None,
        plugin_data: Optional[str] = None,
        version: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Returns the full document structure of a specific Figma file, identified by file ID, including all pages, frames, layers, components, and styles. Use this tool when you need complete access to a files design content. For large files, consider using figma_get_file_nodes to retrieve only specific elements. Do not use this tool for metadata only; use figma_get_file_metadata for that purpose.

        Args:
            fileId: The ID of the Figma file. (required)
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

    def figma_get_file_metadata(
        self,
        fileId: str,
    ) -> Dict[str, Any]:
        """Returns metadata for a specific Figma file, identified by file ID, including its name, last modified timestamp, thumbnail URL, and version information. Use this tool when you need file-level metadata without downloading the full document structure. Do not use this tool to retrieve the full file content or node-level data; use figma_get_file or figma_get_file_nodes for those purposes.

        Args:
            fileId: The ID of the Figma file. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def figma_get_file_nodes(
        self,
        fileId: str,
        ids: str,
        depth: Optional[str] = None,
        geometry: Optional[str] = None,
        plugin_data: Optional[str] = None,
        version: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Returns specific nodes from a Figma file, identified by file ID and one or more node IDs. A node represents any design element such as a frame, group, component, or text layer. Use this tool when you need the design data for specific elements within a file without fetching the entire file. Do not use this tool to retrieve all file content; use figma_get_file for that purpose.

        Args:
            fileId: The ID of the Figma file to access. (required)
            ids: Specifies the IDs of the objects to be retrieved. (required)
            depth: Specifies the depth of the response data.
            geometry: Specifies the geometry to be included in the response.
            plugin_data: Specifies any plugin-specific data to be included.
            version: Specifies the version of the API to use.
        Returns:
            API response as a dictionary.
        """
        ...

    def figma_get_image(
        self,
        imageId: str,
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
        """Returns a rendered image (PNG, JPG, SVG, or PDF) of a specific node or frame within a Figma file, identified by file ID and node ID. Use this tool to export a visual representation of a design element for display or asset generation. Do not use this tool to retrieve raw file structure or metadata; use figma_get_file or figma_get_file_metadata for those purposes.

        Args:
            imageId: The ID of the image to export. (required)
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

    def figma_get_me(
        self,
    ) -> Dict[str, Any]:
        """Returns profile information for the currently authenticated Figma user, including their user ID, name, email address, and profile image URL. Use this tool to verify the authenticated identity or obtain the current users ID for permission checks. Do not use this tool to retrieve information about other users or teams.
        Returns:
            API response as a dictionary.
        """
        ...

    def figma_list_file_comments(
        self,
        fileId: str,
        as_md: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Returns all comments posted on a specific Figma file, identified by file ID, including comment text, author, timestamp, and position on the canvas. Use this tool to review feedback or extract discussion history from a design file. Do not use this tool to post a new comment; use figma_post_comment_on_file for that purpose.

        Args:
            fileId: The ID of the Figma file. (required)
            as_md: Parameter to specify markdown format.
        Returns:
            API response as a dictionary.
        """
        ...

    def figma_list_file_versions(
        self,
        fileId: str,
    ) -> Dict[str, Any]:
        """Returns the full version history of a specific Figma file, identified by file ID. Each entry includes a version ID, timestamp, and description of the change. Use this tool to audit edits, compare versions, or identify a specific historical state of a file. Do not use this tool to retrieve the current file content; use figma_get_file for that purpose.

        Args:
            fileId: The unique identifier of the Figma file. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def figma_list_project_files(
        self,
        projectId: str,
    ) -> Dict[str, Any]:
        """Returns a list of all Figma files within a specific project, identified by project ID. Use this tool to enumerate files in a project and obtain file IDs for further operations such as retrieving file content or comments. Do not use this tool to retrieve the content of a specific file; use figma_get_file for that purpose.

        Args:
            projectId: The ID of the Figma project. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def figma_list_team_component_sets(
        self,
        teamId: str,
        after: Optional[str] = None,
        before: Optional[str] = None,
        page_size: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Returns a list of all published component sets belonging to a specific Figma team, identified by team ID. Component sets group related variants of a component together. Use this tool to discover available component sets in a teams design system. Do not use this tool to retrieve individual components; use figma_list_team_components for that purpose.

        Args:
            teamId: The ID of the Figma team. (required)
            after: Cursor to start pagination from.
            before: Cursor to end pagination at.
            page_size: Number of results per page.
        Returns:
            API response as a dictionary.
        """
        ...

    def figma_list_team_components(
        self,
        teamId: str,
        after: Optional[str] = None,
        before: Optional[str] = None,
        page_size: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Returns a list of all published components belonging to a specific Figma team, identified by team ID. Use this tool to enumerate reusable design components available across a teams projects. Do not use this tool to retrieve component sets or styles; use figma_list_team_component_sets or figma_list_team_styles for those purposes.

        Args:
            teamId: The ID of the Figma team. (required)
            after: Cursor to fetch results after a specific item.
            before: Cursor to fetch results before a specific item.
            page_size: Number of results per page.
        Returns:
            API response as a dictionary.
        """
        ...

    def figma_list_team_projects(
        self,
        teamId: str,
    ) -> Dict[str, Any]:
        """Returns a list of all projects belonging to a specific Figma team, identified by team ID. Use this tool to enumerate projects and obtain project IDs needed to retrieve files within those projects. Do not use this tool to retrieve files directly; use figma_list_project_files for that purpose.

        Args:
            teamId: The ID of the Figma team. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def figma_list_team_styles(
        self,
        teamId: str,
        after: Optional[str] = None,
        before: Optional[str] = None,
        page_size: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Returns a list of all published styles (color, text, effect, and grid styles) belonging to a specific Figma team, identified by team ID. Use this tool to audit or reference the design system styles available to a team. Do not use this tool to retrieve component sets or project files.

        Args:
            teamId: The ID of the Figma team. (required)
            after: Cursor to start pagination from.
            before: Cursor to end pagination at.
            page_size: Number of results per page.
        Returns:
            API response as a dictionary.
        """
        ...

    def figma_post_comment_on_file(
        self,
        client_meta: _FigmaPostCommentOnFileClientMeta,
        fileId: str,
        message: str,
    ) -> Dict[str, Any]:
        """Posts a new comment on a specific Figma file, identified by its file ID. Use this tool to leave feedback, annotations, or review notes directly on a Figma design file. This action creates a new comment record visible to all collaborators with access to the file. Do not use this tool to reply to an existing comment thread or to retrieve existing comments.

        Args:
            client_meta: Metadata about the client making the request. (required)
            fileId: The unique identifier of the Figma file. (required)
            message: A message associated with the request. (required)
        Returns:
            API response as a dictionary.
        """
        ...

