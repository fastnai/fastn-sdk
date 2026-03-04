"""Fastn Acumatica connector — auto-generated type stubs.

Do not edit manually. Regenerate with `fastn connector sync`.
"""
from __future__ import annotations

from typing import Any, Dict, List, Optional, TypedDict


class _AcumaticaCreateContactAddress(TypedDict, total=False):
    AddressLine1: Dict[str, Any]
    City: Dict[str, Any]
    Country: Dict[str, Any]
    PostalCode: Dict[str, Any]
    State: Dict[str, Any]

class _AcumaticaCreateContactCompanyname(TypedDict, total=False):
    value: str

class _AcumaticaCreateContactEmail(TypedDict, total=False):
    value: str

class _AcumaticaCreateContactFirstname(TypedDict, total=False):
    value: str

class _AcumaticaCreateContactLastname(TypedDict, total=False):
    value: str

class _AcumaticaCreateLeadAddress(TypedDict, total=False):
    AddressLine1: Dict[str, Any]
    City: Dict[str, Any]
    Country: Dict[str, Any]
    PostalCode: Dict[str, Any]
    State: Dict[str, Any]

class _AcumaticaCreateLeadClassid(TypedDict, total=False):
    value: str

class _AcumaticaCreateLeadCompanyname(TypedDict, total=False):
    value: str

class _AcumaticaCreateLeadEmail(TypedDict, total=False):
    value: str

class _AcumaticaCreateLeadFirstname(TypedDict, total=False):
    value: str

class _AcumaticaCreateLeadLastname(TypedDict, total=False):
    value: str

class _AcumaticaCreateLeadStatus(TypedDict, total=False):
    value: str

class _AcumaticaCreateOpportunityBusinessaccount(TypedDict, total=False):
    value: str

class _AcumaticaCreateOpportunityClassid(TypedDict, total=False):
    value: str

class _AcumaticaCreateOpportunityClosedate(TypedDict, total=False):
    value: str

class _AcumaticaCreateOpportunityDetails(TypedDict, total=False):
    value: str

class _AcumaticaCreateOpportunityOpportunityid(TypedDict, total=False):
    value: str

class _AcumaticaCreateOpportunityOwner(TypedDict, total=False):
    value: str

class _AcumaticaCreateOpportunityStage(TypedDict, total=False):
    value: str

class _AcumaticaCreateOpportunitySubject(TypedDict, total=False):
    value: str

class _AcumaticaCreateSalesOrderCustomerid(TypedDict, total=False):
    value: str

class _AcumaticaCreateSalesOrderDescription(TypedDict, total=False):
    value: str

class _AcumaticaCreateSalesOrderOrdertype(TypedDict, total=False):
    value: str

class _AcumaticaCreateSalesOrderLocationid(TypedDict, total=False):
    value: str

class _AcumaticaCreateStockItemBaseuom(TypedDict, total=False):
    value: str

class _AcumaticaCreateStockItemDefaultwarehouse(TypedDict, total=False):
    value: str

class _AcumaticaCreateStockItemDescription(TypedDict, total=False):
    value: str

class _AcumaticaCreateStockItemInventoryid(TypedDict, total=False):
    value: str

class _AcumaticaCreateStockItemItemclass(TypedDict, total=False):
    value: str

class _AcumaticaCreateStockItemPostingclass(TypedDict, total=False):
    value: str

class _AcumaticaCreateStockItemPriceclassid(TypedDict, total=False):
    value: str

class _AcumaticaCreateStockItemProductmanager(TypedDict, total=False):
    value: str

class _AcumaticaCreateStockItemPurchaseunit(TypedDict, total=False):
    value: str

class _AcumaticaCreateStockItemSalesunit(TypedDict, total=False):
    value: str

class _AcumaticaCreateStockItemTaxcategory(TypedDict, total=False):
    value: str

