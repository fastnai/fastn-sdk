"""Fastn GitHub Enterprise connector — auto-generated type stubs.

Do not edit manually. Regenerate with `fastn connector sync`.
"""
from __future__ import annotations

from typing import Any, Dict, List, Optional, TypedDict


class _GithubEnterpriseCreateCommitAuthor(TypedDict, total=False):
    date: str
    email: str
    name: str

class GithubEnterpriseConnector:
    """GitHub Enterprise connector ().

    Provides 21 tools.
    """

    def github_enterprise_create_blob(
        self,
        content: str,
        encoding: str,
        owner: str,
        repoName: str,
    ) -> Dict[str, Any]:
        """Creates a new Git blob object in a specified GitHub Enterprise repository, storing raw file content (typically Base64-encoded) in the repositorys Git database. Use this as the first step in a low-level Git file-write workflow before creating a tree (github_enterprise_create_tree) and commit (github_enterprise_create_commit). Do not use this to update existing files through the contents API directly. The blob is stored permanently in the Git object database once created.

        Args:
            content: Content of the request body. (required)
            encoding: Encoding of the request body content. (required)
            owner: GitHub owner (user or organization) of the repository. (required)
            repoName: Name of the GitHub repository. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def github_enterprise_create_commit(
        self,
        author: _GithubEnterpriseCreateCommitAuthor,
        message: str,
        owner: str,
        parents: List[Any],
        repoName: str,
        tree: str,
        signature: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Creates a new Git commit object in a specified GitHub Enterprise repository, recording a snapshot of the repository tree with a message and parent commit reference. Use this as part of a low-level Git workflow after creating a tree (github_enterprise_create_tree) to finalize changes. Do not use this as a standalone action without subsequently updating a branch reference (use github_enterprise_update_branch). Commits are permanent once created and become part of the repository history.

        Args:
            author: Author details for the commit. (required)
            message: Commit message. (required)
            owner: Repository owner's username. (required)
            parents: Array of parent commit SHAs. (required)
            repoName: Repository name. (required)
            tree: SHA of the tree object. (required)
            signature: Commit signature.
        Returns:
            API response as a dictionary.
        """
        ...

    def github_enterprise_create_new_tree_using_blob(
        self,
        owner: str,
        repoName: str,
        base_tree: Optional[str] = None,
        tree: Optional[List[Any]] = None,
    ) -> Dict[str, Any]:
        """Creates a new Git tree object in a specified GitHub Enterprise repository by composing it from one or more existing blob SHAs, typically as part of a programmatic file-update workflow. Use this after creating blobs (github_enterprise_create_blob) and before creating a commit (github_enterprise_create_commit). Do not use this when github_enterprise_create_tree already covers your needs; this tool is a workflow-specific variant that explicitly accepts blob references. The resulting tree is permanently stored in the repositorys Git object database.

        Args:
            owner: The owner (user or organization) of the repository. (required)
            repoName: The name of the repository. (required)
            base_tree: The SHA of the base tree.
            tree: 
        Returns:
            API response as a dictionary.
        """
        ...

    def github_enterprise_create_pull_request(
        self,
        base: str,
        head: str,
        owner: str,
        repoName: str,
        title: str,
        body: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Creates a new pull request in a specified GitHub Enterprise repository, proposing to merge changes from a head branch into a base branch for review. Use this when you want to initiate a code review or merge workflow between two branches. Do not use this to update an existing pull request or to merge branches directly. This action is irreversible in the sense that it notifies reviewers and creates a permanent pull request record; the PR can be closed but not deleted.

        Args:
            base: The base branch of the repository. (required)
            head: The head branch of the repository. (required)
            owner: The owner of the repository. (required)
            repoName: The name of the repository. (required)
            title: The title of the new repository. (required)
            body: The body of the new repository.
        Returns:
            API response as a dictionary.
        """
        ...

    def github_enterprise_create_reference(
        self,
        owner: str,
        ref: str,
        repoName: str,
        sha: str,
    ) -> Dict[str, Any]:
        """Creates a new Git reference (branch or tag) in a specified GitHub Enterprise repository, pointing to a given commit SHA. Use this to programmatically create a new branch or tag as part of an automated workflow. Do not use this to update an existing reference (use github_enterprise_update_branch) or to create a pull request (use github_enterprise_create_pull_request). Creating a reference immediately makes the branch or tag visible to all collaborators.

        Args:
            owner: GitHub username or organization name owning the repository. (required)
            ref: Git ref for the request (e.g., branch name). (required)
            repoName: Name of the repository. (required)
            sha: SHA hash of the commit. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def github_enterprise_create_tree(
        self,
        base_tree: str,
        owner: str,
        repoName: str,
        tree: List[Any],
    ) -> Dict[str, Any]:
        """Creates a new Git tree object in a specified GitHub Enterprise repository, defining a file structure by referencing blobs and existing trees. Use this as part of a low-level Git data workflow when programmatically constructing commits (typically after creating blobs with github_enterprise_create_blob). Do not use this to directly commit files through the contents API. This action creates a permanent tree object in the repositorys Git database.

        Args:
            base_tree: Base tree for the GitHub repository. (required)
            owner: Owner (username or organization) of the GitHub repository. (required)
            repoName: Name of the GitHub repository. (required)
            tree:  (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def github_enterprise_get_access_token(
        self,
        client_id: str,
        client_secret: str,
        code: str,
        redirect_uri: str,
    ) -> Dict[str, Any]:
        """Exchanges an OAuth authorization code for a GitHub Enterprise access token via the OAuth 2.0 token endpoint. Use this during the OAuth authentication flow to obtain a bearer token required for all authenticated API operations. Do not use this to refresh an existing token or to authenticate with a personal access token directly. This call creates a new access token; store the result securely as it grants API access on behalf of the user.

        Args:
            client_id: Client ID for the GitHub application. (required)
            client_secret: Client secret for the GitHub application. (required)
            code: Authorization code received from GitHub. (required)
            redirect_uri: Redirect URI registered for the GitHub application. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def github_enterprise_get_blob_from_hash(
        self,
        hash: str,
        repoId: str,
    ) -> Dict[str, Any]:
        """Retrieves a Git blob object from a GitHub Enterprise repository using its SHA hash. Use this when you need the raw contents of a specific file or data object identified by its blob hash. Do not use this to browse directory contents or file paths (use github_enterprise_get_dir or github_enterprise_get_repo_data instead). Returns the blobs content and encoding (typically Base64).

        Args:
            hash: Commit hash of the repository. (required)
            repoId: Unique identifier for the GitHub repository. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def github_enterprise_get_branch(
        self,
        branch: str,
        owner: str,
        repoName: str,
    ) -> Dict[str, Any]:
        """Retrieves detailed information about a single named branch within a specified GitHub Enterprise repository, including the latest commit SHA, protection status, and branch metadata. Use this when you need the current state of a specific known branch. Do not use this to list all branches (use github_enterprise_list_branches) or to retrieve a branch from a repo referenced by a partial path (use github_enterprise_get_branch_from_repository).

        Args:
            branch: The branch name within the GitHub repository. (required)
            owner: The owner (username or organization) of the GitHub repository. (required)
            repoName: The name of the GitHub repository. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def github_enterprise_get_branch_from_repository(
        self,
        page: Optional[str] = None,
        per_page: Optional[str] = None,
        repo: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Retrieves a specific branch from a GitHub Enterprise repository by repository identifier. Use this when you need metadata and status for a single named branch within a known repo path. Do not use this to list all branches in a repository (use github_enterprise_list_branches instead). Note: the endpoint path uses a partial repo URL parameter; ensure the correct repo identifier is supplied.

        Args:
            page: 
            per_page: 
            repo: 
        Returns:
            API response as a dictionary.
        """
        ...

    def github_enterprise_get_dir(
        self,
        owner: str,
        repoName: str,
    ) -> Dict[str, Any]:
        """Retrieves the contents of the root directory (or a specified path) within a GitHub Enterprise repository, identified by owner and repository name. Use this when you need to list files and subdirectories at a specific path in a repository. Do not use this to retrieve raw file contents (use github_enterprise_get_blob_from_hash) or the full recursive file tree (use github_enterprise_get_repo_content). Returns file names, types, sizes, and download URLs.

        Args:
            owner: The owner (username or organization) of the GitHub repository. (required)
            repoName: The name of the GitHub repository. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def github_enterprise_get_latest_commit_sha(
        self,
        branchName: str,
        owner: str,
        repoName: str,
    ) -> Dict[str, Any]:
        """Retrieves the SHA of the latest commit on a specified branch in a GitHub Enterprise repository by resolving the branchs HEAD Git reference. Use this as the first step in a low-level Git write workflow to obtain the current commit SHA before creating a new tree or commit. Do not use this to get full commit details (use github_enterprise_get_tree_sha_base_commit with the returned SHA). Returns the resolved SHA string for the branch tip.

        Args:
            branchName:  (required)
            owner: The owner or organization of the repository. (required)
            repoName: The name of the repository. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def github_enterprise_get_repo_content(
        self,
        id: str,
        ref: str,
        recursive: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Retrieves the Git tree (file and directory structure) of a GitHub Enterprise repository at a specified ref (branch, tag, or commit SHA). Use this when you need a recursive or top-level view of the repositorys file tree. Do not use this to retrieve the raw contents of a single file (use github_enterprise_get_blob_from_hash or github_enterprise_get_repo_data instead). Returns a list of tree entries including paths, types, and SHAs.

        Args:
            id: ID parameter for the GitHub API request. (required)
            ref: Repository Identifier. (required)
            recursive: Setting this parameter to any value returns the objects or subtrees referenced by the tree specified in :tree_sha. For example, setting recursive to any of the following will enable returning objects or subtrees: 0, 1, true, and false. Omit this parameter to prevent recursively returning objects or subtrees.
        Returns:
            API response as a dictionary.
        """
        ...

    def github_enterprise_get_repo_data(
        self,
        owner: str,
        path: str,
        repoName: str,
    ) -> Dict[str, Any]:
        """Retrieves the contents of a specific file or directory at a given path within a GitHub Enterprise repository, identified by owner, repository name, and path. Use this when you need the decoded content of a single file at a known path. Do not use this to list all files in the repository tree (use github_enterprise_get_repo_content) or to retrieve a blob by SHA (use github_enterprise_get_blob_from_hash). Returns file content, encoding, size, and the files SHA.

        Args:
            owner: The owner (user or organization) of the repository. (required)
            path: The path to the resource within the repository. (required)
            repoName: The name of the repository. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def github_enterprise_get_tree_sha_base_commit(
        self,
        baseCommitSha: str,
        owner: str,
        repoName: str,
    ) -> Dict[str, Any]:
        """Retrieves the Git commit object for a specified commit SHA in a GitHub Enterprise repository, including the tree SHA it points to. Use this to obtain the tree SHA of a base commit before creating a new tree (github_enterprise_create_tree) in a low-level Git write workflow. Do not use this to get the latest commit SHA for a branch (use github_enterprise_get_latest_commit_sha). Returns commit metadata including tree SHA, author, message, and parent commits.

        Args:
            baseCommitSha: SHA of the base commit for the Github repository. (required)
            owner: Owner (username or organization) of the Github repository. (required)
            repoName: Name of the Github repository. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def github_enterprise_list_branches(
        self,
        owner: str,
        repoName: str,
    ) -> Dict[str, Any]:
        """Lists all branches in a specified GitHub Enterprise repository, identified by owner and repository name. Use this when you need an overview of all branches in a repository, such as to enumerate active development lines or check branch existence. Do not use this to retrieve details of a single specific branch (use github_enterprise_get_branch instead). Returns branch names and their associated commit SHAs.

        Args:
            owner:  (required)
            repoName:  (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def github_enterprise_list_my_orgs(
        self,
    ) -> Dict[str, Any]:
        """Lists all GitHub Enterprise organizations associated with the currently authenticated account. Use this when you need to discover which organizations the authenticated user belongs to, for example before fetching organization-scoped repositories. Do not use this to list organizations for another user. Requires a valid authenticated session or OAuth token.
        Returns:
            API response as a dictionary.
        """
        ...

    def github_enterprise_list_my_repositories(
        self,
        page: Optional[str] = None,
        per_page: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Lists all GitHub Enterprise repositories owned by the currently authenticated user. Use this when you need to enumerate the personal repositories of the logged-in user. Do not use this to list repositories for an organization (use github_enterprise_list_repositories_from_org) or for another user by username (use github_enterprise_list_repositories). Requires authentication.

        Args:
            page: 
            per_page: 
        Returns:
            API response as a dictionary.
        """
        ...

    def github_enterprise_list_repositories(
        self,
        org: str,
        page: Optional[str] = None,
        per_page: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Lists all GitHub Enterprise repositories associated with a specified user account, identified by username or organization handle. Use this when you need to enumerate public repositories for a given user. Do not use this to list the authenticated users own repositories (use github_enterprise_list_my_repositories) or organization repositories (use github_enterprise_list_repositories_from_org). Returns repository metadata including names, visibility, and URLs.

        Args:
            org: The name of the GitHub organization. (required)
            page: The page number for pagination.
            per_page: The number of items per page for pagination.
        Returns:
            API response as a dictionary.
        """
        ...

    def github_enterprise_list_repositories_from_org(
        self,
        orgId: Optional[str] = None,
        page: Optional[str] = None,
        per_page: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Lists all repositories belonging to a specific GitHub Enterprise organization, identified by organization ID. Use this when you need to enumerate repositories under an organization account. Do not use this to list repositories for a personal user account (use github_enterprise_list_repositories instead) or for the authenticated users own repos (use github_enterprise_list_my_repositories instead).

        Args:
            orgId: 
            page: 
            per_page: 
        Returns:
            API response as a dictionary.
        """
        ...

    def github_enterprise_update_branch(
        self,
        branchName: str,
        force: bool,
        owner: str,
        repoName: str,
        sha: str,
    ) -> Dict[str, Any]:
        """Updates the HEAD reference of a specified branch in a GitHub Enterprise repository to point to a new commit SHA, effectively advancing or force-updating the branch. Use this after creating a commit (github_enterprise_create_commit) to publish changes to a branch. Do not use this to create a new branch (use github_enterprise_create_reference). Force-updating a branch rewrites its history and may cause data loss for collaborators who have based work on the previous tip; use with caution.

        Args:
            branchName:  (required)
            force: Force the merge operation (true/false). (required)
            owner: Github username or organization name of the repository owner. (required)
            repoName: Name of the repository. (required)
            sha: SHA of the commit to merge. (required)
        Returns:
            API response as a dictionary.
        """
        ...

