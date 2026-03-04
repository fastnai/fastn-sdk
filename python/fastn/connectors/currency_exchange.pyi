"""Fastn Currency Exchange connector — auto-generated type stubs.

Do not edit manually. Regenerate with `fastn connector sync`.
"""
from __future__ import annotations

from typing import Any, Dict, List, Optional, TypedDict


class CurrencyExchangeConnector:
    """Currency Exchange connector ().

    Provides 2 tools.
    """

    def currency_exchange_convert_currency(
        self,
        from: str,
        to: str,
    ) -> Dict[str, Any]:
        """Converts an amount from a base currency to one or more target currencies using real-time exchange rates from the Currency Exchange service. Use this when you need the current converted value between currency pairs. Do not use this for historical rate lookups. Does not modify any data.

        Args:
            from: The three-letter ISO 4217 code of the source currency (e.g., USD). (required)
            to: The three-letter ISO 4217 code of the target currency (e.g., EUR). (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def currency_exchange_list_currencies(
        self,
        access_key: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Returns a list of all currencies supported by the Currency Exchange service. Use this to discover valid currency codes before performing a conversion or rate lookup. Does not perform any conversion or return exchange rate values. Does not modify any data.

        Args:
            access_key: 
        Returns:
            API response as a dictionary.
        """
        ...

