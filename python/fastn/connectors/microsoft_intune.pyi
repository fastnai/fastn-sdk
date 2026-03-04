"""Fastn Microsoft Intune connector — auto-generated type stubs.

Do not edit manually. Regenerate with `fastn connector sync`.
"""
from __future__ import annotations

from typing import Any, Dict, List, Optional, TypedDict


class MicrosoftIntuneConnector:
    """Microsoft Intune connector ().

    Provides 18 tools.
    """

    def microsoft_intune_add_device_to_group(
        self,
        deviceId: str,
        groupId: str,
    ) -> Dict[str, Any]:
        """Adds a device as a member of a specified Azure AD group using the groups ID. Use this to organize devices into groups for policy assignment, conditional access, or management scope targeting. Requires a valid group ID and device object reference. This action modifies group membership and may immediately affect any policies or access rules applied to that group.

        Args:
            deviceId: ID of the device in Microsoft Intune. (required)
            groupId: ID of the group in Microsoft Intune. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def microsoft_intune_create_group(
        self,
        displayName: str,
        mailEnabled: bool,
        mailNickname: str,
        securityEnabled: bool,
        description: Optional[str] = None,
        groupTypes: Optional[List[Any]] = None,
    ) -> Dict[str, Any]:
        """Creates a new Azure AD group for organizing users or devices within the organization. Use this when you need a new group to apply Intune policies, conditional access rules, or management scopes. This action has persistent side effects — the group is created in Azure AD and will remain until explicitly deleted. Do not use this to modify or add members to an existing group.

        Args:
            displayName: Display name of the group. (required)
            mailEnabled: Indicates whether the group is mail-enabled. (required)
            mailNickname: Mail nickname for the group. (required)
            securityEnabled: Indicates whether the group is security-enabled. (required)
            description: Description of the group.
            groupTypes: Array of group types.  Example: ['Security']
        Returns:
            API response as a dictionary.
        """
        ...

    def microsoft_intune_create_script(
        self,
        displayName: str,
        fileName: str,
        scriptContent: str,
        description: Optional[str] = None,
        enforceSignatureCheck: Optional[bool] = None,
        runAs32Bit: Optional[bool] = None,
    ) -> Dict[str, Any]:
        """Creates a new device management script in Microsoft Intune. Use this when you need to deploy a new PowerShell or shell script to managed devices for automation or configuration tasks. The script will be stored in Intune and can subsequently be assigned to device groups. This action has persistent side effects — the script is saved to the system and will remain until explicitly deleted. Do not use this to update an existing script.

        Args:
            displayName: Display name of the script. (required)
            fileName: Name of the script file. (required)
            scriptContent: Content of the script to be uploaded. (required)
            description: Description of the script.
            enforceSignatureCheck: Specifies whether to enforce signature check for the script.
            runAs32Bit: Specifies whether the script should run as 32-bit.
        Returns:
            API response as a dictionary.
        """
        ...

    def microsoft_intune_create_subscription(
        self,
        NotificationUrl: Optional[str] = None,
        changeType: Optional[str] = None,
        expirationDateTime: Optional[str] = None,
        lifecycleNotificationUrl: Optional[str] = None,
        resource: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Creates a new Microsoft Graph change notification subscription to receive real-time webhook notifications for Intune or Azure AD resource changes such as device state changes or group membership updates. Use this when you need continuous event-driven notifications delivered to a configured webhook endpoint. The subscription remains active until it expires or is explicitly deleted. This action has persistent side effects — notifications will be sent to the webhook endpoint until the subscription is removed. Do not use this for one-time data queries; use the appropriate list or get tool instead.

        Args:
            NotificationUrl: 
            changeType: 
            expirationDateTime: 
            lifecycleNotificationUrl: 
            resource: 
        Returns:
            API response as a dictionary.
        """
        ...

    def microsoft_intune_delete_subscription(
        self,
        subId: str,
        body: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Permanently deletes an existing Microsoft Graph change notification subscription identified by its subscription ID. Use this when you want to stop receiving webhook notifications for a previously created subscription. This action is irreversible — once deleted, the subscription cannot be restored and notifications will cease immediately. Do not use this to temporarily pause notifications; there is no pause mechanism.

        Args:
            subId: The Azure subscription ID associated with the Microsoft Intune tenant. (required)
            body: The main body of the request for the Microsoft Intune API.
        Returns:
            API response as a dictionary.
        """
        ...

    def microsoft_intune_execute_batch(
        self,
        body: Optional[Dict[str, Any]] = None,
    ) -> Dict[str, Any]:
        """Executes multiple Microsoft Graph API requests in a single HTTP call using the Graph batch endpoint. Use this to combine up to 20 independent requests into one network round-trip, improving efficiency when multiple read or write operations need to be performed together. Each request in the batch is processed independently and may succeed or fail individually. Side effects depend on the individual requests included in the batch — write operations within the batch will modify data. Do not use this for single operations; use the appropriate dedicated tool instead.

        Args:
            body: Request body for the Microsoft Intune API.
        Returns:
            API response as a dictionary.
        """
        ...

    def microsoft_intune_get_group(
        self,
        id: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Retrieves detailed information about a specific Azure AD group using its unique group ID. Use this to fetch properties such as display name, membership type, and settings for a single known group. Requires a valid group ID. Do not use this to list all groups; use microsoft_intune_list_groups for that. This tool is read-only and has no side effects.

        Args:
            id: 
        Returns:
            API response as a dictionary.
        """
        ...

    def microsoft_intune_get_organization(
        self,
    ) -> Dict[str, Any]:
        """Retrieves details about the organizations Azure AD tenant, including its display name, verified domains, and configuration settings. Use this to obtain tenant-level metadata for auditing or configuration purposes. This tool is read-only and has no side effects.
        Returns:
            API response as a dictionary.
        """
        ...

    def microsoft_intune_get_security_groups_count(
        self,
    ) -> Dict[str, Any]:
        """Returns the total count of mail-disabled security groups in the organization. Use this to obtain a numeric summary of security groups for reporting or threshold checks without retrieving full group details. Do not use this to retrieve the groups themselves; use microsoft_intune_list_security_groups for that. This tool is read-only and has no side effects.
        Returns:
            API response as a dictionary.
        """
        ...

    def microsoft_intune_list_devices(
        self,
        count: Optional[str] = None,
        filter: Optional[str] = None,
        orderBy: Optional[str] = None,
        select: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Lists all devices registered in Azure AD within the organization. Use this to retrieve a broad inventory of all Azure AD-joined or registered devices for monitoring or auditing purposes. This differs from listing Intune-managed devices specifically; use microsoft_intune_list_managed_devices if you need only Intune-enrolled devices. This tool is read-only and has no side effects.

        Args:
            count: Indicates whether to return the total number of records.
            filter: Filter criteria for the request.
            orderBy: Specifies the field(s) to sort the results by.
            select: Specifies the fields to be returned in the response.
        Returns:
            API response as a dictionary.
        """
        ...

    def microsoft_intune_list_devices_by_group(
        self,
        groupId: str,
        select: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Lists all devices that are transitive members of a specified Azure AD group, including devices inherited through nested groups. Use this to identify all devices in scope for a particular group, regardless of nesting depth. Requires a valid group ID. Do not use this if you only need direct device members; this returns the full transitive closure. This tool is read-only and has no side effects.

        Args:
            groupId: ID of the group. (required)
            select: Specifies the fields to be returned in the response.  (e.g.,  'displayName,id')
        Returns:
            API response as a dictionary.
        """
        ...

    def microsoft_intune_list_groups(
        self,
        count: Optional[bool] = None,
        expand: Optional[str] = None,
        filter: Optional[str] = None,
        select: Optional[str] = None,
        skipToken: Optional[str] = None,
        top: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Lists all Azure AD groups within the organization. Use this to retrieve a complete collection of groups for auditing, selection, or management tasks. Do not use this to retrieve a single group by ID; use microsoft_intune_get_group for that. This tool is read-only and has no side effects.

        Args:
            count: Indicates whether to include the total count of results.
            expand: OData expand expression to include related entities.
            filter: OData filter expression to refine the results.
            select: OData select expression to specify the fields to return.
            skipToken: OData skip token for paging results.
            top: OData top expression to limit the number of results.
        Returns:
            API response as a dictionary.
        """
        ...

    def microsoft_intune_list_groups_delta(
        self,
        deltaToken: Optional[str] = None,
        filter: Optional[str] = None,
        select: Optional[str] = None,
        skipToken: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Retrieves incremental changes to Azure AD groups since the last delta query, using the Microsoft Graph delta tracking mechanism. Use this for efficient change tracking to detect newly created, updated, or deleted groups without fetching the full group list each time. Requires a delta token from a previous delta query for incremental results; omit it for the initial full sync. Do not use this if you need the complete current list of groups without change context; use microsoft_intune_list_groups instead. This tool is read-only and has no side effects.

        Args:
            deltaToken: Delta token for retrieving changes since the last request.
            filter: OData filter expression to filter the results.
            select: Comma-separated list of properties to select.
            skipToken: Skip token for paging.
        Returns:
            API response as a dictionary.
        """
        ...

    def microsoft_intune_list_managed_devices(
        self,
        ConsistencyLevel: str,
        deviceId: str,
        filter: Optional[str] = None,
        search: Optional[str] = None,
        select: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Lists all managed devices registered in Microsoft Intune. Use this to retrieve a collection of devices under Intune management for monitoring, auditing, or status review. Returns device metadata such as OS, compliance state, and enrollment details. Do not use this to retrieve a single device by ID; use a get action for that. This tool is read-only and has no side effects.

        Args:
            ConsistencyLevel: Consistency level for the Microsoft Intune API request. (required)
            deviceId: ID of the device for the Microsoft Intune API request. (required)
            filter: Filter criteria for the Microsoft Intune API request.
            search: Search term for the Microsoft Intune API request.
            select: Fields to select in the Microsoft Intune API response.
        Returns:
            API response as a dictionary.
        """
        ...

    def microsoft_intune_list_scripts(
        self,
    ) -> Dict[str, Any]:
        """Lists all device management scripts configured in Microsoft Intune. Use this to retrieve available scripts for review, auditing, or selecting a script to assign or execute. Returns script metadata including name, description, and platform. This tool is read-only and has no side effects. Do not use this to create or modify scripts.
        Returns:
            API response as a dictionary.
        """
        ...

    def microsoft_intune_list_security_groups(
        self,
        body: Dict[str, Any],
        expand: Optional[str] = None,
        filter: Optional[str] = None,
        select: Optional[str] = None,
        skipToken: Optional[str] = None,
        top: Optional[float] = None,
    ) -> Dict[str, Any]:
        """Lists all security groups in the organization from Azure AD, including their properties and membership configuration. Use this to retrieve security groups for auditing, policy assignment, or access control reviews. Do not use this to retrieve distribution or Microsoft 365 groups; apply filters if a specific group type is needed. This tool is read-only and has no side effects.

        Args:
            body: Body of the request for Microsoft Intune API.  May be empty for some requests. (required)
            expand: OData expand expression
            filter: OData filter expression
            select: OData select expression
            skipToken: Token to skip items in the result set
            top: Number of items to return
        Returns:
            API response as a dictionary.
        """
        ...

    def microsoft_intune_list_transitive_members(
        self,
        ConsistencyLevel: str,
        groupId: str,
        filter: Optional[str] = None,
        orderby: Optional[str] = None,
        search: Optional[str] = None,
        select: Optional[str] = None,
        skip: Optional[str] = None,
        skipToken: Optional[str] = None,
        top: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Lists all device members of a specified group, including members inherited transitively through nested groups. Use this when you need a complete, flattened view of all devices belonging to a group hierarchy, not just direct members. Requires a valid group ID. Do not use this if you only need direct members of a group. This tool is read-only and has no side effects.

        Args:
            ConsistencyLevel: Specifies the consistency level for the request. (required)
            groupId: ID of the group. (required)
            filter: OData filter expression.
            orderby: Property to order results by.
            search: Search term.
            select: Comma-separated list of properties to select.
            skip: Number of results to skip.
            skipToken: Token to skip results.
            top: Number of results to return.
        Returns:
            API response as a dictionary.
        """
        ...

    def microsoft_intune_reauthorize_subscription(
        self,
        subscriptionId: str,
    ) -> Dict[str, Any]:
        """Reauthorizes an existing Microsoft Graph change notification subscription to extend or renew its authorization. Use this when a subscriptions authorization has expired or been revoked and you need to restore notification delivery without deleting and recreating it. Requires a valid subscription ID. This action modifies the subscription state. Do not use this to create a new subscription or update subscription filters.

        Args:
            subscriptionId: Subscription ID for accessing the Microsoft Intune service. (required)
        Returns:
            API response as a dictionary.
        """
        ...

