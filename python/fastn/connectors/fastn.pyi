"""Fastn fastn connector — auto-generated type stubs.

Do not edit manually. Regenerate with `fastn connector sync`.
"""
from __future__ import annotations

from typing import Any, Dict, List, Optional, TypedDict


class _FastnAddRecordInput(TypedDict, total=False):
    clientId: str
    records: List[Any]
    tableName: str

class _FastnCreateConnectorMapper(TypedDict, total=False):
    authConfig: Dict[str, Any]
    authType: str
    body: str
    headers: List[Any]
    method: str
    params: List[Any]
    url: str

class _FastnCreateConnectorAltMapper(TypedDict, total=False):
    authConfig: Dict[str, Any]
    authType: str
    body: str
    headers: List[Any]
    method: str
    params: List[Any]

class _FastnCreateResolverStepStep(TypedDict, total=False):
    composite: Dict[str, Any]
    debugBreakAfter: int
    enableDebug: bool
    id: str
    next: str
    outputSchema: str
    type: str

class _FastnCreateWebhooksWithRoutesDlqconfigurations(TypedDict, total=False):
    isEnabled: bool
    numberOfRetries: int

class _FastnCreateWebhooksWithRoutesSchedule(TypedDict, total=False):
    enable: bool
    flowHeaders: List[Any]
    flowId: str
    name: str
    payloadJson: Dict[str, Any]
    rate: Dict[str, Any]
    type: str

class _FastnCreateWebhooksWithRoutesSqsconfigurations(TypedDict, total=False):
    accessPrinciple: str
    isEnabled: bool

class _FastnCreateWebhooksWithRoutesV2Dlqconfigurations(TypedDict, total=False):
    isEnabled: bool
    numberOfRetries: int

class _FastnCreateWebhooksWithRoutesV2Schedule(TypedDict, total=False):
    enable: bool
    flowHeaders: List[Any]
    flowId: str
    name: str
    payloadJson: Dict[str, Any]
    rate: Dict[str, Any]
    type: str

class _FastnCreateWebhooksWithRoutesV2Sqsconfigurations(TypedDict, total=False):
    accessPrinciple: str
    isEnabled: bool

class _FastnExecuteCurlInput(TypedDict, total=False):
    command: str
    shouldExecute: bool
    template: bool
    templateHeaders: bool

class _FastnExecuteCurlFastnDomainInput(TypedDict, total=False):
    command: str
    shouldExecute: bool
    template: bool
    templateHeaders: bool

class _FastnGetChartTypeInput(TypedDict, total=False):
    prompt: str

class _FastnTestConnectorApiDatasource(TypedDict, total=False):
    clientId: str
    code: str
    configurationLayer: Dict[str, Any]
    connectorId: str
    contract: Dict[str, Any]
    contractVariables: List[Any]
    groupId: str
    isCommunityCreated: bool
    isConfiguration: bool
    name: str
    type: str

class _FastnTestConnectorApiRequestsettings(TypedDict, total=False):
    turnOffSslVerification: bool

class _FastnUpdateResolverStepStep(TypedDict, total=False):
    composite: Dict[str, Any]
    debugBreakAfter: int
    enableDebug: bool
    id: str
    next: str
    outputSchema: str
    type: str

class _FastnUpdateSchedulerSchedule(TypedDict, total=False):
    apiId: str
    cron: Dict[str, Any]
    enable: str
    headers: List[Any]
    payload: Dict[str, Any]
    rate: Dict[str, Any]
    type: str

class _FastnUpdateWebhookDlqconfigurations(TypedDict, total=False):
    isEnabled: str
    numberOfRetries: str

class _FastnUpdateWebhookModel(TypedDict, total=False):
    id: str

