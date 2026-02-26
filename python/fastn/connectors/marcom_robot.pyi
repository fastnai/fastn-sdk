"""Fastn Marcom Robot connector — auto-generated type stubs.

Do not edit manually. Regenerate with `fastn connector sync`.
"""
from __future__ import annotations

from typing import Any, Dict, List, Optional


class MarcomRobotConnector:
    """Marcom Robot connector ().

    Provides 2 tools.
    """

    def domain_enrichment(
        self,
        company_domain: str,
    ) -> Dict[str, Any]:
        """Enriches domain information in your system by enhancing data with additional insights, utilizing the domainEnrichment connector for better understanding of web domains and their associated attributes.

        Args:
            company_domain: The domain of the company. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def email_enrichment(
        self,
        company_email: str,
    ) -> Dict[str, Any]:
        """Enriches email data in your system by retrieving supplementary information about email addresses, using the emailEnrichment connector to improve contact records and enhance engagement strategies.

        Args:
            company_email: The company email address. (required)
        Returns:
            API response as a dictionary.
        """
        ...

