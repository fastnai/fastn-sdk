"""Fastn SmartSheet connector — auto-generated type stubs.

Do not edit manually. Regenerate with `fastn connector sync`.
"""
from __future__ import annotations

from typing import Any, Dict, List, Optional


class SmartsheetConnector:
    """SmartSheet connector ().

    Provides 15 tools.
    """

    def create_webhook(
        self,
        callbackUrl: str,
        events: List[Any],
        name: str,
        version: int,
        scope: Optional[str] = None,
        scopeObjectId: Optional[int] = None,
        subscope: Optional[Dict[str, Any]] = None,
    ) -> Dict[str, Any]:
        """Creates a new webhook in the specified system.

        Args:
            callbackUrl: URL to receive SmartSheet webhook notifications. (required)
            events: List of events that trigger the SmartSheet webhook. (required)
            name: Name of the SmartSheet webhook. (required)
            version: Version of the SmartSheet webhook. (required)
            scope: Scope of the SmartSheet webhook (e.g., sheet, folder).
            scopeObjectId: ID of the SmartSheet object the webhook applies to.
            subscope: Sub-scope details for the SmartSheet webhook.
        Returns:
            API response as a dictionary.
        """
        ...

    def delete_webhook(
        self,
        webhookId: str,
    ) -> Dict[str, Any]:
        """Deletes a specified webhook from the system.

        Args:
            webhookId: Unique identifier for the SmartSheet webhook. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def get_dashboards(
        self,
        accessApiLevel: Optional[str] = None,
        includeAll: Optional[str] = None,
        modifiedSince: Optional[str] = None,
        numericDates: Optional[str] = None,
        page: Optional[str] = None,
        pageSize: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Retrieves a list of dashboards available in the specified context.

        Args:
            accessApiLevel: Specifies the access level for the API call.
            includeAll: Indicates whether to include all items or only a subset.
            modifiedSince: Filters results to include only items modified since the specified date and time.
            numericDates: Indicates whether dates should be returned as numeric values.
            page: Specifies the page number for pagination.
            pageSize: Specifies the number of items to return per page.
        Returns:
            API response as a dictionary.
        """
        ...

    def get_sheet(
        self,
        include: Optional[str] = None,
        level: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Fetches the details of a specific sheet within a given workspace.

        Args:
            include: Specifies which fields to include in the response.
            level: Specifies the detail level of the response.
        Returns:
            API response as a dictionary.
        """
        ...

    def get_sheet_attachments(
        self,
        includeAll: Optional[str] = None,
        page: Optional[str] = None,
        pageSize: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Retrieves attachments associated with a specific sheet in the defined context.

        Args:
            includeAll: Flag to include all records (true/false).
            page: Page number to retrieve.
            pageSize: Number of records to retrieve per page.
        Returns:
            API response as a dictionary.
        """
        ...

    def get_sheets(
        self,
        accessApiLevel: Optional[str] = None,
        include: Optional[str] = None,
        includeAll: Optional[str] = None,
        modifiedSince: Optional[str] = None,
        numericDates: Optional[str] = None,
        page: Optional[str] = None,
        pageSize: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Fetches all sheets available within a specified workspace.

        Args:
            accessApiLevel: Specifies the access level for the SmartSheet API.
            include: Specifies the fields to include in the response.
            includeAll: Indicates whether to include all records in the response.
            modifiedSince: Specifies the date and time since which modifications should be included.
            numericDates: Indicates whether to return dates in numeric format.
            page: Specifies the page number for pagination.
            pageSize: Specifies the number of records per page in the response.
        Returns:
            API response as a dictionary.
        """
        ...

    def get_user(
        self,
        userId: str,
    ) -> Dict[str, Any]:
        """Retrieves the details of a specific user in the system.

        Args:
            userId: User ID for SmartSheet API request. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def get_users(
        self,
        email: Optional[str] = None,
        include: Optional[str] = None,
        includeAll: Optional[str] = None,
        modifiedSince: Optional[str] = None,
        numericDates: Optional[str] = None,
        page: Optional[str] = None,
        pageSize: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Fetches a list of all users within the defined context.

        Args:
            email: Email address for filtering results (if applicable).
            include: Specifies which fields to include in the response.
            includeAll: Indicates whether to include all items, regardless of pagination.
            modifiedSince: Filter results to only include items modified since this timestamp.
            numericDates: Indicates whether to return dates in numeric format.
            page: Specifies the page number for paginated results.
            pageSize: Specifies the number of items per page in the response.
        Returns:
            API response as a dictionary.
        """
        ...

    def get_webhook(
        self,
        webhookId: str,
    ) -> Dict[str, Any]:
        """Retrieves the details of a specific webhook using its unique identifier.

        Args:
            webhookId: Webhook ID for the SmartSheet SmartSheet API. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def get_webhooks(
        self,
        includeAll: Optional[str] = None,
        page: Optional[str] = None,
        pageSize: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Retrieves all webhooks associated with the specified system.

        Args:
            includeAll: Flag to include all records (true/false).
            page: Page number to retrieve.
            pageSize: Number of records to return per page.
        Returns:
            API response as a dictionary.
        """
        ...

    def get_workspace(
        self,
        workspaceId: str,
    ) -> Dict[str, Any]:
        """Fetches details of the specified workspace, including metadata.

        Args:
            workspaceId: ID of the SmartSheet workspace. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def get_workspace_folders(
        self,
        includeAll: Optional[str] = None,
        page: Optional[str] = None,
        pageSize: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Retrieves folders present within a specific workspace.

        Args:
            includeAll: Flag to include all records or a subset.
            page: Page number to retrieve.
            pageSize: Number of records to retrieve per page.
        Returns:
            API response as a dictionary.
        """
        ...

    def get_workspace_shares(
        self,
        accessApiLevel: Optional[str] = None,
        includeAll: Optional[str] = None,
        page: Optional[str] = None,
        pageSize: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Retrieves sharing permissions and details for a specific workspace.

        Args:
            accessApiLevel: Specifies the access API level for the SmartSheet request.
            includeAll: Specifies whether to include all items in the SmartSheet request.
            page: Specifies the page number for the SmartSheet request.
            pageSize: Specifies the number of items per page for the SmartSheet request.
        Returns:
            API response as a dictionary.
        """
        ...

    def get_workspaces(
        self,
        accessApiLevel: Optional[str] = None,
        includeAll: Optional[str] = None,
        page: Optional[str] = None,
        pageSize: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Fetches a list of all workspaces available in the system.

        Args:
            accessApiLevel: Specifies the access level for the SmartSheet API.
            includeAll: Flag to include all records in SmartSheet API response (true/false).
            page: Page number for SmartSheet API pagination.
            pageSize: Number of records to return per page in SmartSheet API response.
        Returns:
            API response as a dictionary.
        """
        ...

    def update_webhook(
        self,
        callbackUrl: Optional[str] = None,
        enabled: Optional[bool] = None,
        events: Optional[List[Any]] = None,
        name: Optional[str] = None,
        version: Optional[int] = None,
    ) -> Dict[str, Any]:
        """Updates an existing webhook with new information in the specified system.

        Args:
            callbackUrl: URL to receive webhook events.
            enabled: Indicates if the webhook is enabled.
            events: List of events to trigger the webhook.
            name: Name of the webhook.
            version: Version of the webhook.
        Returns:
            API response as a dictionary.
        """
        ...

