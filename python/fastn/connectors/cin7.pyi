"""Fastn Cin7 connector — auto-generated type stubs.

Do not edit manually. Regenerate with `fastn connector sync`.
"""
from __future__ import annotations

from typing import Any, Dict, List, Optional, TypedDict


class _Cin7CreateAdvancedPurchaseAdditionalattributes(TypedDict, total=False):
    AdditionalAttribute1: str
    AdditionalAttribute10: str
    AdditionalAttribute2: str
    AdditionalAttribute3: str
    AdditionalAttribute4: str
    AdditionalAttribute5: str
    AdditionalAttribute6: str
    AdditionalAttribute7: str
    AdditionalAttribute8: str
    AdditionalAttribute9: str

class _Cin7CreateAdvancedPurchaseBillingaddress(TypedDict, total=False):
    City: str
    Country: str
    Line1: str
    Line2: str
    Postcode: str
    State: str

class _Cin7CreateAdvancedPurchaseShippingaddress(TypedDict, total=False):
    City: str
    Country: str
    Line1: str
    Line2: str
    Postcode: str
    ShipToOther: bool
    State: str

class _Cin7CreateProductPricetiers(TypedDict, total=False):
    Tier_1: float
    Tier_10: float
    Tier_2: float
    Tier_3: float
    Tier_4: float
    Tier_5: float
    Tier_6: float
    Tier_7: float
    Tier_8: float
    Tier_9: float

class _Cin7CreateSaleAdditionalattributes(TypedDict, total=False):
    AdditionalAttribute1: str
    AdditionalAttribute10: str
    AdditionalAttribute2: str
    AdditionalAttribute3: str
    AdditionalAttribute4: str
    AdditionalAttribute5: str
    AdditionalAttribute6: str
    AdditionalAttribute7: str
    AdditionalAttribute8: str
    AdditionalAttribute9: str

class _Cin7CreateSaleBillingaddress(TypedDict, total=False):
    City: str
    Country: str
    Line1: str
    Line2: str
    Postcode: str
    State: str

class _Cin7CreateSaleShippingaddress(TypedDict, total=False):
    City: str
    Company: str
    Contact: str
    Country: str
    Line1: str
    Line2: str
    Postcode: str
    ShipToOther: bool
    State: str

class _Cin7CreateSaleFulfillmentShipShippingaddress(TypedDict, total=False):
    City: str
    Company: str
    Contact: str
    Country: str
    DisplayAddressLine1: str
    DisplayAddressLine2: str
    ID: str
    Line1: str
    Line2: str
    Postcode: str
    ShipToOther: bool
    State: str

class _Cin7UpdateAdvancedPurchaseAdditionalattributes(TypedDict, total=False):
    AdditionalAttribute1: str
    AdditionalAttribute10: str
    AdditionalAttribute2: str
    AdditionalAttribute3: str
    AdditionalAttribute4: str
    AdditionalAttribute5: str
    AdditionalAttribute6: str
    AdditionalAttribute7: str
    AdditionalAttribute8: str
    AdditionalAttribute9: str

class _Cin7UpdateAdvancedPurchaseBillingaddress(TypedDict, total=False):
    City: str
    Country: str
    Line1: str
    Line2: str
    Postcode: str
    State: str

class _Cin7UpdateAdvancedPurchaseShippingaddress(TypedDict, total=False):
    City: str
    Country: str
    Line1: str
    Line2: str
    Postcode: str
    ShipToOther: bool
    State: str

class _Cin7UpdateProductsPricetiers(TypedDict, total=False):
    Tier_1: float
    Tier_10: float
    Tier_2: float
    Tier_3: float
    Tier_4: float
    Tier_5: float
    Tier_6: float
    Tier_7: float
    Tier_8: float
    Tier_9: float

class _Cin7UpdatePurchaseAdditionalattributes(TypedDict, total=False):
    AdditionalAttribute1: str
    AdditionalAttribute10: str
    AdditionalAttribute2: str
    AdditionalAttribute3: str
    AdditionalAttribute4: str
    AdditionalAttribute5: str
    AdditionalAttribute6: str
    AdditionalAttribute7: str
    AdditionalAttribute8: str
    AdditionalAttribute9: str

class _Cin7UpdatePurchaseBillingaddress(TypedDict, total=False):
    City: str
    Country: str
    Line1: str
    Line2: str
    Postcode: str
    State: str

class _Cin7UpdatePurchaseShippingaddress(TypedDict, total=False):
    City: str
    Country: str
    Line1: str
    Line2: str
    Postcode: str
    ShipToOther: bool
    State: str

class _Cin7UpdateSaleFulfillmentShipShippingaddress(TypedDict, total=False):
    City: str
    Company: str
    Contact: str
    Country: str
    DisplayAddressLine1: str
    DisplayAddressLine2: str
    ID: str
    Line1: str
    Line2: str
    Postcode: str
    ShipToOther: bool
    State: str

