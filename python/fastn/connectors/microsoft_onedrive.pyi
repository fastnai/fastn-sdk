"""Fastn Microsoft OneDrive connector — auto-generated type stubs.

Do not edit manually. Regenerate with `fastn connector sync`.
"""
from __future__ import annotations

from typing import Any, Dict, List, Optional


class MicrosoftOnedriveConnector:
    """Microsoft OneDrive connector ().

    Provides 18 tools.
    """

    def create_folder(
        self,
        _microsoft_graph_conflictBehavior: Optional[str] = None,
        folder: Optional[Dict[str, Any]] = None,
        name: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Creates a new folder within the specified context of the connector.

        Args:
            _microsoft_graph_conflictBehavior: Conflict behavior setting for Microsoft Graph API.
            folder: Details about the parent folder (if applicable).
            name: Name of the file or folder to be created.
        Returns:
            API response as a dictionary.
        """
        ...

    def create_sharable_link(
        self,
        scope: Optional[str] = None,
        type: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Generates a sharable link for a file or folder in the connector.

        Args:
            scope: 
            type: 
        Returns:
            API response as a dictionary.
        """
        ...

    def create_subscription(
        self,
        changeType: str,
        expirationDateTime: str,
        notificationUrl: str,
        resource: str,
        clientState: Optional[str] = None,
        lifecycleNotificationUrl: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Creates a new subscription using the specified details in the connector.

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

    def delete_subscription(
        self,
        subscriptionId: str,
    ) -> Dict[str, Any]:
        """Deletes a specific subscription from the connector.

        Args:
            subscriptionId: The unique identifier of the subscription to be deleted. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def download_file(
        self,
        fileName: str,
    ) -> Dict[str, Any]:
        """Downloads a file from the connector to the local device.

        Args:
            fileName: ID of the file to be accessed on Microsoft OneDrive. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def get_file(
        self,
        expand: Optional[str] = None,
        filter: Optional[str] = None,
        orderby: Optional[str] = None,
        search: Optional[str] = None,
        select: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Fetches detailed information about a specific file from the connector.

        Args:
            expand: 
            filter: 
            orderby: 
            search: 
            select: 
        Returns:
            API response as a dictionary.
        """
        ...

    def get_files(
        self,
        orderby: Optional[str] = None,
        select: Optional[str] = None,
        skipToken: Optional[str] = None,
        top: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Retrieves a list of files from the specified connector.

        Args:
            orderby: 
            select: 
            skipToken: 
            top: 
        Returns:
            API response as a dictionary.
        """
        ...

    def get_files_and_folders(
        self,
        expand: Optional[str] = None,
        orderby: Optional[str] = None,
        select: Optional[str] = None,
        skipToken: Optional[str] = None,
        top: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Retrieves both files and folders from the connector in a single request.

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

    def get_files_from_folder(
        self,
        expand: Optional[str] = None,
        orderby: Optional[str] = None,
        select: Optional[str] = None,
        skipToken: Optional[str] = None,
        top: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Obtains all files located within a specific folder in the connector.

        Args:
            expand: Expand related entities inline.
            orderby: Specify the key by which to order the results.
            select: Specify which properties to include in the response.
            skipToken: Token for pagination to skip previous results.
            top: Maximum number of items to return.
        Returns:
            API response as a dictionary.
        """
        ...

    def get_my_drive(
        self,
    ) -> Dict[str, Any]:
        """Gets information about the user's drive in the context of the connector.
        Returns:
            API response as a dictionary.
        """
        ...

    def get_my_user(
        self,
    ) -> Dict[str, Any]:
        """Retrieves the user's profile information from the connector.
        Returns:
            API response as a dictionary.
        """
        ...

    def get_subscription(
        self,
        subscriptionId: str,
    ) -> Dict[str, Any]:
        """Retrieves the details of a specific subscription from the connector.

        Args:
            subscriptionId: The unique identifier of the subscription to retrieve. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def get_subscriptions(
        self,
        orderby: Optional[str] = None,
        top: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Fetches all active subscriptions from the connector associated with the user.

        Args:
            orderby: Specifies the order in which to return the subscription items.
            top: The maximum number of subscription items to return.
        Returns:
            API response as a dictionary.
        """
        ...

    def move_file(
        self,
        parentReference: Optional[Dict[str, Any]] = None,
    ) -> Dict[str, Any]:
        """Moves a specified file to a different location within the connector.

        Args:
            parentReference: Reference to the parent object in MicrosoftOneDrive.
        Returns:
            API response as a dictionary.
        """
        ...

    def rename_file_or_folder(
        self,
        name: str,
    ) -> Dict[str, Any]:
        """Renames a file or folder in the connector as per the provided name.

        Args:
            name: Name of the file on Microsoft OneDrive. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def search_file(
        self,
        fileName: str,
    ) -> Dict[str, Any]:
        """Searches for a specific file in the connector using defined criteria.

        Args:
            fileName: Name of the file for the Microsoft OneDrive API. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def update_subscription(
        self,
        expirationDateTime: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Updates an existing subscription's details in the connector.

        Args:
            expirationDateTime: The new expiration time of the subscription in ISO 8601 format.
        Returns:
            API response as a dictionary.
        """
        ...

    def upload_file(
        self,
    ) -> Dict[str, Any]:
        """Uploads a file to the specified location within the connector.
        Returns:
            API response as a dictionary.
        """
        ...

