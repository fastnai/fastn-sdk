"""Fastn Cin7 connector — auto-generated type stubs.

Do not edit manually. Regenerate with `fastn connector sync`.
"""
from __future__ import annotations

from typing import Any, Dict, List, Optional


class Cin7Connector:
    """Cin7 connector ().

    Provides 83 tools.
    """

    def create_advanced_purchase(
        self,
        Approach: str,
        Location: str,
        Supplier: str,
        SupplierID: str,
        TaxRule: str,
        AdditionalAttributes: Optional[Dict[str, Any]] = None,
        BillingAddress: Optional[Dict[str, Any]] = None,
        BlindReceipt: Optional[bool] = None,
        Contact: Optional[str] = None,
        CurrencyRate: Optional[int] = None,
        Note: Optional[str] = None,
        Phone: Optional[str] = None,
        PurchaseType: Optional[str] = None,
        RequiredBy: Optional[str] = None,
        ShippingAddress: Optional[Dict[str, Any]] = None,
        TaxCalculation: Optional[str] = None,
        Terms: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Creates a new advanced purchase record in the system.

        Args:
            Approach: Specifies the processing approach or method. (required)
            Location: Specifies the relevant location or warehouse. (required)
            Supplier: The name of the supplier. (required)
            SupplierID: Unique identifier for the supplier. (required)
            TaxRule: Specifies the tax rule to apply. (required)
            AdditionalAttributes: A set of custom or additional data fields.
            BillingAddress: The address used for billing purposes.
            BlindReceipt: Indicates if this is a blind receipt (true/false).
            Contact: The name of the primary contact person.
            CurrencyRate: The exchange rate for the transaction currency.
            Note: Any additional notes or comments.
            Phone: The contact phone number.
            PurchaseType: The category or type of purchase.
            RequiredBy: The date when the items are required (e.g., YYYY-MM-DD).
            ShippingAddress: The address where items will be shipped.
            TaxCalculation: Defines the method for tax calculation.
            Terms: Payment or contract terms.
        Returns:
            API response as a dictionary.
        """
        ...

    def create_advanced_purchase_credit_note(
        self,
        CreditNoteDate: str,
        CreditNoteInvoiceNumber: str,
        CreditNoteNumber: str,
        Lines: List[Any],
        PurchaseID: str,
        Status: str,
        TaskID: str,
        AdditionalCharges: Optional[List[Any]] = None,
        CombineAdditionalCharges: Optional[bool] = None,
        Tax: Optional[int] = None,
        Total: Optional[float] = None,
        TotalBeforeTax: Optional[float] = None,
        Unstock: Optional[List[Any]] = None,
    ) -> Dict[str, Any]:
        """Creates a new credit note for advanced purchases in the system.

        Args:
            CreditNoteDate: The date the credit note was issued (e.g., YYYY-MM-DD). (required)
            CreditNoteInvoiceNumber: The invoice number associated with this credit note. (required)
            CreditNoteNumber: The unique number for the credit note. (required)
            Lines:  (required)
            PurchaseID: The unique identifier for the related purchase order. (required)
            Status: Specifies the current status of the credit note. (required)
            TaskID: The unique identifier for the associated task. (required)
            AdditionalCharges: 
            CombineAdditionalCharges: Indicates if additional charges should be combined (true/false).
            Tax: The total tax amount for the credit note.
            Total: The final total amount including taxes and charges.
            TotalBeforeTax: The total amount before taxes are applied.
            Unstock: 
        Returns:
            API response as a dictionary.
        """
        ...

    def create_advanced_purchase_invoice(
        self,
        InvoiceDate: str,
        InvoiceDueDate: str,
        InvoiceNumber: str,
        PurchaseID: str,
        Status: str,
        TaskID: str,
        AdditionalCharges: Optional[List[Any]] = None,
        CombineAdditionalCharges: Optional[bool] = None,
        InvoiceTotalAmount: Optional[int] = None,
        InvoiceTotalTaxAmount: Optional[int] = None,
        Lines: Optional[List[Any]] = None,
        Tax: Optional[int] = None,
        Total: Optional[int] = None,
        TotalBeforeTax: Optional[int] = None,
    ) -> Dict[str, Any]:
        """Creates a new invoice for an advanced purchase in the system.

        Args:
            InvoiceDate: Date of the invoice in YYYY-MM-DD format. (required)
            InvoiceDueDate: Due date for the invoice. (required)
            InvoiceNumber: The invoice number assigned by the supplier. (required)
            PurchaseID: Reference identifier for the purchase. (required)
            Status: Current status of the purchase. (required)
            TaskID: Optional task identifier associated with the purchase. (required)
            AdditionalCharges: Additional charges applicable to the purchase.
            CombineAdditionalCharges: Whether to combine additional charges into the total.
            InvoiceTotalAmount: Total invoice amount.
            InvoiceTotalTaxAmount: Total tax amount on the invoice.
            Lines: 
            Tax: Total tax amount.
            Total: Total amount of the purchase.
            TotalBeforeTax: Subtotal before tax.
        Returns:
            API response as a dictionary.
        """
        ...

    def create_advanced_purchase_manual_journals(
        self,
        PurchaseID: str,
        Status: str,
        TaskID: str,
        Lines: Optional[List[Any]] = None,
    ) -> Dict[str, Any]:
        """Creates a new manual journal entry for advanced purchases in the system.

        Args:
            PurchaseID: Unique identifier for the purchase. (required)
            Status: Current status to assign for the purchase/task. (required)
            TaskID: Identifier for the associated task. (required)
            Lines: 
        Returns:
            API response as a dictionary.
        """
        ...

    def create_advanced_purchase_payments(
        self,
        Account: str,
        CurrencyRate: int,
        DatePaid: str,
        TaskID: str,
        Type: str,
        Amount: Optional[int] = None,
        DateCreated: Optional[str] = None,
        DepositID: Optional[str] = None,
        Reference: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Creates new payments associated with advanced purchases in the system.

        Args:
            Account: The account related to the transaction. (required)
            CurrencyRate: The currency exchange rate applicable to the transaction. (required)
            DatePaid: The date when the payment was made. (required)
            TaskID: The unique identifier for the Cin7 task. (required)
            Type: The type of the task to perform. (required)
            Amount: Monetary amount involved in the task.
            DateCreated: The creation date of the task.
            DepositID: The deposit identifier associated with the task.
            Reference: Reference or note associated with the task.
        Returns:
            API response as a dictionary.
        """
        ...

    def create_advanced_purchase_put_away(
        self,
        PurchaseID: str,
        Status: str,
        Lines: Optional[List[Any]] = None,
        TaskID: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Creates a new put away record for advanced purchases in the system.

        Args:
            PurchaseID: Unique identifier for the purchase. (required)
            Status: Current status of the purchase (DRAFT or AUTHORISED). (required)
            Lines: 
            TaskID: Optional task identifier related to this operation.
        Returns:
            API response as a dictionary.
        """
        ...

    def create_advanced_purchase_stock(
        self,
        PurchaseID: str,
        Status: str,
        Lines: Optional[List[Any]] = None,
        TaskID: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Creates stock records associated with advanced purchases in the system.

        Args:
            PurchaseID: Identifier for the Purchase record. (required)
            Status: Current status of the purchase/task. (required)
            Lines: 
            TaskID: Identifier for the related Task.
        Returns:
            API response as a dictionary.
        """
        ...

    def create_credit_note(
        self,
        Account: Optional[str] = None,
        CombineAdditionalCharges: Optional[bool] = None,
        CreditNoteConversionRate: Optional[int] = None,
        CreditNoteDate: Optional[str] = None,
        CreditNoteInvoiceNumber: Optional[str] = None,
        DoStockAdjustment: Optional[bool] = None,
        Lines: Optional[List[Any]] = None,
        Memo: Optional[str] = None,
        Refunds: Optional[List[Any]] = None,
        SaleId: Optional[str] = None,
        Status: Optional[str] = None,
        TaskID: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Issues a credit note for a specific sale in the system.

        Args:
            Account: 
            CombineAdditionalCharges: 
            CreditNoteConversionRate: 
            CreditNoteDate: 
            CreditNoteInvoiceNumber: 
            DoStockAdjustment: 
            Lines: 
            Memo: 
            Refunds: 
            SaleId: 
            Status: 
            TaskID: 
        Returns:
            API response as a dictionary.
        """
        ...

    def create_customer(
        self,
        AccountReceivable: str,
        Currency: str,
        Name: str,
        PaymentTerm: str,
        RevenueAccount: str,
        Status: str,
        TaxRule: str,
        AdditionalAttribute1: Optional[str] = None,
        AdditionalAttribute10: Optional[str] = None,
        AdditionalAttribute2: Optional[str] = None,
        AdditionalAttribute3: Optional[str] = None,
        AdditionalAttribute4: Optional[str] = None,
        AdditionalAttribute5: Optional[str] = None,
        AdditionalAttribute6: Optional[str] = None,
        AdditionalAttribute7: Optional[str] = None,
        AdditionalAttribute8: Optional[str] = None,
        AdditionalAttribute9: Optional[str] = None,
        Addresses: Optional[List[Any]] = None,
        AttributeSet: Optional[str] = None,
        Carrier: Optional[str] = None,
        Comments: Optional[str] = None,
        Contacts: Optional[List[Any]] = None,
        Discount: Optional[int] = None,
        IsOnCreditHold: Optional[bool] = None,
        Location: Optional[str] = None,
        PriceTier: Optional[str] = None,
        SalesRepresentative: Optional[str] = None,
        Tags: Optional[str] = None,
        TaxNumber: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Creates a new customer profile in the system.

        Args:
            AccountReceivable:  (required)
            Currency:  (required)
            Name:  (required)
            PaymentTerm:  (required)
            RevenueAccount:  (required)
            Status:  (required)
            TaxRule:  (required)
            AdditionalAttribute1: 
            AdditionalAttribute10: 
            AdditionalAttribute2: 
            AdditionalAttribute3: 
            AdditionalAttribute4: 
            AdditionalAttribute5: 
            AdditionalAttribute6: 
            AdditionalAttribute7: 
            AdditionalAttribute8: 
            AdditionalAttribute9: 
            Addresses: 
            AttributeSet: 
            Carrier: 
            Comments: 
            Contacts: 
            Discount: 
            IsOnCreditHold: 
            Location: 
            PriceTier: 
            SalesRepresentative: 
            Tags: 
            TaxNumber: 
        Returns:
            API response as a dictionary.
        """
        ...

    def create_product(
        self,
        Category: str,
        CostingMethod: str,
        Name: str,
        PriceTier1: float,
        SKU: str,
        Status: str,
        Type: str,
        UOM: str,
        AdditionalAttribute1: Optional[str] = None,
        AdditionalAttribute10: Optional[str] = None,
        AdditionalAttribute2: Optional[str] = None,
        AdditionalAttribute3: Optional[str] = None,
        AdditionalAttribute4: Optional[str] = None,
        AdditionalAttribute5: Optional[str] = None,
        AdditionalAttribute6: Optional[str] = None,
        AdditionalAttribute7: Optional[str] = None,
        AdditionalAttribute8: Optional[str] = None,
        AdditionalAttribute9: Optional[str] = None,
        AlwaysShowQuantity: Optional[str] = None,
        AttributeSet: Optional[str] = None,
        AverageCost: Optional[float] = None,
        Barcode: Optional[str] = None,
        Brand: Optional[str] = None,
        COGSAccount: Optional[str] = None,
        DefaultLocation: Optional[str] = None,
        Description: Optional[str] = None,
        DiscountRule: Optional[str] = None,
        DropShipMode: Optional[str] = None,
        ExpenseAccount: Optional[str] = None,
        Height: Optional[float] = None,
        ID: Optional[str] = None,
        InventoryAccount: Optional[str] = None,
        LastModifiedOn: Optional[str] = None,
        Length: Optional[float] = None,
        MinimumBeforeReorder: Optional[float] = None,
        PickZones: Optional[str] = None,
        PriceTier10: Optional[float] = None,
        PriceTier2: Optional[float] = None,
        PriceTier3: Optional[float] = None,
        PriceTier4: Optional[float] = None,
        PriceTier5: Optional[float] = None,
        PriceTier6: Optional[float] = None,
        PriceTier7: Optional[float] = None,
        PriceTier8: Optional[float] = None,
        PriceTier9: Optional[float] = None,
        PriceTiers: Optional[Dict[str, Any]] = None,
        PurchaseTaxRule: Optional[str] = None,
        ReorderQuantity: Optional[float] = None,
        RevenueAccount: Optional[str] = None,
        SaleTaxRule: Optional[str] = None,
        Sellable: Optional[bool] = None,
        StockLocator: Optional[str] = None,
        Tags: Optional[str] = None,
        Weight: Optional[float] = None,
        Width: Optional[float] = None,
    ) -> Dict[str, Any]:
        """Creates a new product in the system.

        Args:
            Category:  (required)
            CostingMethod:  (required)
            Name:  (required)
            PriceTier1:  (required)
            SKU:  (required)
            Status:  (required)
            Type:  (required)
            UOM:  (required)
            AdditionalAttribute1: 
            AdditionalAttribute10: 
            AdditionalAttribute2: 
            AdditionalAttribute3: 
            AdditionalAttribute4: 
            AdditionalAttribute5: 
            AdditionalAttribute6: 
            AdditionalAttribute7: 
            AdditionalAttribute8: 
            AdditionalAttribute9: 
            AlwaysShowQuantity: 
            AttributeSet: 
            AverageCost: 
            Barcode: 
            Brand: 
            COGSAccount: 
            DefaultLocation: 
            Description: 
            DiscountRule: 
            DropShipMode: 
            ExpenseAccount: 
            Height: 
            ID: 
            InventoryAccount: 
            LastModifiedOn: 
            Length: 
            MinimumBeforeReorder: 
            PickZones: 
            PriceTier10: 
            PriceTier2: 
            PriceTier3: 
            PriceTier4: 
            PriceTier5: 
            PriceTier6: 
            PriceTier7: 
            PriceTier8: 
            PriceTier9: 
            PriceTiers: 
            PurchaseTaxRule: 
            ReorderQuantity: 
            RevenueAccount: 
            SaleTaxRule: 
            Sellable: 
            StockLocator: 
            Tags: 
            Weight: 
            Width: 
        Returns:
            API response as a dictionary.
        """
        ...

    def create_sale(
        self,
        Customer: str,
        CustomerID: str,
        AdditionalAttributes: Optional[Dict[str, Any]] = None,
        AutoPickPackShipMode: Optional[str] = None,
        BillingAddress: Optional[Dict[str, Any]] = None,
        Carrier: Optional[str] = None,
        Contact: Optional[str] = None,
        CurrencyRate: Optional[str] = None,
        CustomerReference: Optional[str] = None,
        DefaultAccount: Optional[str] = None,
        Email: Optional[str] = None,
        Location: Optional[str] = None,
        Note: Optional[str] = None,
        Phone: Optional[str] = None,
        PriceTier: Optional[str] = None,
        SaleOrderDate: Optional[str] = None,
        SalesRepresentative: Optional[str] = None,
        ShipBy: Optional[str] = None,
        ShippingAddress: Optional[Dict[str, Any]] = None,
        ShippingNotes: Optional[str] = None,
        SkipQuote: Optional[str] = None,
        TaxInclusive: Optional[str] = None,
        TaxRule: Optional[str] = None,
        Terms: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Creates a new sale transaction in the system.

        Args:
            Customer:  (required)
            CustomerID:  (required)
            AdditionalAttributes: 
            AutoPickPackShipMode: 
            BillingAddress: 
            Carrier: 
            Contact: 
            CurrencyRate: 
            CustomerReference: 
            DefaultAccount: 
            Email: 
            Location: 
            Note: 
            Phone: 
            PriceTier: 
            SaleOrderDate: 
            SalesRepresentative: 
            ShipBy: 
            ShippingAddress: 
            ShippingNotes: 
            SkipQuote: 
            TaxInclusive: 
            TaxRule: 
            Terms: 
        Returns:
            API response as a dictionary.
        """
        ...

    def create_sale_fulfillment(
        self,
        SaleID: str,
    ) -> Dict[str, Any]:
        """Creates a new sale fulfillment record in the system.

        Args:
            SaleID: Identifier of the sale record in Cin7. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def create_sale_fulfillment_pack(
        self,
        Lines: List[Any],
        Status: str,
        TaskID: str,
    ) -> Dict[str, Any]:
        """Creates a new fulfillment pack in the system.

        Args:
            Lines:  (required)
            Status: Current status of the task. (required)
            TaskID: Unique identifier for the task. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def create_sale_fulfillment_pick(
        self,
        Status: str,
        TaskID: str,
        AutoPickMode: Optional[str] = None,
        Lines: Optional[List[Any]] = None,
    ) -> Dict[str, Any]:
        """Creates a new fulfillment pick for a sale in the system.

        Args:
            Status: Current status of the task. (required)
            TaskID: A unique identifier for the task. (required)
            AutoPickMode: Mode for automatic picking process.
            Lines: 
        Returns:
            API response as a dictionary.
        """
        ...

    def create_sale_fulfillment_ship(
        self,
        Lines: List[Any],
        Status: str,
        TaskID: str,
        RequireBy: Optional[str] = None,
        ShippingAddress: Optional[Dict[str, Any]] = None,
        ShippingNotes: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Creates a new shipment for a sale fulfillment in the system.

        Args:
            Lines:  (required)
            Status: Current status of the task. (required)
            TaskID: Unique identifier for the task. (required)
            RequireBy: Date by which the task is required.
            ShippingAddress: Delivery address details.
            ShippingNotes: Additional notes related to shipping.
        Returns:
            API response as a dictionary.
        """
        ...

    def create_sale_invoice(
        self,
        InvoiceDate: str,
        InvoiceDueDate: str,
        SaleID: str,
        Status: str,
        TaskID: str,
        AdditionalCharges: Optional[List[Any]] = None,
        BillingAddressLine1: Optional[str] = None,
        BillingAddressLine2: Optional[str] = None,
        CombineAdditionalCharges: Optional[bool] = None,
        CurrencyConversionRate: Optional[float] = None,
        Lines: Optional[List[Any]] = None,
        LinkedFulfillmentNumber: Optional[str] = None,
        Memo: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Creates a new invoice for a sale in the system.

        Args:
            InvoiceDate: Date when the invoice was issued. (required)
            InvoiceDueDate: Due date for the invoice payment. (required)
            SaleID: Unique identifier for the sale. (required)
            Status: Current status of the sale. (required)
            TaskID: Identifier for the task related to the sale. (required)
            AdditionalCharges: 
            BillingAddressLine1: First line of the billing address.
            BillingAddressLine2: Second line of the billing address.
            CombineAdditionalCharges: Flag to indicate if additional charges should be combined.
            CurrencyConversionRate: Conversion rate used for currency calculations.
            Lines: 
            LinkedFulfillmentNumber: Reference number for linked fulfillment.
            Memo: Optional memo or note regarding the sale.
        Returns:
            API response as a dictionary.
        """
        ...

    def create_sale_order(
        self,
        AdditionalCharges: Optional[List[Any]] = None,
        AutoPickPackShipMode: Optional[str] = None,
        Lines: Optional[List[Any]] = None,
        Memo: Optional[str] = None,
        SaleID: Optional[str] = None,
        Status: Optional[str] = None,
        Tax: Optional[int] = None,
        Total: Optional[int] = None,
        TotalBeforeTax: Optional[int] = None,
    ) -> Dict[str, Any]:
        """Creates a new sale order in the system.

        Args:
            AdditionalCharges: 
            AutoPickPackShipMode: 
            Lines: 
            Memo: 
            SaleID: 
            Status: 
            Tax: 
            Total: 
            TotalBeforeTax: 
        Returns:
            API response as a dictionary.
        """
        ...

    def create_sale_payment(
        self,
        Account: Optional[str] = None,
        Amount: Optional[int] = None,
        CreditID: Optional[str] = None,
        CurrencyRate: Optional[int] = None,
        DatePaid: Optional[str] = None,
        Reference: Optional[str] = None,
        TaskID: Optional[str] = None,
        Type: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Processes a payment for a specific sale in the system.

        Args:
            Account: Account associated with the task in Cin7.
            Amount: Amount associated with the task in Cin7.
            CreditID: Credit ID associated with the task in Cin7.
            CurrencyRate: Currency rate for the task in Cin7.
            DatePaid: Date the task was paid in Cin7.
            Reference: Reference for the task in Cin7.
            TaskID: ID of the task in Cin7.
            Type: Type of the task in Cin7.
        Returns:
            API response as a dictionary.
        """
        ...

    def create_stock_adjustment(
        self,
        EffectiveDate: str,
        Status: str,
        Account: Optional[str] = None,
        Lines: Optional[List[Any]] = None,
        Reference: Optional[str] = None,
        StocktakeNumber: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Creates a new stock adjustment record in the system.

        Args:
            EffectiveDate: The date when the stocktake becomes effective. (required)
            Status: Current status of the stocktake. (required)
            Account: Account associated with the stocktake.
            Lines: 
            Reference: Additional reference information.
            StocktakeNumber: Unique identifier for the stocktake.
        Returns:
            API response as a dictionary.
        """
        ...

    def create_stock_take(
        self,
        EffectiveDate: str,
        Location: str,
        Account: Optional[str] = None,
        Categories: Optional[List[Any]] = None,
        LocationID: Optional[str] = None,
        Reference: Optional[str] = None,
        Tags: Optional[List[Any]] = None,
    ) -> Dict[str, Any]:
        """Creates a new stock take in the system.

        Args:
            EffectiveDate: The date when the request or changes take effect. (required)
            Location: The location relevant to the request. (required)
            Account: The account associated with this request.
            Categories: 
            LocationID: Unique identifier for the location.
            Reference: Optional reference information for the request.
            Tags: List of tags associated with the request.
        Returns:
            API response as a dictionary.
        """
        ...

    def create_stock_transfer(
        self,
        From: str,
        Status: str,
        To: str,
        CompletionDate: Optional[str] = None,
        CostDistributionType: Optional[str] = None,
        DepartureDate: Optional[str] = None,
        FromLocation: Optional[str] = None,
        InTransitAccount: Optional[str] = None,
        Lines: Optional[List[Any]] = None,
        ManualJournals: Optional[List[Any]] = None,
        Reference: Optional[str] = None,
        RequiredByDate: Optional[str] = None,
        SkipOrder: Optional[bool] = None,
        ToLocation: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Creates a new stock transfer order in the system.

        Args:
            From: Origin location of the transfer. (required)
            Status: Current status of the transfer or process. (required)
            To: Destination location of the transfer. (required)
            CompletionDate: Expected or actual completion date of the transfer.
            CostDistributionType: Method of distributing costs for the transfer.
            DepartureDate: Date when the transfer departs.
            FromLocation: Detailed origin location information.
            InTransitAccount: Account used for in-transit inventory accounting.
            Lines: 
            ManualJournals: Optional manual journal entries related to the transfer.
            Reference: Additional reference information for the transfer.
            RequiredByDate: Date by which the transfer should be completed.
            SkipOrder: Flag to indicate whether to skip processing the order.
            ToLocation: Detailed destination location information.
        Returns:
            API response as a dictionary.
        """
        ...

    def create_stock_transfer_order(
        self,
        Lines: List[Any],
        Status: str,
        TaskID: str,
    ) -> Dict[str, Any]:
        """Creates a new stock transfer order record in the system.

        Args:
            Lines:  (required)
            Status: Current status of the task. (required)
            TaskID: Unique identifier for the task. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def create_webhook(
        self,
        ExternalAuthorizationType: Optional[str] = None,
        ExternalBearerToken: Optional[str] = None,
        ExternalHeaders: Optional[List[Any]] = None,
        ExternalPassword: Optional[str] = None,
        ExternalURL: Optional[str] = None,
        ExternalUserName: Optional[str] = None,
        IsActive: Optional[bool] = None,
        Type: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Creates a new webhook in the system to listen for specific events.

        Args:
            ExternalAuthorizationType: 
            ExternalBearerToken: 
            ExternalHeaders: 
            ExternalPassword: 
            ExternalURL: 
            ExternalUserName: 
            IsActive: 
            Type: 
        Returns:
            API response as a dictionary.
        """
        ...

    def delete_advanced_purchase(
        self,
        ID: str,
        Void: Optional[bool] = None,
    ) -> Dict[str, Any]:
        """Deletes a specific advanced purchase from the system.

        Args:
            ID: Unique identifier for the resource. (required)
            Void: Indicates whether the operation should be voided.
        Returns:
            API response as a dictionary.
        """
        ...

    def delete_advanced_purchase_credit_note(
        self,
        TaskID: str,
    ) -> Dict[str, Any]:
        """Deletes a specific credit note for advanced purchases from the system.

        Args:
            TaskID: Identifier for the specific task to operate on. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def delete_advanced_purchase_invoice(
        self,
        TaskID: str,
        Void: Optional[bool] = None,
    ) -> Dict[str, Any]:
        """Deletes a specific advanced purchase invoice from the system.

        Args:
            TaskID: Unique identifier for the Cin7 task. (required)
            Void: Indicates whether to void the specified task.
        Returns:
            API response as a dictionary.
        """
        ...

    def delete_advanced_purchase_payments(
        self,
        ID: str,
        DeleteAllocation: Optional[bool] = None,
    ) -> Dict[str, Any]:
        """Deletes specific payments related to advanced purchases from the system.

        Args:
            ID: The unique identifier of the allocation to delete. (required)
            DeleteAllocation: Flag indicating whether the allocation should be deleted.
        Returns:
            API response as a dictionary.
        """
        ...

    def delete_advanced_purchase_stock(
        self,
        TaskID: str,
        Void: Optional[bool] = None,
    ) -> Dict[str, Any]:
        """Deletes specific stock records related to advanced purchases from the system.

        Args:
            TaskID: The unique identifier of the task to operate on. (required)
            Void: Flag indicating whether to void the task.
        Returns:
            API response as a dictionary.
        """
        ...

    def delete_sale(
        self,
        ID: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Deletes a specific sale from the system.

        Args:
            ID: 
        Returns:
            API response as a dictionary.
        """
        ...

    def delete_sale_fulfillment(
        self,
        TaskID: str,
        Void: Optional[bool] = None,
    ) -> Dict[str, Any]:
        """Deletes a specific sale fulfillment from the system.

        Args:
            TaskID: The identifier for the specific task. (required)
            Void: Indicates whether the task should be voided.
        Returns:
            API response as a dictionary.
        """
        ...

    def delete_sale_invoice(
        self,
        TaskID: str,
        Void: Optional[bool] = None,
    ) -> Dict[str, Any]:
        """Deletes a specific sale invoice from the system.

        Args:
            TaskID: Unique identifier for the specific task. (required)
            Void: Indicates whether to void the task.
        Returns:
            API response as a dictionary.
        """
        ...

    def delete_stock_adjustment(
        self,
        ID: str,
        Void: Optional[bool] = None,
    ) -> Dict[str, Any]:
        """Deletes a specific stock adjustment from the system.

        Args:
            ID: Unique identifier for the resource or item. (required)
            Void: Flag indicating whether to void the operation.
        Returns:
            API response as a dictionary.
        """
        ...

    def delete_stock_take(
        self,
        ID: str,
        Void: Optional[bool] = None,
    ) -> Dict[str, Any]:
        """Deletes a specific stock take from the system.

        Args:
            ID: The identifier for the resource or entity in Cin7. (required)
            Void: Indicator whether the operation is a void action.
        Returns:
            API response as a dictionary.
        """
        ...

    def delete_stock_transfer(
        self,
        ID: str,
        Void: Optional[bool] = None,
    ) -> Dict[str, Any]:
        """Deletes a specific stock transfer from the system.

        Args:
            ID: Unique identifier for the resource in Cin7. (required)
            Void: Optional parameter to specify void actions, if applicable.
        Returns:
            API response as a dictionary.
        """
        ...

    def delete_webhook(
        self,
        ID: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Deletes an existing webhook from the system.

        Args:
            ID: ID parameter for the My connectors API request.
        Returns:
            API response as a dictionary.
        """
        ...

    def deprecate_product(
        self,
        productId: str,
    ) -> Dict[str, Any]:
        """Marks a product as deprecated in the system, making it unavailable for new transactions.

        Args:
            productId:  (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def get_advanced_purchase(
        self,
        ID: str,
        CombineAdditionalCharges: Optional[bool] = None,
    ) -> Dict[str, Any]:
        """Retrieves details of advanced purchases made in the system.

        Args:
            ID: The unique identifier for the record or item being referenced. (required)
            CombineAdditionalCharges: Whether to combine additional charges in the Cin7 request.
        Returns:
            API response as a dictionary.
        """
        ...

    def get_advanced_purchase_credit_note(
        self,
        PurchaseID: str,
        CombineAdditionalCharges: Optional[bool] = None,
    ) -> Dict[str, Any]:
        """Retrieves credit note details for advanced purchases in the system.

        Args:
            PurchaseID: Identifier of the purchase record to operate on. (required)
            CombineAdditionalCharges: Flag to indicate whether to combine additional charges.
        Returns:
            API response as a dictionary.
        """
        ...

    def get_advanced_purchase_invoice(
        self,
        PurchaseID: str,
        CombineAdditionalCharges: Optional[bool] = None,
    ) -> Dict[str, Any]:
        """Fetches invoice details for an advanced purchase in the system.

        Args:
            PurchaseID: The identifier for the purchase transaction. (required)
            CombineAdditionalCharges: Flag to determine whether to combine additional charges in the response.
        Returns:
            API response as a dictionary.
        """
        ...

    def get_advanced_purchase_manual_journals(
        self,
        PurchaseID: str,
    ) -> Dict[str, Any]:
        """Retrieves manual journal entries related to advanced purchases in the system.

        Args:
            PurchaseID: The unique identifier of the purchase in Cin7. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def get_advanced_purchase_payments(
        self,
        PurchaseID: str,
        CreditNoteNumber: Optional[str] = None,
        InvoiceNumber: Optional[str] = None,
        OrderNumber: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Retrieves payment details related to advanced purchases in the system.

        Args:
            PurchaseID: The unique identifier of the purchase. (required)
            CreditNoteNumber: The unique identifier of the credit note.
            InvoiceNumber: The unique identifier of the invoice.
            OrderNumber: The unique identifier of the order.
        Returns:
            API response as a dictionary.
        """
        ...

    def get_advanced_purchase_put_away(
        self,
        PurchaseID: str,
    ) -> Dict[str, Any]:
        """Retrieves put away details for advanced purchases in the system.

        Args:
            PurchaseID:  (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def get_advanced_purchase_stock(
        self,
        PurchaseID: str,
    ) -> Dict[str, Any]:
        """Fetches stock details related to an advanced purchase in the system.

        Args:
            PurchaseID: The unique identifier for the Cin7 purchase. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def get_chart_of_accounts(
        self,
        Class: Optional[str] = None,
        Code: Optional[str] = None,
        Limit: Optional[str] = None,
        Name: Optional[str] = None,
        Page: Optional[str] = None,
        Status: Optional[str] = None,
        Type: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Retrieves the chart of accounts in the financial system.

        Args:
            Class: 
            Code: 
            Limit: 
            Name: 
            Page: 
            Status: 
            Type: 
        Returns:
            API response as a dictionary.
        """
        ...

    def get_customers(
        self,
        ContactFilter: Optional[str] = None,
        ID: Optional[str] = None,
        IncludeDeprecated: Optional[str] = None,
        IncludeProductPrices: Optional[str] = None,
        Limit: Optional[str] = None,
        ModifiedSince: Optional[str] = None,
        Name: Optional[str] = None,
        Page: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Fetches a list of customers in the system.

        Args:
            ContactFilter: Filter contacts based on specified criteria.
            ID: ID of the resource to retrieve.
            IncludeDeprecated: Whether to include deprecated data in the response (true/false).
            IncludeProductPrices: Whether to include product prices in the response (true/false).
            Limit: Limit the number of results returned.
            ModifiedSince: Filter results modified since this timestamp.
            Name: Filter results by name.
            Page: Specify the page number for pagination.
        Returns:
            API response as a dictionary.
        """
        ...

    def get_locations(
        self,
        Deprecated: Optional[str] = None,
        ID: Optional[str] = None,
        Limit: Optional[str] = None,
        Name: Optional[str] = None,
        Page: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Fetches the available locations in the system.

        Args:
            Deprecated: 
            ID: 
            Limit: 
            Name: 
            Page: 
        Returns:
            API response as a dictionary.
        """
        ...

    def get_payment_terms(
        self,
    ) -> Dict[str, Any]:
        """Fetches the payment terms applicable to transactions in the system.
        Returns:
            API response as a dictionary.
        """
        ...

    def get_price_tiers(
        self,
    ) -> Dict[str, Any]:
        """Retrieves the pricing tiers used for pricing products in the system.
        Returns:
            API response as a dictionary.
        """
        ...

    def get_product_availability(
        self,
        batch: Optional[str] = None,
        category: Optional[str] = None,
        limit: Optional[str] = None,
        location: Optional[str] = None,
        page: Optional[str] = None,
        sku: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Checks the availability status of a specific product in the system.

        Args:
            batch: 
            category: 
            limit: 
            location: 
            page: 
            sku: 
        Returns:
            API response as a dictionary.
        """
        ...

    def get_product_categories(
        self,
        Limit: Optional[str] = None,
        Name: Optional[str] = None,
        Page: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Retrieves a list of product categories available in the system.

        Args:
            Limit: Number of records per page.
            Name: Name filter for the request.
            Page: Page number for pagination.
        Returns:
            API response as a dictionary.
        """
        ...

    def get_products(
        self,
        ID: Optional[str] = None,
        ModifiedSince: Optional[str] = None,
        brand: Optional[str] = None,
        category: Optional[str] = None,
        createdSince: Optional[str] = None,
        limit: Optional[str] = None,
        name: Optional[str] = None,
        page: Optional[str] = None,
        sku: Optional[str] = None,
        sortBy: Optional[str] = None,
        sortDirection: Optional[str] = None,
        status: Optional[str] = None,
        updatedSince: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Retrieves a list of all products available in the system.

        Args:
            ID: 
            ModifiedSince: Filter results modified since this date/time.
            brand: Filter results by brand name.
            category: Filter results by product category.
            createdSince: Filter results created since this date/time.
            limit: Limit the number of results returned.
            name: Filter results by product name.
            page: Specify the page number for pagination.
            sku: Filter results by SKU.
            sortBy: Field to sort results by.
            sortDirection: Sort direction (asc or desc).
            status: Filter results by product status.
            updatedSince: Filter results updated since this date/time.
        Returns:
            API response as a dictionary.
        """
        ...

    def get_purchase(
        self,
        CombineAdditionalCharges: Optional[str] = None,
        ID: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Retrieves details of a specific purchase in the system.

        Args:
            CombineAdditionalCharges: 
            ID: 
        Returns:
            API response as a dictionary.
        """
        ...

    def get_purchase_list(
        self,
        UpdatedSince: Optional[str] = None,
        limit: Optional[str] = None,
        page: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Fetches a list of purchases in the system.

        Args:
            UpdatedSince: 
            limit: 
            page: 
        Returns:
            API response as a dictionary.
        """
        ...

    def get_sale(
        self,
        CombineAdditionalCharges: Optional[str] = None,
        CountryFormat: Optional[str] = None,
        HideInventoryMovements: Optional[str] = None,
        ID: Optional[str] = None,
        IncludeTransactions: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Retrieves details about a specific sale in the system.

        Args:
            CombineAdditionalCharges: Specifies whether to combine additional charges.
            CountryFormat: Specifies the country format for the response.
            HideInventoryMovements: Specifies whether to hide inventory movements.
            ID: Identifier for the request.
            IncludeTransactions: Specifies whether to include transactions in the response.
        Returns:
            API response as a dictionary.
        """
        ...

    def get_sale_fulfillment(
        self,
        SaleID: str,
        IncludeProductInfo: Optional[bool] = None,
        limit: Optional[int] = None,
        page: Optional[int] = None,
    ) -> Dict[str, Any]:
        """Retrieves fulfillment details for a specific sale in the system.

        Args:
            SaleID: The unique identifier for a sale. (required)
            IncludeProductInfo: Flag to include detailed product information.
            limit: Maximum number of items to return.
            page: Specifies which page of results to retrieve.
        Returns:
            API response as a dictionary.
        """
        ...

    def get_sale_fulfillment_pack(
        self,
        TaskID: str,
        IncludeProductInfo: Optional[bool] = None,
    ) -> Dict[str, Any]:
        """Retrieves details of a specific fulfillment pack for a sale in the system.

        Args:
            TaskID: Identifier for the specific task to perform. (required)
            IncludeProductInfo: Flag to include detailed product information.
        Returns:
            API response as a dictionary.
        """
        ...

    def get_sale_fulfillment_pick(
        self,
        TaskID: str,
        IncludeProductInfo: Optional[bool] = None,
    ) -> Dict[str, Any]:
        """Retrieves details of a specific fulfillment pick within a sale in the system.

        Args:
            TaskID:  (required)
            IncludeProductInfo: 
        Returns:
            API response as a dictionary.
        """
        ...

    def get_sale_fulfillment_ship(
        self,
        TaskID: str,
    ) -> Dict[str, Any]:
        """Retrieves shipment details for a specific sale fulfillment in the system.

        Args:
            TaskID: Unique identifier for the task in Cin7. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def get_sale_invoice(
        self,
        SaleID: str,
        CombineAdditionalCharges: Optional[bool] = None,
        IncludeProductInfo: Optional[bool] = None,
    ) -> Dict[str, Any]:
        """Retrieves invoice details for a specific sale in the system.

        Args:
            SaleID: Unique identifier for the sale transaction. (required)
            CombineAdditionalCharges: Flag to indicate if additional charges should be combined.
            IncludeProductInfo: Flag to include product information in the response.
        Returns:
            API response as a dictionary.
        """
        ...

    def get_sales_list(
        self,
        CombinedInvoiceStatus: Optional[str] = None,
        CombinedPackStatus: Optional[str] = None,
        CombinedPickStatus: Optional[str] = None,
        CombinedShippingStatus: Optional[str] = None,
        CreatedSince: Optional[str] = None,
        CreditNoteStatus: Optional[str] = None,
        CustomerID: Optional[str] = None,
        ExternalID: Optional[str] = None,
        Limit: Optional[str] = None,
        OrderLocationID: Optional[str] = None,
        OrderStatus: Optional[str] = None,
        Page: Optional[str] = None,
        QuoteStatus: Optional[str] = None,
        Search: Optional[str] = None,
        ShipBy: Optional[str] = None,
        Status: Optional[str] = None,
        UpdatedSince: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Retrieves the list of sales recorded in the system.

        Args:
            CombinedInvoiceStatus: Filter orders by combined invoice status.
            CombinedPackStatus: Filter orders by combined packing status.
            CombinedPickStatus: Filter orders by combined picking status.
            CombinedShippingStatus: Filter orders by combined shipping status.
            CreatedSince: Filter orders created since a specific date and time.
            CreditNoteStatus: Filter credit notes by status.
            CustomerID: Filter orders by customer ID.
            ExternalID: Filter orders by external ID.
            Limit: Limit the number of results returned.
            OrderLocationID: Filter orders by order location ID.
            OrderStatus: Filter orders by status.
            Page: Specify the page number for pagination.
            QuoteStatus: Filter quotes by status.
            Search: Search orders based on various criteria.
            ShipBy: Filter orders by ship by date.
            Status: Filter orders by status.
            UpdatedSince: Filter orders updated since a specific date and time.
        Returns:
            API response as a dictionary.
        """
        ...

    def get_stock_adjustment(
        self,
        TaskID: str,
    ) -> Dict[str, Any]:
        """Retrieves details about a specific stock adjustment in the system.

        Args:
            TaskID: Identifier of the task to process. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def get_stock_adjustment_list(
        self,
        Limit: Optional[int] = None,
        Page: Optional[int] = None,
        Status: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Retrieves a list of stock adjustments made in the system.

        Args:
            Limit: Maximum number of items to retrieve.
            Page: Page number of results to fetch.
            Status: Filter by order status.
        Returns:
            API response as a dictionary.
        """
        ...

    def get_stock_take(
        self,
        TaskID: str,
    ) -> Dict[str, Any]:
        """Fetches details of a specific stock take in the system.

        Args:
            TaskID: Unique identifier for the task. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def get_stock_take_list(
        self,
        Limit: Optional[int] = None,
        Page: Optional[int] = None,
        Status: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Retrieves a list of stock takes conducted in the system.

        Args:
            Limit: Maximum number of items to retrieve per request.
            Page: Page number of the results to retrieve.
            Status: Filter results by status.
        Returns:
            API response as a dictionary.
        """
        ...

    def get_stock_transfer(
        self,
        TaskID: str,
    ) -> Dict[str, Any]:
        """Fetches details of a specific stock transfer in the system.

        Args:
            TaskID: Identifier for the task to be processed. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def get_stock_transfer_list(
        self,
        Limit: Optional[int] = None,
        Page: Optional[int] = None,
        Search: Optional[str] = None,
        Status: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Retrieves a list of stock transfers in the system.

        Args:
            Limit: Maximum number of items to return per request.
            Page: Page number for paginated results.
            Search: Search term to filter results.
            Status: Filter by status of the items.
        Returns:
            API response as a dictionary.
        """
        ...

    def get_stock_transfer_order(
        self,
        TaskID: str,
    ) -> Dict[str, Any]:
        """Retrieves details of a specific stock transfer order in the system.

        Args:
            TaskID: Unique identifier for the task you want to perform. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def get_tax_rules(
        self,
        Account: Optional[str] = None,
        ID: Optional[str] = None,
        IsActive: Optional[str] = None,
        IsTaxForPurchase: Optional[str] = None,
        IsTaxForSale: Optional[str] = None,
        Limit: Optional[str] = None,
        Name: Optional[str] = None,
        Page: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Fetches all tax rules currently implemented in the system.

        Args:
            Account: 
            ID: 
            IsActive: 
            IsTaxForPurchase: 
            IsTaxForSale: 
            Limit: 
            Name: 
            Page: 
        Returns:
            API response as a dictionary.
        """
        ...

    def get_webhooks(
        self,
    ) -> Dict[str, Any]:
        """Fetches all registered webhooks within the system.
        Returns:
            API response as a dictionary.
        """
        ...

    def update_advanced_purchase(
        self,
        ID: str,
        Supplier: str,
        TaxRule: str,
        AdditionalAttributes: Optional[Dict[str, Any]] = None,
        BillingAddress: Optional[Dict[str, Any]] = None,
        BlindReceipt: Optional[bool] = None,
        Contact: Optional[str] = None,
        CurrencyRate: Optional[int] = None,
        Location: Optional[str] = None,
        Note: Optional[str] = None,
        Phone: Optional[str] = None,
        RequiredBy: Optional[str] = None,
        ShippingAddress: Optional[Dict[str, Any]] = None,
        SupplierID: Optional[str] = None,
        TaxCalculation: Optional[str] = None,
        Terms: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Updates details of an existing advanced purchase in the system.

        Args:
            ID: Unique identifier for the record. (required)
            Supplier: The name of the supplier. (required)
            TaxRule: Specifies the tax rule to apply. (required)
            AdditionalAttributes: A set of custom or additional data fields.
            BillingAddress: The address used for billing purposes.
            BlindReceipt: Indicates if this is a blind receipt (true/false).
            Contact: The name of the primary contact person.
            CurrencyRate: The exchange rate for the transaction currency.
            Location: Specifies the relevant location or warehouse.
            Note: Any additional notes or comments.
            Phone: The contact phone number.
            RequiredBy: The date when the items are required (e.g., YYYY-MM-DD).
            ShippingAddress: The address where items will be shipped.
            SupplierID: Unique identifier for the supplier.
            TaxCalculation: Defines the method for tax calculation.
            Terms: Payment or contract terms.
        Returns:
            API response as a dictionary.
        """
        ...

    def update_advanced_purchase_payments(
        self,
        TaskID: str,
        Account: Optional[str] = None,
        Amount: Optional[int] = None,
        CurrencyRate: Optional[int] = None,
        DateCreated: Optional[str] = None,
        DatePaid: Optional[str] = None,
        ID: Optional[str] = None,
        Reference: Optional[str] = None,
        Type: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Updates details of payments related to advanced purchases in the system.

        Args:
            TaskID: Unique identifier for the task. (required)
            Account: Bank or ledger account associated with the task.
            Amount: Monetary amount related to the task.
            CurrencyRate: Exchange rate applied for currency conversion.
            DateCreated: Creation date of the task.
            DatePaid: Date when the payment was completed.
            ID: Resource identifier.
            Reference: Reference number or code associated with the task.
            Type: The type/category of the task.
        Returns:
            API response as a dictionary.
        """
        ...

    def update_advanced_purchase_stock(
        self,
        PurchaseID: str,
        Status: str,
        TaskID: str,
        Lines: Optional[List[Any]] = None,
    ) -> Dict[str, Any]:
        """Updates details of stock records related to advanced purchases in the system.

        Args:
            PurchaseID: Unique identifier for the purchase order. (required)
            Status: Current status of the purchase (e.g., DRAFT or AUTHORISED). (required)
            TaskID: Internal task identifier associated with this purchase. (required)
            Lines: 
        Returns:
            API response as a dictionary.
        """
        ...

    def update_customer(
        self,
        AccountReceivable: Optional[str] = None,
        AdditionalAttribute1: Optional[str] = None,
        AdditionalAttribute10: Optional[str] = None,
        AdditionalAttribute2: Optional[str] = None,
        AdditionalAttribute3: Optional[str] = None,
        AdditionalAttribute4: Optional[str] = None,
        AdditionalAttribute5: Optional[str] = None,
        AdditionalAttribute6: Optional[str] = None,
        AdditionalAttribute7: Optional[str] = None,
        AdditionalAttribute8: Optional[str] = None,
        AdditionalAttribute9: Optional[str] = None,
        Addresses: Optional[List[Any]] = None,
        AttributeSet: Optional[str] = None,
        Carrier: Optional[str] = None,
        Comments: Optional[str] = None,
        Contacts: Optional[List[Any]] = None,
        CreditLimit: Optional[float] = None,
        Currency: Optional[str] = None,
        Discount: Optional[float] = None,
        DisplayName: Optional[str] = None,
        ID: Optional[str] = None,
        IsOnCreditHold: Optional[bool] = None,
        LastModifiedOn: Optional[str] = None,
        Location: Optional[str] = None,
        Name: Optional[str] = None,
        PaymentTerm: Optional[str] = None,
        PriceTier: Optional[str] = None,
        ProductPrices: Optional[List[Any]] = None,
        RevenueAccount: Optional[str] = None,
        SalesRepresentative: Optional[str] = None,
        Status: Optional[str] = None,
        Tags: Optional[str] = None,
        TaxNumber: Optional[str] = None,
        TaxRule: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Updates an existing customer profile in the system.

        Args:
            AccountReceivable: 
            AdditionalAttribute1: 
            AdditionalAttribute10: 
            AdditionalAttribute2: 
            AdditionalAttribute3: 
            AdditionalAttribute4: 
            AdditionalAttribute5: 
            AdditionalAttribute6: 
            AdditionalAttribute7: 
            AdditionalAttribute8: 
            AdditionalAttribute9: 
            Addresses: 
            AttributeSet: 
            Carrier: 
            Comments: 
            Contacts: 
            CreditLimit: 
            Currency: 
            Discount: 
            DisplayName: 
            ID: 
            IsOnCreditHold: 
            LastModifiedOn: 
            Location: 
            Name: 
            PaymentTerm: 
            PriceTier: 
            ProductPrices: 
            RevenueAccount: 
            SalesRepresentative: 
            Status: 
            Tags: 
            TaxNumber: 
            TaxRule: 
        Returns:
            API response as a dictionary.
        """
        ...

    def update_products(
        self,
        ID: str,
        AdditionalAttribute1: Optional[str] = None,
        AdditionalAttribute10: Optional[str] = None,
        AdditionalAttribute2: Optional[str] = None,
        AdditionalAttribute3: Optional[str] = None,
        AdditionalAttribute4: Optional[str] = None,
        AdditionalAttribute5: Optional[str] = None,
        AdditionalAttribute6: Optional[str] = None,
        AdditionalAttribute7: Optional[str] = None,
        AdditionalAttribute8: Optional[str] = None,
        AdditionalAttribute9: Optional[str] = None,
        AlwaysShowQuantity: Optional[str] = None,
        AttributeSet: Optional[str] = None,
        AverageCost: Optional[float] = None,
        Barcode: Optional[str] = None,
        Brand: Optional[str] = None,
        COGSAccount: Optional[str] = None,
        Category: Optional[str] = None,
        CostingMethod: Optional[str] = None,
        DefaultLocation: Optional[str] = None,
        Description: Optional[str] = None,
        DiscountRule: Optional[str] = None,
        DropShipMode: Optional[str] = None,
        ExpenseAccount: Optional[str] = None,
        Height: Optional[float] = None,
        InventoryAccount: Optional[str] = None,
        LastModifiedOn: Optional[str] = None,
        Length: Optional[float] = None,
        MinimumBeforeReorder: Optional[float] = None,
        Name: Optional[str] = None,
        PickZones: Optional[str] = None,
        PriceTier1: Optional[float] = None,
        PriceTier10: Optional[float] = None,
        PriceTier2: Optional[float] = None,
        PriceTier3: Optional[float] = None,
        PriceTier4: Optional[float] = None,
        PriceTier5: Optional[float] = None,
        PriceTier6: Optional[float] = None,
        PriceTier7: Optional[float] = None,
        PriceTier8: Optional[float] = None,
        PriceTier9: Optional[float] = None,
        PriceTiers: Optional[Dict[str, Any]] = None,
        PurchaseTaxRule: Optional[str] = None,
        ReorderQuantity: Optional[float] = None,
        RevenueAccount: Optional[str] = None,
        SKU: Optional[str] = None,
        SaleTaxRule: Optional[str] = None,
        Sellable: Optional[bool] = None,
        Status: Optional[str] = None,
        StockLocator: Optional[str] = None,
        Tags: Optional[str] = None,
        Type: Optional[str] = None,
        UOM: Optional[str] = None,
        Weight: Optional[float] = None,
        Width: Optional[float] = None,
    ) -> Dict[str, Any]:
        """Updates existing products in the system based on provided details.

        Args:
            ID:  (required)
            AdditionalAttribute1: 
            AdditionalAttribute10: 
            AdditionalAttribute2: 
            AdditionalAttribute3: 
            AdditionalAttribute4: 
            AdditionalAttribute5: 
            AdditionalAttribute6: 
            AdditionalAttribute7: 
            AdditionalAttribute8: 
            AdditionalAttribute9: 
            AlwaysShowQuantity: 
            AttributeSet: 
            AverageCost: 
            Barcode: 
            Brand: 
            COGSAccount: 
            Category: 
            CostingMethod: 
            DefaultLocation: 
            Description: 
            DiscountRule: 
            DropShipMode: 
            ExpenseAccount: 
            Height: 
            InventoryAccount: 
            LastModifiedOn: 
            Length: 
            MinimumBeforeReorder: 
            Name: 
            PickZones: 
            PriceTier1: 
            PriceTier10: 
            PriceTier2: 
            PriceTier3: 
            PriceTier4: 
            PriceTier5: 
            PriceTier6: 
            PriceTier7: 
            PriceTier8: 
            PriceTier9: 
            PriceTiers: 
            PurchaseTaxRule: 
            ReorderQuantity: 
            RevenueAccount: 
            SKU: 
            SaleTaxRule: 
            Sellable: 
            Status: 
            StockLocator: 
            Tags: 
            Type: 
            UOM: 
            Weight: 
            Width: 
        Returns:
            API response as a dictionary.
        """
        ...

    def update_purchase(
        self,
        AdditionalAttributes: Optional[Dict[str, Any]] = None,
        Approach: Optional[str] = None,
        BillingAddress: Optional[Dict[str, Any]] = None,
        BlindReceipt: Optional[bool] = None,
        Contact: Optional[str] = None,
        CurrencyRate: Optional[int] = None,
        ID: Optional[str] = None,
        Location: Optional[str] = None,
        Note: Optional[str] = None,
        Phone: Optional[str] = None,
        RequiredBy: Optional[str] = None,
        ShippingAddress: Optional[Dict[str, Any]] = None,
        Supplier: Optional[str] = None,
        SupplierID: Optional[str] = None,
        TaxCalculation: Optional[str] = None,
        TaxRule: Optional[str] = None,
        Terms: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Updates details of a specific purchase in the system.

        Args:
            AdditionalAttributes: 
            Approach: 
            BillingAddress: 
            BlindReceipt: 
            Contact: 
            CurrencyRate: 
            ID: 
            Location: 
            Note: 
            Phone: 
            RequiredBy: 
            ShippingAddress: 
            Supplier: 
            SupplierID: 
            TaxCalculation: 
            TaxRule: 
            Terms: 
        Returns:
            API response as a dictionary.
        """
        ...

    def update_sale_fulfillment_pack(
        self,
        Status: str,
        TaskID: str,
        Lines: Optional[List[Any]] = None,
    ) -> Dict[str, Any]:
        """Updates an existing fulfillment pack in the system.

        Args:
            Status: Current status of the task. (required)
            TaskID: Unique identifier for the task. (required)
            Lines: 
        Returns:
            API response as a dictionary.
        """
        ...

    def update_sale_fulfillment_pick(
        self,
        Status: str,
        TaskID: str,
        AutoPickMode: Optional[str] = None,
        Lines: Optional[List[Any]] = None,
    ) -> Dict[str, Any]:
        """Updates an existing fulfillment pick in the system.

        Args:
            Status: Current status of the task. (required)
            TaskID: Unique identifier for the task. (required)
            AutoPickMode: Mode for automatic picking process.
            Lines: 
        Returns:
            API response as a dictionary.
        """
        ...

    def update_sale_fulfillment_ship(
        self,
        Lines: List[Any],
        Status: str,
        TaskID: str,
        AddTrackingNumbers: Optional[bool] = None,
        RequireBy: Optional[str] = None,
        ShippingAddress: Optional[Dict[str, Any]] = None,
        ShippingNotes: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Updates an existing shipment's details in the system.

        Args:
            Lines:  (required)
            Status: Current status of the task. (required)
            TaskID: Unique identifier for the task. (required)
            AddTrackingNumbers: Flag indicating whether to add tracking numbers.
            RequireBy: The date by which the action is required.
            ShippingAddress: Destination address for shipment.
            ShippingNotes: Additional notes related to shipping.
        Returns:
            API response as a dictionary.
        """
        ...

    def update_sale_invoice(
        self,
        SaleID: str,
        TaskID: str,
        AdditionalCharges: Optional[List[Any]] = None,
        BillingAddressLine1: Optional[str] = None,
        BillingAddressLine2: Optional[str] = None,
        CombineAdditionalCharges: Optional[bool] = None,
        CurrencyConversionRate: Optional[float] = None,
        InvoiceDate: Optional[str] = None,
        InvoiceDueDate: Optional[str] = None,
        Lines: Optional[List[Any]] = None,
        LinkedFulfillmentNumber: Optional[str] = None,
        Memo: Optional[str] = None,
        Status: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Updates the details of an existing sale invoice in the system.

        Args:
            SaleID: Unique identifier for the sale. (required)
            TaskID: Identifier for the related task. (required)
            AdditionalCharges: 
            BillingAddressLine1: First line of the billing address.
            BillingAddressLine2: Second line of the billing address.
            CombineAdditionalCharges: Flag to indicate if additional charges should be combined.
            CurrencyConversionRate: Rate used to convert currencies as needed.
            InvoiceDate: Date when the invoice was issued.
            InvoiceDueDate: Due date for the invoice payment.
            Lines: 
            LinkedFulfillmentNumber: Reference number for linked fulfillment.
            Memo: Additional notes or comments regarding the sale.
            Status: Current status of the sale.
        Returns:
            API response as a dictionary.
        """
        ...

    def update_stock_adjustment(
        self,
        EffectiveDate: str,
        Status: str,
        TaskID: str,
        Account: Optional[str] = None,
        Lines: Optional[List[Any]] = None,
        Reference: Optional[str] = None,
        StocktakeNumber: Optional[str] = None,
        UpdateOnHand: Optional[bool] = None,
    ) -> Dict[str, Any]:
        """Updates an existing stock adjustment record in the system.

        Args:
            EffectiveDate: The date when the task or data becomes effective. (required)
            Status: Current status of the task or inventory item. (required)
            TaskID: Unique identifier for the task. (required)
            Account: Account associated with the inventory or task.
            Lines: 
            Reference: Reference information related to the task.
            StocktakeNumber: Identifier for the stocktake operation.
            UpdateOnHand: Flag indicating whether to update the on-hand stock.
        Returns:
            API response as a dictionary.
        """
        ...

    def update_stock_transfer(
        self,
        From: str,
        Lines: List[Any],
        Status: str,
        TaskID: str,
        CompletionDate: Optional[str] = None,
        CostDistributionType: Optional[str] = None,
        DepartureDate: Optional[str] = None,
        FromLocation: Optional[str] = None,
        InTransitAccount: Optional[str] = None,
        ManualJournals: Optional[List[Any]] = None,
        Reference: Optional[str] = None,
        RequiredByDate: Optional[str] = None,
        SkipOrder: Optional[bool] = None,
        To: Optional[str] = None,
        ToLocation: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Updates an existing stock transfer in the system.

        Args:
            From: Origin location or entity. (required)
            Lines:  (required)
            Status: Current status of the task. (required)
            TaskID: The identifier for the specific task. (required)
            CompletionDate: Expected or actual completion date.
            CostDistributionType: Method of distributing costs.
            DepartureDate: Scheduled date of departure.
            FromLocation: Detailed origin location.
            InTransitAccount: Account associated with in-transit inventory.
            ManualJournals: List of manual journal entries.
            Reference: Reference number or code.
            RequiredByDate: Date by which completion is required.
            SkipOrder: Flag to skip order processing.
            To: Destination location or entity.
            ToLocation: Detailed destination location.
        Returns:
            API response as a dictionary.
        """
        ...

    def update_webhook(
        self,
        ExternalAuthorizationType: str,
        ExternalURL: str,
        ID: str,
        IsActive: bool,
        ExternalBearerToken: Optional[str] = None,
        ExternalHeaders: Optional[List[Any]] = None,
        ExternalPassword: Optional[str] = None,
        ExternalUserName: Optional[str] = None,
        Name: Optional[str] = None,
        Type: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Updates an existing webhook configuration in the system.

        Args:
            ExternalAuthorizationType: Type of external authorization used. (required)
            ExternalURL: External URL associated with the record, if applicable. (required)
            ID: Unique identifier of the record in Cin7. (required)
            IsActive: Indicates whether the item is active. (required)
            ExternalBearerToken: Bearer token for external authentication.
            ExternalHeaders: 
            ExternalPassword: Password for external authentication, if applicable.
            ExternalUserName: Username for external authentication, if applicable.
            Name: Human-readable name for the item.
            Type: The type/category of the record to process.
        Returns:
            API response as a dictionary.
        """
        ...

    def updatet_stock_take(
        self,
        Status: str,
        TaskID: str,
        Account: Optional[str] = None,
        Bins: Optional[List[Any]] = None,
        Brands: Optional[List[Any]] = None,
        Categories: Optional[List[Any]] = None,
        EffectiveDate: Optional[str] = None,
        Location: Optional[str] = None,
        LocationID: Optional[str] = None,
        NonZeroStockOnHandProducts: Optional[List[Any]] = None,
        PickZones: Optional[List[Any]] = None,
        Reference: Optional[str] = None,
        StockLocators: Optional[List[Any]] = None,
        Tags: Optional[List[Any]] = None,
        UseRelativeQuantity: Optional[bool] = None,
        ZeroStockOnHandProducts: Optional[List[Any]] = None,
    ) -> Dict[str, Any]:
        """Updates an existing stock take in the system.

        Args:
            Status: Current status of the task. (required)
            TaskID: Unique identifier for the task. (required)
            Account: Account associated with the task.
            Bins: List of bins.
            Brands: List of brands.
            Categories: 
            EffectiveDate: The date when the task becomes effective.
            Location: Name or details of the location.
            LocationID: Identifier for the location.
            NonZeroStockOnHandProducts: 
            PickZones: Array of pick zones.
            Reference: Reference identifier.
            StockLocators: Array of stock locators.
            Tags: Array of tags associated with the task.
            UseRelativeQuantity: Flag to determine if relative quantities are used.
            ZeroStockOnHandProducts: 
        Returns:
            API response as a dictionary.
        """
        ...

