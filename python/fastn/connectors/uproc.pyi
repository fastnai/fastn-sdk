"""Fastn uProc connector — auto-generated type stubs.

Do not edit manually. Regenerate with `fastn connector sync`.
"""
from __future__ import annotations

from typing import Any, Dict, List, Optional, TypedDict


class _UprocProcessMultipleParams(TypedDict, total=False):
    mobile: List[Any]

class _UprocProcessMultipleCallback(TypedDict, total=False):
    data: str
    end: str
    error: str
    progress: str
    start: str

class _UprocProcessRowParams(TypedDict, total=False):
    mobile: str

class _UprocProcessRowWithCallbackCallback(TypedDict, total=False):
    data: str

class _UprocProcessRowWithCallbackParams(TypedDict, total=False):
    mobile: str

class _UprocStreamProcessCallback(TypedDict, total=False):
    data: str
    end: str
    error: str
    progress: str
    start: str

class UprocConnector:
    """uProc connector ().

    Provides 4 tools.
    """

    def uproc_process_multiple(
        self,
        params: _UprocProcessMultipleParams,
        processor: str,
        callback: Optional[_UprocProcessMultipleCallback] = None,
        limit: Optional[str] = None,
        normalized: Optional[bool] = None,
        write_titles: Optional[bool] = None,
    ) -> Dict[str, Any]:
        """Submits multiple data rows to the uProc API for batch processing in a single request, allowing validation, cleaning, or enrichment of several records at once. Use this tool when you have more than one record to process and want to reduce the number of API calls. Do not use this tool for a single record — use uproc_process_row instead. Do not use this tool for continuous real-time data streams — use uproc_stream_process instead.

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

    def uproc_process_row(
        self,
        params: _UprocProcessRowParams,
        processor: str,
        cache: Optional[bool] = None,
        limit: Optional[str] = None,
        normalized: Optional[bool] = None,
    ) -> Dict[str, Any]:
        """Submits a single data row to the uProc API for synchronous processing, such as validating, cleaning, or enriching an individual data record. Use this tool when you need to process exactly one record and want an immediate response. Do not use this tool for multiple records — use uproc_process_multiple instead. Do not use this tool if you need an asynchronous callback — use uproc_process_row_with_callback instead.

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

    def uproc_process_row_with_callback(
        self,
        callback: _UprocProcessRowWithCallbackCallback,
        params: _UprocProcessRowWithCallbackParams,
        processor: str,
        cache: Optional[bool] = None,
        limit: Optional[str] = None,
        normalized: Optional[bool] = None,
    ) -> Dict[str, Any]:
        """Submits a single data row to the uProc API for processing and registers a callback URL to receive the result asynchronously once processing is complete. Use this tool when you need to process one record at a time and want to be notified upon completion rather than waiting for a synchronous response. Do not use this tool if you do not need a callback — use uproc_process_row for synchronous single-row processing instead.

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

    def uproc_stream_process(
        self,
        processors: List[Any],
        stream: str,
        callback: Optional[_UprocStreamProcessCallback] = None,
        first_row: Optional[str] = None,
        last_row: Optional[str] = None,
        limit: Optional[str] = None,
        upload_results: Optional[bool] = None,
        write_titles: Optional[bool] = None,
    ) -> Dict[str, Any]:
        """Streams a continuous flow of data records to the uProc API for real-time processing. Use this tool when you need to process a high-throughput or ongoing stream of data that requires immediate handling as records arrive. Do not use this tool for single-record or small batch operations — use uproc_process_row or uproc_process_multiple instead.

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

