"""Fastn Fibery connector — auto-generated type stubs.

Do not edit manually. Regenerate with `fastn connector sync`.
"""
from __future__ import annotations

from typing import Any, Dict, List, Optional


class FiberyConnector:
    """Fibery connector ().

    Provides 2 tools.
    """

    def get_file(
        self,
        fileId: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Retrieves a file from the designated cloud storage in the file management connector.

        Args:
            fileId: 
        Returns:
            API response as a dictionary.
        """
        ...

    def upload_file(
        self,
        file: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Uploads a file to the designated cloud storage in the file management connector.

        Args:
            file: 
        Returns:
            API response as a dictionary.
        """
        ...

