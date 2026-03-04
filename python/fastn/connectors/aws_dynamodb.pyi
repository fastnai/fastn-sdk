"""Fastn AWS DynamoDB connector — auto-generated type stubs.

Do not edit manually. Regenerate with `fastn connector sync`.
"""
from __future__ import annotations

from typing import Any, Dict, List, Optional, TypedDict


class AwsDynamodbConnector:
    """AWS DynamoDB connector ().

    Provides 4 tools.
    """

    def aws_dynamodb_delete_item(
        self,
        Key: Dict[str, Any],
        TableName: str,
        ConditionExpression: Optional[str] = None,
        ReturnValues: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Permanently deletes a single item from a specified AWS DynamoDB table identified by its primary key. Use this tool when you need to remove a specific record from a DynamoDB table. Do not use this tool to delete an entire table or multiple items at once. This action is irreversible — the deleted item cannot be recovered unless point-in-time recovery or backups are configured.

        Args:
            Key: The primary key of the item to be retrieved or updated. (required)
            TableName: The name of the DynamoDB table. (required)
            ConditionExpression: A condition expression to be evaluated before the item is updated.
            ReturnValues: Specifies the attributes to be returned after the operation.
        Returns:
            API response as a dictionary.
        """
        ...

    def aws_dynamodb_list_tables(
        self,
    ) -> Dict[str, Any]:
        """Retrieves a list of all DynamoDB table names available in the configured AWS account and region. Use this tool when you need to discover which tables exist before performing operations such as queries, inserts, or deletes. Do not use this tool to retrieve the contents or schema of a specific table.
        Returns:
            API response as a dictionary.
        """
        ...

    def aws_dynamodb_put_item(
        self,
        Item: Dict[str, Any],
        TableName: str,
        ConditionExpression: Optional[str] = None,
        ExpressionAttributeValues: Optional[Dict[str, Any]] = None,
    ) -> Dict[str, Any]:
        """Creates a new item or completely replaces an existing item in a specified AWS DynamoDB table. If an item with the same primary key already exists, it will be overwritten entirely. Use this tool when you need to insert a new record or fully replace an existing record. Do not use this tool when you only need to update specific attributes of an existing item — use an update operation instead. This action will overwrite existing data without warning.

        Args:
            Item: The item to be put into the DynamoDB table. (required)
            TableName: The name of the DynamoDB table. (required)
            ConditionExpression: A condition expression that specifies when the item is to be put into the table.
            ExpressionAttributeValues: Values for the condition expression.
        Returns:
            API response as a dictionary.
        """
        ...

    def aws_dynamodb_query(
        self,
        ConsistentRead: bool,
        Statement: str,
        Limit: Optional[int] = None,
        NextToken: Optional[str] = None,
        Parameters: Optional[List[Any]] = None,
        ReturnConsumedCapacity: Optional[str] = None,
        ReturnValuesOnConditionCheckFailure: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Queries a specific AWS DynamoDB table using key conditions and optional filter expressions to retrieve one or more items that share a partition key. Use this tool when you need to retrieve items from a DynamoDB table based on primary key values or index conditions. Do not use this tool for full table scans — use a scan operation for that. Do not use this tool to modify or delete data.

        Args:
            ConsistentRead: Indicates whether to perform a consistent read. (required)
            Statement: DynamoDB statement to execute. (required)
            Limit: Maximum number of items to return.
            NextToken: Token for pagination of results.
            Parameters: 
            ReturnConsumedCapacity: Indicates whether to return consumed capacity information.
            ReturnValuesOnConditionCheckFailure: Specifies whether to return values on condition check failure.
        Returns:
            API response as a dictionary.
        """
        ...

