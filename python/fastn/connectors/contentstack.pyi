"""Fastn Contentstack connector — auto-generated type stubs.

Do not edit manually. Regenerate with `fastn connector sync`.
"""
from __future__ import annotations

from typing import Any, Dict, List, Optional, TypedDict


class _ContentStackCreateBranchBranch(TypedDict, total=False):
    source: str
    uid: str

class _ContentStackCreateContentTypeContentType(TypedDict, total=False):
    options: Dict[str, Any]
    schema: List[Any]
    title: str
    uid: str

class _ContentStackCreateContentTypeWithCustomAssetFieldContentType(TypedDict, total=False):
    _version: int
    inbuilt_class: bool
    options: Dict[str, Any]
    schema: List[Any]
    title: str
    uid: str

class _ContentStackCreateContentTypeWithJsonRteContentType(TypedDict, total=False):
    options: Dict[str, Any]
    schema: List[Any]
    title: str
    uid: str

class _ContentStackCreateContentTypeWithSelectFieldContentType(TypedDict, total=False):
    options: Dict[str, Any]
    schema: List[Any]
    title: str
    uid: str

class _ContentStackCreateContentTypeWithTaxonomyContentType(TypedDict, total=False):
    schema: List[Any]
    title: str
    uid: str

class _ContentStackCreateContentTypeWithTaxonomyOptions(TypedDict, total=False):
    is_page: bool
    singleton: bool
    sub_title: List[Any]
    title: str

class _ContentStackCreateEntryEntry(TypedDict, total=False):
    title: str
    url: str

class _ContentStackCreateEntryMasterLocaleEntry(TypedDict, total=False):
    tags: List[Any]
    title: str
    url: str

class _ContentStackCreateEntryWithCustomAssetFieldEntry(TypedDict, total=False):
    asset_field: Dict[str, Any]
    tags: List[Any]
    title: str

class _ContentStackCreateEntryWithJsonRteEntry(TypedDict, total=False):
    json_rte: Dict[str, Any]
    title: str
    url: str

class _ContentStackCreateEnvironmentEnvironment(TypedDict, total=False):
    name: str
    urls: List[Any]

class _ContentStackCreateLanguageLocale(TypedDict, total=False):
    code: str
    fallback_locale: str
    name: str

class _ContentStackCreateReleaseRelease(TypedDict, total=False):
    archived: bool
    description: str
    locked: bool
    name: str

class _ContentStackCreateRoleRole(TypedDict, total=False):
    api_key: str
    description: str
    name: str
    org_uid: str
    rules: List[Any]
    uid: str
    users: List[Any]

class _ContentStackCreateTaxonomyTaxonomy(TypedDict, total=False):
    description: str
    name: str
    uid: str

class _ContentStackCreateWebhookWebhook(TypedDict, total=False):
    branches: List[Any]
    channels: List[Any]
    concise_payload: bool
    destinations: List[Any]
    disabled: bool
    name: str
    notifiers: str
    retry_policy: str

class _ContentStackCreateWorkflowWorkflow(TypedDict, total=False):
    admin_users: Dict[str, Any]
    branches: List[Any]
    content_types: List[Any]
    enabled: bool
    name: str
    workflow_stages: List[Any]

class _ContentStackSetFallbackLanguageLocale(TypedDict, total=False):
    code: str
    fallback_locale: str
    name: str

class _ContentStackUpdateContentTypeContentType(TypedDict, total=False):
    options: Dict[str, Any]
    schema: List[Any]
    title: str
    uid: str

class _ContentStackUpdateEntryEntry(TypedDict, total=False):
    taxonomies: List[Any]
    title: str
    url: str

class _ContentStackUpdateEntryWithJsonRteEntry(TypedDict, total=False):
    json_rte: Dict[str, Any]
    title: str
    url: str

class _ContentStackUpdateEnvironmentEnvironment(TypedDict, total=False):
    name: str
    urls: List[Any]

class _ContentStackUpdateLanguageLocale(TypedDict, total=False):
    fallback_locale: str
    name: str

class _ContentStackUpdateReleaseRelease(TypedDict, total=False):
    description: str
    name: str

class _ContentStackUpdateRoleRole(TypedDict, total=False):
    api_key: str
    description: str
    name: str
    org_uid: str
    rules: List[Any]
    uid: str
    users: List[Any]

class _ContentStackUpdateTaxonomyTaxonomy(TypedDict, total=False):
    description: str
    name: str

class _ContentStackUpdateWebhookWebhook(TypedDict, total=False):
    branches: List[Any]
    channels: List[Any]
    concise_payload: bool
    destinations: List[Any]
    disabled: bool
    name: str
    notifiers: str
    retry_policy: str

class _ContentStackUpdateWorkflowWorkflow(TypedDict, total=False):
    admin_users: Dict[str, Any]
    branches: List[Any]
    content_types: List[Any]
    enabled: bool
    name: str
    workflow_stages: List[Any]

