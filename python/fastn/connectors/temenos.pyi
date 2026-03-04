"""Fastn Temenos connector — auto-generated type stubs.

Do not edit manually. Regenerate with `fastn connector sync`.
"""
from __future__ import annotations

from typing import Any, Dict, List, Optional, TypedDict


class _TemenosComputeCustomerRiskCustomerdetails(TypedDict, total=False):
    address1: str
    address2: str
    application: str
    bankId2: str
    birthCity: str
    birthCountry: str
    birthDate: str
    branch: str
    careOf: str
    city: str
    closed: str
    company: str
    coreData1: str
    coreData2: str
    coreData3: str
    coreData4: str
    coreData5: str
    country: str
    customerId: str
    firstName: str
    fiscalCountry: str
    name: str
    natCountry: str
    nationalId: str
    occupation: str
    passportNumber: str
    pep: str
    segmentCode: str
    socialSecurityNumber: str
    ssnCountry: str
    state: str
    telephoneNumberFix: str
    telephoneNumberMobile: str
    title: str
    typeId: str
    zipCode: str

class _TemenosComputeCustomerRiskSectors(TypedDict, total=False):
    sectorNames: List[Any]

class _TemenosCreateAccountBody(TypedDict, total=False):
    activityId: str
    currency: str
    partyIds: List[Any]
    productId: str

class _TemenosCreateAccountHeader(TypedDict, total=False):
    override: Dict[str, Any]

class _TemenosCreateCustomerBody(TypedDict, total=False):
    accountOfficerId: int
    communicationDevices: List[Any]
    customerMnemonic: str
    customerNames: List[Any]
    customerStatus: str
    dateOfBirth: str
    displayNames: List[Any]
    gender: str
    industryId: int
    language: int
    nationalityId: str
    sectorId: int
    target: int

class _TemenosCreatePaymentOrderBody(TypedDict, total=False):
    PSDCompliant: str
    accountType: str
    accountWithBankBIC: str
    accountWithBankClearingCode: str
    accountWithBankCountryId: str
    accountWithBankIBAN: str
    accountWithInstitutionAddresses: List[Any]
    action: str
    additionalInformations: List[Any]
    amount: int
    beneficiaryAccountId: str
    beneficiaryAddresses: List[Any]
    beneficiaryBIC: str
    beneficiaryBankClearingCode: str
    beneficiaryCountryCode: str
    beneficiaryEmailId: str
    beneficiaryIBAN: str
    beneficiaryId: str
    beneficiaryName: str
    beneficiaryPhoneNumber: str
    bulkReference: str
    bulkTypeId: str
    cancelReason: str
    cancelRemark: str
    chargeAccountCurrencyId: str
    chargeAccountId: str
    chargeBearer: str
    charges: List[Any]
    clearingChannel: str
    creditAccountIBAN: str
    creditAccountId: str
    creditPortfolio: str
    creditValueDate: str
    debitAccountIBAN: str
    debitAccountId: str
    debitCurrency: str
    debitValueDate: str
    endToEndReference: str
    exchangeRate: str
    executionDate: str
    forexCustomerRate: str
    forexSpread: str
    indicativeRate: str
    initiationTime: str
    instructionIdReference: str
    invoiceReferences: List[Any]
    localInstrumentCode: str
    narratives: List[Any]
    orderingCustomerId: str
    orderingCustomerName: str
    orderingPortfolio: str
    orderingPostAddrLine: List[Any]
    orderingReference: str
    overrides: List[Any]
    paymentCurrencyId: str
    paymentOrderProductId: str
    paymentSource: str
    preAuthorizationReference: str
    purpose: str
    reasons: List[Any]
    recordStatus: str
    remittanceInformations: List[Any]
    requestedAmount: str
    requestedCurrency: str
    requiredCreditValueDate: str
    signatories: List[Any]
    sourceType: str
    structuredCommunicationCode: str
    structuredCreditorReference: str
    structuredIssuer: str
    termsAndConditions: str
    totalDebitAmount: str
    treasuryRate: str

class _TemenosCreatePaymentOrderHeader(TypedDict, total=False):
    audit: Dict[str, Any]
    override: Dict[str, Any]

class _TemenosCreatePersonalLoanBody(TypedDict, total=False):
    activityId: str
    arrangementEffectiveDate: str
    arrangmentId: str
    commitment: Dict[str, Any]
    currency: str
    partyIds: List[Any]
    partyRoles: List[Any]
    productId: str

class _TemenosCreatePersonalLoanHeader(TypedDict, total=False):
    override: Dict[str, Any]

class _TemenosGetCustomerDetailsBody(TypedDict, total=False):
    accountOfficerId: int
    customer: str
    customerMnemonic: str
    customerNames: List[Any]
    customerStatus: int
    displayNames: List[Any]
    industryId: int
    language: int
    nationalityId: str
    sectorId: int
    target: int

