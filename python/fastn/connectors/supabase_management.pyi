"""Fastn Supabase Management connector — auto-generated type stubs.

Do not edit manually. Regenerate with `fastn connector sync`.
"""
from __future__ import annotations

from typing import Any, Dict, List, Optional, TypedDict


class _SupabaseManagementCreateProjectRegionSelection(TypedDict, total=False):
    code: str
    type: str

class _SupabaseManagementDeployFunctionMetadata(TypedDict, total=False):
    entrypoint_path: str
    import_map_path: str
    name: str
    static_patterns: str
    verify_jwt: str

class SupabaseManagementConnector:
    """Supabase Management connector ().

    Provides 21 tools.
    """

    def supabase_management_bulk_update_functions(
        self,
        ref: str,
        body: Optional[List[Any]] = None,
    ) -> Dict[str, Any]:
        """Updates configuration or metadata for multiple Supabase Edge Functions in a single project in one request. Use this when you need to apply the same or varied changes across several functions at once instead of making individual update calls. Do not use this to create new functions or deploy function code — use the create or deploy function tools instead. This operation modifies existing function records and cannot be undone automatically.

        Args:
            ref: Reference point (branch name, tag, or commit SHA) used for the operation, e.g. a git ref or deployment reference. (required)
            body: 
        Returns:
            API response as a dictionary.
        """
        ...

    def supabase_management_create_function(
        self,
        body: str,
        name: str,
        ref: str,
        slug: str,
        entrypoint_path: Optional[str] = None,
        ezbr_sha256: Optional[str] = None,
        import_map: Optional[str] = None,
        import_map_path: Optional[bool] = None,
        verify_jwt: Optional[bool] = None,
    ) -> Dict[str, Any]:
        """Creates a new Edge Function record within a Supabase project. Use this when you need to register a new function before deploying its code. Do not use this to update an existing function — use the update function tool instead. After creation, use the deploy function tool to push the function code and make it invocable.

        Args:
            body: The primary content or code of the function/resource (for example, source code or configuration payload). (required)
            name: The name of the resource or function to create or update. (required)
            ref: Reference identifier (for example a branch, commit hash, or deployment reference) relevant to the operation. (required)
            slug: A unique slug used to identify the resource within the Supabase project. (required)
            entrypoint_path: Path to the function's entrypoint file used during deployment or execution.
            ezbr_sha256: SHA-256 hash value used for integrity checks or verification within the deployment process.
            import_map: Import map content or reference used when deploying or configuring functions.
            import_map_path: Flag indicating whether import_map refers to a file path (true) or inline content (false).
            verify_jwt: Whether to enable JWT verification for the deployed function or resource.
        Returns:
            API response as a dictionary.
        """
        ...

    def supabase_management_create_organization(
        self,
        name: str,
    ) -> Dict[str, Any]:
        """Creates a new Supabase organization that can own projects and members. Use this when you need to set up a new organizational unit under the authenticated account. Do not use this to update an existing organization — no update organization tool is available; use the Supabase dashboard instead. Organization creation is immediate and the new org will be available for project creation right away.

        Args:
            name: The name of the resource (for example, a record or entity) relevant to the Supabase operation. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def supabase_management_create_project(
        self,
        db_pass: str,
        name: str,
        organization_slug: str,
        region: str,
        desired_instance_size: Optional[str] = None,
        kps_enabled: Optional[bool] = None,
        organization_id: Optional[str] = None,
        plan: Optional[str] = None,
        postgres_engine: Optional[str] = None,
        region_selection: Optional[_SupabaseManagementCreateProjectRegionSelection] = None,
        release_channel: Optional[str] = None,
        template_url: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Creates a new Supabase project under a specified organization, provisioning a Postgres database and associated services. Use this when you need to set up a new project from scratch. Do not use this to update an existing project — use the update project tool instead. Project creation provisions cloud resources and may take a short time to complete; the project will not be immediately ready for use upon return.

        Args:
            db_pass: Password for the default database user (for example, the 'postgres' user's password). Required when provisioning a database. (required)
            name: The human-readable name for the Supabase project or instance. (required)
            organization_slug: The slug (URL-friendly identifier) of the organization that will own the project. (required)
            region: Geographic region where the project will be hosted (for example, 'us-east-1'). (required)
            desired_instance_size: Requested instance size or tier for the database (for example, 'db-small', 'db-medium').
            kps_enabled: Whether the Key Provider Service (KPS) is enabled for the project.
            organization_id: The unique identifier (UUID) of the organization under which the project will be created.
            plan: Subscription plan or tier for the project (for example, 'free', 'pro', or a custom plan identifier).
            postgres_engine: Postgres engine/version to use for the database (for example, '13', '14').
            region_selection: Structured region selection specifying how the region is chosen and its code.
            release_channel: Release channel for updates and upgrades (for example, 'stable' or 'beta').
            template_url: URL to a project template or configuration that should be used to initialize the project.
        Returns:
            API response as a dictionary.
        """
        ...

    def supabase_management_delete_function(
        self,
        function_slug: str,
        ref: str,
    ) -> Dict[str, Any]:
        """Permanently deletes a specific Edge Function from a Supabase project identified by its function slug. Use this when you need to remove a function that is no longer needed. Do not use this if you only want to disable or pause a function — this action is irreversible and the function definition and deployment will be permanently lost. Confirm the correct project ref and function slug before calling.

        Args:
            function_slug: The slug (identifier) of the function within the specified Supabase project. (required)
            ref: The unique project reference (ref) that identifies the Supabase project. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def supabase_management_delete_project(
        self,
        ref: str,
    ) -> Dict[str, Any]:
        """Permanently deletes a Supabase project and all of its associated resources, including the database, functions, and configuration. Use this only when you need to fully remove a project. Do not use this if you only want to suspend the project temporarily — use the pause project tool instead. This action is irreversible; all project data will be lost and cannot be recovered.

        Args:
            ref: The project ref (unique identifier) of the Supabase project used by the Management API. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def supabase_management_deploy_function(
        self,
        file: str,
        function_slug: str,
        metadata: _SupabaseManagementDeployFunctionMetadata,
        ref: str,
        slug: str,
        bundleOnly: Optional[bool] = None,
    ) -> Dict[str, Any]:
        """Deploys the code bundle for a specific Edge Function to a Supabase project, making it live and invocable. Use this when you need to push new or updated function source code to an existing function slot. Do not use this to create a brand-new function record — use the create function tool first, then deploy. Deploying overwrites the currently active function code and takes effect immediately.

        Args:
            file: The file contents or reference (for example, a base64-encoded bundle or file path) for the function or resource being managed. (required)
            function_slug: The slug identifier of the function within the Supabase project. (required)
            metadata: Function or resource metadata and configuration used by Supabase Management. (required)
            ref: Repository reference, branch, or version to use for the operation. (required)
            slug: The unique slug identifying the Supabase project or resource targeted by this request. (required)
            bundleOnly: If true, restricts the operation to bundle-only behavior (affects what is returned or processed).
        Returns:
            API response as a dictionary.
        """
        ...

    def supabase_management_get_function(
        self,
        function_slug: str,
        ref: str,
    ) -> Dict[str, Any]:
        """Retrieves the metadata and configuration details of a single Edge Function in a Supabase project, including its name, slug, status, and settings. Use this when you need to inspect a specific functions configuration. Do not use this to retrieve the functions source code — use the get function body tool instead, and do not use this to list all functions — use the list functions tool instead.

        Args:
            function_slug: The slug (identifier) of the Supabase function or resource being targeted. (required)
            ref: The unique project reference (ref) identifying the Supabase project. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def supabase_management_get_function_body(
        self,
        function_slug: str,
        ref: str,
    ) -> Dict[str, Any]:
        """Retrieves the raw source code body of a specific Edge Function from a Supabase project. Use this when you need to inspect or audit the current deployed code of a function. Do not use this to get function metadata such as name or settings — use the get function tool instead.

        Args:
            function_slug: The slug (unique name) of the Supabase function being targeted. (required)
            ref: The unique project reference (ref) identifier for the Supabase project. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def supabase_management_get_organization(
        self,
        slug: str,
    ) -> Dict[str, Any]:
        """Retrieves the configuration and metadata details of a single Supabase organization identified by its slug. Use this when you need to inspect a specific organizations name, plan, or settings. Do not use this to list all organizations — use the list organizations tool instead, and do not use this to retrieve organization members — use the list organization members tool instead.

        Args:
            slug: The project's unique ref/slug used as the path segment for the Supabase API base URL. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def supabase_management_get_project(
        self,
        ref: str,
    ) -> Dict[str, Any]:
        """Retrieves the configuration and metadata details of a single Supabase project identified by its ref. Use this when you need to inspect a specific projects status, region, or settings. Do not use this to list all projects — use the list projects tool instead.

        Args:
            ref: Reference path or endpoint segment used in the Supabse URL (for example a table name or resource path). (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def supabase_management_invoke_function(
        self,
        functionSlug: str,
        projectSlug: str,
        body: Optional[Dict[str, Any]] = None,
    ) -> Dict[str, Any]:
        """Invokes a deployed Supabase Edge Function by its slug within a specific project. Use this when you need to trigger execution of a serverless Edge Function and receive its response. Do not use this to deploy, update, or retrieve function metadata — use the deploy or update function tools instead. Note: the function must already be deployed and active; invoking a non-existent or paused function will result in an error.

        Args:
            functionSlug: The slug (identifier) of the Supabase Edge Function to invoke. (required)
            projectSlug: The slug or unique identifier of the Supabase project. (required)
            body: Payload to send to the Supabase function or API. Contains JSON data specific to the endpoint being called.
        Returns:
            API response as a dictionary.
        """
        ...

    def supabase_management_list_functions(
        self,
        ref: str,
    ) -> Dict[str, Any]:
        """Retrieves a list of all Edge Functions registered in a specific Supabase project. Use this when you need an overview of all functions available in a project, such as for auditing, selection, or bulk operations. Do not use this to retrieve the details or code of a single function — use the get function or get function body tools instead.

        Args:
            ref: The Supabase project reference (ref) used in Management API URLs to identify the target project. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def supabase_management_list_organization_members(
        self,
        slug: str,
    ) -> Dict[str, Any]:
        """Retrieves a list of all members belonging to a specific Supabase organization identified by its slug, including their roles and user details. Use this when you need to audit or display who has access to an organization. Do not use this to retrieve organization-level settings — use the get organization tool instead.

        Args:
            slug: The Supabase project reference (project id or slug) used to construct the project's REST URL (e.g., <project>.supabase.co). (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def supabase_management_list_organization_projects(
        self,
        slug: str,
        limit: Optional[int] = None,
        offset: Optional[int] = None,
        search: Optional[str] = None,
        sort: Optional[str] = None,
        statuses: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Retrieves a list of all Supabase projects belonging to a specific organization identified by its slug. Use this when you need to enumerate all projects under a given organization, such as for auditing or selection purposes. Do not use this to retrieve details of a single project — use the get project tool instead, and do not use this to list projects across all organizations — use the list projects tool instead.

        Args:
            slug: The unique project slug or identifier used in the Supabase Management API URL to target a specific project. (required)
            limit: Maximum number of items to return (pagination limit) represented as a string.
            offset: Pagination offset represented as a string (number of items to skip).
            search: Search term used to filter results (e.g., by name or description).
            sort: Sort criteria for returned results (for example 'created_at.desc' or 'name.asc').
            statuses: Comma-separated list of statuses to filter the results by (e.g., active,inactive).
        Returns:
            API response as a dictionary.
        """
        ...

    def supabase_management_list_organizations(
        self,
    ) -> Dict[str, Any]:
        """Retrieves a list of all Supabase organizations accessible to the authenticated user. Use this when you need to enumerate available organizations, such as to select one for project creation or member management. Do not use this to retrieve details of a single organization — use the get organization tool instead.
        Returns:
            API response as a dictionary.
        """
        ...

    def supabase_management_list_projects(
        self,
    ) -> Dict[str, Any]:
        """Retrieves a list of all Supabase projects accessible to the authenticated user across all organizations. Use this when you need an overview of all available projects, such as for selection or auditing. Do not use this to retrieve details of a single project — use the get project tool instead, and do not use this to list projects scoped to a specific organization — use the list organization projects tool instead.
        Returns:
            API response as a dictionary.
        """
        ...

    def supabase_management_pause_project(
        self,
        ref: str,
    ) -> Dict[str, Any]:
        """Pauses a running Supabase project, suspending its compute resources and making it temporarily inaccessible. Use this to reduce resource usage for inactive projects. Do not use this if the project needs to remain available — use the restore project tool to reverse this action. Pausing will interrupt all active connections and API access to the project until it is restored.

        Args:
            ref: The unique project reference (ref) that identifies the Supabase project to operate on. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def supabase_management_restore_project(
        self,
        ref: str,
    ) -> Dict[str, Any]:
        """Restores a previously paused Supabase project, making it active and accessible again. Use this when a project has been paused (e.g., due to inactivity or manual pause) and needs to be reactivated. Do not use this on a project that is already active — use the get project tool first to verify the projects current status. Restoration may take a short time to complete.

        Args:
            ref: The Supabase project reference (ref) that identifies the target project for the management operation. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def supabase_management_update_function(
        self,
        function_slug: str,
        ref: str,
        body: Optional[str] = None,
        entrypoint_path: Optional[str] = None,
        ezbr_sha256: Optional[str] = None,
        import_map: Optional[bool] = None,
        import_map_path: Optional[str] = None,
        name: Optional[str] = None,
        slug: Optional[str] = None,
        verify_jwt: Optional[bool] = None,
    ) -> Dict[str, Any]:
        """Updates the configuration or metadata of a single existing Edge Function in a Supabase project, such as its name, import map setting, or verify JWT flag. Use this when you need to change function settings without redeploying its code. Do not use this to deploy new function code — use the deploy function tool instead, and do not use this to create a new function — use the create function tool instead.

        Args:
            function_slug: Slug identifier for the function being targeted by this management operation. (required)
            ref: Reference identifier for the target resource (for example, a git ref, deployment ref, or environment ref). (required)
            body: Raw body content for the request, such as function source code, configuration JSON, or other payload data.
            entrypoint_path: Path to the function's entrypoint file (e.g., index.js or main.py) within the uploaded bundle.
            ezbr_sha256: SHA-256 checksum (ezbr) used to validate the integrity of the uploaded artifact or bundle.
            import_map: Whether to import an import_map configuration when deploying or updating a function.
            import_map_path: Filesystem or repository path to the import_map file to be used during function deployment.
            name: Name provided in the request body, used to set or update the resource's human-readable name.
            slug: Unique slug identifier for the resource; often used as a stable identifier for functions or other managed objects.
            verify_jwt: Indicates whether JWT verification should be enabled in the request payload (body-level setting).
        Returns:
            API response as a dictionary.
        """
        ...

    def supabase_management_update_project(
        self,
        name: str,
        ref: str,
    ) -> Dict[str, Any]:
        """Updates the configuration or metadata of an existing Supabase project, such as its name or settings. Use this when you need to modify project-level properties. Do not use this to pause or restore a project — use the dedicated pause or restore project tools instead, and do not use this to delete a project — use the delete project tool.

        Args:
            name: The name of the resource (for example, project or organization) to create or manage. (required)
            ref: A reference identifier (for example, project ref or branch ref) used by the endpoint. (required)
        Returns:
            API response as a dictionary.
        """
        ...

