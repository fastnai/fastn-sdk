"""Fastn Smartsheet connector — auto-generated type stubs.

Do not edit manually. Regenerate with `fastn connector sync`.
"""
from __future__ import annotations

from typing import Any, Dict, List, Optional, TypedDict


class _SmartsheetCreateWebhookSubscope(TypedDict, total=False):
    columnIds: List[Any]

class SmartsheetConnector:
    """Smartsheet connector ().

    Provides 15 tools.
    """

    def smartsheet_create_webhook(
        self,
        callbackUrl: str,
        events: List[Any],
        name: str,
        version: int,
        scope: Optional[str] = None,
        scopeObjectId: Optional[int] = None,
        subscope: Optional[_SmartsheetCreateWebhookSubscope] = None,
    ) -> Dict[str, Any]:
        """Creates a new Smartsheet webhook that sends HTTP event notifications to a specified callback URL when defined events occur on a sheet or resource. Use this to set up automated integrations triggered by Smartsheet changes. Use smartsheet_update_webhook to modify an existing webhook. The webhook is created in a disabled state by default and must be enabled separately before it will fire.

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

    def smartsheet_delete_webhook(
        self,
        webhookId: str,
    ) -> Dict[str, Any]:
        """Permanently deletes a specific Smartsheet webhook identified by webhookId, stopping all future event notifications sent to that webhooks callback URL. Use this when a webhook is no longer needed. This action is irreversible; the webhook cannot be recovered after deletion. Use smartsheet_update_webhook to disable a webhook temporarily instead of deleting it.

        Args:
            webhookId: Unique identifier for the SmartSheet webhook. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def smartsheet_get_sheet(
        self,
        sheetId: str,
        include: Optional[str] = None,
        level: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Retrieves the full contents of a specific Smartsheet sheet identified by sheetId, including columns, rows, and cell data. Use this when you need to read or analyze sheet data. Use smartsheet_list_sheets to find a sheetId first if you do not already have one. Use smartsheet_list_sheet_attachments to retrieve attachments separately. Does not modify the sheet.

        Args:
            sheetId: The ID of the SmartSheet to access. (required)
            include: Specifies which fields to include in the response.
            level: Specifies the detail level of the response.
        Returns:
            API response as a dictionary.
        """
        ...

    def smartsheet_get_user(
        self,
        userId: str,
    ) -> Dict[str, Any]:
        """Retrieves full profile details for a single Smartsheet user identified by userId, including name, email, and account status. Use this when you already have a userId and need detailed information about that user. Use smartsheet_list_users to discover userIds first if you do not already have one. Does not modify user data.

        Args:
            userId: User ID for SmartSheet API request. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def smartsheet_get_webhook(
        self,
        webhookId: str,
    ) -> Dict[str, Any]:
        """Retrieves the full configuration and status details of a single Smartsheet webhook identified by webhookId, including its callback URL, enabled state, and subscribed events. Use this when you already have a webhookId and need to inspect its settings. Use smartsheet_list_webhooks to discover webhookIds when you do not yet have one. Does not modify the webhook.

        Args:
            webhookId: Webhook ID for the SmartSheet SmartSheet API. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def smartsheet_get_workspace(
        self,
        workspaceId: str,
    ) -> Dict[str, Any]:
        """Retrieves full details and metadata for a single Smartsheet workspace identified by workspaceId. Use this when you already know the workspaceId and need its name, permalink, or other attributes. Use smartsheet_list_workspaces to discover workspaceIds when you do not yet have one. Does not return sharing permissions or folder contents.

        Args:
            workspaceId: ID of the SmartSheet workspace. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def smartsheet_list_dashboards(
        self,
        accessApiLevel: Optional[str] = None,
        includeAll: Optional[str] = None,
        modifiedSince: Optional[str] = None,
        numericDates: Optional[str] = None,
        page: Optional[str] = None,
        pageSize: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Lists all dashboards (called Sights in the Smartsheet API) accessible to the authenticated user. Use this to discover available dashboards and obtain their identifiers. Do not use this to retrieve sheet or workspace data; dashboards are separate visual summary objects distinct from sheets. Does not modify any data.

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

    def smartsheet_list_sheet_attachments(
        self,
        sheetId: str,
        includeAll: Optional[str] = None,
        page: Optional[str] = None,
        pageSize: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Lists all attachments associated with a specific Smartsheet sheet identified by sheetId. Use this to discover files attached at the sheet level. Note that attachments on individual rows are included only if they were added at the sheet level; row-level attachments may require a separate row endpoint. Does not download file content.

        Args:
            sheetId: ID of the SmartSheet to access. (required)
            includeAll: Flag to include all records (true/false).
            page: Page number to retrieve.
            pageSize: Number of records to retrieve per page.
        Returns:
            API response as a dictionary.
        """
        ...

    def smartsheet_list_sheets(
        self,
        accessApiLevel: Optional[str] = None,
        include: Optional[str] = None,
        includeAll: Optional[str] = None,
        modifiedSince: Optional[str] = None,
        numericDates: Optional[str] = None,
        page: Optional[str] = None,
        pageSize: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Lists all sheets accessible to the authenticated user across the entire Smartsheet account. Use this to discover sheets and obtain sheetIds before loading a specific sheets data. Use smartsheet_get_sheet when you already have a sheetId and need full sheet contents. Does not filter by workspace; returns summary-level metadata only.

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

    def smartsheet_list_users(
        self,
        email: Optional[str] = None,
        include: Optional[str] = None,
        includeAll: Optional[str] = None,
        modifiedSince: Optional[str] = None,
        numericDates: Optional[str] = None,
        page: Optional[str] = None,
        pageSize: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Lists all users in the Smartsheet account accessible to the authenticated administrator. Use this to enumerate account members or find a userId before retrieving a specific users details. Use smartsheet_get_user when you already have a userId. Requires admin-level access; returns summary-level user records.

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

    def smartsheet_list_webhooks(
        self,
        includeAll: Optional[str] = None,
        page: Optional[str] = None,
        pageSize: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Lists all webhooks registered in the authenticated Smartsheet account. Use this to audit existing webhooks, check their status, or find a webhookId before retrieving, updating, or deleting a specific webhook. Use smartsheet_get_webhook when you already have a webhookId and need full details. Does not modify any webhooks.

        Args:
            includeAll: Flag to include all records (true/false).
            page: Page number to retrieve.
            pageSize: Number of records to return per page.
        Returns:
            API response as a dictionary.
        """
        ...

    def smartsheet_list_workspace_folders(
        self,
        workspaceId: str,
        includeAll: Optional[str] = None,
        page: Optional[str] = None,
        pageSize: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Lists all folders contained within a specific Smartsheet workspace identified by workspaceId. Use this to explore the folder structure of a workspace before navigating to individual sheets. Use smartsheet_list_workspaces to find a workspaceId first if you do not already have one. Does not return folder contents such as sheets.

        Args:
            workspaceId: ID of the workspace in SmartSheet. (required)
            includeAll: Flag to include all records or a subset.
            page: Page number to retrieve.
            pageSize: Number of records to retrieve per page.
        Returns:
            API response as a dictionary.
        """
        ...

    def smartsheet_list_workspace_shares(
        self,
        workspaceId: str,
        accessApiLevel: Optional[str] = None,
        includeAll: Optional[str] = None,
        page: Optional[str] = None,
        pageSize: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Lists all sharing permissions and collaborator details for a specific Smartsheet workspace identified by workspaceId. Use this to audit who has access to a workspace and at what permission level. Use smartsheet_get_workspace instead when you need general workspace metadata rather than sharing details. Does not modify any permissions.

        Args:
            workspaceId: ID of the workspace in SmartSheet. (required)
            accessApiLevel: Specifies the access API level for the SmartSheet request.
            includeAll: Specifies whether to include all items in the SmartSheet request.
            page: Specifies the page number for the SmartSheet request.
            pageSize: Specifies the number of items per page for the SmartSheet request.
        Returns:
            API response as a dictionary.
        """
        ...

    def smartsheet_list_workspaces(
        self,
        accessApiLevel: Optional[str] = None,
        includeAll: Optional[str] = None,
        page: Optional[str] = None,
        pageSize: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Lists all workspaces available to the authenticated user in Smartsheet. Use this to discover workspaces before drilling into a specific one. Use smartsheet_get_workspace when you already have a workspaceId and need its full details. Returns summary-level metadata for each workspace; does not return sheets, folders, or sharing details.

        Args:
            accessApiLevel: Specifies the access level for the SmartSheet API.
            includeAll: Flag to include all records in SmartSheet API response (true/false).
            page: Page number for SmartSheet API pagination.
            pageSize: Number of records to return per page in SmartSheet API response.
        Returns:
            API response as a dictionary.
        """
        ...

    def smartsheet_update_webhook(
        self,
        webhookId: str,
        callbackUrl: Optional[str] = None,
        enabled: Optional[bool] = None,
        events: Optional[List[Any]] = None,
        name: Optional[str] = None,
        version: Optional[int] = None,
    ) -> Dict[str, Any]:
        """Updates the configuration of an existing Smartsheet webhook identified by webhookId, such as its name, callback URL, or enabled status. Use this to modify or temporarily disable a webhook without deleting it. Use smartsheet_create_webhook to register a new webhook instead. Changes take effect immediately upon a successful response.

        Args:
            webhookId: ID of the webhook in SmartSheet. (required)
            callbackUrl: URL to receive webhook events.
            enabled: Indicates if the webhook is enabled.
            events: List of events to trigger the webhook.
            name: Name of the webhook.
            version: Version of the webhook.
        Returns:
            API response as a dictionary.
        """
        ...

