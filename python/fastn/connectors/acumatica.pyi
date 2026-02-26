"""Fastn Acumatica connector — auto-generated type stubs.

Do not edit manually. Regenerate with `fastn connector sync`.
"""
from __future__ import annotations

from typing import Any, Dict, List, Optional


class AcumaticaConnector:
    """Acumatica connector ().

    Provides 28 tools.
    """

    def create_contact(
        self,
        Address: Optional[Dict[str, Any]] = None,
        CompanyName: Optional[Dict[str, Any]] = None,
        Email: Optional[Dict[str, Any]] = None,
        FirstName: Optional[Dict[str, Any]] = None,
        LastName: Optional[Dict[str, Any]] = None,
    ) -> Dict[str, Any]:
        """Creates a new contact in the customer relationship management system.

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

    def create_lead(
        self,
        Address: Optional[Dict[str, Any]] = None,
        ClassID: Optional[Dict[str, Any]] = None,
        CompanyName: Optional[Dict[str, Any]] = None,
        Email: Optional[Dict[str, Any]] = None,
        FirstName: Optional[Dict[str, Any]] = None,
        LastName: Optional[Dict[str, Any]] = None,
        Status: Optional[Dict[str, Any]] = None,
    ) -> Dict[str, Any]:
        """Creates a new lead in the sales management system.

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

    def create_opportunity(
        self,
        BusinessAccount: Optional[Dict[str, Any]] = None,
        ClassID: Optional[Dict[str, Any]] = None,
        CloseDate: Optional[Dict[str, Any]] = None,
        Details: Optional[Dict[str, Any]] = None,
        OpportunityID: Optional[Dict[str, Any]] = None,
        Owner: Optional[Dict[str, Any]] = None,
        Stage: Optional[Dict[str, Any]] = None,
        Subject: Optional[Dict[str, Any]] = None,
    ) -> Dict[str, Any]:
        """Creates a new opportunity in the sales management pipeline.

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

    def create_sales_order(
        self,
        expand: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Creates a new sales order in the sales management system.

        Args:
            expand: Specifies fields to expand in the response.
        Returns:
            API response as a dictionary.
        """
        ...

    def create_stock_item(
        self,
        BaseUOM: Optional[Dict[str, Any]] = None,
        DefaultWarehouse: Optional[Dict[str, Any]] = None,
        Description: Optional[Dict[str, Any]] = None,
        InventoryID: Optional[Dict[str, Any]] = None,
        ItemClass: Optional[Dict[str, Any]] = None,
        PostingClass: Optional[Dict[str, Any]] = None,
        PriceClassID: Optional[Dict[str, Any]] = None,
        ProductManager: Optional[Dict[str, Any]] = None,
        PurchaseUnit: Optional[Dict[str, Any]] = None,
        SalesUnit: Optional[Dict[str, Any]] = None,
        TaxCategory: Optional[Dict[str, Any]] = None,
    ) -> Dict[str, Any]:
        """Creates a new stock item in the inventory management system.

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

    def delete_contact(
        self,
        contactId: str,
    ) -> Dict[str, Any]:
        """Deletes an existing contact from the customer relationship management system.

        Args:
            contactId: ID of the contact. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def delete_lead(
        self,
        leadId: str,
    ) -> Dict[str, Any]:
        """Deletes a lead from the sales management system.

        Args:
            leadId: The ID of the lead. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def delete_opportunity(
        self,
        opportunityId: str,
    ) -> Dict[str, Any]:
        """Deletes an opportunity from the sales management pipeline.

        Args:
            opportunityId: ID of the opportunity. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def delete_sales_order(
        self,
        orderNumber: str,
        orderType: str,
    ) -> Dict[str, Any]:
        """Deletes an existing sales order from the sales management system.

        Args:
            orderNumber: The unique identifier for the order in Accumatica. (required)
            orderType: The type of order (e.g., sales order, purchase order). (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def delete_stock_item(
        self,
        stockItemId: str,
    ) -> Dict[str, Any]:
        """Deletes a stock item from the inventory management system.

        Args:
            stockItemId: The ID of the stock item. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def generate_token(
        self,
        client_id: str,
        client_secret: str,
        password: str,
        username: str,
    ) -> Dict[str, Any]:
        """Generates a new authentication token for secure API access.

        Args:
            client_id:  (required)
            client_secret:  (required)
            password:  (required)
            username:  (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def get_contact(
        self,
        contactId: str,
    ) -> Dict[str, Any]:
        """Retrieves detailed information for a specific contact.

        Args:
            contactId: The ID of the contact. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def get_contacts(
        self,
        expand: Optional[str] = None,
        filter: Optional[str] = None,
        inlinecount: Optional[str] = None,
        orderby: Optional[str] = None,
        select: Optional[str] = None,
        skip: Optional[str] = None,
        top: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Retrieves a list of all contacts in the customer relationship management system.

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

    def get_customers(
        self,
        expand: Optional[str] = None,
        filter: Optional[str] = None,
        inlinecount: Optional[str] = None,
        orderby: Optional[str] = None,
        select: Optional[str] = None,
        skip: Optional[str] = None,
        top: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Retrieves a list of all customers in the system.

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

    def get_entities(
        self,
        expand: Optional[str] = None,
        filter: Optional[str] = None,
        inlinecount: Optional[str] = None,
        orderby: Optional[str] = None,
        select: Optional[str] = None,
        skip: Optional[str] = None,
        top: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Retrieves a list of all entities within the application.

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

    def get_lead(
        self,
        leadId: str,
    ) -> Dict[str, Any]:
        """Retrieves detailed information for a specific lead.

        Args:
            leadId: The ID of the lead. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def get_leads(
        self,
        expand: Optional[str] = None,
        filter: Optional[str] = None,
        orderby: Optional[str] = None,
        select: Optional[str] = None,
        skip: Optional[str] = None,
        top: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Retrieves a list of all leads in the sales management system.

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

    def get_meta_data_of_tables(
        self,
    ) -> Dict[str, Any]:
        """Fetches metadata for the specified tables, including column details and data types.
        Returns:
            API response as a dictionary.
        """
        ...

    def get_opportunities(
        self,
        expand: Optional[str] = None,
        filter: Optional[str] = None,
        orderby: Optional[str] = None,
        select: Optional[str] = None,
        skip: Optional[str] = None,
        top: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Retrieves a list of all opportunities in the sales management pipeline.

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

    def get_opportunity(
        self,
        opportunityId: str,
    ) -> Dict[str, Any]:
        """Retrieves detailed information for a specific opportunity.

        Args:
            opportunityId: The ID of the opportunity. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def get_records(
        self,
        expand: Optional[str] = None,
        filter: Optional[str] = None,
        orderby: Optional[str] = None,
        select: Optional[str] = None,
        skip: Optional[str] = None,
        top: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Retrieves records from a specified table in the database.

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

    def get_sale_order(
        self,
        expand: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Retrieves detailed information for a specific sales order.

        Args:
            expand: 
        Returns:
            API response as a dictionary.
        """
        ...

    def get_sales_orders(
        self,
        skip: Optional[str] = None,
        top: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Retrieves a list of all sales orders in the sales management system.

        Args:
            skip: 
            top: 
        Returns:
            API response as a dictionary.
        """
        ...

    def get_stock_item(
        self,
        stockItemId: str,
    ) -> Dict[str, Any]:
        """Retrieves detailed information for a specific stock item.

        Args:
            stockItemId: The ID of the stock item. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def get_stock_items(
        self,
        expand: Optional[str] = None,
        select: Optional[str] = None,
        skip: Optional[str] = None,
        top: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Retrieves a list of all stock items in the inventory management system.

        Args:
            expand: 
            select: 
            skip: 
            top: 
        Returns:
            API response as a dictionary.
        """
        ...

    def get_tables(
        self,
    ) -> Dict[str, Any]:
        """Retrieves a list of available tables in the database.
        Returns:
            API response as a dictionary.
        """
        ...

    def login(
        self,
        name: Optional[str] = None,
        password: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Logs in a user to the application, providing access to the system's features.

        Args:
            name: 
            password: 
        Returns:
            API response as a dictionary.
        """
        ...

    def logout(
        self,
    ) -> Dict[str, Any]:
        """Logs out a user from the application, terminating their session.
        Returns:
            API response as a dictionary.
        """
        ...

