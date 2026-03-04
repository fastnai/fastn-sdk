"""Fastn Microsoft Fabric connector — auto-generated type stubs.

Do not edit manually. Regenerate with `fastn connector sync`.
"""
from __future__ import annotations

from typing import Any, Dict, List, Optional, TypedDict


class _MicrosoftFabricCreateKqlDatabaseCreationpayload(TypedDict, total=False):
    databaseType: str
    parentEventhouseItemId: str

class MicrosoftFabricConnector:
    """Microsoft Fabric connector ().

    Provides 17 tools.
    """

    def microsoft_fabric_add_rows(
        self,
        datasetId: str,
        groupId: str,
        rows: List[Any],
        tableName: str,
    ) -> Dict[str, Any]:
        """Appends one or more new rows of data to a specified table within a dataset in a Microsoft Fabric workspace group. Use this tool when you need to ingest or stream new data records into an existing push dataset table. Do not use this tool to modify or delete existing rows, or to alter the table schema — use the upsert table tool for schema changes. This operation modifies the dataset content and appended rows cannot be selectively removed without additional API calls.

        Args:
            datasetId: ID of the dataset in Microsoft Fabric. (required)
            groupId: ID of the workspace group in Microsoft Fabric. (required)
            rows:  (required)
            tableName: Name of the table within the dataset in Microsoft Fabric. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def microsoft_fabric_create_dataset(
        self,
        groupId: str,
        name: str,
        tables: Optional[List[Any]] = None,
    ) -> Dict[str, Any]:
        """Creates a new push dataset within a specified workspace group in Microsoft Fabric. Use this tool when you need to define a new dataset including its table schemas for subsequent data ingestion or reporting. Do not use this tool to update an existing datasets schema — use the upsert table tool instead. This operation provisions a persistent dataset resource.

        Args:
            groupId: Group ID for the request. (required)
            name: Name of the dataset or operation. (required)
            tables: 
        Returns:
            API response as a dictionary.
        """
        ...

    def microsoft_fabric_create_event_house(
        self,
        displayName: str,
        workspaceId: str,
        description: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Creates a new EventHouse within a specified Microsoft Fabric workspace. Use this tool when you need to provision an EventHouse — a managed container for one or more KQL databases used for real-time analytics and event streaming scenarios. Do not use this tool to create individual KQL databases inside an existing EventHouse — use the create KQL database tool instead. This operation creates a persistent resource and cannot be automatically undone.

        Args:
            displayName: Display name for the Microsoft Fabric resource. (required)
            workspaceId: Workspace ID for the Microsoft Fabric resource. (required)
            description: Description of the Microsoft Fabric resource.
        Returns:
            API response as a dictionary.
        """
        ...

    def microsoft_fabric_create_group(
        self,
        name: str,
        workspaceV2: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Creates a new workspace group in Microsoft Fabric (Power BI). Use this tool when you need to provision a new collaborative workspace for organizing datasets, reports, and dashboards within your Power BI environment. Do not use this tool to modify or add members to an existing group. This operation creates a persistent group and the action cannot be automatically undone.

        Args:
            name: Name parameter for the Microsoft Fabric API request. (required)
            workspaceV2: Workspace ID (V2) for the Microsoft Fabric API request.
        Returns:
            API response as a dictionary.
        """
        ...

    def microsoft_fabric_create_kql_database(
        self,
        creationPayload: _MicrosoftFabricCreateKqlDatabaseCreationpayload,
        displayName: str,
        workspaceId: str,
        description: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Creates a new KQL (Kusto Query Language) database within a specified Microsoft Fabric workspace. Use this tool when you need to provision a new KQL database for storing and querying time-series or log data using Kusto queries. Database creation is asynchronous; use the get KQL database creation status tool to poll for completion. Do not use this tool to query or modify an existing KQL database. This operation creates a persistent resource and cannot be automatically undone.

        Args:
            creationPayload: Payload for creating a resource in Microsoft Fabric. (required)
            displayName: Display name for the resource in Microsoft Fabric. (required)
            workspaceId: ID of the workspace in Microsoft Fabric. (required)
            description: Description of the resource in Microsoft Fabric.
        Returns:
            API response as a dictionary.
        """
        ...

    def microsoft_fabric_execute_kql_query(
        self,
        csl: str,
        db: str,
        properties: str,
        queryServiceUrl: str,
    ) -> Dict[str, Any]:
        """Executes a KQL (Kusto Query Language) management or query command against an Azure Data Explorer cluster via the Microsoft Fabric query service REST endpoint. Use this tool when you need to run read queries, filter, aggregate, or analyze large datasets stored in Azure Data Explorer in real time, or when you need to issue management REST commands via the /v1/rest/mgmt endpoint. Do not use this tool for schema modification operations or data ingestion that require dedicated ingestion APIs. Requires a valid KQL query or management command string and a configured query service URL. This tool reads data and issues management commands; management commands may have side effects on the cluster.

        Args:
            csl: The CSL (Common Schema Language) query string. (required)
            db: The name of the database to query. (required)
            properties: Additional properties for the request. (required)
            queryServiceUrl: The URL of the query service. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def microsoft_fabric_generate_auth_token(
        self,
        client_id: str,
        client_secret: str,
        password: str,
        scope: str,
        tenantId: str,
        username: str,
    ) -> Dict[str, Any]:
        """Generates an OAuth 2.0 access token from the Microsoft identity platform for authenticating with Microsoft Fabric and Power BI APIs. Use this tool when you need to obtain a bearer token before making API calls to Microsoft Fabric services. Do not use this tool for interactive user login flows or when a different OAuth grant type is required. The generated token is temporary and will expire based on the configured token lifetime.

        Args:
            client_id: Client ID for Microsoft Fabric authentication. (required)
            client_secret: Client secret for Microsoft Fabric authentication. (required)
            password: User password for Microsoft Fabric authentication. (required)
            scope: Scope of access for the Microsoft Fabric API. (required)
            tenantId: Tenant ID for Microsoft Fabric. (required)
            username: Username for Microsoft Fabric authentication. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def microsoft_fabric_get_dataset(
        self,
        datasetId: str,
        groupId: str,
    ) -> Dict[str, Any]:
        """Retrieves the details of a single dataset by its ID within a specified workspace group in Microsoft Fabric. Use this tool when you need metadata about a specific dataset, such as its name, tables, datasource connections, or refresh schedule. Do not use this tool to list all datasets in a workspace — use the list datasets tool instead. This is a read-only operation with no side effects.

        Args:
            datasetId: The ID of the dataset in Microsoft Fabric. (required)
            groupId: The ID of the group containing the dataset in Microsoft Fabric. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def microsoft_fabric_get_event_house(
        self,
        eventHouseId: str,
        workspaceId: str,
    ) -> Dict[str, Any]:
        """Retrieves the details of a specific EventHouse by its ID within a Microsoft Fabric workspace. Use this tool when you need metadata about a particular EventHouse, such as its name, status, or associated KQL databases. Do not use this tool to list all EventHouses in a workspace — use the list EventHouses tool instead. This is a read-only operation with no side effects.

        Args:
            eventHouseId: Identifier for the event house in Microsoft Fabric. (required)
            workspaceId: Identifier for the workspace in Microsoft Fabric. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def microsoft_fabric_get_group(
        self,
        groupId: str,
    ) -> Dict[str, Any]:
        """Retrieves details of a specific workspace group by its ID in Microsoft Fabric. Use this tool when you need metadata about a particular group, such as its name, type, or capacity settings. Do not use this tool to list all groups — use the list groups tool instead. This is a read-only operation with no side effects.

        Args:
            groupId: ID of the group for the Microsoft Fabric API request. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def microsoft_fabric_get_kql_database(
        self,
        kqlDatabaseId: str,
        workspaceId: str,
    ) -> Dict[str, Any]:
        """Retrieves the details of a specific KQL (Kusto Query Language) database by its ID within a Microsoft Fabric workspace. Use this tool when you need metadata about a single KQL database, such as its name, status, or configuration. Do not use this tool to list all KQL databases in a workspace — use the list KQL databases tool instead. This is a read-only operation with no side effects.

        Args:
            kqlDatabaseId: ID of the KQL database in Microsoft Fabric. (required)
            workspaceId: ID of the workspace in Microsoft Fabric. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def microsoft_fabric_get_kql_database_creation_status(
        self,
        location: str,
    ) -> Dict[str, Any]:
        """Polls the creation status of a KQL (Kusto Query Language) database provisioning operation in Microsoft Fabric. Use this tool after calling the create KQL database tool to check whether the asynchronous database creation has completed, is still in progress, or has failed. The required URL is returned by the create KQL database operations Location response header. Do not use this tool to retrieve database details once provisioning is complete — use the get KQL database tool instead. This is a read-only polling operation with no side effects.

        Args:
            location: Location of the resource in Microsoft Fabric. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def microsoft_fabric_list_datasets(
        self,
        groupId: str,
    ) -> Dict[str, Any]:
        """Retrieves a list of all datasets available within a specified workspace group in Microsoft Fabric. Use this tool when you need an overview of all datasets in a group, for example to find a dataset ID before performing further operations. Do not use this tool to retrieve details of a single dataset — use the get dataset tool instead. This is a read-only operation with no side effects.

        Args:
            groupId: ID of the group for the Microsoft Fabric API request. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def microsoft_fabric_list_event_houses(
        self,
        workspaceId: str,
    ) -> Dict[str, Any]:
        """Retrieves a list of all EventHouses within a specified Microsoft Fabric workspace. Use this tool when you need an overview of all EventHouse resources available in a workspace, for example to locate an EventHouse ID before querying its KQL databases. Do not use this tool to retrieve details of a single EventHouse — use the get EventHouse tool instead. This is a read-only operation with no side effects.

        Args:
            workspaceId: ID of the workspace in Microsoft Fabric. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def microsoft_fabric_list_groups(
        self,
    ) -> Dict[str, Any]:
        """Retrieves a list of all workspace groups available in the Microsoft Fabric (Power BI) organization. Use this tool when you need an overview of all groups, for example to find a group ID before creating datasets or managing group members. Do not use this tool to retrieve details of a single group — use the get group tool instead. This is a read-only operation with no side effects.
        Returns:
            API response as a dictionary.
        """
        ...

    def microsoft_fabric_list_kql_databases(
        self,
        workspaceId: str,
    ) -> Dict[str, Any]:
        """Retrieves a list of all KQL (Kusto Query Language) databases available within a specified Microsoft Fabric workspace. Use this tool when you need an inventory of KQL databases in a workspace, for example to find a database ID before executing queries or checking creation status. Do not use this tool to retrieve details of a single KQL database — use the get KQL database tool instead. This is a read-only operation with no side effects.

        Args:
            workspaceId: Workspace ID for the Microsoft Fabric workspace. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def microsoft_fabric_upsert_table(
        self,
        columns: List[Any],
        datasetId: str,
        groupId: str,
        name: str,
        tableName: str,
    ) -> Dict[str, Any]:
        """Creates or fully replaces a table definition within a specified dataset in a Microsoft Fabric (Power BI) workspace group. Use this tool when you need to define or overwrite the schema of a table in an existing dataset. If the table already exists it will be replaced entirely; if it does not exist it will be created. Do not use this tool to append rows to an existing table — use the add rows tool instead. This operation modifies the dataset schema and may cause loss of existing table data.

        Args:
            columns:  (required)
            datasetId: ID of the dataset in Microsoft Fabric. (required)
            groupId: ID of the group in Microsoft Fabric. (required)
            name: Name of the dataset or table in Microsoft Fabric. (required)
            tableName: Name of the table in Microsoft Fabric. (required)
        Returns:
            API response as a dictionary.
        """
        ...

