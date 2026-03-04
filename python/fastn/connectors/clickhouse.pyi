"""Fastn ClickHouse connector — auto-generated type stubs.

Do not edit manually. Regenerate with `fastn connector sync`.
"""
from __future__ import annotations

from typing import Any, Dict, List, Optional, TypedDict


class ClickhouseConnector:
    """ClickHouse connector ().

    Provides 10 tools.
    """

    def clickhouse_create_byoc_infrastructure(
        self,
        accountId: str,
        availabilityZoneSuffixes: List[Any],
        orgID: str,
        regionId: str,
        vpcCidrRange: str,
    ) -> Dict[str, Any]:
        """Creates a new Bring Your Own Cloud (BYOC) infrastructure configuration within a ClickHouse Cloud organization, allowing ClickHouse services to run inside your own cloud account. Use this tool when you need to set up BYOC connectivity for an organization. Do not use this tool to create a standard managed service (use clickhouse_create_service instead). Requires a valid organization ID. This action provisions infrastructure in your cloud environment and is not easily reversible.

        Args:
            accountId: ID of the account. (required)
            availabilityZoneSuffixes: Suffixes of the availability zones. (required)
            orgID: ID of the organization. (required)
            regionId: ID of the region. (required)
            vpcCidrRange: CIDR range for the VPC. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def clickhouse_create_invitation(
        self,
        email: str,
        orgID: str,
        role: str,
    ) -> Dict[str, Any]:
        """Sends an invitation to a user to join a specific ClickHouse Cloud organization. Use this tool when you need to onboard a new member by email. Do not use this tool to add an existing member directly or to list current invitations (use clickhouse_list_invitations instead). Requires a valid organization ID. This action sends an email notification to the invited user.

        Args:
            email: User email address. (required)
            orgID: ID of the organization. (required)
            role: User role. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def clickhouse_create_service(
        self,
        backupId: str,
        byocId: str,
        complianceType: str,
        dataWarehouseId: str,
        encryptionAssumedRoleIdentifier: str,
        encryptionKey: str,
        endpoints: List[Any],
        hasTransparentDataEncryption: bool,
        idleScaling: bool,
        idleTimeoutMinutes: int,
        ipAccessList: List[Any],
        isReadonly: bool,
        maxReplicaMemoryGb: int,
        maxTotalMemoryGb: int,
        minReplicaMemoryGb: int,
        minTotalMemoryGb: int,
        name: str,
        numReplicas: int,
        orgID: str,
        privateEndpointIds: List[Any],
        privatePreviewTermsChecked: bool,
        provider: str,
        region: str,
        releaseChannel: str,
        tier: str,
    ) -> Dict[str, Any]:
        """Creates a new ClickHouse Cloud service (database cluster) within a specified organization. Use this tool when you need to provision a new database service with defined parameters such as region, tier, and configuration. Do not use this tool to modify an existing service. Requires a valid organization ID. This action provisions cloud resources and may incur costs; it cannot be undone without a separate delete operation.

        Args:
            backupId: ID of the backup to restore from. (required)
            byocId: Bring your own certificate ID. (required)
            complianceType: Compliance type of the instance. (required)
            dataWarehouseId: ID of the associated data warehouse. (required)
            encryptionAssumedRoleIdentifier: Assumed role ARN for encryption. (required)
            encryptionKey: Encryption key for the instance. (required)
            endpoints:  (required)
            hasTransparentDataEncryption: Enable/disable transparent data encryption. (required)
            idleScaling: Enable/disable idle scaling. (required)
            idleTimeoutMinutes: Timeout before idle scaling. (required)
            ipAccessList:  (required)
            isReadonly: Enable/disable readonly mode. (required)
            maxReplicaMemoryGb: Maximum memory for replicas. (required)
            maxTotalMemoryGb: Maximum total memory allocated to the instance. (required)
            minReplicaMemoryGb: Minimum memory for replicas. (required)
            minTotalMemoryGb: Minimum total memory allocated to the instance. (required)
            name: Name of the Clickhouse instance. (required)
            numReplicas: Number of replicas for the instance. (required)
            orgID: Identifier of the organization. (required)
            privateEndpointIds: List of private endpoint IDs. (required)
            privatePreviewTermsChecked: Indicates acceptance of private preview terms. (required)
            provider: Cloud provider for the instance. (required)
            region: Geographic region of the instance. (required)
            releaseChannel: Release channel of the instance. (required)
            tier: Performance tier of the instance. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def clickhouse_get_organization_details(
        self,
        orgID: str,
    ) -> Dict[str, Any]:
        """Retrieves detailed attributes and settings for a specific ClickHouse Cloud organization by its ID. Use this tool when you need in-depth information about a single organization, such as its configuration or metadata. Do not use this tool to list all organizations (use clickhouse_list_organizations instead). Requires a valid organization ID. No data is modified by this call.

        Args:
            orgID: ID of the organization. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def clickhouse_list_invitations(
        self,
        orgID: str,
    ) -> Dict[str, Any]:
        """Lists all pending and sent invitations for a specific ClickHouse Cloud organization, including their statuses. Use this tool when you need to review who has been invited to join an organization. Do not use this tool to create a new invitation (use clickhouse_create_invitation instead). Requires a valid organization ID. No data is modified by this call.

        Args:
            orgID: The ID of the organization. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def clickhouse_list_org_members(
        self,
        orgID: str,
    ) -> Dict[str, Any]:
        """Lists all members of a specific ClickHouse Cloud organization, including their roles and permissions. Use this tool when you need to audit or review who has access to an organization. Do not use this tool to add or remove members. Requires a valid organization ID. No data is modified by this call.

        Args:
            orgID: The ID of the organization. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def clickhouse_list_organization_activities(
        self,
        orgID: str,
        from_date: Optional[str] = None,
        to_date: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Lists the activity log entries for a specific ClickHouse Cloud organization, detailing recent actions taken by members or the system. Use this tool when you need to audit or investigate recent changes within an organization. Do not use this tool to retrieve member lists or service details. Requires a valid organization ID. No data is modified by this call.

        Args:
            orgID: The ID of the organization. (required)
            from_date: The starting date of the date range.
            to_date: The ending date of the date range.
        Returns:
            API response as a dictionary.
        """
        ...

    def clickhouse_list_organization_services(
        self,
        orgID: str,
    ) -> Dict[str, Any]:
        """Lists all ClickHouse Cloud services associated with a specific organization. Use this tool when you need an inventory of services (database clusters) running under an organization. Do not use this tool to retrieve details for a single service or to create new services (use clickhouse_create_service instead). Requires a valid organization ID. No data is modified by this call.

        Args:
            orgID: The ID of the organization. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def clickhouse_list_organizations(
        self,
    ) -> Dict[str, Any]:
        """Lists all ClickHouse Cloud organizations associated with the authenticated account. Use this tool when you need to discover available organizations or retrieve their IDs for use in subsequent calls. Do not use this tool to retrieve detailed attributes of a single organization (use clickhouse_get_organization_details instead). No data is modified by this call.
        Returns:
            API response as a dictionary.
        """
        ...

    def clickhouse_list_service_backups(
        self,
        orgID: str,
        serviceID: str,
    ) -> Dict[str, Any]:
        """Lists all available backups for a specific ClickHouse Cloud service within an organization. Use this tool when you need to review backup history or verify recovery options for a service. Do not use this tool to initiate or restore a backup. Requires a valid organization ID and service ID. No data is modified by this call.

        Args:
            orgID: The ID of the organization. (required)
            serviceID: The ID of the service within the organization. (required)
        Returns:
            API response as a dictionary.
        """
        ...

