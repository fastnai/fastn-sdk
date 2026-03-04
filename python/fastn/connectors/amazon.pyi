"""Fastn Amazon connector — auto-generated type stubs.

Do not edit manually. Regenerate with `fastn connector sync`.
"""
from __future__ import annotations

from typing import Any, Dict, List, Optional, TypedDict


class _AmazonCreateDestinationResourcespecification(TypedDict, total=False):
    sqs: Dict[str, Any]

class _AmazonCreateSubscriptionProcessingdirective(TypedDict, total=False):
    eventFilter: Dict[str, Any]

class AmazonConnector:
    """Amazon connector ().

    Provides 12 tools.
    """

    def amazon_create_destination(
        self,
        name: Optional[str] = None,
        resourceSpecification: Optional[_AmazonCreateDestinationResourcespecification] = None,
        x_amz_access_token: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Creates a new notification destination in the Amazon Selling Partner Notifications API, such as an SQS queue or EventBridge event bus, to which seller notifications can be delivered. Use this tool before creating a subscription that requires a delivery endpoint. Do not use this tool to update an existing destination — delete and recreate it instead.

        Args:
            name: 
            resourceSpecification: 
            x_amz_access_token: 
        Returns:
            API response as a dictionary.
        """
        ...

    def amazon_create_or_update_listing(
        self,
        issueLocale: str,
        marketplaceIds: str,
        sellerId: str,
        sku: str,
        attributes: Optional[Dict[str, Any]] = None,
        productType: Optional[str] = None,
        region: Optional[str] = None,
        requirements: Optional[str] = None,
        x_amz_access_token: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Creates a new Amazon product listing or fully replaces an existing listing for a specific seller and SKU using a complete set of listing attributes. Use this tool when onboarding a new product or performing a full listing replacement. For partial updates to existing listings, use amazon_partially_update_listing instead.

        Args:
            issueLocale:  (required)
            marketplaceIds:  (required)
            sellerId:  (required)
            sku:  (required)
            attributes: 
            productType: 
            region: 
            requirements: 
            x_amz_access_token: 
        Returns:
            API response as a dictionary.
        """
        ...

    def amazon_create_subscription(
        self,
        destinationId: Optional[str] = None,
        notificationType: Optional[str] = None,
        payloadVersion: Optional[str] = None,
        processingDirective: Optional[_AmazonCreateSubscriptionProcessingdirective] = None,
        region: Optional[str] = None,
        x_amz_access_token: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Creates a new Amazon Selling Partner notification subscription for a specified notification type, linking it to an existing destination so that seller events of that type are delivered there. Use this tool when you want to start receiving a particular category of Amazon notifications. Ensure the destination already exists before calling this tool. Do not use this tool to update an existing subscription — delete and recreate it instead.

        Args:
            destinationId: 
            notificationType: 
            payloadVersion: 
            processingDirective: 
            region: 
            x_amz_access_token: 
        Returns:
            API response as a dictionary.
        """
        ...

    def amazon_delete_destination(
        self,
        destinationId: Optional[str] = None,
        x_amz_access_token: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Permanently deletes a specific notification destination from the Amazon Selling Partner Notifications API by its destination ID. Use this tool when a notification endpoint is no longer needed. This action is irreversible — the destination will be removed and any subscriptions relying on it may stop receiving notifications. Do not use this tool to delete a subscription — use amazon_delete_subscription instead.

        Args:
            destinationId: 
            x_amz_access_token: 
        Returns:
            API response as a dictionary.
        """
        ...

    def amazon_delete_listing_item(
        self,
        issueLocale: str,
        marketplaceIds: str,
        sellerId: str,
        sku: str,
        region: Optional[str] = None,
        x_amz_access_token: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Permanently deletes a specific product listing item from Amazons marketplace for a given seller and SKU. Use this tool when a product should be removed from the sellers catalog. This action is irreversible — the listing will be removed from Amazons marketplace. Do not use this tool to update listing details — use amazon_partially_update_listing or amazon_create_or_update_listing instead.

        Args:
            issueLocale:  (required)
            marketplaceIds:  (required)
            sellerId:  (required)
            sku:  (required)
            region: 
            x_amz_access_token: 
        Returns:
            API response as a dictionary.
        """
        ...

    def amazon_delete_subscription(
        self,
        notificationType: str,
        subscriptionId: str,
        region: Optional[str] = None,
        x_amz_access_token: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Permanently deletes an existing Amazon Selling Partner notification subscription identified by its notification type and subscription ID. Use this tool when a subscription to a notification type is no longer required. This action is irreversible — the subscription will be removed and the associated destination will no longer receive notifications of that type. Do not use this tool to delete a destination — use amazon_delete_destination instead.

        Args:
            notificationType:  (required)
            subscriptionId:  (required)
            region: 
            x_amz_access_token: 
        Returns:
            API response as a dictionary.
        """
        ...

    def amazon_generate_token(
        self,
        client_id: Optional[str] = None,
        client_secret: Optional[str] = None,
        grant_type: Optional[str] = None,
        refresh_token: Optional[str] = None,
        scope: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Generates a new OAuth 2.0 access token from Amazons authorization service for authenticating subsequent Selling Partner API requests. Use this tool to obtain or refresh an access token before making API calls that require authorization. Do not use this tool to manage notification destinations or subscriptions.

        Args:
            client_id: 
            client_secret: 
            grant_type: 
            refresh_token: 
            scope: 
        Returns:
            API response as a dictionary.
        """
        ...

    def amazon_get_destination(
        self,
        destinationId: Optional[str] = None,
        x_amz_access_token: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Retrieves the details of a specific notification destination from the Amazon Selling Partner Notifications API by its destination ID, including its type and configuration. Use this tool when you need to inspect a single destination. Do not use this tool to list all destinations — use amazon_list_destinations instead.

        Args:
            destinationId: 
            x_amz_access_token: 
        Returns:
            API response as a dictionary.
        """
        ...

    def amazon_get_listing_item(
        self,
        includedData: Optional[str] = None,
        issueLocale: Optional[str] = None,
        marketplaceIds: Optional[str] = None,
        region: Optional[str] = None,
        sellerId: Optional[str] = None,
        sku: Optional[str] = None,
        x_amz_access_token: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Retrieves the details of a specific Amazon product listing item for a given seller and SKU, including its attributes, status, and issues. Use this tool when you need to inspect the current state of a single listing. Do not use this tool to update or delete a listing.

        Args:
            includedData: 
            issueLocale: 
            marketplaceIds: 
            region: 
            sellerId: 
            sku: 
            x_amz_access_token: 
        Returns:
            API response as a dictionary.
        """
        ...

    def amazon_get_subscription(
        self,
        notificationType: str,
        subscriptionId: str,
        region: Optional[str] = None,
        x_amz_access_token: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Retrieves the details of a specific Amazon Selling Partner notification subscription by notification type and subscription ID, including its status and destination. Use this tool when you need to inspect a single subscription record. Do not use this tool to list all subscriptions or to create or delete subscriptions.

        Args:
            notificationType:  (required)
            subscriptionId:  (required)
            region: 
            x_amz_access_token: 
        Returns:
            API response as a dictionary.
        """
        ...

    def amazon_list_destinations(
        self,
        x_amz_access_token: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Lists all available notification destinations configured in the Amazon Selling Partner Notifications API. Use this tool to retrieve a full list of destinations (e.g., SQS queues, EventBridge event buses) that can receive seller notifications. Do not use this tool to retrieve a single destination by ID — use amazon_get_destination instead.

        Args:
            x_amz_access_token: 
        Returns:
            API response as a dictionary.
        """
        ...

    def amazon_partially_update_listing(
        self,
        issueLocale: Optional[str] = None,
        marketplaceIds: Optional[str] = None,
        patches: Optional[List[Any]] = None,
        productType: Optional[str] = None,
        region: Optional[str] = None,
        sellerId: Optional[str] = None,
        sku: Optional[str] = None,
        x_amz_access_token: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Applies a partial update (PATCH) to an existing Amazon product listing for a specific seller and SKU, modifying only the fields provided in the request body. Use this tool when you need to update specific attributes of a listing without replacing the entire record. Do not use this tool for a full listing replacement — use amazon_create_or_update_listing instead.

        Args:
            issueLocale: 
            marketplaceIds: 
            patches: 
            productType: 
            region: 
            sellerId: 
            sku: 
            x_amz_access_token: 
        Returns:
            API response as a dictionary.
        """
        ...

