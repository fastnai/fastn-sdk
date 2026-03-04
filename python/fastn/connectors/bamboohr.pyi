"""Fastn BambooHR connector — auto-generated type stubs.

Do not edit manually. Regenerate with `fastn connector sync`.
"""
from __future__ import annotations

from typing import Any, Dict, List, Optional, TypedDict


class _BamboohrCreateWebhookPostfields(TypedDict, total=False):
    dateOfBirth: str
    department: str
    division: str
    facebook: str
    firstName: str
    instagram: str
    jobTitle: str
    lastName: str
    linkedIn: str
    location: str
    mobilePhone: str
    pinterest: str
    preferredName: str
    twitterFeed: str
    workEmail: str
    workPhone: str
    workPhoneExtension: str

class BamboohrConnector:
    """BambooHR connector ().

    Provides 13 tools.
    """

    def bamboohr_create_application(
        self,
        email: str,
        firstName: str,
        jobId: str,
        lastName: str,
        address: Optional[str] = None,
        city: Optional[str] = None,
        collegeName: Optional[str] = None,
        country: Optional[str] = None,
        dateAvailable: Optional[str] = None,
        desiredSalary: Optional[str] = None,
        highestEducation: Optional[str] = None,
        phoneNumber: Optional[str] = None,
        referredBy: Optional[str] = None,
        source: Optional[str] = None,
        state: Optional[str] = None,
        zip: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Creates a new applicant tracking application (candidate profile) in BambooHR for a job opening. Use this when submitting a new candidate into the hiring pipeline. Do not use this to update an existing candidate or retrieve application data. This action creates a permanent application record in BambooHRs applicant tracking system.

        Args:
            email: Applicant's email address. (required)
            firstName: Applicant's first name. (required)
            jobId: ID of the job the applicant applied for. (required)
            lastName: Applicant's last name. (required)
            address: Applicant's address.
            city: Applicant's city.
            collegeName: Name of the college attended by the applicant.
            country: Applicant's country.
            dateAvailable: Date when the applicant is available to start.
            desiredSalary: Applicant's desired salary.
            highestEducation: Applicant's highest level of education.
            phoneNumber: Applicant's phone number.
            referredBy: Person who referred the applicant.
            source: Source where the applicant was found.
            state: Applicant's state.
            zip: Applicant's zip code.
        Returns:
            API response as a dictionary.
        """
        ...

    def bamboohr_create_employee(
        self,
        firstName: str,
        lastName: str,
        canUploadPhoto: Optional[int] = None,
        department: Optional[str] = None,
        displayName: Optional[str] = None,
        division: Optional[str] = None,
        facebook: Optional[str] = None,
        instagram: Optional[str] = None,
        jobTitle: Optional[str] = None,
        linkedIn: Optional[str] = None,
        location: Optional[str] = None,
        mobilePhone: Optional[str] = None,
        photoUploaded: Optional[bool] = None,
        photoUrl: Optional[str] = None,
        pinterest: Optional[str] = None,
        preferredName: Optional[str] = None,
        pronouns: Optional[str] = None,
        supervisor: Optional[str] = None,
        twitterFeed: Optional[str] = None,
        workEmail: Optional[str] = None,
        workPhone: Optional[str] = None,
        workPhoneExtension: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Creates a new employee record in BambooHR. Use this to onboard a new hire into the HR system. Do not use this to update an existing employee record. This action permanently adds an employee to the BambooHR system and may trigger downstream payroll or benefits workflows depending on your configuration.

        Args:
            firstName: The employee's first name. (required)
            lastName: The employee's last name. (required)
            canUploadPhoto: Indicates whether the employee can upload a photo (1 for yes, 0 for no).
            department: The employee's department.
            displayName: The employee's display name.
            division: The employee's division.
            facebook: The URL to the employee's Facebook profile.
            instagram: The URL to the employee's Instagram profile.
            jobTitle: The employee's job title.
            linkedIn: The URL to the employee's LinkedIn profile.
            location: The employee's location.
            mobilePhone: The employee's mobile phone number.
            photoUploaded: Indicates whether a photo has been uploaded for the employee.
            photoUrl: The URL of the employee's photo.
            pinterest: The URL to the employee's Pinterest profile.
            preferredName: The employee's preferred name.
            pronouns: The employee's pronouns.
            supervisor: The employee's supervisor.
            twitterFeed: The employee's Twitter feed URL.
            workEmail: The employee's work email address.
            workPhone: The employee's work phone number.
            workPhoneExtension: The employee's work phone extension.
        Returns:
            API response as a dictionary.
        """
        ...

    def bamboohr_create_employee_training_record(
        self,
        completed: str,
        credits: int,
        employeeID: str,
        hours: int,
        instructor: str,
        notes: str,
        type: int,
    ) -> Dict[str, Any]:
        """Adds a new training record to a specific employees profile in BambooHR, identified by their employee ID. Use this to log completed or assigned training activities for development tracking. Do not use this to update or delete existing training records. This action permanently appends a record to the employees training history.

        Args:
            completed: Date of completion. (required)
            credits: Number of credits. (required)
            employeeID: The ID of the employee. (required)
            hours: Number of hours. (required)
            instructor: Name of the instructor. (required)
            notes: Any additional notes. (required)
            type: Type of training. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def bamboohr_create_job_opening(
        self,
        applicationQuestionAddress: Optional[str] = None,
        applicationQuestionCollege: Optional[str] = None,
        applicationQuestionCoverLetter: Optional[str] = None,
        applicationQuestionDateAvailable: Optional[str] = None,
        applicationQuestionDesiredSalary: Optional[str] = None,
        applicationQuestionHighestEducation: Optional[str] = None,
        applicationQuestionLinkedinUrl: Optional[str] = None,
        applicationQuestionReferences: Optional[str] = None,
        applicationQuestionReferredBy: Optional[str] = None,
        applicationQuestionResume: Optional[str] = None,
        applicationQuestionWebsiteUrl: Optional[str] = None,
        compensation: Optional[str] = None,
        department: Optional[str] = None,
        employmentType: Optional[str] = None,
        hiringLead: Optional[str] = None,
        internalJobCode: Optional[str] = None,
        jobDescription: Optional[str] = None,
        jobStatus: Optional[str] = None,
        minimumExperience: Optional[str] = None,
        postingTitle: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Creates a new job opening in BambooHRs applicant tracking system. Use this to post a new position for hiring. Do not use this to update an existing job opening or list current openings. This action permanently adds a job opening record to the system.

        Args:
            applicationQuestionAddress: Details about the address question in the application.
            applicationQuestionCollege: Details about the college question in the application.
            applicationQuestionCoverLetter: Details about the cover letter question in the application.
            applicationQuestionDateAvailable: Details about the date available question in the application.
            applicationQuestionDesiredSalary: Details about the desired salary question in the application.
            applicationQuestionHighestEducation: Details about the highest education question in the application.
            applicationQuestionLinkedinUrl: Details about the LinkedIn URL question in the application.
            applicationQuestionReferences: Details about the references question in the application.
            applicationQuestionReferredBy: Details about the referred by question in the application.
            applicationQuestionResume: Details about the resume question in the application.
            applicationQuestionWebsiteUrl: Details about the website URL question in the application.
            compensation: Compensation details for the job.
            department: The department the job belongs to.
            employmentType: The type of employment (e.g., full-time, part-time).
            hiringLead: The name of the hiring lead.
            internalJobCode: The internal job code used within the company.
            jobDescription: The description of the job.
            jobStatus: The status of the job posting (e.g., open, closed).
            minimumExperience: The minimum experience required for the job.
            postingTitle: The title of the job posting.
        Returns:
            API response as a dictionary.
        """
        ...

    def bamboohr_create_webhook(
        self,
        includeCompanyDomain: str,
        monitorFields: List[Any],
        name: str,
        postFields: _BamboohrCreateWebhookPostfields,
        format: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Registers a new webhook in BambooHR to receive real-time HTTP notifications when specified employee or HR events occur. Use this to subscribe an external endpoint to BambooHR events. Do not use this to update or delete existing webhooks. This action creates a persistent subscription and will send repeated outbound HTTP requests to the registered URL until the webhook is removed.

        Args:
            includeCompanyDomain: Include the company domain in the response. (required)
            monitorFields: An array of fields to monitor. (required)
            name: The name of the entity. (required)
            postFields: Fields to be posted to BambooHR. (required)
            format: The format of the response data.
        Returns:
            API response as a dictionary.
        """
        ...

    def bamboohr_get_company_information(
        self,
    ) -> Dict[str, Any]:
        """Retrieves general company information from BambooHR, including the company name, address, phone number, and industry. Use this to access organization-level metadata. Do not use this to retrieve employee or payroll data. This is a read-only operation with no side effects.
        Returns:
            API response as a dictionary.
        """
        ...

    def bamboohr_get_employee_by_id(
        self,
        employeeId: str,
    ) -> Dict[str, Any]:
        """Retrieves detailed information for a single BambooHR employee using their unique employee ID. Use this when you need full profile data for a known employee. Do not use this to search employees by name or list all employees — use the directory or updated employees tools instead. This is a read-only operation with no side effects.

        Args:
            employeeId: The ID of the employee. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def bamboohr_list_company_eins(
        self,
    ) -> Dict[str, Any]:
        """Lists all Employer Identification Numbers (EINs) associated with the company in BambooHR. EINs are tax identifiers assigned by the IRS used for payroll and compliance purposes. Use this to retrieve EIN data for payroll processing or reporting. This is a read-only operation with no side effects.
        Returns:
            API response as a dictionary.
        """
        ...

    def bamboohr_list_employees_directory(
        self,
    ) -> Dict[str, Any]:
        """Lists the full employee directory for the organization from BambooHR, returning a summary of all active employees including names, departments, and contact details. Use this to browse or search the company roster. Do not use this to retrieve detailed data for a single employee — use bamboohr_get_employee_by_id instead. This is a read-only operation with no side effects.
        Returns:
            API response as a dictionary.
        """
        ...

    def bamboohr_list_job_applications(
        self,
    ) -> Dict[str, Any]:
        """Lists all job applications submitted in BambooHRs applicant tracking system, optionally filtered by job opening. Use this to review or audit candidates across open positions. Do not use this to retrieve a single application by ID or to create new applications. This is a read-only operation with no side effects.
        Returns:
            API response as a dictionary.
        """
        ...

    def bamboohr_list_job_summaries(
        self,
        sortBy: Optional[str] = None,
        sortOrder: Optional[str] = None,
        statusGroups: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Lists summary information for all job openings currently tracked in BambooHRs applicant tracking system, including job titles and status. Use this to get an overview of active and inactive positions. Do not use this to retrieve full job details or applications. This is a read-only operation with no side effects.

        Args:
            sortBy: The field to sort the results by.
            sortOrder: The order in which results should be sorted (e.g., asc, desc).
            statusGroups: Filter results by specified status groups.
        Returns:
            API response as a dictionary.
        """
        ...

    def bamboohr_list_updated_employees(
        self,
        since: Optional[str] = None,
        type: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Lists all BambooHR employees whose records have been modified since a specified timestamp. Use this to poll for recent employee data changes and sync downstream systems. Does not return employees with no recent updates. This is a read-only operation with no side effects.

        Args:
            since: Filter results to include only data modified since this date.
            type: Specifies the type of request.
        Returns:
            API response as a dictionary.
        """
        ...

    def bamboohr_update_employee(
        self,
        firstName: str,
        lastName: str,
        canUploadPhoto: Optional[int] = None,
        department: Optional[str] = None,
        displayName: Optional[str] = None,
        division: Optional[str] = None,
        employeeId: Optional[str] = None,
        facebook: Optional[str] = None,
        instagram: Optional[str] = None,
        jobTitle: Optional[str] = None,
        linkedIn: Optional[str] = None,
        location: Optional[str] = None,
        mobilePhone: Optional[str] = None,
        photoUploaded: Optional[bool] = None,
        photoUrl: Optional[str] = None,
        pinterest: Optional[str] = None,
        preferredName: Optional[str] = None,
        pronouns: Optional[str] = None,
        supervisor: Optional[str] = None,
        twitterFeed: Optional[str] = None,
        workEmail: Optional[str] = None,
        workPhone: Optional[str] = None,
        workPhoneExtension: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Updates one or more fields on an existing employee record in BambooHR, identified by their employee ID. Use this to modify personal, job, or contact information for an employee. Do not use this to create a new employee or retrieve employee data. Changes are applied immediately and overwrite existing field values.

        Args:
            firstName: The employee's first name. (required)
            lastName: The employee's last name. (required)
            canUploadPhoto: Indicates if the employee can upload a photo (1 for yes, 0 for no).
            department: The employee's department.
            displayName: The employee's display name.
            division: The employee's division.
            employeeId: The ID of the employee.
            facebook: The employee's Facebook profile URL.
            instagram: The employee's Instagram profile URL.
            jobTitle: The employee's job title.
            linkedIn: The employee's LinkedIn profile URL.
            location: The employee's location.
            mobilePhone: The employee's mobile phone number.
            photoUploaded: Indicates if a photo has been uploaded for the employee.
            photoUrl: The URL of the employee's photo.
            pinterest: The employee's Pinterest profile URL.
            preferredName: The employee's preferred name.
            pronouns: The employee's pronouns.
            supervisor: The employee's supervisor.
            twitterFeed: The employee's Twitter feed URL.
            workEmail: The employee's work email address.
            workPhone: The employee's work phone number.
            workPhoneExtension: The employee's work phone extension.
        Returns:
            API response as a dictionary.
        """
        ...

