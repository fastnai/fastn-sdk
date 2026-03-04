"""Fastn Power Automate connector — auto-generated type stubs.

Do not edit manually. Regenerate with `fastn connector sync`.
"""
from __future__ import annotations

from typing import Any, Dict, List, Optional, TypedDict


class _PowerAutomateCreateCustomConnectorProperties(TypedDict, total=False):
    backendService: Dict[str, Any]
    capabilities: List[Any]
    connectionParameterSets: str
    connectionParameters: Dict[str, Any]
    description: str
    displayName: str
    environment: Dict[str, Any]
    openApiDefinition: Dict[str, Any]
    policyTemplateInstances: List[Any]

class PowerAutomateConnector:
    """Power Automate connector ().

    Provides 3 tools.
    """

    def power_automate_create_custom_connector(
        self,
        properties: _PowerAutomateCreateCustomConnectorProperties,
        expand: Optional[str] = None,
        filter: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Creates a new custom connector in the Power Apps environment in the United States region by providing a name and description. Use this tool when you need to register a new custom API connector within the Microsoft Power Platform. This action provisions a new resource and is not reversible without explicitly deleting the created connector. Requires a valid access token, connector name, and description.

        Args:
            properties: Properties of the Power Automate connector. (required)
            expand: Expansion parameters for related data.
            filter: Filter criteria for data retrieval.
        Returns:
            API response as a dictionary.
        """
        ...

    def power_automate_get_access_token(
        self,
        client_id: str,
        client_secret: str,
        password: str,
        tenantId: str,
        username: str,
    ) -> Dict[str, Any]:
        """Requests an OAuth 2.0 access token from Microsofts identity platform for a given tenant, enabling authenticated calls to Power Automate and Power Platform APIs. Use this tool before making any API requests that require bearer token authorization. Do not use this tool to retrieve user credentials or non-OAuth tokens. The token is short-lived; store and reuse it within its validity window rather than calling this tool repeatedly. Requires a valid tenantId, client credentials, and scope.

        Args:
            client_id: Client ID for Power Automate OAuth 2.0 flow. (required)
            client_secret: Client secret for Power Automate OAuth 2.0 flow. (required)
            password: User's password for Power Automate authentication. (required)
            tenantId: Tenant ID for Power Automate. (required)
            username: Username for Power Automate authentication. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def power_automate_get_environment(
        self,
        expand: Optional[str] = None,
        filter: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Retrieves a list of available APIs and connectors for the Power Apps environment in the United States region, providing details on the current operational context and available integrations. Use this tool when you need to inspect what connectors or APIs are available within the Power Platform environment. Note: this endpoint is currently scoped to the United States region. Requires a valid access token.

        Args:
            expand: Expansion parameters for the Power Automate request.
            filter: Filter criteria for the Power Automate request.
        Returns:
            API response as a dictionary.
        """
        ...

