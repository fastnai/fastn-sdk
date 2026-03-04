"""Fastn Kroger connector — auto-generated type stubs.

Do not edit manually. Regenerate with `fastn connector sync`.
"""
from __future__ import annotations

from typing import Any, Dict, List, Optional, TypedDict


class KrogerConnector:
    """Kroger connector ().

    Provides 1 tools.
    """

    def kroger_get_product(
        self,
        product_id: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Retrieves detailed product information from the Kroger catalog by GTIN-13 product identifier. Use this tool when you need to look up product attributes, item details, offer pricing, or variant groupings for a specific Kroger product. Do NOT use this tool to search products by keyword or category — this lookup requires a known GTIN-13 identifier. This is a read-only operation with no side effects.

        Args:
            product_id: Unique identifier for the product within the Kroger system.
        Returns:
            API response as a dictionary.
        """
        ...

