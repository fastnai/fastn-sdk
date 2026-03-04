"""Fastn Google Drive connector — auto-generated type stubs.

Do not edit manually. Regenerate with `fastn connector sync`.
"""
from __future__ import annotations

from typing import Any, Dict, List, Optional, TypedDict


class _GoogleDriveCreateWebhookParams(TypedDict, total=False):
    ttl: str

class GoogleDriveConnector:
    """Google Drive connector ().

    Provides 17 tools.
    """

    def google_drive_create_folder(
        self,
        name: str,
    ) -> Dict[str, Any]:
        """Creates a new empty folder in Google Drive. Use this to set up directory structure before uploading or organizing files. To upload a file, use google_drive_upload_file. This operation creates a new folder resource and may trigger change notifications if webhooks are configured.

        Args:
            name: Name of the file to be created in Google Drive. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def google_drive_create_webhook(
        self,
        address: str,
        id: str,
        type: str,
        pageToken: Optional[str] = None,
        params: Optional[_GoogleDriveCreateWebhookParams] = None,
    ) -> Dict[str, Any]:
        """Creates a new Google Drive push notification channel (webhook) that delivers real-time change notifications to a specified callback URL whenever files are modified. Use this to set up event-driven integrations. Do not use this to poll for changes manually — use google_drive_list_changes instead. Creating a webhook registers an active subscription that will send HTTP requests to your endpoint until stopped.

        Args:
            address: The URL to receive notifications when changes occur. (required)
            id: A UUID or string that identifies this channel. (required)
            type: The type of delivery mechanism used for this channel (e.g., 'web_hook'). (required)
            pageToken: Token to specify the page of results to retrieve.
            params: Extra parameters for the channel configuration.
        Returns:
            API response as a dictionary.
        """
        ...

    def google_drive_delete_file(
        self,
        fileId: str,
    ) -> Dict[str, Any]:
        """Permanently deletes a specified file from Google Drive by its file ID. Use this to remove files that are no longer needed. This action is irreversible — the file cannot be recovered after deletion unless it was previously backed up. Do not use this to move a file to the trash; this is a hard delete. Triggers change notifications if webhooks are active.

        Args:
            fileId: ID of the file in Google Drive. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def google_drive_delete_webhook(
        self,
        id: str,
        resourceId: str,
    ) -> Dict[str, Any]:
        """Stops and deletes an existing Google Drive push notification channel (webhook), preventing further change notifications from being sent to the registered endpoint. Use this when a webhook subscription is no longer needed or must be rotated. This action is irreversible — the stopped channel cannot be restarted and a new webhook must be created if notifications are needed again. Calls the channel stop endpoint via POST.

        Args:
            id: The unique identifier of the webhook subscription to delete. (required)
            resourceId: The identifier of the resource associated with the webhook. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def google_drive_download_file(
        self,
        fileId: str,
        alt: Optional[str] = None,
        range: Optional[str] = None,
        responseContentType: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Downloads the binary content of a specified Google Drive file to the local system using a direct GET request. Use this for standard file downloads by file ID. For Google Workspace native files (Docs, Sheets, Slides) that need format conversion, use google_drive_export_file instead. Read-only operation with no side effects. Note: a separate POST-based download action also exists in this connector for asynchronous downloads.

        Args:
            fileId: ID of the Google Drive file. (required)
            alt: Specifies the format of the response. (e.g., 'media')
            range: 
            responseContentType: 
        Returns:
            API response as a dictionary.
        """
        ...

    def google_drive_download_file_post(
        self,
        fileId: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Downloads the binary content of a specified file from Google Drive using the async download endpoint (POST). Use this for files that require server-side processing before download, such as large files. For standard file downloads, prefer google_drive_download_file. Does not modify the file. Note: there is a duplicate download action in this connector — confirm which endpoint is appropriate for your use case.

        Args:
            fileId: 
        Returns:
            API response as a dictionary.
        """
        ...

    def google_drive_export_file(
        self,
        fileId: Optional[str] = None,
        mimeType: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Exports a Google Workspace file (such as Google Docs, Sheets, or Slides) from Google Drive in a specified MIME type format (e.g., PDF, DOCX, XLSX). Use this when you need to convert a native Google Workspace document into a downloadable format. Do not use this for non-Google files already in binary format — use google_drive_download_file instead. Read-only operation with no side effects.

        Args:
            fileId: ID of the file for My connectors.
            mimeType: MIME type of the file for My connectors.
        Returns:
            API response as a dictionary.
        """
        ...

    def google_drive_get_changes(
        self,
        startPageToken: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Retrieves file changes in Google Drive starting from a specific page token. Use this tool to poll for incremental changes to files and folders since a known checkpoint. Requires a valid startPageToken obtained from a prior changes listing. Do not use this to list all current files — use google_drive_list_files instead. Does not modify any data.

        Args:
            startPageToken: Token indicating the starting page for retrieving results.
        Returns:
            API response as a dictionary.
        """
        ...

    def google_drive_get_file(
        self,
        fileId: str,
        fields: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Retrieves detailed metadata about a specific Google Drive file by its file ID, including name, MIME type, size, parent folders, and modification timestamps. Use this to inspect file properties. To download the actual file content, use google_drive_download_file. Read-only operation with no side effects.

        Args:
            fileId: ID of the file in Google Drive. (required)
            fields: 
        Returns:
            API response as a dictionary.
        """
        ...

    def google_drive_list_changes(
        self,
        pageToken: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Lists all changes made to files and folders in Google Drive since a given point in time, using the changes feed. Use this to audit recent activity or synchronize state across systems. To retrieve changes from a specific token checkpoint, use google_drive_get_changes. Read-only operation with no side effects.

        Args:
            pageToken: Page token for pagination of results from the Google Drive API.
        Returns:
            API response as a dictionary.
        """
        ...

    def google_drive_list_file_permissions(
        self,
        fileId: str,
    ) -> Dict[str, Any]:
        """Lists all sharing permissions associated with a specific Google Drive file, including which users or groups have access and their permission roles (e.g., reader, writer, owner). Use this to audit or review file access controls. Read-only operation with no side effects.

        Args:
            fileId: ID of the Google Drive file. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def google_drive_list_files(
        self,
    ) -> Dict[str, Any]:
        """Lists files stored in Google Drive, optionally filtered by query parameters such as name, MIME type, or parent folder. Use this to browse or search across all accessible files. To list files within a specific folder only, use google_drive_list_files_from_folder. To retrieve metadata for a single known file, use google_drive_get_file. Read-only operation with no side effects.
        Returns:
            API response as a dictionary.
        """
        ...

    def google_drive_list_files_from_folder(
        self,
        fields: Optional[str] = None,
        q: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Lists all files located within a specific Google Drive folder. Use this to enumerate the contents of a known folder by its ID. To list all files across Google Drive without a folder filter, use google_drive_list_files instead. Does not return folder metadata itself, only its child file entries. Read-only operation with no side effects.

        Args:
            fields: A comma-separated list of the fields to include in the response for each file.
            q: A query string for filtering files in Google Drive based on the Drive API query language.
        Returns:
            API response as a dictionary.
        """
        ...

    def google_drive_move_and_rename_file(
        self,
        fileId: str,
        fileName: str,
        filePath: str,
    ) -> Dict[str, Any]:
        """Moves a file to a different folder and renames it in a single operation within Google Drive. Use this when both the location and the name of a file need to change simultaneously. If only a rename or only a move is needed, use google_drive_update_file or google_drive_move_file respectively. This operation modifies the files metadata in place and does not create a copy.

        Args:
            fileId:  (required)
            fileName:  (required)
            filePath:  (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def google_drive_move_file(
        self,
        addParents: str,
        fileId: str,
        removeParents: str,
    ) -> Dict[str, Any]:
        """Moves a file to a different folder in Google Drive by updating its parent reference. Use this when only the files location needs to change. To simultaneously rename and move a file, use google_drive_move_and_rename_file. To rename without moving, use google_drive_update_file. This operation modifies file metadata and may trigger change notifications if webhooks are active.

        Args:
            addParents: Source folder ID (required)
            fileId: ID of the file in Google Drive. (required)
            removeParents: Destination folder ID (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def google_drive_update_file(
        self,
        fileId: str,
        name: str,
    ) -> Dict[str, Any]:
        """Updates the metadata or content of an existing file in Google Drive, such as its name, description, or binary content. Use this to modify a file that already exists. To upload a brand-new file, use google_drive_upload_file. To move a file to a different folder, use google_drive_move_file. This operation modifies the file in place and may trigger change notifications if webhooks are active.

        Args:
            fileId: ID of the file in Google Drive. (required)
            name: Name of the file to be created or updated in Google Drive. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def google_drive_upload_file(
        self,
        body: Optional[str] = None,
        contentType: Optional[str] = None,
        uploadType: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Uploads a new file to Google Drive, storing it in cloud storage. Use this to add files that do not yet exist in Google Drive. To update the content of an existing file, use google_drive_update_file instead. This operation creates a new file resource and may trigger change notifications if webhooks are configured.

        Args:
            body: 
            contentType: 
            uploadType: 
        Returns:
            API response as a dictionary.
        """
        ...

