"""Fastn Pet store connector — auto-generated type stubs.

Do not edit manually. Regenerate with `fastn connector sync`.
"""
from __future__ import annotations

from typing import Any, Dict, List, Optional


class PetStoreConnector:
    """Pet store connector ().

    Provides 14 tools.
    """

    def create_order(
        self,
        complete: Optional[bool] = None,
        id: Optional[int] = None,
        petId: Optional[int] = None,
        quantity: Optional[int] = None,
        shipDate: Optional[str] = None,
        status: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Creates a new order in the system for a given pet.

        Args:
            complete: 
            id: 
            petId: 
            quantity: 
            shipDate: 
            status: 
        Returns:
            API response as a dictionary.
        """
        ...

    def create_pet(
        self,
        category: Optional[Dict[str, Any]] = None,
        id: Optional[int] = None,
        name: Optional[str] = None,
        photoUrls: Optional[List[Any]] = None,
        status: Optional[str] = None,
        tags: Optional[List[Any]] = None,
    ) -> Dict[str, Any]:
        """Creates a new pet entry in the system.

        Args:
            category: 
            id: 
            name: 
            photoUrls: 
            status: 
            tags: 
        Returns:
            API response as a dictionary.
        """
        ...

    def create_user(
        self,
    ) -> Dict[str, Any]:
        """Registers a new user in the system.
        Returns:
            API response as a dictionary.
        """
        ...

    def delete_order(
        self,
        orderId: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Removes an existing order from the system using its ID.

        Args:
            orderId: 
        Returns:
            API response as a dictionary.
        """
        ...

    def delete_pet(
        self,
        petId: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Deletes a specific pet from the system using its ID.

        Args:
            petId: 
        Returns:
            API response as a dictionary.
        """
        ...

    def delete_user(
        self,
        username: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Deletes a specific user from the system using their ID.

        Args:
            username: 
        Returns:
            API response as a dictionary.
        """
        ...

    def get_inventory(
        self,
    ) -> Dict[str, Any]:
        """Retrieves the inventory of available pets in the system.
        Returns:
            API response as a dictionary.
        """
        ...

    def get_order(
        self,
        orderId: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Retrieves details about a specific order using its ID.

        Args:
            orderId: 
        Returns:
            API response as a dictionary.
        """
        ...

    def get_pet(
        self,
        petId: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Fetches details about a specific pet using its ID.

        Args:
            petId: 
        Returns:
            API response as a dictionary.
        """
        ...

    def get_pet_by_status(
        self,
        status: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Fetches a list of pets based on their current status.

        Args:
            status: 
        Returns:
            API response as a dictionary.
        """
        ...

    def get_user(
        self,
        username: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Retrieves details about a specific user using their ID.

        Args:
            username: 
        Returns:
            API response as a dictionary.
        """
        ...

    def update_pet(
        self,
        category: Optional[Dict[str, Any]] = None,
        id: Optional[int] = None,
        name: Optional[str] = None,
        photoUrls: Optional[List[Any]] = None,
        status: Optional[str] = None,
        tags: Optional[List[Any]] = None,
    ) -> Dict[str, Any]:
        """Updates the details of an existing pet in the system.

        Args:
            category: 
            id: 
            name: 
            photoUrls: 
            status: 
            tags: 
        Returns:
            API response as a dictionary.
        """
        ...

    def update_pet_by_form_data(
        self,
        name: Optional[str] = None,
        status: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Updates pet details using form data submission in the system.

        Args:
            name: 
            status: 
        Returns:
            API response as a dictionary.
        """
        ...

    def update_user(
        self,
        email: Optional[str] = None,
        firstName: Optional[str] = None,
        id: Optional[int] = None,
        lastName: Optional[str] = None,
        password: Optional[str] = None,
        phone: Optional[str] = None,
        userStatus: Optional[int] = None,
        username: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Updates the information of an existing user in the system.

        Args:
            email: 
            firstName: 
            id: 
            lastName: 
            password: 
            phone: 
            userStatus: 
            username: 
        Returns:
            API response as a dictionary.
        """
        ...

