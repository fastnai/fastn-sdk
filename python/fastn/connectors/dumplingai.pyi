"""Fastn DumplingAI connector — auto-generated type stubs.

Do not edit manually. Regenerate with `fastn connector sync`.
"""
from __future__ import annotations

from typing import Any, Dict, List, Optional


class DumplingaiConnector:
    """DumplingAI connector ().

    Provides 6 tools.
    """

    def crawl_website(
        self,
        url: str,
        depth: Optional[int] = None,
        format: Optional[str] = None,
        limit: Optional[int] = None,
    ) -> Dict[str, Any]:
        """Crawls a specified website to gather data and extract information relevant to your research or analysis.

        Args:
            url: URL for the request. (required)
            depth: Depth of the request.
            format: Format of the response.
            limit: Limit of the request.
        Returns:
            API response as a dictionary.
        """
        ...

    def get_youtube_video_transcript(
        self,
        videoUrl: str,
        includeTimestamps: Optional[bool] = None,
        preferredLanguage: Optional[str] = None,
        timestampsToCombine: Optional[int] = None,
    ) -> Dict[str, Any]:
        """Retrieves the transcript of a specified YouTube video for text-based review and analysis.

        Args:
            videoUrl: URL of the video to be processed. (required)
            includeTimestamps: Whether to include timestamps in the output.
            preferredLanguage: Preferred language for processing.
            timestampsToCombine: Number of timestamps to combine.
        Returns:
            API response as a dictionary.
        """
        ...

    def run_js_code(
        self,
        code: str,
        commands: Optional[str] = None,
        parseJson: Optional[bool] = None,
    ) -> Dict[str, Any]:
        """Executes custom JavaScript code within a safe environment, allowing for dynamic script testing and debugging.

        Args:
            code: Code to be executed. (required)
            commands: Commands to be executed.
            parseJson: Indicates whether the response should be parsed as JSON.
        Returns:
            API response as a dictionary.
        """
        ...

    def search(
        self,
        query: str,
    ) -> Dict[str, Any]:
        """Performs a search query across various databases or platforms to retrieve relevant information or results based on the input keywords.

        Args:
            query: The query string for the request. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def search_maps(
        self,
        query: str,
        language: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Conducts a location-based search on maps to find places, businesses, or points of interest based on specified criteria.

        Args:
            query: The search query. (required)
            language: The language of the query.
        Returns:
            API response as a dictionary.
        """
        ...

    def search_news(
        self,
        query: str,
        country: Optional[str] = None,
        language: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Searches for the latest news articles across different sources to provide updates on current events that match specific topics or keywords.

        Args:
            query: Search query for the DumplingAI API. (required)
            country: Country code related to the DumplingAI request.
            language: Language code for the DumplingAI request.
        Returns:
            API response as a dictionary.
        """
        ...

