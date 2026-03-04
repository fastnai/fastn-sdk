"""Fastn Keboola connector — auto-generated type stubs.

Do not edit manually. Regenerate with `fastn connector sync`.
"""
from __future__ import annotations

from typing import Any, Dict, List, Optional, TypedDict


class KeboolaConnector:
    """Keboola connector ().

    Provides 11 tools.
    """

    def keboola_create_maintainer(
        self,
        defaultConnectionExasolId: str,
        defaultConnectionRedshiftId: str,
        defaultConnectionSnowflakeId: str,
        defaultConnectionSynapseId: str,
        defaultConnectionTeradataId: str,
        defaultFileStorageId: str,
        name: str,
        zendeskUrl: str,
    ) -> Dict[str, Any]:
        """Creates a new maintainer in the Keboola platform on the Azure-hosted management API. Use this tool when you need to provision a new top-level maintainer entity. Do not use this tool to create organizations under a maintainer; use keboola_create_organization instead.

        Args:
            defaultConnectionExasolId: The ID of the default Exasol connection. (required)
            defaultConnectionRedshiftId: The ID of the default Redshift connection. (required)
            defaultConnectionSnowflakeId: The ID of the default Snowflake connection. (required)
            defaultConnectionSynapseId: The ID of the default Synapse connection. (required)
            defaultConnectionTeradataId: The ID of the default Teradata connection. (required)
            defaultFileStorageId: The ID of the default file storage. (required)
            name: The name of the Keebola instance. (required)
            zendeskUrl: The URL of the Zendesk instance. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def keboola_create_organization(
        self,
        crmId: str,
        maintainerId: str,
        name: str,
    ) -> Dict[str, Any]:
        """Creates a new organization under a specific Keboola maintainer, identified by its maintainer ID. Use this tool when you need to provision a new organization within an existing maintainers scope. Do not use this tool to update an existing organization; use the appropriate update tool instead.

        Args:
            crmId: The CRM ID for the Keebola request. (required)
            maintainerId: The ID of the maintainer. (required)
            name: The name for the Keebola request. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def keboola_delete_maintainer(
        self,
        maintainerId: str,
    ) -> Dict[str, Any]:
        """Permanently deletes a specific maintainer from the Keboola platform, identified by its maintainer ID. Use this tool only when the maintainer record must be fully removed. Do not use this tool to update maintainer details. Warning: this action is irreversible and may affect organizations managed by this maintainer.

        Args:
            maintainerId: The ID of the maintainer. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def keboola_delete_organization(
        self,
        organizationId: str,
    ) -> Dict[str, Any]:
        """Permanently deletes a specific organization from the Keboola platform, identified by its organization ID. Use this tool only when the organization and all its associated data must be fully removed. Do not use this tool to update organization details. Warning: this action is irreversible and will remove all projects and data associated with the organization.

        Args:
            organizationId: The organization ID for the Keebola API request. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def keboola_get_maintainer(
        self,
        maintainerId: str,
    ) -> Dict[str, Any]:
        """Retrieves details for a single Keboola maintainer, identified by its maintainer ID. Use this tool when you need the full profile of one specific maintainer. Do not use this tool to list all maintainers; use keboola_list_maintainers instead.

        Args:
            maintainerId: The ID of the maintainer. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def keboola_get_organization(
        self,
        organizationId: str,
    ) -> Dict[str, Any]:
        """Retrieves details for a single Keboola organization, identified by its organization ID. Use this tool when you need the full profile of one specific organization. Do not use this tool to list multiple organizations; use keboola_list_maintainer_organizations instead.

        Args:
            organizationId: The ID of the organization to target. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def keboola_get_project(
        self,
        projectId: str,
    ) -> Dict[str, Any]:
        """Retrieves detailed information about a single Keboola project, identified by its project ID. Use this tool when you need the full configuration and metadata for one specific project. Do not use this tool to list all projects across an organization.

        Args:
            projectId:  (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def keboola_list_maintainer_organizations(
        self,
        maintainerId: str,
        limit: Optional[str] = None,
        offset: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Retrieves a list of organizations associated with a specific Keboola maintainer, identified by its maintainer ID. Use this tool when you need to see which organizations fall under a given maintainers scope. Do not use this tool to retrieve details about a single organization; use keboola_get_organization instead.

        Args:
            maintainerId: The ID of the maintainer. (required)
            limit: The limit for pagination.
            offset: The offset for pagination.
        Returns:
            API response as a dictionary.
        """
        ...

    def keboola_list_maintainers(
        self,
        limit: Optional[str] = None,
        offset: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Retrieves a list of all maintainers registered in the Keboola platform. Use this tool when you need to enumerate maintainers for lookup, auditing, or management. Do not use this tool to fetch details about a single maintainer; use keboola_get_maintainer instead.

        Args:
            limit: The maximum number of records to return.
            offset: The starting offset for pagination.
        Returns:
            API response as a dictionary.
        """
        ...

    def keboola_list_organization_users(
        self,
        organizationId: str,
        limit: Optional[str] = None,
        offset: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Retrieves a list of users associated with a specific Keboola organization, identified by its organization ID. Use this tool when you need to audit or manage membership within an organization. Do not use this tool to retrieve details about a single user or to list organizations.

        Args:
            organizationId: The ID of the organization. (required)
            limit: The limit for pagination.
            offset: The offset for pagination.
        Returns:
            API response as a dictionary.
        """
        ...

    def keboola_verify_token(
        self,
    ) -> Dict[str, Any]:
        """Verifies the authenticity and validity of a Keboola API token. Use this tool to confirm that an authentication token is active and properly scoped before performing other Keboola operations. Do not use this tool to create or revoke tokens.
        Returns:
            API response as a dictionary.
        """
        ...

