"""Fastn Ninox connector — auto-generated type stubs.

Do not edit manually. Regenerate with `fastn connector sync`.
"""
from __future__ import annotations

from typing import Any, Dict, List, Optional, TypedDict


class NinoxConnector:
    """Ninox connector ().

    Provides 13 tools.
    """

    def ninox_create_record(
        self,
        body: List[Any],
        databaseID: str,
        tableID: str,
        teamID: str,
    ) -> Dict[str, Any]:
        """Creates one or more new records in a specified table within a Ninox database. Use this tool when you need to add new entries to a given team, database, and table. Do NOT use this tool to update existing records — use ninox_update_record instead. This action permanently writes new data to the database.

        Args:
            body:  (required)
            databaseID: The unique identifier of the database. (required)
            tableID: The unique identifier of the table. (required)
            teamID: The unique identifier of the team. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def ninox_delete_record(
        self,
        databaseID: str,
        recordID: str,
        tableID: str,
        teamID: str,
    ) -> Dict[str, Any]:
        """Permanently deletes a single record from a specified table in a Ninox database. Use this tool when you need to remove one specific record identified by its record ID from a given team, database, and table. Do NOT use this tool to delete multiple records at once — use ninox_delete_records instead. This action is irreversible; the deleted record cannot be recovered.

        Args:
            databaseID: The unique identifier for the target database. (required)
            recordID: The unique identifier for the target record. (required)
            tableID: The unique identifier for the target table. (required)
            teamID: The unique identifier for the team owning the database. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def ninox_delete_records(
        self,
        databaseId: str,
        tableId: str,
        teamId: str,
        body: Optional[List[Any]] = None,
    ) -> Dict[str, Any]:
        """Permanently deletes multiple records from a specified table in a Ninox database in a single request. Use this tool when you need to bulk-remove several records from a given team, database, and table. Do NOT use this tool to delete a single record — use ninox_delete_record instead. This action is irreversible; deleted records cannot be recovered.

        Args:
            databaseId:  (required)
            tableId:  (required)
            teamId:  (required)
            body: 
        Returns:
            API response as a dictionary.
        """
        ...

    def ninox_execute_read_only_get_query(
        self,
        databaseID: str,
        query: str,
        teamID: str,
    ) -> Dict[str, Any]:
        """Executes a read-only Ninox script query using HTTP GET to retrieve data from a specified Ninox database without modifying it. Use this tool when you want to run a simple read query that can be passed as URL parameters. Do NOT use this tool if your query payload is large (use ninox_execute_read_only_post_query) or if you need to modify data (use ninox_execute_writable_query). This is a read-only operation with no side effects.

        Args:
            databaseID: The ID of the database. (required)
            query: The query string for the Ninox API request. (required)
            teamID: The ID of the team. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def ninox_execute_read_only_post_query(
        self,
        databaseID: str,
        query: str,
        teamID: str,
    ) -> Dict[str, Any]:
        """Executes a read-only Ninox script query using HTTP POST to retrieve data from a specified Ninox database without modifying it. Use this tool when your query payload is too large for a GET request or when you need to send a structured query body. Do NOT use this tool if you need to modify data — use ninox_execute_writable_query instead. This is a read-only operation with no side effects.

        Args:
            databaseID: The ID of the Ninox database. (required)
            query: The query to be executed on the Ninox database. (required)
            teamID: The ID of the Ninox team. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def ninox_execute_writable_query(
        self,
        databaseID: str,
        query: str,
        teamID: str,
    ) -> Dict[str, Any]:
        """Executes a writable Ninox script query that modifies data in a specified Ninox database. Use this tool when you need to perform data-write operations (inserts, updates, deletes, or complex logic) using the Ninox scripting language via the exec endpoint. Do NOT use this tool for read-only queries — use ninox_execute_read_only_post_query or ninox_execute_read_only_get_query instead. This action modifies data and may be irreversible depending on the script executed.

        Args:
            databaseID: The ID of the Ninox database. (required)
            query: The Ninox query string. (required)
            teamID: The ID of the Ninox team. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def ninox_get_database(
        self,
        databaseID: str,
        teamID: str,
    ) -> Dict[str, Any]:
        """Retrieves the details and metadata of a single Ninox database within a specified team workspace. Use this tool when you need to inspect a specific databases configuration, name, or schema information by its database ID. Do NOT use this tool to list all databases — use ninox_list_databases instead. This is a read-only operation with no side effects.

        Args:
            databaseID: The unique identifier for the target Ninox database. (required)
            teamID: The unique identifier for the team accessing the database. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def ninox_get_record(
        self,
        databaseID: str,
        recordID: str,
        tableID: str,
        teamID: str,
        choiceStyle: Optional[str] = None,
        style: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Retrieves the full details of a single record from a specified table in a Ninox database. Use this tool when you need to fetch all field values for one specific record identified by its record ID. Do NOT use this tool to retrieve multiple records — use ninox_list_records instead. This is a read-only operation with no side effects.

        Args:
            databaseID: The unique identifier of the Ninox database. (required)
            recordID: The unique identifier of the record within the table. (required)
            tableID: The unique identifier of the table within the database. (required)
            teamID: The unique identifier of the team associated with the database. (required)
            choiceStyle: Specifies the style of choices (e.g., dropdown, radio buttons).
            style: Specifies the style of the element (e.g., text field, number field).
        Returns:
            API response as a dictionary.
        """
        ...

    def ninox_get_workspace(
        self,
        teamID: str,
    ) -> Dict[str, Any]:
        """Retrieves the details and metadata of a single Ninox team workspace identified by its team ID. Use this tool when you need to inspect a specific workspaces configuration or properties. Do NOT use this tool to list all workspaces — use ninox_list_workspaces instead. This is a read-only operation with no side effects.

        Args:
            teamID: The ID of the Ninox team. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def ninox_list_databases(
        self,
        teamID: str,
    ) -> Dict[str, Any]:
        """Retrieves a list of all Ninox databases available within a specified team workspace. Use this tool when you need to discover available databases or obtain database IDs for use in other Ninox tools. Do NOT use this tool to retrieve details of a single database — use ninox_get_database instead. This is a read-only operation with no side effects.

        Args:
            teamID: The ID of the Ninox team. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def ninox_list_records(
        self,
        databaseID: str,
        tableID: str,
        teamID: str,
        choiceStyle: Optional[str] = None,
        style: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Retrieves all records from a specified table in a Ninox database. Use this tool when you need to fetch a full list of records from a given team, database, and table. Do NOT use this tool to retrieve a single record — use ninox_get_record instead. This is a read-only operation with no side effects.

        Args:
            databaseID: The unique identifier for the target database. (required)
            tableID: The unique identifier for the target table within the database. (required)
            teamID: The unique identifier for the team associated with the database and table. (required)
            choiceStyle: Specifies the style for choice fields.
            style: Specifies the style for the request.
        Returns:
            API response as a dictionary.
        """
        ...

    def ninox_list_workspaces(
        self,
    ) -> Dict[str, Any]:
        """Retrieves a list of all Ninox team workspaces accessible with the authenticated credentials. Use this tool when you need to discover available workspaces or obtain team IDs for use in other Ninox tools. Do NOT use this tool to retrieve details of a single workspace — use ninox_get_workspace instead. This is a read-only operation with no side effects.
        Returns:
            API response as a dictionary.
        """
        ...

    def ninox_update_record(
        self,
        databaseId: str,
        recordId: str,
        tableId: str,
        teamID: str,
        body: Optional[List[Any]] = None,
    ) -> Dict[str, Any]:
        """Updates the field values of an existing record in a specified Ninox table. Use this tool when you need to modify one or more fields of a single record identified by its record ID. Do NOT use this tool to create new records — use ninox_create_record instead. This action overwrites the specified fields of the existing record.

        Args:
            databaseId:  (required)
            recordId:  (required)
            tableId:  (required)
            teamID:  (required)
            body: 
        Returns:
            API response as a dictionary.
        """
        ...

