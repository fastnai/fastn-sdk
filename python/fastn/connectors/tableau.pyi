"""Fastn Tableau connector — auto-generated type stubs.

Do not edit manually. Regenerate with `fastn connector sync`.
"""
from __future__ import annotations

from typing import Any, Dict, List, Optional


class TableauConnector:
    """Tableau connector ().

    Provides 7 tools.
    """

    def create_datasource(
        self,
    ) -> Dict[str, Any]:
        """Creates a new data source in Tableau, enabling users to import and publish data for analysis.
        Returns:
            API response as a dictionary.
        """
        ...

    def create_tableau_project(
        self,
    ) -> Dict[str, Any]:
        """Creates a new project in Tableau, allowing for the organization and management of related data sources and workbooks.
        Returns:
            API response as a dictionary.
        """
        ...

    def generate_auth_token(
        self,
    ) -> Dict[str, Any]:
        """Generates an authentication token for accessing secured endpoints within the application.
        Returns:
            API response as a dictionary.
        """
        ...

    def get_datasources(
        self,
    ) -> Dict[str, Any]:
        """Fetches the available data sources in Tableau, giving an overview of the datasets ready for reporting and analysis.
        Returns:
            API response as a dictionary.
        """
        ...

    def get_projects(
        self,
    ) -> Dict[str, Any]:
        """Retrieves a list of all projects available in Tableau, providing insights into the organizational structure of data.
        Returns:
            API response as a dictionary.
        """
        ...

    def get_tables(
        self,
        datasourceID: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Obtains the table schema from a data source in Tableau, useful for understanding the data structure.

        Args:
            datasourceID: 
        Returns:
            API response as a dictionary.
        """
        ...

    def publish_tableau_data_source(
        self,
    ) -> Dict[str, Any]:
        """Publishes a data source to Tableau, making it available for use in dashboards and reports.
        Returns:
            API response as a dictionary.
        """
        ...

