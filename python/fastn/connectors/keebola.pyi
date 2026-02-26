"""Fastn Keebola connector — auto-generated type stubs.

Do not edit manually. Regenerate with `fastn connector sync`.
"""
from __future__ import annotations

from typing import Any, Dict, List, Optional


class KeebolaConnector:
    """Keebola connector ().

    Provides 11 tools.
    """

    def create_maintainer(
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
        """Creates a new maintainer in the system.

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

    def create_organization(
        self,
        crmId: str,
        name: str,
    ) -> Dict[str, Any]:
        """Creates a new organization in the system.

        Args:
            crmId: The CRM ID for the Keebola request. (required)
            name: The name for the Keebola request. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def delete_maintainer(
        self,
        maintainerId: str,
    ) -> Dict[str, Any]:
        """Deletes an existing maintainer from the system.

        Args:
            maintainerId: The ID of the maintainer. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def delete_organization(
        self,
        organizationId: str,
    ) -> Dict[str, Any]:
        """Deletes an existing organization from the system.

        Args:
            organizationId: The organization ID for the Keebola API request. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def get_maintainer(
        self,
        maintainerId: str,
    ) -> Dict[str, Any]:
        """Retrieves details for a specific maintainer.

        Args:
            maintainerId: The ID of the maintainer. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def get_maintainer_organizations(
        self,
        limit: Optional[str] = None,
        offset: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Retrieves a list of organizations associated with a specific maintainer.

        Args:
            limit: The limit for pagination.
            offset: The offset for pagination.
        Returns:
            API response as a dictionary.
        """
        ...

    def get_maintainers(
        self,
        limit: Optional[str] = None,
        offset: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Retrieves a list of all maintainers in the system.

        Args:
            limit: The maximum number of records to return.
            offset: The starting offset for pagination.
        Returns:
            API response as a dictionary.
        """
        ...

    def get_organization(
        self,
        organizationId: str,
    ) -> Dict[str, Any]:
        """Retrieves details for a specific organization.

        Args:
            organizationId: The ID of the organization to target. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def get_organization_users(
        self,
        limit: Optional[str] = None,
        offset: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Retrieves a list of users associated with a specific organization.

        Args:
            limit: The limit for pagination.
            offset: The offset for pagination.
        Returns:
            API response as a dictionary.
        """
        ...

    def get_projects_detail(
        self,
        projectId: str,
    ) -> Dict[str, Any]:
        """Retrieves detailed information about projects in the system.

        Args:
            projectId:  (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def verify_token(
        self,
    ) -> Dict[str, Any]:
        """Verifies the authenticity of a provided token.
        Returns:
            API response as a dictionary.
        """
        ...

