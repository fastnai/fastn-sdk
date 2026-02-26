"""Fastn Microsoft SharePoint connector — auto-generated type stubs.

Do not edit manually. Regenerate with `fastn connector sync`.
"""
from __future__ import annotations

from typing import Any, Dict, List, Optional


class MicrosoftSharepointConnector:
    """Microsoft SharePoint connector ().

    Provides 5 tools.
    """

    def create_file(
        self,
    ) -> Dict[str, Any]:
        """Creates a new file in the designated connector's storage system.
        Returns:
            API response as a dictionary.
        """
        ...

    def get_data_from_sheet(
        self,
        itemId: Optional[str] = None,
        range: Optional[str] = None,
        workSheetId: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Extracts data from a specified sheet within a workbook using the connector.

        Args:
            itemId: 
            range: 
            workSheetId: 
        Returns:
            API response as a dictionary.
        """
        ...

    def get_file_content(
        self,
        itemId: Optional[str] = None,
        siteId: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Fetches the content of a specific file from the connector's storage.

        Args:
            itemId: 
            siteId: 
        Returns:
            API response as a dictionary.
        """
        ...

    def get_sites(
        self,
        search: Optional[str] = None,
        skipToken: Optional[str] = None,
        top: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Retrieves a list of sites from the specified connector.

        Args:
            search: 
            skipToken: 
            top: 
        Returns:
            API response as a dictionary.
        """
        ...

    def get_worksheets(
        self,
        count: Optional[str] = None,
        filter: Optional[str] = None,
        orderby: Optional[str] = None,
        select: Optional[str] = None,
        skip: Optional[str] = None,
        top: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Lists all worksheets available in a spreadsheet managed by the connector.

        Args:
            count: 
            filter: 
            orderby: 
            select: 
            skip: 
            top: 
        Returns:
            API response as a dictionary.
        """
        ...