class FastnConnector:
    """fastn connector ().

    Provides 96 tools.
    """

    def create_fastn_db_table(
        self,
        clientId: Optional[str] = None,
        columns: Optional[List[Any]] = None,
        name: Optional[str] = None,
        override: Optional[bool] = None,
    ) -> Dict[str, Any]:
        """Creates a new FastnDB table with specified fields and configurations.

        Args:
            clientId: 
            columns: 
            name: 
            override: 
        Returns:
            API response as a dictionary.
        """
        ...

    def fastn_add_env_configs(
        self,
        configs: Optional[List[Any]] = None,
        projectId: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Adds new environment configuration entries to the specified connector in the Fastn platform via GraphQL. Use this tool when you need to introduce new environment-level settings. This is a write operation that persists new configuration entries. Do not use this tool to update existing configurations — use fastn_update_env_config instead.

        Args:
            configs: 
            projectId: 
        Returns:
            API response as a dictionary.
        """
        ...

    def fastn_add_record(
        self,
        input: Optional[_FastnAddRecordInput] = None,
        projectId: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Inserts a single new record into a specified FastnDB database table via GraphQL. Use this tool when you need to add one row to a table. This is a write operation that persists a new record entry. Do not use this tool to insert multiple records at once — use fastn_add_records_to_db_table instead.

        Args:
            input: 
            projectId: 
        Returns:
            API response as a dictionary.
        """
        ...

    def fastn_add_records_to_db_table(
        self,
        projectId: Optional[str] = None,
        records: Optional[List[Any]] = None,
        tableName: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Inserts multiple records into a specified FastnDB table in a single batch operation via GraphQL. Use this tool when you need to bulk-insert rows into a FastnDB table. This is a write operation that persists new records. Do not use this tool to insert a single record — use fastn_add_record instead, and do not use it to create the table itself — use fastn_create_fastn_db_table instead.

        Args:
            projectId: 
            records: 
            tableName: 
        Returns:
            API response as a dictionary.
        """
        ...

    def fastn_batch_create_webhooks(
        self,
        projectId: Optional[str] = None,
        webhooks: Optional[List[Any]] = None,
    ) -> Dict[str, Any]:
        """Creates multiple webhooks in a single batch operation in the Fastn platform via GraphQL. Use this tool when you need to register several webhooks at once efficiently. This is a write operation that persists multiple new webhook entries. Do not use this tool to create webhooks with routing rules — use fastn_create_webhooks_with_routes instead.

        Args:
            projectId: 
            webhooks: 
        Returns:
            API response as a dictionary.
        """
        ...

    def fastn_batch_import_templates(
        self,
        projectId: Optional[str] = None,
        templates: Optional[List[Any]] = None,
    ) -> Dict[str, Any]:
        """Imports multiple templates into the Fastn platform in a single batch operation via GraphQL. Use this tool when you need to onboard several templates at once. This is a write operation that persists new template entries. Do not use this tool to import a single flow template — use fastn_import_flow_template instead.

        Args:
            projectId: 
            templates: 
        Returns:
            API response as a dictionary.
        """
        ...

    def fastn_build_flow(
        self,
        Name: Optional[str] = None,
        clientId: Optional[str] = None,
        projectId: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Builds a workflow flow in the Fastn platform based on specified parameters and actions via GraphQL. Use this tool when you need to construct or assemble a flow definition. This is a write operation that creates or modifies the flow structure. Do not use this tool to validate a flow graph — use fastn_validate_workflow_graph first.

        Args:
            Name: 
            clientId: 
            projectId: 
        Returns:
            API response as a dictionary.
        """
        ...

    def fastn_create_app_trigger(
        self,
        accountId: Optional[str] = None,
        connectorId: Optional[str] = None,
        connectorImage: Optional[str] = None,
        connectorName: Optional[str] = None,
        event: Optional[str] = None,
        flowId: Optional[str] = None,
        headers: Optional[List[Any]] = None,
        projectId: Optional[str] = None,
        tenantId: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Creates a new application trigger in the Fastn platform for specified conditions via GraphQL. Use this tool when you need to register a new event-based or scheduled trigger for an application. This is a write operation that persists a new trigger entry. Do not use this tool to update an existing trigger — use fastn_update_app_trigger instead.

        Args:
            accountId: 
            connectorId: 
            connectorImage: 
            connectorName: 
            event: 
            flowId: 
            headers: 
            projectId: 
            tenantId: 
        Returns:
            API response as a dictionary.
        """
        ...

    def fastn_create_app_v3(
        self,
        description: Optional[str] = None,
        name: Optional[str] = None,
        roles: Optional[List[Any]] = None,
        type: Optional[str] = None,
        xfabricchannelid: Optional[str] = None,
        xfabrictenantid: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Creates a new application in the Fastn platform using the V3 App Connector via the Identity Management API. Use this tool when you need to register a new app with V3-level capabilities. This is a write operation that persists a new app entry. Do not use this tool to create V1 or V2 widgets — use fastn_create_widget or fastn_create_widget_v2 instead.

        Args:
            description: 
            name: 
            roles: 
            type: 
            xfabricchannelid: 
            xfabrictenantid: 
        Returns:
            API response as a dictionary.
        """
        ...

    def fastn_create_connector(
        self,
        clientId: Optional[str] = None,
        connectorId: Optional[str] = None,
        groupId: Optional[str] = None,
        mapper: Optional[_FastnCreateConnectorMapper] = None,
        name: Optional[str] = None,
        projectId: Optional[str] = None,
        reqSchema: Optional[Dict[str, Any]] = None,
        reqUiSchema: Optional[Dict[str, Any]] = None,
        successSchema: Optional[Dict[str, Any]] = None,
        successUiSchema: Optional[Dict[str, Any]] = None,
    ) -> Dict[str, Any]:
        """Creates a new connector with specified settings in the Fastn platform via GraphQL at the api.{domain}/graphql endpoint. Use this tool when you need to register a new connector integration. This is a write operation that persists a new connector entry. Do not confuse this with the other fastn_create_connector variant that targets the api.{domain}/graphql endpoint with a different connection context.

        Args:
            clientId: 
            connectorId: 
            groupId: 
            mapper: 
            name: 
            projectId: 
            reqSchema: 
            reqUiSchema: 
            successSchema: 
            successUiSchema: 
        Returns:
            API response as a dictionary.
        """
        ...

    def fastn_create_connector_alt(
        self,
        clientId: Optional[str] = None,
        code: Optional[str] = None,
        connectorId: Optional[str] = None,
        groupId: Optional[str] = None,
        mapper: Optional[_FastnCreateConnectorAltMapper] = None,
        name: Optional[str] = None,
        projectId: Optional[str] = None,
        reqSchema: Optional[Dict[str, Any]] = None,
        reqUiSchema: Optional[Dict[str, Any]] = None,
        successSchema: Optional[Dict[str, Any]] = None,
        successUiSchema: Optional[Dict[str, Any]] = None,
        type: Optional[str] = None,
        url: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Creates a new connector with specified settings in the Fastn platform via GraphQL at the api.{domain}/graphql endpoint (alternate context). Use this tool when you need to register a new connector in an alternate connection context. This is a write operation that persists a new connector entry. Do not confuse this with fastn_create_connector which uses a different domain or connection context.

        Args:
            clientId: 
            code: 
            connectorId: 
            groupId: 
            mapper: 
            name: 
            projectId: 
            reqSchema: 
            reqUiSchema: 
            successSchema: 
            successUiSchema: 
            type: 
            url: 
        Returns:
            API response as a dictionary.
        """
        ...

    def fastn_create_external_db_api(
        self,
        actionType: Optional[str] = None,
        actions: Optional[List[Any]] = None,
        clientId: Optional[str] = None,
        connectionId: Optional[str] = None,
        name: Optional[str] = None,
        projectId: Optional[str] = None,
        tabelName: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Creates a new API endpoint for an external database connection in the Fastn platform via GraphQL. Use this tool when you need to expose an external database table or query as a Fastn API. This is a write operation that persists a new API entry. Do not use this tool to create the database connection itself — use fastn_create_external_db_connection instead.

        Args:
            actionType: 
            actions: 
            clientId: 
            connectionId: 
            name: 
            projectId: 
            tabelName: 
        Returns:
            API response as a dictionary.
        """
        ...

    def fastn_create_external_db_connection(
        self,
        clientId: Optional[str] = None,
        connectionName: Optional[str] = None,
        dbHost: Optional[str] = None,
        dbName: Optional[str] = None,
        dbPassword: Optional[str] = None,
        dbUserName: Optional[str] = None,
        projectId: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Creates a new external database connection in the Fastn platform via GraphQL. Use this tool when you need to register a new external database (e.g., PostgreSQL, MySQL) for use in flows or APIs. This is a write operation that persists the connection credentials and configuration. Do not use this tool to create an API on top of the connection — use fastn_create_external_db_api instead.

        Args:
            clientId: 
            connectionName: 
            dbHost: 
            dbName: 
            dbPassword: 
            dbUserName: 
            projectId: 
        Returns:
            API response as a dictionary.
        """
        ...

    def fastn_create_fastn_db_table(
        self,
        input___shape: str,
        clientId: Optional[str] = None,
        columns: Optional[List[Any]] = None,
        name: Optional[str] = None,
        override: Optional[bool] = None,
    ) -> Dict[str, Any]:
        """Creates a new FastnDB table with a defined schema in the Fastn platform via GraphQL. Use this tool when you need to provision a new table for storing structured data. This is a write operation that persists a new table definition. Do not use this tool to add records to the table — use fastn_add_record or fastn_add_records_to_db_table instead.

        Args:
            input___shape:  (required)
            clientId: 
            columns: 
            name: 
            override: 
        Returns:
            API response as a dictionary.
        """
        ...

    def fastn_create_fastn_db_table_v2(
        self,
        clientId: Optional[str] = None,
        columns: Optional[List[Any]] = None,
        name: Optional[str] = None,
        override: Optional[bool] = None,
    ) -> Dict[str, Any]:
        """Creates a new FastnDB table with specified fields and configurations in the Fastn platform via GraphQL. Use this tool when you need to provision a new table with explicit field definitions. This is a write operation that persists a new table schema. Do not confuse this with fastn_create_fastn_db_table which may use a different schema format or context.

        Args:
            clientId: 
            columns: 
            name: 
            override: 
        Returns:
            API response as a dictionary.
        """
        ...

    def fastn_create_internal_db_api(
        self,
        actions: Optional[List[Any]] = None,
        flowName: Optional[str] = None,
        projectId: Optional[str] = None,
        tableName: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Creates an internal API for FastnDB operations in the Fastn platform via GraphQL. Use this tool when you need to expose a FastnDB table or query as a managed internal API endpoint. This is a write operation that persists a new API entry. Do not use this tool for external database APIs — use fastn_create_external_db_api instead.

        Args:
            actions: 
            flowName: 
            projectId: 
            tableName: 
        Returns:
            API response as a dictionary.
        """
        ...

    def fastn_create_model_group(
        self,
        body: Dict[str, Any],
        projectId: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Creates a new model group with specified configurations in the Fastn platform via GraphQL. Use this tool when you need to organize models into a logical group. This is a write operation that persists a new model group entry. Do not use this tool to delete a model — use fastn_delete_model instead.

        Args:
            body:  (required)
            projectId: 
        Returns:
            API response as a dictionary.
        """
        ...

    def fastn_create_project(
        self,
        projectId: Optional[str] = None,
        projectName: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Creates a new project in the Fastn platform with specified configurations via GraphQL. Use this tool when you need to set up a new project workspace. This is a write operation that persists a new project entry. Do not use this tool to retrieve an existing project — use fastn_get_project instead.

        Args:
            projectId: 
            projectName: 
        Returns:
            API response as a dictionary.
        """
        ...

    def fastn_create_resolver_step(
        self,
        clientId: Optional[str] = None,
        expression: Optional[int] = None,
        id: Optional[str] = None,
        isDefault: Optional[bool] = None,
        nodeId: Optional[str] = None,
        parentIds: Optional[List[Any]] = None,
        projectId: Optional[str] = None,
        step: Optional[_FastnCreateResolverStepStep] = None,
    ) -> Dict[str, Any]:
        """Creates a new resolver step within a Fastn workflow via GraphQL. Use this tool when you need to add a data resolution step to an existing workflow. This is a write operation that persists a new resolver step. Do not use this tool to update an existing step — use fastn_update_resolver_step instead.

        Args:
            clientId: 
            expression: 
            id: 
            isDefault: 
            nodeId: 
            parentIds: 
            projectId: 
            step: 
        Returns:
            API response as a dictionary.
        """
        ...

    def fastn_create_secret_with_api_key(
        self,
        ApiKey: Optional[str] = None,
        domain: Optional[str] = None,
        projectId: Optional[str] = None,
        secrets: Optional[List[Any]] = None,
    ) -> Dict[str, Any]:
        """Creates a new secret in the Fastn platform and associates it with a provided API key, using a GraphQL mutation. Use this tool when you need to securely store credentials tied to an API key. This is a write operation that persists a new secret entry. Do not use this tool to update an existing secret — use fastn_update_secrets instead.

        Args:
            ApiKey: 
            domain: 
            projectId: 
            secrets: 
        Returns:
            API response as a dictionary.
        """
        ...

    def fastn_create_secret_with_api_key_v2(
        self,
        ApiKey: Optional[str] = None,
        domain: Optional[str] = None,
        projectId: Optional[str] = None,
        secrets: Optional[List[Any]] = None,
    ) -> Dict[str, Any]:
        """Creates a new secret associated with a provided API key in the Fastn platform via GraphQL using the connection-scoped domain. Use this tool when you need to securely store credentials tied to an API key in a connection context. This is a write operation that persists a new secret entry. Do not use this tool to update an existing secret — use fastn_update_secrets instead.

        Args:
            ApiKey: 
            domain: 
            projectId: 
            secrets: 
        Returns:
            API response as a dictionary.
        """
        ...

    def fastn_create_secrets(
        self,
        customAuth: Optional[str] = None,
        discriminator: Optional[str] = None,
        projectId: Optional[str] = None,
        secrets: Optional[List[Any]] = None,
        tenantId: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Creates one or more secrets to securely store sensitive information in the Fastn platform via GraphQL. Use this tool when you need to provision new secret entries. This is a write operation that persists new secret values. Do not use this tool to update existing secrets — use fastn_update_secrets instead.

        Args:
            customAuth: 
            discriminator: 
            projectId: 
            secrets: 
            tenantId: 
        Returns:
            API response as a dictionary.
        """
        ...

    def fastn_create_table(
        self,
        columns: Optional[List[Any]] = None,
        name: Optional[str] = None,
        projectId: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Creates a new table within a specified database in the Fastn platform via GraphQL. Use this tool when you need to add a new table to an existing database. This is a write operation that persists a new table schema. Do not use this tool to create a FastnDB-specific table — use fastn_create_fastn_db_table instead.

        Args:
            columns: 
            name: 
            projectId: 
        Returns:
            API response as a dictionary.
        """
        ...

    def fastn_create_tenant(
        self,
        id: Optional[str] = None,
        name: Optional[str] = None,
        projectId: Optional[str] = None,
        secret: Optional[Dict[str, Any]] = None,
    ) -> Dict[str, Any]:
        """Creates a new tenant in the Fastn platform with specified parameters via GraphQL. Use this tool when you need to onboard a new tenant into the system. This is a write operation that persists a new tenant entry. Do not use this tool to update an existing tenant — use fastn_update_tenant instead.

        Args:
            id: 
            name: 
            projectId: 
            secret: 
        Returns:
            API response as a dictionary.
        """
        ...

    def fastn_create_webhooks_with_routes(
        self,
        autoGenerateApiKey: Optional[bool] = None,
        dlqConfigurations: Optional[_FastnCreateWebhooksWithRoutesDlqconfigurations] = None,
        isAuthenticated: Optional[bool] = None,
        isAuthenticated_: Optional[str] = None,
        projectId: Optional[str] = None,
        routes: Optional[List[Any]] = None,
        schedule: Optional[_FastnCreateWebhooksWithRoutesSchedule] = None,
        sqsConfigurations: Optional[_FastnCreateWebhooksWithRoutesSqsconfigurations] = None,
        webhookId: Optional[str] = None,
        webhookName: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Creates one or more new webhooks with associated routing rules in the Fastn platform via GraphQL. Use this tool when you need to register webhooks that include specific route configurations for event handling. This is a write operation that persists new webhook entries. Do not use this tool to update existing webhooks — use fastn_update_webhook instead.

        Args:
            autoGenerateApiKey: 
            dlqConfigurations: 
            isAuthenticated: 
            isAuthenticated_: 
            projectId: 
            routes: 
            schedule: 
            sqsConfigurations: 
            webhookId: 
            webhookName: 
        Returns:
            API response as a dictionary.
        """
        ...

    def fastn_create_webhooks_with_routes_v2(
        self,
        autoGenerateApiKey: Optional[bool] = None,
        dlqConfigurations: Optional[_FastnCreateWebhooksWithRoutesV2Dlqconfigurations] = None,
        isAuthenticated: Optional[bool] = None,
        isAuthenticated_: Optional[str] = None,
        projectId: Optional[str] = None,
        routes: Optional[List[Any]] = None,
        schedule: Optional[_FastnCreateWebhooksWithRoutesV2Schedule] = None,
        sqsConfigurations: Optional[_FastnCreateWebhooksWithRoutesV2Sqsconfigurations] = None,
        webhookId: Optional[str] = None,
        webhookName: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Creates one or more new webhooks with associated routing rules in the Fastn platform via GraphQL (auth-scoped domain). Use this tool when you need to register webhooks that include specific route configurations for event handling in the auth context. This is a write operation that persists new webhook entries. Do not use this tool to update existing webhooks — use fastn_update_webhook instead.

        Args:
            autoGenerateApiKey: 
            dlqConfigurations: 
            isAuthenticated: 
            isAuthenticated_: 
            projectId: 
            routes: 
            schedule: 
            sqsConfigurations: 
            webhookId: 
            webhookName: 
        Returns:
            API response as a dictionary.
        """
        ...

    def fastn_create_widget_v2(
        self,
        actions: Optional[List[Any]] = None,
        active: Optional[bool] = None,
        connectedConnectors: Optional[List[Any]] = None,
        connectorId: Optional[str] = None,
        connectorName: Optional[str] = None,
        content: Optional[str] = None,
        dataFlowLabel: Optional[str] = None,
        description: Optional[str] = None,
        descrtiption: Optional[str] = None,
        events: Optional[List[Any]] = None,
        id: Optional[str] = None,
        imageUri: Optional[str] = None,
        images: Optional[List[Any]] = None,
        isTenantScopeEnabled: Optional[bool] = None,
        labels: Optional[List[Any]] = None,
        name: Optional[str] = None,
        projectId: Optional[str] = None,
        starterActions: Optional[str] = None,
        tenantScope: Optional[List[Any]] = None,
        widgetType: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Creates a new widget in the Fastn platform using version 2 specifications via GraphQL. Use this tool when you need to provision a V2 widget with its configuration and layout. This is a write operation that persists a new widget entry. Do not use this tool for V1 widget creation — use fastn_create_widget instead.

        Args:
            actions: 
            active: 
            connectedConnectors: 
            connectorId: 
            connectorName: 
            content: 
            dataFlowLabel: 
            description: 
            descrtiption: 
            events: 
            id: 
            imageUri: 
            images: 
            isTenantScopeEnabled: 
            labels: 
            name: 
            projectId: 
            starterActions: 
            tenantScope: 
            widgetType: 
        Returns:
            API response as a dictionary.
        """
        ...

    def fastn_create_widgets(
        self,
        actiavteFlow: Optional[str] = None,
        clientId: Optional[str] = None,
        connectedConnectorsArray: Optional[List[Any]] = None,
        content: Optional[str] = None,
        deActiavteFlow: Optional[str] = None,
        description: Optional[str] = None,
        imageUri: Optional[str] = None,
        name: Optional[str] = None,
        projectId: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Creates multiple new widgets in the Fastn platform in a single operation via GraphQL. Use this tool when you need to provision several widgets at once. This is a write operation that persists multiple new widget entries. Do not use this tool to create a single widget — use fastn_create_widget or fastn_create_widget_v2 instead.

        Args:
            actiavteFlow: 
            clientId: 
            connectedConnectorsArray: 
            content: 
            deActiavteFlow: 
            description: 
            imageUri: 
            name: 
            projectId: 
        Returns:
            API response as a dictionary.
        """
        ...

    def fastn_delete_api(
        self,
        id: Optional[str] = None,
        projectId: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Permanently deletes an API from the Fastn platform via GraphQL. Use this tool when an API definition is no longer needed and must be removed. This operation is irreversible — the API cannot be recovered after deletion. Do not use this tool to delete an API key — use fastn_delete_api_key instead.

        Args:
            id: 
            projectId: 
        Returns:
            API response as a dictionary.
        """
        ...

    def fastn_delete_api_key(
        self,
        ApiKey: Optional[str] = None,
        Authorization: Optional[str] = None,
        domain: Optional[str] = None,
        projectId: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Permanently deletes an existing API key from the Fastn platform via GraphQL. Use this tool when an API key is no longer needed and must be revoked. This operation is irreversible — the key cannot be recovered after deletion. Do not use this tool to generate a new API key — use fastn_generate_api_key instead.

        Args:
            ApiKey: 
            Authorization: 
            domain: 
            projectId: 
        Returns:
            API response as a dictionary.
        """
        ...

    def fastn_delete_app_trigger(
        self,
        appTriggerId: Optional[str] = None,
        projectId: Optional[str] = None,
        withResources: Optional[bool] = None,
    ) -> Dict[str, Any]:
        """Permanently deletes a specified application trigger from the Fastn platform via GraphQL. Use this tool when a trigger is no longer needed and must be removed. This operation is irreversible — the trigger cannot be recovered after deletion. Do not use this tool to update a trigger — use fastn_update_app_trigger instead.

        Args:
            appTriggerId: 
            projectId: 
            withResources: 
        Returns:
            API response as a dictionary.
        """
        ...

    def fastn_delete_env_configuration(
        self,
        key: Optional[str] = None,
        projectId: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Permanently deletes an environment configuration entry from the Fastn platform via GraphQL. Use this tool when a configuration entry is no longer needed. This operation is irreversible — the configuration cannot be recovered after deletion. Do not use this tool to update a configuration — use fastn_update_env_config instead.

        Args:
            key: 
            projectId: 
        Returns:
            API response as a dictionary.
        """
        ...

    def fastn_delete_model(
        self,
        id: Optional[str] = None,
        projectId: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Permanently deletes a model from the specified connector in the Fastn platform via GraphQL. Use this tool when a model is no longer needed and must be removed. This operation is irreversible — the model cannot be recovered after deletion. Do not use this tool to delete other resource types such as APIs or webhooks.

        Args:
            id: 
            projectId: 
        Returns:
            API response as a dictionary.
        """
        ...

    def fastn_delete_model_v2(
        self,
        id: Optional[str] = None,
        projectId: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Permanently deletes a model from the specified connector in the Fastn platform via GraphQL (auth-scoped domain). Use this tool when a model is no longer needed and must be removed. This operation is irreversible — the model cannot be recovered after deletion. Do not use this tool to delete other resource types such as APIs or webhooks.

        Args:
            id: 
            projectId: 
        Returns:
            API response as a dictionary.
        """
        ...

    def fastn_delete_secret(
        self,
        discriminator: Optional[str] = None,
        projectId: Optional[str] = None,
        secretKey: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Permanently deletes a secret from the Fastn platform via GraphQL. Use this tool when a stored secret is no longer needed. This operation is irreversible — the secret cannot be recovered after deletion. Do not use this tool to update a secret — use fastn_update_secrets instead.

        Args:
            discriminator: 
            projectId: 
            secretKey: 
        Returns:
            API response as a dictionary.
        """
        ...

    def fastn_delete_webhook(
        self,
        id: Optional[str] = None,
        projectId: Optional[str] = None,
        withResources: Optional[bool] = None,
    ) -> Dict[str, Any]:
        """Permanently deletes an existing webhook from the Fastn platform via GraphQL. Use this tool when a webhook registration is no longer needed. This operation is irreversible — the webhook cannot be recovered after deletion. Do not use this tool to update a webhook — use fastn_update_webhook instead.

        Args:
            id: 
            projectId: 
            withResources: 
        Returns:
            API response as a dictionary.
        """
        ...

    def fastn_delete_webhook_v2(
        self,
        id: Optional[str] = None,
        projectId: Optional[str] = None,
        withResources: Optional[bool] = None,
    ) -> Dict[str, Any]:
        """Permanently deletes an existing webhook from the Fastn platform via GraphQL (auth-scoped domain). Use this tool when a webhook registration is no longer needed. This operation is irreversible — the webhook cannot be recovered after deletion. Do not use this tool to update a webhook — use fastn_update_webhook instead.

        Args:
            id: 
            projectId: 
            withResources: 
        Returns:
            API response as a dictionary.
        """
        ...

    def fastn_execute_curl(
        self,
        input: Optional[_FastnExecuteCurlInput] = None,
        projectId: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Executes a raw curl-style HTTP request through the Fastn platform via GraphQL at the api.{domain}/graphql endpoint. Use this tool when you need to make a custom HTTP call not covered by other tools. This is a side-effect operation that sends a live network request. Do not confuse this with the other fastn_execute_curl variant that targets the api.{domain}.fastn.ai endpoint.

        Args:
            input: 
            projectId: 
        Returns:
            API response as a dictionary.
        """
        ...

    def fastn_execute_curl_fastn_domain(
        self,
        authorization: Optional[str] = None,
        input: Optional[_FastnExecuteCurlFastnDomainInput] = None,
        projectId: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Executes a raw curl-style HTTP request through the Fastn platform via GraphQL at the api.{domain}.fastn.ai/graphql endpoint. Use this tool when you need to make a custom HTTP call targeting the fastn.ai-suffixed domain. This is a side-effect operation that sends a live network request. Do not confuse this with the other fastn_execute_curl variant that targets the api.{domain}/graphql endpoint without the fastn.ai suffix.

        Args:
            authorization: 
            input: 
            projectId: 
        Returns:
            API response as a dictionary.
        """
        ...

    def fastn_generate_api_key(
        self,
        allowedOrigins: Optional[List[Any]] = None,
        allowedTenants: Optional[List[Any]] = None,
        apiScopes: Optional[List[Any]] = None,
        expiresAt: Optional[str] = None,
        name: Optional[str] = None,
        projectId: Optional[str] = None,
        webhookScopes: Optional[List[Any]] = None,
        workflowScopes: Optional[List[Any]] = None,
    ) -> Dict[str, Any]:
        """Generates a new API key for accessing Fastn platform resources via GraphQL. Use this tool when you need to provision a new API key for a user or application. This is a write operation that creates and persists a new key. Do not use this tool to list existing API keys — use fastn_list_api_keys instead.

        Args:
            allowedOrigins: 
            allowedTenants: 
            apiScopes: 
            expiresAt: 
            name: 
            projectId: 
            webhookScopes: 
            workflowScopes: 
        Returns:
            API response as a dictionary.
        """
        ...

    def fastn_generate_auth_token(
        self,
    ) -> Dict[str, Any]:
        """Generates an authentication token for user or application access in the Fastn platform via the OpenID Connect token endpoint. Use this tool when you need to obtain a bearer token for authenticating subsequent API calls. This is a write operation that issues a new token credential. Do not use this tool to retrieve an existing connector token — use fastn_get_connector_token instead.
        Returns:
            API response as a dictionary.
        """
        ...

    def fastn_generate_token(
        self,
        connectorId: Optional[str] = None,
        orgId: Optional[str] = None,
        projectId: Optional[str] = None,
        refresh: Optional[str] = None,
        tenantId: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Generates a new authentication token for use with Fastn platform resources via GraphQL. Use this tool when a new token is required for API or connector access. This is a write operation that creates a new token credential. Do not use this tool to retrieve an existing connector token — use fastn_get_connector_token instead.

        Args:
            connectorId: 
            orgId: 
            projectId: 
            refresh: 
            tenantId: 
        Returns:
            API response as a dictionary.
        """
        ...

    def fastn_get_action_by_id(
        self,
        actionId: Optional[str] = None,
        clientId: Optional[str] = None,
        connectorId: Optional[str] = None,
        projectId: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Retrieves configuration and metadata details for a specific action identified by its unique ID in the Fastn platform via GraphQL. Use this tool when you need to inspect a single actions definition or settings. Do not use this tool to execute an action — use fastn_run_action instead.

        Args:
            actionId: 
            clientId: 
            connectorId: 
            projectId: 
        Returns:
            API response as a dictionary.
        """
        ...

    def fastn_get_active_connector_status(
        self,
        connectorId: Optional[str] = None,
        projectId: Optional[str] = None,
        tenantId: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Retrieves the active status of a connector in the Fastn platform via GraphQL. Use this tool when you need to verify whether a specific connector is currently active or inactive. Do not use this tool for widget connector status — use fastn_get_widget_connector_status instead.

        Args:
            connectorId: 
            projectId: 
            tenantId: 
        Returns:
            API response as a dictionary.
        """
        ...

    def fastn_get_api(
        self,
        id: str,
        projectId: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Retrieves configuration and metadata details about a specified API in the Fastn platform via GraphQL. Use this tool when you need to inspect a single APIs settings, routes, or status. Do not use this tool to list all APIs — use fastn_list_apis instead.

        Args:
            id:  (required)
            projectId: 
        Returns:
            API response as a dictionary.
        """
        ...

    def fastn_get_api_v2(
        self,
        id: str,
        projectId: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Retrieves configuration and metadata details about a specified API in the Fastn platform via GraphQL (auth-scoped domain). Use this tool when you need to inspect a single APIs settings, routes, or status. Do not use this tool to list all APIs — use fastn_list_apis instead.

        Args:
            id:  (required)
            projectId: 
        Returns:
            API response as a dictionary.
        """
        ...

    def fastn_get_app_trigger(
        self,
        id: Optional[str] = None,
        projectId: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Retrieves configuration details for a specific application trigger in the Fastn platform via GraphQL. Use this tool when you need to inspect a single triggers settings or conditions. Do not use this tool to list all triggers — use fastn_list_app_triggers instead.

        Args:
            id: 
            projectId: 
        Returns:
            API response as a dictionary.
        """
        ...

    def fastn_get_chart_type(
        self,
        authorization: Optional[str] = None,
        input: Optional[_FastnGetChartTypeInput] = None,
        x_fastn_space_connection_id: Optional[str] = None,
        x_fastn_space_id: Optional[str] = None,
        x_fastn_space_tenantid: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Retrieves the chart type for a specified version from the Fastn platform. Use this tool when you need to determine which chart type is associated with a given versioned resource. Do not use this tool to update or delete chart types.

        Args:
            authorization: 
            input: Free form JSON
            x_fastn_space_connection_id: 
            x_fastn_space_id: 
            x_fastn_space_tenantid: 
        Returns:
            API response as a dictionary.
        """
        ...

    def fastn_get_connector_group_info(
        self,
        groupId: Optional[str] = None,
        projectId: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Retrieves detailed information about a specific connector group in the Fastn platform via GraphQL. Use this tool when you need to inspect a groups configuration, membership, or metadata. Do not use this tool to list all connector groups — use fastn_list_connector_groups instead.

        Args:
            groupId: 
            projectId: 
        Returns:
            API response as a dictionary.
        """
        ...

    def fastn_get_connector_info(
        self,
        clientId: Optional[str] = None,
        connectorId: Optional[str] = None,
        id: Optional[str] = None,
        projectId: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Retrieves detailed configuration and metadata information about a specified connector in the Fastn platform via GraphQL. Use this tool when you need to inspect a connectors settings, type, or status. Do not use this tool to list all connector groups — use fastn_list_connector_groups instead.

        Args:
            clientId: 
            connectorId: 
            id: 
            projectId: 
        Returns:
            API response as a dictionary.
        """
        ...

    def fastn_get_connector_token(
        self,
        connectionId: Optional[str] = None,
        connectorId: Optional[str] = None,
        customAuth: Optional[str] = None,
        orgId: Optional[str] = None,
        projectId: Optional[str] = None,
        tenantId: Optional[str] = None,
        toRefresh: Optional[bool] = None,
    ) -> Dict[str, Any]:
        """Retrieves the authentication token associated with a specified connector in the Fastn platform via GraphQL. Use this tool when you need the token to authenticate calls made through a specific connector. Do not use this tool to generate a new token — use fastn_generate_token instead.

        Args:
            connectionId: 
            connectorId: 
            customAuth: 
            orgId: 
            projectId: 
            tenantId: 
            toRefresh: 
        Returns:
            API response as a dictionary.
        """
        ...

    def fastn_get_flow_schema(
        self,
        clientId: Optional[str] = None,
        id: Optional[str] = None,
        nodeId: Optional[str] = None,
        parentIds: Optional[List[Any]] = None,
        projectId: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Retrieves the schema definition for a specified flow in the Fastn platform via GraphQL. Use this tool when you need to inspect the input/output structure or configuration schema of a flow. Do not use this tool to build or execute a flow — use fastn_build_flow or fastn_run_action instead.

        Args:
            clientId: 
            id: 
            nodeId: 
            parentIds: 
            projectId: 
        Returns:
            API response as a dictionary.
        """
        ...

    def fastn_get_project(
        self,
        projectId: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Retrieves configuration and metadata details about a specified project in the Fastn platform via GraphQL. Use this tool when you need to inspect a single projects settings or status. Do not use this tool to create a new project — use fastn_create_project instead.

        Args:
            projectId: 
        Returns:
            API response as a dictionary.
        """
        ...

    def fastn_get_user_by_token(
        self,
        authorization: Optional[str] = None,
        domain: Optional[str] = None,
        realm: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Retrieves user profile details associated with a specified authentication token from the OpenID Connect userinfo endpoint. Use this tool when you need to look up the identity of a user based on their token. Do not use this tool to generate a new token — use fastn_generate_auth_token instead.

        Args:
            authorization: 
            domain: 
            realm: 
        Returns:
            API response as a dictionary.
        """
        ...

    def fastn_get_webhook(
        self,
        webhookId: str,
        projectId: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Retrieves configuration and metadata details of a specific webhook in the Fastn platform via GraphQL using the auth-scoped domain. Use this tool when you need to inspect a single webhooks settings. Do not use this tool to list all webhooks — use fastn_list_webhooks instead, and do not confuse this with fastn_get_webhook_by_connection which uses the connection-scoped domain.

        Args:
            webhookId:  (required)
            projectId: 
        Returns:
            API response as a dictionary.
        """
        ...

    def fastn_get_webhook_by_connection(
        self,
        webhookId: str,
        authorization: Optional[str] = None,
        domain: Optional[str] = None,
        projectId: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Retrieves details of a specific webhook using the connection-scoped GraphQL endpoint in the Fastn platform. Use this tool when you need to look up a webhook within a specific connection context. Do not confuse this with fastn_get_webhook which uses the auth-scoped domain endpoint.

        Args:
            webhookId:  (required)
            authorization: 
            domain: 
            projectId: 
        Returns:
            API response as a dictionary.
        """
        ...

    def fastn_get_widget_connector_status(
        self,
        connectorId: Optional[str] = None,
        isDependencyConnector: Optional[bool] = None,
        projectId: Optional[str] = None,
        tenantId: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Retrieves the current status of a widget connector in the Fastn platform via GraphQL. Use this tool when you need to check whether a widget connector is active, inactive, or in an error state. Do not use this tool for V2 widget connector status — use fastn_get_widget_connector_status_v2 instead.

        Args:
            connectorId: 
            isDependencyConnector: 
            projectId: 
            tenantId: 
        Returns:
            API response as a dictionary.
        """
        ...

    def fastn_get_widget_connector_status_auth(
        self,
        connectorId: Optional[str] = None,
        projectId: Optional[str] = None,
        tenantId: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Retrieves the status of a widget connector in the Fastn platform via GraphQL using the auth-scoped domain. Use this tool when you need to check a widget connectors state within the auth context. Do not confuse this with fastn_get_widget_connector_status_connection which uses the connection-scoped domain.

        Args:
            connectorId: 
            projectId: 
            tenantId: 
        Returns:
            API response as a dictionary.
        """
        ...

    def fastn_get_widget_connector_status_connection(
        self,
        authorization: Optional[str] = None,
        connections: Optional[List[Any]] = None,
        connectorId: Optional[str] = None,
        customAuth: Optional[str] = None,
        domain: Optional[str] = None,
        projectId: Optional[str] = None,
        tenantId: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Retrieves the status of a widget connector in the Fastn platform via GraphQL using the connection-scoped domain. Use this tool when you need to check a widget connectors state within a specific connection context. Do not confuse this with fastn_get_widget_connector_status_auth which uses the auth-scoped domain.

        Args:
            authorization: 
            connections: 
            connectorId: 
            customAuth: 
            domain: 
            projectId: 
            tenantId: 
        Returns:
            API response as a dictionary.
        """
        ...

    def fastn_get_widget_connector_status_v2(
        self,
        connectorId: Optional[str] = None,
        projectId: Optional[str] = None,
        tenantId: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Retrieves the current status of a widget connector using the version 2 API in the Fastn platform via GraphQL. Use this tool when you need to check whether a V2 widget connector is active, inactive, or in an error state. Do not use this tool for V1 widget connector status — use fastn_get_widget_connector_status instead.

        Args:
            connectorId: 
            projectId: 
            tenantId: 
        Returns:
            API response as a dictionary.
        """
        ...

    def fastn_import_collection_from_postman(
        self,
        clientId: Optional[str] = None,
        collection: Optional[str] = None,
        collectionType: Optional[str] = None,
        collectionUrl: Optional[str] = None,
        connectorId: Optional[str] = None,
        env: Optional[str] = None,
        execute: Optional[bool] = None,
        groupId: Optional[str] = None,
        projectId: Optional[str] = None,
        templateBody: Optional[bool] = None,
        templateHeaders: Optional[bool] = None,
        templateQueryParams: Optional[bool] = None,
        version: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Imports an API collection from Postman into the Fastn platform via GraphQL, converting it for API management use. Use this tool when you want to onboard existing Postman collections as Fastn APIs. This is a write operation that creates new API entries in the system. Do not use this tool to import flow templates — use fastn_import_flow_template instead.

        Args:
            clientId: 
            collection: 
            collectionType: 
            collectionUrl: 
            connectorId: 
            env: 
            execute: 
            groupId: 
            projectId: 
            templateBody: 
            templateHeaders: 
            templateQueryParams: 
            version: 
        Returns:
            API response as a dictionary.
        """
        ...

    def fastn_import_flow_template(
        self,
        deployTo: Optional[str] = None,
        flowName: Optional[str] = None,
        organizationId: Optional[str] = None,
        projectId: Optional[str] = None,
        templateId: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Imports a single flow template into the Fastn platform via GraphQL to enable quick workflow setup. Use this tool when you need to onboard a pre-built flow template. This is a write operation that persists a new template entry. Do not use this tool to import multiple templates at once — use fastn_batch_import_templates instead.

        Args:
            deployTo: 
            flowName: 
            organizationId: 
            projectId: 
            templateId: 
        Returns:
            API response as a dictionary.
        """
        ...

    def fastn_invite_user(
        self,
        email: Optional[str] = None,
        projectId: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Sends an invitation to a new user to join the Fastn platform via GraphQL. Use this tool when you need to onboard a new user by email. This is a write operation that creates an invitation and may trigger an email notification to the invitee. Do not use this tool to update an existing users settings.

        Args:
            email: 
            projectId: 
        Returns:
            API response as a dictionary.
        """
        ...

    def fastn_invoke_connector_action(
        self,
        agentId: Optional[str] = None,
        connectorActionId: Optional[str] = None,
        connectorId: Optional[str] = None,
        orgId: Optional[str] = None,
        payload: Optional[str] = None,
        projectId: Optional[str] = None,
        tenantId: Optional[str] = None,
        timeoutInMilliSeconds: Optional[int] = None,
        turnOffSslVerification_: Optional[bool] = None,
    ) -> Dict[str, Any]:
        """Invokes a specific action on a Fastn connector via GraphQL. Use this tool when you need to trigger a connector-level operation directly. This is a write/side-effect operation — the action executes immediately and may modify external system state. Do not use this tool to run a platform-level action — use fastn_run_action instead.

        Args:
            agentId: 
            connectorActionId: 
            connectorId: 
            orgId: 
            payload: 
            projectId: 
            tenantId: 
            timeoutInMilliSeconds: 
            turnOffSslVerification_: 
        Returns:
            API response as a dictionary.
        """
        ...

    def fastn_list_api_keys(
        self,
        projectId: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Returns a list of all existing API keys in the Fastn platform via GraphQL. Use this tool when you need an overview of all provisioned API keys. Do not use this tool to generate a new API key — use fastn_generate_api_key instead.

        Args:
            projectId: 
        Returns:
            API response as a dictionary.
        """
        ...

    def fastn_list_apis(
        self,
        first: Optional[str] = None,
        projectId: Optional[str] = None,
        query: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Returns a list of all APIs available in the Fastn platform via GraphQL. Use this tool when you need an overview of all registered APIs. Do not use this tool to retrieve details of a single API — use fastn_get_api instead.

        Args:
            first: 
            projectId: 
            query: 
        Returns:
            API response as a dictionary.
        """
        ...

    def fastn_list_app_triggers(
        self,
        after: Optional[str] = None,
        first: Optional[str] = None,
        offset: Optional[str] = None,
        projectId: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Returns a list of all application triggers configured in the Fastn platform via GraphQL. Use this tool when you need an overview of all registered triggers. Do not use this tool to retrieve a single triggers details — use fastn_get_app_trigger instead.

        Args:
            after: 
            first: 
            offset: 
            projectId: 
        Returns:
            API response as a dictionary.
        """
        ...

    def fastn_list_connection_ids(
        self,
        connectorId: Optional[str] = None,
        projectId: Optional[str] = None,
        tenantId: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Returns a list of connection IDs associated with the specified environment in the Fastn platform via GraphQL. Use this tool when you need to enumerate available connections for a given environment. Do not use this tool to retrieve detailed information about a specific connector — use fastn_get_connector_info instead.

        Args:
            connectorId: 
            projectId: 
            tenantId: 
        Returns:
            API response as a dictionary.
        """
        ...

    def fastn_list_connector_groups(
        self,
        after: Optional[str] = None,
        connectorId: Optional[str] = None,
        first: Optional[float] = None,
        projectId: Optional[str] = None,
        query: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Returns a list of all connector groups in the Fastn platform via GraphQL. Use this tool when you need an overview of how connectors are organized into groups. Do not use this tool to retrieve connectors within a specific group — use fastn_list_connectors_from_group instead.

        Args:
            after: 
            connectorId: 
            first: 
            projectId: 
            query: 
        Returns:
            API response as a dictionary.
        """
        ...

    def fastn_list_connectors_from_group(
        self,
        clientId: Optional[str] = None,
        first: Optional[float] = None,
        groupId: Optional[str] = None,
        groupType: Optional[str] = None,
        projectId: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Returns a list of connectors associated with a specified connector group in the Fastn platform via GraphQL. Use this tool when you need to enumerate the connectors belonging to a particular group. Do not use this tool to list all connector groups — use fastn_list_connector_groups instead.

        Args:
            clientId: 
            first: 
            groupId: 
            groupType: 
            projectId: 
        Returns:
            API response as a dictionary.
        """
        ...

    def fastn_list_env_configs(
        self,
        projectId: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Returns a list of all environment configuration entries available in the Fastn platform via GraphQL. Use this tool when you need an overview of current environment settings. Do not use this tool to update configurations — use fastn_update_env_config instead.

        Args:
            projectId: 
        Returns:
            API response as a dictionary.
        """
        ...

    def fastn_list_external_db_tables(
        self,
        clientId: Optional[str] = None,
        dbHost: Optional[str] = None,
        dbName: Optional[str] = None,
        dbPassword: Optional[str] = None,
        dbUserName: Optional[str] = None,
        projectId: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Returns a list of tables available in an external database connection configured in the Fastn platform via GraphQL. Use this tool when you need to discover the table structure of a connected external database. Do not use this tool to create an external database connection — use fastn_create_external_db_connection instead.

        Args:
            clientId: 
            dbHost: 
            dbName: 
            dbPassword: 
            dbUserName: 
            projectId: 
        Returns:
            API response as a dictionary.
        """
        ...

    def fastn_list_mcp_server_tools(
        self,
        connectorId: Optional[str] = None,
        customAuth: Optional[str] = None,
        orgId: Optional[str] = None,
        projectId: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Returns a list of all server tools available in the Fastn MCP (Multi-Channel Platform) environment via GraphQL. Use this tool when you need to discover which server tools are registered and accessible. Do not use this tool to invoke a tool — use fastn_run_action instead.

        Args:
            connectorId: 
            customAuth: 
            orgId: 
            projectId: 
        Returns:
            API response as a dictionary.
        """
        ...

    def fastn_list_secrets(
        self,
        discriminator: Optional[str] = None,
        hide: Optional[bool] = None,
        projectId: Optional[str] = None,
        x_fastn_custom_auth: Optional[bool] = None,
    ) -> Dict[str, Any]:
        """Returns a list of all stored secrets for the specified connector in the Fastn platform via GraphQL. Use this tool when you need an overview of existing secrets. Do not use this tool to delete a secret — use fastn_delete_secret instead, and do not use it to update secrets — use fastn_update_secrets instead.

        Args:
            discriminator: 
            hide: 
            projectId: 
            x_fastn_custom_auth: 
        Returns:
            API response as a dictionary.
        """
        ...

    def fastn_list_templates(
        self,
        clientId: Optional[str] = None,
        orgId: Optional[str] = None,
        projectId: Optional[str] = None,
        query: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Returns a list of all available templates in the Fastn platform via GraphQL. Use this tool when you need to discover which templates are available for use in flows or projects. Do not use this tool to import a template — use fastn_import_flow_template or fastn_batch_import_templates instead.

        Args:
            clientId: 
            orgId: 
            projectId: 
            query: 
        Returns:
            API response as a dictionary.
        """
        ...

    def fastn_list_tenants(
        self,
        after: Optional[str] = None,
        first: Optional[str] = None,
        projectId: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Returns a list of all tenants registered in the Fastn platform via GraphQL. Use this tool when you need an overview of all available tenants. Do not use this tool to retrieve or update details for a single tenant — use fastn_update_tenant instead.

        Args:
            after: 
            first: 
            projectId: 
        Returns:
            API response as a dictionary.
        """
        ...

    def fastn_list_webhooks(
        self,
        after: Optional[float] = None,
        first: Optional[float] = None,
        projectId: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Returns a list of all configured webhooks in the Fastn platform via GraphQL. Use this tool when you need an overview of all active webhook registrations. Do not use this tool to retrieve details of a single webhook — use fastn_get_webhook instead.

        Args:
            after: 
            first: 
            projectId: 
        Returns:
            API response as a dictionary.
        """
        ...

    def fastn_list_webhooks_v2(
        self,
        after: Optional[float] = None,
        first: Optional[float] = None,
        projectId: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Returns a list of all configured webhooks in the Fastn platform via GraphQL (auth-scoped domain). Use this tool when you need an overview of all active webhook registrations in the auth context. Do not use this tool to retrieve details of a single webhook — use fastn_get_webhook instead.

        Args:
            after: 
            first: 
            projectId: 
        Returns:
            API response as a dictionary.
        """
        ...

    def fastn_migrate_secrets_without_expiry(
        self,
        input: Dict[str, Any],
        projectId: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Migrates all secrets in the Fastn platform that do not have an expiry date set, via a GraphQL mutation. Use this tool during maintenance or compliance operations to bring non-expiring secrets into a managed lifecycle. This is a write operation that modifies the state of multiple secrets in bulk. Ensure you have reviewed which secrets will be affected before calling this tool.

        Args:
            input:  (required)
            projectId: 
        Returns:
            API response as a dictionary.
        """
        ...

    def fastn_rotate_expired_secret(
        self,
        input: Dict[str, Any],
        projectId: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Rotates secrets in the Fastn platform that are past their expiry date, via a GraphQL mutation. Use this tool during security maintenance to replace expired credentials with new ones. This is a write operation that modifies secret values and may affect integrations relying on those secrets. Ensure dependent systems are updated after rotation.

        Args:
            input:  (required)
            projectId: 
        Returns:
            API response as a dictionary.
        """
        ...

    def fastn_run_action(
        self,
        actionId: Optional[str] = None,
        data: Optional[Dict[str, Any]] = None,
        projectId: Optional[str] = None,
        turnOffSslVerification: Optional[bool] = None,
    ) -> Dict[str, Any]:
        """Executes a specific action defined in the Fastn platform via GraphQL. Use this tool when you need to trigger a named action on demand. This is a write/side-effect operation — the action will run immediately and may modify data or trigger downstream processes. Do not use this tool to inspect an actions definition — use fastn_get_action_by_id instead.

        Args:
            actionId: 
            data: 
            projectId: 
            turnOffSslVerification: 
        Returns:
            API response as a dictionary.
        """
        ...

    def fastn_run_scheduler_now(
        self,
        projectId: Optional[str] = None,
        scheduleId: Optional[str] = None,
        webhookId: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Immediately triggers a scheduler job in the Fastn platform outside of its normal schedule, via GraphQL. Use this tool when you need to manually execute a scheduled task on demand. This is a side-effect operation that runs the scheduler immediately and may trigger downstream workflows or data processing. Do not use this tool to modify scheduler settings — use fastn_update_scheduler instead.

        Args:
            projectId: 
            scheduleId: 
            webhookId: 
        Returns:
            API response as a dictionary.
        """
        ...

    def fastn_test_connector_api(
        self,
        clientId: Optional[str] = None,
        datasource: Optional[_FastnTestConnectorApiDatasource] = None,
        input: Optional[Dict[str, Any]] = None,
        projectId: Optional[str] = None,
        requestSettings: Optional[_FastnTestConnectorApiRequestsettings] = None,
    ) -> Dict[str, Any]:
        """Tests the API endpoint of a specified connector in the Fastn platform to verify connectivity and functionality, via GraphQL. Use this tool when you need to validate that a connectors API is reachable and responding correctly. This is a diagnostic operation and does not modify connector configuration.

        Args:
            clientId: 
            datasource: 
            input: 
            projectId: 
            requestSettings: 
        Returns:
            API response as a dictionary.
        """
        ...

    def fastn_trigger_webhook_flow(
        self,
        backendUrl: Optional[str] = None,
        clientId: Optional[str] = None,
        connectorId: Optional[str] = None,
        connectorName: Optional[str] = None,
        event: Optional[str] = None,
        flowId: Optional[str] = None,
        headers: Optional[Dict[str, Any]] = None,
        payload: Optional[Dict[str, Any]] = None,
        projectId: Optional[str] = None,
        tenantId: Optional[str] = None,
        userAccountId: Optional[str] = None,
        userProjectId: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Triggers a webhook flow in the Fastn platform based on specified events or parameters via GraphQL. Use this tool when you need to manually fire a webhook-driven workflow. This is a side-effect operation that immediately initiates the flow and may invoke downstream actions or external systems. Do not use this tool to create or update a webhook — use fastn_create_webhooks_with_routes or fastn_update_webhook instead.

        Args:
            backendUrl: 
            clientId: 
            connectorId: 
            connectorName: 
            event: 
            flowId: 
            headers: 
            payload: 
            projectId: 
            tenantId: 
            userAccountId: 
            userProjectId: 
        Returns:
            API response as a dictionary.
        """
        ...

    def fastn_update_app_trigger(
        self,
        accountId: Optional[str] = None,
        connectorId: Optional[str] = None,
        connectorImage: Optional[str] = None,
        connectorName: Optional[str] = None,
        event: Optional[str] = None,
        flowId: Optional[str] = None,
        headers: Optional[List[Any]] = None,
        id: Optional[str] = None,
        projectId: Optional[str] = None,
        tenantId: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Updates the configuration of an existing application trigger in the Fastn platform via GraphQL. Use this tool when you need to modify a triggers conditions, schedule, or target action. This is a write operation that alters the triggers persisted state. Do not use this tool to create a new trigger — use fastn_create_app_trigger instead.

        Args:
            accountId: 
            connectorId: 
            connectorImage: 
            connectorName: 
            event: 
            flowId: 
            headers: 
            id: 
            projectId: 
            tenantId: 
        Returns:
            API response as a dictionary.
        """
        ...

    def fastn_update_env_config(
        self,
        data: Optional[Dict[str, Any]] = None,
        projectId: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Updates one or more environment configuration settings in the Fastn platform via a GraphQL mutation. Use this tool when you need to modify system-level environment parameters or integration configuration values. This is a write operation that directly alters configuration state and may affect system behavior for all users. Confirm the intended changes before calling this tool, as modifications may be difficult to reverse without knowing the prior state. Do not use this tool to create new configurations — use fastn_add_env_configs instead.

        Args:
            data: 
            projectId: 
        Returns:
            API response as a dictionary.
        """
        ...

    def fastn_update_resolver_step(
        self,
        clientId: Optional[str] = None,
        expression: Optional[int] = None,
        id: Optional[str] = None,
        isDefault: Optional[bool] = None,
        nodeId: Optional[str] = None,
        parentIds: Optional[List[Any]] = None,
        projectId: Optional[str] = None,
        step: Optional[_FastnUpdateResolverStepStep] = None,
    ) -> Dict[str, Any]:
        """Updates an existing resolver step within a Fastn workflow via GraphQL. Use this tool when you need to modify the logic, inputs, or outputs of a specific resolver step. This is a write operation that alters the steps persisted configuration. Do not use this tool to create a new resolver step — use fastn_create_resolver_step instead.

        Args:
            clientId: 
            expression: 
            id: 
            isDefault: 
            nodeId: 
            parentIds: 
            projectId: 
            step: 
        Returns:
            API response as a dictionary.
        """
        ...

    def fastn_update_scheduler(
        self,
        apiId: Optional[str] = None,
        projectId: Optional[str] = None,
        schedule: Optional[_FastnUpdateSchedulerSchedule] = None,
        webhookId: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Updates the configuration or scheduling parameters of an existing scheduler in the Fastn platform via GraphQL. Use this tool when you need to change a schedulers timing, target, or other settings. This is a write operation that modifies the schedulers configuration. Do not use this tool to trigger a scheduler immediately — use fastn_run_scheduler_now instead.

        Args:
            apiId: 
            projectId: 
            schedule: 
            webhookId: 
        Returns:
            API response as a dictionary.
        """
        ...

    def fastn_update_secrets(
        self,
        projectId: Optional[str] = None,
        secretKey: Optional[str] = None,
        secretValue: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Updates one or more existing secrets with new values or settings in the Fastn platform via GraphQL. Use this tool when you need to rotate or modify stored secret values. This is a write operation that modifies the persisted secret state. Do not use this tool to create new secrets — use fastn_create_secrets instead.

        Args:
            projectId: 
            secretKey: 
            secretValue: 
        Returns:
            API response as a dictionary.
        """
        ...

    def fastn_update_tenant(
        self,
        id: Optional[str] = None,
        name: Optional[str] = None,
        projectId: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Updates an existing tenants information or settings in the Fastn platform via GraphQL. Use this tool when you need to modify tenant-level configuration, metadata, or access settings. This is a write operation that alters the tenants persisted state. Do not use this tool to create a new tenant — use fastn_create_tenant instead.

        Args:
            id: 
            name: 
            projectId: 
        Returns:
            API response as a dictionary.
        """
        ...

    def fastn_update_webhook(
        self,
        apiKeyId: Optional[str] = None,
        dlqConfigurations: Optional[_FastnUpdateWebhookDlqconfigurations] = None,
        id: Optional[str] = None,
        isAuthenticated: Optional[str] = None,
        model: Optional[_FastnUpdateWebhookModel] = None,
        name: Optional[str] = None,
        projectId: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Updates the configuration of an existing webhook in the Fastn platform via GraphQL. Use this tool when you need to modify a webhooks settings such as its URL, events, or authentication. This is a write operation that alters the webhooks persisted state. Do not use this tool to update routing rules — use fastn_update_webhook_route instead.

        Args:
            apiKeyId: 
            dlqConfigurations: 
            id: 
            isAuthenticated: 
            model: 
            name: 
            projectId: 
        Returns:
            API response as a dictionary.
        """
        ...

    def fastn_update_webhook_route(
        self,
        apiId: Optional[str] = None,
        batchSize: Optional[str] = None,
        description: Optional[str] = None,
        filters: Optional[List[Any]] = None,
        headers: Optional[List[Any]] = None,
        id: Optional[str] = None,
        maximumBatchingWindow: Optional[str] = None,
        projectId: Optional[str] = None,
        routeId: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Updates the routing configuration for a specified webhook in the Fastn platform via GraphQL. Use this tool when you need to change the path or routing rules associated with an existing webhook. This is a write operation that modifies webhook routing state. Do not use this tool to update the webhooks general configuration — use fastn_update_webhook instead.

        Args:
            apiId: 
            batchSize: 
            description: 
            filters: 
            headers: 
            id: 
            maximumBatchingWindow: 
            projectId: 
            routeId: 
        Returns:
            API response as a dictionary.
        """
        ...

    def get_connector_groups(
        self,
        after: Optional[str] = None,
        connectorId: Optional[str] = None,
        first: Optional[str] = None,
        projectId: Optional[str] = None,
        query: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Fetches all connector groups in the system.

        Args:
            after: 
            connectorId: 
            first: 
            projectId: 
            query: 
        Returns:
            API response as a dictionary.
        """
        ...

    def get_connector_groups_test(
        self,
        clientId: Optional[str] = None,
        connectorId: Optional[str] = None,
        first: Optional[int] = None,
        isCommunity: Optional[bool] = None,
        offset: Optional[int] = None,
        projectId: Optional[str] = None,
        query: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Fetches all connector groups for testing purposes.

        Args:
            clientId: 
            connectorId: 
            first: 
            isCommunity: 
            offset: 
            projectId: 
            query: 
        Returns:
            API response as a dictionary.
        """
        ...

    def get_group(
        self,
        id: Optional[str] = None,
        projectId: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Retrieves the details of a specified group.

        Args:
            id: 
            projectId: 
        Returns:
            API response as a dictionary.
        """
        ...

    def update_model_group(
        self,
        authMethods: Optional[List[Any]] = None,
        clientId: Optional[str] = None,
        description: Optional[str] = None,
        docLink: Optional[str] = None,
        enableActivate: Optional[bool] = None,
        id: Optional[str] = None,
        imageUrl: Optional[str] = None,
        isOauth: Optional[bool] = None,
        labels: Optional[List[Any]] = None,
        name: Optional[str] = None,
        oauth: Optional[Dict[str, Any]] = None,
        oauthInputContract: Optional[Dict[str, Any]] = None,
        projectId: Optional[str] = None,
        resourceType: Optional[str] = None,
        tags: Optional[List[Any]] = None,
        type: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Updates an existing model group in the system.

        Args:
            authMethods: 
            clientId: 
            description: 
            docLink: 
            enableActivate: 
            id: 
            imageUrl: 
            isOauth: 
            labels: 
            name: 
            oauth: 
            oauthInputContract: 
            projectId: 
            resourceType: 
            tags: 
            type: 
        Returns:
            API response as a dictionary.
        """
        ...

