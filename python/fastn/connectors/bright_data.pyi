"""Fastn Bright Data connector — auto-generated type stubs.

Do not edit manually. Regenerate with `fastn connector sync`.
"""
from __future__ import annotations

from typing import Any, Dict, List, Optional


class BrightDataConnector:
    """Bright Data connector ().

    Provides 20 tools.
    """

    def add_static_ips(
        self,
        count: int,
        customer: str,
        zone: str,
        country: Optional[str] = None,
        country_city: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Adds static IP addresses in the networking settings of the specified system.

        Args:
            count: The number of data points to retrieve. (required)
            customer: The identifier for the customer making the request. (required)
            zone: The specific zone or region within the country and city. (required)
            country: The country for which to retrieve data.
            country_city: The city within the specified country.
        Returns:
            API response as a dictionary.
        """
        ...

    def add_zone(
        self,
        plan: Dict[str, Any],
        zone: Dict[str, Any],
    ) -> Dict[str, Any]:
        """Creates a new zone within the geographical or logical structure of the given infrastructure.

        Args:
            plan: Specifies the proxy plan details. (required)
            zone: Specifies the proxy zone. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def allow_or_deny_domains(
        self,
        type: str,
        zone: str,
        domain: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Allows or denies access to specified domains based on the settings of the current security protocol.

        Args:
            type: The type of data to be retrieved. (required)
            zone: The geographical zone for the data request. (required)
            domain: The domain for the data request.
        Returns:
            API response as a dictionary.
        """
        ...

    def allowlist_ips(
        self,
        ip: str,
        zone: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Permits specified IP addresses on the allowlist to access the network, enhancing security measures.

        Args:
            ip: The IP address to retrieve data for. (required)
            zone: The BrightData zone to target.
        Returns:
            API response as a dictionary.
        """
        ...

    def available_data_centers_and_isp_count(
        self,
        plancity: Optional[str] = None,
        plancountry: Optional[str] = None,
        plancountry_city: Optional[str] = None,
        plandomain_whitelist: Optional[str] = None,
        plangeo_dbdbip: Optional[str] = None,
        plangeo_dbgoogle: Optional[str] = None,
        plangeo_dbip2location: Optional[str] = None,
        plangeo_dbipcn: Optional[str] = None,
        plangeo_dbmaxmind: Optional[str] = None,
        planips_type: Optional[str] = None,
        planpool_ip_type: Optional[str] = None,
        zone: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Retrieves the list of data centers along with the count of available ISPs in the specified region.

        Args:
            plancity: City for plan selection.
            plancountry: Country for plan selection.
            plancountry_city: Country and city for plan selection.
            plandomain_whitelist: Whitelist of domains for plan selection.
            plangeo_dbdbip: Geolocation database DBIP for plan selection.
            plangeo_dbgoogle: Geolocation database Google for plan selection.
            plangeo_dbip2location: Geolocation database IP2Location for plan selection.
            plangeo_dbipcn: Geolocation database IPCN for plan selection.
            plangeo_dbmaxmind: Geolocation database MaxMind for plan selection.
            planips_type: Type of IPs for plan selection.
            planpool_ip_type: Type of pool IPs for plan selection.
            zone: Geographic zone for plan selection.
        Returns:
            API response as a dictionary.
        """
        ...

    def available_zones(
        self,
        zone: str,
    ) -> Dict[str, Any]:
        """Fetches a list of available zones within the defined infrastructure for deployment.

        Args:
            zone: Specifies the zone for the request. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def download_snapshot_content(
        self,
        format: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Downloads the contents of a specified snapshot for backup or recovery purposes.

        Args:
            format: Specifies the desired output format (e.g., JSON, CSV).
        Returns:
            API response as a dictionary.
        """
        ...

    def get_account(
        self,
    ) -> Dict[str, Any]:
        """Fetches account information, including details about subscription and usage within the specified service.
        Returns:
            API response as a dictionary.
        """
        ...

    def get_active_zones(
        self,
    ) -> Dict[str, Any]:
        """Retrieves a list of currently active zones within the specified infrastructure.
        Returns:
            API response as a dictionary.
        """
        ...

    def get_allow_list_ips(
        self,
        zones: str,
    ) -> Dict[str, Any]:
        """Obtains the currently configured allowlist of IP addresses for security verification.

        Args:
            zones: Specifies the zones for the BrightData API request. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def get_countries(
        self,
    ) -> Dict[str, Any]:
        """Gathers a list of countries, providing information relevant to the geographical context of the application.
        Returns:
            API response as a dictionary.
        """
        ...

    def get_country_cities(
        self,
        country: str,
    ) -> Dict[str, Any]:
        """Retrieves the cities within a specific country, useful for regional targeting or analysis.

        Args:
            country: The target country for the data request. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def get_country_service_status(
        self,
        NETWORK_TYPE: str,
    ) -> Dict[str, Any]:
        """Fetches the operational status of services available in the specified country.

        Args:
            NETWORK_TYPE: Specifies the type of network to use. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def get_total_balance(
        self,
    ) -> Dict[str, Any]:
        """Retrieves the total balance of the account, reflecting current financial standing within the service.
        Returns:
            API response as a dictionary.
        """
        ...

    def instagram_post_discover_by_username(
        self,
        dataset_id: str,
        discover_by: Optional[str] = None,
        include_errors: Optional[str] = None,
        type: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Discovers Instagram posts made by a user based on their username within the Instagram platform.

        Args:
            dataset_id: The ID of the dataset to access. (required)
            discover_by: Method for discovering data within the dataset.
            include_errors: Whether to include error records in the response.
            type: Specifies the type of data to retrieve.
        Returns:
            API response as a dictionary.
        """
        ...

    def tiktok_post_discover_by_username(
        self,
        dataset_id: str,
        include_errors: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Discovers TikTok posts made by a user based on their username within the TikTok platform.

        Args:
            dataset_id: The ID of the dataset to query. (required)
            include_errors: Specifies whether to include error details in the response.
        Returns:
            API response as a dictionary.
        """
        ...

    def trigger_chat_gpt_scrapper(
        self,
        custom_output_fields: str,
        dataset_id: str,
        format: str,
    ) -> Dict[str, Any]:
        """Triggers the ChatGPT scraper to collect and process relevant data as per the specified parameters.

        Args:
            custom_output_fields: Specify custom fields to be included in the output. (required)
            dataset_id: The ID of the dataset to query. (required)
            format: The desired format for the output data (e.g., JSON, CSV). (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def trigger_discover_linkdin_post(
        self,
        dataset_id: str,
        discover_by: Optional[str] = None,
        format: Optional[str] = None,
        include_errors: Optional[str] = None,
        type: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Initiates the discovery of LinkedIn posts for a given user, based on their profile.

        Args:
            dataset_id: The ID of the dataset to query. (required)
            discover_by: Specifies the method used to discover data.
            format: The desired format for the returned data.
            include_errors: Specifies whether to include error details in the response.
            type: The type of data to retrieve.
        Returns:
            API response as a dictionary.
        """
        ...

    def trigger_perplexity_scraping(
        self,
        dataset_id: str,
        custom_output_fields: Optional[str] = None,
        format: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Activates the Perplexity scraping tool to gather information based on the configured criteria.

        Args:
            dataset_id: The ID of the dataset to query. (required)
            custom_output_fields: Specify custom fields to be included in the output.
            format: The desired format for the output data (e.g., JSON, CSV).
        Returns:
            API response as a dictionary.
        """
        ...

    def triggger_linkdin_profiles(
        self,
        dataset_id: str,
        format: Optional[str] = None,
        include_errors: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Triggers the scraping of LinkedIn profiles, fetching data according to specified attributes.

        Args:
            dataset_id: The ID of the dataset to query. (required)
            format: The desired format for the returned data (e.g., JSON, CSV).
            include_errors: Whether to include error details in the response.
        Returns:
            API response as a dictionary.
        """
        ...

