"""Fastn Firebase Firestore connector — auto-generated type stubs.

Do not edit manually. Regenerate with `fastn connector sync`.
"""
from __future__ import annotations

from typing import Any, Dict, List, Optional, TypedDict


class _FirebaseFirestoreBeginTransactionOptions(TypedDict, total=False):
    readOnly: Dict[str, Any]
    readWrite: Dict[str, Any]

class _FirebaseFirestoreCreateDocumentFields(TypedDict, total=False):
    name: Dict[str, Any]

class _FirebaseFirestoreRunQueryNewtransaction(TypedDict, total=False):
    readOnly: Dict[str, Any]
    readWrite: Dict[str, Any]

class _FirebaseFirestoreRunQueryStructuredquery(TypedDict, total=False):
    endAt: Dict[str, Any]
    from: List[Any]
    limit: str
    offset: str
    orderBy: List[Any]
    select: Dict[str, Any]
    startAt: Dict[str, Any]
    where: Dict[str, Any]

class _FirebaseFirestoreUpdateDocumentFields(TypedDict, total=False):
    age: Dict[str, Any]
    email: Dict[str, Any]
    isActive: Dict[str, Any]
    name: Dict[str, Any]
    signupDate: Dict[str, Any]

class FirebaseFirestoreConnector:
    """Firebase Firestore connector ().

    Provides 11 tools.
    """

    def firebase_firestore_begin_transaction(
        self,
        databaseId: str,
        projectId: str,
        access_token: Optional[str] = None,
        alt: Optional[str] = None,
        callback: Optional[str] = None,
        fields: Optional[str] = None,
        key: Optional[str] = None,
        oauth_token: Optional[str] = None,
        options: Optional[_FirebaseFirestoreBeginTransactionOptions] = None,
        prettyPrint: Optional[str] = None,
        quotaUser: Optional[str] = None,
        uploadType: Optional[str] = None,
        upload_protocol: Optional[str] = None,
        xgafv: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Begins a new Firestore transaction and returns a transaction ID, enabling multiple read and write operations to be grouped for atomic execution. Use this tool when you need to perform several document operations that must all succeed or all fail together. Follow up with firebase_firestore_commit_transaction to persist changes or firebase_firestore_rollback_transaction to abort.

        Args:
            databaseId: ID of the Firestore database. (required)
            projectId: ID of the Google Cloud project. (required)
            access_token: Access token for the request.
            alt: Data format for the response.
            callback: JSONP callback function name.
            fields: Comma-separated list of fields to include in the response.
            key: API key.
            oauth_token: OAuth token for authentication.
            options: Options for the Firestore operation.
            prettyPrint: Whether to format the response.
            quotaUser: User's email address for quota purposes.
            uploadType: Type of upload.
            upload_protocol: Upload protocol.
            xgafv: Google API data format version.
        Returns:
            API response as a dictionary.
        """
        ...

    def firebase_firestore_commit_transaction(
        self,
        databaseId: str,
        projectId: str,
        access_token: Optional[str] = None,
        alt: Optional[str] = None,
        callback: Optional[str] = None,
        fields: Optional[str] = None,
        key: Optional[str] = None,
        oauth_token: Optional[str] = None,
        prettyPrint: Optional[str] = None,
        quotaUser: Optional[str] = None,
        transaction: Optional[str] = None,
        uploadType: Optional[str] = None,
        upload_protocol: Optional[str] = None,
        writes: Optional[List[Any]] = None,
        xgafv: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Commits an active Firestore transaction, atomically persisting all writes staged during the transaction to the database. Use this tool to finalize a group of related document operations as a single atomic unit. This operation is irreversible — once committed, changes are permanently written to the database. Must be called with a valid transaction ID obtained from firebase_firestore_begin_transaction.

        Args:
            databaseId: ID of the Firestore database. (required)
            projectId: ID of the Google Cloud project. (required)
            access_token: OAuth 2.0 access token.
            alt: Data format for the response.
            callback: Callback function name.
            fields: Comma-separated list of fields to include in the response.
            key: API key.
            oauth_token: OAuth 1.0a token.
            prettyPrint: Indicate whether to format the response in a human-readable way.
            quotaUser: User quota.
            transaction: Transaction ID (optional).
            uploadType: Type of upload.
            upload_protocol: Upload protocol.
            writes: 
            xgafv: API version.
        Returns:
            API response as a dictionary.
        """
        ...

    def firebase_firestore_create_document(
        self,
        collectionId: str,
        databaseId: str,
        documentId: str,
        fields: _FirebaseFirestoreCreateDocumentFields,
        projectId: str,
        access_token: Optional[str] = None,
        alt: Optional[str] = None,
        callback: Optional[str] = None,
        createTime: Optional[str] = None,
        key: Optional[str] = None,
        maskfieldPaths: Optional[str] = None,
        name: Optional[str] = None,
        oauth_token: Optional[str] = None,
        prettyPrint: Optional[str] = None,
        quotaUser: Optional[str] = None,
        updateTime: Optional[str] = None,
        uploadType: Optional[str] = None,
        upload_protocol: Optional[str] = None,
        xgafv: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Creates a new document in a specified Firestore collection with the provided field data. Use this tool when you need to add a new record to a collection. A new document ID will be auto-generated unless specified. Do not use this tool to update an existing document — use firebase_firestore_update_document instead.

        Args:
            collectionId: ID of the collection. (required)
            databaseId: ID of the Firestore database. (required)
            documentId: ID of the document. (required)
            fields: Fields within the document. (required)
            projectId: ID of the Google Cloud project. (required)
            access_token: OAuth access token.
            alt: Data format for the response.
            callback: Callback URL.
            createTime: Creation timestamp.
            key: API key.
            maskfieldPaths: Fields to mask.
            name: Name of the document.
            oauth_token: OAuth token.
            prettyPrint: Returns response with indentations and line breaks.
            quotaUser: API quota user.
            updateTime: Last update timestamp.
            uploadType: Type of upload.
            upload_protocol: Upload protocol.
            xgafv: V1 error format.
        Returns:
            API response as a dictionary.
        """
        ...

    def firebase_firestore_delete_document(
        self,
        databaseId: str,
        document_path: str,
        projectId: str,
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
        """Permanently deletes a specific document from Firestore using its full document path. Use this tool when a document must be removed from the database. This operation is irreversible — the document and its fields cannot be recovered after deletion. Subcollections of the deleted document are not automatically removed.

        Args:
            databaseId: ID of the Firestore database. (required)
            document_path: Path to the document in Firestore. (required)
            projectId: ID of the Google Cloud project. (required)
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

    def firebase_firestore_get_database(
        self,
        databaseId: str,
        projectId: str,
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
        """Retrieves configuration metadata for a specific Firestore database instance, including its name, location, type, and concurrency settings. Use this tool when you need to inspect database-level properties rather than document or collection data. Do not use this tool to list collections or retrieve documents.

        Args:
            databaseId: The ID of the Firestore database. (required)
            projectId: The ID of the Google Cloud project. (required)
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

    def firebase_firestore_get_document(
        self,
        databaseId: str,
        document_path: str,
        projectId: str,
        maskfieldPaths: Optional[str] = None,
        readTime: Optional[str] = None,
        transaction: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Retrieves a single Firestore document by its full document path, returning all of its field values and metadata. Use this tool when you know the exact path of the document you need. Do not use this tool to list multiple documents in a collection — use firebase_firestore_list_documents or firebase_firestore_run_query instead.

        Args:
            databaseId: ID of the Firestore database. (required)
            document_path: Path to the document in Firestore. (required)
            projectId: ID of the Firebase project. (required)
            maskfieldPaths: Paths to mask in the Firestore document.
            readTime: Read time for the Firestore operation.
            transaction: Transaction ID for the Firestore operation.
        Returns:
            API response as a dictionary.
        """
        ...

    def firebase_firestore_list_collections(
        self,
        databaseId: str,
        projectId: str,
        access_token: Optional[str] = None,
        alt: Optional[str] = None,
        callback: Optional[str] = None,
        fields: Optional[str] = None,
        key: Optional[str] = None,
        oauth_token: Optional[str] = None,
        pageSize: Optional[str] = None,
        pageToken: Optional[str] = None,
        prettyPrint: Optional[str] = None,
        quotaUser: Optional[str] = None,
        uploadType: Optional[str] = None,
        upload_protocol: Optional[str] = None,
        xgafv: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Lists all top-level collection IDs available in a Firestore database. Use this tool when you need to discover which collections exist in the database before querying or managing documents. Do not use this tool to retrieve documents — use firebase_firestore_list_documents or firebase_firestore_run_query instead.

        Args:
            databaseId: ID of the Firestore database. (required)
            projectId: ID of the Google Cloud project. (required)
            access_token: OAuth 2.0 access token.
            alt: Data format for the response.
            callback: Callback function name for asynchronous requests.
            fields: Comma-separated list of fields to include in the response.
            key: API key.
            oauth_token: OAuth 1.0a access token.
            pageSize: Number of documents to return per page.
            pageToken: Token to retrieve the next page of results.
            prettyPrint: Returns response in a pretty printed format.
            quotaUser: User's email address for quota purposes.
            uploadType: Type of upload protocol.
            upload_protocol: Upload protocol used.
            xgafv: Version of the Google APIs client library used.
        Returns:
            API response as a dictionary.
        """
        ...

    def firebase_firestore_list_documents(
        self,
        collectionId: str,
        databaseId: str,
        projectId: str,
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
        """Lists all documents within a specified Firestore collection. Use this tool when you need to enumerate documents in a collection without applying query filters. Do not use this tool to retrieve a single document — use firebase_firestore_get_document instead. For filtered or sorted results, use firebase_firestore_run_query.

        Args:
            collectionId: ID of the Firestore collection. (required)
            databaseId: ID of the Firestore database. (required)
            projectId: ID of the Google Cloud project. (required)
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

    def firebase_firestore_rollback_transaction(
        self,
        databaseId: str,
        projectId: str,
        transaction: str,
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
        """Rolls back an active Firestore transaction, discarding all pending writes and reversing any changes staged during that transaction. Use this tool when an error or condition requires aborting a transaction to maintain data integrity. This operation is irreversible — once rolled back, the staged changes cannot be recovered. Must be called with a valid transaction ID obtained from firebase_firestore_begin_transaction.

        Args:
            databaseId: Identifier of the Firestore database. (required)
            projectId: Identifier of the Google Cloud project. (required)
            transaction: Transaction ID or other transaction-related data (if applicable). (required)
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

    def firebase_firestore_run_query(
        self,
        databaseId: str,
        projectId: str,
        access_token: Optional[str] = None,
        alt: Optional[str] = None,
        callback: Optional[str] = None,
        fields: Optional[str] = None,
        key: Optional[str] = None,
        newTransaction: Optional[_FirebaseFirestoreRunQueryNewtransaction] = None,
        oauth_token: Optional[str] = None,
        prettyPrint: Optional[str] = None,
        quotaUser: Optional[str] = None,
        readTime: Optional[str] = None,
        structuredQuery: Optional[_FirebaseFirestoreRunQueryStructuredquery] = None,
        transaction: Optional[str] = None,
        uploadType: Optional[str] = None,
        upload_protocol: Optional[str] = None,
        xgafv: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Executes a structured query against a Firestore collection or collection group and returns matching documents. Use this tool when you need to filter, sort, or limit documents based on field values. Do not use this tool to retrieve a single document by ID — use firebase_firestore_get_document instead, or firebase_firestore_list_documents to list all documents in a collection without filtering.

        Args:
            databaseId: ID of the Firestore database. (required)
            projectId: ID of the Google Cloud project. (required)
            access_token: Access token for authentication.
            alt: Alternative data format.
            callback: Callback URL.
            fields: Fields to select.
            key: API key.
            newTransaction: Details for a new transaction.
            oauth_token: OAuth token.
            prettyPrint: Pretty print response.
            quotaUser: Quota user.
            readTime: Read time for the operation.
            structuredQuery: Structured query for Firestore.
            transaction: Transaction ID.
            uploadType: Type of upload.
            upload_protocol: Upload protocol.
            xgafv: API version.
        Returns:
            API response as a dictionary.
        """
        ...

    def firebase_firestore_update_document(
        self,
        databaseId: str,
        document_path: str,
        projectId: str,
        access_token: Optional[str] = None,
        alt: Optional[str] = None,
        callback: Optional[str] = None,
        currentDocumentexists: Optional[str] = None,
        currentDocumentupdateTime: Optional[str] = None,
        fields: Optional[_FirebaseFirestoreUpdateDocumentFields] = None,
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
        """Updates an existing Firestore document at the specified document path with new or modified field values. Use this tool to partially or fully overwrite the fields of an existing document. The document must already exist; use firebase_firestore_create_document to create a new one. This operation overwrites specified fields and may permanently remove fields not included in the update payload depending on update mask configuration.

        Args:
            databaseId: ID of the Firestore database. (required)
            document_path: Path to the document. (required)
            projectId: ID of the Google Cloud project. (required)
            access_token: Access token for the request.
            alt: Alternative parameter.
            callback: Callback URL.
            currentDocumentexists: Indicates if the current document exists.
            currentDocumentupdateTime: Last update time of the current document.
            fields: Fields of the document.
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

