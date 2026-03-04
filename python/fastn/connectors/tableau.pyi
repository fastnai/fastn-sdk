"""Fastn Tableau connector — auto-generated type stubs.

Do not edit manually. Regenerate with `fastn connector sync`.
"""
from __future__ import annotations

from typing import Any, Dict, List, Optional, TypedDict


class _TableauGenerateAuthTokenTsrequest(TypedDict, total=False):
    credentials: Dict[str, Any]

class TableauConnector:
    """Tableau connector ().

    Provides 7 tools.
    """

    def tableau_create_datasource(
        self,
        data: Optional[List[Any]] = None,
        tableau_data_source_name: Optional[str] = None,
        tableau_project_id: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Creates and publishes a new data source in Tableau, making it available for use in dashboards, reports, and analysis. Use this when importing a new dataset into Tableau for the first time. Do not use this to update an existing data source; use tableau_publish_datasource to republish.

        Args:
            data: 
            tableau_data_source_name: 
            tableau_project_id: 
        Returns:
            API response as a dictionary.
        """
        ...

    def tableau_create_project(
        self,
        projectDescription: Optional[str] = None,
        projectName: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Creates a new project in the connected Tableau environment for organizing related data sources and workbooks. Use this to set up a new organizational container before publishing content. Do not use this to list existing projects; use tableau_list_projects instead.

        Args:
            projectDescription: Description of the Tableau project.
            projectName: Name of the Tableau project.
        Returns:
            API response as a dictionary.
        """
        ...

    def tableau_generate_auth_token(
        self,
        connection: Dict[str, Any],
        _omit_xml_declaration: Optional[str] = None,
        tsRequest: Optional[_TableauGenerateAuthTokenTsrequest] = None,
    ) -> Dict[str, Any]:
        """Authenticates with the Tableau API and returns a session authentication token required to authorize subsequent API calls. Use this before making any other Tableau API requests that require authentication. This call creates a server-side session. Do not use this for end-user authentication or non-Tableau services.

        Args:
            connection: Details about the connection to the Tableau server. (required)
            _omit_xml_declaration: Flag to omit XML declaration.
            tsRequest: Object containing Tableau specific request parameters.
        Returns:
            API response as a dictionary.
        """
        ...

    def tableau_list_datasources(
        self,
    ) -> Dict[str, Any]:
        """Returns a list of all data sources available in the connected Tableau environment. Use this to discover what datasets are published and ready for reporting and analysis. Do not use this to retrieve table schemas within a data source; use tableau_list_tables instead.
        Returns:
            API response as a dictionary.
        """
        ...

    def tableau_list_projects(
        self,
    ) -> Dict[str, Any]:
        """Returns a list of all projects in the connected Tableau environment. Use this to browse the organizational structure of Tableau workbooks and data sources. Do not use this to create a new project; use tableau_create_project instead.
        Returns:
            API response as a dictionary.
        """
        ...

    def tableau_list_tables(
        self,
        datasourceID: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Returns the table schema from a specified Tableau data source, including table names and column structures. Use this to understand the data structure of a data source before querying or building reports. Do not use this to list data sources; use tableau_list_datasources instead.

        Args:
            datasourceID: 
        Returns:
            API response as a dictionary.
        """
        ...

    def tableau_publish_datasource(
        self,
        listOfItems: List[Any],
        table_name: str,
        tableau_data_source_name: str,
        tableau_project_id: str,
        tableau_url: str,
        write_mode: str,
    ) -> Dict[str, Any]:
        """Publishes a data source to the connected Tableau environment, making it available for use in dashboards and reports. Use this to push an existing or updated data source to Tableau. Do not use this to create a brand-new data source from scratch; use tableau_create_datasource instead.

        Args:
            listOfItems:  (required)
            table_name: The name of the table in Tableau. (required)
            tableau_data_source_name: The name of the Tableau data source. (required)
            tableau_project_id: The ID of the Tableau project. (required)
            tableau_url: The URL of the Tableau server. (required)
            write_mode: The mode to write data to Tableau (e.g., append, overwrite). (required)
        Returns:
            API response as a dictionary.
        """
        ...

