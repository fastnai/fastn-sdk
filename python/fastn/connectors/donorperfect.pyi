"""Fastn DonorPerfect connector — auto-generated type stubs.

Do not edit manually. Regenerate with `fastn connector sync`.
"""
from __future__ import annotations

from typing import Any, Dict, List, Optional, TypedDict


class DonorperfectConnector:
    """DonorPerfect connector ().

    Provides 10 tools.
    """

    def donorperfect_create_contact(
        self,
        params: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Creates a new contact record in DonorPerfect. Use this tool to add a non-donor contact, such as a staff member, volunteer, or organization representative, to the system. Do not use this tool to add a donor — use donorperfect_create_donor for that. This action creates a permanent contact record in the database.

        Args:
            params: Specific parameters for the DonorPerfect API call.
        Returns:
            API response as a dictionary.
        """
        ...

    def donorperfect_create_donor(
        self,
        params: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Creates a new donor record in DonorPerfect. Use this tool when onboarding a new donor who does not yet exist in the system. Do not use this tool to update an existing donor — use donorperfect_update_donor for that. This action creates a permanent donor record in the database.

        Args:
            params: String containing parameters for the DonorPerfect API request.
        Returns:
            API response as a dictionary.
        """
        ...

    def donorperfect_delete_donor_flag(
        self,
        params: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Removes a specific flag from a single donors profile in DonorPerfect. Use this tool when you need to untag or declassify a donor from a particular flag category. Do not use this tool to remove multiple flags in bulk — use donorperfect_delete_flags for that. This action is irreversible.

        Args:
            params: Additional parameters for the DonorPerfect API request.
        Returns:
            API response as a dictionary.
        """
        ...

    def donorperfect_delete_flags(
        self,
        params: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Deletes multiple flags from DonorPerfect in a single operation. Use this tool when you need to bulk-remove flag definitions or flag assignments from the system. Do not use this tool to remove a single flag from one specific donor — use donorperfect_delete_donor_flag for that. This action is irreversible.

        Args:
            params: String containing parameters for the DonorPerfect API call.
        Returns:
            API response as a dictionary.
        """
        ...

    def donorperfect_get_donor(
        self,
        donor_id: str,
    ) -> Dict[str, Any]:
        """Retrieves the full profile details of a specific donor from DonorPerfect using their unique donor ID. Use this tool when you have a known donor ID and need to fetch their complete record. Do not use this tool if you only have an email address — use donorperfect_get_donor_by_email instead.

        Args:
            donor_id: The ID of the donor. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def donorperfect_get_donor_by_email(
        self,
        email: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Retrieves a donors profile from DonorPerfect using their email address. Use this tool when you have a donors email and need to look up their record, ID, or contact details. Do not use this tool if you already have the donors unique ID — use donorperfect_get_donor instead. Returns a single matching donor record if found.

        Args:
            email: 
        Returns:
            API response as a dictionary.
        """
        ...

    def donorperfect_list_donors(
        self,
    ) -> Dict[str, Any]:
        """Retrieves a list of donors from the DonorPerfect database. Use this tool to get a broad set of donor records, for example to audit, export, or process multiple donors at once. Do not use this tool if you need a single donor by ID or email — use donorperfect_get_donor or donorperfect_get_donor_by_email instead.
        Returns:
            API response as a dictionary.
        """
        ...

    def donorperfect_save_address(
        self,
        params: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Saves a new or updated mailing address for a contact in DonorPerfect. Use this tool to add or overwrite address information associated with a contact record. Do not use this tool to update other donor profile fields — use donorperfect_update_donor for that.

        Args:
            params: Additional parameters for the DonorPerfect API request.
        Returns:
            API response as a dictionary.
        """
        ...

    def donorperfect_save_flags(
        self,
        params: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Applies one or more flags to a donors profile in DonorPerfect. Use this tool to tag a donor with classification or segmentation flags for reporting or workflow purposes. Do not use this tool to remove flags — use donorperfect_delete_donor_flag or donorperfect_delete_flags for that.

        Args:
            params: Additional parameters for the DonorPerfect API request.
        Returns:
            API response as a dictionary.
        """
        ...

    def donorperfect_update_donor(
        self,
        params: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Updates the profile details of an existing donor in DonorPerfect. Use this tool to modify fields such as name, contact information, or other donor attributes for an existing record identified by donor ID. Do not use this tool to create a new donor — use donorperfect_create_donor for that. This action overwrites the specified fields on the donor record.

        Args:
            params: String containing parameters for the DonorPerfect API call.
        Returns:
            API response as a dictionary.
        """
        ...

