"""Fastn fastn connector — auto-generated type stubs.

Do not edit manually. Regenerate with `fastn connector sync`.
"""
from __future__ import annotations

from typing import Any, Dict, List, Optional


class FastnConnector:
    """fastn connector ().

    Provides 83 tools.
    """

    def active_connector_status(
        self,
        projectId: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Checks the active status of the connector in the system.

        Args:
            projectId: 
        Returns:
            API response as a dictionary.
        """
        ...

    def add_env_configs(
        self,
        projectId: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Adds environment configurations to the specified connector.

        Args:
            projectId: 
        Returns:
            API response as a dictionary.
        """
        ...

    def add_record(
        self,
        projectId: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Adds a new record to the specified database table.

        Args:
            projectId: 
        Returns:
            API response as a dictionary.
        """
        ...

    def add_records_to_fastn_db_table(
        self,
        projectId: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Adds multiple records to a specified FastnDB table in one operation.

        Args:
            projectId: 
        Returns:
            API response as a dictionary.
        """
        ...

    def batch_create_webhooks(
        self,
        projectId: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Creates multiple webhooks in a batch operation.

        Args:
            projectId: 
        Returns:
            API response as a dictionary.
        """
        ...

    def batch_import_templates(
        self,
        projectId: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Imports multiple templates in a batch operation.

        Args:
            projectId: 
        Returns:
            API response as a dictionary.
        """
        ...

    def build_flow(
        self,
        projectId: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Builds a flow based on specified parameters and actions.

        Args:
            projectId: 
        Returns:
            API response as a dictionary.
        """
        ...

    def connector_test_api(
        self,
        projectId: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Tests the specified connector's API endpoint for functionality.

        Args:
            projectId: 
        Returns:
            API response as a dictionary.
        """
        ...

    def create_app_trigger(
        self,
        projectId: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Creates a new application trigger for the specified conditions.

        Args:
            projectId: 
        Returns:
            API response as a dictionary.
        """
        ...

    def create_app_v3(
        self,
        xfabricchannelid: Optional[str] = None,
        xfabrictenantid: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Creates a new application version 3 with specified settings.

        Args:
            xfabricchannelid: 
            xfabrictenantid: 
        Returns:
            API response as a dictionary.
        """
        ...

    def create_connector(
        self,
        projectId: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Creates a new connector with the specified settings.

        Args:
            projectId: 
        Returns:
            API response as a dictionary.
        """
        ...

    def create_external_db_api(
        self,
        projectId: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Creates a new API for an external database.

        Args:
            projectId: 
        Returns:
            API response as a dictionary.
        """
        ...

    def create_external_db_connection(
        self,
        projectId: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Creates a new external database connection.

        Args:
            projectId: 
        Returns:
            API response as a dictionary.
        """
        ...

    def create_fastn_db_table(
        self,
        clientId: Optional[str] = None,
        columns: Optional[List[Any]] = None,
        name: Optional[str] = None,
        override: Optional[bool] = None,
    ) -> Dict[str, Any]:
        """Creates a FastnDB table with defined schema.

        Args:
            clientId: 
            columns: 
            name: 
            override: 
        Returns:
            API response as a dictionary.
        """
        ...

    def create_internal_db_api(
        self,
        projectId: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Creates an internal API for FastnDB operations.

        Args:
            projectId: 
        Returns:
            API response as a dictionary.
        """
        ...

    def create_model_group(
        self,
        projectId: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Creates a new model group with specified configurations.

        Args:
            projectId: 
        Returns:
            API response as a dictionary.
        """
        ...

    def create_project(
        self,
        projectId: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Creates a new project in the system with specified configurations.

        Args:
            projectId: 
        Returns:
            API response as a dictionary.
        """
        ...

    def create_resolver_step(
        self,
        projectId: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Creates a new resolver step in the workflow.

        Args:
            projectId: 
        Returns:
            API response as a dictionary.
        """
        ...

    def create_secret_with_api_key(
        self,
        ApiKey: Optional[str] = None,
        domain: Optional[str] = None,
        projectId: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Creates a secret with an associated API key.

        Args:
            ApiKey: 
            domain: 
            projectId: 
        Returns:
            API response as a dictionary.
        """
        ...

    def create_secrets(
        self,
        customAuth: Optional[str] = None,
        projectId: Optional[str] = None,
        tenantId: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Creates secrets to store sensitive information securely.

        Args:
            customAuth: 
            projectId: 
            tenantId: 
        Returns:
            API response as a dictionary.
        """
        ...

    def create_table(
        self,
        projectId: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Creates a new table within the specified database.

        Args:
            projectId: 
        Returns:
            API response as a dictionary.
        """
        ...

    def create_tenant(
        self,
        projectId: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Creates a new tenant in the system with specified parameters.

        Args:
            projectId: 
        Returns:
            API response as a dictionary.
        """
        ...

    def create_webhooks_with_routes(
        self,
        projectId: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Creates new webhooks with the specified routes for event handling.

        Args:
            projectId: 
        Returns:
            API response as a dictionary.
        """
        ...

    def create_widget_v2(
        self,
        projectId: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Creates a new widget using version 2 specifications.

        Args:
            projectId: 
        Returns:
            API response as a dictionary.
        """
        ...

    def create_widgets(
        self,
        projectId: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Creates new widgets with the defined specifications.

        Args:
            projectId: 
        Returns:
            API response as a dictionary.
        """
        ...

    def delete_api(
        self,
        projectId: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Deletes an API from the system.

        Args:
            projectId: 
        Returns:
            API response as a dictionary.
        """
        ...

    def delete_api_key(
        self,
        Authorization: Optional[str] = None,
        domain: Optional[str] = None,
        projectId: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Deletes an existing API key from the system.

        Args:
            Authorization: 
            domain: 
            projectId: 
        Returns:
            API response as a dictionary.
        """
        ...

    def delete_app_trigger(
        self,
        projectId: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Deletes a specified application trigger from the system.

        Args:
            projectId: 
        Returns:
            API response as a dictionary.
        """
        ...

    def delete_env_configuration(
        self,
        projectId: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Deletes an environment configuration from the system.

        Args:
            projectId: 
        Returns:
            API response as a dictionary.
        """
        ...

    def delete_model(
        self,
        projectId: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Deletes a model from the specified connector.

        Args:
            projectId: 
        Returns:
            API response as a dictionary.
        """
        ...

    def delete_secret(
        self,
        projectId: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Deletes a secret from the system.

        Args:
            projectId: 
        Returns:
            API response as a dictionary.
        """
        ...

    def delete_webhook(
        self,
        projectId: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Deletes an existing webhook from the system.

        Args:
            projectId: 
        Returns:
            API response as a dictionary.
        """
        ...

    def execute_curl(
        self,
        projectId: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Executes a curl command for network operations.

        Args:
            projectId: 
        Returns:
            API response as a dictionary.
        """
        ...

    def generate_api_key(
        self,
        projectId: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Generates a new API key for accessing resources.

        Args:
            projectId: 
        Returns:
            API response as a dictionary.
        """
        ...

    def generate_auth_token(
        self,
    ) -> Dict[str, Any]:
        """Generates an authentication token for user or application access.
        Returns:
            API response as a dictionary.
        """
        ...

    def generate_token(
        self,
        projectId: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Generates a new token for authentication purposes.

        Args:
            projectId: 
        Returns:
            API response as a dictionary.
        """
        ...

    def get_action_by_id(
        self,
        projectId: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Retrieves details about a specific action by its identifier.

        Args:
            projectId: 
        Returns:
            API response as a dictionary.
        """
        ...

    def get_api(
        self,
        projectId: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Retrieves details about a specified API.

        Args:
            projectId: 
        Returns:
            API response as a dictionary.
        """
        ...

    def get_api_keys(
        self,
        projectId: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Retrieves all existing API keys.

        Args:
            projectId: 
        Returns:
            API response as a dictionary.
        """
        ...

    def get_apis(
        self,
        projectId: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Fetches all APIs available in the system.

        Args:
            projectId: 
        Returns:
            API response as a dictionary.
        """
        ...

    def get_app_trigger(
        self,
        projectId: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Retrieves details about a specific application trigger.

        Args:
            projectId: 
        Returns:
            API response as a dictionary.
        """
        ...

    def get_app_triggers(
        self,
        projectId: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Fetches a list of all application triggers configured in the system.

        Args:
            projectId: 
        Returns:
            API response as a dictionary.
        """
        ...

    def get_connection_ids(
        self,
        connectorId: Optional[str] = None,
        projectId: Optional[str] = None,
        tenantId: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Retrieves connection IDs associated with the specified environment.

        Args:
            connectorId: 
            projectId: 
            tenantId: 
        Returns:
            API response as a dictionary.
        """
        ...

    def get_connector_group_info(
        self,
        projectId: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Retrieves information about a specific connector group.

        Args:
            projectId: 
        Returns:
            API response as a dictionary.
        """
        ...

    def get_connector_groups(
        self,
        projectId: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Fetches all connector groups in the system.

        Args:
            projectId: 
        Returns:
            API response as a dictionary.
        """
        ...

    def get_connector_groups_test(
        self,
        projectId: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Fetches all connector groups for testing purposes.

        Args:
            projectId: 
        Returns:
            API response as a dictionary.
        """
        ...

    def get_connector_info(
        self,
        projectId: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Retrieves detailed information about a specified connector.

        Args:
            projectId: 
        Returns:
            API response as a dictionary.
        """
        ...

    def get_connector_token(
        self,
        customAuth: Optional[str] = None,
        projectId: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Retrieves the token associated with the specified connector.

        Args:
            customAuth: 
            projectId: 
        Returns:
            API response as a dictionary.
        """
        ...

    def get_connectors_from_group(
        self,
        projectId: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Retrieves connectors associated with a specified group.

        Args:
            projectId: 
        Returns:
            API response as a dictionary.
        """
        ...

    def get_env_configs(
        self,
        projectId: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Retrieves all environment configurations available.

        Args:
            projectId: 
        Returns:
            API response as a dictionary.
        """
        ...

    def get_external_db_tables(
        self,
        projectId: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Retrieves tables from an external database connection.

        Args:
            projectId: 
        Returns:
            API response as a dictionary.
        """
        ...

    def get_flow_schema(
        self,
        projectId: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Fetches the schema for a specified flow.

        Args:
            projectId: 
        Returns:
            API response as a dictionary.
        """
        ...

    def get_group(
        self,
        projectId: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Retrieves the details of a specified group.

        Args:
            projectId: 
        Returns:
            API response as a dictionary.
        """
        ...

    def get_project(
        self,
        projectId: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Retrieves details about a specified project.

        Args:
            projectId: 
        Returns:
            API response as a dictionary.
        """
        ...

    def get_secrets(
        self,
        projectId: Optional[str] = None,
        x_fastn_custom_auth: Optional[bool] = None,
    ) -> Dict[str, Any]:
        """Retrieves all stored secrets for the specified connector.

        Args:
            projectId: 
            x_fastn_custom_auth: 
        Returns:
            API response as a dictionary.
        """
        ...

    def get_templates(
        self,
        projectId: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Retrieves all available templates for use.

        Args:
            projectId: 
        Returns:
            API response as a dictionary.
        """
        ...

    def get_tenants(
        self,
        projectId: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Retrieves a list of all tenants in the system.

        Args:
            projectId: 
        Returns:
            API response as a dictionary.
        """
        ...

    def get_user_by_token(
        self,
        authorization: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Gets user details associated with the specified token.

        Args:
            authorization: 
        Returns:
            API response as a dictionary.
        """
        ...

    def get_webhook(
        self,
    ) -> Dict[str, Any]:
        """Retrieves details of a specific webhook.
        Returns:
            API response as a dictionary.
        """
        ...

    def get_webhooks(
        self,
        projectId: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Fetches a list of all configured webhooks.

        Args:
            projectId: 
        Returns:
            API response as a dictionary.
        """
        ...

    def get_widget_connector_status(
        self,
        projectId: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Checks the status of a widget connector for the specified version.

        Args:
            projectId: 
        Returns:
            API response as a dictionary.
        """
        ...

    def get_widget_connector_status_v2(
        self,
        projectId: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Gets the status of a widget connector in version 2.

        Args:
            projectId: 
        Returns:
            API response as a dictionary.
        """
        ...

    def import_collection_from_postman(
        self,
        projectId: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Imports a collection from Postman for API management.

        Args:
            projectId: 
        Returns:
            API response as a dictionary.
        """
        ...

    def import_flow_template(
        self,
        projectId: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Imports a flow template to the system for easy setup.

        Args:
            projectId: 
        Returns:
            API response as a dictionary.
        """
        ...

    def invite_user(
        self,
        projectId: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Invites a new user to join the platform.

        Args:
            projectId: 
        Returns:
            API response as a dictionary.
        """
        ...

    def invoke_connector_action(
        self,
        projectId: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Invokes a specific action on the connector as defined.

        Args:
            projectId: 
        Returns:
            API response as a dictionary.
        """
        ...

    def list_mcp_server_tools(
        self,
        customAuth: Optional[str] = None,
        projectId: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Lists all server tools available in the MCP environment.

        Args:
            customAuth: 
            projectId: 
        Returns:
            API response as a dictionary.
        """
        ...

    def migrate_secrets_without_expiry(
        self,
    ) -> Dict[str, Any]:
        """Migrates secrets in the system that do not have an expiry date.
        Returns:
            API response as a dictionary.
        """
        ...

    def retreivel_chart_type_v1(
        self,
        authorization: Optional[str] = None,
        x_fastn_space_connection_id: Optional[str] = None,
        x_fastn_space_id: Optional[str] = None,
        x_fastn_space_tenantid: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Retrieves the chart type for the specified version.

        Args:
            authorization: 
            x_fastn_space_connection_id: 
            x_fastn_space_id: 
            x_fastn_space_tenantid: 
        Returns:
            API response as a dictionary.
        """
        ...

    def rotate_expired_secret(
        self,
    ) -> Dict[str, Any]:
        """Rotates secrets that are past their expiry date.
        Returns:
            API response as a dictionary.
        """
        ...

    def run_action(
        self,
        projectId: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Runs a specific action defined in the system.

        Args:
            projectId: 
        Returns:
            API response as a dictionary.
        """
        ...

    def run_scheduler_now(
        self,
        projectId: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Executes the scheduler immediately as a manual trigger.

        Args:
            projectId: 
        Returns:
            API response as a dictionary.
        """
        ...

    def trigger_webhook_flow(
        self,
        projectId: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Triggers a webhook flow based on specific events or parameters.

        Args:
            projectId: 
        Returns:
            API response as a dictionary.
        """
        ...

    def update_app_trigger(
        self,
        projectId: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Updates the configurations of an existing application trigger.

        Args:
            projectId: 
        Returns:
            API response as a dictionary.
        """
        ...

    def update_env_config(
        self,
        projectId: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Updates environment configuration settings in the system.

        Args:
            projectId: 
        Returns:
            API response as a dictionary.
        """
        ...

    def update_model_group(
        self,
        projectId: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Updates an existing model group in the system.

        Args:
            projectId: 
        Returns:
            API response as a dictionary.
        """
        ...

    def update_resolver_step(
        self,
        projectId: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Updates an existing resolver step in the workflow.

        Args:
            projectId: 
        Returns:
            API response as a dictionary.
        """
        ...

    def update_scheduler(
        self,
        projectId: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Updates scheduler settings or parameters.

        Args:
            projectId: 
        Returns:
            API response as a dictionary.
        """
        ...

    def update_secrets(
        self,
        projectId: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Updates existing secrets with new values or settings.

        Args:
            projectId: 
        Returns:
            API response as a dictionary.
        """
        ...

    def update_tenant(
        self,
        projectId: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Updates an existing tenant with new information or settings.

        Args:
            projectId: 
        Returns:
            API response as a dictionary.
        """
        ...

    def update_webhook(
        self,
        projectId: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Updates the configuration of an existing webhook.

        Args:
            projectId: 
        Returns:
            API response as a dictionary.
        """
        ...

    def update_webhook_route(
        self,
        projectId: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Updates the route for a specified webhook.

        Args:
            projectId: 
        Returns:
            API response as a dictionary.
        """
        ...

    def widget_connector_status(
        self,
        projectId: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Checks the status of a widget connector in the system.

        Args:
            projectId: 
        Returns:
            API response as a dictionary.
        """
        ...

