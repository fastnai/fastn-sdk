"""Fastn Snowflake connector — auto-generated type stubs.

Do not edit manually. Regenerate with `fastn connector sync`.
"""
from __future__ import annotations

from typing import Any, Dict, List, Optional, TypedDict


class _SnowflakeExecuteStatementBindings(TypedDict, total=False):
    _1: Dict[str, Any]

class _SnowflakeExecuteStatementParameters(TypedDict, total=False):
    MULTI_STATEMENT_COUNT: int

class SnowflakeConnector:
    """Snowflake connector ().

    Provides 17 tools.
    """

    def snowflake_cancel_statement(
        self,
        statementHandle: str,
        requestId: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Cancels an in-progress SQL statement execution in Snowflake identified by its statement handle. Use this tool when you need to stop a long-running or runaway query to free up compute resources. Requires the statementHandle URL parameter. Do not use this tool to cancel a statement that has already completed or to delete the results of a completed query. Cancellation is immediate but cannot be undone — the statement must be resubmitted if the operation is still needed.

        Args:
            statementHandle:  (required)
            requestId: 
        Returns:
            API response as a dictionary.
        """
        ...

    def snowflake_create_database(
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
        """Creates a new database in the Snowflake account. Use this tool when you need to provision a new top-level data storage container for organizing schemas and tables. Do not use this tool to create schemas or tables within an existing database — use createSchema or createTable for those purposes.

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

    def snowflake_create_network_policy(
        self,
    ) -> Dict[str, Any]:
        """Creates a new network policy in Snowflake to control which IP addresses are allowed or blocked from accessing the Snowflake account. Use this tool when you need to enforce IP-based access restrictions for security purposes. Do not use this tool to update or delete an existing network policy. Creating a network policy does not automatically apply it to users or the account — a separate assignment step is required. This tool is implemented via Python code rather than a direct REST API call.
        Returns:
            API response as a dictionary.
        """
        ...

    def snowflake_create_schema(
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
        """Creates a new schema within a specified Snowflake database. Use this tool when you need to add a logical grouping namespace for related database objects such as tables and views. Requires the database name as a URL parameter. Do not use this tool to create databases or tables — use createDatabase or createTable for those purposes.

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

    def snowflake_create_table(
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
        """Creates or replaces a table within a specified database and schema in Snowflake using a PUT request. Use this tool when you need to define a new table structure for storing data. Requires the database name, schema name, and table name as URL parameters, along with a column definition payload. Note: because this uses a PUT request, submitting this tool against an existing table name may overwrite the existing table definition. Do not use this tool to insert data into an existing table — use executeStatement for DML operations.

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

    def snowflake_create_warehouse(
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
        """Creates a new virtual warehouse in the Snowflake account to provision compute resources for query execution and data processing. Use this tool when you need to add a new warehouse with a specified configuration. Do not use this tool to modify an existing warehouse or resume a suspended one. Creating a warehouse will immediately begin incurring compute costs when it is active.

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

    def snowflake_delete_database(
        self,
        databaseName: str,
        ifExists: Optional[str] = None,
        restrict: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Permanently deletes a specified database and all objects it contains (schemas, tables, views, etc.) from the Snowflake account. Use this tool only when you need to remove an entire database and all of its contents. Requires the database name as a URL parameter. This action is irreversible — the database and all contained objects will be permanently removed. Do not use this tool to delete individual schemas or tables within a database.

        Args:
            databaseName:  (required)
            ifExists: 
            restrict: 
        Returns:
            API response as a dictionary.
        """
        ...

    def snowflake_delete_schema(
        self,
        databaseName: str,
        schemaName: str,
        ifExists: Optional[str] = None,
        restrict: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Permanently deletes a specified schema and all objects it contains (tables, views, etc.) from a Snowflake database. Use this tool only when you need to remove an entire schema and all of its contents. Requires the database name and schema name as URL parameters. This action is irreversible — the schema and all contained objects will be permanently removed. Do not use this tool to delete only individual tables or objects within a schema.

        Args:
            databaseName:  (required)
            schemaName:  (required)
            ifExists: 
            restrict: 
        Returns:
            API response as a dictionary.
        """
        ...

    def snowflake_delete_table(
        self,
        databaseName: str,
        schemaName: str,
        tableName: str,
        ifExists: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Permanently deletes a specified table from a Snowflake database and schema. Use this tool only when you need to remove a table and all of its data. Requires the database name, schema name, and table name as URL parameters. This action is irreversible — all data and the table structure will be permanently removed. Do not use this tool to truncate a tables data while retaining its structure, or to delete only specific rows.

        Args:
            databaseName:  (required)
            schemaName:  (required)
            tableName:  (required)
            ifExists: 
        Returns:
            API response as a dictionary.
        """
        ...

    def snowflake_delete_warehouse(
        self,
        warehouseName: str,
        ifExists: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Permanently deletes a specified virtual warehouse from the Snowflake account. Use this tool only when you need to remove a warehouse that is no longer needed. Requires the warehouse name as a URL parameter. This action is irreversible — the warehouse and its configuration will be permanently removed. Any queries running on the warehouse at the time of deletion will be terminated. Do not use this tool to suspend or resize a warehouse.

        Args:
            warehouseName:  (required)
            ifExists: 
        Returns:
            API response as a dictionary.
        """
        ...

    def snowflake_execute_statement(
        self,
        async: Optional[str] = None,
        bindings: Optional[_SnowflakeExecuteStatementBindings] = None,
        database: Optional[str] = None,
        parameters: Optional[_SnowflakeExecuteStatementParameters] = None,
        requestId: Optional[str] = None,
        role: Optional[str] = None,
        schema: Optional[str] = None,
        statement: Optional[str] = None,
        timeout: Optional[int] = None,
        warehouse: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Submits and executes a SQL statement in Snowflake. Use this tool when you need to run a SQL query or DML operation and retrieve its results. This tool sends a POST request and initiates execution, which may be asynchronous for long-running queries. Do not use this tool to check the status of an already-submitted statement or retrieve paginated partition results — use the appropriate get or list tools for those purposes. Executing DML statements (INSERT, UPDATE, DELETE) will modify data. Execution cannot be undone; use cancelStatement to stop an in-progress execution.

        Args:
            async: 
            bindings: 
            database: 
            parameters: 
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

    def snowflake_get_statement_result(
        self,
        statementHandle: str,
        partition: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Retrieves the result or status of a previously submitted SQL statement execution in Snowflake, identified by its statement handle. Use this tool when you need to poll for the result of an asynchronous statement or retrieve a specific partition of results from a completed query. Do not use this tool to submit a new SQL statement — use executeStatement for that. Requires the statementHandle URL parameter. Does not modify any data.

        Args:
            statementHandle:  (required)
            partition: 
        Returns:
            API response as a dictionary.
        """
        ...

    def snowflake_list_databases(
        self,
        fromName: Optional[str] = None,
        history: Optional[str] = None,
        like: Optional[str] = None,
        showLimit: Optional[str] = None,
        startsWith: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Lists all databases available in the Snowflake account. Use this tool when you need to discover or audit the databases present in your Snowflake environment. Do not use this tool to list schemas or tables within a database — use the listSchemas or listTables tools for those purposes. Returns database names and associated metadata.

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

    def snowflake_list_schemas(
        self,
        databaseName: str,
        fromName: Optional[str] = None,
        history: Optional[str] = None,
        like: Optional[str] = None,
        showLimit: Optional[str] = None,
        startsWith: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Lists all schemas within a specified database in Snowflake. Use this tool when you need to discover or audit the schemas available in a database. Requires the target database name as a parameter. Do not use this tool to list tables within a schema or retrieve schema-level DDL definitions. Returns schema names and associated metadata.

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

    def snowflake_list_tables(
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
        """Lists all tables within a specified database and schema in Snowflake. Use this tool when you need to discover or audit tables within a given schema. Requires the target database name and schema name as parameters. Do not use this tool to retrieve column-level schema definitions for a specific table or to query table data. Returns table names and structural metadata.

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

    def snowflake_list_user_grants(
        self,
    ) -> Dict[str, Any]:
        """Lists all grants (permissions) assigned to the authenticated Snowflake user. Use this tool when you need to audit or review what privileges a user has been granted on Snowflake objects. Uses the authenticated username from the connection credentials. Do not use this tool to grant or revoke permissions — this is a read-only operation. Returns a list of grant records including role, privilege, and object details.
        Returns:
            API response as a dictionary.
        """
        ...

    def snowflake_list_warehouses(
        self,
        like: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Lists all virtual warehouses available in the Snowflake account. Use this tool when you need to discover or audit compute resources available for data processing and query execution. Do not use this tool to retrieve details about a single warehouse or to create, modify, or delete warehouses. Returns warehouse names, sizes, states, and configuration metadata.

        Args:
            like: 
        Returns:
            API response as a dictionary.
        """
        ...

