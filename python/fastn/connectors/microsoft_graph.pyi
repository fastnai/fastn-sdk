"""Fastn Microsoft Graph connector — auto-generated type stubs.

Do not edit manually. Regenerate with `fastn connector sync`.
"""
from __future__ import annotations

from typing import Any, Dict, List, Optional, TypedDict


class _MicrosoftGraphCreateAppRegistrationOptionalclaims(TypedDict, total=False):
    accessToken: List[Any]
    idToken: List[Any]
    saml2Token: List[Any]

class MicrosoftGraphConnector:
    """Microsoft Graph connector ().

    Provides 20 tools.
    """

    def microsoft_graph_create_app_registration(
        self,
        displayName: Optional[str] = None,
        groupMembershipClaims: Optional[str] = None,
        optionalClaims: Optional[_MicrosoftGraphCreateAppRegistrationOptionalclaims] = None,
        passwordCredentials: Optional[List[Any]] = None,
        requiredResourceAccess: Optional[List[Any]] = None,
        signInAudience: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Creates a new application registration in Microsoft Entra ID (Azure AD) via Microsoft Graph, establishing the applications identity, redirect URIs, and permission scopes. Use this when you need to register a new application so it can authenticate users or services and request API permissions. This is a write operation with persistent side effects — the application registration persists in the directory until explicitly deleted. After creating the registration, you must also create a service principal using microsoft_graph_create_service_principal before the application can be assigned permissions within the tenant.

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

    def microsoft_graph_create_app_role_assignments(
        self,
        appRoleId: Optional[str] = None,
        principalId: Optional[str] = None,
        resourceId: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Creates an app role assignment for a specified service principal in Microsoft Graph, granting a user, group, or service principal a specific application role on a resource. Use this when you need to assign application-level permissions (not delegated permissions) to a principal, such as granting a managed identity access to an API. This is a write operation with persistent side effects — the assignment remains active until explicitly removed. Do not use this to grant delegated OAuth2 permissions; use microsoft_graph_create_oauth2_permission_grants for that purpose.

        Args:
            appRoleId: 
            principalId: 
            resourceId: 
        Returns:
            API response as a dictionary.
        """
        ...

    def microsoft_graph_create_oauth2_permission_grants(
        self,
        clientId: Optional[str] = None,
        consentType: Optional[str] = None,
        principalId: Optional[str] = None,
        resourceId: Optional[str] = None,
        scope: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Creates an OAuth2 permission grant in Microsoft Graph that allows a client service principal to access a resource on behalf of a user or all users (admin consent). Use this when you need to grant delegated API permissions to a service principal without requiring individual user consent prompts. This is a write operation with persistent side effects — the grant remains active until explicitly deleted. Do not use this to assign application roles; use microsoft_graph_create_app_role_assignments for that purpose.

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

    def microsoft_graph_create_service_principal(
        self,
        appId: Optional[str] = None,
        displayName: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Creates a new service principal in the current Microsoft Entra ID (Azure AD) tenant for an existing application registration, enabling the application to authenticate and be granted permissions within the tenant. Use this when you have already registered an application and need to instantiate its service principal so it can be assigned roles or permissions. This is a write operation with persistent side effects — the service principal will remain in the directory until explicitly deleted. Do not use this to register a new application; use microsoft_graph_create_app_registration for that purpose.

        Args:
            appId: 
            displayName: 
        Returns:
            API response as a dictionary.
        """
        ...

    def microsoft_graph_generate_auth_token(
        self,
        client_id: Optional[str] = None,
        client_secret: Optional[str] = None,
        password: Optional[str] = None,
        tenantId: Optional[str] = None,
        username: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Generates an OAuth2 access token from the Microsoft identity platform v2 endpoint for a configurable tenant (specified via tenantId), for use with Microsoft Graph and Microsoft 365 API requests. Use this when you need to authenticate against a specific tenant whose ID is known at runtime. Do not use this for fixed-tenant token generation — use microsoft_graph_generate_token for the hardcoded tenant scenario. Do not use this for the client credentials (server-to-server) flow — use microsoft_graph_generate_auth_token_with_client_credentials instead.

        Args:
            client_id: 
            client_secret: 
            password: 
            tenantId: 
            username: 
        Returns:
            API response as a dictionary.
        """
        ...

    def microsoft_graph_generate_auth_token_with_client_credentials(
        self,
        client_id: Optional[str] = None,
        client_secret: Optional[str] = None,
        scope: Optional[str] = None,
        tenantId: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Generates an OAuth2 access token using the client credentials flow (client ID and client secret) for a configurable tenant, targeting the v1 Microsoft identity platform token endpoint. Use this for server-to-server authentication scenarios where no user interaction is required and you need to specify the tenant ID dynamically. Do not use this for delegated (user-context) authentication flows. If you need to use the v2 endpoint or a fixed tenant, use microsoft_graph_generate_auth_token or microsoft_graph_generate_token instead.

        Args:
            client_id: 
            client_secret: 
            scope: 
            tenantId: 
        Returns:
            API response as a dictionary.
        """
        ...

    def microsoft_graph_generate_org_token(
        self,
        client_id: Optional[str] = None,
        client_secret: Optional[str] = None,
        code: Optional[str] = None,
        grant_type: Optional[str] = None,
        redirect_uri: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Generates a new OAuth2 access token from the Microsoft identity platform targeting the organizations v2 endpoint, scoped to organizational (work or school) accounts. Use this when you need to obtain an initial access token for organizational account authentication without specifying a tenant ID. Do not use this for fixed-tenant token generation — use microsoft_graph_generate_token (fixed tenant) or microsoft_graph_generate_auth_token_with_client_credentials (configurable tenant) for those cases.

        Args:
            client_id: 
            client_secret: 
            code: 
            grant_type: 
            redirect_uri: 
        Returns:
            API response as a dictionary.
        """
        ...

    def microsoft_graph_generate_token(
        self,
        connection: Dict[str, Any],
        client_id: Optional[str] = None,
        client_secret: Optional[str] = None,
        grant_type: Optional[str] = None,
        password: Optional[str] = None,
        scope: Optional[str] = None,
        username: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Generates a new OAuth2 authentication token against a fixed Microsoft tenant (a3ba0f98-795c-49b9-aafe-0bcf05db544c) using the Microsoft identity platform token endpoint. Use this when you need to obtain an access token scoped to a specific, hardcoded tenant for authenticating subsequent Microsoft Graph or Microsoft 365 API requests. This tool uses a fixed tenant ID in its endpoint; if you need to generate a token for a different or configurable tenant, use microsoft_graph_generate_auth_token or microsoft_graph_generate_auth_token_with_client_credentials instead.

        Args:
            connection:  (required)
            client_id: 
            client_secret: 
            grant_type: 
            password: 
            scope: 
            username: 
        Returns:
            API response as a dictionary.
        """
        ...

    def microsoft_graph_get_active_token(
        self,
    ) -> Dict[str, Any]:
        """Obtains an active OAuth2 access token from the Microsoft identity platform using the organizations endpoint and v2 token URL. Use this when you need to retrieve a currently valid access token for the authenticated session scoped to organizational accounts. Note that this shares the same endpoint as microsoft_graph_refresh_token and microsoft_graph_generate_token (organizations v2); distinguish usage by the grant type passed in the request body. Do not use this for personal Microsoft accounts or for fixed-tenant token generation.
        Returns:
            API response as a dictionary.
        """
        ...

    def microsoft_graph_get_my_tenant(
        self,
    ) -> Dict[str, Any]:
        """Retrieves organization-level details for the current authenticated tenant from Microsoft Graph, including tenant ID, display name, and domain information. Use this when you need to confirm or inspect properties of the tenant associated with the current authentication context. Note that this calls the /organization endpoint, which returns a collection — use microsoft_graph_list_organizations if you intend to enumerate multiple organizations. Do not use this for retrieving user-specific details.
        Returns:
            API response as a dictionary.
        """
        ...

    def microsoft_graph_get_my_user_details(
        self,
        expand: Optional[str] = None,
        select: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Retrieves the Microsoft 365 profile details of the currently authenticated user, including display name, email address, job title, and other directory attributes. Use this when you need information about the signed-in user without knowing their user ID. Do not use this to retrieve details of another user — use microsoft_graph_get_user with a specific userId for that purpose.

        Args:
            expand: 
            select: 
        Returns:
            API response as a dictionary.
        """
        ...

    def microsoft_graph_get_permissions(
        self,
        appId: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Retrieves the permissions and delegated scopes associated with a service principal identified by its application ID (appId) from Microsoft Graph. Use this when you need to inspect what OAuth2 permissions or app roles are assigned to a specific applications service principal. Do not use this to list all service principals or to retrieve user-level permissions — use the appropriate user or organization tools for those purposes.

        Args:
            appId: 
        Returns:
            API response as a dictionary.
        """
        ...

    def microsoft_graph_get_user(
        self,
        expand: Optional[str] = None,
        select: Optional[str] = None,
        userId: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Retrieves the full profile details of a specific Microsoft Entra ID user identified by their userId from Microsoft Graph, including display name, email, job title, and directory attributes. Use this when you need detailed information about one known user. Do not use this to list multiple users — use microsoft_graph_list_users for that purpose. Do not use this to retrieve the currently authenticated users details — use microsoft_graph_get_my_user_details instead.

        Args:
            expand: 
            select: 
            userId: 
        Returns:
            API response as a dictionary.
        """
        ...

    def microsoft_graph_list_my_direct_reports(
        self,
        select: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Retrieves the list of users who directly report to the currently authenticated user according to the Microsoft 365 organizational hierarchy. Use this when you need to enumerate the direct reports of the signed-in user. Do not use this to retrieve direct reports for another specific user — use microsoft_graph_list_user_direct_reports for that purpose.

        Args:
            select: 
        Returns:
            API response as a dictionary.
        """
        ...

    def microsoft_graph_list_organizations(
        self,
    ) -> Dict[str, Any]:
        """Retrieves a list of all organizations (tenants) accessible via Microsoft Graph for the authenticated context. Use this when you need to enumerate organization details such as tenant IDs, display names, and verified domains. Do not use this when you only need details of the current authenticated tenant — use microsoft_graph_get_my_tenant for that purpose.
        Returns:
            API response as a dictionary.
        """
        ...

    def microsoft_graph_list_user_direct_reports(
        self,
        select: Optional[str] = None,
        userId: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Retrieves the list of users who directly report to a specified user (identified by userId) according to the Microsoft 365 organizational hierarchy. Use this when you need to enumerate the direct reports of a specific user other than the currently authenticated one. Do not use this to retrieve the direct reports of the signed-in user — use microsoft_graph_list_my_direct_reports for that purpose.

        Args:
            select: 
            userId: 
        Returns:
            API response as a dictionary.
        """
        ...

    def microsoft_graph_list_users(
        self,
        count: Optional[str] = None,
        expand: Optional[str] = None,
        filter: Optional[str] = None,
        orderBy: Optional[str] = None,
        select: Optional[str] = None,
        skiptoken: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Retrieves a list of all users in the Microsoft Entra ID (Azure AD) tenant via Microsoft Graph. Use this when you need to enumerate users across the organization, for example to audit accounts, populate a directory, or search for users by filtering the response. Do not use this to retrieve details of a single specific user — use microsoft_graph_get_user with a userId for that purpose.

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

    def microsoft_graph_reauthorize_subscription(
        self,
        subscriptionId: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Reauthorizes an existing Microsoft Graph subscription to restore or extend its authorization before it expires or becomes unauthorized. Use this when a subscriptions authorization has lapsed or when Microsoft Graph notifies you that reauthorization is required to continue receiving webhook notifications. This is a write operation that updates the authorization state of the subscription identified by subscriptionId. Do not use this to create a new subscription or to renew its expiration date — use the create or update subscription tools for those purposes.

        Args:
            subscriptionId: 
        Returns:
            API response as a dictionary.
        """
        ...

    def microsoft_graph_refresh_token(
        self,
        client_id: Optional[str] = None,
        client_secret: Optional[str] = None,
        redirect_uri: Optional[str] = None,
        refresh_token: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Refreshes an existing OAuth2 access token using a refresh token against the Microsoft identity platform organizations v2 endpoint, returning a new access token and optionally a new refresh token to maintain session validity. Use this when an existing access token has expired and you have a valid refresh token available. Do not use this to generate a new token from scratch — use microsoft_graph_generate_token or microsoft_graph_get_active_token for initial token acquisition.

        Args:
            client_id: 
            client_secret: 
            redirect_uri: 
            refresh_token: 
        Returns:
            API response as a dictionary.
        """
        ...

    def microsoft_intune_create_subscription(
        self,
        changeType: str,
        expirationDateTime: str,
        resource: str,
        NotificationUrl: Optional[str] = None,
        clientState: Optional[str] = None,
        lifecycleNotificationUrl: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Creates a new Microsoft Graph change notification subscription to receive real-time webhook notifications for Intune or Azure AD resource changes such as device state changes or group membership updates. Use this when you need continuous event-driven notifications delivered to a configured webhook endpoint. The subscription remains active until it expires or is explicitly deleted. This action has persistent side effects — notifications will be sent to the webhook endpoint until the subscription is removed. Do not use this for one-time data queries; use the appropriate list or get tool instead.

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

