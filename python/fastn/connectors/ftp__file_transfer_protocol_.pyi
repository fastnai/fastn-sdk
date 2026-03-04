"""Fastn FTP (File Transfer Protocol) connector — auto-generated type stubs.

Do not edit manually. Regenerate with `fastn connector sync`.
"""
from __future__ import annotations

from typing import Any, Dict, List, Optional, TypedDict


class FtpFileTransferProtocolConnector:
    """FTP (File Transfer Protocol) connector ().

    Provides 1 tools.
    """

    def file_transport_protocol_test_connection(
        self,
    ) -> Dict[str, Any]:
        """Tests the FTP connector connection to verify that credentials and network connectivity are correctly configured. Use this tool to validate the FTP setup before executing file transfer operations. Do not use this tool to transfer, list, or manage files — it performs no file operations and has no side effects beyond checking connectivity.
        Returns:
            API response as a dictionary.
        """
        ...

