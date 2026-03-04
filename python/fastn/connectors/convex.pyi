"""Fastn Convex connector — auto-generated type stubs.

Do not edit manually. Regenerate with `fastn connector sync`.
"""
from __future__ import annotations

from typing import Any, Dict, List, Optional, TypedDict


class ConvexConnector:
    """Convex connector ().

    Provides 6 tools.
    """

    def convex_create_deploy_key(
        self,
        deploymentName: str,
        name: str,
    ) -> Dict[str, Any]:
        """Creates a new deploy key for a specified Convex deployment, enabling secure programmatic access for CI/CD pipelines and deployment automation. Use this when you need a scoped credential for a deployment. Requires a valid deploymentName. The generated key is sensitive — store it securely immediately, as it may not be retrievable again.

        Args:
            deploymentName: The name of the Convex deployment. (required)
            name: A name associated with the request. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def convex_create_project(
        self,
        deploymentType: str,
        projectName: str,
        teamID: str,
    ) -> Dict[str, Any]:
        """Creates a new Convex project under a specified team. Use this when setting up a new application or workspace within an existing team. Requires a valid teamID. Do not use this to update or duplicate an existing project — use it only for net-new projects.

        Args:
            deploymentType: Type of deployment. (required)
            projectName: Name of the project. (required)
            teamID: The ID of the team. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def convex_delete_project(
        self,
        projectID: str,
    ) -> Dict[str, Any]:
        """Permanently deletes an existing Convex project and all of its associated data, deployments, and resources. Use this only when a project must be fully removed. This action is irreversible — all project data will be lost and cannot be recovered. Requires a valid projectID.

        Args:
            projectID: The ID of the project. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def convex_get_token_details(
        self,
    ) -> Dict[str, Any]:
        """Retrieves details about the authenticated API token in Convex, including its permissions and associated user. Use this to inspect what access a token has before performing sensitive operations. Does not modify any data.
        Returns:
            API response as a dictionary.
        """
        ...

    def convex_list_deployments(
        self,
        projectID: str,
    ) -> Dict[str, Any]:
        """Returns all deployments associated with a specified Convex project, including deployment history and statuses. Use this to audit deployment state or find a specific deployment name. Requires a valid projectID. Does not modify any data.

        Args:
            projectID: The ID of the project to target. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def convex_list_projects(
        self,
        teamID: str,
    ) -> Dict[str, Any]:
        """Returns all projects belonging to a specified Convex team. Use this to enumerate available projects when you need to find a project ID or review the teams project portfolio. Requires a valid teamID. Does not modify any data.

        Args:
            teamID: The ID of the team. (required)
        Returns:
            API response as a dictionary.
        """
        ...

