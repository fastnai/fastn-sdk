"""Fastn Authorization connector — auto-generated type stubs.

Do not edit manually. Regenerate with `fastn connector sync`.
"""
from __future__ import annotations

from typing import Any, Dict, List, Optional


class AuthorizationConnector:
    """Authorization connector ().

    Provides 19 tools.
    """

    def activate_connector(
        self,
        Authorization: Optional[str] = None,
        x_fastn_space_tenantid: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Activates the connector for routing requests and establishing connections to specific services or APIs, ensuring operational readiness.

        Args:
            Authorization: 
            x_fastn_space_tenantid: 
        Returns:
            API response as a dictionary.
        """
        ...

    def auth_code_basic(
        self,
        code: Optional[str] = None,
        grant_type: Optional[str] = None,
        redirect_uri: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Executes an authorization code grant flow utilizing basic authentication, ensuring secure access token retrieval in OAuth 2.0.

        Args:
            code: 
            grant_type: 
            redirect_uri: 
        Returns:
            API response as a dictionary.
        """
        ...

    def auth_code_param(
        self,
        client_id: Optional[str] = None,
        client_secret: Optional[str] = None,
        code: Optional[str] = None,
        redirect_uri: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Fetches the authorization code from a request parameter during the OAuth 2.0 authorization code flow, essential for the token exchange process.

        Args:
            client_id: 
            client_secret: 
            code: 
            redirect_uri: 
        Returns:
            API response as a dictionary.
        """
        ...

    def authorization_code_grant(
        self,
        client_id: Optional[str] = None,
        client_secret: Optional[str] = None,
        code: Optional[str] = None,
        redirect_uri: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Performs an authorization code grant in the OAuth 2.0 flow where the client can exchange an authorization code for an access token, enabling secure API access.

        Args:
            client_id: 
            client_secret: 
            code: 
            redirect_uri: 
        Returns:
            API response as a dictionary.
        """
        ...

    def authorization_code_grant_with_grant_type(
        self,
        client_id: Optional[str] = None,
        client_secret: Optional[str] = None,
        code: Optional[str] = None,
        grant_type: Optional[str] = None,
        redirect_uri: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Initiates the authorization code grant flow with a specified grant type in the OAuth 2.0 protocol, allowing the application to obtain an access token for a resource owner.

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

    def client_credentials_grant(
        self,
        client_id: Optional[str] = None,
        client_secret: Optional[str] = None,
        grant_type: Optional[str] = None,
        scope: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Allows a client application to obtain an access token by using the client credentials, typically for machine-to-machine communication in the OAuth 2.0 framework.

        Args:
            client_id: 
            client_secret: 
            grant_type: 
            scope: 
        Returns:
            API response as a dictionary.
        """
        ...

    def dataplane_connector(
        self,
        apiKey: Optional[str] = None,
        projectId: Optional[str] = None,
        tenantId: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Establishes a connection to a data plane service, facilitating data management and interaction with the connected data environments.

        Args:
            apiKey: 
            projectId: 
            tenantId: 
        Returns:
            API response as a dictionary.
        """
        ...

    def device_code_grant(
        self,
        client_id: Optional[str] = None,
        device_code: Optional[str] = None,
        grant_type: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Facilitates the device code grant flow, allowing users to request access tokens from a device that does not have a browser or limited input capabilities.

        Args:
            client_id: 
            device_code: 
            grant_type: 
        Returns:
            API response as a dictionary.
        """
        ...

    def generate_token_with_json_request(
        self,
        client_id: Optional[str] = None,
        client_secret: Optional[str] = None,
        code: Optional[str] = None,
        grant_type: Optional[str] = None,
        redirect_uri: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Generates an access token using JSON request parameters, streamlining the token acquisition process in a structured manner.

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

    def get_user(
        self,
        baseUrl: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Retrieves user information from the connected service, allowing applications to access and utilize user data effectively.

        Args:
            baseUrl: 
        Returns:
            API response as a dictionary.
        """
        ...

    def refresh_code_param(
        self,
        client_id: Optional[str] = None,
        client_secret: Optional[str] = None,
        fb_exchange_token: Optional[str] = None,
        grant_type: Optional[str] = None,
        set_token_expires_in_60_days: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Retrieves the refresh code from a request parameter, essential for renewing access tokens in the OAuth 2.0 implementation.

        Args:
            client_id: 
            client_secret: 
            fb_exchange_token: 
            grant_type: 
            set_token_expires_in_60_days: 
        Returns:
            API response as a dictionary.
        """
        ...

    def refresh_token_basic_auth_grant(
        self,
        grant_type: Optional[str] = None,
        refresh_token: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Enables the refreshing of an access token using basic authentication with a refresh token, allowing continued access without requiring re-login.

        Args:
            grant_type: 
            refresh_token: 
        Returns:
            API response as a dictionary.
        """
        ...

    def refresh_token_simple(
        self,
        client_id: Optional[str] = None,
        client_secret: Optional[str] = None,
        grant_type: Optional[str] = None,
        refresh_token: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Implements a refresh token request that simplifies the token refresh process in an OAuth 2.0 environment without additional authentication layers.

        Args:
            client_id: 
            client_secret: 
            grant_type: 
            refresh_token: 
        Returns:
            API response as a dictionary.
        """
        ...

    def refresh_token_with_grant_type(
        self,
        client_id: Optional[str] = None,
        client_secret: Optional[str] = None,
        grant_type: Optional[str] = None,
        redirect_uri: Optional[str] = None,
        refresh_token: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Executes the refresh token grant flow using a specified grant type to obtain a new access token without requiring the user to re-authenticate.

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

    def refresh_token_with_json_request(
        self,
        client_id: Optional[str] = None,
        client_secret: Optional[str] = None,
        grant_type: Optional[str] = None,
        refresh_token: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Processes a refresh token request using JSON request parameters to obtain a new access token while ensuring secure continuity.

        Args:
            client_id: 
            client_secret: 
            grant_type: 
            refresh_token: 
        Returns:
            API response as a dictionary.
        """
        ...

    def refresh_token_with_redirect_url(
        self,
        client_id: Optional[str] = None,
        client_secret: Optional[str] = None,
        grant_type: Optional[str] = None,
        redirect_uri: Optional[str] = None,
        refresh_token: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Performs token refresh with the inclusion of a redirect URL, enabling effective redirection to the appropriate resource in the OAuth 2.0 protocol.

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

    def refresh_tokenwith_access_type(
        self,
        access_type: Optional[str] = None,
        client_id: Optional[str] = None,
        client_secret: Optional[str] = None,
        grant_type: Optional[str] = None,
        refresh_token: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Operates the refresh token process while considering access type parameters, serving to refine token issuance in the OAuth 2.0 context.

        Args:
            access_type: 
            client_id: 
            client_secret: 
            grant_type: 
            refresh_token: 
        Returns:
            API response as a dictionary.
        """
        ...

    def resource_owner_password_credentials_grant(
        self,
        client_id: Optional[str] = None,
        client_secret: Optional[str] = None,
        grant_type: Optional[str] = None,
        password: Optional[str] = None,
        scope: Optional[str] = None,
        username: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Enables the acquisition of an access token by utilizing the resource owner's username and password, suited for first-party applications in OAuth 2.0.

        Args:
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

    def simple_authorization_code_grant_(
        self,
        client_id: Optional[str] = None,
        client_secret: Optional[str] = None,
        code: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Conducts a simple authorization code grant exchange in the OAuth 2.0 protocol, where a client can easily acquire an access token with minimal complexity.

        Args:
            client_id: 
            client_secret: 
            code: 
        Returns:
            API response as a dictionary.
        """
        ...

