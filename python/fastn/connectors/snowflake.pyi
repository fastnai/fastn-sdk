"""Fastn Snowflake connector — auto-generated type stubs.

Do not edit manually. Regenerate with `fastn connector sync`.
"""
from __future__ import annotations

from typing import Any, Dict, List, Optional


class SnowflakeConnector:
    """Snowflake connector ().

    Provides 17 tools.
    """

    def cancel_statement_snowflake(
        self,
        requestId: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Cancels an ongoing SQL statement execution in Snowflake, allowing you to halt processes that are no longer needed.

        Args:
            requestId: 
        Returns:
            API response as a dictionary.
        """
        ...

    def create_database_snowflake(
        self,
        createMode: Optional[str] = None,
        kind: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Creates a new database in Snowflake, enabling the organization and storage of data in dedicated structures.

        Args:
            createMode: 
            kind: 
        Returns:
            API response as a dictionary.
        """
        ...

    def create_fastn_network_policy_snowflake(
        self,
    ) -> Dict[str, Any]:
        """Creates a fast network policy in Snowflake, facilitating secure data access and network performance optimization.
        Returns:
            API response as a dictionary.
        """
        ...

    def create_schema_snowflake(
        self,
        createMode: Optional[str] = None,
        kind: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Creates a new schema in Snowflake, helping to organize database objects and manage data more efficiently.

        Args:
            createMode: 
            kind: 
        Returns:
            API response as a dictionary.
        """
        ...

    def create_table_snowflake(
        self,
        name: str,
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
        """Creates a new table in Snowflake, allowing for the structured storage of data within your database.

        Args:
            name:  (required)
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

    def create_warehouse_snowflake(
        self,
        createMode: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Creates a new compute warehouse in Snowflake, providing the necessary resources for processing queries and managing workloads.

        Args:
            createMode: 
        Returns:
            API response as a dictionary.
        """
        ...

    def delete_database_snowflake(
        self,
        ifExists: Optional[str] = None,
        restrict: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Deletes an existing database in Snowflake, permanently removing the database and all its contents.

        Args:
            ifExists: 
            restrict: 
        Returns:
            API response as a dictionary.
        """
        ...

    def delete_schema_snowflake(
        self,
        ifExists: Optional[str] = None,
        restrict: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Deletes an existing schema in Snowflake, clearing out all objects within the schema permanently.

        Args:
            ifExists: 
            restrict: 
        Returns:
            API response as a dictionary.
        """
        ...

    def delete_table_snowflake(
        self,
        ifExists: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Deletes a specific table in Snowflake, removing its structure and data from the database.

        Args:
            ifExists: 
        Returns:
            API response as a dictionary.
        """
        ...

    def drop_warehouses_snowflake(
        self,
        ifExists: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Drops one or more warehouses in Snowflake, efficiently managing resource allocation by removing unneeded processing power.

        Args:
            ifExists: 
        Returns:
            API response as a dictionary.
        """
        ...

    def get_databases_snowflake(
        self,
        fromName: Optional[str] = None,
        history: Optional[str] = None,
        like: Optional[str] = None,
        showLimit: Optional[str] = None,
        startsWith: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Retrieves a list of databases in Snowflake, providing an overview of all database structures within your environment.

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

    def get_partition_results_snowflake(
        self,
        partition: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Gets the results of partitioned queries in Snowflake, giving access to segmented data processing results.

        Args:
            partition: 
        Returns:
            API response as a dictionary.
        """
        ...

    def get_schemas_snowflake(
        self,
        fromName: Optional[str] = None,
        history: Optional[str] = None,
        like: Optional[str] = None,
        showLimit: Optional[str] = None,
        startsWith: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Retrieves a list of schemas in Snowflake, allowing you to view how your databases are organized into logical groups.

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

    def get_statements_snowflake(
        self,
        async: Optional[str] = None,
        requestId: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Retrieves a list of executed SQL statements in Snowflake, allowing for tracking and monitoring of past queries.

        Args:
            async: 
            requestId: 
        Returns:
            API response as a dictionary.
        """
        ...

    def get_tables_snowflake(
        self,
        deep: Optional[str] = None,
        fromName: Optional[str] = None,
        history: Optional[str] = None,
        like: Optional[str] = None,
        showLimit: Optional[str] = None,
        startsWith: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Retrieves a list of tables in Snowflake, helping you to identify all structured data objects within your databases.

        Args:
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

    def get_user_grants_snowflake(
        self,
    ) -> Dict[str, Any]:
        """Retrieves the grants assigned to a user in Snowflake, providing insights into their permissions and access rights.
        Returns:
            API response as a dictionary.
        """
        ...

    def get_warehouses_snowflake(
        self,
        like: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Retrieves a list of warehouses in Snowflake, providing visibility into available computational resources for query processing.

        Args:
            like: 
        Returns:
            API response as a dictionary.
        """
        ...

