"""Fastn Content Stack connector — auto-generated type stubs.

Do not edit manually. Regenerate with `fastn connector sync`.
"""
from __future__ import annotations

from typing import Any, Dict, List, Optional


class ContentStackConnector:
    """Content Stack connector ().

    Provides 91 tools.
    """

    def compare_content_types_between_branches(
        self,
        compare_branch: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Compares content types between different branches in the specified connector.

        Args:
            compare_branch: 
        Returns:
            API response as a dictionary.
        """
        ...

    def compare_global_fields_between_branches(
        self,
        compare_branch: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Compares global fields between different branches in the specified connector.

        Args:
            compare_branch: 
        Returns:
            API response as a dictionary.
        """
        ...

    def compare_specific_content_type_between_branches(
        self,
        base_branch: Optional[str] = None,
        compare_branch: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Compares a specific content type between different branches in the specified connector.

        Args:
            base_branch: 
            compare_branch: 
        Returns:
            API response as a dictionary.
        """
        ...

    def create_a_release(
        self,
        release: Optional[Dict[str, Any]] = None,
    ) -> Dict[str, Any]:
        """Creates a new release in the specified connector.

        Args:
            release: 
        Returns:
            API response as a dictionary.
        """
        ...

    def create_a_role(
        self,
        role: Optional[Dict[str, Any]] = None,
    ) -> Dict[str, Any]:
        """Creates a new role in the specified connector.

        Args:
            role: 
        Returns:
            API response as a dictionary.
        """
        ...

    def create_a_team(
        self,
        name: Optional[str] = None,
        organizationRole: Optional[str] = None,
        stackRoleMapping: Optional[List[Any]] = None,
        users: Optional[List[Any]] = None,
    ) -> Dict[str, Any]:
        """Creates a new team in the specified connector.

        Args:
            name: 
            organizationRole: 
            stackRoleMapping: 
            users: 
        Returns:
            API response as a dictionary.
        """
        ...

    def create_a_webhook(
        self,
        webhook: Optional[Dict[str, Any]] = None,
    ) -> Dict[str, Any]:
        """Creates a new webhook in the specified connector.

        Args:
            webhook: 
        Returns:
            API response as a dictionary.
        """
        ...

    def create_a_workflow(
        self,
        workflow: Optional[Dict[str, Any]] = None,
    ) -> Dict[str, Any]:
        """Creates a new workflow in the specified connector.

        Args:
            workflow: 
        Returns:
            API response as a dictionary.
        """
        ...

    def create_branch(
        self,
        branch: Optional[Dict[str, Any]] = None,
    ) -> Dict[str, Any]:
        """Creates a new branch in the specified connector.

        Args:
            branch: 
        Returns:
            API response as a dictionary.
        """
        ...

    def create_content_type(
        self,
        content_type: Optional[Dict[str, Any]] = None,
    ) -> Dict[str, Any]:
        """Creates a new content type in the specified connector.

        Args:
            content_type: 
        Returns:
            API response as a dictionary.
        """
        ...

    def create_custom_asset_field(
        self,
        content_type: Optional[Dict[str, Any]] = None,
    ) -> Dict[str, Any]:
        """Creates a new custom asset field for a content type in the specified connector.

        Args:
            content_type: 
        Returns:
            API response as a dictionary.
        """
        ...

    def create_entry(
        self,
        entry: Optional[Dict[str, Any]] = None,
    ) -> Dict[str, Any]:
        """Creates a new entry for a specified content type in the specified connector.

        Args:
            entry: 
        Returns:
            API response as a dictionary.
        """
        ...

    def create_entry_master_locale(
        self,
        copy_to_master: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Creates a new entry for a specified content type in the master locale in the specified connector.

        Args:
            copy_to_master: 
        Returns:
            API response as a dictionary.
        """
        ...

    def create_entry_with_custom_asset_field(
        self,
        entry: Optional[Dict[str, Any]] = None,
    ) -> Dict[str, Any]:
        """Creates a new entry with a custom asset field for a specified content type in the specified connector.

        Args:
            entry: 
        Returns:
            API response as a dictionary.
        """
        ...

    def create_entry_with_json_rte(
        self,
        entry: Optional[Dict[str, Any]] = None,
    ) -> Dict[str, Any]:
        """Creates a new entry with a JSON Rich Text Editor field in the specified connector.

        Args:
            entry: 
        Returns:
            API response as a dictionary.
        """
        ...

    def create_environment(
        self,
        environment: Optional[Dict[str, Any]] = None,
    ) -> Dict[str, Any]:
        """Creates a new environment in the specified connector.

        Args:
            environment: 
        Returns:
            API response as a dictionary.
        """
        ...

    def create_json_rte(
        self,
        content_type: Optional[Dict[str, Any]] = None,
    ) -> Dict[str, Any]:
        """Creates a new JSON Rich Text Editor field within a content type in the specified connector.

        Args:
            content_type: 
        Returns:
            API response as a dictionary.
        """
        ...

    def create_language(
        self,
        locale: Optional[Dict[str, Any]] = None,
    ) -> Dict[str, Any]:
        """Creates a new language in the specified connector.

        Args:
            locale: 
        Returns:
            API response as a dictionary.
        """
        ...

    def create_or_update_workflow_details(
        self,
        workflow: Optional[Dict[str, Any]] = None,
    ) -> Dict[str, Any]:
        """Creates or updates workflow details in the specified connector.

        Args:
            workflow: 
        Returns:
            API response as a dictionary.
        """
        ...

    def create_select_field(
        self,
        content_type: Optional[Dict[str, Any]] = None,
    ) -> Dict[str, Any]:
        """Creates a new select field within a content type in the specified connector.

        Args:
            content_type: 
        Returns:
            API response as a dictionary.
        """
        ...

    def create_taxonomy(
        self,
        taxonomy: Optional[Dict[str, Any]] = None,
    ) -> Dict[str, Any]:
        """Creates a new taxonomy in the specified connector.

        Args:
            taxonomy: 
        Returns:
            API response as a dictionary.
        """
        ...

    def create_with_taxonomy(
        self,
        content_type: Optional[Dict[str, Any]] = None,
        options: Optional[Dict[str, Any]] = None,
    ) -> Dict[str, Any]:
        """Creates a new content type with taxonomy integration in the specified connector.

        Args:
            content_type: 
            options: 
        Returns:
            API response as a dictionary.
        """
        ...

    def delete_a_release(
        self,
        releaseId: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Deletes a specific release from the specified connector.

        Args:
            releaseId: 
        Returns:
            API response as a dictionary.
        """
        ...

    def delete_a_team(
        self,
        organizationId: Optional[str] = None,
        teamId: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Deletes a specific team from the specified connector.

        Args:
            organizationId: 
            teamId: 
        Returns:
            API response as a dictionary.
        """
        ...

    def delete_branch(
        self,
        force: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Deletes a specific branch from the specified connector.

        Args:
            force: 
        Returns:
            API response as a dictionary.
        """
        ...

    def delete_content_type(
        self,
        contentUid: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Deletes a specific content type from the specified connector.

        Args:
            contentUid: 
        Returns:
            API response as a dictionary.
        """
        ...

    def delete_entry(
        self,
        contenttypeUid: Optional[str] = None,
        entryUid: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Deletes a specific entry from the specified connector.

        Args:
            contenttypeUid: 
            entryUid: 
        Returns:
            API response as a dictionary.
        """
        ...

    def delete_environment(
        self,
        enviromentName: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Deletes a specific environment from the specified connector.

        Args:
            enviromentName: 
        Returns:
            API response as a dictionary.
        """
        ...

    def delete_language(
        self,
        languageCode: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Deletes a specific language in the specified connector.

        Args:
            languageCode: 
        Returns:
            API response as a dictionary.
        """
        ...

    def delete_role(
        self,
        roleId: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Deletes a specific role from the specified connector.

        Args:
            roleId: 
        Returns:
            API response as a dictionary.
        """
        ...

    def delete_taxonomy(
        self,
        force: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Deletes a specific taxonomy from the specified connector.

        Args:
            force: 
        Returns:
            API response as a dictionary.
        """
        ...

    def delete_webhook(
        self,
        webhookId: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Deletes a specific webhook from the specified connector.

        Args:
            webhookId: 
        Returns:
            API response as a dictionary.
        """
        ...

    def delete_workflow(
        self,
        workflowId: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Deletes a specific workflow from the specified connector.

        Args:
            workflowId: 
        Returns:
            API response as a dictionary.
        """
        ...

    def disable_workflow(
        self,
        workflowId: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Disables a specific workflow in the specified connector.

        Args:
            workflowId: 
        Returns:
            API response as a dictionary.
        """
        ...

    def enable_workflow(
        self,
        workflowId: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Enables a specific workflow in the specified connector.

        Args:
            workflowId: 
        Returns:
            API response as a dictionary.
        """
        ...

    def export_a_webhook(
        self,
        webhookId: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Exports a specific webhook from the specified connector.

        Args:
            webhookId: 
        Returns:
            API response as a dictionary.
        """
        ...

    def export_content_type(
        self,
    ) -> Dict[str, Any]:
        """Exports a specified content type from the specified connector.
        Returns:
            API response as a dictionary.
        """
        ...

    def export_taxonomy(
        self,
        taxonomyUid: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Exports a specific taxonomy from the specified connector.

        Args:
            taxonomyUid: 
        Returns:
            API response as a dictionary.
        """
        ...

    def get_a_language(
        self,
        languageCode: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Fetches the details of a specific language in the specified connector.

        Args:
            languageCode: 
        Returns:
            API response as a dictionary.
        """
        ...

    def get_aliases(
        self,
    ) -> Dict[str, Any]:
        """Fetches all aliases defined in the specified connector.
        Returns:
            API response as a dictionary.
        """
        ...

    def get_all_items_in_a_release(
        self,
        releaseId: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Retrieves all items in a specific release in the specified connector.

        Args:
            releaseId: 
        Returns:
            API response as a dictionary.
        """
        ...

    def get_all_languages(
        self,
    ) -> Dict[str, Any]:
        """Fetches all languages in the specified connector.
        Returns:
            API response as a dictionary.
        """
        ...

    def get_all_organization_invitations(
        self,
        organizationId: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Retrieves all organization invitations in the specified connector.

        Args:
            organizationId: 
        Returns:
            API response as a dictionary.
        """
        ...

    def get_all_organizations(
        self,
    ) -> Dict[str, Any]:
        """Fetches all organizations in the specified connector.
        Returns:
            API response as a dictionary.
        """
        ...

    def get_all_releases(
        self,
    ) -> Dict[str, Any]:
        """Retrieves all releases in the specified connector.
        Returns:
            API response as a dictionary.
        """
        ...

    def get_all_roles(
        self,
    ) -> Dict[str, Any]:
        """Fetches all roles in the specified connector.
        Returns:
            API response as a dictionary.
        """
        ...

    def get_all_stacks_in_an_organization(
        self,
        organizationId: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Fetches all stacks in a specific organization in the specified connector.

        Args:
            organizationId: 
        Returns:
            API response as a dictionary.
        """
        ...

    def get_all_teams(
        self,
        organizationId: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Retrieves all teams in the specified connector.

        Args:
            organizationId: 
        Returns:
            API response as a dictionary.
        """
        ...

    def get_all_users_of_team(
        self,
        organizationId: Optional[str] = None,
        teamId: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Fetches all users within a specific team in the specified connector.

        Args:
            organizationId: 
            teamId: 
        Returns:
            API response as a dictionary.
        """
        ...

    def get_all_webhooks(
        self,
    ) -> Dict[str, Any]:
        """Retrieves all webhooks defined in the specified connector.
        Returns:
            API response as a dictionary.
        """
        ...

    def get_all_workflows(
        self,
    ) -> Dict[str, Any]:
        """Retrieves all workflows in the specified connector.
        Returns:
            API response as a dictionary.
        """
        ...

    def get_audit_log(
        self,
    ) -> Dict[str, Any]:
        """Fetches the audit log in the specified connector.
        Returns:
            API response as a dictionary.
        """
        ...

    def get_branch(
        self,
    ) -> Dict[str, Any]:
        """Fetches details of a specific branch in the specified connector.
        Returns:
            API response as a dictionary.
        """
        ...

    def get_branches(
        self,
    ) -> Dict[str, Any]:
        """Retrieves all branches available in the specified connector.
        Returns:
            API response as a dictionary.
        """
        ...

    def get_content_type(
        self,
        contentUid: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Fetches the details of a specific content type in the specified connector.

        Args:
            contentUid: 
        Returns:
            API response as a dictionary.
        """
        ...

    def get_content_type_delivery(
        self,
        contentUid: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Fetches the delivery details of a specific content type in the specified connector.

        Args:
            contentUid: 
        Returns:
            API response as a dictionary.
        """
        ...

    def get_content_types(
        self,
    ) -> Dict[str, Any]:
        """Retrieves all content types in the specified connector.
        Returns:
            API response as a dictionary.
        """
        ...

    def get_content_types_delivery(
        self,
        include_count: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Retrieves all content types available for delivery in the specified connector.

        Args:
            include_count: 
        Returns:
            API response as a dictionary.
        """
        ...

    def get_entries(
        self,
        contenttypeUid: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Retrieves all entries for a specified content type in the specified connector.

        Args:
            contenttypeUid: 
        Returns:
            API response as a dictionary.
        """
        ...

    def get_entry(
        self,
        contenttypeUid: Optional[str] = None,
        entryUid: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Fetches the details of a specific entry in the specified connector.

        Args:
            contenttypeUid: 
            entryUid: 
        Returns:
            API response as a dictionary.
        """
        ...

    def get_environment(
        self,
        enviromentName: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Retrieves the environment details in the specified connector.

        Args:
            enviromentName: 
        Returns:
            API response as a dictionary.
        """
        ...

    def get_environments(
        self,
    ) -> Dict[str, Any]:
        """Retrieves all environments in the specified connector.
        Returns:
            API response as a dictionary.
        """
        ...

    def get_merge_jobs(
        self,
    ) -> Dict[str, Any]:
        """Retrieves all merge jobs in the specified connector.
        Returns:
            API response as a dictionary.
        """
        ...

    def get_organization(
        self,
        organizationId: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Fetches organization details in the specified connector.

        Args:
            organizationId: 
        Returns:
            API response as a dictionary.
        """
        ...

    def get_organization_log_details(
        self,
        organizationId: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Retrieves organization log details in the specified connector.

        Args:
            organizationId: 
        Returns:
            API response as a dictionary.
        """
        ...

    def get_organization_log_item(
        self,
        logId: Optional[str] = None,
        organizationId: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Fetches specific organization log items in the specified connector.

        Args:
            logId: 
            organizationId: 
        Returns:
            API response as a dictionary.
        """
        ...

    def get_organization_users_by_email(
        self,
        emails: Optional[List[Any]] = None,
    ) -> Dict[str, Any]:
        """Retrieves organization users based on email in the specified connector.

        Args:
            emails: 
        Returns:
            API response as a dictionary.
        """
        ...

    def get_publish_queue(
        self,
    ) -> Dict[str, Any]:
        """Fetches the publish queue in the specified connector.
        Returns:
            API response as a dictionary.
        """
        ...

    def get_references_conten_type(
        self,
    ) -> Dict[str, Any]:
        """Gets references related to a content type in the specified connector.
        Returns:
            API response as a dictionary.
        """
        ...

    def get_release(
        self,
        releaseId: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Retrieves the details of a specific release in the specified connector.

        Args:
            releaseId: 
        Returns:
            API response as a dictionary.
        """
        ...

    def get_role(
        self,
        roleId: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Fetches details of a specific role in the specified connector.

        Args:
            roleId: 
        Returns:
            API response as a dictionary.
        """
        ...

    def get_roles_in_an_organization(
        self,
        organizationId: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Retrieves roles within a specific organization in the specified connector.

        Args:
            organizationId: 
        Returns:
            API response as a dictionary.
        """
        ...

    def get_taxonomies(
        self,
    ) -> Dict[str, Any]:
        """Retrieves all taxonomies in the specified connector.
        Returns:
            API response as a dictionary.
        """
        ...

    def get_taxonomy(
        self,
        taxonomyUid: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Fetches the details of a specific taxonomy in the specified connector.

        Args:
            taxonomyUid: 
        Returns:
            API response as a dictionary.
        """
        ...

    def get_team(
        self,
        organizationId: Optional[str] = None,
        teamId: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Retrieves details of a specific team in the specified connector.

        Args:
            organizationId: 
            teamId: 
        Returns:
            API response as a dictionary.
        """
        ...

    def get_users_of_stack(
        self,
    ) -> Dict[str, Any]:
        """Retrieves all users in the specified stack of the connector.
        Returns:
            API response as a dictionary.
        """
        ...

    def get_webhook(
        self,
        webhookId: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Fetches the details of a specific webhook in the specified connector.

        Args:
            webhookId: 
        Returns:
            API response as a dictionary.
        """
        ...

    def get_workflow(
        self,
        workflowId: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Fetches details of a specific workflow in the specified connector.

        Args:
            workflowId: 
        Returns:
            API response as a dictionary.
        """
        ...

    def remove_a_user_from_team(
        self,
        organizationId: Optional[str] = None,
        teamId: Optional[str] = None,
        userId: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Removes a specific user from a team in the specified connector.

        Args:
            organizationId: 
            teamId: 
            userId: 
        Returns:
            API response as a dictionary.
        """
        ...

    def set_a_fallback_language(
        self,
        locale: Optional[Dict[str, Any]] = None,
    ) -> Dict[str, Any]:
        """Sets a fallback language in the specified connector.

        Args:
            locale: 
        Returns:
            API response as a dictionary.
        """
        ...

    def update_a_release(
        self,
        release: Optional[Dict[str, Any]] = None,
    ) -> Dict[str, Any]:
        """Updates a specific release in the specified connector.

        Args:
            release: 
        Returns:
            API response as a dictionary.
        """
        ...

    def update_a_team(
        self,
        name: Optional[str] = None,
        organizationRole: Optional[str] = None,
        stackRoleMapping: Optional[List[Any]] = None,
        users: Optional[List[Any]] = None,
    ) -> Dict[str, Any]:
        """Updates a specific team in the specified connector.

        Args:
            name: 
            organizationRole: 
            stackRoleMapping: 
            users: 
        Returns:
            API response as a dictionary.
        """
        ...

    def update_content_type(
        self,
        content_type: Optional[Dict[str, Any]] = None,
    ) -> Dict[str, Any]:
        """Updates an existing content type in the specified connector.

        Args:
            content_type: 
        Returns:
            API response as a dictionary.
        """
        ...

    def update_entry(
        self,
        entry: Optional[Dict[str, Any]] = None,
    ) -> Dict[str, Any]:
        """Updates an existing entry in the specified connector.

        Args:
            entry: 
        Returns:
            API response as a dictionary.
        """
        ...

    def update_entry_with_json_rte(
        self,
        entry: Optional[Dict[str, Any]] = None,
    ) -> Dict[str, Any]:
        """Updates an existing entry with a JSON Rich Text Editor field in the specified connector.

        Args:
            entry: 
        Returns:
            API response as a dictionary.
        """
        ...

    def update_environment(
        self,
        environment: Optional[Dict[str, Any]] = None,
    ) -> Dict[str, Any]:
        """Updates environment details in the specified connector.

        Args:
            environment: 
        Returns:
            API response as a dictionary.
        """
        ...

    def update_fallback_language(
        self,
        languageCode: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Updates the fallback language in the specified connector.

        Args:
            languageCode: 
        Returns:
            API response as a dictionary.
        """
        ...

    def update_language(
        self,
        locale: Optional[Dict[str, Any]] = None,
    ) -> Dict[str, Any]:
        """Updates a specific language in the specified connector.

        Args:
            locale: 
        Returns:
            API response as a dictionary.
        """
        ...

    def update_role(
        self,
        role: Optional[Dict[str, Any]] = None,
    ) -> Dict[str, Any]:
        """Updates a specific role in the specified connector.

        Args:
            role: 
        Returns:
            API response as a dictionary.
        """
        ...

    def update_taxonomy(
        self,
        taxonomy: Optional[Dict[str, Any]] = None,
    ) -> Dict[str, Any]:
        """Updates an existing taxonomy in the specified connector.

        Args:
            taxonomy: 
        Returns:
            API response as a dictionary.
        """
        ...

    def update_webhook(
        self,
        webhook: Optional[Dict[str, Any]] = None,
    ) -> Dict[str, Any]:
        """Updates a specific webhook in the specified connector.

        Args:
            webhook: 
        Returns:
            API response as a dictionary.
        """
        ...

