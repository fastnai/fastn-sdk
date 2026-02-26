"""Fastn Azure DevOps connector — auto-generated type stubs.

Do not edit manually. Regenerate with `fastn connector sync`.
"""
from __future__ import annotations

from typing import Any, Dict, List, Optional


class AzureDevopsConnector:
    """Azure DevOps connector ().

    Provides 7 tools.
    """

    def get_accounts(
        self,
        apiversion: Optional[str] = None,
        memberId: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Retrieves a list of accounts associated with the authenticated user using the corresponding API connector.

        Args:
            apiversion: 
            memberId: 
        Returns:
            API response as a dictionary.
        """
        ...

    def get_branches(
        self,
        apiversion: Optional[str] = None,
        filter: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Fetches a list of all branches within a specific repository through the designated API connector.

        Args:
            apiversion: API version for the Azure DevOps request.
            filter: Filter criteria for the Azure DevOps API request.
        Returns:
            API response as a dictionary.
        """
        ...

    def get_changes_from_commit(
        self,
        apiversion: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Gathers details of changes made in a specific commit within a repository using the appropriate API connector.

        Args:
            apiversion: The version of the Azure DevOps API being used.
        Returns:
            API response as a dictionary.
        """
        ...

    def get_my_profile(
        self,
        apiversion: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Fetches profile information of the authenticated user through the designated API connector.

        Args:
            apiversion: 
        Returns:
            API response as a dictionary.
        """
        ...

    def get_projects(
        self,
        apiversion: Optional[str] = None,
        continuationToken: Optional[str] = None,
        top: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Obtains information about the projects associated with a particular organization or user via the relevant API connector.

        Args:
            apiversion: API version for the request.
            continuationToken: 
            top: 
        Returns:
            API response as a dictionary.
        """
        ...

    def get_repo_content(
        self,
        apiversion: Optional[str] = None,
        includeContent: Optional[str] = None,
        includeContentMetadata: Optional[str] = None,
        includeLinks: Optional[str] = None,
        path: Optional[str] = None,
        recursionLevel: Optional[str] = None,
        resolveLfs: Optional[str] = None,
        scopePath: Optional[str] = None,
        version: Optional[str] = None,
        versionDescriptor_type: Optional[str] = None,
        versionDescriptor_version: Optional[str] = None,
        versionType: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Retrieves the content of a specific repository using the appropriate API connector.

        Args:
            apiversion: API version for the request.
            includeContent: 
            includeContentMetadata: Flag to include content metadata in the response.
            includeLinks: Flag to include links in the response.
            path: 
            recursionLevel: Recursion level for nested objects.
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

    def get_repositories(
        self,
        apiversion: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Lists all repositories accessible to the authenticated user using the respective API connector.

        Args:
            apiversion: API version for the Azure DevOps request.
        Returns:
            API response as a dictionary.
        """
        ...