class AcumaticaConnector:
    """Acumatica connector ().

    Provides 28 tools.
    """

    def acumatica_create_contact(
        self,
        Address: Optional[_AcumaticaCreateContactAddress] = None,
        CompanyName: Optional[_AcumaticaCreateContactCompanyname] = None,
        Email: Optional[_AcumaticaCreateContactEmail] = None,
        FirstName: Optional[_AcumaticaCreateContactFirstname] = None,
        LastName: Optional[_AcumaticaCreateContactLastname] = None,
    ) -> Dict[str, Any]:
        """Creates a new contact record in the Acumatica CRM system. Use this when a new individual needs to be added as a contact. This call creates a persistent record in Acumatica. Do not use this to update an existing contact — use an update tool instead. Note: the endpoint uses HTTP PUT, which is Acumaticas standard method for both create and upsert operations.

        Args:
            Address: Address details of the contact.
            CompanyName: Name of the company.
            Email: Email address of the contact.
            FirstName: First name of the contact.
            LastName: Last name of the contact.
        Returns:
            API response as a dictionary.
        """
        ...

    def acumatica_create_lead(
        self,
        Address: Optional[_AcumaticaCreateLeadAddress] = None,
        ClassID: Optional[_AcumaticaCreateLeadClassid] = None,
        CompanyName: Optional[_AcumaticaCreateLeadCompanyname] = None,
        Email: Optional[_AcumaticaCreateLeadEmail] = None,
        FirstName: Optional[_AcumaticaCreateLeadFirstname] = None,
        LastName: Optional[_AcumaticaCreateLeadLastname] = None,
        Status: Optional[_AcumaticaCreateLeadStatus] = None,
    ) -> Dict[str, Any]:
        """Creates a new lead record in the Acumatica sales management system. Use this when a new prospect or inquiry needs to be tracked as a lead. This call creates a persistent record in Acumatica. Do not use this to update an existing lead — use an update tool instead. Note: the endpoint uses HTTP PUT, which is Acumaticas standard method for both create and upsert operations.

        Args:
            Address: Address of the contact.
            ClassID: Class ID of the contact.
            CompanyName: Name of the company associated with the contact.
            Email: Email address of the contact.
            FirstName: First name of the contact.
            LastName: Last name of the contact.
            Status: Status of the contact.
        Returns:
            API response as a dictionary.
        """
        ...

    def acumatica_create_opportunity(
        self,
        BusinessAccount: Optional[_AcumaticaCreateOpportunityBusinessaccount] = None,
        ClassID: Optional[_AcumaticaCreateOpportunityClassid] = None,
        CloseDate: Optional[_AcumaticaCreateOpportunityClosedate] = None,
        Details: Optional[_AcumaticaCreateOpportunityDetails] = None,
        OpportunityID: Optional[_AcumaticaCreateOpportunityOpportunityid] = None,
        Owner: Optional[_AcumaticaCreateOpportunityOwner] = None,
        Stage: Optional[_AcumaticaCreateOpportunityStage] = None,
        Subject: Optional[_AcumaticaCreateOpportunitySubject] = None,
    ) -> Dict[str, Any]:
        """Creates a new opportunity record in the Acumatica sales pipeline. Use this when a new sales opportunity needs to be tracked. This call creates a persistent record in Acumatica. Do not use this to update an existing opportunity — use an update tool instead. Note: the endpoint uses HTTP PUT, which is Acumaticas standard method for both create and upsert operations.

        Args:
            BusinessAccount: Business Account associated with the opportunity in AcumaticaWhole.
            ClassID: Class ID associated with the opportunity in AcumaticaWhole.
            CloseDate: Close date of the opportunity in AcumaticaWhole.
            Details: Details of the opportunity in AcumaticaWhole.
            OpportunityID: Opportunity ID in AcumaticaWhole.
            Owner: Owner of the opportunity in AcumaticaWhole.
            Stage: Stage of the opportunity in AcumaticaWhole.
            Subject: Subject of the opportunity in AcumaticaWhole.
        Returns:
            API response as a dictionary.
        """
        ...

    def acumatica_create_sales_order(
        self,
        CustomerID: _AcumaticaCreateSalesOrderCustomerid,
        Description: _AcumaticaCreateSalesOrderDescription,
        OrderType: _AcumaticaCreateSalesOrderOrdertype,
        Details: Optional[List[Any]] = None,
        LocationID: Optional[_AcumaticaCreateSalesOrderLocationid] = None,
        expand: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Creates a new sales order record in the Acumatica sales management system. Use this when a new customer order needs to be placed and tracked. This call creates a persistent record in Acumatica. Do not use this to update an existing sales order — use an update tool instead. Note: the endpoint uses HTTP PUT, which is Acumaticas standard method for both create and upsert operations.

        Args:
            CustomerID: Identifier for the customer. (required)
            Description: Description of the order or transaction. (required)
            OrderType: Type of order. (required)
            Details: 
            LocationID: Identifier for the location.
            expand: Specifies fields to expand in the response.
        Returns:
            API response as a dictionary.
        """
        ...

    def acumatica_create_stock_item(
        self,
        BaseUOM: Optional[_AcumaticaCreateStockItemBaseuom] = None,
        DefaultWarehouse: Optional[_AcumaticaCreateStockItemDefaultwarehouse] = None,
        Description: Optional[_AcumaticaCreateStockItemDescription] = None,
        InventoryID: Optional[_AcumaticaCreateStockItemInventoryid] = None,
        ItemClass: Optional[_AcumaticaCreateStockItemItemclass] = None,
        PostingClass: Optional[_AcumaticaCreateStockItemPostingclass] = None,
        PriceClassID: Optional[_AcumaticaCreateStockItemPriceclassid] = None,
        ProductManager: Optional[_AcumaticaCreateStockItemProductmanager] = None,
        PurchaseUnit: Optional[_AcumaticaCreateStockItemPurchaseunit] = None,
        SalesUnit: Optional[_AcumaticaCreateStockItemSalesunit] = None,
        TaxCategory: Optional[_AcumaticaCreateStockItemTaxcategory] = None,
    ) -> Dict[str, Any]:
        """Creates a new stock item record in the Acumatica inventory management system. Use this when a new physical product or inventory item needs to be tracked. This call creates a persistent record in Acumatica. Do not use this to update an existing stock item — use an update tool instead. Note: the endpoint uses HTTP PUT, which is Acumaticas standard method for both create and upsert operations.

        Args:
            BaseUOM: The base unit of measure for the inventory item.
            DefaultWarehouse: The default warehouse for the inventory item.
            Description: A description of the inventory item.
            InventoryID: The unique identifier for the inventory item.
            ItemClass: The class of the inventory item.
            PostingClass: The posting class for the inventory item.
            PriceClassID: The ID of the price class for the inventory item.
            ProductManager: The product manager responsible for the inventory item.
            PurchaseUnit: The unit of measure used for purchases.
            SalesUnit: The unit of measure used for sales.
            TaxCategory: The tax category for the inventory item.
        Returns:
            API response as a dictionary.
        """
        ...

    def acumatica_delete_contact(
        self,
        contactId: str,
    ) -> Dict[str, Any]:
        """Permanently deletes a single contact from the Acumatica CRM system by its contact ID. This action is irreversible — the contact record will be removed. Use this only when the contact must be fully deleted. Do not use this to deactivate or update a contact — update its record instead.

        Args:
            contactId: ID of the contact. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def acumatica_delete_lead(
        self,
        leadId: str,
    ) -> Dict[str, Any]:
        """Permanently deletes a single lead from the Acumatica sales management system by its lead ID. This action is irreversible — the lead record will be removed from the system. Use this only when the lead must be fully deleted. Do not use this to disqualify or update a leads status — update its record instead.

        Args:
            leadId: The ID of the lead. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def acumatica_delete_opportunity(
        self,
        opportunityId: str,
    ) -> Dict[str, Any]:
        """Permanently deletes a single opportunity from the Acumatica sales pipeline by its opportunity ID. This action is irreversible — the opportunity record and all associated data will be removed. Use this only when you are certain the opportunity must be deleted. Do not use this to close or lose an opportunity — update its stage instead.

        Args:
            opportunityId: ID of the opportunity. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def acumatica_delete_sales_order(
        self,
        orderNumber: str,
        orderType: str,
    ) -> Dict[str, Any]:
        """Permanently deletes a single sales order from the Acumatica sales management system, identified by its order type and order number. This action is irreversible — the sales order record will be removed. Use this only when the order must be fully deleted. Do not use this to cancel an order — update its status instead.

        Args:
            orderNumber: The unique identifier for the order in Accumatica. (required)
            orderType: The type of order (e.g., sales order, purchase order). (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def acumatica_delete_stock_item(
        self,
        stockItemId: str,
    ) -> Dict[str, Any]:
        """Permanently deletes a single stock item from the Acumatica inventory management system by its stock item ID. This action is irreversible — the item record will be removed from inventory. Use this only when the stock item must be fully deleted. Do not use this to deactivate or discontinue an item — update its status instead.

        Args:
            stockItemId: The ID of the stock item. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def acumatica_generate_token(
        self,
        client_id: str,
        client_secret: str,
        instanceUrl: str,
        password: str,
        username: str,
    ) -> Dict[str, Any]:
        """Generates a new OAuth authentication token for secure API access to the Acumatica instance using the identity server. Use this to obtain a bearer token before making authenticated API calls. This call does not log in a session — it issues a token via the OAuth client credentials or password flow. Do not confuse this with acumatica_login, which creates a cookie-based session.

        Args:
            client_id:  (required)
            client_secret:  (required)
            instanceUrl:  (required)
            password:  (required)
            username:  (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def acumatica_get_contact(
        self,
        contactId: str,
    ) -> Dict[str, Any]:
        """Retrieves full details for a single Acumatica contact identified by its contact ID, including name, email, phone, and linked accounts. Use this when you need complete information about one specific contact. Do not use this to browse multiple contacts — use acumatica_list_contacts instead.

        Args:
            contactId: The ID of the contact. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def acumatica_get_lead(
        self,
        leadId: str,
    ) -> Dict[str, Any]:
        """Retrieves full details for a single Acumatica lead identified by its lead ID, including contact information, status, and assigned owner. Use this when you need complete information about one specific lead. Do not use this to browse multiple leads — use acumatica_list_leads instead.

        Args:
            leadId: The ID of the lead. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def acumatica_get_opportunity(
        self,
        opportunityId: str,
    ) -> Dict[str, Any]:
        """Retrieves full details for a single Acumatica opportunity identified by its opportunity ID, including stage, owner, estimated close date, and associated contacts. Use this when you need complete information about one specific opportunity. Do not use this to browse multiple opportunities — use acumatica_list_opportunities instead.

        Args:
            opportunityId: The ID of the opportunity. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def acumatica_get_sales_order(
        self,
        orderId: str,
        expand: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Retrieves full details for a single Acumatica sales order identified by its order ID, including line items, pricing, shipping details, and status. Use this when you need complete information about one specific sales order. Do not use this to browse multiple orders — use acumatica_list_sales_orders instead.

        Args:
            orderId:  (required)
            expand: 
        Returns:
            API response as a dictionary.
        """
        ...

    def acumatica_get_stock_item(
        self,
        stockItemId: str,
    ) -> Dict[str, Any]:
        """Retrieves full details for a single Acumatica stock item identified by its stock item ID, including description, pricing, unit of measure, and inventory settings. Use this when you need complete information about one specific stock item. Do not use this to browse multiple items — use acumatica_list_stock_items instead.

        Args:
            stockItemId: The ID of the stock item. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def acumatica_list_contacts(
        self,
        expand: Optional[str] = None,
        filter: Optional[str] = None,
        inlinecount: Optional[str] = None,
        orderby: Optional[str] = None,
        select: Optional[str] = None,
        skip: Optional[str] = None,
        top: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Returns a list of all contact records in the Acumatica CRM system. Use this to browse or enumerate contacts across the organization. Do not use this when you already have a contact ID and need full details — use acumatica_get_contact instead.

        Args:
            expand: 
            filter: 
            inlinecount: 
            orderby: 
            select: 
            skip: 
            top: 
        Returns:
            API response as a dictionary.
        """
        ...

    def acumatica_list_customers(
        self,
        expand: Optional[str] = None,
        filter: Optional[str] = None,
        inlinecount: Optional[str] = None,
        orderby: Optional[str] = None,
        select: Optional[str] = None,
        skip: Optional[str] = None,
        top: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Returns a list of all customer records in the Acumatica system, including account names, IDs, and billing details. Use this to browse or enumerate customers. Do not use this to retrieve a single customers full profile — use a dedicated get_customer tool if available.

        Args:
            expand: 
            filter: 
            inlinecount: 
            orderby: 
            select: 
            skip: 
            top: 
        Returns:
            API response as a dictionary.
        """
        ...

    def acumatica_list_entities(
        self,
        expand: Optional[str] = None,
        filter: Optional[str] = None,
        inlinecount: Optional[str] = None,
        orderby: Optional[str] = None,
        select: Optional[str] = None,
        skip: Optional[str] = None,
        top: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Returns a list of all top-level API entity endpoints available in this Acumatica instance. Use this to discover which entity types (e.g., Customer, Lead, SalesOrder) are accessible via the API. Do not use this to retrieve records within a specific entity — use the dedicated list tool for that entity instead.

        Args:
            expand: 
            filter: 
            inlinecount: 
            orderby: 
            select: 
            skip: 
            top: 
        Returns:
            API response as a dictionary.
        """
        ...

    def acumatica_list_leads(
        self,
        expand: Optional[str] = None,
        filter: Optional[str] = None,
        orderby: Optional[str] = None,
        select: Optional[str] = None,
        skip: Optional[str] = None,
        top: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Returns a list of all leads stored in the Acumatica sales management system. Use this to browse or enumerate leads across the system. Do not use this when you already have a lead ID and need its full details — use acumatica_get_lead instead.

        Args:
            expand: 
            filter: 
            orderby: 
            select: 
            skip: 
            top: 
        Returns:
            API response as a dictionary.
        """
        ...

    def acumatica_list_opportunities(
        self,
        expand: Optional[str] = None,
        filter: Optional[str] = None,
        orderby: Optional[str] = None,
        select: Optional[str] = None,
        skip: Optional[str] = None,
        top: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Returns a list of all opportunities currently in the Acumatica sales pipeline. Use this to browse, filter, or enumerate opportunities across the system. Do not use this when you already have an opportunity ID and need its full details — use acumatica_get_opportunity instead.

        Args:
            expand: 
            filter: 
            orderby: 
            select: 
            skip: 
            top: 
        Returns:
            API response as a dictionary.
        """
        ...

    def acumatica_list_records(
        self,
        tableName: str,
        expand: Optional[str] = None,
        filter: Optional[str] = None,
        orderby: Optional[str] = None,
        select: Optional[str] = None,
        skip: Optional[str] = None,
        top: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Returns records from a specified OData table in the Acumatica database, identified by table name. Use this for flexible, direct OData queries against a named table when no dedicated entity tool exists. Do not use this when a purpose-specific tool is available (e.g., acumatica_list_customers). Use acumatica_list_tables to discover available table names.

        Args:
            tableName:  (required)
            expand: 
            filter: 
            orderby: 
            select: 
            skip: 
            top: 
        Returns:
            API response as a dictionary.
        """
        ...

    def acumatica_list_sales_orders(
        self,
        skip: Optional[str] = None,
        top: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Returns a list of all sales orders in the Acumatica sales management system, including order numbers, types, and statuses. Use this to browse or enumerate sales orders. Do not use this when you already have an order ID and need its full details — use acumatica_get_sales_order instead.

        Args:
            skip: 
            top: 
        Returns:
            API response as a dictionary.
        """
        ...

    def acumatica_list_stock_items(
        self,
        expand: Optional[str] = None,
        select: Optional[str] = None,
        skip: Optional[str] = None,
        top: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Returns a list of all stock items in the Acumatica inventory management system, including item IDs, descriptions, and unit of measure. Use this to browse or enumerate inventory items. Do not use this when you already have a stock item ID and need its full details — use acumatica_get_stock_item instead.

        Args:
            expand: 
            select: 
            skip: 
            top: 
        Returns:
            API response as a dictionary.
        """
        ...

    def acumatica_list_table_metadata(
        self,
    ) -> Dict[str, Any]:
        """Returns OData metadata for all tables in the Acumatica instance, including column names, data types, and key fields. Use this to understand the schema of available tables before querying them. Do not use this to retrieve actual data records — use acumatica_list_records instead.
        Returns:
            API response as a dictionary.
        """
        ...

    def acumatica_list_tables(
        self,
    ) -> Dict[str, Any]:
        """Returns a list of all OData-accessible tables available in the Acumatica instance. Use this to discover which tables can be queried via acumatica_list_records. Do not use this to retrieve records or schema details — use acumatica_list_records or acumatica_list_table_metadata instead.
        Returns:
            API response as a dictionary.
        """
        ...

    def acumatica_login(
        self,
        instanceUrl: Optional[str] = None,
        name: Optional[str] = None,
        password: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Authenticates a user against the Acumatica instance and establishes a cookie-based session for subsequent API calls. Use this before making API requests that require session-based authentication. Always call acumatica_logout when done to terminate the session. Do not use this for OAuth token-based authentication — use acumatica_generate_token instead.

        Args:
            instanceUrl: 
            name: 
            password: 
        Returns:
            API response as a dictionary.
        """
        ...

    def acumatica_logout(
        self,
    ) -> Dict[str, Any]:
        """Terminates the current user session in Acumatica, invalidating the active session cookie. Use this after completing operations to securely end the session. This action affects only cookie-based sessions established via acumatica_login — it does not revoke OAuth tokens generated by acumatica_generate_token.
        Returns:
            API response as a dictionary.
        """
        ...

