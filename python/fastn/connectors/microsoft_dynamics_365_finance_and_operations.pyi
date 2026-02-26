"""Fastn Microsoft Dynamics 365 Finance and Operations connector — auto-generated type stubs.

Do not edit manually. Regenerate with `fastn connector sync`.
"""
from __future__ import annotations

from typing import Any, Dict, List, Optional


class MicrosoftDynamics365FinanceAndOperationsConnector:
    """Microsoft Dynamics 365 Finance and Operations connector ().

    Provides 57 tools.
    """

    def create_coupon_usage_microsoft_dynamics_365_finance_and_operations(
        self,
        CouponCodeId: Optional[str] = None,
        CustomerAccount: Optional[str] = None,
        RetailChannelId: Optional[str] = None,
        SalesId: Optional[str] = None,
        UsageId: Optional[str] = None,
        dataAreaId: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Creates coupon usage records in Microsoft Dynamics 365 Finance and Operations.

        Args:
            CouponCodeId: 
            CustomerAccount: 
            RetailChannelId: 
            SalesId: 
            UsageId: 
            dataAreaId: 
        Returns:
            API response as a dictionary.
        """
        ...

    def create_customer_address_microsoft_dynamics_365_finance_and_operations(
        self,
        City: Optional[str] = None,
        CountryRegionISOCode: Optional[str] = None,
        Description: Optional[str] = None,
        IsRoleDelivery: Optional[str] = None,
        PartyNumber: Optional[str] = None,
        Roles: Optional[str] = None,
        State: Optional[str] = None,
        Street: Optional[str] = None,
        ZipCode: Optional[str] = None,
        rsmWebActive: Optional[bool] = None,
    ) -> Dict[str, Any]:
        """Creates a customer address in Microsoft Dynamics 365 Finance and Operations.

        Args:
            City: 
            CountryRegionISOCode: 
            Description: 
            IsRoleDelivery: 
            PartyNumber: 
            Roles: 
            State: 
            Street: 
            ZipCode: 
            rsmWebActive: 
        Returns:
            API response as a dictionary.
        """
        ...

    def create_order_note_document_attachment_microsoft_dynamics_365_finance_and_operations(
        self,
        AttachmentDescription: Optional[str] = None,
        DocumentAttachmentTypeCode: Optional[str] = None,
        Notes: Optional[str] = None,
        SalesOrderNumber: Optional[str] = None,
        dataAreaId: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Creates an order note or document attachment in Microsoft Dynamics 365 Finance and Operations.

        Args:
            AttachmentDescription: 
            DocumentAttachmentTypeCode: 
            Notes: 
            SalesOrderNumber: 
            dataAreaId: 
        Returns:
            API response as a dictionary.
        """
        ...

    def create_sales_order_header_microsoft_dynamics_365_finance_and_operations(
        self,
        CustomerRequisitionNumber: Optional[str] = None,
        CustomersOrderReference: Optional[str] = None,
        DeliveryAddressCity: Optional[str] = None,
        DeliveryAddressCountryRegionISOCode: Optional[str] = None,
        DeliveryAddressDescription: Optional[str] = None,
        DeliveryAddressLocationId: Optional[str] = None,
        DeliveryAddressState: Optional[str] = None,
        DeliveryAddressStreet: Optional[str] = None,
        DeliveryAddressZipCode: Optional[str] = None,
        DeliveryModeCode: Optional[str] = None,
        DeliveryTermsCode: Optional[str] = None,
        Email: Optional[str] = None,
        NMBDeliveryPhone: Optional[str] = None,
        NMBShipCarrierDeliveryContact: Optional[str] = None,
        NMBShipCarrierPostalAddress: Optional[str] = None,
        NmbShipCarrierAccount: Optional[str] = None,
        NmbShipCarrierPostalAddressName: Optional[str] = None,
        OrderingCustomerAccountNumber: Optional[str] = None,
        RequestedShippingDate: Optional[str] = None,
        dataAreaId: Optional[str] = None,
        envReadyToShip: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Creates a new sales order header in Microsoft Dynamics 365 Finance and Operations.

        Args:
            CustomerRequisitionNumber: 
            CustomersOrderReference: 
            DeliveryAddressCity: 
            DeliveryAddressCountryRegionISOCode: 
            DeliveryAddressDescription: 
            DeliveryAddressLocationId: 
            DeliveryAddressState: 
            DeliveryAddressStreet: 
            DeliveryAddressZipCode: 
            DeliveryModeCode: 
            DeliveryTermsCode: 
            Email: 
            NMBDeliveryPhone: 
            NMBShipCarrierDeliveryContact: 
            NMBShipCarrierPostalAddress: 
            NmbShipCarrierAccount: 
            NmbShipCarrierPostalAddressName: 
            OrderingCustomerAccountNumber: 
            RequestedShippingDate: 
            dataAreaId: 
            envReadyToShip: 
        Returns:
            API response as a dictionary.
        """
        ...

    def create_sales_order_lines_microsoft_dynamics_365_finance_and_operations(
        self,
        ItemNumber: Optional[str] = None,
        OrderedSalesQuantity: Optional[int] = None,
        SalesOrderNumber: Optional[str] = None,
        dataAreaId: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Creates new sales order lines in Microsoft Dynamics 365 Finance and Operations.

        Args:
            ItemNumber: 
            OrderedSalesQuantity: 
            SalesOrderNumber: 
            dataAreaId: 
        Returns:
            API response as a dictionary.
        """
        ...

    def customer_packing_slip_journal_microsoft_dynamics_365_finance_and_operations(
        self,
        crosscompany: Optional[str] = None,
        filter: Optional[str] = None,
        select: Optional[str] = None,
        skip: Optional[str] = None,
        top: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Generates a customer packing slip journal in Microsoft Dynamics 365 Finance and Operations.

        Args:
            crosscompany: 
            filter: 
            select: 
            skip: 
            top: 
        Returns:
            API response as a dictionary.
        """
        ...

    def customer_price_group_lookup_microsoft_dynamics_365_finance_and_operations(
        self,
        crosscompany: Optional[str] = None,
        filter: Optional[str] = None,
        select: Optional[str] = None,
        skip: Optional[str] = None,
        top: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Looks up customer price groups in Microsoft Dynamics 365 Finance and Operations.

        Args:
            crosscompany: 
            filter: 
            select: 
            skip: 
            top: 
        Returns:
            API response as a dictionary.
        """
        ...

    def delete_order_note_microsoft_dynamics_365_finance_and_operations(
        self,
        dataAreaId: Optional[str] = None,
        documentId: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Deletes an order note in Microsoft Dynamics 365 Finance and Operations.

        Args:
            dataAreaId: 
            documentId: 
        Returns:
            API response as a dictionary.
        """
        ...

    def delivery_modes_microsoft_dynamics_365_finance_and_operations(
        self,
        crosscompany: Optional[str] = None,
        filter: Optional[str] = None,
        select: Optional[str] = None,
        skip: Optional[str] = None,
        top: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Retrieves delivery modes in Microsoft Dynamics 365 Finance and Operations.

        Args:
            crosscompany: 
            filter: 
            select: 
            skip: 
            top: 
        Returns:
            API response as a dictionary.
        """
        ...

    def delivery_terms_microsoft_dynamics_365_finance_and_operations(
        self,
        crosscompany: Optional[str] = None,
        filter: Optional[str] = None,
        skip: Optional[str] = None,
        top: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Retrieves delivery terms in Microsoft Dynamics 365 Finance and Operations.

        Args:
            crosscompany: 
            filter: 
            skip: 
            top: 
        Returns:
            API response as a dictionary.
        """
        ...

    def get_all_categories_microsoft_dynamics_365_finance_and_operations(
        self,
        filter: Optional[str] = None,
        orderby: Optional[str] = None,
        select: Optional[str] = None,
        skip: Optional[str] = None,
        top: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Gets all categories in Microsoft Dynamics 365 Finance and Operations.

        Args:
            filter: 
            orderby: 
            select: 
            skip: 
            top: 
        Returns:
            API response as a dictionary.
        """
        ...

    def get_all_sales_invoices_microsoft_dynamics_365_finance_and_operations(
        self,
        crosscompany: Optional[str] = None,
        filter: Optional[str] = None,
        select: Optional[str] = None,
        skip: Optional[str] = None,
        top: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Retrieves all sales invoices in Microsoft Dynamics 365 Finance and Operations.

        Args:
            crosscompany: 
            filter: 
            select: 
            skip: 
            top: 
        Returns:
            API response as a dictionary.
        """
        ...

    def get_all_sales_orders_microsoft_dynamics_365_finance_and_operations(
        self,
        crosscompany: Optional[str] = None,
        filter: Optional[str] = None,
        select: Optional[str] = None,
        skip: Optional[str] = None,
        top: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Gets all sales orders in Microsoft Dynamics 365 Finance and Operations.

        Args:
            crosscompany: 
            filter: 
            select: 
            skip: 
            top: 
        Returns:
            API response as a dictionary.
        """
        ...

    def get_all_web_enabled_customers_microsoft_dynamics_365_finance_and_operations(
        self,
        crosscompany: Optional[str] = None,
        filter: Optional[str] = None,
        select: Optional[str] = None,
        skip: Optional[str] = None,
        top: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Retrieves all web-enabled customers in Microsoft Dynamics 365 Finance and Operations.

        Args:
            crosscompany: 
            filter: 
            select: 
            skip: 
            top: 
        Returns:
            API response as a dictionary.
        """
        ...

    def get_category_active_status_microsoft_dynamics_365_finance_and_operations(
        self,
        filter: Optional[str] = None,
        select: Optional[str] = None,
        skip: Optional[str] = None,
        top: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Checks the active status of a category in Microsoft Dynamics 365 Finance and Operations.

        Args:
            filter: 
            select: 
            skip: 
            top: 
        Returns:
            API response as a dictionary.
        """
        ...

    def get_category_assignment_by_list_number_microsoft_dynamics_365_finance_and_operations(
        self,
        filter: Optional[str] = None,
        orderby: Optional[str] = None,
        select: Optional[str] = None,
        skip: Optional[str] = None,
        top: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Gets category assignment by list number in Microsoft Dynamics 365 Finance and Operations.

        Args:
            filter: 
            orderby: 
            select: 
            skip: 
            top: 
        Returns:
            API response as a dictionary.
        """
        ...

    def get_category_assignment_by_product_number_microsoft_dynamics_365_finance_and_operations(
        self,
        filter: Optional[str] = None,
        orderby: Optional[str] = None,
        select: Optional[str] = None,
        skip: Optional[str] = None,
        top: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Gets category assignment by product number in Microsoft Dynamics 365 Finance and Operations.

        Args:
            filter: 
            orderby: 
            select: 
            skip: 
            top: 
        Returns:
            API response as a dictionary.
        """
        ...

    def get_customer_addresses_microsoft_dynamics_365_finance_and_operations(
        self,
        filter: Optional[str] = None,
        select: Optional[str] = None,
        skip: Optional[str] = None,
        top: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Retrieves customer addresses in Microsoft Dynamics 365 Finance and Operations.

        Args:
            filter: 
            select: 
            skip: 
            top: 
        Returns:
            API response as a dictionary.
        """
        ...

    def get_customer_affiliation_microsoft_dynamics_365_finance_and_operations(
        self,
        crosscompany: Optional[str] = None,
        filter: Optional[str] = None,
        select: Optional[str] = None,
        skip: Optional[str] = None,
        top: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Gets customer affiliation details in Microsoft Dynamics 365 Finance and Operations.

        Args:
            crosscompany: 
            filter: 
            select: 
            skip: 
            top: 
        Returns:
            API response as a dictionary.
        """
        ...

    def get_customer_aged_balance_microsoft_dynamics_365_finance_and_operations(
        self,
        crosscompany: Optional[str] = None,
        filter: Optional[str] = None,
        select: Optional[str] = None,
        skip: Optional[str] = None,
        top: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Retrieves the aged balance for a customer in Microsoft Dynamics 365 Finance and Operations.

        Args:
            crosscompany: 
            filter: 
            select: 
            skip: 
            top: 
        Returns:
            API response as a dictionary.
        """
        ...

    def get_customer_by_party_number_microsoft_dynamics_365_finance_and_operations(
        self,
        crosscompany: Optional[str] = None,
        filter: Optional[str] = None,
        skip: Optional[str] = None,
        top: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Gets customer information by party number in Microsoft Dynamics 365 Finance and Operations.

        Args:
            crosscompany: 
            filter: 
            skip: 
            top: 
        Returns:
            API response as a dictionary.
        """
        ...

    def get_customer_cash_discount_microsoft_dynamics_365_finance_and_operations(
        self,
        crosscompany: Optional[str] = None,
        filter: Optional[str] = None,
        select: Optional[str] = None,
        skip: Optional[str] = None,
        top: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Gets customer cash discount details in Microsoft Dynamics 365 Finance and Operations.

        Args:
            crosscompany: 
            filter: 
            select: 
            skip: 
            top: 
        Returns:
            API response as a dictionary.
        """
        ...

    def get_customer_part_number_by_product_microsoft_dynamics_365_finance_and_operations(
        self,
        crosscompany: Optional[str] = None,
        filter: Optional[str] = None,
        select: Optional[str] = None,
        skip: Optional[str] = None,
        top: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Retrieves customer part number associated with a product in Microsoft Dynamics 365 Finance and Operations.

        Args:
            crosscompany: 
            filter: 
            select: 
            skip: 
            top: 
        Returns:
            API response as a dictionary.
        """
        ...

    def get_customer_payment_terms_microsoft_dynamics_365_finance_and_operations(
        self,
        crosscompany: Optional[str] = None,
        filter: Optional[str] = None,
        select: Optional[str] = None,
        skip: Optional[str] = None,
        top: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Gets customer payment terms in Microsoft Dynamics 365 Finance and Operations.

        Args:
            crosscompany: 
            filter: 
            select: 
            skip: 
            top: 
        Returns:
            API response as a dictionary.
        """
        ...

    def get_customer_price_group_microsoft_dynamics_365_finance_and_operations(
        self,
        crosscompany: Optional[str] = None,
        filter: Optional[str] = None,
        select: Optional[str] = None,
        skip: Optional[str] = None,
        top: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Retrieves the customer price group in Microsoft Dynamics 365 Finance and Operations.

        Args:
            crosscompany: 
            filter: 
            select: 
            skip: 
            top: 
        Returns:
            API response as a dictionary.
        """
        ...

    def get_customer_transactions_microsoft_dynamics_365_finance_and_operations(
        self,
        crosscompany: Optional[str] = None,
        filter: Optional[str] = None,
        select: Optional[str] = None,
        skip: Optional[str] = None,
        top: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Gets customer transaction history in Microsoft Dynamics 365 Finance and Operations.

        Args:
            crosscompany: 
            filter: 
            select: 
            skip: 
            top: 
        Returns:
            API response as a dictionary.
        """
        ...

    def get_delivery_modes_microsoft_dynamics_365_finance_and_operations(
        self,
        crosscompany: Optional[str] = None,
        filter: Optional[str] = None,
        select: Optional[str] = None,
        skip: Optional[str] = None,
        top: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Retrieves delivery modes available in Microsoft Dynamics 365 Finance and Operations.

        Args:
            crosscompany: 
            filter: 
            select: 
            skip: 
            top: 
        Returns:
            API response as a dictionary.
        """
        ...

    def get_discount_assignment_by_product_number_microsoft_dynamics_365_finance_and_operations(
        self,
        filter: Optional[str] = None,
        select: Optional[str] = None,
        skip: Optional[str] = None,
        top: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Gets discount assignment by product number in Microsoft Dynamics 365 Finance and Operations.

        Args:
            filter: 
            select: 
            skip: 
            top: 
        Returns:
            API response as a dictionary.
        """
        ...

    def get_discount_category_microsoft_dynamics_365_finance_and_operations(
        self,
        filter: Optional[str] = None,
        select: Optional[str] = None,
        skip: Optional[str] = None,
        top: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Retrieves details about discount categories in Microsoft Dynamics 365 Finance and Operations.

        Args:
            filter: 
            select: 
            skip: 
            top: 
        Returns:
            API response as a dictionary.
        """
        ...

    def get_invoice_lines_microsoft_dynamics_365_finance_and_operations(
        self,
        crosscompany: Optional[str] = None,
        filter: Optional[str] = None,
        select: Optional[str] = None,
        skip: Optional[str] = None,
        top: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Gets invoice lines for a specified invoice in Microsoft Dynamics 365 Finance and Operations.

        Args:
            crosscompany: 
            filter: 
            select: 
            skip: 
            top: 
        Returns:
            API response as a dictionary.
        """
        ...

    def get_invoice_shipments_microsoft_dynamics_365_finance_and_operations(
        self,
        crosscompany: Optional[str] = None,
        filter: Optional[str] = None,
        select: Optional[str] = None,
        skip: Optional[str] = None,
        top: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Retrieves shipment details related to an invoice in Microsoft Dynamics 365 Finance and Operations.

        Args:
            crosscompany: 
            filter: 
            select: 
            skip: 
            top: 
        Returns:
            API response as a dictionary.
        """
        ...

    def get_invoiced_customer_details_microsoft_dynamics_365_finance_and_operations(
        self,
        crosscompany: Optional[str] = None,
        filter: Optional[str] = None,
        select: Optional[str] = None,
        skip: Optional[str] = None,
        top: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Gets details of an invoiced customer in Microsoft Dynamics 365 Finance and Operations.

        Args:
            crosscompany: 
            filter: 
            select: 
            skip: 
            top: 
        Returns:
            API response as a dictionary.
        """
        ...

    def get_list_categories_microsoft_dynamics_365_finance_and_operations(
        self,
        filter: Optional[str] = None,
        orderby: Optional[str] = None,
        select: Optional[str] = None,
        skip: Optional[str] = None,
        top: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Retrieves a list of categories in Microsoft Dynamics 365 Finance and Operations.

        Args:
            filter: 
            orderby: 
            select: 
            skip: 
            top: 
        Returns:
            API response as a dictionary.
        """
        ...

    def get_order_coupon_usage_microsoft_dynamics_365_finance_and_operations(
        self,
        crosscompany: Optional[str] = None,
        filter: Optional[str] = None,
        select: Optional[str] = None,
        skip: Optional[str] = None,
        top: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Gets order coupon usage information in Microsoft Dynamics 365 Finance and Operations.

        Args:
            crosscompany: 
            filter: 
            select: 
            skip: 
            top: 
        Returns:
            API response as a dictionary.
        """
        ...

    def get_order_line_charges_microsoft_dynamics_365_finance_and_operations(
        self,
        crosscompany: Optional[str] = None,
        filter: Optional[str] = None,
        select: Optional[str] = None,
        skip: Optional[str] = None,
        top: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Retrieves order line charges in Microsoft Dynamics 365 Finance and Operations.

        Args:
            crosscompany: 
            filter: 
            select: 
            skip: 
            top: 
        Returns:
            API response as a dictionary.
        """
        ...

    def get_packing_slip_details_microsoft_dynamics_365_finance_and_operations(
        self,
        crosscompany: Optional[str] = None,
        filter: Optional[str] = None,
        select: Optional[str] = None,
        skip: Optional[str] = None,
        top: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Gets packing slip details in Microsoft Dynamics 365 Finance and Operations.

        Args:
            crosscompany: 
            filter: 
            select: 
            skip: 
            top: 
        Returns:
            API response as a dictionary.
        """
        ...

    def get_packing_slip_journal_microsoft_dynamics_365_finance_and_operations(
        self,
        crosscompany: Optional[str] = None,
        filter: Optional[str] = None,
        select: Optional[str] = None,
        skip: Optional[str] = None,
        top: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Retrieves packing slip journal entries in Microsoft Dynamics 365 Finance and Operations.

        Args:
            crosscompany: 
            filter: 
            select: 
            skip: 
            top: 
        Returns:
            API response as a dictionary.
        """
        ...

    def get_product_category_assignment_microsoft_dynamics_365_finance_and_operations(
        self,
        filter: Optional[str] = None,
        select: Optional[str] = None,
        skip: Optional[str] = None,
        top: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Retrieves product category assignment in Microsoft Dynamics 365 Finance and Operations.

        Args:
            filter: 
            select: 
            skip: 
            top: 
        Returns:
            API response as a dictionary.
        """
        ...

    def get_product_category_hierarchy_microsoft_dynamics_365_finance_and_operations(
        self,
        filter: Optional[str] = None,
        orderby: Optional[str] = None,
        select: Optional[str] = None,
        skip: Optional[str] = None,
        top: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Gets the product category hierarchy in Microsoft Dynamics 365 Finance and Operations.

        Args:
            filter: 
            orderby: 
            select: 
            skip: 
            top: 
        Returns:
            API response as a dictionary.
        """
        ...

    def get_product_details_microsoft_dynamics_365_finance_and_operations(
        self,
        crosscompany: Optional[str] = None,
        filter: Optional[str] = None,
        select: Optional[str] = None,
        skip: Optional[str] = None,
        top: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Retrieves detailed specifications of a product in Microsoft Dynamics 365 Finance and Operations.

        Args:
            crosscompany: 
            filter: 
            select: 
            skip: 
            top: 
        Returns:
            API response as a dictionary.
        """
        ...

    def get_product_engineering_attributes_microsoft_dynamics_365_finance_and_operations(
        self,
        crosscompany: Optional[str] = None,
        filter: Optional[str] = None,
        select: Optional[str] = None,
        skip: Optional[str] = None,
        top: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Gets engineering attributes associated with a product in Microsoft Dynamics 365 Finance and Operations.

        Args:
            crosscompany: 
            filter: 
            select: 
            skip: 
            top: 
        Returns:
            API response as a dictionary.
        """
        ...

    def get_product_microsoft_dynamics_365_finance_and_operations(
        self,
        filter: Optional[str] = None,
        select: Optional[str] = None,
        skip: Optional[str] = None,
        top: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Gets details of a specific product in Microsoft Dynamics 365 Finance and Operations.

        Args:
            filter: 
            select: 
            skip: 
            top: 
        Returns:
            API response as a dictionary.
        """
        ...

    def get_product_order_settings_microsoft_dynamics_365_finance_and_operations(
        self,
        crosscompany: Optional[str] = None,
        filter: Optional[str] = None,
        select: Optional[str] = None,
        skip: Optional[str] = None,
        top: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Retrieves product order settings in Microsoft Dynamics 365 Finance and Operations.

        Args:
            crosscompany: 
            filter: 
            select: 
            skip: 
            top: 
        Returns:
            API response as a dictionary.
        """
        ...

    def get_sales_order_lines_microsoft_dynamics_365_finance_and_operations(
        self,
        crosscompany: Optional[str] = None,
        filter: Optional[str] = None,
        select: Optional[str] = None,
        skip: Optional[str] = None,
        top: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Gets sales order lines in Microsoft Dynamics 365 Finance and Operations.

        Args:
            crosscompany: 
            filter: 
            select: 
            skip: 
            top: 
        Returns:
            API response as a dictionary.
        """
        ...

    def get_sales_order_notes_microsoft_dynamics_365_finance_and_operations(
        self,
        crosscompany: Optional[str] = None,
        filter: Optional[str] = None,
        select: Optional[str] = None,
        skip: Optional[str] = None,
        top: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Retrieves notes associated with sales orders in Microsoft Dynamics 365 Finance and Operations.

        Args:
            crosscompany: 
            filter: 
            select: 
            skip: 
            top: 
        Returns:
            API response as a dictionary.
        """
        ...

    def get_shipment_details_microsoft_dynamics_365_finance_and_operations(
        self,
        crosscompany: Optional[str] = None,
        filter: Optional[str] = None,
        select: Optional[str] = None,
        skip: Optional[str] = None,
        top: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Gets details about shipments in Microsoft Dynamics 365 Finance and Operations.

        Args:
            crosscompany: 
            filter: 
            select: 
            skip: 
            top: 
        Returns:
            API response as a dictionary.
        """
        ...

    def get_specific_sales_order_microsoft_dynamics_365_finance_and_operations(
        self,
        crosscompany: Optional[str] = None,
        filter: Optional[str] = None,
        skip: Optional[str] = None,
        top: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Retrieves a specific sales order in Microsoft Dynamics 365 Finance and Operations.

        Args:
            crosscompany: 
            filter: 
            skip: 
            top: 
        Returns:
            API response as a dictionary.
        """
        ...

    def get_third_party_delivery_address_microsoft_dynamics_365_finance_and_operations(
        self,
        crosscompany: Optional[str] = None,
        filter: Optional[str] = None,
        select: Optional[str] = None,
        skip: Optional[str] = None,
        top: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Gets the third-party delivery address in Microsoft Dynamics 365 Finance and Operations.

        Args:
            crosscompany: 
            filter: 
            select: 
            skip: 
            top: 
        Returns:
            API response as a dictionary.
        """
        ...

    def get_warehouse_on_hand_stock_microsoft_dynamics_365_finance_and_operations(
        self,
        crosscompany: Optional[str] = None,
        filter: Optional[str] = None,
        select: Optional[str] = None,
        skip: Optional[str] = None,
        top: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Retrieves on-hand stock information from the warehouse in Microsoft Dynamics 365 Finance and Operations.

        Args:
            crosscompany: 
            filter: 
            select: 
            skip: 
            top: 
        Returns:
            API response as a dictionary.
        """
        ...

    def invoice_to_shipment_mapping_microsoft_dynamics_365_finance_and_operations(
        self,
        crosscompany: Optional[str] = None,
        filter: Optional[str] = None,
        select: Optional[str] = None,
        skip: Optional[str] = None,
        top: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Maps invoices to shipments in Microsoft Dynamics 365 Finance and Operations.

        Args:
            crosscompany: 
            filter: 
            select: 
            skip: 
            top: 
        Returns:
            API response as a dictionary.
        """
        ...

    def packing_slip_details_microsoft_dynamics_365_finance_and_operations(
        self,
        crosscompany: Optional[str] = None,
        filter: Optional[str] = None,
        select: Optional[str] = None,
        skip: Optional[str] = None,
        top: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Gets detailed information from packing slips in Microsoft Dynamics 365 Finance and Operations.

        Args:
            crosscompany: 
            filter: 
            select: 
            skip: 
            top: 
        Returns:
            API response as a dictionary.
        """
        ...

    def packing_slip_tracking_information_microsoft_dynamics_365_finance_and_operations(
        self,
        crosscompany: Optional[str] = None,
        filter: Optional[str] = None,
        select: Optional[str] = None,
        skip: Optional[str] = None,
        top: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Retrieves packing slip tracking information in Microsoft Dynamics 365 Finance and Operations.

        Args:
            crosscompany: 
            filter: 
            select: 
            skip: 
            top: 
        Returns:
            API response as a dictionary.
        """
        ...

    def released_product_details_with_pricing_microsoft_dynamics_365_finance_and_operations(
        self,
        crosscompany: Optional[str] = None,
        filter: Optional[str] = None,
        select: Optional[str] = None,
        skip: Optional[str] = None,
        top: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Gets details of released products along with their pricing in Microsoft Dynamics 365 Finance and Operations.

        Args:
            crosscompany: 
            filter: 
            select: 
            skip: 
            top: 
        Returns:
            API response as a dictionary.
        """
        ...

    def sales_price_lookup_by_sales_order_microsoft_dynamics_365_finance_and_operations(
        self,
        crosscompany: Optional[str] = None,
        expand: Optional[str] = None,
        filter: Optional[str] = None,
        select: Optional[str] = None,
        skip: Optional[str] = None,
        top: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Looks up sales prices by sales order in Microsoft Dynamics 365 Finance and Operations.

        Args:
            crosscompany: 
            expand: 
            filter: 
            select: 
            skip: 
            top: 
        Returns:
            API response as a dictionary.
        """
        ...

    def shipment_details_microsoft_dynamics_365_finance_and_operations(
        self,
        crosscompany: Optional[str] = None,
        filter: Optional[str] = None,
        select: Optional[str] = None,
        skip: Optional[str] = None,
        top: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Gets details about shipments in Microsoft Dynamics 365 Finance and Operations.

        Args:
            crosscompany: 
            filter: 
            select: 
            skip: 
            top: 
        Returns:
            API response as a dictionary.
        """
        ...

    def shipment_methods_microsoft_dynamics_365_finance_and_operations(
        self,
        crosscompany: Optional[str] = None,
        filter: Optional[str] = None,
        select: Optional[str] = None,
        skip: Optional[str] = None,
        top: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Retrieves shipment methods available in Microsoft Dynamics 365 Finance and Operations.

        Args:
            crosscompany: 
            filter: 
            select: 
            skip: 
            top: 
        Returns:
            API response as a dictionary.
        """
        ...

    def update_customer_address_microsoft_dynamics_365_finance_and_operations(
        self,
        City: Optional[str] = None,
        CountryRegionISOCode: Optional[str] = None,
        IsRoleDelivery: Optional[str] = None,
        LocationId: Optional[str] = None,
        PartyNumber: Optional[str] = None,
        Roles: Optional[str] = None,
        State: Optional[str] = None,
        Street: Optional[str] = None,
        ZipCode: Optional[str] = None,
        rsmWebActive: Optional[bool] = None,
    ) -> Dict[str, Any]:
        """Updates a customer address in Microsoft Dynamics 365 Finance and Operations.

        Args:
            City: 
            CountryRegionISOCode: 
            IsRoleDelivery: 
            LocationId: 
            PartyNumber: 
            Roles: 
            State: 
            Street: 
            ZipCode: 
            rsmWebActive: 
        Returns:
            API response as a dictionary.
        """
        ...

