"""Fastn Twilio connector — auto-generated type stubs.

Do not edit manually. Regenerate with `fastn connector sync`.
"""
from __future__ import annotations

from typing import Any, Dict, List, Optional, TypedDict


class TwilioConnector:
    """Twilio connector ().

    Provides 10 tools.
    """

    def twilio_check_account_balance(
        self,
        AccountSID: str,
    ) -> Dict[str, Any]:
        """Retrieves the current account balance and currency for the specified Twilio account. Use this tool when you need to verify available credit before initiating calls or messages, or to monitor spending. This is a read-only operation with no side effects.

        Args:
            AccountSID:  (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def twilio_get_call_details(
        self,
        accountSID: str,
        callSID: str,
    ) -> Dict[str, Any]:
        """Retrieves detailed information about a single call identified by its call SID, including status, duration, direction, timestamps, and participants. Use this tool when you need to inspect or verify a specific call record. Do not use this tool to list all calls; use twilio_list_calls instead. This is a read-only operation with no side effects.

        Args:
            accountSID:  (required)
            callSID: The unique identifier for the Twilio call. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def twilio_get_sms_details(
        self,
        accountSID: str,
        smsID: str,
    ) -> Dict[str, Any]:
        """Retrieves detailed information about a single SMS message identified by its message SID, including status, timestamps, sender, recipient, and body. Use this tool when you need to inspect or verify a specific message. Do not use this tool to list all messages; use twilio_list_sms_messages instead. This is a read-only operation with no side effects.

        Args:
            accountSID:  (required)
            smsID: SMS message ID. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def twilio_list_available_numbers(
        self,
        accountSID: str,
        countryCode: str,
        AreaCode: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Retrieves a list of available local phone numbers in a specified country that can be purchased for use with the Twilio account. Use this tool when you need to find and select a new phone number to buy. Do not use this tool to view already-owned numbers; use twilio_list_purchased_numbers instead. This is a read-only operation with no side effects; it does not purchase or reserve any numbers.

        Args:
            accountSID:  (required)
            countryCode: The country code for the phone number. (required)
            AreaCode: The area code for the phone number.
        Returns:
            API response as a dictionary.
        """
        ...

    def twilio_list_calls(
        self,
        acountSID: str,
    ) -> Dict[str, Any]:
        """Retrieves a list of all calls logged in the Twilio account, optionally filtered by a specified timeframe or other parameters. Use this tool when you need an overview of call history, including inbound and outbound calls. Do not use this tool to retrieve details about a single specific call; use twilio_get_call_details instead. This is a read-only operation with no side effects.

        Args:
            acountSID:  (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def twilio_list_purchased_numbers(
        self,
        accountSID: str,
    ) -> Dict[str, Any]:
        """Retrieves a list of all phone numbers that have been purchased and are active on the Twilio account, including their capabilities (SMS, voice, MMS) and configuration. Use this tool when you need to audit owned numbers or select a sender number for outbound communication. Do not use this tool to search for new numbers to buy; use twilio_list_available_numbers instead. This is a read-only operation with no side effects.

        Args:
            accountSID:  (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def twilio_list_sms_messages(
        self,
        accountSID: str,
    ) -> Dict[str, Any]:
        """Retrieves a list of all SMS messages sent and received through a Twilio account. Use this tool when you need an overview of message history, including inbound and outbound SMS records. Do not use this tool to retrieve details about a single specific message; use twilio_get_sms_details instead. This is a read-only operation with no side effects.

        Args:
            accountSID:  (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def twilio_make_phone_call(
        self,
        From: str,
        To: str,
        Url: str,
        accountSID: str,
    ) -> Dict[str, Any]:
        """Initiates an outbound phone call via Twilio to a specified phone number. Use this tool when you need to programmatically place a voice call from a Twilio number to a recipient. Do not use this tool to retrieve call history; use twilio_list_calls instead. This action creates a new call record in Twilio and immediately begins dialing the recipient.

        Args:
            From: Twilio phone number sending the message. (required)
            To: Recipient phone number. (required)
            Url: URL to receive the response from Twilio. (required)
            accountSID: Your Twilio Account SID. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def twilio_send_message(
        self,
        Body: str,
        From: str,
        To: str,
        accountSID: str,
    ) -> Dict[str, Any]:
        """Sends an SMS or MMS text message via Twilio to a specified recipient phone number. Use this tool when you need to deliver a text message to a phone number using a Twilio messaging service or sender number. Do not use this tool for WhatsApp messages; use twilio_send_whatsapp_message instead. This action creates a new outbound message record in Twilio.

        Args:
            Body: The text content of the SMS message. (required)
            From: The Twilio phone number sending the message. (required)
            To: The recipient's phone number. (required)
            accountSID: Your Twilio Account SID. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def twilio_send_whatsapp_message(
        self,
        Body: str,
        From: str,
        To: str,
        accountSID: str,
    ) -> Dict[str, Any]:
        """Sends a WhatsApp message via Twilio to a specified recipient phone number. Use this tool when you need to deliver a message over WhatsApp using a Twilio-registered WhatsApp sender. Do not use this tool for standard SMS/MMS delivery; use twilio_send_message instead. This action creates a new outbound message record in Twilio.

        Args:
            Body: The text content of the SMS message. (required)
            From: The Twilio phone number sending the message. (required)
            To: The recipient's phone number. (required)
            accountSID:  (required)
        Returns:
            API response as a dictionary.
        """
        ...