class ContentstackConnector:
    """Contentstack connector ().

    Provides 93 tools.
    """

    def content_stack_compare_content_type_between_branches(
        self,
        base_branch: Optional[str] = None,
        compare_branch: Optional[str] = None,
        contenttypeUid: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Compares a specific content type schema between two branches in Contentstack, identified by content type UID. Returns the differences in field definitions between the branches. Use this before merging branches to identify schema conflicts. To compare all content types, use content_stack_compare_content_types_between_branches instead.

        Args:
            base_branch: 
            compare_branch: 
            contenttypeUid: 
        Returns:
            API response as a dictionary.
        """
        ...

    def content_stack_compare_content_types_between_branches(
        self,
        compare_branch: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Compares all content type schemas between two branches in Contentstack. Returns a diff of content type definitions to identify structural changes before merging. Use this for a broad branch comparison. To compare a single content type, use content_stack_compare_content_type_between_branches instead.

        Args:
            compare_branch: 
        Returns:
            API response as a dictionary.
        """
        ...

    def content_stack_compare_global_fields_between_branches(
        self,
        compare_branch: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Compares global field definitions between two branches in Contentstack. Returns differences in global field schemas across branches. Use this before merging branches to identify global field conflicts. To compare content types, use content_stack_compare_content_types_between_branches instead.

        Args:
            compare_branch: 
        Returns:
            API response as a dictionary.
        """
        ...

    def content_stack_create_branch(
        self,
        branch: Optional[_ContentStackCreateBranchBranch] = None,
    ) -> Dict[str, Any]:
        """Creates a new branch in the Contentstack stack to enable parallel content or schema development. Use this to set up isolated development, testing, or staging environments. To delete a branch, use content_stack_delete_branch. To list existing branches, use content_stack_list_branches.

        Args:
            branch: 
        Returns:
            API response as a dictionary.
        """
        ...

    def content_stack_create_content_type(
        self,
        content_type: Optional[_ContentStackCreateContentTypeContentType] = None,
    ) -> Dict[str, Any]:
        """Creates a new standard content type in the Contentstack stack with the specified field schema. Use this for general-purpose content type creation. For content types requiring specialized fields such as taxonomy, JSON RTE, custom assets, or select fields, use the appropriate variant create tools instead.

        Args:
            content_type: 
        Returns:
            API response as a dictionary.
        """
        ...

    def content_stack_create_content_type_with_custom_asset_field(
        self,
        content_type: Optional[_ContentStackCreateContentTypeWithCustomAssetFieldContentType] = None,
    ) -> Dict[str, Any]:
        """Creates a new content type in the Contentstack stack that includes a custom asset field. Use this when the content type schema requires a custom asset reference. For standard content types, use content_stack_create_content_type instead.

        Args:
            content_type: 
        Returns:
            API response as a dictionary.
        """
        ...

    def content_stack_create_content_type_with_json_rte(
        self,
        content_type: Optional[_ContentStackCreateContentTypeWithJsonRteContentType] = None,
    ) -> Dict[str, Any]:
        """Creates a new content type in the Contentstack stack that includes a JSON Rich Text Editor (RTE) field. Use this when the content type schema requires structured rich text. For standard content types without JSON RTE, use content_stack_create_content_type instead.

        Args:
            content_type: 
        Returns:
            API response as a dictionary.
        """
        ...

    def content_stack_create_content_type_with_select_field(
        self,
        content_type: Optional[_ContentStackCreateContentTypeWithSelectFieldContentType] = None,
    ) -> Dict[str, Any]:
        """Creates a new content type in the Contentstack stack that includes a select (dropdown) field. Use this when the content type schema requires a predefined set of selectable options. For standard content types without select fields, use content_stack_create_content_type instead.

        Args:
            content_type: 
        Returns:
            API response as a dictionary.
        """
        ...

    def content_stack_create_content_type_with_taxonomy(
        self,
        content_type: Optional[_ContentStackCreateContentTypeWithTaxonomyContentType] = None,
        options: Optional[_ContentStackCreateContentTypeWithTaxonomyOptions] = None,
    ) -> Dict[str, Any]:
        """Creates a new content type in the Contentstack stack that includes taxonomy field integration. Use this when the content type schema needs to classify entries using Contentstack taxonomies. For content types without taxonomy, use content_stack_create_content_type instead.

        Args:
            content_type: 
            options: 
        Returns:
            API response as a dictionary.
        """
        ...

    def content_stack_create_entry(
        self,
        contenttypeUid: Optional[str] = None,
        entry: Optional[_ContentStackCreateEntryEntry] = None,
    ) -> Dict[str, Any]:
        """Creates a new standard content entry for a specified Contentstack content type, identified by content type UID. Use this for general-purpose entry creation without specialized field types. For entries requiring JSON RTE fields, use content_stack_create_entry_with_json_rte. For entries with custom asset fields, use content_stack_create_entry_with_custom_asset_field.

        Args:
            contenttypeUid: 
            entry: 
        Returns:
            API response as a dictionary.
        """
        ...

    def content_stack_create_entry_master_locale(
        self,
        contenttypeUid: Optional[str] = None,
        copy_to_master: Optional[str] = None,
        entry: Optional[_ContentStackCreateEntryMasterLocaleEntry] = None,
    ) -> Dict[str, Any]:
        """Creates a new content entry in the master locale for a specified Contentstack content type, identified by content type UID. Use this when explicitly creating content in the stacks primary language. For localized entries or entries with specialized field types such as JSON RTE, use the appropriate variant create tools.

        Args:
            contenttypeUid: 
            copy_to_master: 
            entry: 
        Returns:
            API response as a dictionary.
        """
        ...

    def content_stack_create_entry_with_custom_asset_field(
        self,
        contenttypeUid: Optional[str] = None,
        entry: Optional[_ContentStackCreateEntryWithCustomAssetFieldEntry] = None,
    ) -> Dict[str, Any]:
        """Creates a new content entry for a specified content type in Contentstack that includes a custom asset field, identified by content type UID. Use this when the content type schema includes a custom asset reference field. For standard entries without custom asset fields, use content_stack_create_entry instead.

        Args:
            contenttypeUid: 
            entry: 
        Returns:
            API response as a dictionary.
        """
        ...

    def content_stack_create_entry_with_json_rte(
        self,
        contenttypeUid: Optional[str] = None,
        entry: Optional[_ContentStackCreateEntryWithJsonRteEntry] = None,
    ) -> Dict[str, Any]:
        """Creates a new content entry that includes a JSON Rich Text Editor (RTE) field for a specified Contentstack content type, identified by content type UID. Use this when the content type schema includes a JSON RTE field. For standard entries, use content_stack_create_entry instead.

        Args:
            contenttypeUid: 
            entry: 
        Returns:
            API response as a dictionary.
        """
        ...

    def content_stack_create_environment(
        self,
        environment: Optional[_ContentStackCreateEnvironmentEnvironment] = None,
    ) -> Dict[str, Any]:
        """Creates a new publishing environment in the Contentstack stack with the specified name and URL configuration. Use this to set up a new deployment target such as staging or production. To update an existing environment, use content_stack_update_environment instead.

        Args:
            environment: 
        Returns:
            API response as a dictionary.
        """
        ...

    def content_stack_create_language(
        self,
        locale: Optional[_ContentStackCreateLanguageLocale] = None,
    ) -> Dict[str, Any]:
        """Adds a new locale (language) to the Contentstack stack. Use this to enable content localization for a new language. To set a fallback for a locale, use content_stack_set_fallback_language instead. To update an existing locale, use content_stack_update_language instead.

        Args:
            locale: 
        Returns:
            API response as a dictionary.
        """
        ...

    def content_stack_create_release(
        self,
        release: Optional[_ContentStackCreateReleaseRelease] = None,
    ) -> Dict[str, Any]:
        """Creates a new release in the Contentstack stack to group entries and assets for coordinated publishing. Use this when you need to bundle content changes for a scheduled or coordinated deployment. To update an existing release, use content_stack_update_release instead.

        Args:
            release: 
        Returns:
            API response as a dictionary.
        """
        ...

    def content_stack_create_role(
        self,
        role: Optional[_ContentStackCreateRoleRole] = None,
    ) -> Dict[str, Any]:
        """Creates a new role in the Contentstack stack with specified permissions. Use this to define a new set of access controls for users. Note: the underlying endpoint uses DELETE /v3/roles — verify this is correct before use, as it may indicate a misconfiguration. To update an existing role, use content_stack_update_role instead.

        Args:
            role: 
        Returns:
            API response as a dictionary.
        """
        ...

    def content_stack_create_taxonomy(
        self,
        taxonomy: Optional[_ContentStackCreateTaxonomyTaxonomy] = None,
    ) -> Dict[str, Any]:
        """Creates a new taxonomy in the Contentstack stack for organizing and classifying content entries. Use this to define a new term hierarchy. To update an existing taxonomy, use content_stack_update_taxonomy instead.

        Args:
            taxonomy: 
        Returns:
            API response as a dictionary.
        """
        ...

    def content_stack_create_team(
        self,
        name: Optional[str] = None,
        organizationId: Optional[str] = None,
        organizationRole: Optional[str] = None,
        stackRoleMapping: Optional[List[Any]] = None,
        users: Optional[List[Any]] = None,
    ) -> Dict[str, Any]:
        """Creates a new team within a Contentstack organization, identified by organization ID. Use this to group users for shared role-based access. To update an existing team, use content_stack_update_team instead.

        Args:
            name: 
            organizationId: 
            organizationRole: 
            stackRoleMapping: 
            users: 
        Returns:
            API response as a dictionary.
        """
        ...

    def content_stack_create_webhook(
        self,
        webhook: Optional[_ContentStackCreateWebhookWebhook] = None,
    ) -> Dict[str, Any]:
        """Creates a new webhook in the Contentstack stack with the specified URL, triggers, and channel configuration. Use this when you need to set up a new event-driven integration. To update an existing webhook, use content_stack_update_webhook instead.

        Args:
            webhook: 
        Returns:
            API response as a dictionary.
        """
        ...

    def content_stack_create_workflow(
        self,
        workflow: Optional[_ContentStackCreateWorkflowWorkflow] = None,
    ) -> Dict[str, Any]:
        """Creates a new workflow in the Contentstack stack with the specified stages and configuration. Use this when you need to define a new content approval or publishing pipeline. To update an existing workflow, use content_stack_update_workflow or content_stack_create_or_update_workflow_details instead.

        Args:
            workflow: 
        Returns:
            API response as a dictionary.
        """
        ...

    def content_stack_delete_branch(
        self,
        force: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Permanently deletes a specific branch from the Contentstack stack. This action is irreversible — all content and schema changes unique to this branch will be lost. Use with caution and ensure the branch has been merged or is no longer needed. To create a branch, use content_stack_create_branch instead.

        Args:
            force: 
        Returns:
            API response as a dictionary.
        """
        ...

    def content_stack_delete_content_type(
        self,
        contentUid: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Permanently deletes a specific content type from the Contentstack stack, identified by its content UID. This action is irreversible — all entries of this content type and the type definition itself will be removed. To update a content type instead, use content_stack_update_content_type.

        Args:
            contentUid: 
        Returns:
            API response as a dictionary.
        """
        ...

    def content_stack_delete_entry(
        self,
        contenttypeUid: Optional[str] = None,
        entryUid: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Permanently deletes a specific content entry from a Contentstack content type, identified by content type UID and entry UID. This action is irreversible — the entry and all its locale variants will be removed. To update an entry instead, use content_stack_update_entry.

        Args:
            contenttypeUid: 
            entryUid: 
        Returns:
            API response as a dictionary.
        """
        ...

    def content_stack_delete_environment(
        self,
        enviromentName: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Permanently deletes a specific publishing environment from the Contentstack stack, identified by its environment name. This action is irreversible — published content targeting this environment may become inaccessible. To modify an environment instead, use content_stack_update_environment.

        Args:
            enviromentName: 
        Returns:
            API response as a dictionary.
        """
        ...

    def content_stack_delete_language(
        self,
        languageCode: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Permanently deletes a specific locale (language) from the Contentstack stack, identified by its language code. This action is irreversible — localized content for this locale may no longer be accessible. Use with caution. To modify locale settings instead, use content_stack_update_language.

        Args:
            languageCode: 
        Returns:
            API response as a dictionary.
        """
        ...

    def content_stack_delete_release(
        self,
        releaseId: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Permanently deletes a specific release from the Contentstack stack, identified by its release ID. This action is irreversible — all items queued in this release will be removed along with the release itself. To modify a release instead, use content_stack_update_release.

        Args:
            releaseId: 
        Returns:
            API response as a dictionary.
        """
        ...

    def content_stack_delete_role(
        self,
        roleId: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Permanently deletes a specific role from the Contentstack stack, identified by its role ID. This action is irreversible — users assigned to this role will lose the associated permissions. Do not use this to delete organization-level roles. To modify a role instead, use content_stack_update_role.

        Args:
            roleId: 
        Returns:
            API response as a dictionary.
        """
        ...

    def content_stack_delete_taxonomy(
        self,
        force: Optional[str] = None,
        taxonomyUid: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Permanently deletes a specific taxonomy from the Contentstack stack, identified by its taxonomy UID. This action is irreversible — all terms and associations within the taxonomy will be removed. To modify a taxonomy instead, use content_stack_update_taxonomy.

        Args:
            force: 
            taxonomyUid: 
        Returns:
            API response as a dictionary.
        """
        ...

    def content_stack_delete_team(
        self,
        organizationId: Optional[str] = None,
        teamId: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Permanently deletes a specific team from a Contentstack organization, identified by organization ID and team ID. This action is irreversible — all team memberships and associated permissions will be removed. To modify a team instead, use content_stack_update_team.

        Args:
            organizationId: 
            teamId: 
        Returns:
            API response as a dictionary.
        """
        ...

    def content_stack_delete_webhook(
        self,
        webhookId: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Permanently deletes a specific webhook from Contentstack, identified by its webhook ID. This action is irreversible — the webhook will stop firing and cannot be recovered. Use this only when the webhook is no longer needed. To modify a webhook instead, use content_stack_update_webhook.

        Args:
            webhookId: 
        Returns:
            API response as a dictionary.
        """
        ...

    def content_stack_delete_workflow(
        self,
        workflowId: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Permanently deletes a specific workflow from Contentstack, identified by its workflow ID. This action is irreversible — the workflow and all its stage configurations will be removed. Use this only when the workflow is no longer needed. To deactivate without deleting, use content_stack_disable_workflow instead.

        Args:
            workflowId: 
        Returns:
            API response as a dictionary.
        """
        ...

    def content_stack_disable_workflow(
        self,
        workflowId: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Disables a specific workflow in Contentstack, identified by its workflow ID, preventing it from being applied to content entries. Use this to temporarily deactivate a workflow without deleting it. To permanently remove a workflow, use content_stack_delete_workflow instead.

        Args:
            workflowId: 
        Returns:
            API response as a dictionary.
        """
        ...

    def content_stack_enable_workflow(
        self,
        workflowId: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Enables a specific workflow in Contentstack, identified by its workflow ID, making it active for use on content entries. Use this to activate a previously disabled or newly created workflow. Do not use this to create a workflow — use content_stack_create_workflow instead. This action changes the workflows active state.

        Args:
            workflowId: 
        Returns:
            API response as a dictionary.
        """
        ...

    def content_stack_export_content_type(
        self,
        content_type_uid: str,
        contentUid: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Exports a specific content type schema from the Contentstack stack as a downloadable file, identified by its content UID. Use this to back up or migrate content type definitions between stacks. This is a read-only operation with no side effects.

        Args:
            content_type_uid:  (required)
            contentUid: 
        Returns:
            API response as a dictionary.
        """
        ...

    def content_stack_export_taxonomy(
        self,
        taxonomyUid: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Exports a specific taxonomy from the Contentstack stack as a downloadable file, identified by its taxonomy UID. Use this to back up or migrate taxonomy structures between stacks. This is a read-only operation with no side effects.

        Args:
            taxonomyUid: 
        Returns:
            API response as a dictionary.
        """
        ...

    def content_stack_export_webhook(
        self,
        webhookId: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Exports the configuration of a specific webhook from Contentstack as a downloadable file, identified by its webhook ID. Use this to back up or migrate webhook configurations between stacks. This is a read-only operation with no side effects.

        Args:
            webhookId: 
        Returns:
            API response as a dictionary.
        """
        ...

    def content_stack_get_branch(
        self,
    ) -> Dict[str, Any]:
        """Retrieves the details of a specific branch in the Contentstack stack by its branch identifier. Returns branch name, source, and creation metadata. Use this when you need details of a single branch. To retrieve all branches, use content_stack_list_branches instead.
        Returns:
            API response as a dictionary.
        """
        ...

    def content_stack_get_content_type(
        self,
        contentUid: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Retrieves the schema details of a specific content type from the Contentstack Management API, identified by its content UID. Returns field definitions, settings, and metadata. To retrieve all content types, use content_stack_list_content_types. For delivery-focused retrieval, use content_stack_get_content_type_delivery instead.

        Args:
            contentUid: 
        Returns:
            API response as a dictionary.
        """
        ...

    def content_stack_get_content_type_delivery(
        self,
        contentUid: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Retrieves a specific content type schema via the Contentstack Delivery API (CDN), identified by content UID. Use this to fetch content type definitions for front-end or delivery use cases. For management operations, use content_stack_get_content_type (Management API) instead.

        Args:
            contentUid: 
        Returns:
            API response as a dictionary.
        """
        ...

    def content_stack_get_content_type_references(
        self,
    ) -> Dict[str, Any]:
        """Retrieves all references associated with a specific content type (hardcoded to page) in the Contentstack stack. Returns a list of other content types or entries that reference this content type. Use this to understand content dependency graphs before making schema changes.
        Returns:
            API response as a dictionary.
        """
        ...

    def content_stack_get_delivery_entry(
        self,
        contentEntryUid: Optional[str] = None,
        contentTypeUid: Optional[str] = None,
        include_branch: Optional[str] = None,
        include_fallback: Optional[str] = None,
        locale: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Retrieves a specific published content entry via the Contentstack Delivery API (CDN), identified by content type UID and entry UID. Use this to fetch content for front-end rendering or delivery purposes. For management or editing operations, use content_stack_get_entry (Management API) instead.

        Args:
            contentEntryUid: 
            contentTypeUid: 
            include_branch: 
            include_fallback: 
            locale: 
        Returns:
            API response as a dictionary.
        """
        ...

    def content_stack_get_entry(
        self,
        contenttypeUid: Optional[str] = None,
        entryUid: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Retrieves the details of a specific content entry from the Contentstack Management API, identified by content type UID and entry UID. Returns all field values and metadata. Use this for managing or editing entries. To retrieve entries via the Delivery API (CDN), use the delivery-specific get entry tool instead.

        Args:
            contenttypeUid: 
            entryUid: 
        Returns:
            API response as a dictionary.
        """
        ...

    def content_stack_get_environment(
        self,
        enviromentName: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Retrieves the details of a specific publishing environment in Contentstack, identified by its environment name. Returns URLs, associated locales, and deployment settings. Use this when you need details of a specific environment. To retrieve all environments, use content_stack_list_environments instead.

        Args:
            enviromentName: 
        Returns:
            API response as a dictionary.
        """
        ...

    def content_stack_get_language(
        self,
        languageCode: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Retrieves the details of a specific locale (language) in Contentstack, identified by its language code. Returns the locale name, code, and fallback language settings. Use this when you need details of a specific locale. To retrieve all locales, use content_stack_list_languages instead.

        Args:
            languageCode: 
        Returns:
            API response as a dictionary.
        """
        ...

    def content_stack_get_organization(
        self,
        organizationId: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Retrieves the details of a specific Contentstack organization, identified by its organization ID. Returns the organization name, plan, and ownership information. Use this when you need full details of a specific organization. To retrieve all organizations, use content_stack_list_organizations instead.

        Args:
            organizationId: 
        Returns:
            API response as a dictionary.
        """
        ...

    def content_stack_get_organization_log_item(
        self,
        logId: Optional[str] = None,
        organizationId: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Retrieves a specific log item from the audit logs of a Contentstack organization, identified by organization ID and log ID. Use this to inspect a single log event in detail. To retrieve all log items, use content_stack_list_organization_log_details instead.

        Args:
            logId: 
            organizationId: 
        Returns:
            API response as a dictionary.
        """
        ...

    def content_stack_get_publish_queue(
        self,
    ) -> Dict[str, Any]:
        """Retrieves the publish queue in Contentstack, returning a list of pending, in-progress, and completed publish activities for the stack. Use this to monitor content publishing status. This is a read-only operation with no side effects.
        Returns:
            API response as a dictionary.
        """
        ...

    def content_stack_get_release(
        self,
        releaseId: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Retrieves the details of a specific release in Contentstack, identified by its release ID. Returns the release name, description, and status. Use this when you need full details of a specific release. To retrieve all releases, use content_stack_list_releases. To retrieve items within the release, use content_stack_list_release_items instead.

        Args:
            releaseId: 
        Returns:
            API response as a dictionary.
        """
        ...

    def content_stack_get_role(
        self,
        roleId: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Retrieves the details of a specific role in the Contentstack stack, identified by its role ID. Returns the role name, description, and permissions. Use this when you need full details of a specific role. To retrieve all roles, use content_stack_list_roles instead.

        Args:
            roleId: 
        Returns:
            API response as a dictionary.
        """
        ...

    def content_stack_get_taxonomy(
        self,
        taxonomyUid: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Retrieves the details of a specific taxonomy in the Contentstack stack, identified by its taxonomy UID. Returns the taxonomy name, description, and term structure. To retrieve all taxonomies, use content_stack_list_taxonomies instead.

        Args:
            taxonomyUid: 
        Returns:
            API response as a dictionary.
        """
        ...

    def content_stack_get_team(
        self,
        organizationId: Optional[str] = None,
        teamId: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Retrieves the details of a specific team within a Contentstack organization, identified by organization ID and team ID. Returns the team name, description, and membership information. Use this for team-specific details. To retrieve all teams, use content_stack_list_teams instead.

        Args:
            organizationId: 
            teamId: 
        Returns:
            API response as a dictionary.
        """
        ...

    def content_stack_get_webhook(
        self,
        webhookId: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Retrieves the details of a single webhook in Contentstack, identified by its webhook ID. Returns configuration including URL, triggers, and channels. Use this when you need details for a specific webhook. To retrieve all webhooks, use content_stack_list_webhooks instead.

        Args:
            webhookId: 
        Returns:
            API response as a dictionary.
        """
        ...

    def content_stack_get_workflow(
        self,
        workflowId: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Retrieves the details of a single workflow in Contentstack, identified by its workflow ID. Returns stages, transitions, and configuration. Use this when you need full details of a specific workflow. To retrieve all workflows, use content_stack_list_workflows instead.

        Args:
            workflowId: 
        Returns:
            API response as a dictionary.
        """
        ...

    def content_stack_list_aliases(
        self,
    ) -> Dict[str, Any]:
        """Retrieves all branch aliases defined in the Contentstack stack. Returns alias names and their mapped branch targets. Use this to identify which aliases are available before performing branch or alias operations. This is a read-only operation with no side effects.
        Returns:
            API response as a dictionary.
        """
        ...

    def content_stack_list_audit_logs(
        self,
    ) -> Dict[str, Any]:
        """Retrieves the stack-level audit log from Contentstack, returning a list of recorded actions and events for the current stack. Use this to review changes made to content, settings, or users. This is a read-only operation with no side effects.
        Returns:
            API response as a dictionary.
        """
        ...

    def content_stack_list_branches(
        self,
    ) -> Dict[str, Any]:
        """Retrieves all branches available in the Contentstack stack. Returns branch names, UIDs, and creation metadata. Use this to enumerate branches before comparing, merging, or switching between them. To retrieve a single branch, use content_stack_get_branch instead.
        Returns:
            API response as a dictionary.
        """
        ...

    def content_stack_list_content_types(
        self,
    ) -> Dict[str, Any]:
        """Retrieves all content types defined in the Contentstack stack via the Management API. Returns content type UIDs, names, and schema summaries. Use this for content management and schema review tasks. For delivery-focused retrieval, use content_stack_list_content_types_delivery instead.
        Returns:
            API response as a dictionary.
        """
        ...

    def content_stack_list_content_types_delivery(
        self,
        include_count: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Retrieves all content type schemas available via the Contentstack Delivery API (CDN). Use this to enumerate content types for front-end or delivery use cases. For management operations, use content_stack_list_content_types (Management API) instead.

        Args:
            include_count: 
        Returns:
            API response as a dictionary.
        """
        ...

    def content_stack_list_delivery_entries(
        self,
        contentTypeUid: Optional[str] = None,
        include_branch: Optional[str] = None,
        include_fallback: Optional[str] = None,
        locale: Optional[str] = None,
        version: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Retrieves all published content entries for a specified content type via the Contentstack Delivery API (CDN), identified by content type UID. Use this to fetch content for front-end rendering or delivery. For management or editing operations, use content_stack_list_entries (Management API) instead.

        Args:
            contentTypeUid: 
            include_branch: 
            include_fallback: 
            locale: 
            version: 
        Returns:
            API response as a dictionary.
        """
        ...

    def content_stack_list_entries(
        self,
        contenttypeUid: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Retrieves all content entries for a specified Contentstack content type via the Management API, identified by content type UID. Returns a paginated list of entries with their field values. Use this for content management tasks. To retrieve entries via the Delivery API (CDN), use the delivery-specific list entries tool instead.

        Args:
            contenttypeUid: 
        Returns:
            API response as a dictionary.
        """
        ...

    def content_stack_list_environments(
        self,
    ) -> Dict[str, Any]:
        """Retrieves all publishing environments configured in the Contentstack stack. Returns environment names, URLs, and associated locales. Use this to enumerate available environments. To retrieve a single environment, use content_stack_get_environment instead.
        Returns:
            API response as a dictionary.
        """
        ...

    def content_stack_list_languages(
        self,
    ) -> Dict[str, Any]:
        """Retrieves all locales (languages) configured in the Contentstack stack. Returns locale codes, names, and fallback settings. Use this to enumerate available locales. To retrieve a single locale, use content_stack_get_language instead.
        Returns:
            API response as a dictionary.
        """
        ...

    def content_stack_list_merge_jobs(
        self,
    ) -> Dict[str, Any]:
        """Retrieves all branch merge jobs from the Contentstack merge queue. Returns job statuses, source and target branches, and timestamps. Use this to monitor the progress of branch merge operations. This is a read-only operation with no side effects.
        Returns:
            API response as a dictionary.
        """
        ...

    def content_stack_list_organization_invitations(
        self,
        organizationId: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Retrieves all pending and accepted invitations for a Contentstack organization, identified by organization ID. Use this to audit who has been invited to the organization. This is a read-only operation with no side effects.

        Args:
            organizationId: 
        Returns:
            API response as a dictionary.
        """
        ...

    def content_stack_list_organization_log_details(
        self,
        organizationId: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Retrieves the audit log entries for a Contentstack organization, identified by organization ID. Returns a list of log events including user actions and system events. Use this for auditing organization-level activity. To retrieve a single log item, use content_stack_get_organization_log_item instead.

        Args:
            organizationId: 
        Returns:
            API response as a dictionary.
        """
        ...

    def content_stack_list_organizations(
        self,
    ) -> Dict[str, Any]:
        """Retrieves all Contentstack organizations accessible to the authenticated user. Returns organization names and IDs. Use this to identify the correct organization ID before performing organization-specific operations. To retrieve a single organization, use content_stack_get_organization instead.
        Returns:
            API response as a dictionary.
        """
        ...

    def content_stack_list_release_items(
        self,
        releaseId: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Retrieves all items included in a specific Contentstack release, identified by release ID. Returns entry and asset references queued in the release. Use this to review release contents before deployment. To retrieve release metadata, use content_stack_get_release instead.

        Args:
            releaseId: 
        Returns:
            API response as a dictionary.
        """
        ...

    def content_stack_list_releases(
        self,
    ) -> Dict[str, Any]:
        """Retrieves all releases defined in the Contentstack stack. Returns release names, IDs, and statuses. Use this to get an overview of all releases. To retrieve a single release, use content_stack_get_release instead.
        Returns:
            API response as a dictionary.
        """
        ...

    def content_stack_list_roles(
        self,
    ) -> Dict[str, Any]:
        """Retrieves all roles defined in the current Contentstack stack. Returns role names, IDs, and permissions. Use this to get an overview of all stack-level roles. To retrieve organization-level roles, use content_stack_list_roles_in_organization instead. To retrieve a single role, use content_stack_get_role instead.
        Returns:
            API response as a dictionary.
        """
        ...

    def content_stack_list_roles_in_organization(
        self,
        organizationId: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Retrieves all roles defined within a specific Contentstack organization, identified by organization ID. Returns role names, IDs, and permissions. Use this to enumerate organization-level roles. To retrieve stack-level roles, use content_stack_list_roles instead.

        Args:
            organizationId: 
        Returns:
            API response as a dictionary.
        """
        ...

    def content_stack_list_stack_users(
        self,
    ) -> Dict[str, Any]:
        """Retrieves all users who have access to the current Contentstack stack. Returns user IDs, email addresses, and assigned roles. Use this to audit stack-level user access. This is a read-only operation with no side effects.
        Returns:
            API response as a dictionary.
        """
        ...

    def content_stack_list_stacks_in_organization(
        self,
        organizationId: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Retrieves all stacks belonging to a specific Contentstack organization, identified by organization ID. Returns stack names, UIDs, and metadata. Use this to enumerate available stacks in an organization. This is a read-only operation with no side effects.

        Args:
            organizationId: 
        Returns:
            API response as a dictionary.
        """
        ...

    def content_stack_list_taxonomies(
        self,
    ) -> Dict[str, Any]:
        """Retrieves all taxonomies defined in the Contentstack stack. Returns taxonomy names, UIDs, and descriptions. Use this to enumerate available taxonomies. To retrieve a single taxonomy, use content_stack_get_taxonomy instead.
        Returns:
            API response as a dictionary.
        """
        ...

    def content_stack_list_team_users(
        self,
        organizationId: Optional[str] = None,
        teamId: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Retrieves all users belonging to a specific team within a Contentstack organization, identified by organization ID and team ID. Use this to audit team membership. To retrieve details of a single user, use content_stack_search_organization_users_by_email instead.

        Args:
            organizationId: 
            teamId: 
        Returns:
            API response as a dictionary.
        """
        ...

    def content_stack_list_teams(
        self,
        organizationId: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Retrieves all teams within a Contentstack organization, identified by organization ID. Returns team names, IDs, and member counts. Use this to get an overview of all teams. To retrieve a single team, use content_stack_get_team instead.

        Args:
            organizationId: 
        Returns:
            API response as a dictionary.
        """
        ...

    def content_stack_list_webhooks(
        self,
    ) -> Dict[str, Any]:
        """Retrieves all webhooks defined in the Contentstack stack. Returns a list of webhook configurations including their URLs and triggers. Use this to get an overview of all webhooks. To retrieve a single webhook, use content_stack_get_webhook instead.
        Returns:
            API response as a dictionary.
        """
        ...

    def content_stack_list_workflows(
        self,
    ) -> Dict[str, Any]:
        """Retrieves all workflows defined in the Contentstack stack. Returns a list of workflows including their stages, names, and configurations. Use this to get an overview of all available workflows. To retrieve a single workflow, use content_stack_get_workflow instead.
        Returns:
            API response as a dictionary.
        """
        ...

    def content_stack_remove_user_from_team(
        self,
        organizationId: Optional[str] = None,
        teamId: Optional[str] = None,
        userId: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Removes a specific user from a team in a Contentstack organization, identified by organization ID, team ID, and user ID. Use this when revoking a users team membership. This action is permanent — the user will lose all access granted by that team membership.

        Args:
            organizationId: 
            teamId: 
            userId: 
        Returns:
            API response as a dictionary.
        """
        ...

    def content_stack_search_organization_users_by_email(
        self,
        emails: Optional[List[Any]] = None,
        organizationId: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Searches for users in a Contentstack organization by email address, identified by organization ID. Use this to find a users details before performing operations that require a user ID. This performs a POST-based search and does not create or modify any data.

        Args:
            emails: 
            organizationId: 
        Returns:
            API response as a dictionary.
        """
        ...

    def content_stack_set_fallback_language(
        self,
        locale: Optional[_ContentStackSetFallbackLanguageLocale] = None,
    ) -> Dict[str, Any]:
        """Sets a fallback language for a locale in Contentstack by creating a new locale entry with a fallback language specified. Use this when adding a locale that should fall back to another language when content is missing. Do not use this to update an existing locales fallback — use content_stack_update_fallback_language instead.

        Args:
            locale: 
        Returns:
            API response as a dictionary.
        """
        ...

    def content_stack_update_content_type(
        self,
        contentUid: Optional[str] = None,
        content_type: Optional[_ContentStackUpdateContentTypeContentType] = None,
    ) -> Dict[str, Any]:
        """Updates the schema of an existing content type in the Contentstack stack, identified by its content UID. Use this to add, modify, or remove fields from the content type definition. Do not use this to create a new content type — use content_stack_create_content_type instead. Schema changes may affect existing entries.

        Args:
            contentUid: 
            content_type: 
        Returns:
            API response as a dictionary.
        """
        ...

    def content_stack_update_entry(
        self,
        contenttypeUid: Optional[str] = None,
        entry: Optional[_ContentStackUpdateEntryEntry] = None,
        entryUid: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Updates an existing content entry in Contentstack, identified by content type UID and entry UID. Use this for standard entries without specialized field types. For entries with JSON RTE fields, use content_stack_update_entry_with_json_rte instead. This overwrites the existing entry field values.

        Args:
            contenttypeUid: 
            entry: 
            entryUid: 
        Returns:
            API response as a dictionary.
        """
        ...

    def content_stack_update_entry_with_json_rte(
        self,
        contenttypeUid: Optional[str] = None,
        entry: Optional[_ContentStackUpdateEntryWithJsonRteEntry] = None,
        entryUid: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Updates an existing content entry that contains a JSON Rich Text Editor (RTE) field in Contentstack, identified by content type UID and entry UID. Use this instead of content_stack_update_entry when the entry schema includes a JSON RTE field requiring structured JSON content. To create a new entry with JSON RTE, use content_stack_create_entry_with_json_rte.

        Args:
            contenttypeUid: 
            entry: 
            entryUid: 
        Returns:
            API response as a dictionary.
        """
        ...

    def content_stack_update_environment(
        self,
        enviromentName: Optional[str] = None,
        environment: Optional[_ContentStackUpdateEnvironmentEnvironment] = None,
    ) -> Dict[str, Any]:
        """Updates an existing publishing environment in Contentstack, identified by its environment name. Use this to modify environment settings such as URLs or associated locales. Do not use this to create a new environment — use content_stack_create_environment instead.

        Args:
            enviromentName: 
            environment: 
        Returns:
            API response as a dictionary.
        """
        ...

    def content_stack_update_fallback_language(
        self,
        languageCode: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Updates the fallback language setting for an existing locale in Contentstack, identified by its language code. Use this when you need to change which language serves as the fallback for a given locale. Do not use this to update other locale properties — use content_stack_update_language for general locale updates.

        Args:
            languageCode: 
        Returns:
            API response as a dictionary.
        """
        ...

    def content_stack_update_language(
        self,
        languageCode: Optional[str] = None,
        locale: Optional[_ContentStackUpdateLanguageLocale] = None,
    ) -> Dict[str, Any]:
        """Updates an existing locale (language) in Contentstack, identified by its language code. Use this when you need to change locale settings such as the display name. Do not use this to add a new locale — use content_stack_create_language instead. Do not use this to set a fallback language — use content_stack_set_fallback_language instead.

        Args:
            languageCode: 
            locale: 
        Returns:
            API response as a dictionary.
        """
        ...

    def content_stack_update_release(
        self,
        release: Optional[_ContentStackUpdateReleaseRelease] = None,
        releaseId: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Updates an existing release in Contentstack, identified by its release ID. Use this to modify a releases name, description, or scheduled date. Do not use this to create a new release — use content_stack_create_release instead. Do not use this to add items to a release.

        Args:
            release: 
            releaseId: 
        Returns:
            API response as a dictionary.
        """
        ...

    def content_stack_update_role(
        self,
        role: Optional[_ContentStackUpdateRoleRole] = None,
        roleId: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Updates an existing role in Contentstack, identified by its role ID. Use this when you need to modify a roles name, description, or permissions. Do not use this to create a new role — use content_stack_create_role instead. This operation overwrites the existing role configuration.

        Args:
            role: 
            roleId: 
        Returns:
            API response as a dictionary.
        """
        ...

    def content_stack_update_taxonomy(
        self,
        taxonomy: Optional[_ContentStackUpdateTaxonomyTaxonomy] = None,
        taxonomyUid: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Updates an existing taxonomy in the Contentstack stack, identified by its taxonomy UID. Use this to modify taxonomy name, description, or structure. Do not use this to create a new taxonomy — use content_stack_create_taxonomy instead. Do not use this to delete a taxonomy — use content_stack_delete_taxonomy instead.

        Args:
            taxonomy: 
            taxonomyUid: 
        Returns:
            API response as a dictionary.
        """
        ...

    def content_stack_update_team(
        self,
        name: Optional[str] = None,
        organizationId: Optional[str] = None,
        organizationRole: Optional[str] = None,
        stackRoleMapping: Optional[List[Any]] = None,
        teamId: Optional[str] = None,
        users: Optional[List[Any]] = None,
    ) -> Dict[str, Any]:
        """Updates an existing team within a Contentstack organization, identified by organization ID and team ID. Use this to modify a teams name, description, or membership settings. Do not use this to create a new team — use content_stack_create_team instead.

        Args:
            name: 
            organizationId: 
            organizationRole: 
            stackRoleMapping: 
            teamId: 
            users: 
        Returns:
            API response as a dictionary.
        """
        ...

    def content_stack_update_webhook(
        self,
        webhook: Optional[_ContentStackUpdateWebhookWebhook] = None,
        webhookId: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Updates the configuration of an existing webhook in Contentstack, identified by its webhook ID. Use this when you need to change a webhooks URL, triggers, channels, or other settings. Do not use this to create a new webhook — use content_stack_create_webhook instead. This operation overwrites the existing webhook configuration.

        Args:
            webhook: 
            webhookId: 
        Returns:
            API response as a dictionary.
        """
        ...

    def content_stack_update_workflow(
        self,
        workflow: Optional[_ContentStackUpdateWorkflowWorkflow] = None,
        workflowId: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Updates the details of an existing workflow in Contentstack, identified by its workflow ID. Use this to modify workflow stages, names, or configuration. Do not use this to create a new workflow — use content_stack_create_workflow instead.

        Args:
            workflow: 
            workflowId: 
        Returns:
            API response as a dictionary.
        """
        ...

