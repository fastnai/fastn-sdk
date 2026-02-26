"""Fastn Intelizen connector — auto-generated type stubs.

Do not edit manually. Regenerate with `fastn connector sync`.
"""
from __future__ import annotations

from typing import Any, Dict, List, Optional


class IntelizenConnector:
    """Intelizen connector ().

    Provides 4 tools.
    """

    def create_contract(
        self,
        file: str,
        type: str,
    ) -> Dict[str, Any]:
        """Creates a new contract using the createContract connector. This tool allows for the definition of a new contract in the system with specified parameters.

        Args:
            file: File to be processed. (required)
            type: Type of file or operation. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def get_contract(
        self,
        contractId: str,
    ) -> Dict[str, Any]:
        """Retrieves a specific contract using the getContract connector. This tool requires the contract ID to fetch the details of the specified contract.

        Args:
            contractId: ID of the contract. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def get_contracts(
        self,
    ) -> Dict[str, Any]:
        """Fetches a list of contracts using the getContracts connector. This tool provides an overview of all contracts available in the system.
        Returns:
            API response as a dictionary.
        """
        ...

    def upload_file___deprecated__(
        self,
        file: str,
        type: str,
    ) -> Dict[str, Any]:
        """Uploads a file using the uploadFile (deprecated) connector. Note that this tool is deprecated and should be avoided in favor of updated methods.

        Args:
            file: File to be processed by the Intelizen API. (required)
            type: Type of file or operation for the Intelizen API. (required)
        Returns:
            API response as a dictionary.
        """
        ...

