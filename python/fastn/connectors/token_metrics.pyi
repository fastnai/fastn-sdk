"""Fastn Token Metrics connector — auto-generated type stubs.

Do not edit manually. Regenerate with `fastn connector sync`.
"""
from __future__ import annotations

from typing import Any, Dict, List, Optional, TypedDict


class TokenMetricsConnector:
    """Token Metrics connector ().

    Provides 6 tools.
    """

    def token_metrics_get_correlation(
        self,
        category: Optional[str] = None,
        exchange: Optional[str] = None,
        limit: Optional[str] = None,
        page: Optional[str] = None,
        symbol: Optional[str] = None,
        token_id: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Retrieves correlation coefficients between multiple cryptocurrencies from Token Metrics, measuring how closely their price movements are related. Use this tool when you need to assess portfolio diversification, identify co-moving assets, or understand dependencies between tokens. Do not use this for trading signals, support/resistance levels, or individual token details — use the dedicated tools for those. This is a read-only operation with no side effects.

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

    def token_metrics_get_support_and_resistance(
        self,
        limit: Optional[str] = None,
        page: Optional[str] = None,
        symbol: Optional[str] = None,
        token_id: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Retrieves key support and resistance price levels for cryptocurrencies from Token Metrics. Use this tool when you need to identify critical price zones for a token to inform entry/exit strategies or risk management. Do not use this for trading signals, market cap rankings, or correlation analysis — use the dedicated tools for those. This is a read-only operation with no side effects.

        Args:
            limit: The maximum number of results to return.
            page: The page number of results to retrieve.
            symbol: The symbol of the token (e.g., BTC, ETH).
            token_id: The unique identifier for the token.
        Returns:
            API response as a dictionary.
        """
        ...

    def token_metrics_list_ai_reports(
        self,
        limit: Optional[str] = None,
        page: Optional[str] = None,
        symbol: Optional[str] = None,
        token_id: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Retrieves AI-generated investment research reports for cryptocurrencies from Token Metrics, covering trend analysis, ratings, and data-driven insights. Use this tool when you need in-depth analytical reports on specific tokens or the broader market. Do not use this for raw trading signals, price levels, or coin metadata — use the dedicated tools for those. This is a read-only operation with no side effects.

        Args:
            limit: The maximum number of results to return.
            page: The page number of the results to return.
            symbol: The symbol of the token (e.g., BTC, ETH).
            token_id: The unique identifier for the token.
        Returns:
            API response as a dictionary.
        """
        ...

    def token_metrics_list_coins_detail(
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
        """Retrieves detailed information about one or more cryptocurrencies from Token Metrics, including token metadata, ratings, and market performance metrics. Use this tool when you need a comprehensive profile of specific tokens for research or due diligence. Do not use this for trading signals or top market cap rankings — use the dedicated tools for those. This is a read-only operation with no side effects.

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

    def token_metrics_list_top_tokens_by_market_cap(
        self,
        top_k: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Retrieves a ranked list of the top cryptocurrencies by market capitalization from Token Metrics. Use this tool when you need to identify the largest or most dominant tokens in the market for investment screening or portfolio analysis. Do not use this for trading signals, price history, or individual token details — use the dedicated tools for those. This is a read-only operation with no side effects.

        Args:
            top_k: Number of top results to return.
        Returns:
            API response as a dictionary.
        """
        ...

    def token_metrics_list_trading_signals(
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
        """Retrieves actionable buy, sell, or hold trading signals for cryptocurrencies from Token Metrics, based on AI-driven market analysis. Use this tool when you need to inform trading decisions with quantitative signals across one or more tokens. Do not use this for price data, market cap rankings, or support/resistance levels — use the dedicated tools for those. This is a read-only operation with no side effects.

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

