"""Fastn BambooHR connector — auto-generated type stubs.

Do not edit manually. Regenerate with `fastn connector sync`.
"""
from __future__ import annotations

from typing import Any, Dict, List, Optional


class BamboohrConnector:
    """BambooHR connector ().

    Provides 13 tools.
    """

    def add_employee_training_rec(
        self,
        completed: str,
        credits: int,
        hours: int,
        instructor: str,
        notes: str,
        type: int,
    ) -> Dict[str, Any]:
        """Adds a training record for an employee to track their development and skills using the employee training connector.

        Args:
            completed: Date of completion. (required)
            credits: Number of credits. (required)
            hours: Number of hours. (required)
            instructor: Name of the instructor. (required)
            notes: Any additional notes. (required)
            type: Type of training. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def add_webhook(
        self,
        includeCompanyDomain: str,
        monitorFields: List[Any],
        name: str,
        postFields: Dict[str, Any],
        format: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Registers a new webhook for real-time updates and notifications using the webhook management connector.

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

    def create_candidate(
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
        """Creates a new candidate profile in the system for job applications using the candidate management connector.

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

    def create_employee(
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
        """Creates a new employee record in the system utilizing the employee management connector.

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

    def create_job_opening(
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
        """Creates a new job opening within the company's job listings using the job management connector.

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

    def get_all_updated_employees(
        self,
        since: Optional[str] = None,
        type: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Retrieves a list of all employees whose information has been updated recently through the employee database connector.

        Args:
            since: Filter results to include only data modified since this date.
            type: Specifies the type of request.
        Returns:
            API response as a dictionary.
        """
        ...

    def get_company_ei_ns(
        self,
    ) -> Dict[str, Any]:
        """Obtains the Employer Identification Numbers (EINs) associated with the company using the company EINs connector.
        Returns:
            API response as a dictionary.
        """
        ...

    def get_company_information(
        self,
    ) -> Dict[str, Any]:
        """Fetches comprehensive information about the company, including its name, address, and industry, through the company information connector.
        Returns:
            API response as a dictionary.
        """
        ...

    def get_employee_by_id(
        self,
        employeeId: str,
    ) -> Dict[str, Any]:
        """Fetches detailed information about a specific employee based on their unique ID using the employee management connector.

        Args:
            employeeId: The ID of the employee. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def get_employees_directory(
        self,
    ) -> Dict[str, Any]:
        """Retrieves the directory of all employees within the organization using the relevant HR connector.
        Returns:
            API response as a dictionary.
        """
        ...

    def get_job_applications(
        self,
    ) -> Dict[str, Any]:
        """Fetches all job applications submitted for a specific job opening using the job application management connector.
        Returns:
            API response as a dictionary.
        """
        ...

    def get_job_summaries(
        self,
        sortBy: Optional[str] = None,
        sortOrder: Optional[str] = None,
        statusGroups: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Retrieves summaries of all job listings currently available in the company through the job management connector.

        Args:
            sortBy: The field to sort the results by.
            sortOrder: The order in which results should be sorted (e.g., asc, desc).
            statusGroups: Filter results by specified status groups.
        Returns:
            API response as a dictionary.
        """
        ...

    def update_employee(
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
        """Updates the details of an existing employee within the organization using the employee management connector.

        Args:
            firstName: The employee's first name. (required)
            lastName: The employee's last name. (required)
            canUploadPhoto: Indicates if the employee can upload a photo (1 for yes, 0 for no).
            department: The employee's department.
            displayName: The employee's display name.
            division: The employee's division.
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

