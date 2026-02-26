"""Fastn GitHub Enterprise connector — auto-generated type stubs.

Do not edit manually. Regenerate with `fastn connector sync`.
"""
from __future__ import annotations

from typing import Any, Dict, List, Optional


class GithubEnterpriseConnector:
    """GitHub Enterprise connector ().

    Provides 21 tools.
    """

    def create_blob(
        self,
        content: str,
        encoding: str,
    ) -> Dict[str, Any]:
        """Creates a new blob in the designated repository using the specified connector.

        Args:
            content: Content of the request body. (required)
            encoding: Encoding of the request body content. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def create_commit(
        self,
        author: Dict[str, Any],
        message: str,
        parents: List[Any],
        tree: str,
        signature: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Creates a new commit in the specified repository using the defined connector.

        Args:
            author: Author details for the commit. (required)
            message: Commit message. (required)
            parents: Array of parent commit SHAs. (required)
            tree: SHA of the tree object. (required)
            signature: Commit signature.
        Returns:
            API response as a dictionary.
        """
        ...

    def create_new_tree_using_blob(
        self,
        base_tree: Optional[str] = None,
        tree: Optional[List[Any]] = None,
    ) -> Dict[str, Any]:
        """Creates a new tree using a blob in the specified connector context.

        Args:
            base_tree: The SHA of the base tree.
            tree: 
        Returns:
            API response as a dictionary.
        """
        ...

    def create_pull_request(
        self,
        base: str,
        head: str,
        title: str,
        body: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Initiates a new pull request in the connector's repository context.

        Args:
            base: The base branch of the repository. (required)
            head: The head branch of the repository. (required)
            title: The title of the new repository. (required)
            body: The body of the new repository.
        Returns:
            API response as a dictionary.
        """
        ...

    def create_reference(
        self,
        ref: str,
        sha: str,
    ) -> Dict[str, Any]:
        """Establishes a new reference in the repository within the connector context.

        Args:
            ref: Git ref for the request (e.g., branch name). (required)
            sha: SHA hash of the commit. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def create_tree(
        self,
        base_tree: str,
        tree: List[Any],
    ) -> Dict[str, Any]:
        """Creates a new tree in the repository using the specified connector.

        Args:
            base_tree: Base tree for the GitHub repository. (required)
            tree:  (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def get_access_token(
        self,
        client_id: str,
        client_secret: str,
        code: str,
        redirect_uri: str,
    ) -> Dict[str, Any]:
        """Obtains an access token for authentication in the respective connector context.

        Args:
            client_id: Client ID for the GitHub application. (required)
            client_secret: Client secret for the GitHub application. (required)
            code: Authorization code received from GitHub. (required)
            redirect_uri: Redirect URI registered for the GitHub application. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def get_blob_from_hash(
        self,
        hash: str,
        repoId: str,
    ) -> Dict[str, Any]:
        """Fetches a blob from a given hash in the relevant repository using the connector.

        Args:
            hash: Commit hash of the repository. (required)
            repoId: Unique identifier for the GitHub repository. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def get_branch(
        self,
        branch: str,
        owner: str,
        repoName: str,
    ) -> Dict[str, Any]:
        """Retrieves a branch from the repository in the connector context.

        Args:
            branch: The branch name within the GitHub repository. (required)
            owner: The owner (username or organization) of the GitHub repository. (required)
            repoName: The name of the GitHub repository. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def get_branch_from_repository(
        self,
        page: Optional[str] = None,
        per_page: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Fetches a specific branch from a designated repository using the connector.

        Args:
            page: 
            per_page: 
        Returns:
            API response as a dictionary.
        """
        ...

    def get_branches(
        self,
        owner: str,
        repoName: str,
    ) -> Dict[str, Any]:
        """Lists all branches in the specified repository within the connector's context.

        Args:
            owner:  (required)
            repoName:  (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def get_dir(
        self,
        owner: str,
        repoName: str,
    ) -> Dict[str, Any]:
        """Retrieves directory content in the repository using the specified connector.

        Args:
            owner: The owner (username or organization) of the GitHub repository. (required)
            repoName: The name of the GitHub repository. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def get_latest_commit_sha(
        self,
        branchName: str,
        owner: str,
        repoName: str,
    ) -> Dict[str, Any]:
        """Retrieves the SHA of the latest commit from the relevant repository in the connector context.

        Args:
            branchName:  (required)
            owner: The owner or organization of the repository. (required)
            repoName: The name of the repository. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def get_my_orgs(
        self,
    ) -> Dict[str, Any]:
        """Lists organizations associated with the authenticated user in the connector context.
        Returns:
            API response as a dictionary.
        """
        ...

    def get_my_repositories(
        self,
        page: Optional[str] = None,
        per_page: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Fetches repositories associated with the authenticated user in the connector context.

        Args:
            page: 
            per_page: 
        Returns:
            API response as a dictionary.
        """
        ...

    def get_repo_content(
        self,
        recursive: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Retrieves content from the specified repository in the connector context.

        Args:
            recursive: Setting this parameter to any value returns the objects or subtrees referenced by the tree specified in :tree_sha. For example, setting recursive to any of the following will enable returning objects or subtrees: 0, 1, true, and false. Omit this parameter to prevent recursively returning objects or subtrees.
        Returns:
            API response as a dictionary.
        """
        ...

    def get_repo_data(
        self,
        owner: str,
        path: str,
        repoName: str,
    ) -> Dict[str, Any]:
        """Fetches details about the repository in the connector context.

        Args:
            owner: The owner (user or organization) of the repository. (required)
            path: The path to the resource within the repository. (required)
            repoName: The name of the repository. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def get_repositories(
        self,
        page: Optional[str] = None,
        per_page: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Lists all repositories accessible in the connector context.

        Args:
            page: The page number for pagination.
            per_page: The number of items per page for pagination.
        Returns:
            API response as a dictionary.
        """
        ...

    def get_repositories_from_org(
        self,
        page: Optional[str] = None,
        per_page: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Retrieves repositories from a specified organization in the connector context.

        Args:
            page: 
            per_page: 
        Returns:
            API response as a dictionary.
        """
        ...

    def get_tree_sha_base_commit(
        self,
        baseCommitSha: str,
        owner: str,
        repoName: str,
    ) -> Dict[str, Any]:
        """Obtains the tree SHA based on a given commit in the connector context.

        Args:
            baseCommitSha: SHA of the base commit for the Github repository. (required)
            owner: Owner (username or organization) of the Github repository. (required)
            repoName: Name of the Github repository. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def update_branch(
        self,
        force: bool,
        sha: str,
    ) -> Dict[str, Any]:
        """Updates a specified branch within the repository in the relevant connector context.

        Args:
            force: Force the merge operation (true/false). (required)
            sha: SHA of the commit to merge. (required)
        Returns:
            API response as a dictionary.
        """
        ...

