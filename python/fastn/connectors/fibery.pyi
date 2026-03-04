"""Fastn Fibery connector — auto-generated type stubs.

Do not edit manually. Regenerate with `fastn connector sync`.
"""
from __future__ import annotations

from typing import Any, Dict, List, Optional, TypedDict


class FiberyConnector:
    """Fibery connector ().

    Provides 2 tools.
    """

    def fibery_get_file(
        self,
        fileId: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Downloads or retrieves a specific file stored in the Fibery workspace, identified by its file ID. Use this tool when you need to access the binary content or metadata of a file previously uploaded to Fibery. Do not use this tool to upload new files or to list all available files.

        Args:
            fileId: 
        Returns:
            API response as a dictionary.
        """
        ...

    def fibery_upload_file(
        self,
        file: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Uploads a new file to the Fibery workspace file storage. Use this tool when you need to attach or store a file within Fibery for later reference or linkage to workspace entities. This action creates a new file record and returns a file ID that can be used in subsequent operations. Do not use this tool to retrieve or update an existing file.

        Args:
            file: 
        Returns:
            API response as a dictionary.
        """
        ...

