"""Fastn Domo connector — auto-generated type stubs.

Do not edit manually. Regenerate with `fastn connector sync`.
"""
from __future__ import annotations

from typing import Any, Dict, List, Optional, TypedDict


class _DomoCreateDatasetSchema(TypedDict, total=False):
    columns: List[Any]

class DomoConnector:
    """Domo connector ().

    Provides 7 tools.
    """

    def domo_commit_upload(
        self,
        action: Optional[str] = None,
        datasetId: Optional[str] = None,
        index: Optional[bool] = None,
        restateDataTag: Optional[str] = None,
        uploadId: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Finalizes and commits a multi-part data upload session to a Domo dataset. Use this tool after all data parts have been uploaded via domo_upload_data to make the uploaded data available in the target dataset. Do not use this tool before all parts of the upload session have been successfully submitted. This action is irreversible — once committed, the data is written to the dataset.

        Args:
            action: 
            datasetId: 
            index: 
            restateDataTag: 
            uploadId: 
        Returns:
            API response as a dictionary.
        """
        ...

    def domo_create_dataset(
        self,
        dataSourceName: Optional[str] = None,
        schema: Optional[_DomoCreateDatasetSchema] = None,
        userDefinedType: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Creates a new dataset in Domo with a defined schema and parameters. Use this tool when you need to establish a new data source destination before uploading data. Do not use this tool to modify an existing dataset. This action creates a persistent dataset record in Domo.

        Args:
            dataSourceName: 
            schema: 
            userDefinedType: 
        Returns:
            API response as a dictionary.
        """
        ...

    def domo_create_upload(
        self,
        action: Optional[str] = None,
        datasetId: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Initiates a new multi-part data upload session for a Domo dataset. Use this tool to begin a data transfer workflow before sending data chunks via domo_upload_data. Returns an upload session ID required for subsequent upload and commit calls. Do not use this tool if you intend to upload data in a single step without a multi-part session.

        Args:
            action: 
            datasetId: 
        Returns:
            API response as a dictionary.
        """
        ...

    def domo_execute_query(
        self,
        XDOMODeveloperToken: Optional[str] = None,
        datasetId: Optional[str] = None,
        sql: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Executes a SQL query against a specified Domo dataset and returns the result set. Use this tool to retrieve, filter, or aggregate data stored in a Domo dataset. Do not use this tool to modify dataset structure or upload data — use domo_create_dataset or domo_create_upload for those operations. Query execution may consume compute resources depending on dataset size.

        Args:
            XDOMODeveloperToken: 
            datasetId: 
            sql: 
        Returns:
            API response as a dictionary.
        """
        ...

    def domo_get_dataset_schema(
        self,
    ) -> Dict[str, Any]:
        """Retrieves the indexed schema of a specific Domo dataset, including field names, data types, and structural metadata. Use this tool when you need to understand the structure of a dataset before querying or uploading data. Do not use this tool to retrieve the actual data rows — use domo_execute_query for that.
        Returns:
            API response as a dictionary.
        """
        ...

    def domo_list_datasets(
        self,
        limit: Optional[str] = None,
        offset: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Retrieves a list of all available datasets in Domo. Use this tool to discover existing datasets, their IDs, and metadata before performing operations such as querying or uploading. Do not use this tool to retrieve data from within a dataset — use domo_execute_query for that.

        Args:
            limit: 
            offset: 
        Returns:
            API response as a dictionary.
        """
        ...

    def domo_upload_data(
        self,
        body: Optional[str] = None,
        datasetId: Optional[str] = None,
        partId: Optional[str] = None,
        uploadId: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Uploads a single part (chunk) of data to an active Domo upload session for a specific dataset. Use this tool to send data in parts as part of a multi-part upload workflow initiated by domo_create_upload. Each call uploads one part identified by a part ID. Do not use this tool before creating an upload session with domo_create_upload or after the session has been committed. This tool does not finalize the upload — call domo_commit_upload when all parts are sent.

        Args:
            body: 
            datasetId: 
            partId: 
            uploadId: 
        Returns:
            API response as a dictionary.
        """
        ...

