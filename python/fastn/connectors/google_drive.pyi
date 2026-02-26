"""Fastn Google Drive connector — auto-generated type stubs.

Do not edit manually. Regenerate with `fastn connector sync`.
"""
from __future__ import annotations

from typing import Any, Dict, List, Optional


class GoogleDriveConnector:
    """Google Drive connector ().

    Provides 16 tools.
    """

    def create_folder(
        self,
        name: str,
    ) -> Dict[str, Any]:
        """Creates a new folder within the connector's file structure.

        Args:
            name: Name of the file to be created in Google Drive. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def create_webhook(
        self,
        pageToken: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Creates a new webhook in the connector to receive updates.

        Args:
            pageToken: Token to specify the page of results to retrieve.
        Returns:
            API response as a dictionary.
        """
        ...

    def delete_file(
        self,
        fileId: str,
    ) -> Dict[str, Any]:
        """Deletes a specified file from the connector.

        Args:
            fileId: ID of the file in Google Drive. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def delete_webhook(
        self,
        id: str,
        resourceId: str,
    ) -> Dict[str, Any]:
        """Deletes an existing webhook from the connector.

        Args:
            id: The unique identifier of the webhook subscription to delete. (required)
            resourceId: The identifier of the resource associated with the webhook. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def download_file(
        self,
        fileId: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Downloads a specified file from the connector to your local system.

        Args:
            fileId: 
        Returns:
            API response as a dictionary.
        """
        ...

    def export_file(
        self,
        mimeType: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Exports a specified file from the connector to a designated format.

        Args:
            mimeType: MIME type of the file for My connectors.
        Returns:
            API response as a dictionary.
        """
        ...

    def get_changes(
        self,
        startPageToken: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Retrieves changes made to files in the connector since the last check.

        Args:
            startPageToken: Token indicating the starting page for retrieving results.
        Returns:
            API response as a dictionary.
        """
        ...

    def get_file(
        self,
        fields: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Fetches detailed information about a specific file from the connector.

        Args:
            fields: 
        Returns:
            API response as a dictionary.
        """
        ...

    def get_files(
        self,
    ) -> Dict[str, Any]:
        """Retrieves a list of files from the specified connector.
        Returns:
            API response as a dictionary.
        """
        ...

    def get_files_from_folder(
        self,
        fields: Optional[str] = None,
        q: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Retrieves a list of files located within a specific folder in the connector.

        Args:
            fields: A comma-separated list of the fields to include in the response for each file.
            q: A query string for filtering files in Google Drive based on the Drive API query language.
        Returns:
            API response as a dictionary.
        """
        ...

    def list_changes(
        self,
        pageToken: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Lists the changes made to files in the connector's file system.

        Args:
            pageToken: Page token for pagination of results from the Google Drive API.
        Returns:
            API response as a dictionary.
        """
        ...

    def list_file_permissions(
        self,
        fileId: str,
    ) -> Dict[str, Any]:
        """Lists the permissions associated with a specific file in the connector.

        Args:
            fileId: ID of the Google Drive file. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def move_and_rename_file(
        self,
        fileId: str,
        fileName: str,
        filePath: str,
    ) -> Dict[str, Any]:
        """Moves and renames a file within the connector's file system.

        Args:
            fileId:  (required)
            fileName:  (required)
            filePath:  (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def move_file(
        self,
        addParents: str,
        removeParents: str,
    ) -> Dict[str, Any]:
        """Moves a file from one location to another within the connector.

        Args:
            addParents: Source folder ID (required)
            removeParents: Destination folder ID (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def update_file(
        self,
        name: str,
    ) -> Dict[str, Any]:
        """Updates the content of an existing file in the connector.

        Args:
            name: Name of the file to be created or updated in Google Drive. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def upload_file(
        self,
        contentType: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Uploads a file from your local system to the connector.

        Args:
            contentType: 
        Returns:
            API response as a dictionary.
        """
        ...

