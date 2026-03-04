"""Fastn Tavily connector — auto-generated type stubs.

Do not edit manually. Regenerate with `fastn connector sync`.
"""
from __future__ import annotations

from typing import Any, Dict, List, Optional, TypedDict


class TavilyConnector:
    """Tavily connector ().

    Provides 4 tools.
    """

    def tavily_crawl_content(
        self,
        url: str,
        allow_external: Optional[bool] = None,
        exclude_domains: Optional[List[Any]] = None,
        exclude_paths: Optional[List[Any]] = None,
        extract_depth: Optional[str] = None,
        format: Optional[str] = None,
        include_favicon: Optional[bool] = None,
        include_images: Optional[bool] = None,
        instructions: Optional[str] = None,
        limit: Optional[int] = None,
        max_breadth: Optional[int] = None,
        max_depth: Optional[int] = None,
        select_domains: Optional[List[Any]] = None,
        select_paths: Optional[List[Any]] = None,
    ) -> Dict[str, Any]:
        """Crawls one or more web URLs and retrieves their full page content using Tavilys crawl endpoint. Use this tool when you need to systematically gather raw content from a set of pages, follow links, or collect data across multiple pages of a website. Do not use this tool for a targeted keyword search (use tavily_search_query) or when you only need a structural map of a site (use tavily_map_content). This tool makes a POST request, may follow multiple links, and incurs API usage costs proportional to the number of pages crawled.

        Args:
            url:  (required)
            allow_external: 
            exclude_domains: 
            exclude_paths: 
            extract_depth: 
            format: 
            include_favicon: 
            include_images: 
            instructions: 
            limit: 
            max_breadth: 
            max_depth: 
            select_domains: 
            select_paths: 
        Returns:
            API response as a dictionary.
        """
        ...

    def tavily_extract_content(
        self,
        urls: List[Any],
        extract_depth: Optional[str] = None,
        format: Optional[str] = None,
        include_favicon: Optional[bool] = None,
        include_images: Optional[bool] = None,
        timeout: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Extracts clean, structured text content from one or more specific URLs using Tavilys extract endpoint. Use this tool when you have a known URL and need to retrieve its readable content — for example, to summarize an article, parse a product page, or feed page text into an LLM. Do not use this tool for discovering URLs (use tavily_search_query or tavily_crawl_content) or for mapping site structure (use tavily_map_content). This tool makes a POST request and incurs API usage costs per URL processed.

        Args:
            urls: List of URLs from which content will be extracted. (required)
            extract_depth: The depth or level of content extraction.
            format: The format to return the extracted content in.
            include_favicon: Whether to include the favicon in the extracted content.
            include_images: Whether to include images in the extracted content.
            timeout: Maximum time to wait for the content to be extracted.
        Returns:
            API response as a dictionary.
        """
        ...

    def tavily_map_content(
        self,
        url: str,
        allow_external: Optional[bool] = None,
        exclude_domains: Optional[List[Any]] = None,
        exclude_paths: Optional[List[Any]] = None,
        instructions: Optional[str] = None,
        limit: Optional[int] = None,
        max_breadth: Optional[int] = None,
        max_depth: Optional[int] = None,
        select_domains: Optional[List[Any]] = None,
        select_paths: Optional[List[Any]] = None,
    ) -> Dict[str, Any]:
        """Maps the URL structure and content hierarchy of a website or set of URLs using Tavilys map endpoint. Use this tool when you need a structured overview of how pages and content relate to each other on a site, such as building a sitemap or understanding content organization before crawling or extracting. Do not use this tool if you want to perform a keyword search (use tavily_search_query) or extract raw text from specific pages (use tavily_extract_content). This tool makes a POST request and may incur API usage costs.

        Args:
            url: Starting URL for content mapping. (required)
            allow_external: Flag indicating whether external domains are allowed in the mapping.
            exclude_domains: List of domain names to exclude from content mapping.
            exclude_paths: List of URL paths to exclude from content mapping.
            instructions: Additional instructions or notes for content mapping.
            limit: Maximum number of content items to process.
            max_breadth: Maximum number of links to follow from each page.
            max_depth: Maximum crawl depth during content mapping.
            select_domains: List of domain names to include when mapping content.
            select_paths: List of URL paths to include in the mapping process.
        Returns:
            API response as a dictionary.
        """
        ...

    def tavily_search_query(
        self,
        query: str,
        auto_parameters: Optional[bool] = None,
        chunks_per_source: Optional[int] = None,
        country: Optional[str] = None,
        days: Optional[int] = None,
        end_date: Optional[str] = None,
        exclude_domains: Optional[List[Any]] = None,
        include_answer: Optional[bool] = None,
        include_domains: Optional[List[Any]] = None,
        include_favicon: Optional[bool] = None,
        include_image_descriptions: Optional[bool] = None,
        include_images: Optional[bool] = None,
        include_raw_content: Optional[bool] = None,
        max_results: Optional[int] = None,
        search_depth: Optional[str] = None,
        start_date: Optional[str] = None,
        time_range: Optional[str] = None,
        topic: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Performs a real-time web search using a natural language or keyword query via Tavilys search endpoint, returning ranked, LLM-optimized results including titles, URLs, and content snippets. Use this tool when you need to find relevant web pages or answer questions that require up-to-date information from the internet. Do not use this tool if you already have a URL and want to extract its content (use tavily_extract_content) or crawl a site (use tavily_crawl_content). This tool makes a POST request and incurs API usage costs per query.

        Args:
            query: The search query string. (required)
            auto_parameters: Automatically determine parameters for the request.
            chunks_per_source: Number of data chunks to retrieve per source.
            country: The country code or name for filtering data.
            days: Number of days to look back.
            end_date: The end date for the data retrieval period.
            exclude_domains: List of domains to exclude from the search.
            include_answer: Whether to include answers in the results.
            include_domains: List of domains to include in the search.
            include_favicon: Whether to include favicons in the results.
            include_image_descriptions: Whether to include descriptions for images.
            include_images: Whether to include images in the results.
            include_raw_content: Whether to include raw content in the results.
            max_results: Maximum number of results to retrieve.
            search_depth: Depth level of search to perform.
            start_date: The start date for the data retrieval period.
            time_range: Time range for querying data.
            topic: Topic or category for the search.
        Returns:
            API response as a dictionary.
        """
        ...

