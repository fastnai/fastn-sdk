"""Fastn CockroachDB connector — auto-generated type stubs.

Do not edit manually. Regenerate with `fastn connector sync`.
"""
from __future__ import annotations

from typing import Any, Dict, List, Optional, TypedDict


class CockroachdbConnector:
    """CockroachDB connector ().

    Provides 6 tools.
    """

    def cockroachdb_execute_query(
        self,
        query: str,
    ) -> Dict[str, Any]:
        """Executes a raw SQL query against a specified CockroachDB database and returns the results. Use this tool when you need to run SELECT statements to retrieve data or execute DML/DDL statements (INSERT, UPDATE, DELETE, CREATE, DROP) when other structured tools are insufficient. Be aware that write queries (INSERT, UPDATE, DELETE, DROP, etc.) will modify or permanently delete data and are irreversible without a backup. Always validate the SQL query before execution to avoid unintended data loss.

        Args:
            query: The SQL query to be executed. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def cockroachdb_list_databases(
        self,
    ) -> Dict[str, Any]:
        """Lists all databases available in the connected CockroachDB instance. Use this tool when you need to discover which databases exist before querying a specific one or inspecting its tables. Do not use this tool to list tables within a database — use cockroachdb_list_tables instead. This tool is read-only and has no side effects.
        Returns:
            API response as a dictionary.
        """
        ...

    def cockroachdb_list_roles(
        self,
        database: str,
    ) -> Dict[str, Any]:
        """Lists all roles defined in the connected CockroachDB instance, including information on each roles permissions and access levels. Use this tool when you need to audit or inspect role-based access control (RBAC) configurations. Do not use this tool to list individual users — use cockroachdb_list_users instead. This tool is read-only and has no side effects.

        Args:
            database: The name of the database to connect to. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def cockroachdb_list_table_columns(
        self,
        table_name: str,
    ) -> Dict[str, Any]:
        """Lists all columns for a specified table in the connected CockroachDB database, returning column names, data types, and structural metadata. Use this tool when you need to inspect the schema of a specific table before constructing queries or validating data structure. Do not use this tool to list all tables — use cockroachdb_list_tables instead. This tool is read-only and has no side effects.

        Args:
            table_name: The name of the table to interact with. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def cockroachdb_list_tables(
        self,
    ) -> Dict[str, Any]:
        """Lists all tables present in a specified CockroachDB database, allowing you to inspect the database structure. Use this tool when you need to discover available tables before querying or examining schemas. Do not use this tool to retrieve column details for a specific table — use cockroachdb_list_table_columns instead. This tool is read-only and has no side effects.
        Returns:
            API response as a dictionary.
        """
        ...

    def cockroachdb_list_users(
        self,
    ) -> Dict[str, Any]:
        """Lists all users registered in the connected CockroachDB instance, enabling user management and oversight. Use this tool when you need to enumerate database users, for example to audit access or verify a user exists before granting permissions. Do not use this tool to list roles — use cockroachdb_list_roles instead. This tool is read-only and has no side effects.
        Returns:
            API response as a dictionary.
        """
        ...

