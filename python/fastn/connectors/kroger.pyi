"""Fastn Kroger connector — auto-generated type stubs.

Do not edit manually. Regenerate with `fastn connector sync`.
"""
from __future__ import annotations

from typing import Any, Dict, List, Optional


class KrogerConnector:
    """Kroger connector ().

    Provides 1 tools.
    """

    def get_product(
        self,
    ) -> Dict[str, Any]:
        """Retrieves product information from the specified e-commerce connector.
        Returns:
            API response as a dictionary.
        """
        ...

