"""Fastn Twilio connector — auto-generated type stubs.

Do not edit manually. Regenerate with `fastn connector sync`.
"""
from __future__ import annotations

from typing import Any, Dict, List, Optional


class TwilioConnector:
    """Twilio connector ().

    Provides 10 tools.
    """

    def check_account_balance(
        self,
        AccountSID: str,
    ) -> Dict[str, Any]:
        """Checks the account balance in the specified service provider's system.

        Args:
            AccountSID:  (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def get_available_numbers(
        self,
        AreaCode: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Retrieves a list of available phone numbers from the telecommunication service provider.

        Args:
            AreaCode: The area code for the phone number.
        Returns:
            API response as a dictionary.
        """
        ...

    def get_call_details(
        self,
        accountSID: str,
        callSID: str,
    ) -> Dict[str, Any]:
        """Fetches detailed information about a specific call made through the communication platform.

        Args:
            accountSID:  (required)
            callSID: The unique identifier for the Twilio call. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def get_calls(
        self,
        acountSID: str,
    ) -> Dict[str, Any]:
        """Obtains a list of all calls logged in the communication service within a specified timeframe.

        Args:
            acountSID:  (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def get_details_of_sms(
        self,
        accountSID: str,
        smsID: str,
    ) -> Dict[str, Any]:
        """Retrieves detailed information regarding a specific SMS message sent or received in the messaging service.

        Args:
            accountSID:  (required)
            smsID: SMS message ID. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def get_purchased_numbers(
        self,
        accountSID: str,
    ) -> Dict[str, Any]:
        """Provides details about the phone numbers that have been purchased from the telecommunication service provider.

        Args:
            accountSID:  (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def get_sms_messages(
        self,
        accountSID: str,
    ) -> Dict[str, Any]:
        """Fetches all SMS messages sent and received through the messaging service.

        Args:
            accountSID:  (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def make_phone_call(
        self,
        From: str,
        To: str,
        Url: str,
    ) -> Dict[str, Any]:
        """Initiates a phone call using the chosen telecommunication service provider.

        Args:
            From: Twilio phone number sending the message. (required)
            To: Recipient phone number. (required)
            Url: URL to receive the response from Twilio. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def send_message(
        self,
        Body: str,
        From: str,
        To: str,
    ) -> Dict[str, Any]:
        """Sends a text message through the messaging service to a specified recipient.

        Args:
            Body: The text content of the SMS message. (required)
            From: The Twilio phone number sending the message. (required)
            To: The recipient's phone number. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def send_whatsapp_message(
        self,
        Body: str,
        From: str,
        To: str,
    ) -> Dict[str, Any]:
        """Sends a WhatsApp message through the messaging service to a specified recipient.

        Args:
            Body: The text content of the SMS message. (required)
            From: The Twilio phone number sending the message. (required)
            To: The recipient's phone number. (required)
        Returns:
            API response as a dictionary.
        """
        ...

