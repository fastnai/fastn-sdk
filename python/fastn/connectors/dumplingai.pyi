"""Fastn DumplingAI connector — auto-generated type stubs.

Do not edit manually. Regenerate with `fastn connector sync`.
"""
from __future__ import annotations

from typing import Any, Dict, List, Optional, TypedDict


class DumplingaiConnector:
    """DumplingAI connector ().

    Provides 6 tools.
    """

    def dumplingai_crawl_website(
        self,
        url: str,
        depth: Optional[int] = None,
        format: Optional[str] = None,
        limit: Optional[int] = None,
    ) -> Dict[str, Any]:
        """Crawls a specified website URL and extracts its text content, links, and structured data for research or analysis purposes. Use this tool when you need to gather content from an entire website or a set of its pages. Do not use this tool for single-page content extraction where a targeted fetch would suffice, and note that crawling large sites may take significant time and return large volumes of data.

        Args:
            url: URL for the request. (required)
            depth: Depth of the request.
            format: Format of the response.
            limit: Limit of the request.
        Returns:
            API response as a dictionary.
        """
        ...

    def dumplingai_get_youtube_video_transcript(
        self,
        videoUrl: str,
        includeTimestamps: Optional[bool] = None,
        preferredLanguage: Optional[str] = None,
        timestampsToCombine: Optional[int] = None,
    ) -> Dict[str, Any]:
        """Retrieves the full text transcript of a specified YouTube video by its URL or video ID. Use this tool when you need to analyze, summarize, or search the spoken content of a YouTube video without watching it. Do not use this tool if the video does not have captions or a transcript available, as no content will be returned in that case.

        Args:
            videoUrl: URL of the video to be processed. (required)
            includeTimestamps: Whether to include timestamps in the output.
            preferredLanguage: Preferred language for processing.
            timestampsToCombine: Number of timestamps to combine.
        Returns:
            API response as a dictionary.
        """
        ...

    def dumplingai_run_js_code(
        self,
        code: str,
        commands: Optional[str] = None,
        parseJson: Optional[bool] = None,
    ) -> Dict[str, Any]:
        """Executes a provided JavaScript code snippet in a sandboxed server-side environment and returns the output or result. Use this tool when you need to dynamically compute values, transform data, or test JavaScript logic without a local runtime. Be aware that this tool runs arbitrary code on a remote server — only submit trusted code. Do not use this tool for Python or other non-JavaScript execution.

        Args:
            code: Code to be executed. (required)
            commands: Commands to be executed.
            parseJson: Indicates whether the response should be parsed as JSON.
        Returns:
            API response as a dictionary.
        """
        ...

    def dumplingai_search(
        self,
        query: str,
    ) -> Dict[str, Any]:
        """Performs a general web search query and returns relevant results from across the internet based on input keywords or phrases. Use this tool for broad information retrieval when results are not constrained to news or geographic locations. Do not use this tool for news-specific queries — use dumplingai_search_news instead, or for location-based queries — use dumplingai_search_maps instead.

        Args:
            query: The query string for the request. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def dumplingai_search_maps(
        self,
        query: str,
        language: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Performs a location-based search to find places, businesses, or points of interest matching specified criteria such as name, category, or address. Use this tool when the query has a geographic or place-finding intent. Do not use this tool for general web or news searches — use dumplingai_search or dumplingai_search_news instead.

        Args:
            query: The search query. (required)
            language: The language of the query.
        Returns:
            API response as a dictionary.
        """
        ...

    def dumplingai_search_news(
        self,
        query: str,
        country: Optional[str] = None,
        language: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Searches for recent news articles across multiple sources matching specified topics, keywords, or phrases. Use this tool when you need up-to-date news coverage on a subject. Do not use this tool for general web searches — use dumplingai_search instead, or for location-based queries — use dumplingai_search_maps instead.

        Args:
            query: Search query for the DumplingAI API. (required)
            country: Country code related to the DumplingAI request.
            language: Language code for the DumplingAI request.
        Returns:
            API response as a dictionary.
        """
        ...

