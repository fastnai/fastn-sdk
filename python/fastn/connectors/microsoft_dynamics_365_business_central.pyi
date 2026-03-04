"""Fastn Microsoft Dynamics 365 Business Central connector — auto-generated type stubs.

Do not edit manually. Regenerate with `fastn connector sync`.
"""
from __future__ import annotations

from typing import Any, Dict, List, Optional, TypedDict


class MicrosoftDynamics365BusinessCentralConnector:
    """Microsoft Dynamics 365 Business Central connector ().

    Provides 11 tools.
    """

    def get_companies(
        self,
        tenantId: str,
    ) -> Dict[str, Any]:
        """Retrieves a list of companies from the database using the appropriate API connector, providing information on each company available in the system.

        Args:
            tenantId: Tenant ID for accessing the Microsoft Dynamics 365 Business Central instance. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def microsoft_dynamics_365_business_central_create_contact(
        self,
        companyName: str,
        country: str,
        displayName: str,
        jobTitle: str,
        postalCode: str,
        taxLiable: bool,
        tenantId: str,
        addressLine1: Optional[str] = None,
        addressLine2: Optional[str] = None,
        blocked: Optional[str] = None,
        city: Optional[str] = None,
        company: Optional[str] = None,
        companyNumber: Optional[str] = None,
        contactBusinessRelation: Optional[str] = None,
        currencyCode: Optional[str] = None,
        currencyId: Optional[str] = None,
        email: Optional[str] = None,
        id: Optional[str] = None,
        lastInteractionDate: Optional[str] = None,
        lastModifiedDateTime: Optional[str] = None,
        mobilePhoneNumber: Optional[str] = None,
        number: Optional[str] = None,
        paymentMethodId: Optional[str] = None,
        paymentTermsId: Optional[str] = None,
        phoneNumber: Optional[str] = None,
        privacyBlocked: Optional[bool] = None,
        searchName: Optional[str] = None,
        shipmentMethodId: Optional[str] = None,
        state: Optional[str] = None,
        taxAreaId: Optional[str] = None,
        taxRegistrationNumber: Optional[str] = None,
        type: Optional[str] = None,
        website: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Creates a new contact record in the Production environment of a specified Microsoft Dynamics 365 Business Central tenant. Use this tool when you need to add a new individual or organization to the Business Central contact management system, including setting their name, email, phone, and address details. Do not use this tool to update an existing contact or to list contacts (use the list contacts tool instead). This operation permanently adds a new contact and cannot be undone without explicitly deleting the created record.

        Args:
            companyName: The name of the customer's company. (required)
            country: The country of the customer. (required)
            displayName: The display name of the customer. (required)
            jobTitle: The job title of the customer contact. (required)
            postalCode: The postal code of the customer's address. (required)
            taxLiable: Indicates whether the customer is tax liable. (required)
            tenantId: The ID of the tenant. (required)
            addressLine1: The first line of the customer's address.
            addressLine2: The second line of the customer's address.
            blocked: The blocked status of the customer.
            city: The city of the customer.
            company: The name of the company.
            companyNumber: The company number.
            contactBusinessRelation: The business relation of the contact.
            currencyCode: The currency code.
            currencyId: The ID of the currency.
            email: The email address of the customer.
            id: The unique identifier of the customer.
            lastInteractionDate: The date of the last interaction with the customer.
            lastModifiedDateTime: The last time the customer record was modified.
            mobilePhoneNumber: The mobile phone number of the customer.
            number: The customer number.
            paymentMethodId: The ID of the payment method.
            paymentTermsId: The ID of the payment terms.
            phoneNumber: The phone number of the customer.
            privacyBlocked: Indicates whether the customer's privacy is blocked.
            searchName: The search name for the customer.
            shipmentMethodId: The ID of the shipment method.
            state: The state or province of the customer's address.
            taxAreaId: The ID of the tax area.
            taxRegistrationNumber: The tax registration number of the customer.
            type: The type of customer.
            website: The website of the customer.
        Returns:
            API response as a dictionary.
        """
        ...

    def microsoft_dynamics_365_business_central_create_item(
        self,
        companyId: str,
        displayName: str,
        environment: str,
        number: str,
        blocked: Optional[bool] = None,
        tenantId: Optional[str] = None,
        type: Optional[str] = None,
        unitPrice: Optional[int] = None,
    ) -> Dict[str, Any]:
        """Creates a new item record in Microsoft Dynamics 365 Business Central under the specified company. Use this tool when you need to add a new product or inventory item to Business Central, including setting its description, type, unit price, and base unit of measure. Do not use this tool to update an existing item (use the update item tool instead) or to retrieve items (use the list items tool instead). This operation permanently adds a new item to the companys item catalog and cannot be undone without explicitly deleting the created record.

        Args:
            companyId: Identifier of the target Business Central company (company id) for the API call. (required)
            displayName: Human-readable name or title for the record shown in Business Central. (required)
            environment: Business Central environment name (for example, Production or Sandbox) to target. (required)
            number: Unique identifier or code for the record (for example, the item or resource number). (required)
            blocked: Indicates whether the record is blocked (true) or not (false).
            tenantId: Azure AD tenant identifier associated with the Business Central instance.
            type: Type or category of the record as expected by the Business Central endpoint.
            unitPrice: Unit price for the item or record (integer as required by the API).
        Returns:
            API response as a dictionary.
        """
        ...

    def microsoft_dynamics_365_business_central_create_journal(
        self,
        code: str,
        companyId: str,
        displayName: str,
        tenantId: str,
    ) -> Dict[str, Any]:
        """Creates a new journal in the production environment for a specified company in Microsoft Dynamics 365 Business Central. Use this tool when you need to add a new general journal batch to Business Central for recording financial transactions. Do not use this tool to add journal lines to an existing journal, or to retrieve journals (use the list journals tool instead). This operation permanently creates a new journal record and cannot be undone without explicitly deleting the created record.

        Args:
            code: Code related to the request body. (required)
            companyId: Company ID for the request. (required)
            displayName: Display name related to the request body. (required)
            tenantId: Tenant ID for the request. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def microsoft_dynamics_365_business_central_generate_token(
        self,
        client_id: str,
        password: str,
        scope: str,
        tenentId: str,
        username: str,
    ) -> Dict[str, Any]:
        """Generates an OAuth 2.0 authentication token from the Microsoft identity platform for accessing secured Microsoft Dynamics 365 Business Central API endpoints. Use this tool when an access token is required before calling other Business Central tools, or when a previously issued token has expired. Do not use this tool if a valid token is already available, as generating unnecessary tokens may consume rate limits. Note: the endpoint contains a typo in the tenant ID parameter (tenentId); verify your tenant ID is correctly passed. This operation exchanges client credentials or authorization codes for a bearer token; store the resulting token securely and do not expose it in logs.

        Args:
            client_id: Client ID for Microsoft Dynamics 365 Business Central authentication. (required)
            password: Password for Microsoft Dynamics 365 Business Central authentication. (required)
            scope: Scope of access for the Microsoft Dynamics 365 Business Central request. (required)
            tenentId: Tenant ID for the Microsoft Dynamics 365 Business Central request URL. (required)
            username: Username for Microsoft Dynamics 365 Business Central authentication. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def microsoft_dynamics_365_business_central_list_companies(
        self,
        count: Optional[str] = None,
        environment: Optional[str] = None,
        filter: Optional[str] = None,
        orderby: Optional[str] = None,
        select: Optional[str] = None,
        skip: Optional[str] = None,
        tenantId: Optional[str] = None,
        top: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Retrieves a list of all companies available to the authenticated user within a Microsoft Dynamics 365 Business Central tenant. Use this tool when you need to discover company IDs required by other tools (such as list items, list journals, or create contact) or when you need to audit the companies registered in the tenant. Do not use this tool to retrieve detailed financials or settings for a specific company. This is a read-only operation with no side effects.

        Args:
            count: 
            environment: 
            filter: 
            orderby: 
            select: 
            skip: 
            tenantId: 
            top: 
        Returns:
            API response as a dictionary.
        """
        ...

    def microsoft_dynamics_365_business_central_list_contacts(
        self,
        tenantId: str,
        company: Optional[str] = None,
        filter: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Retrieves a list of all contact records from the Production environment of a specified Microsoft Dynamics 365 Business Central tenant. Use this tool when you need to browse or audit contacts, or when you need contact IDs for use with other tools. Do not use this tool to create new contacts (use the create contact tool instead) or to retrieve contacts from non-Production environments. This is a read-only operation with no side effects.

        Args:
            tenantId: The ID of the tenant for Microsoft Dynamics 365 Business Central. (required)
            company: The company ID or name.
            filter: Filter criteria for the request.
        Returns:
            API response as a dictionary.
        """
        ...

    def microsoft_dynamics_365_business_central_list_environments(
        self,
    ) -> Dict[str, Any]:
        """Retrieves a list of all environments (e.g., production and sandbox) available in Microsoft Dynamics 365 Business Central for the authenticated tenant. Use this tool when you need to discover environment names required by other tools or when you need to determine which environments exist before performing environment-specific operations. Do not use this tool to manage or modify environments. This is a read-only operation with no side effects.
        Returns:
            API response as a dictionary.
        """
        ...

    def microsoft_dynamics_365_business_central_list_items(
        self,
        companyId: str,
        environment: str,
        tenantId: str,
        count: Optional[str] = None,
        filter: Optional[str] = None,
        orderby: Optional[str] = None,
        select: Optional[str] = None,
        skip: Optional[str] = None,
        top: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Retrieves a list of all item records for a specified company in Microsoft Dynamics 365 Business Central. Use this tool when you need to browse, search, or audit inventory items, or when you need item IDs for use with other tools such as update item. Do not use this tool to retrieve a single item by ID or to modify item records. Returns item details including number, display name, type, unit price, and base unit of measure. This is a read-only operation with no side effects.

        Args:
            companyId: The identifier or name of the company (companyId) within Business Central to target. (required)
            environment: The Business Central environment (for example, Production or Sandbox) used in the API URL. (required)
            tenantId: The Azure Active Directory tenant ID associated with the Business Central instance. (required)
            count: OData $count flag to include a count of matching resources in the response.
            filter: OData $filter expression to filter the returned results.
            orderby: OData $orderby expression to sort the returned results.
            select: OData $select expression to specify which fields to include in the response.
            skip: OData $skip value to skip a specified number of items in the result set.
            top: OData $top value to limit the number of items returned.
        Returns:
            API response as a dictionary.
        """
        ...

    def microsoft_dynamics_365_business_central_list_journals(
        self,
        companyId: str,
        tenantId: str,
    ) -> Dict[str, Any]:
        """Retrieves a list of all journal records for a specified company in the production environment of Microsoft Dynamics 365 Business Central. Use this tool when you need to browse or audit journal batches, or when you need journal IDs for use with other tools. Do not use this tool to create new journals (use the create journal tool instead) or to retrieve individual journal lines. Note: the endpoint contains a typo in the tenant ID parameter (tenanId); verify your tenant ID is correctly passed. This is a read-only operation with no side effects.

        Args:
            companyId: ID of the company. (required)
            tenantId: Tenant ID. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def microsoft_dynamics_365_business_central_update_item(
        self,
        companyId: str,
        itemId: str,
        IfMatch: Optional[str] = None,
        Inventory: Optional[int] = None,
        _odata_etag: Optional[str] = None,
        baseUnitOfMeasureCode: Optional[str] = None,
        displayName: Optional[str] = None,
        env: Optional[str] = None,
        generalProductPostingGroupCode: Optional[str] = None,
        inventoryPostingGroupId: Optional[str] = None,
        tenantId: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Updates an existing item record in Microsoft Dynamics 365 Business Central. Use this tool when you need to modify item properties such as description, unit price, base unit of measure, or inventory policy for a specific item identified by its item ID. Do not use this tool to create new items (use the create item tool instead) or to retrieve item details (use the list items tool instead). This operation overwrites only the fields provided in the request; other fields remain unchanged. Changes are applied immediately and are not reversible without a subsequent update.

        Args:
            companyId: Identifier of the company in Business Central to target the request to. (required)
            itemId: Unique identifier of the item resource (used in the URL path). (required)
            IfMatch: ETag value used for conditional requests to ensure the resource has not changed (concurrency control).
            Inventory: Current inventory quantity for the item.
            _odata_etag: The OData ETag for the item resource, used for concurrency control when updating the resource.
            baseUnitOfMeasureCode: Code representing the base unit of measure assigned to the item.
            displayName: The human-readable name of the item.
            env: Business Central environment (for example, Production or Sandbox) to target.
            generalProductPostingGroupCode: Code of the general product posting group used for general ledger postings.
            inventoryPostingGroupId: Identifier of the inventory posting group applied to the item for inventory accounting.
            tenantId: Azure Active Directory tenant identifier associated with the Business Central tenant.
        Returns:
            API response as a dictionary.
        """
        ...

