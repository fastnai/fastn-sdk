"""Fastn AWS Kinesis connector — auto-generated type stubs.

Do not edit manually. Regenerate with `fastn connector sync`.
"""
from __future__ import annotations

from typing import Any, Dict, List, Optional


class AwsKinesisConnector:
    """AWS Kinesis connector ().

    Provides 13 tools.
    """

    def create_policy(
        self,
        Policy: Optional[str] = None,
        ResourceARN: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Creates a new policy for managing access and permissions within the specified data connector, which governs how resources are accessed.

        Args:
            Policy: 
            ResourceARN: 
        Returns:
            API response as a dictionary.
        """
        ...

    def create_record(
        self,
        Data: Optional[str] = None,
        PartitionKey: Optional[str] = None,
        StreamName: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Creates a new record in the specified stream of the data connector, enabling the insertion of fresh data into the stream.

        Args:
            Data: 
            PartitionKey: 
            StreamName: 
        Returns:
            API response as a dictionary.
        """
        ...

    def create_stream(
        self,
        ShardCount: Optional[float] = None,
        StreamModeDetails: Optional[Dict[str, Any]] = None,
        StreamName: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Creates a new stream in the specified data connector, allowing data to be ingested and processed.

        Args:
            ShardCount: 
            StreamModeDetails: 
            StreamName: 
        Returns:
            API response as a dictionary.
        """
        ...

    def delete_stream(
        self,
        StreamName: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Deletes a specified stream in the data connector, removing all associated data and configurations.

        Args:
            StreamName: 
        Returns:
            API response as a dictionary.
        """
        ...

    def describe_stream(
        self,
        StreamName: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Describes the details of a specific stream in the specified data connector, providing insights on its configuration and status.

        Args:
            StreamName: 
        Returns:
            API response as a dictionary.
        """
        ...

    def get_records(
        self,
        Limit: Optional[int] = None,
        ShardIterator: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Retrieves records from a specific stream in the specified data connector, allowing consumers to read the latest data.

        Args:
            Limit: 
            ShardIterator: 
        Returns:
            API response as a dictionary.
        """
        ...

    def get_resource_policy(
        self,
        ResourceARN: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Retrieves the resource policy associated with the specified data connector, detailing the permissions and access controls in place.

        Args:
            ResourceARN: 
        Returns:
            API response as a dictionary.
        """
        ...

    def get_shard_iterator(
        self,
        ShardId: Optional[str] = None,
        ShardIteratorType: Optional[str] = None,
        StartingSequenceNumber: Optional[str] = None,
        StreamName: Optional[str] = None,
        Timestamp: Optional[float] = None,
    ) -> Dict[str, Any]:
        """Gets a shard iterator for a specific shard within a stream in the specified data connector, which is required for reading data sequentially.

        Args:
            ShardId: 
            ShardIteratorType: 
            StartingSequenceNumber: 
            StreamName: 
            Timestamp: 
        Returns:
            API response as a dictionary.
        """
        ...

    def get_shards(
        self,
        MaxResults: Optional[int] = None,
        StreamName: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Fetches information about the shards of a particular stream in the specified data connector, which helps in understanding data distribution.

        Args:
            MaxResults: 
            StreamName: 
        Returns:
            API response as a dictionary.
        """
        ...

    def get_stream_consumers(
        self,
        MaxResults: Optional[int] = None,
        StreamARN: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Obtains the list of consumers currently associated with a stream in the specified data connector, useful for managing access and permissions.

        Args:
            MaxResults: 
            StreamARN: 
        Returns:
            API response as a dictionary.
        """
        ...

    def get_streams(
        self,
        ExclusiveStartStreamName: Optional[str] = None,
        Limit: Optional[int] = None,
        NextToken: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Retrieves a list of existing streams from the specified data connector, providing details about each stream.

        Args:
            ExclusiveStartStreamName: 
            Limit: 
            NextToken: 
        Returns:
            API response as a dictionary.
        """
        ...

    def merge_shards(
        self,
        AdjacentShardToMerge: Optional[str] = None,
        ShardToMerge: Optional[str] = None,
        StreamName: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Merges two or more shards within a stream in the specified data connector, optimizing data storage and processing efficiency.

        Args:
            AdjacentShardToMerge: 
            ShardToMerge: 
            StreamName: 
        Returns:
            API response as a dictionary.
        """
        ...

    def register_consumer(
        self,
        ConsumerName: Optional[str] = None,
        StreamARN: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Registers a new consumer for a given stream in the specified data connector, allowing it to process and read data from the stream.

        Args:
            ConsumerName: 
            StreamARN: 
        Returns:
            API response as a dictionary.
        """
        ...

