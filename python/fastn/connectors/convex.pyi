"""Fastn Convex connector — auto-generated type stubs.

Do not edit manually. Regenerate with `fastn connector sync`.
"""
from __future__ import annotations

from typing import Any, Dict, List, Optional


class ConvexConnector:
    """Convex connector ().

    Provides 6 tools.
    """

    def create_deploy_key(
        self,
        name: str,
    ) -> Dict[str, Any]:
        """Creates a deploy key in the specified connector to enable secure access for deployments.

        Args:
            name: A name associated with the request. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def create_project(
        self,
        deploymentType: str,
        projectName: str,
    ) -> Dict[str, Any]:
        """Creates a new project in the specified connector, allowing for task management and collaboration.

        Args:
            deploymentType: Type of deployment. (required)
            projectName: Name of the project. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def delete_project(
        self,
        projectID: str,
    ) -> Dict[str, Any]:
        """Deletes an existing project in the specified connector, permanently removing all associated data and resources.

        Args:
            projectID: The ID of the project. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def get_deployments(
        self,
        projectID: str,
    ) -> Dict[str, Any]:
        """Retrieves a list of deployments in the specified connector, providing information on the deployment history and statuses.

        Args:
            projectID: The ID of the project to target. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def get_projects(
        self,
        teamID: str,
    ) -> Dict[str, Any]:
        """Fetches all projects in the specified connector, allowing you to view and manage your project portfolio.

        Args:
            teamID: The ID of the team. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def token_details(
        self,
    ) -> Dict[str, Any]:
        """Retrieves details about a specific token in the specified connector, including its permissions and associated user.
        Returns:
            API response as a dictionary.
        """
        ...

