"""Fastn Resend connector — auto-generated type stubs.

Do not edit manually. Regenerate with `fastn connector sync`.
"""
from __future__ import annotations

from typing import Any, Dict, List, Optional


class ResendConnector:
    """Resend connector ().

    Provides 20 tools.
    """

    def add_domain(
        self,
        name: str,
    ) -> Dict[str, Any]:
        """Adds a new domain to be managed through the domain management connector.

        Args:
            name: The name field for the Resend request. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def create_api_key(
        self,
        name: str,
    ) -> Dict[str, Any]:
        """Creates a new API key for authenticating requests through the API key management connector.

        Args:
            name: Name field for the Resend API request. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def create_audience(
        self,
        name: str,
    ) -> Dict[str, Any]:
        """Creates a new audience in the audience management connector for targeted communication.

        Args:
            name: Name field for the Resend API request. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def create_contact(
        self,
        email: str,
        first_name: Optional[str] = None,
        last_name: Optional[str] = None,
        unsubscribed: Optional[bool] = None,
    ) -> Dict[str, Any]:
        """Creates a new contact in the contact management connector for future communication.

        Args:
            email: Email address of the user. (required)
            first_name: First name of the user.
            last_name: Last name of the user.
            unsubscribed: Indicates whether the user is unsubscribed.
        Returns:
            API response as a dictionary.
        """
        ...

    def delete_api_key(
        self,
        keyId: str,
    ) -> Dict[str, Any]:
        """Deletes a specified API key using the API key management connector.

        Args:
            keyId: Key ID for identifying the Resend API request. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def delete_audience(
        self,
        audiencesId: str,
    ) -> Dict[str, Any]:
        """Deletes a specified audience from the audience management connector.

        Args:
            audiencesId: ID of the audiences. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def delete_contact(
        self,
        audiencesId: str,
        contactId: str,
    ) -> Dict[str, Any]:
        """Deletes a specified contact from the contact management connector.

        Args:
            audiencesId: The ID of the audiences. (required)
            contactId: The ID of the contact. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def delete_domain(
        self,
        domainId: str,
    ) -> Dict[str, Any]:
        """Deletes a specified domain from management using the domain management connector.

        Args:
            domainId: The ID of the domain for the Resend API request. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def get_api_keys(
        self,
    ) -> Dict[str, Any]:
        """Retrieves a list of all API keys available through the API key management connector.
        Returns:
            API response as a dictionary.
        """
        ...

    def get_audience(
        self,
        audiencesId: str,
    ) -> Dict[str, Any]:
        """Retrieves information about a specific audience using the audience management connector.

        Args:
            audiencesId: ID of the audience to send the message to. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def get_audiences(
        self,
    ) -> Dict[str, Any]:
        """Fetches a list of all audiences managed by the audience management connector.
        Returns:
            API response as a dictionary.
        """
        ...

    def get_contact(
        self,
        audiencesId: str,
        contactId: str,
    ) -> Dict[str, Any]:
        """Retrieves detailed information about a specific contact using the contact management connector.

        Args:
            audiencesId: ID of the audience the contact belongs to. (required)
            contactId: ID of the contact to resend the message to. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def get_contacts(
        self,
        audiencesId: str,
    ) -> Dict[str, Any]:
        """Fetches a list of all contacts managed by the contact management connector.

        Args:
            audiencesId: ID of the audience for the Resend API Resend endpoint. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def get_domain(
        self,
        domainId: str,
    ) -> Dict[str, Any]:
        """Retrieves information about a specific domain using the domain management connector.

        Args:
            domainId: The ID of the domain for the Resend API request. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def get_domains(
        self,
    ) -> Dict[str, Any]:
        """Fetches a list of all domains managed by the domain management connector.
        Returns:
            API response as a dictionary.
        """
        ...

    def get_email(
        self,
        emailId: str,
    ) -> Dict[str, Any]:
        """Retrieves information about a specific email using the email management connector.

        Args:
            emailId: Email ID to resend the email to. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def send_batch_emails(
        self,
    ) -> Dict[str, Any]:
        """Sends multiple emails to a list of specified recipients using the email connector in one batch operation.
        Returns:
            API response as a dictionary.
        """
        ...

    def send_email(
        self,
        from: str,
        subject: str,
        to: List[Any],
        attachments: Optional[List[Any]] = None,
        headers: Optional[Dict[str, Any]] = None,
        text: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Sends an email to a specified recipient using the email connector.

        Args:
            from: Sender email address. (required)
            subject: Subject of the email. (required)
            to: Recipient email addresses. (required)
            attachments: 
            headers: Custom headers for the email.
            text: Body text of the email.
        Returns:
            API response as a dictionary.
        """
        ...

    def update_contact(
        self,
        last_name: str,
    ) -> Dict[str, Any]:
        """Updates an existing contact's information in the contact management connector.

        Args:
            last_name: The last name of the recipient. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def verify_domain_(
        self,
        domainId: str,
    ) -> Dict[str, Any]:
        """Verifies the ownership and configuration of a specified domain using the domain management connector.

        Args:
            domainId: ID of the domain. (required)
        Returns:
            API response as a dictionary.
        """
        ...

