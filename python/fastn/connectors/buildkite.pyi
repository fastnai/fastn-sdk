"""Fastn buildkite connector — auto-generated type stubs.

Do not edit manually. Regenerate with `fastn connector sync`.
"""
from __future__ import annotations

from typing import Any, Dict, List, Optional


class BuildkiteConnector:
    """buildkite connector ().

    Provides 8 tools.
    """

    def cancel_build(
        self,
        BUILD_NUMBER: str,
        ORG_SLUG: str,
        PIPELINE_SLUG: str,
    ) -> Dict[str, Any]:
        """Cancels an ongoing build process in the specified CI/CD system.

        Args:
            BUILD_NUMBER: The specific build number within the pipeline. (required)
            ORG_SLUG: The organization slug associated with the Buildkite account. (required)
            PIPELINE_SLUG: The unique identifier for the specific pipeline in Buildkite. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def create__trigger__build(
        self,
        commit: str,
        branch: Optional[str] = None,
        message: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Triggers the creation of a new build in the specified CI/CD system.

        Args:
            commit: The specific commit SHA to build. (required)
            branch: The branch name to build.
            message: Optional message describing the build.
        Returns:
            API response as a dictionary.
        """
        ...

    def get_build(
        self,
        BUILD_NUMBER: str,
        ORG_SLUG: str,
        PIPELINE_SLUG: str,
    ) -> Dict[str, Any]:
        """Retrieves the details of a specific build in the specified CI/CD system.

        Args:
            BUILD_NUMBER: The specific build number in Buildkite. (required)
            ORG_SLUG: The slug identifier for the Buildkite organization. (required)
            PIPELINE_SLUG: The slug identifier for the specific pipeline in Buildkite. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def get_organizations(
        self,
    ) -> Dict[str, Any]:
        """Fetches a list of organizations within the specified CI/CD system.
        Returns:
            API response as a dictionary.
        """
        ...

    def get_pipeline(
        self,
        ORG_SLUG: str,
        PIPELINE_SLUG: str,
    ) -> Dict[str, Any]:
        """Retrieves the details of a specific pipeline in the specified CI/CD system.

        Args:
            ORG_SLUG: Unique identifier slug for the organization in Buildkite. (required)
            PIPELINE_SLUG: Unique identifier slug for the Buildkite pipeline. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def list_builds(
        self,
        ORG_SLUG: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Lists all builds associated with the specified CI/CD system.

        Args:
            ORG_SLUG: 
        Returns:
            API response as a dictionary.
        """
        ...

    def list_pipelines(
        self,
        ORG_SLUG: str,
    ) -> Dict[str, Any]:
        """Lists all pipelines available in the specified CI/CD system.

        Args:
            ORG_SLUG: Slug identifier for the organization in Buildkite. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def rebuild_or_retry_build(
        self,
        BUILD_NUMBER: str,
        ORG_SLUG: str,
        PIPELINE_SLUG: str,
    ) -> Dict[str, Any]:
        """Rebuilds or retries a specified build in the specified CI/CD system.

        Args:
            BUILD_NUMBER: The specific build number within the pipeline. (required)
            ORG_SLUG: The slug identifier for the organization. (required)
            PIPELINE_SLUG: The slug identifier for the specific pipeline. (required)
        Returns:
            API response as a dictionary.
        """
        ...

