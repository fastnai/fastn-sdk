"""Fastn Resend connector — auto-generated type stubs.

Do not edit manually. Regenerate with `fastn connector sync`.
"""
from __future__ import annotations

from typing import Any, Dict, List, Optional, TypedDict


class _ResendSendEmailHeaders(TypedDict, total=False):
    X_Entity_Ref_ID: str

class ResendConnector:
    """Resend connector ().

    Provides 20 tools.
    """

    def resend_create_api_key(
        self,
        name: str,
    ) -> Dict[str, Any]:
        """Creates a new API key in Resend for authenticating API requests. The full key value is only returned once at creation time and cannot be retrieved again. Use this when provisioning access for a new integration or service. Do not use this to rotate a key — delete the old key first using resend_delete_api_key.

        Args:
            name: Name field for the Resend API request. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def resend_create_audience(
        self,
        name: str,
    ) -> Dict[str, Any]:
        """Creates a new audience in Resend for grouping contacts and targeting email campaigns. Use this before adding contacts to a new segment. Do not use this to update an existing audience or add contacts; use the appropriate update or create contact tools instead.

        Args:
            name: Name field for the Resend API request. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def resend_create_contact(
        self,
        audiencesId: str,
        email: str,
        first_name: Optional[str] = None,
        last_name: Optional[str] = None,
        unsubscribed: Optional[bool] = None,
    ) -> Dict[str, Any]:
        """Creates a new contact record inside a specified Resend audience. The contact will be available for future email campaigns targeting that audience. Use this when adding a new subscriber or contact. Do not use this to update an existing contact; use resend_update_contact instead.

        Args:
            audiencesId: ID of the audience. (required)
            email: Email address of the user. (required)
            first_name: First name of the user.
            last_name: Last name of the user.
            unsubscribed: Indicates whether the user is unsubscribed.
        Returns:
            API response as a dictionary.
        """
        ...

    def resend_create_domain(
        self,
        name: str,
    ) -> Dict[str, Any]:
        """Registers a new sending domain with Resend and returns the DNS records that must be configured for verification. Use this as the first step when setting up a new email sending domain. After adding DNS records, call resend_verify_domain to activate it. Do not use this if the domain is already registered; check with resend_list_domains first.

        Args:
            name: The name field for the Resend request. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def resend_delete_api_key(
        self,
        keyId: str,
    ) -> Dict[str, Any]:
        """Permanently revokes and deletes a Resend API key by its key ID. This action is irreversible — any integrations using the deleted key will immediately lose access. Use this to rotate or retire compromised or unused API keys. Do not use this to list or create keys.

        Args:
            keyId: Key ID for identifying the Resend API request. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def resend_delete_audience(
        self,
        audiencesId: str,
    ) -> Dict[str, Any]:
        """Permanently deletes a Resend audience and all its associated contacts. This action is irreversible — the audience and all contained contacts cannot be recovered. Use this only when you intend to permanently remove an entire audience. Do not use this to remove a single contact; use resend_delete_contact instead.

        Args:
            audiencesId: ID of the audiences. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def resend_delete_contact(
        self,
        audiencesId: str,
        contactId: str,
    ) -> Dict[str, Any]:
        """Permanently deletes a specific contact from a Resend audience. This action is irreversible — the contact record cannot be recovered after deletion. Use this only when you intend to permanently remove a contact. Do not use this to unsubscribe a contact; use updateContact instead.

        Args:
            audiencesId: The ID of the audiences. (required)
            contactId: The ID of the contact. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def resend_delete_domain(
        self,
        domainId: str,
    ) -> Dict[str, Any]:
        """Permanently removes a domain from the Resend account by its domain ID. This action is irreversible — emails can no longer be sent from addresses on this domain via Resend after deletion. Use this only when decommissioning a sending domain. Do not use this to merely unverify a domain.

        Args:
            domainId: The ID of the domain for the Resend API request. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def resend_get_audience(
        self,
        audiencesId: str,
    ) -> Dict[str, Any]:
        """Retrieves the details of a single Resend audience by its audience ID, including its name and creation date. Use this to inspect a specific audience. Do not use this to list all audiences; use resend_list_audiences instead.

        Args:
            audiencesId: ID of the audience to send the message to. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def resend_get_contact(
        self,
        audiencesId: str,
        contactId: str,
    ) -> Dict[str, Any]:
        """Retrieves the full details of a single contact within a Resend audience by contact ID and audience ID. Use this to inspect a specific contacts attributes. Do not use this to list all contacts in an audience; use resend_list_contacts instead.

        Args:
            audiencesId: ID of the audience the contact belongs to. (required)
            contactId: ID of the contact to resend the message to. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def resend_get_domain(
        self,
        domainId: str,
    ) -> Dict[str, Any]:
        """Retrieves the full details of a single Resend sending domain by its domain ID, including DNS record configuration and verification status. Use this to check whether a domain is properly verified before sending. Do not use this to list all domains; use resend_list_domains instead.

        Args:
            domainId: The ID of the domain for the Resend API request. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def resend_get_email(
        self,
        emailId: str,
    ) -> Dict[str, Any]:
        """Retrieves the details of a single sent email from Resend by its email ID, including status, recipients, subject, and timestamps. Use this to inspect or audit a previously sent email. Do not use this to list multiple emails or to send a new email.

        Args:
            emailId: Email ID to resend the email to. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def resend_list_api_keys(
        self,
    ) -> Dict[str, Any]:
        """Returns all API keys associated with the Resend account, including their IDs, names, and creation dates. Use this to audit existing keys before creating or deleting one. Do not use this to retrieve secrets; Resend does not expose key values after creation.
        Returns:
            API response as a dictionary.
        """
        ...

    def resend_list_audiences(
        self,
    ) -> Dict[str, Any]:
        """Returns all audiences defined in the Resend account. Use this to enumerate available audiences before performing contact or audience operations. Do not use this to retrieve details of a single audience; use resend_get_audience instead.
        Returns:
            API response as a dictionary.
        """
        ...

    def resend_list_contacts(
        self,
        audiencesId: str,
    ) -> Dict[str, Any]:
        """Returns all contacts belonging to a specific Resend audience, identified by its audience ID. Use this to enumerate every contact in an audience. Do not use this to retrieve a single contact or to search contacts by attribute.

        Args:
            audiencesId: ID of the audience for the Resend API Resend endpoint. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def resend_list_domains(
        self,
    ) -> Dict[str, Any]:
        """Returns all sending domains registered in the Resend account, including their verification status. Use this to audit configured domains or find a domain ID before performing further operations. Do not use this to retrieve details of a single domain; use resend_get_domain instead.
        Returns:
            API response as a dictionary.
        """
        ...

    def resend_send_batch_emails(
        self,
        body: List[Any],
    ) -> Dict[str, Any]:
        """Sends multiple emails in a single API call by accepting an array of email message objects, each with its own recipient, subject, and body. Use this for efficient bulk sending when dispatching more than one email at a time. Do not use this to send a single email; use resend_send_email instead.

        Args:
            body:  (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def resend_send_email(
        self,
        from: str,
        subject: str,
        to: List[Any],
        attachments: Optional[List[Any]] = None,
        headers: Optional[_ResendSendEmailHeaders] = None,
        text: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Sends a single transactional email to a specified recipient via the Resend API. Supports plain text and HTML content, CC, BCC, reply-to, and attachments. Use this for one-off transactional messages such as receipts, password resets, or notifications. Do not use this to send to multiple recipients in bulk; use resend_send_batch_emails instead.

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

    def resend_update_contact(
        self,
        audiencesId: str,
        contactId: str,
        last_name: str,
    ) -> Dict[str, Any]:
        """Updates the attributes of an existing contact within a Resend audience, such as email address, first name, last name, or subscription status. Use this to modify contact details or to unsubscribe a contact. Do not use this to create a new contact or delete one.

        Args:
            audiencesId: The ID of the audience. (required)
            contactId: The ID of the contact. (required)
            last_name: The last name of the recipient. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def resend_verify_domain(
        self,
        domainId: str,
    ) -> Dict[str, Any]:
        """Triggers a verification check for a Resend domain to confirm that the required DNS records (SPF, DKIM, etc.) have been configured correctly. Use this after adding a domain and setting up DNS records to activate the domain for sending. Do not use this to add a new domain; use resend_create_domain first.

        Args:
            domainId: ID of the domain. (required)
        Returns:
            API response as a dictionary.
        """
        ...

