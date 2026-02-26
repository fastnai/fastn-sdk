"""Fastn Power BI connector — auto-generated type stubs.

Do not edit manually. Regenerate with `fastn connector sync`.
"""
from __future__ import annotations

from typing import Any, Dict, List, Optional


class PowerBiConnector:
    """Power BI connector ().

    Provides 6 tools.
    """

    def create_dataset(
        self,
        name: str,
        tables: List[Any],
    ) -> Dict[str, Any]:
        """Creates a new dataset in the specified connector, enabling you to store and manage data relevant to your application's requirements.

        Args:
            name: Name of the dataset or operation. (required)
            tables:  (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def generate_token(
        self,
    ) -> Dict[str, Any]:
        """Generates an authentication token for the specified connector, which can be used to secure API requests and maintain access to the services provided.
        Returns:
            API response as a dictionary.
        """
        ...

    def get_dataset(
        self,
        datasetId: str,
    ) -> Dict[str, Any]:
        """Retrieves a dataset from the specified connector, allowing you to access existing data for analysis or integration within your application.

        Args:
            datasetId: ID of the dataset in Power BI. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def post_rows(
        self,
        rows: List[Any],
    ) -> Dict[str, Any]:
        """Posts new rows of data to an existing dataset in the specified connector, facilitating the addition of information and updates to data records.

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
        """Updates an existing table in the specified connector with new schema or data, ensuring the structure and contents meet the current needs of your application.

        Args:
            columns:  (required)
            name: Name of the dataset. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def refresh_token(
        self,
        client_id: str,
        client_secret: str,
        redirect_uri: str,
        refresh_token: str,
    ) -> Dict[str, Any]:
        """Refreshes an authentication token for the specified connector, allowing continued access to services without needing to re-authenticate.

        Args:
            client_id: Client ID for Power BI API authentication. (required)
            client_secret: Client secret for Power BI API authentication. (required)
            redirect_uri: Redirect URI for Power BI API authentication. (required)
            refresh_token: Refresh token for Power BI API authentication. (required)
        Returns:
            API response as a dictionary.
        """
        ...

