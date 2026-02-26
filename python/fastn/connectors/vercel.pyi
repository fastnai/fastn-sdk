"""Fastn vercel connector — auto-generated type stubs.

Do not edit manually. Regenerate with `fastn connector sync`.
"""
from __future__ import annotations

from typing import Any, Dict, List, Optional


class VercelConnector:
    """vercel connector ().

    Provides 3 tools.
    """

    def create_deployment(
        self,
        files: List[Any],
        name: str,
        projectSettings: Optional[Dict[str, Any]] = None,
        target: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Creates a new deployment within the specified connector's infrastructure.

        Args:
            files:  (required)
            name: Name of the deployment. (required)
            projectSettings: Project settings for the deployment.
            target: Target environment for the deployment.
        Returns:
            API response as a dictionary.
        """
        ...

    def create_project(
        self,
        name: str,
        framework: Optional[str] = None,
        publicSource: Optional[bool] = None,
    ) -> Dict[str, Any]:
        """Creates a new project in the specified connector environment.

        Args:
            name: The name of the project. (required)
            framework: The framework used in the project.
            publicSource: Indicates whether the source code is publicly accessible.
        Returns:
            API response as a dictionary.
        """
        ...

    def get_deployments(
        self,
        app: Optional[str] = None,
        from: Optional[str] = None,
        limit: Optional[str] = None,
        projectId: Optional[str] = None,
        rollbackCandidate: Optional[str] = None,
        since: Optional[str] = None,
        slug: Optional[str] = None,
        state: Optional[str] = None,
        target: Optional[str] = None,
        teamId: Optional[str] = None,
        to: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Retrieves a list of all deployments associated with the specified connector.

        Args:
            app: Name of the application.
            from: Start date or timestamp for filtering.
            limit: Limit the number of results.
            projectId: ID of the project.
            rollbackCandidate: Rollback candidate identifier.
            since: Filter results since a specific date or timestamp.
            slug: Slug of the application.
            state: Filter by deployment state.
            target: Target environment for deployment.
            teamId: ID of the team.
            to: End date or timestamp for filtering.
        Returns:
            API response as a dictionary.
        """
        ...

