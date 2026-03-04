"""Fastn Microsoft Dynamics 365 Finance and Operations connector — auto-generated type stubs.

Do not edit manually. Regenerate with `fastn connector sync`.
"""
from __future__ import annotations

from typing import Any, Dict, List, Optional, TypedDict


class MicrosoftDynamics365FinanceAndOperationsConnector:
    """Microsoft Dynamics 365 Finance and Operations connector ().

    Provides 58 tools.
    """

    def ms_d365fo_create_coupon_usage(
        self,
        CouponCodeId: str,
        CustomerAccount: str,
        RetailChannelId: str,
        UsageId: str,
        dataAreaId: str,
        SalesId: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Creates a new coupon usage entry in Microsoft Dynamics 365 Finance and Operations by posting to the CouponUsages entity. Use this tool when you need to record the application of a coupon to an order or transaction. This operation writes data to the system and may affect pricing calculations and order totals. Not intended for retrieving existing coupon usage records (use ms_d365fo_get_order_coupon_usage).

        Args:
            CouponCodeId: Identifier for the coupon code being used. (required)
            CustomerAccount: The account identifier of the customer redeeming the coupon. (required)
            RetailChannelId: Identifier of the retail channel where the coupon is applied. (required)
            UsageId: Unique identifier for this coupon usage transaction. (required)
            dataAreaId: Specifies the company or data area context for the record. (required)
            SalesId: Identifier of the related sales transaction.
        Returns:
            API response as a dictionary.
        """
        ...

    def ms_d365fo_create_customer_address(
        self,
        City: str,
        CountryRegionISOCode: str,
        PartyNumber: str,
        Street: str,
        ZipCode: str,
        Description: Optional[str] = None,
        IsRoleDelivery: Optional[str] = None,
        Roles: Optional[str] = None,
        State: Optional[str] = None,
        rsmWebActive: Optional[bool] = None,
    ) -> Dict[str, Any]:
        """Creates a new postal address record for a customer party in Microsoft Dynamics 365 Finance and Operations by posting to the PartyLocationPostalAddressesV2 entity. Use this tool when you need to add a new billing, shipping, or other address to a customer account. This operation writes a new record to the system. Not intended for updating an existing address (use ms_d365fo_update_customer_address) or reading addresses (use ms_d365fo_list_customer_addresses).

        Args:
            City: The city of the customer's address. (required)
            CountryRegionISOCode: The ISO code representing the customer's country or region. (required)
            PartyNumber: The unique identifier of the customer party. (required)
            Street: The street address of the customer. (required)
            ZipCode: The postal code of the customer's address. (required)
            Description: Additional descriptive information about the address.
            IsRoleDelivery: Indicates if the address role is for delivery.
            Roles: The roles associated with this address.
            State: The state or province of the customer's address.
            rsmWebActive: Indicates if the RSM web status is active for this address.
        Returns:
            API response as a dictionary.
        """
        ...

    def ms_d365fo_create_order_note_or_document_attachment(
        self,
        SalesOrderNumber: str,
        dataAreaId: str,
        AttachmentDescription: Optional[str] = None,
        DocumentAttachmentTypeCode: Optional[str] = None,
        Notes: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Creates a new note or document attachment on a sales order header in Microsoft Dynamics 365 Finance and Operations by posting to the SalesOrderHeaderDocumentAttachments entity. Use this tool when you need to attach a text note or document reference to an existing sales order for internal communication, instructions, or compliance purposes. This operation writes data to the system. Not intended for deleting notes (use ms_d365fo_delete_order_note) or retrieving existing notes (use ms_d365fo_list_sales_order_notes).

        Args:
            SalesOrderNumber: The sales order identifier associated with the attachment or operation. (required)
            dataAreaId: The company or legal entity identifier (data area) within Dynamics 365 Finance and Operations. (required)
            AttachmentDescription: A short description of the attachment being added or referenced.
            DocumentAttachmentTypeCode: A code that specifies the type or category of the document attachment.
            Notes: Additional notes or comments related to the attachment or operation.
        Returns:
            API response as a dictionary.
        """
        ...

    def ms_d365fo_create_sales_order_header(
        self,
        OrderingCustomerAccountNumber: str,
        dataAreaId: str,
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
        RequestedShippingDate: Optional[str] = None,
        envReadyToShip: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Creates a new sales order header record in Microsoft Dynamics 365 Finance and Operations by posting to the SalesOrderHeadersV3 entity. Use this tool to initiate a new sales order with customer, currency, delivery, and other header-level information. This operation writes data to the system; once the order is confirmed or released, reversal may require additional steps. Always create the header before adding lines (use ms_d365fo_create_sales_order_lines). Not intended for updating existing sales orders or retrieving order data.

        Args:
            OrderingCustomerAccountNumber: Account number of the ordering customer in Dynamics 365 F&O; typically required to identify the customer placing the order. (required)
            dataAreaId: Legal entity or data area identifier in Dynamics 365 F&O (commonly required to scope the request to the correct company). (required)
            CustomerRequisitionNumber: Customer's internal requisition number associated with this order.
            CustomersOrderReference: Reference or order number provided by the customer for this transaction.
            DeliveryAddressCity: City of the delivery address for the order.
            DeliveryAddressCountryRegionISOCode: ISO country/region code for the delivery address (e.g., 'US', 'GB').
            DeliveryAddressDescription: Additional descriptive information about the delivery address (e.g., building or landmark).
            DeliveryAddressLocationId: Identifier for the delivery location, if managed as a location record in Dynamics 365 F&O.
            DeliveryAddressState: State or province for the delivery address.
            DeliveryAddressStreet: Street address for the delivery location.
            DeliveryAddressZipCode: ZIP or postal code for the delivery address.
            DeliveryModeCode: Code indicating the delivery mode or service level for the order.
            DeliveryTermsCode: Code representing the agreed delivery terms (e.g., Incoterms) for the shipment.
            Email: Contact email address for the customer or recipient related to the order.
            NMBDeliveryPhone: Phone number for the delivery contact at the delivery address.
            NMBShipCarrierDeliveryContact: Contact name or identifier for the shipping carrier responsible for delivery.
            NMBShipCarrierPostalAddress: Postal address of the shipping carrier associated with this shipment.
            NmbShipCarrierAccount: Account identifier for the shipping carrier used for this shipment.
            NmbShipCarrierPostalAddressName: Name associated with the shipping carrier's postal address.
            RequestedShippingDate: Date when the customer requests the shipment to be sent (ISO 8601 format recommended).
            envReadyToShip: Flag or indicator used by the environment/process to mark whether the order is ready to ship.
        Returns:
            API response as a dictionary.
        """
        ...

    def ms_d365fo_create_sales_order_lines(
        self,
        ItemNumber: str,
        OrderedSalesQuantity: int,
        SalesOrderNumber: str,
        dataAreaId: str,
    ) -> Dict[str, Any]:
        """Creates one or more new line items on a sales order in Microsoft Dynamics 365 Finance and Operations by posting to the SalesOrderLines entity. Use this tool when you need to add products, quantities, and pricing lines to an existing sales order header. This operation writes data to the system and is not easily reversible once downstream processes (e.g., reservation, picking) have started. Ensure the sales order header exists before calling this tool (use ms_d365fo_create_sales_order_header if needed). Not intended for updating existing lines or retrieving lines (use ms_d365fo_list_sales_order_lines).

        Args:
            ItemNumber: The product or item number (inventory item identifier) being referenced on the sales order. (required)
            OrderedSalesQuantity: The quantity ordered for the item on the sales order. (required)
            SalesOrderNumber: The identifier of the sales order in Dynamics 365 to which this line or update applies. (required)
            dataAreaId: The company (legal entity) identifier within Dynamics 365 Finance and Operations (often called dataAreaId). (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def ms_d365fo_delete_order_note(
        self,
        dataAreaId: str,
        documentId: str,
    ) -> Dict[str, Any]:
        """Permanently deletes a document attachment or note from a sales order header in Microsoft Dynamics 365 Finance and Operations, identified by dataAreaId and DocumentId. Use this tool only when you need to remove an existing order note or document attachment that is no longer relevant. This operation is irreversible — the deleted note or attachment cannot be recovered. Ensure the correct DocumentId is confirmed before calling this tool. Not intended for creating notes (use ms_d365fo_create_order_note_or_document_attachment) or reading notes (use ms_d365fo_list_sales_order_notes).

        Args:
            dataAreaId: The company or data area identifier within Microsoft Dynamics 365 Finance and Operations. (required)
            documentId: The unique identifier of the order note document to be deleted. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def ms_d365fo_get_category_active_status(
        self,
        filter: Optional[str] = None,
        select: Optional[str] = None,
        skip: Optional[str] = None,
        top: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Checks the active or inactive status of a product category from the EcoResCategoryBiEntities entity in Microsoft Dynamics 365 Finance and Operations. Use this tool when you need to verify whether a category is currently active before using it for product assignments or order processing. This is a read-only operation with no side effects. Not intended for retrieving the category hierarchy (use ms_d365fo_get_product_category_hierarchy) or category assignments (use ms_d365fo_get_product_category_assignment).

        Args:
            filter: OData filter query to limit the results returned by category active status.
            select: OData select query to specify which fields to include in the response.
            skip: Specifies the number of records to skip before returning results.
            top: Specifies the maximum number of records to return.
        Returns:
            API response as a dictionary.
        """
        ...

    def ms_d365fo_get_category_assignment_by_list_number(
        self,
        filter: Optional[str] = None,
        orderby: Optional[str] = None,
        select: Optional[str] = None,
        skip: Optional[str] = None,
        top: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Retrieves product category assignment records filtered by a specific list number from the ProductCategoryAssignments entity in Microsoft Dynamics 365 Finance and Operations. Use this tool when you need to identify which products or categories are associated with a given price or product list number. This is a read-only operation with no side effects. Not intended for filtering by product number (use ms_d365fo_get_category_assignment_by_product_number) or for discount category lookups (use ms_d365fo_get_discount_assignment_by_product_number).

        Args:
            filter: OData filter expression to filter the category assignments by specific criteria.
            orderby: OData order by clause to sort the category assignments by specified fields.
            select: OData select clause to specify which fields of the category assignments should be returned.
            skip: Number of category assignments to skip before starting to collect the result set.
            top: Limits the number of category assignments returned to the specified number.
        Returns:
            API response as a dictionary.
        """
        ...

    def ms_d365fo_get_category_assignment_by_product_number(
        self,
        filter: Optional[str] = None,
        orderby: Optional[str] = None,
        select: Optional[str] = None,
        skip: Optional[str] = None,
        top: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Retrieves product category assignment records filtered by a specific product number from the ProductCategoryAssignments entity in Microsoft Dynamics 365 Finance and Operations. Use this tool when you need to identify which categories a particular product number is assigned to. This is a read-only operation with no side effects. Not intended for filtering by list number (use ms_d365fo_get_category_assignment_by_list_number) or for discount-specific category lookups (use ms_d365fo_get_discount_assignment_by_product_number).

        Args:
            filter: OData filter expression to filter category assignments.
            orderby: Specifies the order in which records are returned.
            select: OData select expression to specify which fields to include in the response.
            skip: Skips the specified number of records.
            top: Limits the number of records returned.
        Returns:
            API response as a dictionary.
        """
        ...

    def ms_d365fo_get_customer_affiliation(
        self,
        crosscompany: Optional[str] = None,
        filter: Optional[str] = None,
        select: Optional[str] = None,
        skip: Optional[str] = None,
        top: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Retrieves customer affiliation records from the CustomerAffiliations entity in Microsoft Dynamics 365 Finance and Operations. Use this tool when you need to determine which retail affiliations or loyalty groups a customer belongs to. This is a read-only operation with no side effects. Not intended for price group lookups (use ms_d365fo_get_customer_price_group) or customer account details (use ms_d365fo_get_customer_by_party_number).

        Args:
            crosscompany: Specifies whether to include records across all companies within the organization.
            filter: OData filter expression to limit the results returned.
            select: Specify which fields to include in the response.
            skip: Number of records to skip from the start of the result set.
            top: Maximum number of records to return.
        Returns:
            API response as a dictionary.
        """
        ...

    def ms_d365fo_get_customer_aged_balance(
        self,
        crosscompany: Optional[str] = None,
        filter: Optional[str] = None,
        select: Optional[str] = None,
        skip: Optional[str] = None,
        top: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Retrieves aged balance details for a customer from the CustAgedBalances entity in Microsoft Dynamics 365 Finance and Operations. Use this tool when you need to view outstanding receivable amounts broken down by aging buckets (e.g., current, 30 days, 60 days) for credit or collections analysis. This is a read-only operation with no side effects. Not intended for individual customer transactions (use ms_d365fo_list_customer_transactions) or customer account details (use ms_d365fo_get_customer_by_party_number).

        Args:
            crosscompany: Specifies whether to include data across companies (true/false).
            filter: OData filter expression to filter the customer aged balances.
            select: OData select expression to specify which properties to include in the response.
            skip: Number of records to skip from the beginning of the result set.
            top: Number of records to return from the top of the result set.
        Returns:
            API response as a dictionary.
        """
        ...

    def ms_d365fo_get_customer_by_party_number(
        self,
        crosscompany: Optional[str] = None,
        filter: Optional[str] = None,
        skip: Optional[str] = None,
        top: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Retrieves customer account information from the CustomersV3 entity in Microsoft Dynamics 365 Finance and Operations using a party number as the lookup key. Use this tool when you have a known party number and need to retrieve the associated customer record. This is a read-only operation with no side effects. Not intended for retrieving all web-enabled customers (use ms_d365fo_list_web_enabled_customers) or for customer addresses (use ms_d365fo_list_customer_addresses).

        Args:
            crosscompany: Indicates whether the query should run across multiple legal entities/companies (typically true or false).
            filter: OData $filter expression to restrict the set of returned records (for example: Name eq 'ABC').
            skip: OData $skip value to offset the returned records for paging.
            top: OData $top value to limit the number of records returned.
        Returns:
            API response as a dictionary.
        """
        ...

    def ms_d365fo_get_customer_cash_discount(
        self,
        crosscompany: Optional[str] = None,
        filter: Optional[str] = None,
        select: Optional[str] = None,
        skip: Optional[str] = None,
        top: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Retrieves cash discount configuration records from the CashDiscounts entity in Microsoft Dynamics 365 Finance and Operations. Use this tool when you need to determine the early-payment discount terms available to a customer. This is a read-only operation with no side effects. Not intended for retrieving payment terms (use ms_d365fo_get_customer_payment_terms) or category-based discounts (use ms_d365fo_get_discount_category).

        Args:
            crosscompany: Indicates if the query should be executed across companies.
            filter: OData filter expression to narrow down the customer cash discount results.
            select: Specifies which fields to include in the response.
            skip: Number of records to skip from the start.
            top: Limits the number of records returned.
        Returns:
            API response as a dictionary.
        """
        ...

    def ms_d365fo_get_customer_packing_slip_journal(
        self,
        crosscompany: Optional[str] = None,
        filter: Optional[str] = None,
        select: Optional[str] = None,
        skip: Optional[str] = None,
        top: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Retrieves customer packing slip journal records from the CustPackingSlipJourBiEntities entity in Microsoft Dynamics 365 Finance and Operations. Use this tool when you need to access packing slip journal data for reporting or business intelligence purposes. This is a read-only operation with no side effects — it does not generate or post a new journal. Not intended for detailed packing slip export records (use ms_d365fo_get_packing_slip_details) or tracking information (use ms_d365fo_get_packing_slip_tracking_information).

        Args:
            crosscompany: Specifies whether the query should span multiple legal entities/companies. Typical values are 'true' or 'false'.
            filter: OData $filter expression to restrict the set of returned entities (e.g., status eq 'Active').
            select: OData $select expression to specify which properties to include in the response (comma-separated).
            skip: OData $skip value to offset the returned records for paging.
            top: OData $top value to limit the number of returned records.
        Returns:
            API response as a dictionary.
        """
        ...

    def ms_d365fo_get_customer_part_number_by_product(
        self,
        crosscompany: Optional[str] = None,
        filter: Optional[str] = None,
        select: Optional[str] = None,
        skip: Optional[str] = None,
        top: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Retrieves the customer-specific part number associated with an internal product from the CustomerProductDescriptionsV2 entity in Microsoft Dynamics 365 Finance and Operations. Use this tool when you need to translate an internal item number to a customers own product reference number for order processing or communication. This is a read-only operation with no side effects. Not intended for retrieving general product details (use ms_d365fo_get_product_details).

        Args:
            crosscompany: Indicates whether the query should include data from multiple companies.
            filter: OData filter expression to specify which records to retrieve.
            select: OData select expression to specify which fields to include in the response.
            skip: The number of records to skip before starting to return records.
            top: The number of records to return from the query.
        Returns:
            API response as a dictionary.
        """
        ...

    def ms_d365fo_get_customer_payment_terms(
        self,
        crosscompany: Optional[str] = None,
        filter: Optional[str] = None,
        select: Optional[str] = None,
        skip: Optional[str] = None,
        top: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Retrieves payment terms records from the PaymentTerms entity in Microsoft Dynamics 365 Finance and Operations. Use this tool when you need to look up the payment terms (e.g., Net 30, 2/10 Net 30) applicable to a customer or order. This is a read-only operation with no side effects. Not intended for cash discount details (use ms_d365fo_get_customer_cash_discount) or customer-level financial summaries.

        Args:
            crosscompany: Indicates whether to include data from multiple companies in the response.
            filter: OData filter expression to restrict the returned customer payment terms.
            select: OData select expression to specify which fields to include in the response.
            skip: Specifies the number of records to skip before returning results.
            top: Limits the number of records returned.
        Returns:
            API response as a dictionary.
        """
        ...

    def ms_d365fo_get_customer_price_group(
        self,
        crosscompany: Optional[str] = None,
        filter: Optional[str] = None,
        select: Optional[str] = None,
        skip: Optional[str] = None,
        top: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Retrieves customer price group details from the RetailAffiliationPriceGroups entity in Microsoft Dynamics 365 Finance and Operations. Use this tool when you need to identify which retail affiliation price group a customer belongs to for pricing calculations. This is a read-only operation with no side effects. Not intended for looking up the price group in the context of a specific product (use ms_d365fo_get_sales_price_by_sales_order) or for general customer affiliation data (use ms_d365fo_get_customer_affiliation).

        Args:
            crosscompany: Specifies whether to include data across legal entities (companies).
            filter: OData filter expression to limit the returned Customer Price Groups.
            select: OData select expression to define which fields to return.
            skip: Number of Customer Price Groups to skip before starting to collect the result set.
            top: Limits the number of Customer Price Groups returned.
        Returns:
            API response as a dictionary.
        """
        ...

    def ms_d365fo_get_discount_assignment_by_product_number(
        self,
        filter: Optional[str] = None,
        select: Optional[str] = None,
        skip: Optional[str] = None,
        top: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Retrieves product category assignment records filtered by product number to identify discount-relevant category assignments in Microsoft Dynamics 365 Finance and Operations. Use this tool when you need to determine which discount categories a specific product number belongs to. This is a read-only operation with no side effects. Not intended for retrieving discount categories without a product filter (use ms_d365fo_get_discount_category) or for general category assignments (use ms_d365fo_get_product_category_assignment).

        Args:
            filter: OData filter query to specify which discount assignments to retrieve.
            select: Comma-separated list of fields to include in the response.
            skip: Number of records to skip before starting to return results.
            top: Number of records to return from the top of the result set.
        Returns:
            API response as a dictionary.
        """
        ...

    def ms_d365fo_get_discount_category(
        self,
        filter: Optional[str] = None,
        select: Optional[str] = None,
        skip: Optional[str] = None,
        top: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Retrieves product category records used for discount configuration from the ProductCategories entity in Microsoft Dynamics 365 Finance and Operations. Use this tool when you need to identify which product categories are associated with discount structures. This is a read-only operation with no side effects. Not intended for retrieving discount assignments by product number (use ms_d365fo_get_discount_assignment_by_product_number) or for the full category hierarchy (use ms_d365fo_get_product_category_hierarchy).

        Args:
            filter: OData filter expression to limit the returned discount categories.
            select: OData select expression to specify which properties should be included in the response.
            skip: Specifies the number of records to skip before starting to return results.
            top: Specifies the number of records to return from the top of the collection.
        Returns:
            API response as a dictionary.
        """
        ...

    def ms_d365fo_get_invoice_to_shipment_mapping(
        self,
        crosscompany: Optional[str] = None,
        filter: Optional[str] = None,
        select: Optional[str] = None,
        skip: Optional[str] = None,
        top: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Retrieves the mapping between invoices and their associated shipment records from the EDIInvoiceShipmentLists entity in Microsoft Dynamics 365 Finance and Operations. Use this tool when you need to determine which shipments correspond to a given invoice or vice versa. This is a read-only operation with no side effects. Not intended for retrieving full shipment details (use ms_d365fo_get_shipment_details) or invoice lines (use ms_d365fo_list_invoice_lines).

        Args:
            crosscompany: Indicates whether to include data across multiple companies.
            filter: Expression used to filter the data returned by the query.
            select: Specifies which properties to include in the response.
            skip: Number of records to skip before returning results.
            top: Limits the number of records returned.
        Returns:
            API response as a dictionary.
        """
        ...

    def ms_d365fo_get_invoiced_customer_details(
        self,
        crosscompany: Optional[str] = None,
        filter: Optional[str] = None,
        select: Optional[str] = None,
        skip: Optional[str] = None,
        top: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Retrieves customer details for invoiced customers from the Customers entity in Microsoft Dynamics 365 Finance and Operations. Use this tool when you need customer account information in the context of invoicing, such as account number, name, or billing details. This is a read-only operation with no side effects. Not intended for looking up customers by party number (use ms_d365fo_get_customer_by_party_number) or for retrieving all web-enabled customers (use ms_d365fo_list_web_enabled_customers).

        Args:
            crosscompany: Indicates whether to query data across multiple companies.
            filter: OData filter expression to specify criteria for invoiced customer details.
            select: OData select statement to specify which fields to retrieve.
            skip: Specifies the number of records to skip from the start of the result set for pagination.
            top: Specifies the maximum number of invoiced customer records to return.
        Returns:
            API response as a dictionary.
        """
        ...

    def ms_d365fo_get_order_coupon_usage(
        self,
        crosscompany: Optional[str] = None,
        filter: Optional[str] = None,
        select: Optional[str] = None,
        skip: Optional[str] = None,
        top: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Retrieves coupon usage records for orders from the CouponUsages entity in Microsoft Dynamics 365 Finance and Operations. Use this tool when you need to check which coupons have been applied to orders and their usage details. This is a read-only operation with no side effects. Not intended for creating coupon usage entries (use ms_d365fo_create_coupon_usage) or for retrieving order line charges (use ms_d365fo_list_order_line_charges).

        Args:
            crosscompany: Indicates whether the query should include data across companies.
            filter: OData filter expression to specify which data to retrieve.
            select: OData select expression to specify which fields to include in the response.
            skip: Skips the specified number of records before starting to return results.
            top: Limits the number of records to return.
        Returns:
            API response as a dictionary.
        """
        ...

    def ms_d365fo_get_packing_slip_details(
        self,
        crosscompany: Optional[str] = None,
        filter: Optional[str] = None,
        select: Optional[str] = None,
        skip: Optional[str] = None,
        top: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Retrieves detailed packing slip records from the rsmITTCustPackingSlipJournalExport entity in Microsoft Dynamics 365 Finance and Operations. Use this tool when you need exported packing slip data for customer shipments, including line-level detail. This is a read-only operation with no side effects. Note: this tool shares the same endpoint as ms_d365fo_get_packing_slip_details (ActionID: get-packing-slip-details); prefer this tool for export-oriented packing slip data. Not intended for tracking information (use ms_d365fo_get_packing_slip_tracking_information) or journal summaries (use ms_d365fo_get_packing_slip_journal).

        Args:
            crosscompany: Specify if the query should be executed across multiple companies.
            filter: OData filter expression to specify which packing slip details to return.
            select: Fields to include in the response.
            skip: Number of records to skip before starting to return results.
            top: Limits the number of records returned.
        Returns:
            API response as a dictionary.
        """
        ...

    def ms_d365fo_get_packing_slip_journal(
        self,
        crosscompany: Optional[str] = None,
        filter: Optional[str] = None,
        select: Optional[str] = None,
        skip: Optional[str] = None,
        top: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Retrieves packing slip journal records from the CustPackingSlipJourBiEntities entity in Microsoft Dynamics 365 Finance and Operations. Use this tool when you need summary-level packing slip journal data for business intelligence or reporting purposes. This is a read-only operation with no side effects. Not intended for detailed packing slip export records (use ms_d365fo_get_packing_slip_details) or tracking information (use ms_d365fo_get_packing_slip_tracking_information).

        Args:
            crosscompany: Indicates if the query should include data across legal entities.
            filter: OData filter expression to filter packing slip journals.
            select: OData select expression to specify which properties to include.
            skip: Number of records to skip for pagination.
            top: Number of records to return from the top of the result set.
        Returns:
            API response as a dictionary.
        """
        ...

    def ms_d365fo_get_packing_slip_tracking_information(
        self,
        crosscompany: Optional[str] = None,
        filter: Optional[str] = None,
        select: Optional[str] = None,
        skip: Optional[str] = None,
        top: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Retrieves shipment tracking information associated with packing slips from the PackingSlipTrackingInformation entity in Microsoft Dynamics 365 Finance and Operations. Use this tool when you need to look up carrier tracking details or shipment status linked to a packing slip. This is a read-only operation with no side effects. Not intended for retrieving full packing slip details or journal records (use ms_d365fo_get_packing_slip_details or ms_d365fo_get_packing_slip_journal for those).

        Args:
            crosscompany: Indicates if the query applies across multiple companies.
            filter: OData filter expression to limit the records returned.
            select: OData select expression to specify which fields to return.
            skip: Number of records to skip in the result set.
            top: Number of records to return from the top of the collection.
        Returns:
            API response as a dictionary.
        """
        ...

    def ms_d365fo_get_product(
        self,
        filter: Optional[str] = None,
        select: Optional[str] = None,
        skip: Optional[str] = None,
        top: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Retrieves base product information from the ProductsV2 entity in Microsoft Dynamics 365 Finance and Operations. Use this tool when you need core product master data such as product number, product type, and product name, without release-specific or pricing context. This is a read-only operation with no side effects. Not intended for released product details with pricing (use ms_d365fo_get_released_product_details_with_pricing) or engineering attributes (use ms_d365fo_get_product_engineering_attributes).

        Args:
            filter: OData filter expression to specify which products to retrieve.
            select: Comma-separated list of product properties to include in the response.
            skip: Number of products to skip for pagination purposes.
            top: Limits the number of products returned by the query.
        Returns:
            API response as a dictionary.
        """
        ...

    def ms_d365fo_get_product_category_assignment(
        self,
        filter: Optional[str] = None,
        select: Optional[str] = None,
        skip: Optional[str] = None,
        top: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Retrieves product category assignment records from the ProductCategoryAssignments entity in Microsoft Dynamics 365 Finance and Operations. Use this tool when you need to determine which categories a product is assigned to. This is a read-only operation with no side effects. Not intended for retrieving the category hierarchy structure (use ms_d365fo_get_product_category_hierarchy) or for filtering assignments by a specific product number or list number (use ms_d365fo_get_category_assignment_by_product_number or ms_d365fo_get_category_assignment_by_list_number).

        Args:
            filter: OData filter expression to filter the product category assignments.
            select: Specify which fields to return in the response.
            skip: Number of records to skip for pagination.
            top: Number of records to return from the top of the result set.
        Returns:
            API response as a dictionary.
        """
        ...

    def ms_d365fo_get_product_category_hierarchy(
        self,
        filter: Optional[str] = None,
        orderby: Optional[str] = None,
        select: Optional[str] = None,
        skip: Optional[str] = None,
        top: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Retrieves the product category hierarchy from the ProductCategories entity in Microsoft Dynamics 365 Finance and Operations. Use this tool when you need to understand the parent-child structure of product categories, or browse the full category tree. This is a read-only operation with no side effects. Not intended for retrieving category assignments for specific products (use ms_d365fo_get_category_assignment_by_product_number) or checking category active status (use ms_d365fo_get_category_active_status).

        Args:
            filter: Filters to apply on the product category hierarchy.
            orderby: Specifies the order of the results.
            select: Comma-separated list of properties to include in the response.
            skip: Specifies the number of results to skip.
            top: Limits the number of results returned.
        Returns:
            API response as a dictionary.
        """
        ...

    def ms_d365fo_get_product_details(
        self,
        crosscompany: Optional[str] = None,
        filter: Optional[str] = None,
        select: Optional[str] = None,
        skip: Optional[str] = None,
        top: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Retrieves detailed information for a released product from the ReleasedProductsV2 entity in Microsoft Dynamics 365 Finance and Operations. Use this tool when you need comprehensive product attributes such as item number, unit of measure, item group, and storage dimensions for a released product. This is a read-only operation with no side effects. Not intended for base product records without release context (use ms_d365fo_get_product) or for engineering attributes (use ms_d365fo_get_product_engineering_attributes).

        Args:
            crosscompany: Specifies if the query should cross company boundaries.
            filter: OData filter expression to narrow down the product results.
            select: Comma-separated list of fields to include in the response.
            skip: Number of products to skip before starting to collect the result set.
            top: Limits the number of products returned.
        Returns:
            API response as a dictionary.
        """
        ...

    def ms_d365fo_get_product_engineering_attributes(
        self,
        crosscompany: Optional[str] = None,
        filter: Optional[str] = None,
        select: Optional[str] = None,
        skip: Optional[str] = None,
        top: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Retrieves engineering attribute values for released product versions from the ReleasedEngineeringProductVersionAttributeValues entity in Microsoft Dynamics 365 Finance and Operations. Use this tool when you need technical or engineering specification attributes tied to a versioned released product. This is a read-only operation with no side effects. Not intended for standard product details (use ms_d365fo_get_product_details) or order settings (use ms_d365fo_get_product_order_settings).

        Args:
            crosscompany: Indicator to include records from all companies.
            filter: OData filter expression to restrict the results returned.
            select: Comma-separated list of fields to include in the response.
            skip: Number of records to skip for paging.
            top: Limits the number of records returned.
        Returns:
            API response as a dictionary.
        """
        ...

    def ms_d365fo_get_product_order_settings(
        self,
        crosscompany: Optional[str] = None,
        filter: Optional[str] = None,
        select: Optional[str] = None,
        skip: Optional[str] = None,
        top: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Retrieves product-specific order settings from the ProductSpecificOrderSettingsV3 entity in Microsoft Dynamics 365 Finance and Operations. Use this tool when you need to check order quantity constraints, lead times, or other order-level configuration for a specific product. This is a read-only operation with no side effects. Not intended for product pricing (use ms_d365fo_get_released_product_details_with_pricing) or product engineering attributes (use ms_d365fo_get_product_engineering_attributes).

        Args:
            crosscompany: Indicates whether to include data across legal entities.
            filter: OData filter expression to limit the set of product order settings returned.
            select: OData select expression to specify which properties to return.
            skip: Number of product order settings to skip before starting to collect the result set.
            top: Limits the number of product order settings returned.
        Returns:
            API response as a dictionary.
        """
        ...

    def ms_d365fo_get_released_product_details_with_pricing(
        self,
        crosscompany: Optional[str] = None,
        filter: Optional[str] = None,
        select: Optional[str] = None,
        skip: Optional[str] = None,
        top: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Retrieves detailed information about released products including pricing data from the ReleasedProductsV2 entity in Microsoft Dynamics 365 Finance and Operations. Use this tool when you need product specifications and associated pricing for a released product. This is a read-only operation with no side effects. Not intended for retrieving base product records without pricing (use ms_d365fo_get_product for that) or for product engineering attributes.

        Args:
            crosscompany: Indicates whether to cross company boundaries when retrieving data.
            filter: OData filter expression to restrict the released product results.
            select: OData select expression to specify which fields to include in the response.
            skip: Number of released product records to skip for pagination.
            top: Specifies the maximum number of released product records to retrieve.
        Returns:
            API response as a dictionary.
        """
        ...

    def ms_d365fo_get_sales_order(
        self,
        crosscompany: Optional[str] = None,
        filter: Optional[str] = None,
        skip: Optional[str] = None,
        top: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Retrieves the header details for a specific sales order from the SalesOrderHeadersV3 entity in Microsoft Dynamics 365 Finance and Operations. Use this tool when you need to look up the details of a single, known sales order by its identifier. This is a read-only operation with no side effects. Not intended for listing all sales orders (use ms_d365fo_list_sales_orders), retrieving sales order lines (use ms_d365fo_list_sales_order_lines), or order notes (use ms_d365fo_list_sales_order_notes).

        Args:
            crosscompany: Indicates whether to include data from multiple companies.
            filter: OData filter expression to specify which sales orders to retrieve.
            skip: Number of sales orders to skip before starting to collect the result set.
            top: Limits the number of sales orders returned.
        Returns:
            API response as a dictionary.
        """
        ...

    def ms_d365fo_get_sales_price_by_sales_order(
        self,
        crosscompany: Optional[str] = None,
        expand: Optional[str] = None,
        filter: Optional[str] = None,
        select: Optional[str] = None,
        skip: Optional[str] = None,
        top: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Looks up the sales price for a sales order by querying sales order headers in Microsoft Dynamics 365 Finance and Operations. Use this tool when you need to retrieve pricing information associated with a specific sales order header from the SalesOrderHeadersV3 entity. This is a read-only operation with no side effects. Not intended for retrieving individual product prices outside the context of a sales order header, or for listing all sales orders (use ms_d365fo_list_sales_orders for that).

        Args:
            crosscompany: Specifies whether to query across companies.
            expand: OData expand expression to include related entities.
            filter: OData filter expression to limit the results.
            select: OData select expression to define which fields to return.
            skip: Number of results to skip before returning data.
            top: Limits the number of results returned.
        Returns:
            API response as a dictionary.
        """
        ...

    def ms_d365fo_get_shipment_details(
        self,
        crosscompany: Optional[str] = None,
        filter: Optional[str] = None,
        select: Optional[str] = None,
        skip: Optional[str] = None,
        top: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Retrieves shipment details from the EDICUMEWHSShipments entity in Microsoft Dynamics 365 Finance and Operations. Use this tool when you need to retrieve warehouse shipment records, including status and related EDI shipment data. This is a read-only operation with no side effects. Not intended for invoice-to-shipment mapping (use ms_d365fo_get_invoice_to_shipment_mapping) or packing slip tracking (use ms_d365fo_get_packing_slip_tracking_information).

        Args:
            crosscompany: Indicates whether the query should run across companies (typically 'true' or 'false').
            filter: OData $filter expression to narrow down the returned records (e.g., Status eq 'Active').
            select: OData $select expression specifying which fields to return (comma-separated list).
            skip: OData $skip value to offset the returned records for paging.
            top: OData $top value to limit the number of returned records.
        Returns:
            API response as a dictionary.
        """
        ...

    def ms_d365fo_get_third_party_delivery_address(
        self,
        crosscompany: Optional[str] = None,
        filter: Optional[str] = None,
        select: Optional[str] = None,
        skip: Optional[str] = None,
        top: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Retrieves the postal delivery address for a third-party party from the PartyLocationPostalAddressesV2 entity in Microsoft Dynamics 365 Finance and Operations. Use this tool when you need to look up a delivery address belonging to a third-party entity (not the primary customer). This is a read-only operation with no side effects. Not intended for retrieving customer addresses (use ms_d365fo_list_customer_addresses) or for updating addresses (use ms_d365fo_update_customer_address).

        Args:
            crosscompany: Flag to indicate if the query should cross company boundaries.
            filter: OData filter expression to filter the third-party delivery addresses returned.
            select: OData select expression to specify which fields to retrieve.
            skip: Specifies the number of records to skip.
            top: Limits the number of records returned.
        Returns:
            API response as a dictionary.
        """
        ...

    def ms_d365fo_get_warehouse_on_hand_stock(
        self,
        crosscompany: Optional[str] = None,
        filter: Optional[str] = None,
        select: Optional[str] = None,
        skip: Optional[str] = None,
        top: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Retrieves on-hand inventory stock levels for warehouses from the WarehousesOnHandV2 entity in Microsoft Dynamics 365 Finance and Operations. Use this tool when you need to check current stock availability across one or more warehouses for order fulfillment or inventory planning. This is a read-only operation with no side effects. Not intended for product details or pricing; use ms_d365fo_get_product_details for those.

        Args:
            crosscompany: Indicates whether to include data from multiple companies when querying inventory.
            filter: OData filter expression to specify which warehouse on-hand stock records to retrieve.
            select: OData select expression to specify which fields to include in the response.
            skip: The number of records to skip before starting to return results.
            top: The maximum number of records to return.
        Returns:
            API response as a dictionary.
        """
        ...

    def ms_d365fo_list_all_categories(
        self,
        filter: Optional[str] = None,
        orderby: Optional[str] = None,
        select: Optional[str] = None,
        skip: Optional[str] = None,
        top: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Retrieves all product category records from the ProductCategories entity in Microsoft Dynamics 365 Finance and Operations. Use this tool when you need a complete list of product categories for browsing, reporting, or validation. This is a read-only operation with no side effects. Not intended for category assignments (use ms_d365fo_get_product_category_assignment) or category active status (use ms_d365fo_get_category_active_status).

        Args:
            filter: OData filter expression to filter the categories returned.
            orderby: OData orderby expression to sort the categories.
            select: OData select expression to specify which fields to include in the response.
            skip: Number of categories to skip before starting to collect the result set.
            top: Specifies the maximum number of categories to return.
        Returns:
            API response as a dictionary.
        """
        ...

    def ms_d365fo_list_categories(
        self,
        filter: Optional[str] = None,
        orderby: Optional[str] = None,
        select: Optional[str] = None,
        skip: Optional[str] = None,
        top: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Retrieves a list of product category assignments from the ProductCategoryAssignments entity in Microsoft Dynamics 365 Finance and Operations. Use this tool when you need to enumerate all category assignment records without filtering by product or list number. This is a read-only operation with no side effects. Not intended for filtering by product number (use ms_d365fo_get_category_assignment_by_product_number) or list number (use ms_d365fo_get_category_assignment_by_list_number), or for retrieving the full category hierarchy (use ms_d365fo_get_product_category_hierarchy).

        Args:
            filter: OData filter expression to limit the categories returned.
            orderby: Specifies the order in which to return the categories.
            select: Comma-separated list of fields to include in the response.
            skip: Number of categories to skip when returning results.
            top: Limits the number of categories returned.
        Returns:
            API response as a dictionary.
        """
        ...

    def ms_d365fo_list_customer_address_contacts(
        self,
        crosscompany: Optional[str] = None,
        filter: Optional[str] = None,
        select: Optional[str] = None,
        skip: Optional[str] = None,
        top: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Retrieves electronic contact records (such as email addresses and phone numbers) associated with customer postal addresses from the PostalAddressElectronicContactsV2 entity in Microsoft Dynamics 365 Finance and Operations. Use this tool when you need to look up contact details linked to a specific customer address location. This is a read-only operation with no side effects. Not intended for retrieving postal address records themselves (use ms_d365fo_list_customer_addresses) or customer account information (use ms_d365fo_get_customer_by_party_number).

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

    def ms_d365fo_list_customer_addresses(
        self,
        filter: Optional[str] = None,
        select: Optional[str] = None,
        skip: Optional[str] = None,
        top: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Retrieves postal address records for customers from the PartyLocationPostalAddressesV2 entity in Microsoft Dynamics 365 Finance and Operations. Use this tool when you need to list all addresses associated with a customer party. This is a read-only operation with no side effects. Not intended for updating addresses (use ms_d365fo_update_customer_address), creating addresses (use ms_d365fo_create_customer_address), or retrieving third-party delivery addresses (use ms_d365fo_get_third_party_delivery_address).

        Args:
            filter: OData filter expression to limit the customer addresses returned.
            select: Specifies which fields to include in the response for customer addresses.
            skip: Number of customer addresses to skip for paging.
            top: Limits the number of customer addresses returned.
        Returns:
            API response as a dictionary.
        """
        ...

    def ms_d365fo_list_customer_transactions(
        self,
        crosscompany: Optional[str] = None,
        filter: Optional[str] = None,
        select: Optional[str] = None,
        skip: Optional[str] = None,
        top: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Retrieves customer transaction records from the CustTransactions entity in Microsoft Dynamics 365 Finance and Operations. Use this tool when you need to view open or closed financial transactions for a customer, such as invoices, payments, and credit notes. This is a read-only operation with no side effects. Not intended for customer aged balances (use ms_d365fo_get_customer_aged_balance) or customer details (use ms_d365fo_get_invoiced_customer_details).

        Args:
            crosscompany: Indicates whether to include transactions across all companies.
            filter: OData filter expression to limit the customer transactions returned.
            select: OData select expression specifying properties to include in the results.
            skip: Specifies the number of customer transactions to skip before starting to return results.
            top: Specifies the maximum number of customer transactions to retrieve.
        Returns:
            API response as a dictionary.
        """
        ...

    def ms_d365fo_list_delivery_modes(
        self,
        crosscompany: Optional[str] = None,
        filter: Optional[str] = None,
        select: Optional[str] = None,
        skip: Optional[str] = None,
        top: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Retrieves delivery mode records from the DeliveryModesV2 entity in Microsoft Dynamics 365 Finance and Operations. Use this tool when you need a list of configured delivery modes (e.g., truck, air, parcel) for order configuration. This is a read-only operation with no side effects. Not intended for delivery terms (use ms_d365fo_list_delivery_terms) or shipment methods by channel (use ms_d365fo_list_shipment_methods). Note: this tool shares the same endpoint as the ms_d365fo_list_delivery_modes_alt tool; prefer this tool for general delivery mode lookups.

        Args:
            crosscompany: Specify whether to include data from multiple companies (true/false).
            filter: OData filter expression to restrict the delivery modes returned.
            select: OData select statement to specify which properties to include in the response.
            skip: Number of delivery mode records to skip before retrieving the remaining.
            top: Limits the number of delivery mode records returned.
        Returns:
            API response as a dictionary.
        """
        ...

    def ms_d365fo_list_delivery_modes_alt(
        self,
        crosscompany: Optional[str] = None,
        filter: Optional[str] = None,
        select: Optional[str] = None,
        skip: Optional[str] = None,
        top: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Retrieves available delivery mode records from the DeliveryModesV2 entity in Microsoft Dynamics 365 Finance and Operations. Use this tool when you need to enumerate configured delivery modes for order setup. This is a read-only operation with no side effects. Note: this tool shares the same endpoint as ms_d365fo_list_delivery_modes; prefer ms_d365fo_list_delivery_modes for standard delivery mode lookups. Not intended for delivery terms (use ms_d365fo_list_delivery_terms) or channel-level shipment methods (use ms_d365fo_list_shipment_methods).

        Args:
            crosscompany: Indicates whether to include data across companies.
            filter: OData filter expression to filter the delivery modes.
            select: OData select statement specifying which fields to return.
            skip: Number of records to skip in the result set.
            top: Limits the number of records returned by the query.
        Returns:
            API response as a dictionary.
        """
        ...

    def ms_d365fo_list_delivery_terms(
        self,
        crosscompany: Optional[str] = None,
        filter: Optional[str] = None,
        skip: Optional[str] = None,
        top: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Retrieves all delivery terms records from the DeliveryTerms entity in Microsoft Dynamics 365 Finance and Operations. Use this tool when you need to list available delivery terms (e.g., EXW, CIF, DDP) for order configuration or validation. This is a read-only operation with no side effects. Not intended for delivery modes (use ms_d365fo_list_delivery_modes) or shipment methods (use ms_d365fo_list_shipment_methods).

        Args:
            crosscompany: Indicates whether to include data across all companies or only the current one.
            filter: OData filter expression to limit the results returned by the Delivery Terms query.
            skip: Specifies the number of records to skip before starting to return results.
            top: Specifies the maximum number of records to return from the Delivery Terms.
        Returns:
            API response as a dictionary.
        """
        ...

    def ms_d365fo_list_invoice_lines(
        self,
        crosscompany: Optional[str] = None,
        filter: Optional[str] = None,
        select: Optional[str] = None,
        skip: Optional[str] = None,
        top: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Retrieves sales invoice line items from the SalesInvoiceLines entity in Microsoft Dynamics 365 Finance and Operations. Use this tool when you need the individual line details of a sales invoice, such as item numbers, quantities, unit prices, and amounts. This is a read-only operation with no side effects. Not intended for invoice headers (use ms_d365fo_list_sales_invoices) or for invoice-to-shipment mapping (use ms_d365fo_list_invoice_shipments).

        Args:
            crosscompany: Indicates whether to include data across legal entities.
            filter: OData filter expression to limit the invoice lines returned.
            select: OData select expression to specify the fields to return.
            skip: Number of invoice lines to skip before starting to collect the result set.
            top: Number of invoice lines to return from the top of the collection.
        Returns:
            API response as a dictionary.
        """
        ...

    def ms_d365fo_list_invoice_shipments(
        self,
        crosscompany: Optional[str] = None,
        filter: Optional[str] = None,
        select: Optional[str] = None,
        skip: Optional[str] = None,
        top: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Retrieves invoice-to-shipment mapping records from the EDIInvoiceShipmentLists entity in Microsoft Dynamics 365 Finance and Operations. Use this tool when you need to list all shipment records linked to invoices for EDI or fulfillment reconciliation purposes. This is a read-only operation with no side effects. Not intended for full shipment details (use ms_d365fo_get_shipment_details) or invoice line items (use ms_d365fo_list_invoice_lines).

        Args:
            crosscompany: Indicates whether to include data across multiple legal entities.
            filter: OData filter expression to limit invoice shipments returned.
            select: OData select expression specifying which fields to include in the response.
            skip: The number of records to skip before starting to return results.
            top: The number of records to return from the top of the result set.
        Returns:
            API response as a dictionary.
        """
        ...

    def ms_d365fo_list_order_line_charges(
        self,
        crosscompany: Optional[str] = None,
        filter: Optional[str] = None,
        select: Optional[str] = None,
        skip: Optional[str] = None,
        top: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Retrieves charge records applied to sales order lines from the EDISalesOrderLineCharges entity in Microsoft Dynamics 365 Finance and Operations. Use this tool when you need to identify surcharges, fees, or other charges associated with individual order lines. This is a read-only operation with no side effects. Not intended for order header-level charges or coupon usage (use ms_d365fo_get_order_coupon_usage).

        Args:
            crosscompany: Specify whether to include data across multiple companies.
            filter: OData filter expression to filter the order line charges results.
            select: OData select expression to specify which fields to include in the response.
            skip: The number of records to skip before returning results.
            top: The number of records to return from the top of the result set.
        Returns:
            API response as a dictionary.
        """
        ...

    def ms_d365fo_list_sales_invoices(
        self,
        crosscompany: Optional[str] = None,
        filter: Optional[str] = None,
        select: Optional[str] = None,
        skip: Optional[str] = None,
        top: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Retrieves all sales invoice headers from the SalesInvoiceHeadersV2 entity in Microsoft Dynamics 365 Finance and Operations. Use this tool when you need to enumerate or review sales invoices for reporting, reconciliation, or lookup purposes. This is a read-only operation with no side effects. Not intended for invoice line items (use ms_d365fo_list_invoice_lines) or invoice-to-shipment mapping (use ms_d365fo_list_invoice_shipments).

        Args:
            crosscompany: Indicates whether to query across companies.
            filter: OData filter expression to filter sales invoices.
            select: OData select expression to specify which fields to include.
            skip: Number of sales invoices to skip in the result set.
            top: Maximum number of sales invoices to return.
        Returns:
            API response as a dictionary.
        """
        ...

    def ms_d365fo_list_sales_order_lines(
        self,
        crosscompany: Optional[str] = None,
        filter: Optional[str] = None,
        select: Optional[str] = None,
        skip: Optional[str] = None,
        top: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Retrieves the line items for sales orders from the SalesOrderLines entity in Microsoft Dynamics 365 Finance and Operations. Use this tool when you need the individual product lines, quantities, and pricing associated with sales orders. This is a read-only operation with no side effects. Not intended for retrieving the sales order header (use ms_d365fo_get_sales_order) or creating sales order lines (use ms_d365fo_create_sales_order_lines).

        Args:
            crosscompany: Indicates whether to include records across all companies in the organization.
            filter: OData filter expression to specify which sales order lines to retrieve.
            select: Comma-separated list of properties to include in the response.
            skip: Number of sales order line records to skip for pagination.
            top: Limits the number of sales order line records returned.
        Returns:
            API response as a dictionary.
        """
        ...

    def ms_d365fo_list_sales_order_notes(
        self,
        crosscompany: Optional[str] = None,
        filter: Optional[str] = None,
        select: Optional[str] = None,
        skip: Optional[str] = None,
        top: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Retrieves document attachments and notes associated with sales order headers from the SalesOrderHeaderDocumentAttachments entity in Microsoft Dynamics 365 Finance and Operations. Use this tool when you need to view all notes or attached documents for a sales order. This is a read-only operation with no side effects. Not intended for creating notes (use ms_d365fo_create_order_note_or_document_attachment) or deleting notes (use ms_d365fo_delete_order_note).

        Args:
            crosscompany: Indicates whether to include data across all legal entities (companies).
            filter: An OData filter expression to filter the sales order notes.
            select: Select specific fields to be returned in the response.
            skip: Skips a specified number of records in the result set.
            top: Limits the number of records returned.
        Returns:
            API response as a dictionary.
        """
        ...

    def ms_d365fo_list_sales_orders(
        self,
        crosscompany: Optional[str] = None,
        filter: Optional[str] = None,
        select: Optional[str] = None,
        skip: Optional[str] = None,
        top: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Retrieves all sales order headers from the SalesOrderHeadersV3 entity in Microsoft Dynamics 365 Finance and Operations. Use this tool when you need to enumerate or search across sales orders, such as for reporting or bulk processing. This is a read-only operation with no side effects. Not intended for retrieving a single specific sales order (use ms_d365fo_get_sales_order) or sales order line items (use ms_d365fo_list_sales_order_lines).

        Args:
            crosscompany: Specify whether to include sales orders across all legal entities.
            filter: OData filter expression to filter the sales orders returned.
            select: OData select expression to specify which fields of the sales orders to return.
            skip: Specifies the number of sales order records to skip before returning results.
            top: Specifies the number of sales order records to return.
        Returns:
            API response as a dictionary.
        """
        ...

    def ms_d365fo_list_sales_orders_v2(
        self,
        crosscompany: Optional[str] = None,
        expand: Optional[str] = None,
        filter: Optional[str] = None,
        select: Optional[str] = None,
        skip: Optional[str] = None,
        top: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Retrieves all sales order headers from the SalesOrderHeadersV3 entity in Microsoft Dynamics 365 Finance and Operations. Use this tool when you need to enumerate or search across sales orders for reporting or bulk processing. This is a read-only operation with no side effects. Note: this tool is functionally equivalent to ms_d365fo_list_sales_orders and targets the same endpoint; prefer ms_d365fo_list_sales_orders unless this specific instance is required. Not intended for a single specific sales order (use ms_d365fo_get_sales_order) or sales order lines (use ms_d365fo_list_sales_order_lines).

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

    def ms_d365fo_list_shipment_methods(
        self,
        crosscompany: Optional[str] = None,
        filter: Optional[str] = None,
        select: Optional[str] = None,
        skip: Optional[str] = None,
        top: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Retrieves the list of available shipment methods (delivery mode channel lines) configured in Microsoft Dynamics 365 Finance and Operations. Use this tool when you need to present or validate shipping method options for a sales order or channel. Returns a collection of records from the DeliveryModeChannelLines entity. This is a read-only operation with no side effects. Not intended for retrieving delivery terms or delivery modes from DeliveryModesV2 (use ms_d365fo_list_delivery_modes for those).

        Args:
            crosscompany: Indicates if the query should apply across companies.
            filter: OData filter expression to limit the shipment methods returned.
            select: Comma-separated list of properties to include in the response.
            skip: Number of shipment methods to skip before returning results.
            top: Limits the number of shipment methods returned.
        Returns:
            API response as a dictionary.
        """
        ...

    def ms_d365fo_list_web_enabled_customers(
        self,
        crosscompany: Optional[str] = None,
        filter: Optional[str] = None,
        select: Optional[str] = None,
        skip: Optional[str] = None,
        top: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Retrieves all customer accounts that are enabled for web (e-commerce or portal) access from the CustomersV3 entity in Microsoft Dynamics 365 Finance and Operations. Use this tool when you need to enumerate customers with web access for portal management or synchronization tasks. This is a read-only operation with no side effects. Not intended for looking up a specific customer by party number (use ms_d365fo_get_customer_by_party_number) or for all customers regardless of web status.

        Args:
            crosscompany: Indicates whether to query data across companies (true or false).
            filter: OData filter expression to filter the customers returned.
            select: OData select expression to specify which properties to include in the response.
            skip: Number of records to skip for paging.
            top: Limits the number of records returned.
        Returns:
            API response as a dictionary.
        """
        ...

    def ms_d365fo_lookup_customer_price_group(
        self,
        crosscompany: Optional[str] = None,
        filter: Optional[str] = None,
        select: Optional[str] = None,
        skip: Optional[str] = None,
        top: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Looks up customer price group information from the RetailAffiliationPriceGroups entity in Microsoft Dynamics 365 Finance and Operations. Use this tool when you need to identify the retail affiliation price group for a customer to apply correct pricing. This is a read-only operation with no side effects. Not intended for retrieving price groups already known via ms_d365fo_get_customer_price_group — this tool is functionally equivalent and may be consolidated.

        Args:
            crosscompany: Indicates whether the query should run across multiple legal entities/companies (commonly 'true' or 'false').
            filter: OData $filter expression to restrict which records are returned (e.g., Status eq 'Active').
            select: OData $select expression specifying which fields to include in the response (comma-separated).
            skip: OData $skip value to skip a number of records (used for paging).
            top: OData $top value to limit the number of records returned.
        Returns:
            API response as a dictionary.
        """
        ...

    def ms_d365fo_update_customer_address(
        self,
        LocationId: str,
        PartyNumber: str,
        locationId: str,
        partyNumber: str,
        validFrom: str,
        City: Optional[str] = None,
        CountryRegionISOCode: Optional[str] = None,
        IsRoleDelivery: Optional[str] = None,
        Roles: Optional[str] = None,
        State: Optional[str] = None,
        Street: Optional[str] = None,
        ZipCode: Optional[str] = None,
        rsmWebActive: Optional[bool] = None,
    ) -> Dict[str, Any]:
        """Updates an existing postal address record for a customer party in Microsoft Dynamics 365 Finance and Operations. Use this tool when you need to modify address fields (such as street, city, postal code, or country) for a known party and location combination, identified by PartyNumber, LocationId, and ValidFrom. This tool partially updates the record using PATCH — only the fields provided in the request body are changed; other fields are left unchanged. This is a destructive write operation; incorrect updates to address data may affect order fulfillment, invoicing, and shipping. Not intended for creating new addresses (use ms_d365fo_create_customer_address instead) or for reading address data.

        Args:
            LocationId: Identifier of the location associated with this body payload (matches the locationId used in the URL when applicable). (required)
            PartyNumber: The party identifier for the record in Dynamics 365 (matches the partyNumber used in the URL when applicable). (required)
            locationId: Identifier of the location resource to target in Dynamics 365. (required)
            partyNumber: Unique party (customer/vendor) identifier used in the URL path or query. (required)
            validFrom: Effective start date/time for the operation or for filtering records (ISO 8601 format). (required)
            City: City component of the address.
            CountryRegionISOCode: ISO code representing the country or region for the address or entity (e.g., US, GB).
            IsRoleDelivery: Flag indicating whether the role pertains to delivery (true/false expressed as string where applicable by the API).
            Roles: Comma-separated or otherwise formatted roles assigned to the party/location as expected by the endpoint.
            State: State or province component of the address.
            Street: Street address line for the location or party.
            ZipCode: Postal code for the address.
            rsmWebActive: Indicates whether the RSM web flag is active for this party/location.
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

