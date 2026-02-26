"""Fastn Firebase Firestore connector — auto-generated type stubs.

Do not edit manually. Regenerate with `fastn connector sync`.
"""
from __future__ import annotations

from typing import Any, Dict, List, Optional


class FirebaseFirestoreConnector:
    """Firebase Firestore connector ().

    Provides 11 tools.
    """

    def begin_transaction(
        self,
        access_token: Optional[str] = None,
        alt: Optional[str] = None,
        callback: Optional[str] = None,
        fields: Optional[str] = None,
        key: Optional[str] = None,
        oauth_token: Optional[str] = None,
        prettyPrint: Optional[str] = None,
        quotaUser: Optional[str] = None,
        uploadType: Optional[str] = None,
        upload_protocol: Optional[str] = None,
        xgafv: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Begins a new transaction in the database to group multiple operations for atomic execution.

        Args:
            access_token: Access token for the request.
            alt: Data format for the response.
            callback: JSONP callback function name.
            fields: Comma-separated list of fields to include in the response.
            key: API key.
            oauth_token: OAuth token for authentication.
            prettyPrint: Whether to format the response.
            quotaUser: User's email address for quota purposes.
            uploadType: Type of upload.
            upload_protocol: Upload protocol.
            xgafv: Google API data format version.
        Returns:
            API response as a dictionary.
        """
        ...

    def commit_transaction(
        self,
        access_token: Optional[str] = None,
        alt: Optional[str] = None,
        callback: Optional[str] = None,
        fields: Optional[str] = None,
        key: Optional[str] = None,
        oauth_token: Optional[str] = None,
        prettyPrint: Optional[str] = None,
        quotaUser: Optional[str] = None,
        uploadType: Optional[str] = None,
        upload_protocol: Optional[str] = None,
        xgafv: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Commits the current transaction, saving all changes made during the transaction period to the database.

        Args:
            access_token: OAuth 2.0 access token.
            alt: Data format for the response.
            callback: Callback function name.
            fields: Comma-separated list of fields to include in the response.
            key: API key.
            oauth_token: OAuth 1.0a token.
            prettyPrint: Indicate whether to format the response in a human-readable way.
            quotaUser: User quota.
            uploadType: Type of upload.
            upload_protocol: Upload protocol.
            xgafv: API version.
        Returns:
            API response as a dictionary.
        """
        ...

    def create_document(
        self,
        documentId: str,
        access_token: Optional[str] = None,
        alt: Optional[str] = None,
        callback: Optional[str] = None,
        fields: Optional[str] = None,
        key: Optional[str] = None,
        maskfieldPaths: Optional[str] = None,
        oauth_token: Optional[str] = None,
        prettyPrint: Optional[str] = None,
        quotaUser: Optional[str] = None,
        uploadType: Optional[str] = None,
        upload_protocol: Optional[str] = None,
        xgafv: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Creates a new document in the database with the provided data fields.

        Args:
            documentId: ID of the document. (required)
            access_token: OAuth access token.
            alt: Data format for the response.
            callback: Callback URL.
            fields: Comma-separated list of fields to return.
            key: API key.
            maskfieldPaths: Fields to mask.
            oauth_token: OAuth token.
            prettyPrint: Returns response with indentations and line breaks.
            quotaUser: API quota user.
            uploadType: Type of upload.
            upload_protocol: Upload protocol.
            xgafv: V1 error format.
        Returns:
            API response as a dictionary.
        """
        ...

    def delete_document(
        self,
        access_token: Optional[str] = None,
        alt: Optional[str] = None,
        callback: Optional[str] = None,
        currentDocumentexists: Optional[str] = None,
        currentDocumentupdateTime: Optional[str] = None,
        fields: Optional[str] = None,
        key: Optional[str] = None,
        oauth_token: Optional[str] = None,
        prettyPrint: Optional[str] = None,
        quotaUser: Optional[str] = None,
        uploadType: Optional[str] = None,
        upload_protocol: Optional[str] = None,
        xgafv: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Deletes a specific document from the database using its unique document ID.

        Args:
            access_token: Access token for authorization.
            alt: Alternative data format.
            callback: Callback URL.
            currentDocumentexists: Indicates if the current document exists.
            currentDocumentupdateTime: Last updated time of the current document.
            fields: Comma-separated list of fields to retrieve.
            key: API Key.
            oauth_token: OAuth token for authorization.
            prettyPrint: Specifies whether to format the response in a human-readable way.
            quotaUser: User quota for the request.
            uploadType: Type of upload.
            upload_protocol: Upload protocol.
            xgafv: Version of the Google APIs to use.
        Returns:
            API response as a dictionary.
        """
        ...

    def get_collections(
        self,
        access_token: Optional[str] = None,
        alt: Optional[str] = None,
        callback: Optional[str] = None,
        fields: Optional[str] = None,
        key: Optional[str] = None,
        oauth_token: Optional[str] = None,
        prettyPrint: Optional[str] = None,
        quotaUser: Optional[str] = None,
        uploadType: Optional[str] = None,
        upload_protocol: Optional[str] = None,
        xgafv: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Fetches all collections available in the database context for querying and data management.

        Args:
            access_token: OAuth 2.0 access token.
            alt: Data format for the response.
            callback: Callback function name for asynchronous requests.
            fields: Comma-separated list of fields to include in the response.
            key: API key.
            oauth_token: OAuth 1.0a access token.
            prettyPrint: Returns response in a pretty printed format.
            quotaUser: User's email address for quota purposes.
            uploadType: Type of upload protocol.
            upload_protocol: Upload protocol used.
            xgafv: Version of the Google APIs client library used.
        Returns:
            API response as a dictionary.
        """
        ...

    def get_database(
        self,
        access_token: Optional[str] = None,
        alt: Optional[str] = None,
        callback: Optional[str] = None,
        fields: Optional[str] = None,
        prettyPrint: Optional[str] = None,
        quotaUser: Optional[str] = None,
        uploadType: Optional[str] = None,
        upload_protocol: Optional[str] = None,
        xgafv: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Retrieves database metadata and information about the database structure.

        Args:
            access_token: An access token for the request.
            alt: Specifies the alternative data format for the response.
            callback: JSONP callback function name.
            fields: Comma-separated list of fields to include in the response.
            prettyPrint: Specifies whether to return the response in a pretty-printed format.
            quotaUser: User to impersonate for the request.
            uploadType: Type of upload protocol.
            upload_protocol: Protocol used for uploading data.
            xgafv: API version to use.
        Returns:
            API response as a dictionary.
        """
        ...

    def get_document(
        self,
        maskfieldPaths: Optional[str] = None,
        readTime: Optional[str] = None,
        transaction: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Retrieves a specific document from the database using the specified document ID.

        Args:
            maskfieldPaths: Paths to mask in the Firestore document.
            readTime: Read time for the Firestore operation.
            transaction: Transaction ID for the Firestore operation.
        Returns:
            API response as a dictionary.
        """
        ...

    def get_documents(
        self,
        access_token: Optional[str] = None,
        alt: Optional[str] = None,
        callback: Optional[str] = None,
        key: Optional[str] = None,
        maskfieldPaths: Optional[str] = None,
        orderBy: Optional[str] = None,
        pageSize: Optional[str] = None,
        pageToken: Optional[str] = None,
        quotaUser: Optional[str] = None,
        readTime: Optional[str] = None,
        showMissing: Optional[str] = None,
        transaction: Optional[str] = None,
        uploadType: Optional[str] = None,
        upload_protocol: Optional[str] = None,
        xgafv: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Fetches multiple documents from the database, allowing for batch retrieval based on specified criteria.

        Args:
            access_token: Access token for the request.
            alt: Alternate data format for the response.
            callback: Callback function for the response.
            key: API Key for the request.
            maskfieldPaths: Fields to mask in the response.
            orderBy: Field to order the results by.
            pageSize: Number of results per page.
            pageToken: Token for pagination.
            quotaUser: Quota user for the request.
            readTime: Read time for the request.
            showMissing: Whether to show missing fields.
            transaction: Transaction ID for the request.
            uploadType: Type of upload.
            upload_protocol: Upload protocol for the request.
            xgafv: Google API version.
        Returns:
            API response as a dictionary.
        """
        ...

    def rollback_transaction(
        self,
        access_token: Optional[str] = None,
        alt: Optional[str] = None,
        callback: Optional[str] = None,
        fields: Optional[str] = None,
        key: Optional[str] = None,
        oauth_token: Optional[str] = None,
        prettyPrint: Optional[str] = None,
        quotaUser: Optional[str] = None,
        uploadType: Optional[str] = None,
        upload_protocol: Optional[str] = None,
        xgafv: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Rolls back the current transaction, reverting all changes made during the transaction period to maintain data integrity.

        Args:
            access_token: An access token.
            alt: Data format preference.
            callback: Callback URL.
            fields: Comma-separated list of fields to return.
            key: API Key for authentication.
            oauth_token: OAuth token for authentication.
            prettyPrint: Indicate whether to return formatted JSON response.
            quotaUser: User to charge quota to.
            uploadType: Type of upload.
            upload_protocol: Protocol for uploading data.
            xgafv: API version.
        Returns:
            API response as a dictionary.
        """
        ...

    def run_query(
        self,
        access_token: Optional[str] = None,
        alt: Optional[str] = None,
        callback: Optional[str] = None,
        fields: Optional[str] = None,
        key: Optional[str] = None,
        oauth_token: Optional[str] = None,
        prettyPrint: Optional[str] = None,
        quotaUser: Optional[str] = None,
        uploadType: Optional[str] = None,
        upload_protocol: Optional[str] = None,
        xgafv: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Executes a custom query on the database to retrieve data based on specific query parameters.

        Args:
            access_token: Access token for authentication.
            alt: Alternative data format.
            callback: Callback URL.
            fields: Fields to select.
            key: API key.
            oauth_token: OAuth token.
            prettyPrint: Pretty print response.
            quotaUser: Quota user.
            uploadType: Type of upload.
            upload_protocol: Upload protocol.
            xgafv: API version.
        Returns:
            API response as a dictionary.
        """
        ...

    def update_document(
        self,
        access_token: Optional[str] = None,
        alt: Optional[str] = None,
        callback: Optional[str] = None,
        currentDocumentexists: Optional[str] = None,
        currentDocumentupdateTime: Optional[str] = None,
        fields: Optional[str] = None,
        key: Optional[str] = None,
        maskfieldPaths: Optional[str] = None,
        oauth_token: Optional[str] = None,
        prettyPrint: Optional[str] = None,
        quotaUser: Optional[str] = None,
        updateMaskfieldPaths: Optional[str] = None,
        uploadType: Optional[str] = None,
        upload_protocol: Optional[str] = None,
        xgafv: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Updates an existing document in the database with new data fields identified by the document ID.

        Args:
            access_token: Access token for the request.
            alt: Alternative parameter.
            callback: Callback URL.
            currentDocumentexists: Indicates if the current document exists.
            currentDocumentupdateTime: Last update time of the current document.
            fields: Comma-separated list of fields to return.
            key: API Key.
            maskfieldPaths: Fields to mask.
            oauth_token: OAuth token.
            prettyPrint: Returns response in a pretty-printed format.
            quotaUser: Quota User.
            updateMaskfieldPaths: Fields to update.
            uploadType: Type of upload.
            upload_protocol: Upload protocol.
            xgafv: API version.
        Returns:
            API response as a dictionary.
        """
        ...

