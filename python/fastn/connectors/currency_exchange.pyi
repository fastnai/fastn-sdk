"""Fastn Currency Exchange connector — auto-generated type stubs.

Do not edit manually. Regenerate with `fastn connector sync`.
"""
from __future__ import annotations

from typing import Any, Dict, List, Optional


class CurrencyExchangeConnector:
    """Currency Exchange connector ().

    Provides 2 tools.
    """

    def all_currencies(
        self,
        access_key: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Provides a list of all available currencies supported by the currency conversion connector.

        Args:
            access_key: 
        Returns:
            API response as a dictionary.
        """
        ...

    def convert_currency(
        self,
        from: str,
        to: str,
    ) -> Dict[str, Any]:
        """Converts an amount from one currency to another using the currency conversion connector.

        Args:
            from: The three-letter ISO 4217 code of the source currency (e.g., USD). (required)
            to: The three-letter ISO 4217 code of the target currency (e.g., EUR). (required)
        Returns:
            API response as a dictionary.
        """
        ...

