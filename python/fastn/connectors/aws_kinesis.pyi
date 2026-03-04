"""Fastn AWS Kinesis connector — auto-generated type stubs.

Do not edit manually. Regenerate with `fastn connector sync`.
"""
from __future__ import annotations

from typing import Any, Dict, List, Optional, TypedDict


class _AwsKinesisCreateStreamStreammodedetails(TypedDict, total=False):
    StreamMode: str

class AwsKinesisConnector:
    """AWS Kinesis connector ().

    Provides 13 tools.
    """

    def aws_kinesis_create_stream(
        self,
        ShardCount: Optional[float] = None,
        StreamModeDetails: Optional[_AwsKinesisCreateStreamStreammodedetails] = None,
        StreamName: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Creates a new AWS Kinesis data stream with a specified name and shard count in the configured region. Use this tool when you need to provision a new stream for real-time data ingestion and processing. Do not use this tool to modify an existing stream or to write records — use the appropriate put record tools for that. Stream creation may take a short time before the stream becomes active.

        Args:
            ShardCount: 
            StreamModeDetails: 
            StreamName: 
        Returns:
            API response as a dictionary.
        """
        ...

    def aws_kinesis_delete_stream(
        self,
        StreamName: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Permanently deletes a specified AWS Kinesis data stream along with all its shards and data. Use this tool only when the stream and all its data are no longer needed. Do not use this tool if any consumers or producers are still active on the stream. This action is irreversible — all unread data in the stream will be lost.

        Args:
            StreamName: 
        Returns:
            API response as a dictionary.
        """
        ...

    def aws_kinesis_describe_stream(
        self,
        StreamName: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Retrieves detailed configuration and status information for a specified AWS Kinesis data stream, including shard details, retention period, stream status, and encryption settings. Use this tool when you need to inspect the current state or configuration of a stream before reading, writing, or modifying it. Do not use this tool to retrieve records from the stream.

        Args:
            StreamName: 
        Returns:
            API response as a dictionary.
        """
        ...

    def aws_kinesis_get_resource_policy(
        self,
        ResourceARN: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Retrieves the resource-based IAM policy attached to a specified AWS Kinesis resource, detailing which principals have access and what actions they are permitted to perform. Use this tool when you need to audit or review access control policies on a Kinesis stream or consumer. Do not use this tool to create or modify policies.

        Args:
            ResourceARN: 
        Returns:
            API response as a dictionary.
        """
        ...

    def aws_kinesis_get_shard_iterator(
        self,
        ShardId: Optional[str] = None,
        ShardIteratorType: Optional[str] = None,
        StartingSequenceNumber: Optional[str] = None,
        StreamName: Optional[str] = None,
        Timestamp: Optional[float] = None,
    ) -> Dict[str, Any]:
        """Retrieves a shard iterator for a specific shard in an AWS Kinesis data stream. A shard iterator is a required cursor that specifies the position in the shard from which to start reading records. Use this tool before calling the get_records tool to establish a read position. Do not use this tool to read records directly — a shard iterator must subsequently be passed to the get_records operation.

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

    def aws_kinesis_list_records(
        self,
        Limit: Optional[int] = None,
        ShardIterator: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Retrieves a batch of data records from a specified shard in an AWS Kinesis data stream using a shard iterator. Use this tool after obtaining a shard iterator via aws_kinesis_get_shard_iterator to sequentially read records from a stream. Do not use this tool without a valid shard iterator, and do not use it to write data to a stream.

        Args:
            Limit: 
            ShardIterator: 
        Returns:
            API response as a dictionary.
        """
        ...

    def aws_kinesis_list_shards(
        self,
        MaxResults: Optional[int] = None,
        StreamName: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Retrieves a list of shards belonging to a specified AWS Kinesis data stream, including shard IDs, hash key ranges, and sequence number ranges. Use this tool when you need to understand the partitioning structure of a stream, or to enumerate shards before obtaining shard iterators for reading. Do not use this tool to read data records directly.

        Args:
            MaxResults: 
            StreamName: 
        Returns:
            API response as a dictionary.
        """
        ...

    def aws_kinesis_list_stream_consumers(
        self,
        MaxResults: Optional[int] = None,
        StreamARN: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Retrieves a list of all enhanced fan-out consumers registered to a specified AWS Kinesis data stream, including their names, ARNs, and registration status. Use this tool when you need to audit or manage the consumers associated with a stream. Do not use this tool to register new consumers or to read data records from the stream.

        Args:
            MaxResults: 
            StreamARN: 
        Returns:
            API response as a dictionary.
        """
        ...

    def aws_kinesis_list_streams(
        self,
        ExclusiveStartStreamName: Optional[str] = None,
        Limit: Optional[int] = None,
        NextToken: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Retrieves a list of all AWS Kinesis data streams available in the configured account and region, including their names and statuses. Use this tool when you need to discover which streams exist before performing stream-level operations. Do not use this tool to retrieve records or shard details from a specific stream.

        Args:
            ExclusiveStartStreamName: 
            Limit: 
            NextToken: 
        Returns:
            API response as a dictionary.
        """
        ...

    def aws_kinesis_merge_shards(
        self,
        AdjacentShardToMerge: Optional[str] = None,
        ShardToMerge: Optional[str] = None,
        StreamName: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Merges two adjacent shards in a specified AWS Kinesis data stream into a single shard, reducing the total number of shards and associated costs. Use this tool when you need to decrease the throughput capacity of a stream or reduce shard costs. Do not use this tool if the shards are not adjacent or if you need to increase stream throughput. This action alters the streams partitioning structure and may affect in-flight data consumers.

        Args:
            AdjacentShardToMerge: 
            ShardToMerge: 
            StreamName: 
        Returns:
            API response as a dictionary.
        """
        ...

    def aws_kinesis_put_record(
        self,
        Data: Optional[str] = None,
        PartitionKey: Optional[str] = None,
        StreamName: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Writes a single data record into a specified AWS Kinesis data stream. Use this tool when you need to publish an individual event or data payload to a Kinesis stream for real-time processing. Do not use this tool to write multiple records at once — use a batch put operation for that. Each call to this tool writes data that becomes available to stream consumers.

        Args:
            Data: 
            PartitionKey: 
            StreamName: 
        Returns:
            API response as a dictionary.
        """
        ...

    def aws_kinesis_put_resource_policy(
        self,
        Policy: Optional[str] = None,
        ResourceARN: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Creates or replaces the resource-based IAM policy on a specified AWS Kinesis resource, controlling which principals can access it and what actions they can perform. Use this tool when you need to grant or restrict cross-account or service access to a Kinesis stream. Do not use this tool to retrieve an existing policy — use aws_kinesis_get_resource_policy for that. This action will overwrite any existing resource policy on the target resource.

        Args:
            Policy: 
            ResourceARN: 
        Returns:
            API response as a dictionary.
        """
        ...

    def aws_kinesis_register_consumer(
        self,
        ConsumerName: Optional[str] = None,
        StreamARN: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Registers a new enhanced fan-out consumer for a specified AWS Kinesis data stream, enabling the consumer to receive its own dedicated read throughput via HTTP/2 streaming. Use this tool when you need to add a new application or service that will independently consume data from a Kinesis stream with dedicated bandwidth. Do not use this tool for standard (polling-based) stream consumers.

        Args:
            ConsumerName: 
            StreamARN: 
        Returns:
            API response as a dictionary.
        """
        ...

