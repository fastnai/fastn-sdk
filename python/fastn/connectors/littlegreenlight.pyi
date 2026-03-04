"""Fastn LittleGreenLight connector — auto-generated type stubs.

Do not edit manually. Regenerate with `fastn connector sync`.
"""
from __future__ import annotations

from typing import Any, Dict, List, Optional, TypedDict


class LittlegreenlightConnector:
    """LittleGreenLight connector ().

    Provides 1 tools.
    """

    def littlegreenlight_push_civic_champ_data(
        self,
        body: Dict[str, Any],
    ) -> Dict[str, Any]:
        """Pushes donor or constituent data from an external Civic Champ integration into LittleGreenLight. Use this when you need to sync or import records from Civic Champ into the LittleGreenLight CRM. This action creates or updates records in LittleGreenLight and may overwrite existing data. Do not use this for general data exports or for integrations other than Civic Champ.

        Args:
            body: Body parameters for the LittleGreenLight LittleGreenLight endpoint. (required)
        Returns:
            API response as a dictionary.
        """
        ...

