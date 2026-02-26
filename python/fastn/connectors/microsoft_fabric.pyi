"""Fastn Microsoft Fabric connector — auto-generated type stubs.

Do not edit manually. Regenerate with `fastn connector sync`.
"""
from __future__ import annotations

from typing import Any, Dict, List, Optional


class MicrosoftFabricConnector:
    """Microsoft Fabric connector ().

    Provides 17 tools.
    """

    def create_dataset(
        self,
        name: str,
        tables: Optional[List[Any]] = None,
    ) -> Dict[str, Any]:
        """Creates a new dataset in the data management system.

        Args:
            name: Name of the dataset or operation. (required)
            tables: 
        Returns:
            API response as a dictionary.
        """
        ...

    def create_event_house(
        self,
        displayName: str,
        description: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Creates a new event house in the event management system.

        Args:
            displayName: Display name for the Microsoft Fabric resource. (required)
            description: Description of the Microsoft Fabric resource.
        Returns:
            API response as a dictionary.
        """
        ...

    def create_group(
        self,
        workspaceV2: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Creates a new group in the user management system.

        Args:
            workspaceV2: Workspace ID (V2) for the Microsoft Fabric API request.
        Returns:
            API response as a dictionary.
        """
        ...

    def create_kql_database(
        self,
        creationPayload: Dict[str, Any],
        displayName: str,
        description: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Sets up a new KQL (Kusto Query Language) database in the data management system.

        Args:
            creationPayload: Payload for creating a resource in Microsoft Fabric. (required)
            displayName: Display name for the resource in Microsoft Fabric. (required)
            description: Description of the resource in Microsoft Fabric.
        Returns:
            API response as a dictionary.
        """
        ...

    def execute_kql_query(
        self,
        csl: str,
        db: str,
        properties: str,
    ) -> Dict[str, Any]:
        """Executes a KQL query against a specified KQL database in the data management system.

        Args:
            csl: The CSL (Common Schema Language) query string. (required)
            db: The name of the database to query. (required)
            properties: Additional properties for the request. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def generate_token(
        self,
        client_id: str,
        client_secret: str,
        password: str,
        scope: str,
        username: str,
    ) -> Dict[str, Any]:
        """Generates a new token for authentication in the API context.

        Args:
            client_id: Client ID for Microsoft Fabric authentication. (required)
            client_secret: Client secret for Microsoft Fabric authentication. (required)
            password: User password for Microsoft Fabric authentication. (required)
            scope: Scope of access for the Microsoft Fabric API. (required)
            username: Username for Microsoft Fabric authentication. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def get_dataset(
        self,
        datasetId: str,
        groupId: str,
    ) -> Dict[str, Any]:
        """Fetches details of a specific dataset in the data management system.

        Args:
            datasetId: The ID of the dataset in Microsoft Fabric. (required)
            groupId: The ID of the group containing the dataset in Microsoft Fabric. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def get_datasets(
        self,
        groupId: str,
    ) -> Dict[str, Any]:
        """Retrieves a list of datasets available in the data management system.

        Args:
            groupId: ID of the group for the Microsoft Fabric API request. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def get_event_house(
        self,
        eventHouseId: str,
        workspaceId: str,
    ) -> Dict[str, Any]:
        """Fetches details of a specific event house in the event management system.

        Args:
            eventHouseId: Identifier for the event house in Microsoft Fabric. (required)
            workspaceId: Identifier for the workspace in Microsoft Fabric. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def get_event_houses(
        self,
        workspaceId: str,
    ) -> Dict[str, Any]:
        """Fetches all event houses in the event management system.

        Args:
            workspaceId: ID of the workspace in Microsoft Fabric. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def get_group_by_id(
        self,
        groupId: str,
    ) -> Dict[str, Any]:
        """Fetches information about a specific group by its ID in the user management system.

        Args:
            groupId: ID of the group for the Microsoft Fabric API request. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def get_groups(
        self,
    ) -> Dict[str, Any]:
        """Retrieves a list of groups in the specified user management system.
        Returns:
            API response as a dictionary.
        """
        ...

    def get_kql_database(
        self,
        kqlDatabaseId: str,
        workspaceId: str,
    ) -> Dict[str, Any]:
        """Retrieves details of a specific KQL database in the data management system.

        Args:
            kqlDatabaseId: ID of the KQL database in Microsoft Fabric. (required)
            workspaceId: ID of the workspace in Microsoft Fabric. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def get_kql_database_creation_status(
        self,
        location: str,
    ) -> Dict[str, Any]:
        """Checks the creation status of a KQL database in the data management system.

        Args:
            location: Location of the resource in Microsoft Fabric. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def get_kql_databases(
        self,
        workspaceId: str,
    ) -> Dict[str, Any]:
        """Retrieves a list of KQL databases available in the data management system.

        Args:
            workspaceId: Workspace ID for the Microsoft Fabric workspace. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def post_rows(
        self,
        rows: List[Any],
    ) -> Dict[str, Any]:
        """Posts new rows of data to a specified dataset in the data management system.

        Args:
            rows:  (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def put_table(
        self,
        columns: List[Any],
        name: str,
    ) -> Dict[str, Any]:
        """Updates or adds a table in the specified dataset of the data management system.

        Args:
            columns:  (required)
            name: Name of the dataset or table in Microsoft Fabric. (required)
        Returns:
            API response as a dictionary.
        """
        ...