class _TemenosOnboardAndComputeCustomerRiskCustomerdetails(TypedDict, total=False):
    address1: str
    address2: str
    application: str
    bankId2: str
    birthCity: str
    birthCountry: str
    birthDate: str
    branch: str
    careOf: str
    city: str
    closed: str
    company: str
    coreData1: str
    coreData2: str
    coreData3: str
    coreData4: str
    coreData5: str
    country: str
    customerId: str
    firstName: str
    fiscalCountry: str
    name: str
    natCountry: str
    nationalId: str
    occupation: str
    passportNumber: str
    pep: str
    segmentCode: str
    socialSecurityNumber: str
    ssnCountry: str
    state: str
    telephoneNumberFix: str
    telephoneNumberMobile: str
    title: str
    typeId: str
    zipCode: str

class _TemenosOnboardAndComputeCustomerRiskSectors(TypedDict, total=False):
    sectorNames: List[Any]

class _TemenosRedeemDepositAccountBody(TypedDict, total=False):
    activityId: str
    commitment: Dict[str, Any]
    currency: str
    customerMnemonic: str
    customerNames: List[Any]
    displayNames: List[Any]
    language: str
    nationalityId: str
    partyIds: List[Any]
    partyRoles: List[Any]
    productId: str
    residenceId: str
    sectorId: str
    settlement: List[Any]
    streets: List[Any]

class _TemenosUpdateCustomerCustomerdetails(TypedDict, total=False):
    address1: str
    address2: str
    application: str
    bankId2: str
    birthCity: str
    birthCountry: str
    birthDate: str
    branch: str
    careOf: str
    city: str
    closed: str
    company: str
    coreData1: str
    coreData2: str
    coreData3: str
    coreData4: str
    coreData5: str
    country: str
    customerId: str
    firstName: str
    fiscalCountry: str
    name: str
    natCountry: str
    nationalId: str
    occupation: str
    passportNumber: str
    pep: str
    segmentCode: str
    socialSecurityNumber: str
    ssnCountry: str
    state: str
    telephoneNumberFix: str
    telephoneNumberMobile: str
    title: str
    typeId: str
    zipCode: str

class _TemenosUpdateCustomerSectors(TypedDict, total=False):
    sectorNames: List[Any]

