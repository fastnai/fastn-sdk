"""Fastn Token Metrics connector — auto-generated type stubs.

Do not edit manually. Regenerate with `fastn connector sync`.
"""
from __future__ import annotations

from typing import Any, Dict, List, Optional


class TokenMetricsConnector:
    """Token Metrics connector ().

    Provides 6 tools.
    """

    def ai_reports(
        self,
        limit: Optional[str] = None,
        page: Optional[str] = None,
        symbol: Optional[str] = None,
        token_id: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Generates comprehensive reports using the AIReports tool to analyze data trends and insights.

        Args:
            limit: The maximum number of results to return.
            page: The page number of the results to return.
            symbol: The symbol of the token (e.g., BTC, ETH).
            token_id: The unique identifier for the token.
        Returns:
            API response as a dictionary.
        """
        ...

    def correlation(
        self,
        category: Optional[str] = None,
        exchange: Optional[str] = None,
        limit: Optional[str] = None,
        page: Optional[str] = None,
        symbol: Optional[str] = None,
        token_id: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Analyzes the relationship between multiple data sets using the correlation tool to identify dependencies and patterns.

        Args:
            category: Filter results by token category.
            exchange: Filter results by exchange.
            limit: Limit the number of results returned.
            page: Specify the page number for paginated results.
            symbol: Filter results by token symbol.
            token_id: Filter results by token ID.
        Returns:
            API response as a dictionary.
        """
        ...

    def get_coins_detail(
        self,
        blockchain_address: Optional[str] = None,
        category: Optional[str] = None,
        exchange: Optional[str] = None,
        limit: Optional[str] = None,
        page: Optional[str] = None,
        symbol: Optional[str] = None,
        token_id: Optional[str] = None,
        token_name: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Retrieves detailed information about various cryptocurrencies using the getCoinsDetail tool to provide insights on market performance.

        Args:
            blockchain_address: The blockchain address to filter by.
            category: The category of tokens to filter by.
            exchange: The exchange to filter by.
            limit: The maximum number of results to return.
            page: The page number for pagination.
            symbol: The token symbol to filter by.
            token_id: The token ID to filter by.
            token_name: The token name to filter by.
        Returns:
            API response as a dictionary.
        """
        ...

    def support_and_resistance(
        self,
        limit: Optional[str] = None,
        page: Optional[str] = None,
        symbol: Optional[str] = None,
        token_id: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Identifies key support and resistance levels in market data using the supportAndResistance tool for trading strategy development.

        Args:
            limit: The maximum number of results to return.
            page: The page number of results to retrieve.
            symbol: The symbol of the token (e.g., BTC, ETH).
            token_id: The unique identifier for the token.
        Returns:
            API response as a dictionary.
        """
        ...

    def top_token_by_market_cap(
        self,
        top_k: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Fetches the top tokens ranked by market capitalization using the topTokenByMarketCap tool to inform investment decisions.

        Args:
            top_k: Number of top results to return.
        Returns:
            API response as a dictionary.
        """
        ...

    def trading_signal(
        self,
        category: Optional[str] = None,
        endDate: Optional[str] = None,
        exchange: Optional[str] = None,
        fdv: Optional[str] = None,
        limit: Optional[str] = None,
        marketcap: Optional[str] = None,
        page: Optional[str] = None,
        signal: Optional[str] = None,
        startDate: Optional[str] = None,
        symbol: Optional[str] = None,
        token_id: Optional[str] = None,
        volume: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Provides actionable trading signals based on market analysis using the tradingSignal tool to enhance trading strategies.

        Args:
            category: Filter results by token category.
            endDate: The end date for the data range (YYYY-MM-DD).
            exchange: Filter results by exchange.
            fdv: Filter results by FDV.
            limit: Limit the number of results returned.
            marketcap: Filter results by market capitalization.
            page: Specify the page number for pagination.
            signal: Filter results by signal.
            startDate: The start date for the data range (YYYY-MM-DD).
            symbol: Filter results by token symbol.
            token_id: Filter results by token ID.
            volume: Filter results by volume.
        Returns:
            API response as a dictionary.
        """
        ...

