"""Fastn Attio connector — auto-generated type stubs.

Do not edit manually. Regenerate with `fastn connector sync`.
"""
from __future__ import annotations

from typing import Any, Dict, List, Optional, TypedDict


class _AttioCreateCompanyRecordData(TypedDict, total=False):
    values: Dict[str, Any]

class _AttioCreateDealRecordData(TypedDict, total=False):
    values: Dict[str, Any]

class _AttioCreateListData(TypedDict, total=False):
    api_slug: str
    name: str
    parent_object: str
    workspace_access: str
    workspace_member_access: List[Any]

class _AttioCreateNoteData(TypedDict, total=False):
    content: str
    created_at: str
    format: str
    meeting_id: str
    parent_object: str
    parent_record_id: str
    title: str

class _AttioCreatePersonRecordData(TypedDict, total=False):
    values: Dict[str, Any]

class _AttioCreateTaskData(TypedDict, total=False):
    assignees: List[Any]
    content: str
    deadline_at: str
    format: str
    is_completed: bool
    linked_records: List[Any]

class _AttioListCompanyRecordsFilter(TypedDict, total=False):
    _and: List[Any]

class _AttioListDealRecordsFilter(TypedDict, total=False):
    _and: List[Any]

class _AttioListPersonRecordsFilter(TypedDict, total=False):
    _and: List[Any]

class _AttioSearchRecordsRequestAs(TypedDict, total=False):
    email_address: str
    type: str
    workspace_member_id: str

class _AttioUpdateCompanyRecordData(TypedDict, total=False):
    values: Dict[str, Any]

class _AttioUpdateDealRecordData(TypedDict, total=False):
    values: Dict[str, Any]

class _AttioUpdateListData(TypedDict, total=False):
    api_slug: str
    name: str
    workspace_access: str
    workspace_member_access: List[Any]

class _AttioUpdatePersonRecordData(TypedDict, total=False):
    values: Dict[str, Any]

class _AttioUpdateTaskData(TypedDict, total=False):
    assignees: List[Any]
    deadline_at: str
    is_completed: bool
    linked_records: List[Any]

