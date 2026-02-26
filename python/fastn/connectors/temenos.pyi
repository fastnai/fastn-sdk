"""Fastn Temenos connector — auto-generated type stubs.

Do not edit manually. Regenerate with `fastn connector sync`.
"""
from __future__ import annotations

from typing import Any, Dict, List, Optional


class TemenosConnector:
    """Temenos connector ().

    Provides 13 tools.
    """

    def account_details(
        self,
        apikey: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Retrieves the details of an existing account in the banking system.

        Args:
            apikey: 
        Returns:
            API response as a dictionary.
        """
        ...

    def create_account(
        self,
        apikey: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Creates a new account in the banking system.

        Args:
            apikey: 
        Returns:
            API response as a dictionary.
        """
        ...

    def create_customer(
        self,
        apikey: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Creates a new customer profile in the banking system.

        Args:
            apikey: 
        Returns:
            API response as a dictionary.
        """
        ...

    def create_payment_order(
        self,
        apikey: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Initiates a new payment order in the banking system.

        Args:
            apikey: 
        Returns:
            API response as a dictionary.
        """
        ...

    def create_personal_loan(
        self,
        apikey: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Creates a new personal loan application in the banking system.

        Args:
            apikey: 
        Returns:
            API response as a dictionary.
        """
        ...

    def customer(
        self,
        apikey: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Defines the parameters related to a customer within the banking system.

        Args:
            apikey: 
        Returns:
            API response as a dictionary.
        """
        ...

    def customer_details(
        self,
        apikey: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Obtains details regarding a specific customer in the banking system.

        Args:
            apikey: 
        Returns:
            API response as a dictionary.
        """
        ...

    def get_the_customer_information(
        self,
        apikey: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Fetches comprehensive information about a customer in the banking system.

        Args:
            apikey: 
        Returns:
            API response as a dictionary.
        """
        ...

    def loan_details(
        self,
        apikey: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Retrieves details of a specific loan in the banking system.

        Args:
            apikey: 
        Returns:
            API response as a dictionary.
        """
        ...

    def redeem_deposit_account(
        self,
        apikey: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Redeems funds from a deposit account in the banking system.

        Args:
            apikey: 
        Returns:
            API response as a dictionary.
        """
        ...

    def to_compute_the_customer_risk_(
        self,
        apikey: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Calculates the risk associated with a customer in the banking system.

        Args:
            apikey: 
        Returns:
            API response as a dictionary.
        """
        ...

    def to_onboard_a_customer_and_compute_(
        self,
        apikey: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Onboards a customer and calculates their profile information in the banking system.

        Args:
            apikey: 
        Returns:
            API response as a dictionary.
        """
        ...

    def to_update_customer(
        self,
        apikey: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Updates existing customer information in the banking system.

        Args:
            apikey: 
        Returns:
            API response as a dictionary.
        """
        ...

