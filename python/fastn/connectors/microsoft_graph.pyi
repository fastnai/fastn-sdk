"""Fastn Microsoft Graph connector — auto-generated type stubs.

Do not edit manually. Regenerate with `fastn connector sync`.
"""
from __future__ import annotations

from typing import Any, Dict, List, Optional


class MicrosoftGraphConnector:
    """Microsoft Graph connector ().

    Provides 19 tools.
    """

    def create_app_registration(
        self,
        displayName: Optional[str] = None,
        groupMembershipClaims: Optional[str] = None,
        optionalClaims: Optional[Dict[str, Any]] = None,
        passwordCredentials: Optional[List[Any]] = None,
        requiredResourceAccess: Optional[List[Any]] = None,
        signInAudience: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Creates a new application registration within the system.

        Args:
            displayName: 
            groupMembershipClaims: 
            optionalClaims: 
            passwordCredentials: 
            requiredResourceAccess: 
            signInAudience: 
        Returns:
            API response as a dictionary.
        """
        ...

    def create_app_role_assignments(
        self,
        appRoleId: Optional[str] = None,
        principalId: Optional[str] = None,
        resourceId: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Creates app role assignments to specify permissions for users or service principals.

        Args:
            appRoleId: 
            principalId: 
            resourceId: 
        Returns:
            API response as a dictionary.
        """
        ...

    def create_oauth2_permission_grants(
        self,
        clientId: Optional[str] = None,
        consentType: Optional[str] = None,
        principalId: Optional[str] = None,
        resourceId: Optional[str] = None,
        scope: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Creates OAuth2 permission grants to allow a service principal to access resources.

        Args:
            clientId: 
            consentType: 
            principalId: 
            resourceId: 
            scope: 
        Returns:
            API response as a dictionary.
        """
        ...

    def create_service_principal(
        self,
        appId: Optional[str] = None,
        displayName: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Creates a new service principal to allow applications to access resources.

        Args:
            appId: 
            displayName: 
        Returns:
            API response as a dictionary.
        """
        ...

    def create_subscription(
        self,
        changeType: str,
        expirationDateTime: str,
        resource: str,
        NotificationUrl: Optional[str] = None,
        clientState: Optional[str] = None,
        lifecycleNotificationUrl: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Creates a new subscription within the system.

        Args:
            changeType: Type of change that triggered the notification. (required)
            expirationDateTime: Expiration date and time for the notification. (required)
            resource: Resource related to the notification. (required)
            NotificationUrl: URL to receive notifications.
            clientState: 
            lifecycleNotificationUrl: URL for lifecycle notifications.
        Returns:
            API response as a dictionary.
        """
        ...

    def generate_auth_token(
        self,
        client_id: Optional[str] = None,
        client_secret: Optional[str] = None,
        password: Optional[str] = None,
        username: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Generates an authentication token for use with API requests.

        Args:
            client_id: 
            client_secret: 
            password: 
            username: 
        Returns:
            API response as a dictionary.
        """
        ...

    def generate_auth_token_with_client_credentials(
        self,
        client_id: Optional[str] = None,
        client_secret: Optional[str] = None,
        scope: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Generates an authentication token using client credentials for server-to-server communication.

        Args:
            client_id: 
            client_secret: 
            scope: 
        Returns:
            API response as a dictionary.
        """
        ...

    def generate_token(
        self,
    ) -> Dict[str, Any]:
        """Generates a new token for authentication purposes.
        Returns:
            API response as a dictionary.
        """
        ...

    def get_active_token(
        self,
    ) -> Dict[str, Any]:
        """Retrieves the currently active token being used in the session.
        Returns:
            API response as a dictionary.
        """
        ...

    def get_my_direct_reports(
        self,
        select: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Fetches the direct reports of the currently authenticated user.

        Args:
            select: 
        Returns:
            API response as a dictionary.
        """
        ...

    def get_my_tenant(
        self,
    ) -> Dict[str, Any]:
        """Retrieves details of the current tenant in the system.
        Returns:
            API response as a dictionary.
        """
        ...

    def get_my_user_details(
        self,
        expand: Optional[str] = None,
        select: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Retrieves the details of the currently authenticated user.

        Args:
            expand: 
            select: 
        Returns:
            API response as a dictionary.
        """
        ...

    def get_organizations(
        self,
    ) -> Dict[str, Any]:
        """Retrieves a list of organizations in the system.
        Returns:
            API response as a dictionary.
        """
        ...

    def get_permissions(
        self,
        appId: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Fetches the permissions associated with the currently authenticated user.

        Args:
            appId: 
        Returns:
            API response as a dictionary.
        """
        ...

    def get_user(
        self,
        expand: Optional[str] = None,
        select: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Retrieves the details of a specific user from the system.

        Args:
            expand: 
            select: 
        Returns:
            API response as a dictionary.
        """
        ...

    def get_user_direct_reports(
        self,
        select: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Fetches the direct reports of a specified user.

        Args:
            select: 
        Returns:
            API response as a dictionary.
        """
        ...

    def get_users(
        self,
        count: Optional[str] = None,
        expand: Optional[str] = None,
        filter: Optional[str] = None,
        orderBy: Optional[str] = None,
        select: Optional[str] = None,
        skiptoken: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Fetches a list of all users from the system.

        Args:
            count: 
            expand: 
            filter: 
            orderBy: 
            select: 
            skiptoken: 
        Returns:
            API response as a dictionary.
        """
        ...

    def reauthorize_subscription(
        self,
        subscriptionId: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Reauthorizes an existing subscription to ensure continued service access.

        Args:
            subscriptionId: 
        Returns:
            API response as a dictionary.
        """
        ...

    def refresh_token(
        self,
        client_id: Optional[str] = None,
        client_secret: Optional[str] = None,
        redirect_uri: Optional[str] = None,
        refresh_token: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Refreshes an existing token to maintain session validity.

        Args:
            client_id: 
            client_secret: 
            redirect_uri: 
            refresh_token: 
        Returns:
            API response as a dictionary.
        """
        ...

