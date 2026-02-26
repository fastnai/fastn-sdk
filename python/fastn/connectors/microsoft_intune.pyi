"""Fastn Microsoft Intune connector — auto-generated type stubs.

Do not edit manually. Regenerate with `fastn connector sync`.
"""
from __future__ import annotations

from typing import Any, Dict, List, Optional


class MicrosoftIntuneConnector:
    """Microsoft Intune connector ().

    Provides 18 tools.
    """

    def add_device_to_group(
        self,
        deviceId: str,
    ) -> Dict[str, Any]:
        """Adds a device to a specified group, facilitating organized management and oversight of devices.

        Args:
            deviceId: ID of the device in Microsoft Intune. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def batch(
        self,
    ) -> Dict[str, Any]:
        """Executes a batch process in the system to efficiently handle multiple tasks or operations at once.
        Returns:
            API response as a dictionary.
        """
        ...

    def create_group(
        self,
        displayName: str,
        mailEnabled: bool,
        mailNickname: str,
        securityEnabled: bool,
        description: Optional[str] = None,
        groupTypes: Optional[List[Any]] = None,
    ) -> Dict[str, Any]:
        """Creates a new group within the system, facilitating the organization of users or devices for better management.

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

    def create_script(
        self,
        displayName: str,
        fileName: str,
        scriptContent: str,
        description: Optional[str] = None,
        enforceSignatureCheck: Optional[bool] = None,
        runAs32Bit: Optional[bool] = None,
    ) -> Dict[str, Any]:
        """Creates a new script in the system, allowing for automation and execution of specific tasks.

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

    def create_subscription(
        self,
        changeType: str,
        expirationDateTime: str,
        resource: str,
        NotificationUrl: Optional[str] = None,
        clientState: Optional[str] = None,
        lifecycleNotificationUrl: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Creates a new subscription in the system, allowing access to specific features or services.

        Args:
            changeType: Type of change that triggered the notification. (required)
            expirationDateTime: Expiration date and time for the notification. (required)
            resource: Resource related to the notification. (required)
            NotificationUrl: URL to receive notifications.
            clientState: 
            lifecycleNotificationUrl: URL for lifecycle notifications.
        Returns:
            API response as a dictionary.
        """
        ...

    def delete_subscription(
        self,
    ) -> Dict[str, Any]:
        """Deletes an existing subscription in the system, terminating access to specific services or features.
        Returns:
            API response as a dictionary.
        """
        ...

    def delta_track(
        self,
        deltaToken: Optional[str] = None,
        filter: Optional[str] = None,
        select: Optional[str] = None,
        skipToken: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Tracks changes in a given context to ensure accurate updates and modifications are recorded.

        Args:
            deltaToken: Delta token for retrieving changes since the last request.
            filter: OData filter expression to filter the results.
            select: Comma-separated list of properties to select.
            skipToken: Skip token for paging.
        Returns:
            API response as a dictionary.
        """
        ...

    def get_devices(
        self,
        count: Optional[str] = None,
        filter: Optional[str] = None,
        orderBy: Optional[str] = None,
        select: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Retrieves a list of devices within the system, enabling effective device management and monitoring.

        Args:
            count: Indicates whether to return the total number of records.
            filter: Filter criteria for the request.
            orderBy: Specifies the field(s) to sort the results by.
            select: Specifies the fields to be returned in the response.
        Returns:
            API response as a dictionary.
        """
        ...

    def get_devices_by_group(
        self,
        select: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Retrieves devices associated with a specific group, allowing for targeted management under the designated group.

        Args:
            select: Specifies the fields to be returned in the response.  (e.g.,  'displayName,id')
        Returns:
            API response as a dictionary.
        """
        ...

    def get_groups(
        self,
        count: Optional[bool] = None,
        expand: Optional[str] = None,
        filter: Optional[str] = None,
        select: Optional[str] = None,
        skipToken: Optional[str] = None,
        top: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Fetches a list of all groups within the organization, assisting in group management and oversight.

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

    def get_groups_by_id(
        self,
        id: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Fetches information about a specific group using its ID, allowing for detailed management and modifications.

        Args:
            id: 
        Returns:
            API response as a dictionary.
        """
        ...

    def get_managed_device(
        self,
        filter: Optional[str] = None,
        search: Optional[str] = None,
        select: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Fetches information about a managed device in the system, enabling effective monitoring and management of device status.

        Args:
            filter: Filter criteria for the Microsoft Intune API request.
            search: Search term for the Microsoft Intune API request.
            select: Fields to select in the Microsoft Intune API response.
        Returns:
            API response as a dictionary.
        """
        ...

    def get_organization(
        self,
    ) -> Dict[str, Any]:
        """Retrieves information about the organization, including its details and settings within the system.
        Returns:
            API response as a dictionary.
        """
        ...

    def get_scripts(
        self,
    ) -> Dict[str, Any]:
        """Fetches a list of scripts available in the system, enabling management and execution of predefined tasks.
        Returns:
            API response as a dictionary.
        """
        ...

    def get_security_groups(
        self,
        expand: Optional[str] = None,
        filter: Optional[str] = None,
        select: Optional[str] = None,
        skipToken: Optional[str] = None,
        top: Optional[float] = None,
    ) -> Dict[str, Any]:
        """Retrieves detailed information about security groups, enabling management of security settings across various groups.

        Args:
            expand: OData expand expression
            filter: OData filter expression
            select: OData select expression
            skipToken: Token to skip items in the result set
            top: Number of items to return
        Returns:
            API response as a dictionary.
        """
        ...

    def get_security_groups_count(
        self,
    ) -> Dict[str, Any]:
        """Fetches the count of security groups in the system, providing insights into the security structure and organization.
        Returns:
            API response as a dictionary.
        """
        ...

    def get_transitive_members(
        self,
        filter: Optional[str] = None,
        orderby: Optional[str] = None,
        search: Optional[str] = None,
        select: Optional[str] = None,
        skip: Optional[str] = None,
        skipToken: Optional[str] = None,
        top: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Retrieves members of a group, including transitive members, allowing for a comprehensive view of group composition.

        Args:
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

    def reauthorize_subscription(
        self,
        subscriptionId: str,
    ) -> Dict[str, Any]:
        """Reauthorizes an existing subscription in the system, ensuring continued access to services or features.

        Args:
            subscriptionId: Subscription ID for accessing the Microsoft Intune service. (required)
        Returns:
            API response as a dictionary.
        """
        ...

