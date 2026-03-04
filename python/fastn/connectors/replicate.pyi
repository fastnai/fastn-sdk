"""Fastn Replicate connector — auto-generated type stubs.

Do not edit manually. Regenerate with `fastn connector sync`.
"""
from __future__ import annotations

from typing import Any, Dict, List, Optional, TypedDict


class ReplicateConnector:
    """Replicate connector ().

    Provides 12 tools.
    """

    def replicate_get_account(
        self,
    ) -> Dict[str, Any]:
        """Retrieves profile and account information for the authenticated Replicate user, including username, account type, and associated metadata. Use this to verify the current authenticated identity or display account details. Do not use this to list predictions, models, or deployments — use the appropriate list tools for those resources.
        Returns:
            API response as a dictionary.
        """
        ...

    def replicate_get_default_webhook_secret(
        self,
    ) -> Dict[str, Any]:
        """Retrieves the default webhook signing secret from Replicate, used to verify the authenticity of incoming webhook payloads. Use this when you need to validate webhook requests sent by Replicate to your endpoint. Do not use this to manage or rotate secrets — this tool only reads the current default secret.
        Returns:
            API response as a dictionary.
        """
        ...

    def replicate_get_model(
        self,
        modelName: str,
        modelOwner: str,
    ) -> Dict[str, Any]:
        """Retrieves metadata and configuration details for a specific Replicate model, identified by its owner and model name. Use this to inspect a models description, visibility, latest version, and other properties. Do not use this to list all public models or to retrieve a specific model version — use replicate_list_public_models or replicate_get_model_version instead.

        Args:
            modelName: The name of the model in the Replicate API. (required)
            modelOwner: The owner of the model in the Replicate API. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def replicate_get_model_collection(
        self,
        collectionSlug: str,
    ) -> Dict[str, Any]:
        """Retrieves details of a specific curated model collection on Replicate, identified by its collection slug. Use this to explore the models grouped under a named collection. Do not use this to list all available collections — use replicate_list_model_collections instead.

        Args:
            collectionSlug: Slug of the collection for the Replicate Replicate API. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def replicate_get_model_version(
        self,
        modelName: str,
        modelOwner: str,
        versionId: str,
    ) -> Dict[str, Any]:
        """Retrieves detailed information about a specific version of a Replicate model, identified by the model owner, model name, and version ID. Use this when you need version-specific metadata such as input/output schema or the versions creation date. Do not use this to list all versions of a model — use replicate_list_model_versions instead.

        Args:
            modelName: The name of the model. (required)
            modelOwner: The owner of the model. (required)
            versionId: The ID of the model version. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def replicate_list_deployments(
        self,
    ) -> Dict[str, Any]:
        """Returns a paginated list of all model deployments configured under the authenticated Replicate account. Use this to review available deployments or check deployment status. Do not use this to create a new deployment or manage a specific deployment — use the appropriate create or update deployment tools instead.
        Returns:
            API response as a dictionary.
        """
        ...

    def replicate_list_hardware(
        self,
    ) -> Dict[str, Any]:
        """Returns a list of available hardware options (e.g., GPU types) that can be used when running model predictions on Replicate. Use this to determine valid hardware values before creating or configuring a deployment or prediction. Do not use this to retrieve hardware details for a specific model or deployment.
        Returns:
            API response as a dictionary.
        """
        ...

    def replicate_list_model_collections(
        self,
    ) -> Dict[str, Any]:
        """Returns a paginated list of all curated model collections available on the Replicate platform. Use this to browse high-level collection categories before drilling into a specific collection. Do not use this to retrieve models within a specific collection — use replicate_get_model_collection with the relevant collection slug instead.
        Returns:
            API response as a dictionary.
        """
        ...

    def replicate_list_model_versions(
        self,
        modelName: str,
        modelOwner: str,
    ) -> Dict[str, Any]:
        """Returns a paginated list of all available versions for a specific Replicate model, identified by its owner and name. Use this to discover available versions before running a prediction or to compare version histories. Do not use this to retrieve details of a single specific version — use replicate_get_model_version instead.

        Args:
            modelName: Name of the model in the Replicate API. (required)
            modelOwner: Owner of the model in the Replicate API. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def replicate_list_predictions(
        self,
    ) -> Dict[str, Any]:
        """Returns a paginated list of all predictions previously created on Replicate under the authenticated account. Use this to audit, monitor, or review past prediction runs. Do not use this to create a new prediction or retrieve the result of a single specific prediction — use the appropriate get or create prediction tools instead.
        Returns:
            API response as a dictionary.
        """
        ...

    def replicate_list_public_models(
        self,
    ) -> Dict[str, Any]:
        """Returns a paginated list of publicly available models on the Replicate platform. Use this to browse or discover models that can be used for predictions. Do not use this to retrieve details of a specific model or to list models belonging only to the authenticated account — use replicate_get_model for single-model details.
        Returns:
            API response as a dictionary.
        """
        ...

    def replicate_list_trainings(
        self,
    ) -> Dict[str, Any]:
        """Returns a paginated list of all model training sessions associated with the authenticated Replicate account. Use this to review or audit past and ongoing training jobs. Do not use this to start a new training session or fetch details of a single training run — use the appropriate create or get training tools instead.
        Returns:
            API response as a dictionary.
        """
        ...