class TemenosConnector:
    """Temenos connector ().

    Provides 13 tools.
    """

    def temenos_compute_customer_risk(
        self,
        apikey: Optional[str] = None,
        assessments: Optional[List[Any]] = None,
        cifFields: Optional[List[Any]] = None,
        customerDetails: Optional[_TemenosComputeCustomerRiskCustomerdetails] = None,
        sectors: Optional[_TemenosComputeCustomerRiskSectors] = None,
    ) -> Dict[str, Any]:
        """Calculates the risk score associated with an existing customer in the Temenos banking system. Use this tool when you need to assess or recompute a customers risk profile independently of the onboarding process. Do not use this tool if you need to onboard a new customer and compute risk simultaneously; use the onboard-and-compute tool instead. This action triggers a risk computation and persists the result.

        Args:
            apikey: 
            assessments: 
            cifFields: 
            customerDetails: 
            sectors: 
        Returns:
            API response as a dictionary.
        """
        ...

    def temenos_create_account(
        self,
        apikey: Optional[str] = None,
        body: Optional[_TemenosCreateAccountBody] = None,
        header: Optional[_TemenosCreateAccountHeader] = None,
    ) -> Dict[str, Any]:
        """Creates a new current account in the Temenos banking system. Use this tool when you need to open a new current account for a customer. Do not use this tool to create loan accounts, deposit accounts, or to update an existing account. This action persists a new account record and is not reversible without a separate closure process.

        Args:
            apikey: 
            body: 
            header: 
        Returns:
            API response as a dictionary.
        """
        ...

    def temenos_create_customer(
        self,
        apikey: Optional[str] = None,
        body: Optional[_TemenosCreateCustomerBody] = None,
        header: Optional[Dict[str, Any]] = None,
    ) -> Dict[str, Any]:
        """Creates a new customer profile in the Temenos banking system. Use this tool when you need to register a new customer. Do not use this tool to update an existing customer or retrieve customer information. This action persists a new customer record and is not reversible without a separate deletion process.

        Args:
            apikey: 
            body: 
            header: 
        Returns:
            API response as a dictionary.
        """
        ...

    def temenos_create_payment_order(
        self,
        apikey: Optional[str] = None,
        body: Optional[_TemenosCreatePaymentOrderBody] = None,
        header: Optional[_TemenosCreatePaymentOrderHeader] = None,
    ) -> Dict[str, Any]:
        """Initiates a new payment order in the Temenos banking system. Use this tool when you need to create and submit a payment order for processing. Do not use this tool to query existing payment orders or to create a loan. Note: this tool currently calls the personal loans endpoint—verify the endpoint configuration before use. This action creates a financial transaction and may not be reversible once submitted.

        Args:
            apikey: 
            body: 
            header: 
        Returns:
            API response as a dictionary.
        """
        ...

    def temenos_create_personal_loan(
        self,
        apikey: Optional[str] = None,
        body: Optional[_TemenosCreatePersonalLoanBody] = None,
        header: Optional[_TemenosCreatePersonalLoanHeader] = None,
    ) -> Dict[str, Any]:
        """Creates a new personal loan application in the Temenos banking system. Use this tool when you need to submit a personal loan application for a customer. Do not use this tool to create other loan types, payment orders, or accounts. This action persists a new loan record and is not reversible without a separate cancellation process.

        Args:
            apikey: 
            body: 
            header: 
        Returns:
            API response as a dictionary.
        """
        ...

    def temenos_get_account_details(
        self,
        apikey: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Retrieves the details of an existing account in the Temenos banking system, such as balance, status, and account metadata. Use this tool when you need to look up information about a specific account. Do not use this tool to create or update an account. This is a read-only operation with no side effects.

        Args:
            apikey: 
        Returns:
            API response as a dictionary.
        """
        ...

    def temenos_get_customer(
        self,
        apikey: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Retrieves details of a customer from the Temenos banking system. Use this tool when you need to look up an existing customer record by their identifier. Do not use this tool to create or update a customer. This is a read-only operation with no side effects.

        Args:
            apikey: 
        Returns:
            API response as a dictionary.
        """
        ...

    def temenos_get_customer_details(
        self,
        apikey: Optional[str] = None,
        body: Optional[_TemenosGetCustomerDetailsBody] = None,
        header: Optional[Dict[str, Any]] = None,
    ) -> Dict[str, Any]:
        """Retrieves details for a specific customer in the Temenos banking system. Use this tool when you need to look up existing customer information such as contact details or personal data. Do not use this tool to update a customer or create a new customer. This is a read-only operation with no side effects.

        Args:
            apikey: 
            body: 
            header: 
        Returns:
            API response as a dictionary.
        """
        ...

    def temenos_get_customer_information(
        self,
        apikey: Optional[str] = None,
        company: Optional[str] = None,
        customerId: Optional[str] = None,
        infoType: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Retrieves comprehensive information about a customer in the Temenos banking system. Use this tool when you need to access KYC information and detailed customer profile data for a specific customer. Do not use this tool to retrieve customer lists or to update customer data. This is a read-only operation with no side effects.

        Args:
            apikey: 
            company: 
            customerId: 
            infoType: 
        Returns:
            API response as a dictionary.
        """
        ...

    def temenos_get_loan_details(
        self,
        apikey: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Retrieves details of loans in the Temenos banking system. Use this tool when you need to look up loan information such as balance, status, or repayment schedule. Do not use this tool to create or update a loan. This is a read-only operation with no side effects.

        Args:
            apikey: 
        Returns:
            API response as a dictionary.
        """
        ...

    def temenos_onboard_and_compute_customer_risk(
        self,
        apikey: Optional[str] = None,
        assessments: Optional[List[Any]] = None,
        cifFields: Optional[List[Any]] = None,
        customerDetails: Optional[_TemenosOnboardAndComputeCustomerRiskCustomerdetails] = None,
        sectors: Optional[_TemenosOnboardAndComputeCustomerRiskSectors] = None,
    ) -> Dict[str, Any]:
        """Onboards a new customer and calculates their risk profile in the Temenos banking system. Use this tool when you need to simultaneously register a customer and compute their risk score during the onboarding process. Do not use this tool if you only need to compute risk for an already-onboarded customer; use the dedicated risk computation tool instead. This action creates a new customer record and triggers a risk calculation, both of which are persisted.

        Args:
            apikey: 
            assessments: 
            cifFields: 
            customerDetails: 
            sectors: 
        Returns:
            API response as a dictionary.
        """
        ...

    def temenos_redeem_deposit_account(
        self,
        apikey: Optional[str] = None,
        body: Optional[_TemenosRedeemDepositAccountBody] = None,
    ) -> Dict[str, Any]:
        """Redeems funds from a deposit account in the Temenos banking system. Use this tool when a customer wants to withdraw or redeem their deposit. Do not use this tool to create a deposit, update account details, or process loan payments. This action is financial and may be irreversible once processed; confirm all parameters before execution.

        Args:
            apikey: 
            body: 
        Returns:
            API response as a dictionary.
        """
        ...

    def temenos_update_customer(
        self,
        apikey: Optional[str] = None,
        assessments: Optional[List[Any]] = None,
        cifFields: Optional[List[Any]] = None,
        customerDetails: Optional[_TemenosUpdateCustomerCustomerdetails] = None,
        sectors: Optional[_TemenosUpdateCustomerSectors] = None,
    ) -> Dict[str, Any]:
        """Updates the document status for an existing customer in the Temenos banking system. Use this tool when you need to update KYC document statuses for a specific customer. Do not use this tool to create a new customer or retrieve customer information. This action modifies existing customer records and the change is persisted immediately.

        Args:
            apikey: 
            assessments: 
            cifFields: 
            customerDetails: 
            sectors: 
        Returns:
            API response as a dictionary.
        """
        ...

