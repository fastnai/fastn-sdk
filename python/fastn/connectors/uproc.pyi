"""Fastn uProc connector — auto-generated type stubs.

Do not edit manually. Regenerate with `fastn connector sync`.
"""
from __future__ import annotations

from typing import Any, Dict, List, Optional


class UprocConnector:
    """uProc connector ().

    Provides 4 tools.
    """

    def multiple(
        self,
        params: Dict[str, Any],
        processor: str,
        callback: Optional[Dict[str, Any]] = None,
        limit: Optional[str] = None,
        normalized: Optional[bool] = None,
        write_titles: Optional[bool] = None,
    ) -> Dict[str, Any]:
        """Executes multiple operations sequentially using the 'multiple' connector, allowing for handling various tasks in a single workflow.

        Args:
            params: Parameters for the uProc request. (required)
            processor: The processor to be used. (required)
            callback: Callback information.
            limit: A limit for the operation.
            normalized: Indicates whether the data is normalized.
            write_titles: Specifies whether to write titles.
        Returns:
            API response as a dictionary.
        """
        ...

    def one_row(
        self,
        params: Dict[str, Any],
        processor: str,
        cache: Optional[bool] = None,
        limit: Optional[str] = None,
        normalized: Optional[bool] = None,
    ) -> Dict[str, Any]:
        """Performs a single row operation with the 'oneRow' connector, suitable for tasks that require manipulation of individual data entries.

        Args:
            params: Additional parameters for processing. (required)
            processor: Specifies the processor to use. (required)
            cache: 
            limit: 
            normalized: Indicates whether the input data is normalized.
        Returns:
            API response as a dictionary.
        """
        ...

    def one_row_with_callback(
        self,
        callback: Dict[str, Any],
        params: Dict[str, Any],
        processor: str,
        cache: Optional[bool] = None,
        limit: Optional[str] = None,
        normalized: Optional[bool] = None,
    ) -> Dict[str, Any]:
        """Handles a single row operation with the option for a callback using the 'oneRowWithCallback' connector, facilitating additional processing after the main task completion.

        Args:
            callback: Callback information. (required)
            params: Parameters for the uProc process. (required)
            processor: The processor to be used. (required)
            cache: Indicates whether to use caching.
            limit: Limit for the uProc process.
            normalized: Indicates whether the data is normalized.
        Returns:
            API response as a dictionary.
        """
        ...

    def stream(
        self,
        processors: List[Any],
        stream: str,
        callback: Optional[Dict[str, Any]] = None,
        first_row: Optional[str] = None,
        last_row: Optional[str] = None,
        limit: Optional[str] = None,
        upload_results: Optional[bool] = None,
        write_titles: Optional[bool] = None,
    ) -> Dict[str, Any]:
        """Streams data in real-time using the 'stream' connector, perfect for continuous data flow tasks that require immediate processing.

        Args:
            processors:  (required)
            stream: Identifier for the data stream. (required)
            callback: Configuration for callbacks during processing.
            first_row: Index or label of the first row to process.
            last_row: Index or label of the last row to process.
            limit: Limit on the number of rows to process.
            upload_results: Whether to upload processing results.
            write_titles: Whether to write titles to the output.
        Returns:
            API response as a dictionary.
        """
        ...