class Cin7Connector:
    """Cin7 connector ().

    Provides 88 tools.
    """

    def cin7_create_advanced_purchase(
        self,
        Approach: str,
        Location: str,
        Supplier: str,
        SupplierID: str,
        TaxRule: str,
        AdditionalAttributes: Optional[_Cin7CreateAdvancedPurchaseAdditionalattributes] = None,
        BillingAddress: Optional[_Cin7CreateAdvancedPurchaseBillingaddress] = None,
        BlindReceipt: Optional[bool] = None,
        Contact: Optional[str] = None,
        CurrencyRate: Optional[int] = None,
        Note: Optional[str] = None,
        Phone: Optional[str] = None,
        PurchaseType: Optional[str] = None,
        RequiredBy: Optional[str] = None,
        ShippingAddress: Optional[_Cin7CreateAdvancedPurchaseShippingaddress] = None,
        TaxCalculation: Optional[str] = None,
        Terms: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Creates a new advanced purchase record in Cin7. Use this when purchasing goods under an advanced purchase workflow that includes separate steps for invoicing, stock receipts, and payments. Do not use this for standard purchase orders — use the standard purchase tools instead. This operation initiates a multi-step procurement process.

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

    def cin7_create_advanced_purchase_credit_note(
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
        """Creates a credit note for an advanced purchase in Cin7, typically to record a supplier credit or return. Use this when a supplier issues a credit against an advanced purchase. Do not use this for sale credit notes — use cin7_create_credit_note instead. This operation creates a financial record that may affect accounts payable.

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

    def cin7_create_advanced_purchase_invoice(
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
        """Creates a supplier invoice for an advanced purchase in Cin7. Use this to record a payable invoice against an advanced purchase order. Do not use this for sale invoices — use cin7_create_sale_invoice instead. This operation creates a financial liability in the system.

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

    def cin7_create_advanced_purchase_manual_journals(
        self,
        PurchaseID: str,
        Status: str,
        TaskID: str,
        Lines: Optional[List[Any]] = None,
    ) -> Dict[str, Any]:
        """Creates a manual journal entry associated with an advanced purchase in Cin7. Use this to post accounting adjustments or corrections related to an advanced purchase. Do not use this for standard invoice or payment entries — use the dedicated invoice and payment tools instead. This operation creates a financial record in the system.

        Args:
            PurchaseID: Unique identifier for the purchase. (required)
            Status: Current status to assign for the purchase/task. (required)
            TaskID: Identifier for the associated task. (required)
            Lines: 
        Returns:
            API response as a dictionary.
        """
        ...

    def cin7_create_advanced_purchase_payments(
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
        """Creates new payment records associated with an advanced purchase in Cin7. Use this to record a payment against an advanced purchase order. Do not use this to update an existing payment — use cin7_update_advanced_purchase_payments instead. This operation adds a financial transaction to the advanced purchase.

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

    def cin7_create_advanced_purchase_put_away(
        self,
        PurchaseID: str,
        Status: str,
        Lines: Optional[List[Any]] = None,
        TaskID: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Creates a put-away record for received stock associated with an advanced purchase in Cin7. Use this to assign received inventory to specific warehouse locations after a purchase receipt. Do not use this for standard purchase put-aways outside the advanced purchase workflow. This operation updates inventory location data.

        Args:
            PurchaseID: Unique identifier for the purchase. (required)
            Status: Current status of the purchase (DRAFT or AUTHORISED). (required)
            Lines: 
            TaskID: Optional task identifier related to this operation.
        Returns:
            API response as a dictionary.
        """
        ...

    def cin7_create_advanced_purchase_stock(
        self,
        PurchaseID: str,
        Status: str,
        Lines: Optional[List[Any]] = None,
        TaskID: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Creates stock receipt records associated with an advanced purchase in Cin7. Use this to record received inventory against an advanced purchase order. Do not use this to update existing stock records — use cin7_update_advanced_purchase_stock instead. This operation increases inventory levels in Cin7.

        Args:
            PurchaseID: Identifier for the Purchase record. (required)
            Status: Current status of the purchase/task. (required)
            Lines: 
            TaskID: Identifier for the related Task.
        Returns:
            API response as a dictionary.
        """
        ...

    def cin7_create_carrier(
        self,
        Description: str,
    ) -> Dict[str, Any]:
        """Creates a new carrier record in Cin7. Use this to add a shipping carrier that can be assigned to fulfillments and shipments. Do not use this to update an existing carrier — use cin7_update_carrier instead. This operation permanently adds a new carrier to the system.

        Args:
            Description: A descriptive name or details for the carrier. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def cin7_create_credit_note(
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
        """Issues a credit note against a sale in Cin7, typically to record a customer refund or return. Use this when a customer is owed a credit against a previously invoiced sale. Do not use this for supplier credit notes — use cin7_create_advanced_purchase_credit_note instead. This operation creates an accounts receivable credit that may affect financial reporting.

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

    def cin7_create_customer(
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
        """Creates a new customer profile in Cin7, including contact details, billing address, and payment terms. Use this to onboard a new customer before creating sales or invoices for them. Do not use this to update an existing customer — use cin7_update_customer instead.

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

    def cin7_create_product(
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
        PriceTiers: Optional[_Cin7CreateProductPricetiers] = None,
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
        """Creates a new product record in Cin7, including SKU, name, category, and pricing details. Use this to add a product to the catalog before it can be sold or purchased. Do not use this to update an existing product — use cin7_update_products instead.

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

    def cin7_create_sale(
        self,
        Customer: str,
        CustomerID: str,
        AdditionalAttributes: Optional[_Cin7CreateSaleAdditionalattributes] = None,
        AutoPickPackShipMode: Optional[str] = None,
        BillingAddress: Optional[_Cin7CreateSaleBillingaddress] = None,
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
        ShippingAddress: Optional[_Cin7CreateSaleShippingaddress] = None,
        ShippingNotes: Optional[str] = None,
        SkipQuote: Optional[str] = None,
        TaxInclusive: Optional[str] = None,
        TaxRule: Optional[str] = None,
        Terms: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Creates a new top-level sale record in Cin7. Use this to initiate a sale transaction that can then have orders, invoices, fulfillments, and payments added to it. Do not use this to create a sale order or quote directly — use cin7_create_sale_order or cin7_create_sale_quote instead.

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

    def cin7_create_sale_fulfillment(
        self,
        SaleID: str,
    ) -> Dict[str, Any]:
        """Creates a new fulfillment record for a sale in Cin7, initiating the pick, pack, and ship workflow. Use this after a sale order is confirmed and ready to be dispatched. Do not use this to update an existing fulfillment — use the dedicated update tools for each fulfillment stage. This operation allocates stock against the sale.

        Args:
            SaleID: Identifier of the sale record in Cin7. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def cin7_create_sale_fulfillment_pack(
        self,
        Lines: List[Any],
        Status: str,
        TaskID: str,
    ) -> Dict[str, Any]:
        """Creates a new packing record within a sale fulfillment in Cin7. Use this to record that items have been packed for shipment as part of a fulfillment. Do not use this to update an existing pack record — use cin7_update_sale_fulfillment_pack instead.

        Args:
            Lines:  (required)
            Status: Current status of the task. (required)
            TaskID: Unique identifier for the task. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def cin7_create_sale_fulfillment_pick(
        self,
        Status: str,
        TaskID: str,
        AutoPickMode: Optional[str] = None,
        Lines: Optional[List[Any]] = None,
    ) -> Dict[str, Any]:
        """Creates a new pick record within a sale fulfillment in Cin7. Use this to record that items have been picked from the warehouse for a sale fulfillment. Do not use this to update an existing pick — use cin7_update_sale_fulfillment_pick instead.

        Args:
            Status: Current status of the task. (required)
            TaskID: A unique identifier for the task. (required)
            AutoPickMode: Mode for automatic picking process.
            Lines: 
        Returns:
            API response as a dictionary.
        """
        ...

    def cin7_create_sale_fulfillment_ship(
        self,
        Lines: List[Any],
        Status: str,
        TaskID: str,
        RequireBy: Optional[str] = None,
        ShippingAddress: Optional[_Cin7CreateSaleFulfillmentShipShippingaddress] = None,
        ShippingNotes: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Creates a new shipment record within a sale fulfillment in Cin7. Use this to record that goods have been shipped to a customer as part of a sale fulfillment. Do not use this to update an existing shipment — use cin7_update_sale_fulfillment_ship instead. This operation updates inventory dispatch records.

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

    def cin7_create_sale_invoice(
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
        """Creates a new invoice for a sale in Cin7. Use this to generate a customer invoice from a sale order. Do not use this for supplier invoices — use cin7_create_advanced_purchase_invoice instead. This operation creates an accounts receivable record and may trigger downstream accounting entries.

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

    def cin7_create_sale_order(
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
        """Creates a new sale order in Cin7, confirming a customers intent to purchase. Use this after a quote has been accepted or when creating an order directly. Do not use this to create a quote — use cin7_create_sale_quote instead. Creating a sale order may allocate stock.

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

    def cin7_create_sale_payment(
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
        """Records a payment received against a sale in Cin7. Use this to mark a sale invoice as partially or fully paid. Do not use this to create a supplier payment — use cin7_create_advanced_purchase_payments instead. This operation reduces the outstanding accounts receivable balance.

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

    def cin7_create_sale_quote(
        self,
        AdditionalCharges: Optional[List[Any]] = None,
        CombineAdditionalCharges: Optional[bool] = None,
        Lines: Optional[List[Any]] = None,
        Memo: Optional[str] = None,
        Prepayments: Optional[List[Any]] = None,
        SaleID: Optional[str] = None,
        Status: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Creates a new sale quote in Cin7 for a prospective customer order. Use this to generate a quote before converting it to a sale order. Do not use this to create a confirmed sale order — use cin7_create_sale_order instead. Creating a quote does not commit stock or generate an invoice.

        Args:
            AdditionalCharges: 
            CombineAdditionalCharges: 
            Lines: 
            Memo: 
            Prepayments: 
            SaleID: 
            Status: 
        Returns:
            API response as a dictionary.
        """
        ...

    def cin7_create_stock_adjustment(
        self,
        EffectiveDate: str,
        Status: str,
        Account: Optional[str] = None,
        Lines: Optional[List[Any]] = None,
        Reference: Optional[str] = None,
        StocktakeNumber: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Creates a new stock adjustment record in Cin7 to manually increase or decrease inventory levels. Use this to correct stock discrepancies or record write-offs. Do not use this for stock takes — use cin7_create_stock_take instead. Posting the adjustment will permanently update inventory levels.

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

    def cin7_create_stock_take(
        self,
        EffectiveDate: str,
        Location: str,
        Account: Optional[str] = None,
        Categories: Optional[List[Any]] = None,
        LocationID: Optional[str] = None,
        Reference: Optional[str] = None,
        Tags: Optional[List[Any]] = None,
    ) -> Dict[str, Any]:
        """Creates a new stock take record in Cin7 to count and reconcile physical inventory against system records. Use this to initiate a stock count. Do not use this to update an existing stock take — use cin7_update_stock_take instead. Completing a stock take may adjust inventory levels in the system.

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

    def cin7_create_stock_transfer(
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
        """Creates a new stock transfer record in Cin7 to move inventory between warehouse locations. Use this to initiate the top-level stock transfer. Do not confuse this with cin7_create_stock_transfer_order, which creates the order sub-resource. This operation initiates an inventory movement between locations.

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

    def cin7_create_stock_transfer_order(
        self,
        Lines: List[Any],
        Status: str,
        TaskID: str,
    ) -> Dict[str, Any]:
        """Creates a new stock transfer order in Cin7 to move inventory between warehouse locations. Use this to initiate a transfer of stock from one location to another. Do not use this for the top-level stock transfer record — use cin7_create_stock_transfer instead. This operation reserves stock for transfer.

        Args:
            Lines:  (required)
            Status: Current status of the task. (required)
            TaskID: Unique identifier for the task. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def cin7_create_webhook(
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
        """Registers a new webhook in Cin7 to receive event notifications at a specified URL. Use this to subscribe to Cin7 events such as sale creation or stock changes. Do not use this to update an existing webhook — use cin7_update_webhook instead. The webhook will begin receiving events immediately after creation.

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

    def cin7_delete_advanced_purchase(
        self,
        ID: str,
        Void: Optional[bool] = None,
    ) -> Dict[str, Any]:
        """Permanently deletes an advanced purchase record from Cin7. Use this only when an advanced purchase was created in error and has no associated invoices, payments, or stock receipts. Do not use this on active or partially fulfilled advanced purchases. This action is irreversible.

        Args:
            ID: Unique identifier for the resource. (required)
            Void: Indicates whether the operation should be voided.
        Returns:
            API response as a dictionary.
        """
        ...

    def cin7_delete_advanced_purchase_credit_note(
        self,
        TaskID: str,
    ) -> Dict[str, Any]:
        """Permanently deletes a credit note associated with an advanced purchase from Cin7. Use this only to remove an erroneous credit note before it has been applied. Do not use this if the credit note has already been reconciled. This action is irreversible.

        Args:
            TaskID: Identifier for the specific task to operate on. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def cin7_delete_advanced_purchase_invoice(
        self,
        TaskID: str,
        Void: Optional[bool] = None,
    ) -> Dict[str, Any]:
        """Permanently deletes an invoice associated with an advanced purchase from Cin7. Use this only to remove an incorrect invoice before it has been posted or paid. Do not use this if the invoice is linked to completed payments. This action is irreversible.

        Args:
            TaskID: Unique identifier for the Cin7 task. (required)
            Void: Indicates whether to void the specified task.
        Returns:
            API response as a dictionary.
        """
        ...

    def cin7_delete_advanced_purchase_payments(
        self,
        ID: str,
        DeleteAllocation: Optional[bool] = None,
    ) -> Dict[str, Any]:
        """Permanently deletes a payment record associated with an advanced purchase from Cin7. Use this only when an erroneous payment entry needs to be removed. Do not use this if the payment has already been reconciled or posted to accounting. This action is irreversible — deleted payment records cannot be recovered.

        Args:
            ID: The unique identifier of the allocation to delete. (required)
            DeleteAllocation: Flag indicating whether the allocation should be deleted.
        Returns:
            API response as a dictionary.
        """
        ...

    def cin7_delete_advanced_purchase_stock(
        self,
        TaskID: str,
        Void: Optional[bool] = None,
    ) -> Dict[str, Any]:
        """Permanently deletes a stock record associated with an advanced purchase from Cin7. Use this to remove an incorrect or cancelled stock receipt linked to an advanced purchase. Do not use this if the stock has already been allocated or consumed downstream. This action is irreversible.

        Args:
            TaskID: The unique identifier of the task to operate on. (required)
            Void: Flag indicating whether to void the task.
        Returns:
            API response as a dictionary.
        """
        ...

    def cin7_delete_carrier(
        self,
        ID: str,
    ) -> Dict[str, Any]:
        """Permanently deletes a carrier from Cin7. Use this only when a carrier record is no longer needed. Do not use this if the carrier is referenced by active shipments or fulfillments. This action is irreversible — deleted carriers cannot be recovered.

        Args:
            ID: Identifier of the carrier resource to retrieve or modify. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def cin7_delete_sale(
        self,
        ID: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Permanently deletes a sale record from Cin7. Use this only to remove a sale that was created in error and has no associated invoices, payments, or fulfillments. Do not use this on an active or completed sale. This action is irreversible and may affect revenue reporting.

        Args:
            ID: 
        Returns:
            API response as a dictionary.
        """
        ...

    def cin7_delete_sale_fulfillment(
        self,
        TaskID: str,
        Void: Optional[bool] = None,
    ) -> Dict[str, Any]:
        """Permanently deletes a sale fulfillment record from Cin7. Use this only to remove an erroneous fulfillment that has not been shipped or completed. Do not use this on a fulfillment with associated shipments or stock movements. This action is irreversible.

        Args:
            TaskID: The identifier for the specific task. (required)
            Void: Indicates whether the task should be voided.
        Returns:
            API response as a dictionary.
        """
        ...

    def cin7_delete_sale_invoice(
        self,
        TaskID: str,
        Void: Optional[bool] = None,
    ) -> Dict[str, Any]:
        """Permanently deletes a sale invoice from Cin7. Use this only to remove an erroneous invoice that has not been sent to the customer or reconciled. Do not use this on a paid or partially paid invoice. This action is irreversible and may affect accounts receivable.

        Args:
            TaskID: Unique identifier for the specific task. (required)
            Void: Indicates whether to void the task.
        Returns:
            API response as a dictionary.
        """
        ...

    def cin7_delete_stock_adjustment(
        self,
        ID: str,
        Void: Optional[bool] = None,
    ) -> Dict[str, Any]:
        """Permanently deletes a stock adjustment record from Cin7. Use this only to remove an erroneous adjustment that has not yet been posted. Do not use this on a completed adjustment that has already changed inventory levels. This action is irreversible and may affect stock counts.

        Args:
            ID: Unique identifier for the resource or item. (required)
            Void: Flag indicating whether to void the operation.
        Returns:
            API response as a dictionary.
        """
        ...

    def cin7_delete_stock_take(
        self,
        ID: str,
        Void: Optional[bool] = None,
    ) -> Dict[str, Any]:
        """Permanently deletes a stock take record from Cin7. Use this only to remove an erroneous stock take that has not been completed or posted. Do not use this on a completed stock take that has already adjusted inventory. This action is irreversible.

        Args:
            ID: The identifier for the resource or entity in Cin7. (required)
            Void: Indicator whether the operation is a void action.
        Returns:
            API response as a dictionary.
        """
        ...

    def cin7_delete_stock_transfer(
        self,
        ID: str,
        Void: Optional[bool] = None,
    ) -> Dict[str, Any]:
        """Permanently deletes a stock transfer from Cin7. Use this only when a stock transfer was created in error and has not yet been processed or received. Do not use this on completed or in-transit transfers. This action is irreversible and may affect inventory counts.

        Args:
            ID: Unique identifier for the resource in Cin7. (required)
            Void: Optional parameter to specify void actions, if applicable.
        Returns:
            API response as a dictionary.
        """
        ...

    def cin7_delete_webhook(
        self,
        ID: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Permanently deletes a registered webhook from Cin7. Use this to remove a webhook that is no longer needed or that points to an invalid endpoint. Do not use this if the webhook is still actively receiving events needed by downstream systems. This action is irreversible.

        Args:
            ID: ID parameter for the My connectors API request.
        Returns:
            API response as a dictionary.
        """
        ...

    def cin7_deprecate_product(
        self,
        productId: str,
    ) -> Dict[str, Any]:
        """Marks an existing product as deprecated in Cin7, preventing it from being selected for new sales or purchases. Use this when a product is being discontinued. Do not use this to delete a product — deprecated products remain in the system for historical records. This change takes effect immediately and may prevent future transactions for this product.

        Args:
            productId:  (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def cin7_get_advanced_purchase(
        self,
        ID: str,
        CombineAdditionalCharges: Optional[bool] = None,
    ) -> Dict[str, Any]:
        """Retrieves details of a specific advanced purchase in Cin7, including supplier, line items, and status. Use this to review a single advanced purchase record. Do not use this to list all advanced purchases — apply filters or use a list endpoint. This is a read-only operation with no side effects.

        Args:
            ID: The unique identifier for the record or item being referenced. (required)
            CombineAdditionalCharges: Whether to combine additional charges in the Cin7 request.
        Returns:
            API response as a dictionary.
        """
        ...

    def cin7_get_advanced_purchase_credit_note(
        self,
        PurchaseID: str,
        CombineAdditionalCharges: Optional[bool] = None,
    ) -> Dict[str, Any]:
        """Retrieves credit note details associated with an advanced purchase in Cin7. Use this to review supplier credits linked to a specific advanced purchase. This is a read-only operation with no side effects.

        Args:
            PurchaseID: Identifier of the purchase record to operate on. (required)
            CombineAdditionalCharges: Flag to indicate whether to combine additional charges.
        Returns:
            API response as a dictionary.
        """
        ...

    def cin7_get_advanced_purchase_invoice(
        self,
        PurchaseID: str,
        CombineAdditionalCharges: Optional[bool] = None,
    ) -> Dict[str, Any]:
        """Retrieves invoice details for a specific advanced purchase in Cin7. Use this to review the payable invoice associated with an advanced purchase. Do not use this for sale invoices — use cin7_get_sale_invoice instead. This is a read-only operation with no side effects.

        Args:
            PurchaseID: The identifier for the purchase transaction. (required)
            CombineAdditionalCharges: Flag to determine whether to combine additional charges in the response.
        Returns:
            API response as a dictionary.
        """
        ...

    def cin7_get_advanced_purchase_manual_journals(
        self,
        PurchaseID: str,
    ) -> Dict[str, Any]:
        """Retrieves manual journal entries associated with an advanced purchase in Cin7. Use this to review accounting adjustments linked to a specific advanced purchase. This is a read-only operation with no side effects.

        Args:
            PurchaseID: The unique identifier of the purchase in Cin7. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def cin7_get_advanced_purchase_payments(
        self,
        PurchaseID: str,
        CreditNoteNumber: Optional[str] = None,
        InvoiceNumber: Optional[str] = None,
        OrderNumber: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Retrieves payment details associated with an advanced purchase in Cin7. Use this to review payments recorded against a specific advanced purchase. Do not use this to list all purchases — scope the request to a specific advanced purchase ID. This is a read-only operation with no side effects.

        Args:
            PurchaseID: The unique identifier of the purchase. (required)
            CreditNoteNumber: The unique identifier of the credit note.
            InvoiceNumber: The unique identifier of the invoice.
            OrderNumber: The unique identifier of the order.
        Returns:
            API response as a dictionary.
        """
        ...

    def cin7_get_advanced_purchase_put_away(
        self,
        PurchaseID: str,
    ) -> Dict[str, Any]:
        """Retrieves put-away details for stock associated with an advanced purchase in Cin7. Use this to review where received inventory has been placed in the warehouse. This is a read-only operation with no side effects.

        Args:
            PurchaseID:  (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def cin7_get_advanced_purchase_stock(
        self,
        PurchaseID: str,
    ) -> Dict[str, Any]:
        """Retrieves stock receipt details associated with an advanced purchase in Cin7. Use this to review inventory quantities and details received under an advanced purchase. This is a read-only operation with no side effects.

        Args:
            PurchaseID: The unique identifier for the Cin7 purchase. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def cin7_get_chart_of_accounts(
        self,
        Class: Optional[str] = None,
        Code: Optional[str] = None,
        Limit: Optional[str] = None,
        Name: Optional[str] = None,
        Page: Optional[str] = None,
        Status: Optional[str] = None,
        Type: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Retrieves the chart of accounts from Cin7s financial configuration. Use this to look up valid account codes when posting invoices, payments, or journal entries. This is a read-only reference data operation with no side effects.

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

    def cin7_get_product_availability(
        self,
        batch: Optional[str] = None,
        category: Optional[str] = None,
        limit: Optional[str] = None,
        location: Optional[str] = None,
        page: Optional[str] = None,
        sku: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Checks the availability and stock levels of a specific product in Cin7 across warehouse locations. Use this to determine whether a product is in stock before creating a sale or fulfillment. This is a read-only operation with no side effects.

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

    def cin7_get_purchase(
        self,
        CombineAdditionalCharges: Optional[str] = None,
        ID: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Retrieves the full details of a specific purchase order in Cin7, including line items, supplier, and status. Use this when you need complete information about a single purchase. Do not use this to list multiple purchases — use cin7_list_purchases instead. This is a read-only operation with no side effects.

        Args:
            CombineAdditionalCharges: 
            ID: 
        Returns:
            API response as a dictionary.
        """
        ...

    def cin7_get_sale(
        self,
        CombineAdditionalCharges: Optional[str] = None,
        CountryFormat: Optional[str] = None,
        HideInventoryMovements: Optional[str] = None,
        ID: Optional[str] = None,
        IncludeTransactions: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Retrieves the full details of a specific sale in Cin7, including its status, associated orders, fulfillments, and invoices. Use this to inspect a single sale record. Do not use this to list all sales — use cin7_list_sales instead. This is a read-only operation with no side effects.

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

    def cin7_get_sale_fulfillment(
        self,
        SaleID: str,
        IncludeProductInfo: Optional[bool] = None,
        limit: Optional[int] = None,
        page: Optional[int] = None,
    ) -> Dict[str, Any]:
        """Retrieves fulfillment details for a specific sale in Cin7, including pick, pack, and ship status. Use this to inspect the fulfillment state of a sale. Do not use this for invoice or payment details — use the dedicated sale invoice tools instead. This is a read-only operation.

        Args:
            SaleID: The unique identifier for a sale. (required)
            IncludeProductInfo: Flag to include detailed product information.
            limit: Maximum number of items to return.
            page: Specifies which page of results to retrieve.
        Returns:
            API response as a dictionary.
        """
        ...

    def cin7_get_sale_fulfillment_pack(
        self,
        TaskID: str,
        IncludeProductInfo: Optional[bool] = None,
    ) -> Dict[str, Any]:
        """Retrieves packing details for a specific sale fulfillment in Cin7. Use this to inspect what has been packed for a fulfillment. Do not use this for pick or ship details — use the dedicated pick and ship tools instead. This is a read-only operation with no side effects.

        Args:
            TaskID: Identifier for the specific task to perform. (required)
            IncludeProductInfo: Flag to include detailed product information.
        Returns:
            API response as a dictionary.
        """
        ...

    def cin7_get_sale_fulfillment_pick(
        self,
        TaskID: str,
        IncludeProductInfo: Optional[bool] = None,
    ) -> Dict[str, Any]:
        """Retrieves pick details for a specific sale fulfillment in Cin7. Use this to inspect which items have been picked for a fulfillment. Do not use this for pack or ship details — use the dedicated pack and ship tools instead. This is a read-only operation with no side effects.

        Args:
            TaskID:  (required)
            IncludeProductInfo: 
        Returns:
            API response as a dictionary.
        """
        ...

    def cin7_get_sale_fulfillment_ship(
        self,
        TaskID: str,
    ) -> Dict[str, Any]:
        """Retrieves shipment details for a specific sale fulfillment in Cin7, including carrier, tracking, and shipped quantities. Use this to inspect the shipment component of a fulfillment. Do not use this for pack or pick details — use the dedicated pack and pick tools instead. This is a read-only operation.

        Args:
            TaskID: Unique identifier for the task in Cin7. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def cin7_get_sale_invoice(
        self,
        SaleID: str,
        CombineAdditionalCharges: Optional[bool] = None,
        IncludeProductInfo: Optional[bool] = None,
    ) -> Dict[str, Any]:
        """Retrieves invoice details for a specific sale in Cin7, including line items, amounts, and payment status. Use this to inspect a single sale invoice. Do not use this for supplier invoices — use cin7_get_advanced_purchase_invoice instead. This is a read-only operation with no side effects.

        Args:
            SaleID: Unique identifier for the sale transaction. (required)
            CombineAdditionalCharges: Flag to indicate if additional charges should be combined.
            IncludeProductInfo: Flag to include product information in the response.
        Returns:
            API response as a dictionary.
        """
        ...

    def cin7_get_stock_adjustment(
        self,
        TaskID: str,
    ) -> Dict[str, Any]:
        """Retrieves the details of a specific stock adjustment in Cin7, including quantities, reason, and status. Use this to inspect a single adjustment record. Do not use this to list all adjustments — use cin7_list_stock_adjustments instead. This is a read-only operation with no side effects.

        Args:
            TaskID: Identifier of the task to process. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def cin7_get_stock_take(
        self,
        TaskID: str,
    ) -> Dict[str, Any]:
        """Retrieves the details of a specific stock take in Cin7, including counted quantities and status. Use this to inspect a single stock take record. Do not use this to list all stock takes — use cin7_list_stock_takes instead. This is a read-only operation with no side effects.

        Args:
            TaskID: Unique identifier for the task. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def cin7_get_stock_transfer(
        self,
        TaskID: str,
    ) -> Dict[str, Any]:
        """Retrieves the details of a specific stock transfer in Cin7, including items, quantities, and status. Use this to inspect a single stock transfer record. Do not use this to list all transfers — use cin7_list_stock_transfers instead. This is a read-only operation with no side effects.

        Args:
            TaskID: Identifier for the task to be processed. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def cin7_get_stock_transfer_order(
        self,
        TaskID: str,
    ) -> Dict[str, Any]:
        """Retrieves the details of a specific stock transfer order in Cin7, including items, quantities, and source/destination locations. Use this to review the order component of a stock transfer. Do not use this to retrieve the top-level stock transfer — use cin7_get_stock_transfer instead. This is a read-only operation.

        Args:
            TaskID: Unique identifier for the task you want to perform. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def cin7_list_carriers(
        self,
        CarrierID: Optional[str] = None,
        Description: Optional[str] = None,
        Limit: Optional[str] = None,
        Page: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Retrieves a list of all carriers configured in Cin7. Use this to browse or search available carriers for use in shipments or fulfillments. Do not use this to retrieve a single carrier by ID — filter the results after fetching. This is a read-only operation with no side effects.

        Args:
            CarrierID: Unique identifier of a specific carrier. Provide this to retrieve or act on a single carrier.
            Description: A text description or name of the carrier to filter results or provide context.
            Limit: Maximum number of carrier records to return per page.
            Page: Page number for paginated results when listing carriers.
        Returns:
            API response as a dictionary.
        """
        ...

    def cin7_list_customers(
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
        """Retrieves a paginated list of customers in Cin7. Use this to browse or search for customers by name, email, or other attributes. Do not use this to get the full details of a single customer — filter results after fetching. This is a read-only operation with no side effects.

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

    def cin7_list_locations(
        self,
        Deprecated: Optional[str] = None,
        ID: Optional[str] = None,
        Limit: Optional[str] = None,
        Name: Optional[str] = None,
        Page: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Retrieves all warehouse and storage locations configured in Cin7. Use this to look up valid location IDs when creating stock transfers, adjustments, or purchase receipts. This is a read-only reference data operation with no side effects.

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

    def cin7_list_payment_terms(
        self,
    ) -> Dict[str, Any]:
        """Retrieves all payment terms configured in Cin7 (e.g., Net 30, Due on Receipt). Use this to look up valid payment term options when creating or updating customers, suppliers, or purchase and sale orders. This is a read-only reference data operation with no side effects.
        Returns:
            API response as a dictionary.
        """
        ...

    def cin7_list_price_tiers(
        self,
    ) -> Dict[str, Any]:
        """Retrieves all price tiers configured in Cin7. Use this to look up available pricing tiers when creating or updating products, customers, or sale orders. This is a read-only reference data operation with no side effects.
        Returns:
            API response as a dictionary.
        """
        ...

    def cin7_list_product_categories(
        self,
        Limit: Optional[str] = None,
        Name: Optional[str] = None,
        Page: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Retrieves all product categories configured in Cin7. Use this to look up valid category IDs when creating or updating products. This is a read-only reference data operation with no side effects.

        Args:
            Limit: Number of records per page.
            Name: Name filter for the request.
            Page: Page number for pagination.
        Returns:
            API response as a dictionary.
        """
        ...

    def cin7_list_products(
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
        """Retrieves a list of all products available in Cin7, including SKU, name, category, and pricing. Use this to browse or search the product catalog. Do not use this to check stock levels — use cin7_get_product_availability instead. This is a read-only operation with no side effects.

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

    def cin7_list_purchases(
        self,
        UpdatedSince: Optional[str] = None,
        limit: Optional[str] = None,
        page: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Retrieves a paginated list of purchase orders in Cin7. Use this to browse or filter purchases by date, supplier, or status. Do not use this to retrieve the full details of a single purchase — use cin7_get_purchase instead. This is a read-only operation with no side effects.

        Args:
            UpdatedSince: 
            limit: 
            page: 
        Returns:
            API response as a dictionary.
        """
        ...

    def cin7_list_sales(
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
        """Retrieves a paginated list of sales recorded in Cin7. Use this to browse or filter sales by date, customer, or status. Do not use this to get full details of a single sale — use cin7_get_sale instead. This is a read-only operation with no side effects.

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

    def cin7_list_stock_adjustments(
        self,
        Limit: Optional[int] = None,
        Page: Optional[int] = None,
        Status: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Retrieves a paginated list of stock adjustments in Cin7. Use this to browse or filter adjustments by date, location, or status. Do not use this to get the full details of a single adjustment — use cin7_get_stock_adjustment instead. This is a read-only operation with no side effects.

        Args:
            Limit: Maximum number of items to retrieve.
            Page: Page number of results to fetch.
            Status: Filter by order status.
        Returns:
            API response as a dictionary.
        """
        ...

    def cin7_list_stock_takes(
        self,
        Limit: Optional[int] = None,
        Page: Optional[int] = None,
        Status: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Retrieves a paginated list of stock takes conducted in Cin7. Use this to browse or filter stock takes by date or status. Do not use this to get the full details of a single stock take — use cin7_get_stock_take instead. This is a read-only operation with no side effects.

        Args:
            Limit: Maximum number of items to retrieve per request.
            Page: Page number of the results to retrieve.
            Status: Filter results by status.
        Returns:
            API response as a dictionary.
        """
        ...

    def cin7_list_stock_transfers(
        self,
        Limit: Optional[int] = None,
        Page: Optional[int] = None,
        Search: Optional[str] = None,
        Status: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Retrieves a paginated list of stock transfers in Cin7. Use this to browse or filter transfers by date, location, or status. Do not use this to get full details of a single transfer — use cin7_get_stock_transfer instead. This is a read-only operation with no side effects.

        Args:
            Limit: Maximum number of items to return per request.
            Page: Page number for paginated results.
            Search: Search term to filter results.
            Status: Filter by status of the items.
        Returns:
            API response as a dictionary.
        """
        ...

    def cin7_list_tax_rules(
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
        """Retrieves all tax rules configured in Cin7. Use this to look up valid tax codes when creating or updating products, sales, or purchases. This is a read-only reference data operation with no side effects.

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

    def cin7_list_webhooks(
        self,
        body: Dict[str, Any],
    ) -> Dict[str, Any]:
        """Retrieves all webhooks registered in Cin7. Use this to review existing webhook configurations and their subscribed events. Do not use this to create or update webhooks — use the dedicated create and update tools. This is a read-only operation with no side effects.

        Args:
            body:  (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def cin7_update_advanced_purchase(
        self,
        ID: str,
        Supplier: str,
        TaxRule: str,
        AdditionalAttributes: Optional[_Cin7UpdateAdvancedPurchaseAdditionalattributes] = None,
        BillingAddress: Optional[_Cin7UpdateAdvancedPurchaseBillingaddress] = None,
        BlindReceipt: Optional[bool] = None,
        Contact: Optional[str] = None,
        CurrencyRate: Optional[int] = None,
        Location: Optional[str] = None,
        Note: Optional[str] = None,
        Phone: Optional[str] = None,
        RequiredBy: Optional[str] = None,
        ShippingAddress: Optional[_Cin7UpdateAdvancedPurchaseShippingaddress] = None,
        SupplierID: Optional[str] = None,
        TaxCalculation: Optional[str] = None,
        Terms: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Updates the details of an existing advanced purchase in Cin7 (e.g., supplier, dates, or line items). Use this to amend an advanced purchase that has been created but not yet fully processed. Do not use this to create a new advanced purchase — use cin7_create_advanced_purchase instead.

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

    def cin7_update_advanced_purchase_payments(
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
        """Updates payment records associated with an advanced purchase in Cin7. Use this to modify payment amounts, dates, or references on an existing advanced purchase payment. Do not use this to create a new payment — use cin7_create_advanced_purchase_payments instead. This operation modifies existing financial records.

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

    def cin7_update_advanced_purchase_stock(
        self,
        PurchaseID: str,
        Status: str,
        TaskID: str,
        Lines: Optional[List[Any]] = None,
    ) -> Dict[str, Any]:
        """Updates stock records associated with an advanced purchase in Cin7 (e.g., quantities, batch details, or location). Use this to correct or amend stock receipt information on an advanced purchase. Do not use this to create new stock records — use cin7_create_advanced_purchase_stock instead.

        Args:
            PurchaseID: Unique identifier for the purchase order. (required)
            Status: Current status of the purchase (e.g., DRAFT or AUTHORISED). (required)
            TaskID: Internal task identifier associated with this purchase. (required)
            Lines: 
        Returns:
            API response as a dictionary.
        """
        ...

    def cin7_update_carrier(
        self,
        CarrierID: str,
        Description: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Updates the details of an existing carrier in Cin7 (e.g., carrier name, contact info, or shipping settings). Use this when you need to modify a carrier record that already exists. Do not use this to create a new carrier or delete one. This operation overwrites existing carrier data with the values provided.

        Args:
            CarrierID: Unique identifier for the carrier. Required to reference or update a specific carrier. (required)
            Description: A descriptive name or notes for the carrier.
        Returns:
            API response as a dictionary.
        """
        ...

    def cin7_update_customer(
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
        """Updates the profile details of an existing customer in Cin7 (e.g., contact information, addresses, or payment terms). Use this to modify a customer record that already exists. Do not use this to create a new customer — use cin7_create_customer instead.

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

    def cin7_update_products(
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
        PriceTiers: Optional[_Cin7UpdateProductsPricetiers] = None,
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
        """Updates the details of one or more existing products in Cin7 (e.g., name, SKU, price, or category). Use this to modify product records in bulk or individually. Do not use this to create new products — use cin7_create_product instead. Do not use this to deprecate a product — use cin7_deprecate_product instead.

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

    def cin7_update_purchase(
        self,
        AdditionalAttributes: Optional[_Cin7UpdatePurchaseAdditionalattributes] = None,
        Approach: Optional[str] = None,
        BillingAddress: Optional[_Cin7UpdatePurchaseBillingaddress] = None,
        BlindReceipt: Optional[bool] = None,
        Contact: Optional[str] = None,
        CurrencyRate: Optional[int] = None,
        ID: Optional[str] = None,
        Location: Optional[str] = None,
        Note: Optional[str] = None,
        Phone: Optional[str] = None,
        RequiredBy: Optional[str] = None,
        ShippingAddress: Optional[_Cin7UpdatePurchaseShippingaddress] = None,
        Supplier: Optional[str] = None,
        SupplierID: Optional[str] = None,
        TaxCalculation: Optional[str] = None,
        TaxRule: Optional[str] = None,
        Terms: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Updates the details of an existing purchase order in Cin7 (e.g., quantities, supplier, or line items). Use this when you need to modify a purchase that has already been created. Do not use this to create a new purchase or to update sub-resources such as invoices or payments. This operation overwrites existing purchase data with the values provided.

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

    def cin7_update_sale_fulfillment_pack(
        self,
        Status: str,
        TaskID: str,
        Lines: Optional[List[Any]] = None,
    ) -> Dict[str, Any]:
        """Updates an existing packing record within a sale fulfillment in Cin7. Use this to amend pack details such as carton counts or packed quantities. Do not use this to create a new pack record — use cin7_create_sale_fulfillment_pack instead.

        Args:
            Status: Current status of the task. (required)
            TaskID: Unique identifier for the task. (required)
            Lines: 
        Returns:
            API response as a dictionary.
        """
        ...

    def cin7_update_sale_fulfillment_pick(
        self,
        Status: str,
        TaskID: str,
        AutoPickMode: Optional[str] = None,
        Lines: Optional[List[Any]] = None,
    ) -> Dict[str, Any]:
        """Updates an existing pick record within a sale fulfillment in Cin7. Use this to amend pick details such as quantities or picker assignments. Do not use this to create a new pick record — use cin7_create_sale_fulfillment_pick instead.

        Args:
            Status: Current status of the task. (required)
            TaskID: Unique identifier for the task. (required)
            AutoPickMode: Mode for automatic picking process.
            Lines: 
        Returns:
            API response as a dictionary.
        """
        ...

    def cin7_update_sale_fulfillment_ship(
        self,
        Lines: List[Any],
        Status: str,
        TaskID: str,
        AddTrackingNumbers: Optional[bool] = None,
        RequireBy: Optional[str] = None,
        ShippingAddress: Optional[_Cin7UpdateSaleFulfillmentShipShippingaddress] = None,
        ShippingNotes: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Updates the details of an existing shipment within a sale fulfillment in Cin7 (e.g., carrier, tracking number, or shipped quantities). Use this to amend a shipment record after it has been created. Do not use this to create a new shipment — use cin7_create_sale_fulfillment_ship instead.

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

    def cin7_update_sale_invoice(
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
        """Updates the details of an existing sale invoice in Cin7 (e.g., line items, amounts, or due date). Use this to correct or amend an invoice before it is paid. Do not use this to create a new invoice — use cin7_create_sale_invoice instead.

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

    def cin7_update_stock_adjustment(
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
        """Updates an existing stock adjustment record in Cin7 (e.g., quantities, reason, or location). Use this to correct an adjustment before it has been posted. Do not use this to create a new adjustment — use cin7_create_stock_adjustment instead.

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

    def cin7_update_stock_take(
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
        """Updates an existing stock take record in Cin7 (e.g., counted quantities or notes). Use this to amend a stock take that is still in progress. Do not use this to create a new stock take — use cin7_create_stock_take instead. Changes to a completed stock take may affect inventory valuation.

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

    def cin7_update_stock_transfer(
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
        """Updates an existing stock transfer in Cin7 (e.g., quantities, locations, or reference details). Use this to amend a transfer before it has been completed. Do not use this to create a new transfer — use cin7_create_stock_transfer instead.

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

    def cin7_update_webhook(
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
        """Updates the configuration of an existing webhook in Cin7 (e.g., target URL, subscribed events, or active status). Use this when you need to modify a webhook that has already been registered. Do not use this to create a new webhook — use cin7_create_webhook instead. Changes take effect immediately for future events.

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

