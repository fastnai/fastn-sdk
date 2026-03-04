"""Fastn Netlify connector — auto-generated type stubs.

Do not edit manually. Regenerate with `fastn connector sync`.
"""
from __future__ import annotations

from typing import Any, Dict, List, Optional, TypedDict


class NetlifyConnector:
    """Netlify connector ().

    Provides 3 tools.
    """

    def netlify_create_site(
        self,
        custom_domain: Optional[str] = None,
        name: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Creates a new site on Netlify, provisioning a hosting environment for a web application. Use this tool when you need to register and configure a new site for deployment. Do not use this tool to deploy code to an existing site — use netlify_deploy_code_to_site instead. This operation provisions a new site resource on Netlify.

        Args:
            custom_domain: 
            name: 
        Returns:
            API response as a dictionary.
        """
        ...

    def netlify_deploy_code_to_site(
        self,
        site_id: str,
        Authorization: Optional[str] = None,
        files: Optional[Dict[str, Any]] = None,
    ) -> Dict[str, Any]:
        """Triggers a new deployment of code to a specified Netlify site, updating the live website with new features, fixes, or content. Use this tool when you need to publish changes to an existing site. Do not use this tool to create a new site — use netlify_create_site instead. This operation updates the live site and is not automatically reversible, though previous deploys can be restored via the Netlify dashboard.

        Args:
            site_id:  (required)
            Authorization: 
            files: 
        Returns:
            API response as a dictionary.
        """
        ...

    def netlify_list_site_deploys(
        self,
        siteId: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Lists all deployments associated with a specified Netlify site, returning deploy history including statuses, timestamps, and versions. Use this tool when you need to audit, track, or review past deployments for a site. Do not use this tool to trigger a new deployment — use netlify_deploy_code_to_site instead.

        Args:
            siteId: 
        Returns:
            API response as a dictionary.
        """
        ...

