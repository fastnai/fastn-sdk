"""Fastn HP Workforce Experience connector — auto-generated type stubs.

Do not edit manually. Regenerate with `fastn connector sync`.
"""
from __future__ import annotations

from typing import Any, Dict, List, Optional


class HpWorkforceExperienceConnector:
    """HP Workforce Experience connector ().

    Provides 3 tools.
    """

    def get_collumns_metadata(
        self,
        tablename: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Fetches the metadata for columns within the specified connector, detailing the structure, data types, and properties of each column in the dataset.

        Args:
            tablename: 
        Returns:
            API response as a dictionary.
        """
        ...

    def get_insights_data(
        self,
        query: Optional[str] = None,
        tenantDetails: Optional[List[Any]] = None,
    ) -> Dict[str, Any]:
        """Obtains insights data using the specified connector, allowing for the extraction of detailed analytical data for further processing or visualization.

        Args:
            query: 
            tenantDetails: 
        Returns:
            API response as a dictionary.
        """
        ...

    def get_insights_table(
        self,
    ) -> Dict[str, Any]:
        """Retrieves the insights table within the specified connector, providing an overview of key metrics and data points relevant to the analysis.
        Returns:
            API response as a dictionary.
        """
        ...

