"""Fastn Netlify connector — auto-generated type stubs.

Do not edit manually. Regenerate with `fastn connector sync`.
"""
from __future__ import annotations

from typing import Any, Dict, List, Optional


class NetlifyConnector:
    """Netlify connector ().

    Provides 3 tools.
    """

    def create_site(
        self,
        custom_domain: Optional[str] = None,
        name: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Creates a new site using the specified connector in the context of web hosting management.

        Args:
            custom_domain: 
            name: 
        Returns:
            API response as a dictionary.
        """
        ...

    def deploy_code_to_site(
        self,
    ) -> Dict[str, Any]:
        """Deploys code to the specified site using the designated connector, effectively updating the website with new features or fixes.
        Returns:
            API response as a dictionary.
        """
        ...

    def get_site_deploys(
        self,
        siteId: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Retrieves the list of deployments associated with the specified site through the connector, allowing for tracking of changes and versions.

        Args:
            siteId: 
        Returns:
            API response as a dictionary.
        """
        ...

