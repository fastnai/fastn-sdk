"""Fastn Azure DevOps connector — auto-generated type stubs.

Do not edit manually. Regenerate with `fastn connector sync`.
"""
from __future__ import annotations

from typing import Any, Dict, List, Optional, TypedDict


class AzureDevopsConnector:
    """Azure DevOps connector ().

    Provides 7 tools.
    """

    def azure_devops_get_changes_from_commit(
        self,
        apiversion: Optional[str] = None,
        commitId: Optional[str] = None,
        organizationName: Optional[str] = None,
        projectName: Optional[str] = None,
        repoName: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Retrieves the file-level changes (additions, modifications, deletions) introduced by a specific commit in an Azure DevOps Git repository. Use this tool when you need to inspect what changed in a particular commit, for example during code review, audit, or diff analysis. Do not use this tool to list commits or branches — use the appropriate list tools for discovery. Requires organization name, project name, repository name, and a valid commit ID.

        Args:
            apiversion: The version of the Azure DevOps API being used.
            commitId: The ID of the Git commit.
            organizationName: The name of the Azure DevOps organization.
            projectName: The name of the Azure DevOps project.
            repoName: The name of the Git repository.
        Returns:
            API response as a dictionary.
        """
        ...

    def azure_devops_get_my_profile(
        self,
        apiversion: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Retrieves the profile information of the currently authenticated Azure DevOps user, including display name, email, and account details. Use this tool when you need to identify who is authenticated or personalize responses based on the current users profile. Do not use this tool to list accounts or projects — use azure_devops_list_accounts or azure_devops_list_projects for those.

        Args:
            apiversion: 
        Returns:
            API response as a dictionary.
        """
        ...

    def azure_devops_get_repo_content(
        self,
        apiversion: Optional[str] = None,
        includeContent: Optional[str] = None,
        includeContentMetadata: Optional[str] = None,
        includeLinks: Optional[str] = None,
        organizationName: Optional[str] = None,
        path: Optional[str] = None,
        projectName: Optional[str] = None,
        recursionLevel: Optional[str] = None,
        repoName: Optional[str] = None,
        resolveLfs: Optional[str] = None,
        scopePath: Optional[str] = None,
        version: Optional[str] = None,
        versionDescriptor_type: Optional[str] = None,
        versionDescriptor_version: Optional[str] = None,
        versionType: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Retrieves the content of a file or directory listing within a specific Azure DevOps Git repository. Use this tool when you need to read source code, configuration files, or browse the file tree of a repository. Do not use this tool to list repositories or branches — use azure_devops_list_repositories or azure_devops_list_branches for discovery. Requires organization name, project name, repository name, and optionally a path to a specific file or folder.

        Args:
            apiversion: API version for the request.
            includeContent: 
            includeContentMetadata: Flag to include content metadata in the response.
            includeLinks: Flag to include links in the response.
            organizationName: Name of the Azure DevOps organization.
            path: 
            projectName: Name of the Azure DevOps project.
            recursionLevel: Recursion level for nested objects.
            repoName: Name of the repository.
            resolveLfs: Flag to resolve LFS pointers.
            scopePath: Scope path for the request.
            version: 
            versionDescriptor_type: Type of version descriptor.
            versionDescriptor_version: Version descriptor for the request.
            versionType: 
        Returns:
            API response as a dictionary.
        """
        ...

    def azure_devops_list_accounts(
        self,
        apiversion: Optional[str] = None,
        memberId: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Lists all Azure DevOps accounts associated with the currently authenticated user. Use this tool when you need to discover which Azure DevOps organizations or accounts a user belongs to, for example as a first step before querying projects or repositories. Do not use this tool to retrieve project or repository details — use azure_devops_list_projects or azure_devops_list_repositories for those.

        Args:
            apiversion: 
            memberId: 
        Returns:
            API response as a dictionary.
        """
        ...

    def azure_devops_list_branches(
        self,
        apiversion: Optional[str] = None,
        filter: Optional[str] = None,
        organizationName: Optional[str] = None,
        projectName: Optional[str] = None,
        repoName: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Lists all branches (Git refs) within a specific repository in an Azure DevOps project. Use this tool when you need to discover available branches before checking out content or inspecting commits on a branch. Do not use this tool to retrieve file content or commit changes — use azure_devops_get_repo_content or azure_devops_get_changes_from_commit for those. Requires organization name, project name, and repository name.

        Args:
            apiversion: API version for the Azure DevOps request.
            filter: Filter criteria for the Azure DevOps API request.
            organizationName: Name of the Azure DevOps organization.
            projectName: Name of the Azure DevOps project.
            repoName: Name of the Azure DevOps repository.
        Returns:
            API response as a dictionary.
        """
        ...

    def azure_devops_list_projects(
        self,
        apiversion: Optional[str] = None,
        continuationToken: Optional[str] = None,
        organizationName: Optional[str] = None,
        top: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Lists all projects within a specific Azure DevOps organization. Use this tool when you need to discover which projects exist in an organization before querying repositories, branches, or commits. Do not use this tool to retrieve repositories or commits — use azure_devops_list_repositories or azure_devops_get_changes_from_commit for those. Requires the organization name.

        Args:
            apiversion: API version for the request.
            continuationToken: 
            organizationName: Name of the Azure DevOps organization.
            top: 
        Returns:
            API response as a dictionary.
        """
        ...

    def azure_devops_list_repositories(
        self,
        apiversion: Optional[str] = None,
        organizationName: Optional[str] = None,
        projectName: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Lists all Git repositories accessible within a specific Azure DevOps project. Use this tool when you need to discover available repositories before reading content, branches, or commits. Do not use this tool to retrieve the content or branches of a specific repository — use azure_devops_get_repo_content or azure_devops_list_branches for those. Requires organization name and project name.

        Args:
            apiversion: API version for the Azure DevOps request.
            organizationName: Name of the Azure DevOps organization.
            projectName: Name of the Azure DevOps project.
        Returns:
            API response as a dictionary.
        """
        ...

