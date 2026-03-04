"""Fastn Snowflake (legacy) connector — auto-generated type stubs.

Do not edit manually. Regenerate with `fastn connector sync`.
"""
from __future__ import annotations

from typing import Any, Dict, List, Optional, TypedDict


class _GetStatementsSnowflake(legacy)Bindings(TypedDict, total=False):
    _1: Dict[str, Any]

class SnowflakeLegacyConnector:
    """Snowflake (legacy) connector ().

    Provides 25 tools.
    """

    def cancel_statement_snowflake__legacy_(
        self,
        statementHandle: str,
        requestId: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Cancels a currently running statement in the Snowflake (legacy) connector, providing control over ongoing data operations.

        Args:
            statementHandle:  (required)
            requestId: 
        Returns:
            API response as a dictionary.
        """
        ...

    def create_database_snowflake__legacy_(
        self,
        name: str,
        comment: Optional[str] = None,
        createMode: Optional[str] = None,
        data_retention_time_in_days: Optional[int] = None,
        default_ddl_collation: Optional[str] = None,
        kind: Optional[str] = None,
        log_level: Optional[str] = None,
        max_data_extension_time_in_days: Optional[int] = None,
        serverless_task_max_statement_size: Optional[str] = None,
        serverless_task_min_statement_size: Optional[str] = None,
        suspend_task_after_num_failures: Optional[int] = None,
        trace_level: Optional[str] = None,
        user_task_managed_initial_warehouse_size: Optional[str] = None,
        user_task_timeout_ms: Optional[int] = None,
    ) -> Dict[str, Any]:
        """Creates a new database in the Snowflake (legacy) connector, enabling organization and segregation of data within your data warehouse.

        Args:
            name:  (required)
            comment: 
            createMode: 
            data_retention_time_in_days: 
            default_ddl_collation: 
            kind: 
            log_level: 
            max_data_extension_time_in_days: 
            serverless_task_max_statement_size: 
            serverless_task_min_statement_size: 
            suspend_task_after_num_failures: 
            trace_level: 
            user_task_managed_initial_warehouse_size: 
            user_task_timeout_ms: 
        Returns:
            API response as a dictionary.
        """
        ...

    def create_schema_snowflake__legacy_(
        self,
        databaseName: str,
        name: str,
        comment: Optional[str] = None,
        createMode: Optional[str] = None,
        data_retention_time_in_days: Optional[int] = None,
        default_ddl_collation: Optional[str] = None,
        kind: Optional[str] = None,
        log_level: Optional[str] = None,
        managed_access: Optional[bool] = None,
        max_data_extension_time_in_days: Optional[int] = None,
        pipe_execution_paused: Optional[bool] = None,
        serverless_task_max_statement_size: Optional[str] = None,
        serverless_task_min_statement_size: Optional[str] = None,
        suspend_task_after_num_failures: Optional[int] = None,
        trace_level: Optional[str] = None,
        user_task_managed_initial_warehouse_size: Optional[str] = None,
        user_task_timeout_ms: Optional[int] = None,
    ) -> Dict[str, Any]:
        """Creates a new schema in the Snowflake (legacy) connector, allowing for structured organization of tables and data objects within a database.

        Args:
            databaseName:  (required)
            name:  (required)
            comment: 
            createMode: 
            data_retention_time_in_days: 
            default_ddl_collation: 
            kind: 
            log_level: 
            managed_access: 
            max_data_extension_time_in_days: 
            pipe_execution_paused: 
            serverless_task_max_statement_size: 
            serverless_task_min_statement_size: 
            suspend_task_after_num_failures: 
            trace_level: 
            user_task_managed_initial_warehouse_size: 
            user_task_timeout_ms: 
        Returns:
            API response as a dictionary.
        """
        ...

    def create_table_snowflake__legacy_(
        self,
        databaseName: str,
        name: str,
        schemaName: str,
        tableName: str,
        change_tracking: Optional[bool] = None,
        cluster_by: Optional[List[Any]] = None,
        columns: Optional[List[Any]] = None,
        comment: Optional[str] = None,
        constraints: Optional[List[Any]] = None,
        data_retention_time_in_days: Optional[int] = None,
        default_ddl_collation: Optional[str] = None,
        enable_schema_evolution: Optional[bool] = None,
        kind: Optional[str] = None,
        max_data_extension_time_in_days: Optional[int] = None,
    ) -> Dict[str, Any]:
        """Creates a new table in the Snowflake (legacy) connector, allowing you to define the structure and organization of your data.

        Args:
            databaseName:  (required)
            name:  (required)
            schemaName:  (required)
            tableName:  (required)
            change_tracking: 
            cluster_by: 
            columns: 
            comment: 
            constraints: 
            data_retention_time_in_days: 
            default_ddl_collation: 
            enable_schema_evolution: 
            kind: 
            max_data_extension_time_in_days: 
        Returns:
            API response as a dictionary.
        """
        ...

    def create_warehouse_snowflake__legacy_(
        self,
        name: str,
        auto_resume: Optional[bool] = None,
        auto_suspend: Optional[int] = None,
        comment: Optional[str] = None,
        createMode: Optional[str] = None,
        enable_query_acceleration: Optional[bool] = None,
        initially_suspended: Optional[bool] = None,
        max_cluster_count: Optional[int] = None,
        max_concurrency_level: Optional[int] = None,
        min_cluster_count: Optional[int] = None,
        query_acceleration_max_scale_factor: Optional[int] = None,
        resource_monitor: Optional[str] = None,
        scaling_policy: Optional[str] = None,
        size: Optional[str] = None,
        statement_queued_timeout_in_seconds: Optional[int] = None,
        statement_timeout_in_seconds: Optional[int] = None,
        target_statement_size: Optional[str] = None,
        type: Optional[str] = None,
        wait_for_completion: Optional[bool] = None,
        warehouse_credit_limit: Optional[int] = None,
        warehouse_size: Optional[str] = None,
        warehouse_type: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Creates a new warehouse in the Snowflake (legacy) connector, enabling scalable processing resources for your data operations.

        Args:
            name:  (required)
            auto_resume: 
            auto_suspend: 
            comment: 
            createMode: 
            enable_query_acceleration: 
            initially_suspended: 
            max_cluster_count: 
            max_concurrency_level: 
            min_cluster_count: 
            query_acceleration_max_scale_factor: 
            resource_monitor: 
            scaling_policy: 
            size: 
            statement_queued_timeout_in_seconds: 
            statement_timeout_in_seconds: 
            target_statement_size: 
            type: 
            wait_for_completion: 
            warehouse_credit_limit: 
            warehouse_size: 
            warehouse_type: 
        Returns:
            API response as a dictionary.
        """
        ...

    def delete_database_snowflake__legacy_(
        self,
        databaseName: str,
        ifExists: Optional[str] = None,
        restrict: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Deletes an existing database in the Snowflake (legacy) connector, allowing for the removal of unused or unwanted data structures.

        Args:
            databaseName:  (required)
            ifExists: 
            restrict: 
        Returns:
            API response as a dictionary.
        """
        ...

    def delete_schema_snowflake__legacy_(
        self,
        databaseName: str,
        schemaName: str,
        ifExists: Optional[str] = None,
        restrict: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Deletes an existing schema in the Snowflake (legacy) connector, enabling you to clean up your data organization.

        Args:
            databaseName:  (required)
            schemaName:  (required)
            ifExists: 
            restrict: 
        Returns:
            API response as a dictionary.
        """
        ...

    def delete_table_snowflake__legacy_(
        self,
        databaseName: str,
        schemaName: str,
        tableName: str,
        ifExists: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Deletes an existing table in the Snowflake (legacy) connector, removing data structures that are no longer needed.

        Args:
            databaseName:  (required)
            schemaName:  (required)
            tableName:  (required)
            ifExists: 
        Returns:
            API response as a dictionary.
        """
        ...

    def drop_ware_houses_snowflake__legacy_(
        self,
        warehouseName: str,
        ifExists: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Drops warehouses in the Snowflake (legacy) connector, freeing up resources that are no longer in use.

        Args:
            warehouseName:  (required)
            ifExists: 
        Returns:
            API response as a dictionary.
        """
        ...

    def generate_token_snowflake__legacy_(
        self,
        client_id: str,
        client_secret: str,
        code: str,
    ) -> Dict[str, Any]:
        """Generates a new authentication token for the Snowflake (legacy) connector, enabling secure access for data operations.

        Args:
            client_id: Client ID for Snowflake authentication. (required)
            client_secret: Client secret for Snowflake authentication. (required)
            code: Authorization code received from Snowflake. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def get_databases_snowflake__legacy_(
        self,
        fromName: Optional[str] = None,
        history: Optional[str] = None,
        like: Optional[str] = None,
        showLimit: Optional[str] = None,
        startsWith: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Retrieves a list of databases from the Snowflake (legacy) connector, providing insight into your data environment and organization.

        Args:
            fromName: 
            history: 
            like: 
            showLimit: 
            startsWith: 
        Returns:
            API response as a dictionary.
        """
        ...

    def get_schemas_snowflake__legacy_(
        self,
        databaseName: str,
        fromName: Optional[str] = None,
        history: Optional[str] = None,
        like: Optional[str] = None,
        showLimit: Optional[str] = None,
        startsWith: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Retrieves a list of schemas from the Snowflake (legacy) connector, helping you understand the organization of data within your databases.

        Args:
            databaseName:  (required)
            fromName: 
            history: 
            like: 
            showLimit: 
            startsWith: 
        Returns:
            API response as a dictionary.
        """
        ...

    def get_statement_handle_snowflake__legacy_(
        self,
        statementHandle: str,
        partition: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Gets the handle of a specific statement using the Snowflake (legacy) connector, allowing for tracking and management of executed queries.

        Args:
            statementHandle:  (required)
            partition: 
        Returns:
            API response as a dictionary.
        """
        ...

    def get_statements_snowflake__legacy_(
        self,
        async: Optional[str] = None,
        bindings: Optional[_GetStatementsSnowflake(legacy)Bindings] = None,
        database: Optional[str] = None,
        requestId: Optional[str] = None,
        role: Optional[str] = None,
        schema: Optional[str] = None,
        statement: Optional[str] = None,
        timeout: Optional[int] = None,
        warehouse: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Retrieves a list of statements or queries executed in the Snowflake (legacy) connector, providing insight into data interactions.

        Args:
            async: 
            bindings: 
            database: 
            requestId: 
            role: 
            schema: 
            statement: 
            timeout: 
            warehouse: 
        Returns:
            API response as a dictionary.
        """
        ...

    def get_tables__copy__snowflake__legacy_(
        self,
        databaseName: str,
        schemaName: str,
        deep: Optional[str] = None,
        fromName: Optional[str] = None,
        history: Optional[str] = None,
        like: Optional[str] = None,
        showLimit: Optional[str] = None,
        startsWith: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Retrieves a list of tables within a specified schema using the Snowflake (legacy) connector, helping you understand your data structure.

        Args:
            databaseName:  (required)
            schemaName:  (required)
            deep: 
            fromName: 
            history: 
            like: 
            showLimit: 
            startsWith: 
        Returns:
            API response as a dictionary.
        """
        ...

    def get_tables_snowflake__legacy_(
        self,
        databaseName: str,
        schemaName: str,
        deep: Optional[str] = None,
        fromName: Optional[str] = None,
        history: Optional[str] = None,
        like: Optional[str] = None,
        showLimit: Optional[str] = None,
        startsWith: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Retrieves a list of tables within a specified schema using the Snowflake (legacy) connector, helping you understand your data structure.

        Args:
            databaseName:  (required)
            schemaName:  (required)
            deep: 
            fromName: 
            history: 
            like: 
            showLimit: 
            startsWith: 
        Returns:
            API response as a dictionary.
        """
        ...

    def get_wareshouses_snowflake__legacy_(
        self,
        like: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Retrieves a list of warehouses in the Snowflake (legacy) connector, providing an overview of available processing resources.

        Args:
            like: 
        Returns:
            API response as a dictionary.
        """
        ...

    def snowflake__legacy__execute_query(
        self,
        database: str,
        query: str,
        schema: Optional[str] = None,
        warehouse: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Executes a SQL query against Snowflake using the legacy Python-based connector and returns the results. Use this tool when you need to retrieve or manipulate data in Snowflake via the legacy connector. DML statements (INSERT, UPDATE, DELETE) will modify data and the effects may be irreversible. Do not use this tool to manage warehouses, schemas, or databases — use the appropriate create, list, or delete tools for those purposes. Prefer the standard Snowflake connectors executeStatement tool for new implementations.

        Args:
            database: The name of the database to execute the query against. (required)
            query: The SQL query to be executed. (required)
            schema: The name of the schema containing the target database objects.
            warehouse: 
        Returns:
            API response as a dictionary.
        """
        ...

    def snowflake__legacy__get_table_schema(
        self,
        database: Optional[str] = None,
        tableName: Optional[str] = None,
        warehouse: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Retrieves the column-level schema definition (column names, data types, nullability, etc.) for a specific table in Snowflake using the legacy Python-based connector. Use this tool when you need to understand the structure of a specific table before querying or transforming its data. Do not use this tool to list all tables in a schema — use the legacy listTables tool for that. Prefer the standard Snowflake connector for new implementations.

        Args:
            database: 
            tableName: 
            warehouse: 
        Returns:
            API response as a dictionary.
        """
        ...

    def snowflake__legacy__list_databases(
        self,
        warehouse: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Lists all databases available in the Snowflake account using the legacy Python-based connector. Use this tool when you need to discover or audit databases via the legacy connector. Do not use this tool to list schemas or tables within a database. Prefer the standard Snowflake connectors listDatabases tool for new implementations.

        Args:
            warehouse: 
        Returns:
            API response as a dictionary.
        """
        ...

    def snowflake__legacy__list_schemas(
        self,
        database: Optional[str] = None,
        warehouse: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Lists all schemas within a specified Snowflake database using the legacy Python-based connector. Use this tool when you need to discover the schemas available in a database via the legacy connector. Do not use this tool to list tables within a schema — use the legacy listTables tool for that. Prefer the standard Snowflake connectors listSchemas tool for new implementations.

        Args:
            database: 
            warehouse: 
        Returns:
            API response as a dictionary.
        """
        ...

    def snowflake__legacy__list_tables(
        self,
        database: str,
        warehouse: str,
    ) -> Dict[str, Any]:
        """Lists all tables within a specified schema in Snowflake using the legacy Python-based connector. Use this tool when you need to discover tables available in a given schema via the legacy connector. Do not use this tool to retrieve column-level definitions for a specific table — use the legacy getTableSchema tool for that. Prefer the standard Snowflake connectors listTables tool for new implementations.

        Args:
            database: The name of the database to connect to. (required)
            warehouse:  (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def snowflake__legacy__list_user_permissions(
        self,
    ) -> Dict[str, Any]:
        """Lists all permissions and access rights for a specified user in the Snowflake legacy connector. Use this tool when you need to audit what a user is allowed to do within the Snowflake environment using the legacy Python-based connector. Do not use this tool to grant or revoke permissions — this is a read-only operation. Prefer the standard Snowflake connectors getUserGrants tool for new implementations.
        Returns:
            API response as a dictionary.
        """
        ...

    def snowflake__legacy__list_warehouses(
        self,
    ) -> Dict[str, Any]:
        """Lists all virtual warehouses available in the Snowflake account using the legacy Python-based connector. Use this tool when you need to discover or audit compute resources via the legacy connector. Do not use this tool to create, modify, or delete warehouses. Prefer the standard Snowflake connectors listWarehouses tool for new implementations.
        Returns:
            API response as a dictionary.
        """
        ...

    def snowflake_sql(
        self,
        database: str,
        schema: str,
        statement: str,
        warehouse: str,
    ) -> Dict[str, Any]:
        """Executes SQL queries against a Snowflake database using the Snowflake SQL connector, allowing users to interact directly with data stored in their Snowflake environment.

        Args:
            database: Name of the Snowflake database to use. (required)
            schema: Name of the Snowflake schema to use. (required)
            statement: SQL statement to be executed. (required)
            warehouse: Name of the Snowflake warehouse to use. (required)
        Returns:
            API response as a dictionary.
        """
        ...

