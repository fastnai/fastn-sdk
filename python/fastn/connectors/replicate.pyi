"""Fastn Replicate connector — auto-generated type stubs.

Do not edit manually. Regenerate with `fastn connector sync`.
"""
from __future__ import annotations

from typing import Any, Dict, List, Optional


class ReplicateConnector:
    """Replicate connector ().

    Provides 12 tools.
    """

    def get_account(
        self,
    ) -> Dict[str, Any]:
        """Retrieves the account information for the user in the specified connector.
        Returns:
            API response as a dictionary.
        """
        ...

    def get_collection_of_models(
        self,
        collectionSlug: str,
    ) -> Dict[str, Any]:
        """Fetches details of a specific collection of models in the specified connector.

        Args:
            collectionSlug: Slug of the collection for the Replicate Replicate API. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def get_default_webhook_secret(
        self,
    ) -> Dict[str, Any]:
        """Retrieves the default webhook secret used for integrations in the specified connector.
        Returns:
            API response as a dictionary.
        """
        ...

    def get_model(
        self,
        modelName: str,
        modelOwner: str,
    ) -> Dict[str, Any]:
        """Retrieves details of a specific model in the connector.

        Args:
            modelName: The name of the model in the Replicate API. (required)
            modelOwner: The owner of the model in the Replicate API. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def get_model_version(
        self,
        modelName: str,
        modelOwner: str,
        versionId: str,
    ) -> Dict[str, Any]:
        """Fetches details of a specific model version in the specified connector.

        Args:
            modelName: The name of the model. (required)
            modelOwner: The owner of the model. (required)
            versionId: The ID of the model version. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def list_collections_of_models(
        self,
    ) -> Dict[str, Any]:
        """Lists all collections associated with models in the given connector.
        Returns:
            API response as a dictionary.
        """
        ...

    def list_deployments(
        self,
    ) -> Dict[str, Any]:
        """Lists all deployments currently active in the specified connector.
        Returns:
            API response as a dictionary.
        """
        ...

    def list_hardware_for_models(
        self,
    ) -> Dict[str, Any]:
        """Enumerates all hardware associated with the specified models in the connector.
        Returns:
            API response as a dictionary.
        """
        ...

    def list_model_versions(
        self,
        modelName: str,
        modelOwner: str,
    ) -> Dict[str, Any]:
        """Lists all versions of a model within the connector.

        Args:
            modelName: Name of the model in the Replicate API. (required)
            modelOwner: Owner of the model in the Replicate API. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def list_predictions(
        self,
    ) -> Dict[str, Any]:
        """Lists all predictions made within the context of the specified connector.
        Returns:
            API response as a dictionary.
        """
        ...

    def list_public_models(
        self,
    ) -> Dict[str, Any]:
        """Lists all public models available in the specified connector.
        Returns:
            API response as a dictionary.
        """
        ...

    def list_trainings(
        self,
    ) -> Dict[str, Any]:
        """Enumerates all training sessions conducted within the connector.
        Returns:
            API response as a dictionary.
        """
        ...

