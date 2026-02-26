"""Fastn AWS DynamoDB connector — auto-generated type stubs.

Do not edit manually. Regenerate with `fastn connector sync`.
"""
from __future__ import annotations

from typing import Any, Dict, List, Optional


class AwsDynamodbConnector:
    """AWS DynamoDB connector ().

    Provides 4 tools.
    """

    def delete_item(
        self,
        Key: Dict[str, Any],
        TableName: str,
        ConditionExpression: Optional[str] = None,
        ReturnValues: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Removes an item from the specified database connector.

        Args:
            Key: The primary key of the item to be retrieved or updated. (required)
            TableName: The name of the DynamoDB table. (required)
            ConditionExpression: A condition expression to be evaluated before the item is updated.
            ReturnValues: Specifies the attributes to be returned after the operation.
        Returns:
            API response as a dictionary.
        """
        ...

    def get_tables(
        self,
    ) -> Dict[str, Any]:
        """Retrieves the list of tables available in the specified database connector.
        Returns:
            API response as a dictionary.
        """
        ...

    def put_item(
        self,
        Item: Dict[str, Any],
        TableName: str,
        ConditionExpression: Optional[str] = None,
        ExpressionAttributeValues: Optional[Dict[str, Any]] = None,
    ) -> Dict[str, Any]:
        """Adds or updates an item in the specified database connector.

        Args:
            Item: The item to be put into the DynamoDB table. (required)
            TableName: The name of the DynamoDB table. (required)
            ConditionExpression: A condition expression that specifies when the item is to be put into the table.
            ExpressionAttributeValues: Values for the condition expression.
        Returns:
            API response as a dictionary.
        """
        ...

    def query(
        self,
        ConsistentRead: bool,
        Statement: str,
        Limit: Optional[int] = None,
        NextToken: Optional[str] = None,
        Parameters: Optional[List[Any]] = None,
        ReturnConsumedCapacity: Optional[str] = None,
        ReturnValuesOnConditionCheckFailure: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Executes a database query to retrieve data from the specified connector.

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

