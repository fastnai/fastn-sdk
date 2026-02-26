"""Fastn Domo connector — auto-generated type stubs.

Do not edit manually. Regenerate with `fastn connector sync`.
"""
from __future__ import annotations

from typing import Any, Dict, List, Optional


class DomoConnector:
    """Domo connector ().

    Provides 7 tools.
    """

    def commit_upload(
        self,
        action: Optional[str] = None,
        index: Optional[bool] = None,
        restateDataTag: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Finalizes the data upload process in the connector, committing the uploaded data to the specified dataset.

        Args:
            action: 
            index: 
            restateDataTag: 
        Returns:
            API response as a dictionary.
        """
        ...

    def create_dataset(
        self,
        dataSourceName: Optional[str] = None,
        schema: Optional[Dict[str, Any]] = None,
        userDefinedType: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Creates a new dataset within the specified connector, allowing you to define its parameters and structure.

        Args:
            dataSourceName: 
            schema: 
            userDefinedType: 
        Returns:
            API response as a dictionary.
        """
        ...

    def create_upload(
        self,
        action: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Initiates a data upload process in the selected connector, setting up the context for the data transfer.

        Args:
            action: 
        Returns:
            API response as a dictionary.
        """
        ...

    def execute_query(
        self,
        XDOMODeveloperToken: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Executes a query against the selected database using the designated query language in the connector.

        Args:
            XDOMODeveloperToken: 
        Returns:
            API response as a dictionary.
        """
        ...

    def get_dataset_schema(
        self,
    ) -> Dict[str, Any]:
        """Fetches the schema of a specific dataset, providing details about its structure and fields in the selected connector.
        Returns:
            API response as a dictionary.
        """
        ...

    def get_datasets(
        self,
        limit: Optional[str] = None,
        offset: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Retrieves a list of available datasets in the specified data connector.

        Args:
            limit: 
            offset: 
        Returns:
            API response as a dictionary.
        """
        ...

    def upload_data(
        self,
    ) -> Dict[str, Any]:
        """Uploads data to an ongoing upload session in the connector, allowing you to send data in chunks.
        Returns:
            API response as a dictionary.
        """
        ...

