"""Fastn Marcom Robot connector — auto-generated type stubs.

Do not edit manually. Regenerate with `fastn connector sync`.
"""
from __future__ import annotations

from typing import Any, Dict, List, Optional, TypedDict


class MarcomRobotConnector:
    """Marcom Robot connector ().

    Provides 2 tools.
    """

    def marcom_robot_enrich_domain(
        self,
        company_domain: str,
    ) -> Dict[str, Any]:
        """Retrieves enriched company and firmographic data for a given web domain using the Marcom Robot enrichment API. Returns information such as company name, industry, size, location, and technology stack associated with the domain. Use this to enrich account records or research a company before engagement. Use marcom_robot_enrich_email if you have a specific contact email address instead. Does not modify any data.

        Args:
            company_domain: The domain of the company. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def marcom_robot_enrich_email(
        self,
        company_email: str,
    ) -> Dict[str, Any]:
        """Retrieves supplementary information about a given email address using the Marcom Robot enrichment API. Returns firmographic and contact-level data associated with the email, such as name, company, job title, and social profiles. Use this to enrich CRM contact records or qualify leads before outreach. Use marcom_robot_enrich_domain if you only have a company domain rather than a specific email address. Does not modify any data.

        Args:
            company_email: The company email address. (required)
        Returns:
            API response as a dictionary.
        """
        ...

