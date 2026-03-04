"""Fastn Microsoft OneDrive connector — auto-generated type stubs.

Do not edit manually. Regenerate with `fastn connector sync`.
"""
from __future__ import annotations

from typing import Any, Dict, List, Optional, TypedDict


class _MicrosoftOneDriveMoveFileParentreference(TypedDict, total=False):
    id: str

class MicrosoftOnedriveConnector:
    """Microsoft OneDrive connector ().

    Provides 20 tools.
    """

    def microsoft_one_drive_create_folder(
        self,
        _microsoft_graph_conflictBehavior: Optional[str] = None,
        folder: Optional[Dict[str, Any]] = None,
        name: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Creates a new folder at the root level of the authenticated users Microsoft OneDrive. Use this when you need to organize files by creating a new directory. Do not use this to create nested subfolders inside an existing folder or to upload files (use microsoft_one_drive_upload_file instead).

        Args:
            _microsoft_graph_conflictBehavior: Conflict behavior setting for Microsoft Graph API.
            folder: Details about the parent folder (if applicable).
            name: Name of the file or folder to be created.
        Returns:
            API response as a dictionary.
        """
        ...

    def microsoft_one_drive_create_sharable_link(
        self,
        fileId: str,
        scope: Optional[str] = None,
        type: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Generates a shareable link for a specific file or folder in the authenticated users Microsoft OneDrive by its item ID. Use this when you need to share a file or folder with others via a URL. Do not use this to manage permissions directly or to share with specific individuals by email. The generated link may be publicly accessible depending on the link type specified.

        Args:
            fileId:  (required)
            scope: 
            type: 
        Returns:
            API response as a dictionary.
        """
        ...

    def microsoft_one_drive_create_subscription(
        self,
        changeType: str,
        expirationDateTime: str,
        notificationUrl: str,
        resource: str,
        clientState: Optional[str] = None,
        lifecycleNotificationUrl: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Creates a new Microsoft Graph change notification subscription to receive webhook notifications when files or folders in OneDrive change. Use this when you need to set up real-time or near-real-time monitoring of drive changes. Do not use this to update an existing subscription (use microsoft_one_drive_update_subscription instead). Subscriptions have a limited lifetime and must be renewed before expiration.

        Args:
            changeType: Type of changes to monitor, such as created, updated, or deleted. (required)
            expirationDateTime: Date and time when the subscription expires, in UTC ISO 8601 format. (required)
            notificationUrl: URL where notifications will be sent when changes occur. (required)
            resource: The resource path to monitor for changes, e.g., a drive or item ID. (required)
            clientState: Optional client-provided string sent with each notification for validation.
            lifecycleNotificationUrl: Optional URL to receive lifecycle notifications about the subscription.
        Returns:
            API response as a dictionary.
        """
        ...

    def microsoft_one_drive_delete_subscription(
        self,
        subscriptionId: str,
    ) -> Dict[str, Any]:
        """Permanently deletes a specific Microsoft Graph change notification subscription by its subscription ID, stopping all future notifications for that subscription. Use this when you need to cancel webhook notifications for OneDrive changes. Do not use this to update or pause a subscription (use microsoft_one_drive_update_subscription instead). This action is irreversible — the subscription cannot be restored after deletion.

        Args:
            subscriptionId: The unique identifier of the subscription to be deleted. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def microsoft_one_drive_download_file(
        self,
        fileName: str,
    ) -> Dict[str, Any]:
        """Downloads the binary content of a file from the authenticated users Microsoft OneDrive by its path-based file name. Use this when you need to retrieve the actual content of a file for reading or processing. Do not use this to get only file metadata without downloading content (use microsoft_one_drive_get_file instead).

        Args:
            fileName: ID of the file to be accessed on Microsoft OneDrive. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def microsoft_one_drive_get_delta_changes(
        self,
        deltatoken: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Retrieves a list of changes (additions, modifications, and deletions) to files and folders in the authenticated users Microsoft OneDrive root since the last delta sync. Use this when you need to track incremental updates to the drive without scanning all items. Do not use this for an initial full listing of all files (use microsoft_one_drive_list_files_and_folders instead). Supports delta tokens for pagination across multiple sync cycles.

        Args:
            deltatoken: 
        Returns:
            API response as a dictionary.
        """
        ...

    def microsoft_one_drive_get_file(
        self,
        expand: Optional[str] = None,
        filter: Optional[str] = None,
        itemId: Optional[str] = None,
        orderby: Optional[str] = None,
        search: Optional[str] = None,
        select: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Retrieves metadata and details about a specific file or folder in the authenticated users Microsoft OneDrive by its item ID, including name, size, type, and last modified date. Use this when you need to inspect file properties without downloading its content. Do not use this to download the files binary content (use microsoft_one_drive_download_file instead).

        Args:
            expand: 
            filter: 
            itemId: 
            orderby: 
            search: 
            select: 
        Returns:
            API response as a dictionary.
        """
        ...

    def microsoft_one_drive_get_my_drive(
        self,
    ) -> Dict[str, Any]:
        """Retrieves metadata about the authenticated users Microsoft OneDrive, including storage quota, used space, drive type, and owner information. Use this when you need to check available storage or general drive properties. Do not use this to list files or folders (use microsoft_one_drive_list_files_and_folders instead).
        Returns:
            API response as a dictionary.
        """
        ...

    def microsoft_one_drive_get_my_user(
        self,
    ) -> Dict[str, Any]:
        """Retrieves the authenticated users Microsoft account profile information, including display name, email address, and user ID from the Microsoft Graph API. Use this when you need to identify the current user or obtain their account details. Do not use this to retrieve drive or file information (use microsoft_one_drive_get_my_drive instead).
        Returns:
            API response as a dictionary.
        """
        ...

    def microsoft_one_drive_get_subscription(
        self,
        subscriptionId: str,
    ) -> Dict[str, Any]:
        """Retrieves the details of a single Microsoft Graph change notification subscription by its subscription ID, including its notification URL, expiration time, and resource scope. Use this when you need to inspect the configuration of a specific subscription. Do not use this to list all subscriptions (use microsoft_one_drive_list_subscriptions instead).

        Args:
            subscriptionId: The unique identifier of the subscription to retrieve. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def microsoft_one_drive_list_files(
        self,
        orderby: Optional[str] = None,
        select: Optional[str] = None,
        skipToken: Optional[str] = None,
        top: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Lists all items (files and folders) at the root of the authenticated users Microsoft OneDrive. Use this when you need a flat listing of top-level drive contents. Do not use this to list contents of a specific subfolder (use microsoft_one_drive_list_files_from_folder instead). Note: this endpoint is equivalent to microsoft_one_drive_list_files_and_folders and may return duplicate results if both are called.

        Args:
            orderby: 
            select: 
            skipToken: 
            top: 
        Returns:
            API response as a dictionary.
        """
        ...

    def microsoft_one_drive_list_files_and_folders(
        self,
        expand: Optional[str] = None,
        orderby: Optional[str] = None,
        select: Optional[str] = None,
        skipToken: Optional[str] = None,
        top: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Lists all files and folders at the root level of the authenticated users Microsoft OneDrive in a single request. Use this when you need an overview of top-level items in the drive. Do not use this to list contents of a specific subfolder (use microsoft_one_drive_get_files_from_folder instead) or to search for a file by name (use microsoft_one_drive_search_file instead).

        Args:
            expand: 
            orderby: 
            select: 
            skipToken: 
            top: 
        Returns:
            API response as a dictionary.
        """
        ...

    def microsoft_one_drive_list_files_from_folder(
        self,
        itemId: str,
        expand: Optional[str] = None,
        orderby: Optional[str] = None,
        select: Optional[str] = None,
        skipToken: Optional[str] = None,
        top: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Lists all child items (files and subfolders) within a specific folder in the authenticated users Microsoft OneDrive by the folders item ID. Use this when you need to enumerate the contents of a known folder. Do not use this to list root-level items (use microsoft_one_drive_list_files_and_folders instead) or to search across the entire drive (use microsoft_one_drive_search_file instead).

        Args:
            itemId: The unique identifier of the item. (required)
            expand: Expand related entities inline.
            orderby: Specify the key by which to order the results.
            select: Specify which properties to include in the response.
            skipToken: Token for pagination to skip previous results.
            top: Maximum number of items to return.
        Returns:
            API response as a dictionary.
        """
        ...

    def microsoft_one_drive_list_subscriptions(
        self,
        orderby: Optional[str] = None,
        top: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Lists all active Microsoft Graph change notification subscriptions associated with the authenticated user. Use this when you need to review existing webhook subscriptions for OneDrive change tracking. Do not use this to retrieve details of a single subscription (use microsoft_one_drive_get_subscription instead).

        Args:
            orderby: Specifies the order in which to return the subscription items.
            top: The maximum number of subscription items to return.
        Returns:
            API response as a dictionary.
        """
        ...

    def microsoft_one_drive_move_file(
        self,
        fileId: str,
        parentReference: Optional[_MicrosoftOneDriveMoveFileParentreference] = None,
    ) -> Dict[str, Any]:
        """Moves a file to a different folder within the authenticated users Microsoft OneDrive by updating its parent reference using the item ID. Use this when you need to relocate a file to another folder. Do not use this to rename a file without moving it (use microsoft_one_drive_rename_file_or_folder instead). Requires the files item ID and the destination folders details.

        Args:
            fileId: ID of the file in MicrosoftOneDrive. (required)
            parentReference: Reference to the parent object in MicrosoftOneDrive.
        Returns:
            API response as a dictionary.
        """
        ...

    def microsoft_one_drive_rename_file_or_folder(
        self,
        fileId: str,
        name: str,
    ) -> Dict[str, Any]:
        """Renames a file or folder in the authenticated users Microsoft OneDrive by its item ID. Use this when you need to change the display name of an existing file or folder without moving it. Do not use this to move a file to a different folder (use microsoft_one_drive_move_file instead). Requires the target items ID.

        Args:
            fileId: ID of the file on Microsoft OneDrive. (required)
            name: Name of the file on Microsoft OneDrive. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def microsoft_one_drive_search_file(
        self,
        fileName: str,
    ) -> Dict[str, Any]:
        """Searches for files and folders in the authenticated users Microsoft OneDrive root by matching a file name query string. Use this when you need to locate a file by name or partial name without knowing its exact path or ID. Returns a list of matching items with their metadata. Do not use this to list all files in a folder (use microsoft_one_drive_list_files_and_folders or microsoft_one_drive_get_files_from_folder instead).

        Args:
            fileName: Name of the file for the Microsoft OneDrive API. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def microsoft_one_drive_update_subscription(
        self,
        subscriptionId: str,
        expirationDateTime: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Updates an existing Microsoft Graph change notification subscription (e.g., extends its expiration date or updates the notification URL) by its subscription ID. Use this when you need to renew or modify an active subscription before it expires. Do not use this to create a new subscription (use microsoft_one_drive_create_subscription instead) or to cancel one (use microsoft_one_drive_delete_subscription instead).

        Args:
            subscriptionId: The unique identifier of the subscription to update. (required)
            expirationDateTime: The new expiration time of the subscription in ISO 8601 format.
        Returns:
            API response as a dictionary.
        """
        ...

    def microsoft_one_drive_upload_file(
        self,
        body: str,
        fileName: str,
    ) -> Dict[str, Any]:
        """Uploads a file to a specified path in the authenticated users Microsoft OneDrive by writing its content at the given file name location. Use this when you need to store a new file or overwrite an existing file at a known path in OneDrive. Do not use this to upload files in raw binary format (use microsoft_one_drive_upload_file_in_binary instead) or to move an existing file to a new location. This operation will overwrite any existing file at the target path without warning.

        Args:
            body:  (required)
            fileName:  (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def microsoft_one_drive_upload_file_in_binary(
        self,
        fileName: str,
        body: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Uploads a file to the authenticated users Microsoft OneDrive in raw binary format by writing its content at the specified file name path. Use this when you need to upload binary data (e.g., images, PDFs, executables) directly to OneDrive. Do not use this for non-binary or text-based uploads where microsoft_one_drive_upload_file is sufficient. This operation will overwrite any existing file at the target path without warning.

        Args:
            fileName:  (required)
            body: 
        Returns:
            API response as a dictionary.
        """
        ...

