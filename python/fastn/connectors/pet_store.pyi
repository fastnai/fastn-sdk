"""Fastn Pet store connector — auto-generated type stubs.

Do not edit manually. Regenerate with `fastn connector sync`.
"""
from __future__ import annotations

from typing import Any, Dict, List, Optional, TypedDict


class _PetStoreCreatePetCategory(TypedDict, total=False):
    id: int
    name: str

class _PetStoreUpdatePetCategory(TypedDict, total=False):
    id: int
    name: str

class PetStoreConnector:
    """Pet store connector ().

    Provides 14 tools.
    """

    def pet_store_create_order(
        self,
        complete: Optional[bool] = None,
        id: Optional[int] = None,
        petId: Optional[int] = None,
        quantity: Optional[int] = None,
        shipDate: Optional[str] = None,
        status: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Creates a new purchase order in the Pet Store system for a specified pet, including quantity and shipment details. Use this to place a new order for a pet in the store inventory. Do not use this to update or delete an existing order — use pet_store_delete_order for removal.

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

    def pet_store_create_pet(
        self,
        category: Optional[_PetStoreCreatePetCategory] = None,
        id: Optional[int] = None,
        name: Optional[str] = None,
        photoUrls: Optional[List[Any]] = None,
        status: Optional[str] = None,
        tags: Optional[List[Any]] = None,
    ) -> Dict[str, Any]:
        """Creates a new pet entry in the Pet Store system with the provided details such as name, category, status, and photo URLs. Use this to add a new pet to the stores inventory. Do not use this to update an existing pet — use pet_store_update_pet instead.

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

    def pet_store_create_user(
        self,
        body: Optional[List[Any]] = None,
    ) -> Dict[str, Any]:
        """Registers one or more new users in the Pet Store system by submitting a list of user objects, including username, email, and password. Use this to batch-create user accounts. Do not use this to update an existing user — use pet_store_update_user instead.

        Args:
            body: 
        Returns:
            API response as a dictionary.
        """
        ...

    def pet_store_delete_order(
        self,
        orderId: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Permanently removes a specific order from the Pet Store system identified by its order ID. Use this to cancel and delete an order that should no longer exist in the system. This action is irreversible — the order cannot be recovered after deletion. Do not use this to update an orders status; use the appropriate update tool instead.

        Args:
            orderId: 
        Returns:
            API response as a dictionary.
        """
        ...

    def pet_store_delete_pet(
        self,
        petId: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Permanently deletes a specific pet record from the Pet Store system identified by its pet ID. Use this to remove a pet listing that is no longer available or relevant. This action is irreversible — the pet record cannot be recovered after deletion. Do not use this to update pet details; use pet_store_update_pet instead.

        Args:
            petId: 
        Returns:
            API response as a dictionary.
        """
        ...

    def pet_store_delete_user(
        self,
        username: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Permanently deletes a specific user from the Pet Store system identified by their username. Use this to remove a user account that is no longer needed. This action is irreversible — the user record cannot be recovered after deletion. Do not use this to update or deactivate a user; use pet_store_update_user instead.

        Args:
            username: 
        Returns:
            API response as a dictionary.
        """
        ...

    def pet_store_get_inventory(
        self,
    ) -> Dict[str, Any]:
        """Retrieves the current inventory of the Pet Store, returning a map of pet status labels to their respective counts (e.g., available, pending, sold). Use this to get an aggregate overview of stock levels across all pet statuses. Do not use this to retrieve details about individual pets — use pet_store_get_pet or pet_store_list_pets_by_status instead.
        Returns:
            API response as a dictionary.
        """
        ...

    def pet_store_get_order(
        self,
        orderId: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Retrieves the details of a specific order in the Pet Store system identified by its order ID, including pet ID, quantity, status, and shipment date. Use this to look up a single orders information. Do not use this to list all orders; this tool fetches a single order by ID only.

        Args:
            orderId: 
        Returns:
            API response as a dictionary.
        """
        ...

    def pet_store_get_pet(
        self,
        petId: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Retrieves the full details of a specific pet in the Pet Store system identified by its pet ID, including name, category, status, and photo URLs. Use this to look up a single pet record. Do not use this to list multiple pets — use pet_store_list_pets_by_status to filter pets by status.

        Args:
            petId: 
        Returns:
            API response as a dictionary.
        """
        ...

    def pet_store_get_user(
        self,
        username: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Retrieves profile details for a specific user in the Pet Store system identified by their username, including name, email, and account status. Use this to look up a single users information. Do not use this to list all users; this tool fetches a single user by username only.

        Args:
            username: 
        Returns:
            API response as a dictionary.
        """
        ...

    def pet_store_list_pets_by_status(
        self,
        status: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Retrieves a list of pets from the Pet Store system filtered by their current status, such as available, pending, or sold. Use this to browse or filter the pet inventory by availability status. Do not use this to retrieve a single pet by ID — use pet_store_get_pet instead.

        Args:
            status: 
        Returns:
            API response as a dictionary.
        """
        ...

    def pet_store_update_pet(
        self,
        category: Optional[_PetStoreUpdatePetCategory] = None,
        id: Optional[int] = None,
        name: Optional[str] = None,
        photoUrls: Optional[List[Any]] = None,
        status: Optional[str] = None,
        tags: Optional[List[Any]] = None,
    ) -> Dict[str, Any]:
        """Updates the details of an existing pet in the Pet Store system using a full JSON request body, such as name, status, or category. Use this to modify an existing pets complete record. Do not use this to create a new pet — use pet_store_create_pet instead. For form-data updates, use pet_store_update_pet_by_form_data.

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

    def pet_store_update_pet_by_form_data(
        self,
        name: Optional[str] = None,
        petId: Optional[str] = None,
        status: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Updates the details of an existing pet in the Pet Store system using form-encoded data, identified by the pets ID. Use this when updating pet information via a multipart form submission, such as name or status fields. Do not use this for full JSON-body updates — use pet_store_update_pet instead.

        Args:
            name: 
            petId: 
            status: 
        Returns:
            API response as a dictionary.
        """
        ...

    def pet_store_update_user(
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
        """Updates the profile information of an existing user in the Pet Store system identified by their username. Use this to modify user details such as name, email, or password. Do not use this to create a new user — use pet_store_create_user instead.

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

