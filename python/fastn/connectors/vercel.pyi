"""Fastn Vercel connector — auto-generated type stubs.

Do not edit manually. Regenerate with `fastn connector sync`.
"""
from __future__ import annotations

from typing import Any, Dict, List, Optional, TypedDict


class _VercelCreateDeploymentProjectsettings(TypedDict, total=False):
    buildCommand: str
    devCommand: str
    framework: str
    installCommand: str
    outputDirectory: str

class VercelConnector:
    """Vercel connector ().

    Provides 3 tools.
    """

    def vercel_create_deployment(
        self,
        files: List[Any],
        name: str,
        projectSettings: Optional[_VercelCreateDeploymentProjectsettings] = None,
        target: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Creates and triggers a new deployment on Vercel for a specified project. Upon success, Vercel begins building and deploying the application, returning a deployment ID and preview URL. Use this tool when you need to deploy new or updated application code to Vercel. Note that this initiates a build process that may incur usage costs. Do not use this tool to list or inspect existing deployments — use vercel_list_deployments instead.

        Args:
            files:  (required)
            name: Name of the deployment. (required)
            projectSettings: Project settings for the deployment.
            target: Target environment for the deployment.
        Returns:
            API response as a dictionary.
        """
        ...

    def vercel_create_project(
        self,
        name: str,
        framework: Optional[str] = None,
        publicSource: Optional[bool] = None,
    ) -> Dict[str, Any]:
        """Creates a new project in the authenticated Vercel account, setting up the project configuration required before deployments can be made. Use this tool when you are onboarding a new application or repository to Vercel for the first time. Do not use this tool to deploy code — use vercel_create_deployment after the project has been created.

        Args:
            name: The name of the project. (required)
            framework: The framework used in the project.
            publicSource: Indicates whether the source code is publicly accessible.
        Returns:
            API response as a dictionary.
        """
        ...

    def vercel_list_deployments(
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
        """Retrieves a list of all deployments associated with the authenticated Vercel account, including deployment status, creation date, and associated project details. Use this tool when you need an overview of current or past deployments. Do not use this tool to create a new deployment — use vercel_create_deployment instead.

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

