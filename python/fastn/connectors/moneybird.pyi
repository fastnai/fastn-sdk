"""Fastn Moneybird connector — auto-generated type stubs.

Do not edit manually. Regenerate with `fastn connector sync`.
"""
from __future__ import annotations

from typing import Any, Dict, List, Optional, TypedDict


class _MoneybirdCreateContactContact(TypedDict, total=False):
    company_name: str
    email: str
    firstname: str
    lastname: str

class _MoneybirdCreateProductProduct(TypedDict, total=False):
    currency: str
    description: str
    ledger_account_id: str
    price: str
    tax_rate_id: str

class _MoneybirdCreateSalesInvoiceSalesInvoice(TypedDict, total=False):
    contact_id: str
    details_attributes: List[Any]
    invoice_date: str
    reference: str

class _MoneybirdUpdateProductProduct(TypedDict, total=False):
    description: str
    price: str

class MoneybirdConnector:
    """Moneybird connector ().

    Provides 10 tools.
    """

    def moneybird_create_contact(
        self,
        administrationId: str,
        contact: _MoneybirdCreateContactContact,
    ) -> Dict[str, Any]:
        """Creates a new contact in the specified Moneybird administration, enabling the contact to be associated with invoices and other financial records. Use this tool when you need to add a new customer, supplier, or business relation to Moneybird. Do not use this tool to update an existing contact — use the appropriate update tool for that purpose.

        Args:
            administrationId: The administration ID for the Moneybird API endpoint. (required)
            contact: Contact details for the Moneybird API endpoint. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def moneybird_create_product(
        self,
        administrationId: str,
        product: _MoneybirdCreateProductProduct,
    ) -> Dict[str, Any]:
        """Creates a new product in the specified Moneybird administration, enabling it to be referenced in invoices and other financial documents. Use this tool when you need to add a new product or service to the Moneybird catalog. Do not use this tool to update an existing product — use the update product tool for that purpose.

        Args:
            administrationId: ID of the administration. (required)
            product: Product details for the Moneybird API. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def moneybird_create_sales_invoice(
        self,
        administrationId: str,
        sales_invoice: _MoneybirdCreateSalesInvoiceSalesInvoice,
    ) -> Dict[str, Any]:
        """Creates a new sales invoice in the specified Moneybird administration, associating it with a contact and line items. Use this tool when you need to generate an invoice for a customer. Do not use this tool to update or send an existing invoice — use the appropriate update or send tools for those purposes.

        Args:
            administrationId: Administration ID for Moneybird. (required)
            sales_invoice: Details of the sales invoice. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def moneybird_delete_product(
        self,
        administrationId: str,
        productId: str,
    ) -> Dict[str, Any]:
        """Permanently deletes a specific product from the Moneybird administration by its ID. Use this tool when a product needs to be fully removed from the catalog and is no longer in use. Do not use this tool to update product details — use the update product tool for that purpose. This action is irreversible — the deleted product cannot be recovered.

        Args:
            administrationId: ID of the administration. (required)
            productId: ID of the product. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def moneybird_list_administrations(
        self,
    ) -> Dict[str, Any]:
        """Retrieves the list of all Moneybird administrations accessible by the authenticated account. Use this tool when you need to look up administration IDs required as parameters for other Moneybird tools. Do not use this tool to retrieve data within a specific administration — use the appropriate scoped tools for that purpose.
        Returns:
            API response as a dictionary.
        """
        ...

    def moneybird_list_contacts(
        self,
        administrationId: str,
    ) -> Dict[str, Any]:
        """Retrieves a list of contacts from the specified Moneybird administration. Use this tool when you need to browse or search for existing contacts and their details. Do not use this tool to create a new contact — use the create contact tool for that purpose.

        Args:
            administrationId: ID of the administration in Moneybird. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def moneybird_list_document_styles(
        self,
        administrationId: str,
    ) -> Dict[str, Any]:
        """Retrieves the list of document styles available in the specified Moneybird administration, which define the visual formatting applied to invoices and other financial documents. Use this tool when you need to look up available document styles before creating or updating a document. Do not use this tool to retrieve invoices or contacts — use the appropriate sales invoice or contact tools for those purposes.

        Args:
            administrationId: The ID of the administration to access via the Moneybird API. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def moneybird_list_products(
        self,
        administrationId: str,
    ) -> Dict[str, Any]:
        """Retrieves the list of all products available in the specified Moneybird administration. Use this tool when you need to browse or look up product IDs and details before referencing them in invoices or other documents. Do not use this tool to retrieve a single product by ID — use the appropriate get tool if available.

        Args:
            administrationId: ID of the administration for the Moneybird API request. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def moneybird_list_sales_invoices(
        self,
        administrationId: str,
    ) -> Dict[str, Any]:
        """Retrieves a list of all sales invoices from the specified Moneybird administration, including their statuses, amounts, and associated contacts. Use this tool when you need to review, search, or audit existing invoices. Do not use this tool to create a new invoice — use the create sales invoice tool for that purpose.

        Args:
            administrationId: ID of the administration. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def moneybird_update_product(
        self,
        administrationId: str,
        product: _MoneybirdUpdateProductProduct,
        productId: str,
    ) -> Dict[str, Any]:
        """Updates the details of an existing product in a Moneybird administration, such as its name, price, or description. Use this tool when you need to modify the attributes of a product that already exists. Do not use this tool to create a new product — use the create product tool for that purpose.

        Args:
            administrationId: ID of the administration. (required)
            product: Product information. (required)
            productId: ID of the product. (required)
        Returns:
            API response as a dictionary.
        """
        ...

