"""Fastn Buildkite connector — auto-generated type stubs.

Do not edit manually. Regenerate with `fastn connector sync`.
"""
from __future__ import annotations

from typing import Any, Dict, List, Optional, TypedDict


class BuildkiteConnector:
    """Buildkite connector ().

    Provides 8 tools.
    """

    def buildkite_cancel_build(
        self,
        BUILD_NUMBER: str,
        ORG_SLUG: str,
        PIPELINE_SLUG: str,
    ) -> Dict[str, Any]:
        """Cancels a running or scheduled build in Buildkite identified by its build number, pipeline slug, and organization. Use this to stop a build that is no longer needed or was triggered in error. Do not use this on builds that have already completed — cancellation only applies to active or queued builds. This action is irreversible; a cancelled build cannot be resumed and must be retried as a new build if needed.

        Args:
            BUILD_NUMBER: The specific build number within the pipeline. (required)
            ORG_SLUG: The organization slug associated with the Buildkite account. (required)
            PIPELINE_SLUG: The unique identifier for the specific pipeline in Buildkite. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def buildkite_create_build(
        self,
        ORG_SLUG: str,
        PIPELINE_SLUG: str,
        commit: str,
        branch: Optional[str] = None,
        message: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Creates and triggers a new build for a specified pipeline and organization in Buildkite, initiating the full CI/CD run. Use this when you want to start a fresh build, such as after a code change or on demand. Do not use this to re-run an existing build — use buildkite_retry_build for that. Note: triggering a build consumes pipeline execution resources and may incur costs depending on your infrastructure configuration.

        Args:
            ORG_SLUG: The slug identifier for the Buildkite organization. (required)
            PIPELINE_SLUG: The slug identifier for the specific pipeline. (required)
            commit: The specific commit SHA to build. (required)
            branch: The branch name to build.
            message: Optional message describing the build.
        Returns:
            API response as a dictionary.
        """
        ...

    def buildkite_get_build(
        self,
        BUILD_NUMBER: str,
        ORG_SLUG: str,
        PIPELINE_SLUG: str,
    ) -> Dict[str, Any]:
        """Retrieves detailed information about a single Buildkite build by its build number, pipeline slug, and organization, including status, log output references, timing, and job results. Use this when you need to inspect the outcome or progress of a specific build. Do not use this to list multiple builds — use buildkite_list_builds for that.

        Args:
            BUILD_NUMBER: The specific build number in Buildkite. (required)
            ORG_SLUG: The slug identifier for the Buildkite organization. (required)
            PIPELINE_SLUG: The slug identifier for the specific pipeline in Buildkite. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def buildkite_get_pipeline(
        self,
        ORG_SLUG: str,
        PIPELINE_SLUG: str,
    ) -> Dict[str, Any]:
        """Retrieves the full configuration and metadata of a single Buildkite pipeline identified by its slug and organization, including steps, environment settings, and repository linkage. Use this when you need detailed information about a specific pipeline. Do not use this to list all pipelines — use buildkite_list_pipelines for that.

        Args:
            ORG_SLUG: Unique identifier slug for the organization in Buildkite. (required)
            PIPELINE_SLUG: Unique identifier slug for the Buildkite pipeline. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def buildkite_list_builds(
        self,
        ORG_SLUG: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Lists all builds across a Buildkite organization, returning build numbers, statuses, branch names, and timestamps. Use this to review build history or monitor the overall state of CI/CD activity. Do not use this to retrieve a single builds details — use buildkite_get_build for that.

        Args:
            ORG_SLUG: 
        Returns:
            API response as a dictionary.
        """
        ...

    def buildkite_list_organizations(
        self,
    ) -> Dict[str, Any]:
        """Lists all Buildkite organizations accessible to the authenticated user, returning organization slugs and names. Use this to discover which organizations are available before making organization-scoped requests such as listing pipelines or builds. Do not use this to retrieve details of a single organization.
        Returns:
            API response as a dictionary.
        """
        ...

    def buildkite_list_pipelines(
        self,
        ORG_SLUG: str,
    ) -> Dict[str, Any]:
        """Lists all pipelines configured within a Buildkite organization, returning their names, slugs, and configuration metadata. Use this to discover available pipelines or to enumerate pipelines before querying a specific one. Do not use this to retrieve details of a single pipeline — use buildkite_get_pipeline for that.

        Args:
            ORG_SLUG: Slug identifier for the organization in Buildkite. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def buildkite_retry_build(
        self,
        BUILD_NUMBER: str,
        ORG_SLUG: str,
        PIPELINE_SLUG: str,
    ) -> Dict[str, Any]:
        """Retries a previous build in Buildkite by creating a new build run from an existing build number within a specified pipeline and organization. Use this when a build has failed or needs to be re-run without reconfiguring pipeline settings. Do not use this to create a brand-new build from scratch — use buildkite_create_build for that. This action triggers a new build run and consumes pipeline execution resources.

        Args:
            BUILD_NUMBER: The specific build number within the pipeline. (required)
            ORG_SLUG: The slug identifier for the organization. (required)
            PIPELINE_SLUG: The slug identifier for the specific pipeline. (required)
        Returns:
            API response as a dictionary.
        """
        ...