class AttioConnector:
    """Attio connector ().

    Provides 32 tools.
    """

    def attio_create_company_record(
        self,
        data: _AttioCreateCompanyRecordData,
    ) -> Dict[str, Any]:
        """Creates a new company record in Attio. Use this tool when a new company needs to be added to the CRM, providing details such as company name, domain, and industry. Do not use this tool to update an existing company — use attio_update_company_record instead. This operation creates a permanent record; duplicates will not be automatically detected.

        Args:
            data: The core data object containing all relevant information. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def attio_create_deal_record(
        self,
        data: _AttioCreateDealRecordData,
    ) -> Dict[str, Any]:
        """Creates a new deal record in Attio. Use this tool when a new business deal needs to be tracked, providing details such as deal name, value, associated company, and stage. Do not use this tool to update an existing deal — use attio_update_deal_record instead. This operation creates a permanent record; duplicates will not be automatically detected.

        Args:
            data: Data object containing values for the API request. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def attio_create_list(
        self,
        data: _AttioCreateListData,
    ) -> Dict[str, Any]:
        """Creates a new list in Attio. Use this tool to define a new collection for organizing records, specifying the list name, associated object type, and other configuration. Do not use this tool to update an existing list — use attio_update_list instead. This operation creates a permanent list structure.

        Args:
            data: Contains the main data fields for the request. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def attio_create_note(
        self,
        data: _AttioCreateNoteData,
    ) -> Dict[str, Any]:
        """Creates a new note in Attio and associates it with a specific record (e.g., a company, person, or deal). Use this tool to add documentation, context, or annotations to a CRM record. Do not use this tool to update an existing note — delete and recreate if a note must be changed. This operation creates a permanent record.

        Args:
            data: Data object containing various details for the request. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def attio_create_person_record(
        self,
        data: _AttioCreatePersonRecordData,
    ) -> Dict[str, Any]:
        """Creates a new person (contact) record in Attio. Use this tool when a new individual needs to be added to the CRM, providing details such as name, email, and phone number. Do not use this tool to update an existing person — use attio_update_person_record instead. This operation creates a permanent record; duplicates will not be automatically detected.

        Args:
            data: Data payload sent to Attio. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def attio_create_task(
        self,
        data: _AttioCreateTaskData,
    ) -> Dict[str, Any]:
        """Creates a new task in Attio. Use this tool to assign and track work within the workspace, providing details such as title, description, assignee, due date, and linked record. Do not use this tool to update an existing task — use attio_update_task instead. This operation creates a permanent record.

        Args:
            data: Data object containing task details. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def attio_delete_company_record(
        self,
        recordId: str,
    ) -> Dict[str, Any]:
        """Permanently deletes a specific company record from Attio by its unique record ID. Use this tool only when a company must be removed entirely from the database. Do not use this tool to update company details — use attio_update_company_record instead. This action is irreversible; the deleted record cannot be recovered.

        Args:
            recordId: The unique identifier for a specific record in Attio. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def attio_delete_deal_record(
        self,
        recordId: str,
    ) -> Dict[str, Any]:
        """Permanently deletes a specific deal record from Attio by its unique record ID. Use this tool only when a deal must be removed entirely from the database. Do not use this tool to archive or update a deal — use attio_update_deal_record instead. This action is irreversible; the deleted deal record cannot be recovered.

        Args:
            recordId: Unique identifier of the record in Attio. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def attio_delete_note(
        self,
        noteId: str,
    ) -> Dict[str, Any]:
        """Permanently deletes a specific note from Attio by its unique note ID. Use this tool only when a note must be removed entirely. Do not use this tool to edit a notes content — notes may need to be recreated if content must change. This action is irreversible; the deleted note cannot be recovered.

        Args:
            noteId: The unique identifier for the note within Attio. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def attio_delete_person_record(
        self,
        recordId: str,
    ) -> Dict[str, Any]:
        """Permanently deletes a specific person record from Attio by its unique record ID. Use this tool only when a contact must be removed entirely from the database. Do not use this tool to update a persons details — use attio_update_person_record instead. This action is irreversible; the deleted record cannot be recovered.

        Args:
            recordId: Identifier for the specific record in Attio. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def attio_delete_task(
        self,
        taskId: str,
    ) -> Dict[str, Any]:
        """Permanently deletes a specific task from Attio by its unique task ID. Use this tool only when a task must be removed entirely from the workspace. Do not use this tool to mark a task as complete or update its details — use attio_update_task instead. This action is irreversible; the deleted task cannot be recovered.

        Args:
            taskId: The unique identifier of the task. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def attio_get_company_record(
        self,
        recordId: str,
    ) -> Dict[str, Any]:
        """Retrieves a single company record from Attio by its unique record ID. Use this tool when you need full details about a specific company. Do not use this tool to retrieve multiple companies — use attio_list_company_records instead. This is a read-only operation with no side effects.

        Args:
            recordId: Unique identifier of the record in Attio. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def attio_get_deal_record(
        self,
        recordId: str,
    ) -> Dict[str, Any]:
        """Retrieves a single deal record from Attio by its unique record ID. Use this tool when you need full details about a specific deal (e.g., value, status, associated contacts). Do not use this tool to retrieve multiple deals — use attio_list_deal_records instead. This is a read-only operation with no side effects.

        Args:
            recordId: The unique identifier for a record in Attio. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def attio_get_list(
        self,
        listId: str,
    ) -> Dict[str, Any]:
        """Retrieves the metadata and configuration of a single list in Attio by its unique list ID. Use this tool when you need details about a specific lists structure or settings. Do not use this tool to retrieve all lists — use attio_list_lists instead. This is a read-only operation with no side effects.

        Args:
            listId: The unique identifier of the list in Attio. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def attio_get_note(
        self,
        noteId: str,
    ) -> Dict[str, Any]:
        """Retrieves a single note from Attio by its unique note ID. Use this tool when you need the full content of a specific note. Do not use this tool to retrieve multiple notes — use attio_list_notes instead. This is a read-only operation with no side effects.

        Args:
            noteId: The identifier for the specific note within Attio. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def attio_get_object(
        self,
        objectId: str,
    ) -> Dict[str, Any]:
        """Retrieves the schema and metadata of a single Attio object (e.g., companies, people, deals, or a custom object) by its unique object ID or slug. Use this tool to inspect an objects attributes and configuration. Do not use this tool to retrieve records belonging to an object — use the relevant list or get record tools instead. This is a read-only operation with no side effects.

        Args:
            objectId: Unique identifier for the specific Attio object. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def attio_get_person_record(
        self,
        recordId: str,
    ) -> Dict[str, Any]:
        """Retrieves a single person (contact) record from Attio by its unique record ID. Use this tool when you need full details about a specific individual. Do not use this tool to retrieve multiple people — use attio_list_person_records instead. This is a read-only operation with no side effects.

        Args:
            recordId: The unique identifier for the specific record in Attio. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def attio_get_task(
        self,
        taskId: str,
    ) -> Dict[str, Any]:
        """Retrieves a single task from Attio by its unique task ID. Use this tool when you need full details about a specific task, including its description, assignee, and due date. Do not use this tool to retrieve multiple tasks — use attio_list_tasks instead. This is a read-only operation with no side effects.

        Args:
            taskId: Unique identifier for the task in Attio. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def attio_list_company_records(
        self,
        filter: Optional[_AttioListCompanyRecordsFilter] = None,
        limit: Optional[int] = None,
        offset: Optional[int] = None,
        sorts: Optional[List[Any]] = None,
    ) -> Dict[str, Any]:
        """Lists company records in Attio using a query to filter, sort, and paginate results. Use this tool to retrieve a collection of companies (e.g., all companies in a specific industry or region). Do not use this tool if you need a single company by ID — use attio_get_company_record instead. This is a read-only operation with no side effects.

        Args:
            filter: Filtering options to refine the data retrieval.
            limit: Maximum number of records to return.
            offset: Number of records to skip for pagination.
            sorts: 
        Returns:
            API response as a dictionary.
        """
        ...

    def attio_list_deal_records(
        self,
        filter: Optional[_AttioListDealRecordsFilter] = None,
        limit: Optional[int] = None,
        offset: Optional[int] = None,
        sorts: Optional[List[Any]] = None,
    ) -> Dict[str, Any]:
        """Lists deal records in Attio using a query to filter, sort, and paginate results. Use this tool to retrieve a collection of deals (e.g., all open deals, deals above a certain value). Do not use this tool if you need a single deal by ID — use attio_get_deal_record instead. This is a read-only operation with no side effects.

        Args:
            filter: Filter criteria for querying data from Attio.
            limit: Maximum number of records to return.
            offset: Number of records to skip before starting to return results.
            sorts: 
        Returns:
            API response as a dictionary.
        """
        ...

    def attio_list_lists(
        self,
    ) -> Dict[str, Any]:
        """Lists all lists defined in the Attio workspace, including their names, IDs, and associated object types. Use this tool to discover what lists are available for organizing records. Do not use this tool if you need details about a single list by ID — use attio_get_list instead. This is a read-only operation with no side effects.
        Returns:
            API response as a dictionary.
        """
        ...

    def attio_list_notes(
        self,
        limit: Optional[int] = None,
        offset: Optional[int] = None,
        parent_object: Optional[str] = None,
        parent_record_id: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Lists all notes stored in Attio, optionally filtered by associated record or object. Use this tool to retrieve a collection of notes across your workspace. Do not use this tool if you need a single note by ID — use attio_get_note instead. This is a read-only operation with no side effects.

        Args:
            limit: Maximum number of records to retrieve.
            offset: Number of records to skip before starting to collect the result set.
            parent_object: The parent object in Attio from which to query.
            parent_record_id: Identifier of the parent record in Attio.
        Returns:
            API response as a dictionary.
        """
        ...

    def attio_list_objects(
        self,
    ) -> Dict[str, Any]:
        """Lists all objects (standard and custom) defined in the Attio workspace, including their slugs, names, and metadata. Use this tool to discover what object types are available in the workspace. Do not use this tool to retrieve records — use the relevant list record tools instead. This is a read-only operation with no side effects.
        Returns:
            API response as a dictionary.
        """
        ...

    def attio_list_person_records(
        self,
        filter: Optional[_AttioListPersonRecordsFilter] = None,
        limit: Optional[int] = None,
        offset: Optional[int] = None,
        sorts: Optional[List[Any]] = None,
    ) -> Dict[str, Any]:
        """Lists person (contact) records in Attio using a query to filter, sort, and paginate results. Use this tool to retrieve a collection of people (e.g., all contacts with a specific role or company). Do not use this tool if you need a single person by ID — use attio_get_person_record instead. This is a read-only operation with no side effects.

        Args:
            filter: Filtering criteria for the API request.
            limit: Maximum number of records to retrieve.
            offset: Number of records to skip.
            sorts: 
        Returns:
            API response as a dictionary.
        """
        ...

    def attio_list_tasks(
        self,
        assignee: Optional[str] = None,
        is_completed: Optional[bool] = None,
        limit: Optional[int] = None,
        linked_object: Optional[str] = None,
        linked_record_id: Optional[str] = None,
        offset: Optional[int] = None,
        sort: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Lists all tasks in the Attio workspace, optionally filtered by assignee, status, or linked record. Use this tool to retrieve a collection of tasks for review or reporting. Do not use this tool if you need a single task by ID — use attio_get_task instead. This is a read-only operation with no side effects.

        Args:
            assignee: The person assigned to the task or record.
            is_completed: Indicates whether the task or record is completed.
            limit: Limits the number of records returned.
            linked_object: The object linked to the record, such as a contact or deal.
            linked_record_id: The ID of the linked record.
            offset: Number of records to skip before starting to collect the response set.
            sort: Sorting order of the results.
        Returns:
            API response as a dictionary.
        """
        ...

    def attio_list_workspace_members(
        self,
    ) -> Dict[str, Any]:
        """Lists all members of the Attio workspace, including their names, roles, and identifiers. Use this tool to discover who has access to the workspace or to resolve member IDs for task assignment. This is a read-only operation with no side effects.
        Returns:
            API response as a dictionary.
        """
        ...

    def attio_search_records(
        self,
        objects: List[Any],
        query: str,
        request_as: _AttioSearchRecordsRequestAs,
        limit: Optional[int] = None,
    ) -> Dict[str, Any]:
        """Search across all records in Attio using specified filter criteria (e.g., name, status, custom attributes). Use this tool when you need to find one or more records of any object type (companies, people, deals, or custom objects) based on a query. Do not use this tool if you already know the records unique ID — use the specific get tool instead. Returns a list of matching records. This is a read-only operation with no side effects.

        Args:
            objects: Array of object types to include in the request (each item is an object type identifier). (required)
            query: The search or query string to be executed against Attio. (required)
            request_as: Specifies the identity context under which the request should be made. (required)
            limit: Maximum number of results to return for the request.
        Returns:
            API response as a dictionary.
        """
        ...

    def attio_update_company_record(
        self,
        recordId: str,
        data: Optional[_AttioUpdateCompanyRecordData] = None,
    ) -> Dict[str, Any]:
        """Updates one or more fields on an existing company record in Attio identified by its unique record ID. Use this tool to modify company details such as name, domain, industry, or custom attributes. Do not use this tool to create a new company — use attio_create_company_record instead. Only the fields provided in the request body will be updated (partial update). This operation modifies data in place.

        Args:
            recordId: Unique identifier for the record in Attio. (required)
            data: Main data object containing values to be sent to Attio.
        Returns:
            API response as a dictionary.
        """
        ...

    def attio_update_deal_record(
        self,
        recordId: str,
        data: Optional[_AttioUpdateDealRecordData] = None,
    ) -> Dict[str, Any]:
        """Updates one or more fields on an existing deal record in Attio identified by its unique record ID. Use this tool to modify deal details such as name, stage, value, or custom attributes. Do not use this tool to create a new deal — use attio_create_deal_record instead. Only the fields provided in the request body will be updated (partial update). This operation modifies data in place.

        Args:
            recordId: Unique identifier for the record in Attio. (required)
            data: Data object containing values to be sent to Attio.
        Returns:
            API response as a dictionary.
        """
        ...

    def attio_update_list(
        self,
        listId: str,
        data: Optional[_AttioUpdateListData] = None,
    ) -> Dict[str, Any]:
        """Updates the metadata or configuration of an existing list in Attio identified by its unique list ID. Use this tool to modify list properties such as name or description. Do not use this tool to add or remove entries within a list, or to create a new list — use attio_create_list instead. Only the fields provided in the request body will be updated (partial update). This operation modifies data in place.

        Args:
            listId: The unique identifier for the list in Attio. (required)
            data: The data payload containing workspace and user details.
        Returns:
            API response as a dictionary.
        """
        ...

    def attio_update_person_record(
        self,
        recordId: str,
        data: Optional[_AttioUpdatePersonRecordData] = None,
    ) -> Dict[str, Any]:
        """Updates one or more fields on an existing person (contact) record in Attio identified by its unique record ID. Use this tool to modify contact details such as name, email, phone, or custom attributes. Do not use this tool to create a new person — use attio_create_person_record instead. Only the fields provided in the request body will be updated (partial update). This operation modifies data in place.

        Args:
            recordId: Unique identifier for the record in Attio. (required)
            data: Main data object containing all record details.
        Returns:
            API response as a dictionary.
        """
        ...

    def attio_update_task(
        self,
        taskId: str,
        data: Optional[_AttioUpdateTaskData] = None,
    ) -> Dict[str, Any]:
        """Updates one or more fields on an existing task in Attio identified by its unique task ID. Use this tool to modify task details such as title, description, assignee, due date, or completion status. Do not use this tool to create a new task — use attio_create_task instead. Only the fields provided in the request body will be updated (partial update). This operation modifies data in place.

        Args:
            taskId: Unique identifier for the task. (required)
            data: Details of the task such as deadline, completion status, linked records, and assignees.
        Returns:
            API response as a dictionary.
        """
        ...

