"""Fastn Authorization connector — auto-generated type stubs.

Do not edit manually. Regenerate with `fastn connector sync`.
"""
from __future__ import annotations

from typing import Any, Dict, List, Optional, TypedDict


class _AuthorizationActivateConnectorInput(TypedDict, total=False):
    fastn_connection: Dict[str, Any]
    oauth: Dict[str, Any]

class AuthorizationConnector:
    """Authorization connector ().

    Provides 21 tools.
    """

    def authorization_activate_connector(
        self,
        Authorization: Optional[str] = None,
        domain: Optional[str] = None,
        input: Optional[_AuthorizationActivateConnectorInput] = None,
        x_fastn_space_tenantid: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Activates a connector to enable routing of requests and establish connections to specific services or APIs. Use this tool when a connector must be activated before it can process requests or relay traffic. Do not use this for token operations — this tool changes the operational state of the connector. Sends a POST request to the ActivateConnector API endpoint; this action modifies connector state and may be irreversible without a corresponding deactivation step.

        Args:
            Authorization: 
            domain: 
            input: 
            x_fastn_space_tenantid: 
        Returns:
            API response as a dictionary.
        """
        ...

    def authorization_client_credentials_grant(
        self,
        baseUrl: Optional[str] = None,
        client_id: Optional[str] = None,
        client_secret: Optional[str] = None,
        grant_type: Optional[str] = None,
        scope: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Obtains an OAuth 2.0 access token using client credentials (client ID and client secret), without any user context. Use this tool for machine-to-machine (M2M) communication where the application acts on its own behalf rather than on behalf of a user. Do not use this when a user context or delegated access is required — use an authorization code grant tool instead. Sends a POST request to the base URL and returns a client-scoped access token.

        Args:
            baseUrl: 
            client_id: 
            client_secret: 
            grant_type: 
            scope: 
        Returns:
            API response as a dictionary.
        """
        ...

    def authorization_connect_dataplane(
        self,
        apiKey: Optional[str] = None,
        apiName: Optional[str] = None,
        domain: Optional[str] = None,
        input: Optional[Dict[str, Any]] = None,
        projectId: Optional[str] = None,
        tenantId: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Establishes a connection to a data plane service endpoint, enabling data management operations and interaction with the connected data environment. Use this tool when you need to route requests through a data plane API for data processing or management. Do not use this for standard OAuth token operations. Sends a POST request to the configured data plane API endpoint and may alter connection state.

        Args:
            apiKey: 
            apiName: 
            domain: 
            input: 
            projectId: 
            tenantId: 
        Returns:
            API response as a dictionary.
        """
        ...

    def authorization_device_code_grant(
        self,
        baseUrl: Optional[str] = None,
        client_id: Optional[str] = None,
        device_code: Optional[str] = None,
        grant_type: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Executes the OAuth 2.0 device authorization grant flow, allowing a device with limited or no browser input capabilities to request an access token. Use this tool when the client device cannot perform a redirect-based OAuth flow (e.g., smart TVs, CLI tools). Do not use this for flows where the user can interact with a browser — use authorization_code_grant tools instead. Sends a POST request to the base URL and returns an access token upon successful device authorization.

        Args:
            baseUrl: 
            client_id: 
            device_code: 
            grant_type: 
        Returns:
            API response as a dictionary.
        """
        ...

    def authorization_exchange_auth_code(
        self,
        baseUrl: Optional[str] = None,
        client_id: Optional[str] = None,
        client_secret: Optional[str] = None,
        code: Optional[str] = None,
        redirect_uri: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Exchanges an OAuth 2.0 authorization code for an access token by submitting client credentials and the code in the request body. Use this tool as the standard authorization code grant exchange step after the user has authorized the application and you have received the authorization code. Do not use this if the endpoint requires Basic authentication — use exchange_auth_code_basic instead, or if a grant type parameter is required, use exchange_auth_code_with_grant_type. Sends a POST request to the base URL.

        Args:
            baseUrl: 
            client_id: 
            client_secret: 
            code: 
            redirect_uri: 
        Returns:
            API response as a dictionary.
        """
        ...

    def authorization_exchange_auth_code_basic(
        self,
        baseUrl: Optional[str] = None,
        code: Optional[str] = None,
        grant_type: Optional[str] = None,
        redirect_uri: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Exchanges an authorization code for an access token using HTTP Basic authentication in the OAuth 2.0 authorization code grant flow. Use this tool when the token endpoint requires Basic authentication (client ID and secret as Base64-encoded credentials) during the code exchange step. Do not use this if the client credentials are passed in the request body — use authorizationCodeGrant instead. Sends a POST request to the base URL.

        Args:
            baseUrl: 
            code: 
            grant_type: 
            redirect_uri: 
        Returns:
            API response as a dictionary.
        """
        ...

    def authorization_exchange_auth_code_simple(
        self,
        baseUrl: Optional[str] = None,
        client_id: Optional[str] = None,
        client_secret: Optional[str] = None,
        code: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Exchanges an OAuth 2.0 authorization code for an access token using a minimal, straightforward request with no additional parameters. Use this tool for simple authorization code grant flows where only the code, client ID, client secret, and redirect URI are required. Do not use this if your flow requires grant type, Basic authentication, or other additional parameters — use the appropriate specialized grant tool instead. Sends a POST request to the base URL.

        Args:
            baseUrl: 
            client_id: 
            client_secret: 
            code: 
        Returns:
            API response as a dictionary.
        """
        ...

    def authorization_exchange_auth_code_with_grant_type(
        self,
        baseUrl: Optional[str] = None,
        client_id: Optional[str] = None,
        client_secret: Optional[str] = None,
        code: Optional[str] = None,
        grant_type: Optional[str] = None,
        redirect_uri: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Exchanges an OAuth 2.0 authorization code for an access token by explicitly including the authorization_code grant type parameter in the request body. Use this tool when the token endpoint requires the grant_type field to be set during the authorization code exchange. Do not use this if the endpoint does not require an explicit grant_type parameter — use exchange_auth_code instead. Sends a POST request to the base URL.

        Args:
            baseUrl: 
            client_id: 
            client_secret: 
            code: 
            grant_type: 
            redirect_uri: 
        Returns:
            API response as a dictionary.
        """
        ...

    def authorization_generate_token_with_json_request(
        self,
        baseUrl: Optional[str] = None,
        client_id: Optional[str] = None,
        client_secret: Optional[str] = None,
        code: Optional[str] = None,
        grant_type: Optional[str] = None,
        redirect_uri: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Generates a new access token by submitting credentials or grant parameters as a JSON request body. Use this tool when the token endpoint requires JSON-formatted input to issue a new token. Do not use this to refresh an existing token — use a refresh token tool instead. Sends a POST request to the base URL and returns a new access token.

        Args:
            baseUrl: 
            client_id: 
            client_secret: 
            code: 
            grant_type: 
            redirect_uri: 
        Returns:
            API response as a dictionary.
        """
        ...

    def authorization_get_auth_code_param(
        self,
        baseUrl: Optional[str] = None,
        client_id: Optional[str] = None,
        client_secret: Optional[str] = None,
        code: Optional[str] = None,
        redirect_uri: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Retrieves the authorization code from a URL query parameter during the OAuth 2.0 authorization code flow. Use this tool when you need to extract the authorization code value passed as a request parameter before exchanging it for an access token. Do not use this to exchange the code for a token — use an authorization code grant tool for that step. Sends a GET request to the base URL.

        Args:
            baseUrl: 
            client_id: 
            client_secret: 
            code: 
            redirect_uri: 
        Returns:
            API response as a dictionary.
        """
        ...

    def authorization_get_refresh_code_param(
        self,
        baseUrl: Optional[str] = None,
        client_id: Optional[str] = None,
        client_secret: Optional[str] = None,
        fb_exchange_token: Optional[str] = None,
        grant_type: Optional[str] = None,
        set_token_expires_in_60_days: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Retrieves the refresh code from a URL query parameter, typically as a step in the OAuth 2.0 token renewal flow. Use this tool when you need to extract a refresh code passed as a request parameter before exchanging it for a new access token. Do not use this to directly obtain an access token — it only retrieves the refresh code value. Sends a GET request to the base URL.

        Args:
            baseUrl: 
            client_id: 
            client_secret: 
            fb_exchange_token: 
            grant_type: 
            set_token_expires_in_60_days: 
        Returns:
            API response as a dictionary.
        """
        ...

    def authorization_get_token_with_app_key_secret(
        self,
        app_key: Optional[str] = None,
        app_secret: Optional[str] = None,
        auth_code: Optional[str] = None,
        baseUrl: Optional[str] = None,
        grant_type: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Retrieves an access token by authenticating with an application key and application secret. Use this tool when you need to obtain a new access token via app-key/secret credentials. Does not refresh existing tokens — use a refresh token tool for that. Calling this tool initiates an authenticated GET request and returns a new token.

        Args:
            app_key: 
            app_secret: 
            auth_code: 
            baseUrl: 
            grant_type: 
        Returns:
            API response as a dictionary.
        """
        ...

    def authorization_refresh_token_basic_auth(
        self,
        baseUrl: Optional[str] = None,
        grant_type: Optional[str] = None,
        refresh_token: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Refreshes an OAuth 2.0 access token using a refresh token submitted with HTTP Basic authentication (client ID and secret as Base64-encoded credentials). Use this tool when the token endpoint requires Basic authentication during the refresh grant flow. Do not use this if the endpoint accepts client credentials in the request body — use refresh_token_simple or refresh_token_with_grant_type instead. Sends a POST request to the base URL.

        Args:
            baseUrl: 
            grant_type: 
            refresh_token: 
        Returns:
            API response as a dictionary.
        """
        ...

    def authorization_refresh_token_simple(
        self,
        baseUrl: Optional[str] = None,
        client_id: Optional[str] = None,
        client_secret: Optional[str] = None,
        grant_type: Optional[str] = None,
        refresh_token: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Refreshes an expired OAuth 2.0 access token using a minimal request with no additional authentication layers or extra parameters. Use this tool for straightforward token refresh scenarios where only the refresh token is required. Do not use this if your token endpoint requires Basic authentication, a specific grant type parameter, or JSON body format — use the appropriate specialized refresh tool instead. Sends a POST request to the base URL.

        Args:
            baseUrl: 
            client_id: 
            client_secret: 
            grant_type: 
            refresh_token: 
        Returns:
            API response as a dictionary.
        """
        ...

    def authorization_refresh_token_with_access_type(
        self,
        access_type: Optional[str] = None,
        baseUrl: Optional[str] = None,
        client_id: Optional[str] = None,
        client_secret: Optional[str] = None,
        grant_type: Optional[str] = None,
        refresh_token: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Refreshes an OAuth 2.0 access token and includes an access type parameter (e.g., offline or online) in the request to control token issuance behavior. Use this tool when the token endpoint requires an explicit access type during refresh, such as when requesting offline access. Do not use this for simple refresh flows that do not require an access type parameter — use refresh_token_simple instead. Sends a POST request to the base URL.

        Args:
            access_type: 
            baseUrl: 
            client_id: 
            client_secret: 
            grant_type: 
            refresh_token: 
        Returns:
            API response as a dictionary.
        """
        ...

    def authorization_refresh_token_with_app_key_secret(
        self,
        app_key: Optional[str] = None,
        app_secret: Optional[str] = None,
        grant_type: Optional[str] = None,
        refresh_token: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Refreshes an existing access token by authenticating with an application key and application secret. Use this tool when an access token has expired and you need a new one using app-key/secret credentials. Do not use this to obtain a first-time token — use the get_token_with_app_key_secret tool instead. This tool sends a GET request to the auth base URL.

        Args:
            app_key: 
            app_secret: 
            grant_type: 
            refresh_token: 
        Returns:
            API response as a dictionary.
        """
        ...

    def authorization_refresh_token_with_grant_type(
        self,
        baseUrl: Optional[str] = None,
        client_id: Optional[str] = None,
        client_secret: Optional[str] = None,
        grant_type: Optional[str] = None,
        redirect_uri: Optional[str] = None,
        refresh_token: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Refreshes an OAuth 2.0 access token by explicitly including the refresh_token grant type parameter in the request body. Use this tool when the token endpoint requires the grant_type field to be set to refresh_token for the refresh flow. Do not use this for endpoints that infer the grant type automatically — use refresh_token_simple instead. Sends a POST request to the base URL.

        Args:
            baseUrl: 
            client_id: 
            client_secret: 
            grant_type: 
            redirect_uri: 
            refresh_token: 
        Returns:
            API response as a dictionary.
        """
        ...

    def authorization_refresh_token_with_json_request(
        self,
        baseUrl: Optional[str] = None,
        client_id: Optional[str] = None,
        client_secret: Optional[str] = None,
        grant_type: Optional[str] = None,
        refresh_token: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Refreshes an existing access token by submitting token parameters as a JSON request body. Use this tool when the token endpoint requires JSON-formatted input for the refresh grant. Do not use this if the endpoint expects form-encoded parameters — use a form-based refresh tool instead. Sends a POST request and returns a new access token.

        Args:
            baseUrl: 
            client_id: 
            client_secret: 
            grant_type: 
            refresh_token: 
        Returns:
            API response as a dictionary.
        """
        ...

    def authorization_refresh_token_with_redirect_url(
        self,
        client_id: Optional[str] = None,
        client_secret: Optional[str] = None,
        grant_type: Optional[str] = None,
        redirect_uri: Optional[str] = None,
        refresh_token: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Refreshes an OAuth 2.0 access token and includes a redirect URL in the request, enabling redirection to the appropriate resource after token renewal. Use this tool when your OAuth 2.0 flow requires a redirect URL during the token refresh step (e.g., Contentful OAuth). Do not use this for refresh flows that do not require a redirect URL — use a simpler refresh token tool instead. Sends a POST request to the Contentful OAuth token endpoint.

        Args:
            client_id: 
            client_secret: 
            grant_type: 
            redirect_uri: 
            refresh_token: 
        Returns:
            API response as a dictionary.
        """
        ...

    def authorization_resource_owner_password_grant(
        self,
        baseUrl: Optional[str] = None,
        client_id: Optional[str] = None,
        client_secret: Optional[str] = None,
        grant_type: Optional[str] = None,
        password: Optional[str] = None,
        scope: Optional[str] = None,
        username: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Obtains an OAuth 2.0 access token by submitting the resource owners username and password directly to the token endpoint. Use this tool only for trusted, first-party applications where the client can securely handle user credentials. Do not use this for third-party applications or when user credentials should not be exposed to the client — use authorization code grant flows instead. Sends a POST request to the base URL; handle credentials with care as this flow transmits user passwords.

        Args:
            baseUrl: 
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

    def fabric_get_user(
        self,
        baseUrl: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Retrieves profile and identity details for the currently authenticated user from the configured Fabric base URL. Use this tool to fetch user information after authentication has been established. Do not use this tool to manage tokens or perform authentication flows — use fabric_get_access_token or fabric_generate_auth_token instead. This is a read-only operation with no side effects.

        Args:
            baseUrl: 
        Returns:
            API response as a dictionary.
        """
        ...

