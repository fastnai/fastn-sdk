"""Fastn DonorPerfect connector — auto-generated type stubs.

Do not edit manually. Regenerate with `fastn connector sync`.
"""
from __future__ import annotations

from typing import Any, Dict, List, Optional


class DonorperfectConnector:
    """DonorPerfect connector ().

    Provides 10 tools.
    """

    def create_contact(
        self,
        params: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Creates a new contact in the system using the createContact tool.

        Args:
            params: Specific parameters for the DonorPerfect API call.
        Returns:
            API response as a dictionary.
        """
        ...

    def create_donor(
        self,
        params: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Adds a new donor to the database utilizing the createDonor tool.

        Args:
            params: String containing parameters for the DonorPerfect API request.
        Returns:
            API response as a dictionary.
        """
        ...

    def delete_donor_flag(
        self,
        params: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Removes a specific flag from a donor's profile with the deleteDonorFlag tool.

        Args:
            params: Additional parameters for the DonorPerfect API request.
        Returns:
            API response as a dictionary.
        """
        ...

    def delete_flags(
        self,
        params: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Deletes multiple flags from the system using the deleteFlags tool.

        Args:
            params: String containing parameters for the DonorPerfect API call.
        Returns:
            API response as a dictionary.
        """
        ...

    def get_donor(
        self,
        donor_id: str,
    ) -> Dict[str, Any]:
        """Fetches the specific details of a donor using their unique identifier with the getDonor tool.

        Args:
            donor_id: The ID of the donor. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def get_donor_by_email(
        self,
        email: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Obtains donor information based on their email address with the getDonorByEmail tool.

        Args:
            email: 
        Returns:
            API response as a dictionary.
        """
        ...

    def get_donors(
        self,
    ) -> Dict[str, Any]:
        """Retrieves a list of donors from the database through the getDonors tool.
        Returns:
            API response as a dictionary.
        """
        ...

    def save_address(
        self,
        params: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Saves a new address for a contact using the saveAddress tool.

        Args:
            params: Additional parameters for the DonorPerfect API request.
        Returns:
            API response as a dictionary.
        """
        ...

    def save_flags(
        self,
        params: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Applies flags to a donor’s profile with the saveFlags tool.

        Args:
            params: Additional parameters for the DonorPerfect API request.
        Returns:
            API response as a dictionary.
        """
        ...

    def update_donor(
        self,
        params: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Updates the details of an existing donor in the system with the updateDonor tool.

        Args:
            params: String containing parameters for the DonorPerfect API call.
        Returns:
            API response as a dictionary.
        """
        ...

