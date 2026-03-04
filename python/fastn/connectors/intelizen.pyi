"""Fastn Intelizen connector — auto-generated type stubs.

Do not edit manually. Regenerate with `fastn connector sync`.
"""
from __future__ import annotations

from typing import Any, Dict, List, Optional, TypedDict


class IntelizenConnector:
    """Intelizen connector ().

    Provides 4 tools.
    """

    def intelizen_create_contract(
        self,
        file: str,
        type: str,
    ) -> Dict[str, Any]:
        """Creates a new contract in the Intelizen system with specified parameters. Use this tool when you need to define and register a new contract. This tool does not update or replace existing contracts — use a dedicated update endpoint for modifications. Note: this action is irreversible; once created, the contract is committed to the system and cannot be automatically rolled back.

        Args:
            file: File to be processed. (required)
            type: Type of file or operation. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def intelizen_get_contract(
        self,
        contractId: str,
    ) -> Dict[str, Any]:
        """Retrieves the full details of a single contract from the Intelizen system by its unique contract ID. Use this tool when you need complete information about a specific contract. Requires a valid contractId; use intelizen_list_contracts first if you need to discover available contract IDs. This is a read-only operation with no side effects.

        Args:
            contractId: ID of the contract. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def intelizen_list_contracts(
        self,
    ) -> Dict[str, Any]:
        """Retrieves a list of all contracts available in the Intelizen system. Use this tool when you need an overview of all contracts, such as for display, filtering, or bulk processing. For details about a single specific contract, use intelizen_get_contract instead. This is a read-only operation with no side effects.
        Returns:
            API response as a dictionary.
        """
        ...

    def intelizen_upload_file_deprecated(
        self,
        file: str,
        type: str,
    ) -> Dict[str, Any]:
        """DEPRECATED. Previously used to upload a file to the Intelizen contracts endpoint. Do not use this tool in new workflows; it is retained only for legacy compatibility. Use intelizen_create_contract instead for all file upload and contract creation operations. Calling this tool may result in unexpected behavior or future breakage.

        Args:
            file: File to be processed by the Intelizen API. (required)
            type: Type of file or operation for the Intelizen API. (required)
        Returns:
            API response as a dictionary.
        """
        ...

