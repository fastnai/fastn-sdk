"""Fastn Microsoft SharePoint connector — auto-generated type stubs.

Do not edit manually. Regenerate with `fastn connector sync`.
"""
from __future__ import annotations

from typing import Any, Dict, List, Optional, TypedDict


class MicrosoftSharepointConnector:
    """Microsoft SharePoint connector ().

    Provides 5 tools.
    """

    def microsoft_share_point_create_file(
        self,
        body: Optional[str] = None,
        fileName: Optional[str] = None,
        path: Optional[str] = None,
        siteId: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Creates or overwrites a file at a specified path within a Microsoft SharePoint sites document library by uploading its content. Use this when you need to add a new file or replace an existing one in a SharePoint site. Requires the site ID, file path, and file name. Do not use this to update only file metadata. This operation will overwrite any existing file at the target path without warning.

        Args:
            body: 
            fileName: 
            path: 
            siteId: 
        Returns:
            API response as a dictionary.
        """
        ...

    def microsoft_share_point_get_data_from_sheet(
        self,
        itemId: Optional[str] = None,
        range: Optional[str] = None,
        workSheetId: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Retrieves cell data from a specified range within a worksheet of an Excel workbook stored in the authenticated users OneDrive via Microsoft SharePoint. Use this when you need to read specific cell values from an Excel spreadsheet by providing the item ID, worksheet ID, and cell range (e.g., A1:C10). Do not use this to list all worksheets in a workbook (use microsoft_share_point_list_worksheets instead) or to retrieve non-Excel file content (use microsoft_share_point_get_file_content instead).

        Args:
            itemId: 
            range: 
            workSheetId: 
        Returns:
            API response as a dictionary.
        """
        ...

    def microsoft_share_point_get_file_content(
        self,
        itemId: Optional[str] = None,
        siteId: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Downloads the raw content of a specific file from a Microsoft SharePoint sites document library by site ID and item ID. Use this when you need to retrieve the binary or text content of a file stored in SharePoint. Do not use this to retrieve file metadata only or to read Excel worksheet data (use microsoft_share_point_get_data_from_sheet instead).

        Args:
            itemId: 
            siteId: 
        Returns:
            API response as a dictionary.
        """
        ...

    def microsoft_share_point_list_sites(
        self,
        search: Optional[str] = None,
        skipToken: Optional[str] = None,
        top: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Lists all Microsoft SharePoint sites accessible to the authenticated user via the Microsoft Graph API. Use this when you need to discover available SharePoint sites and retrieve their site IDs for subsequent operations. Do not use this to list files within a site (use microsoft_share_point_get_file_content or microsoft_share_point_create_file with the appropriate site ID instead).

        Args:
            search: 
            skipToken: 
            top: 
        Returns:
            API response as a dictionary.
        """
        ...

    def microsoft_share_point_list_worksheets(
        self,
        count: Optional[str] = None,
        filter: Optional[str] = None,
        itemId: Optional[str] = None,
        orderby: Optional[str] = None,
        select: Optional[str] = None,
        skip: Optional[str] = None,
        top: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Lists all worksheets within an Excel workbook stored in the authenticated users OneDrive via Microsoft SharePoint, returning each worksheets name and ID. Use this when you need to discover available sheets before reading data from a specific one. Do not use this to retrieve cell data from a sheet (use microsoft_share_point_get_data_from_sheet instead).

        Args:
            count: 
            filter: 
            itemId: 
            orderby: 
            select: 
            skip: 
            top: 
        Returns:
            API response as a dictionary.
        """
        ...

