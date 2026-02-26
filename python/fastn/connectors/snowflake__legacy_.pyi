"""Fastn Snowflake (legacy) connector — auto-generated type stubs.

Do not edit manually. Regenerate with `fastn connector sync`.
"""
from __future__ import annotations

from typing import Any, Dict, List, Optional


class SnowflakeLegacyConnector:
    """Snowflake (legacy) connector ().

    Provides 9 tools.
    """

    def execute_query(
        self,
        database: str,
        query: str,
        schema: Optional[str] = None,
        warehouse: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Executes a specified SQL query on an active database connection established via the Snowflake SQL connector, retrieving or modifying data as instructed.

        Args:
            database: The name of the database to execute the query against. (required)
            query: The SQL query to be executed. (required)
            schema: The name of the schema containing the target database objects.
            warehouse: 
        Returns:
            API response as a dictionary.
        """
        ...

    def generate_token(
        self,
        client_id: str,
        client_secret: str,
        code: str,
    ) -> Dict[str, Any]:
        """Generates a new authentication token for use with your connected applications and services, providing secure access to resources via the generateToken connector.

        Args:
            client_id: Client ID for Snowflake authentication. (required)
            client_secret: Client secret for Snowflake authentication. (required)
            code: Authorization code received from Snowflake. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def get_databases(
        self,
        warehouse: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Retrieves a list of all databases available in the connected Snowflake environment using the getDatabases connector, enabling exploration of data sources.

        Args:
            warehouse: 
        Returns:
            API response as a dictionary.
        """
        ...

    def get_schemas(
        self,
        database: Optional[str] = None,
        warehouse: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Fetches all schemas associated with a given database in Snowflake using the getSchemas connector, aiding users in navigating the database structure.

        Args:
            database: 
            warehouse: 
        Returns:
            API response as a dictionary.
        """
        ...

    def get_table_schema(
        self,
        database: Optional[str] = None,
        tableName: Optional[str] = None,
        warehouse: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Retrieves the schema of a specified table in Snowflake using the getTableSchema connector, providing insight into the organization and types of data within that table.

        Args:
            database: 
            tableName: 
            warehouse: 
        Returns:
            API response as a dictionary.
        """
        ...

    def get_tables(
        self,
        database: str,
        warehouse: str,
    ) -> Dict[str, Any]:
        """Fetches information about all tables within a specified database in Snowflake using the getTables connector, helping users understand the structure of their data.

        Args:
            database: The name of the database to connect to. (required)
            warehouse:  (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def get_user_permissions(
        self,
    ) -> Dict[str, Any]:
        """Obtains user permissions for accessing various resources in the Snowflake environment using the getUserPermissions connector, facilitating security and compliance management.
        Returns:
            API response as a dictionary.
        """
        ...

    def get_warehouses(
        self,
    ) -> Dict[str, Any]:
        """Lists all available warehouses in the connected Snowflake account via the getWarehouses connector, allowing users to manage compute resources effectively.
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

