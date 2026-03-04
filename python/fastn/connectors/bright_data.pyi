"""Fastn Bright Data connector — auto-generated type stubs.

Do not edit manually. Regenerate with `fastn connector sync`.
"""
from __future__ import annotations

from typing import Any, Dict, List, Optional, TypedDict


class _BrightDataCreateZonePlan(TypedDict, total=False):
    asn: str
    bandwidth: str
    city: str
    country: str
    country_city: str
    custom_headers: bool
    domain_whitelist: str
    ip_alloc_preset: str
    ips: int
    ips_type: str
    mobile: str
    pool_ip_type: str
    serp: str
    solve_captcha_disable: bool
    type: str
    ub_premium: bool
    vip: str
    vip_country: str
    vip_country_city: str
    vips: str
    vips_type: str

class _BrightDataCreateZoneZone(TypedDict, total=False):
    name: str
    type: str

class BrightDataConnector:
    """Bright Data connector ().

    Provides 20 tools.
    """

    def bright_data_add_allowlist_ips(
        self,
        ip: str,
        zone: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Adds one or more IP addresses to the allowlist (whitelist) for a specified Bright Data proxy zone, permitting those IPs to route traffic through the zone. Use this tool when you need to grant access to new client IPs. Do not use this tool to view the current allowlist — use bright_data_list_allowlist_ips for that. This operation modifies zone security settings and takes effect immediately.

        Args:
            ip: The IP address to retrieve data for. (required)
            zone: The BrightData zone to target.
        Returns:
            API response as a dictionary.
        """
        ...

    def bright_data_add_static_ips(
        self,
        count: int,
        customer: str,
        zone: str,
        country: Optional[str] = None,
        country_city: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Allocates and adds static IP addresses to a specified Bright Data proxy zone. Use this tool when you need dedicated, persistent IPs assigned to a zone for stable outbound identity. Do not use this tool to manage the IP allowlist for zone access control — use bright_data_add_allowlist_ips for that. Adding static IPs is a billable action and the IPs are assigned immediately upon calling this tool.

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

    def bright_data_create_zone(
        self,
        plan: _BrightDataCreateZonePlan,
        zone: _BrightDataCreateZoneZone,
    ) -> Dict[str, Any]:
        """Creates a new proxy zone in the Bright Data network with the specified configuration (e.g. zone type, country targeting, plan). Use this tool when you need to provision a new proxy zone for routing traffic or scraping jobs. Do not use this tool to retrieve existing zones — use bright_data_list_available_zones or bright_data_list_active_zones for that. Zone creation is a billable action and may be difficult to reverse — confirm zone parameters before calling this tool.

        Args:
            plan: Specifies the proxy plan details. (required)
            zone: Specifies the proxy zone. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def bright_data_download_snapshot_content(
        self,
        snapshotID: str,
        format: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Downloads the full content of a completed scraping job snapshot, identified by its snapshot ID. Use this tool after triggering a scraping job and confirming the snapshot is ready, to retrieve the structured output data. Do not use this tool to trigger a new scraping job — use the appropriate platform-specific trigger tool for that. Large snapshots may take time to transfer. This is a read-only operation with no side effects.

        Args:
            snapshotID: The ID of the snapshot to retrieve. (required)
            format: Specifies the desired output format (e.g., JSON, CSV).
        Returns:
            API response as a dictionary.
        """
        ...

    def bright_data_get_account(
        self,
    ) -> Dict[str, Any]:
        """Retrieves account status and details for the authenticated Bright Data customer, including subscription plan and service usage information. Use this tool when you need a high-level overview of the accounts current state. Do not use this tool to check account balance — use bright_data_get_total_balance for that. This is a read-only operation with no side effects.
        Returns:
            API response as a dictionary.
        """
        ...

    def bright_data_get_country_service_status(
        self,
        NETWORK_TYPE: str,
    ) -> Dict[str, Any]:
        """Retrieves the operational status of Bright Data proxy network services for a specified network type and country. Use this tool when you need to verify whether a particular proxy network type (e.g. residential, datacenter) is available and functioning in a target country before routing traffic through it. Do not use this tool to list available countries — use bright_data_list_countries for that. This is a read-only operation with no side effects.

        Args:
            NETWORK_TYPE: Specifies the type of network to use. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def bright_data_get_total_balance(
        self,
    ) -> Dict[str, Any]:
        """Retrieves the current account balance for the authenticated Bright Data customer. Use this tool when you need to check available funds before triggering scraping jobs or purchasing additional capacity. Do not use this tool to retrieve account subscription details or usage statistics — use bright_data_get_account for that. This is a read-only operation with no side effects.
        Returns:
            API response as a dictionary.
        """
        ...

    def bright_data_list_active_zones(
        self,
    ) -> Dict[str, Any]:
        """Retrieves a list of all currently active proxy zones configured under the authenticated Bright Data account. Use this tool when you need to see which zones are live and available for routing traffic. Do not use this tool to list all available zones regardless of status — use bright_data_list_available_zones for that. This is a read-only operation with no side effects.
        Returns:
            API response as a dictionary.
        """
        ...

    def bright_data_list_allowlist_ips(
        self,
        zones: str,
    ) -> Dict[str, Any]:
        """Retrieves the list of IP addresses currently on the allowlist (whitelist) for a Bright Data zone. Use this tool when you need to audit or review which IP addresses are permitted to access the proxy zone. Do not use this tool to add IPs to the allowlist — use bright_data_add_allowlist_ips for that. This is a read-only operation with no side effects.

        Args:
            zones: Specifies the zones for the BrightData API request. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def bright_data_list_available_zones(
        self,
        zone: str,
    ) -> Dict[str, Any]:
        """Retrieves a list of all available proxy zones and their associated VIP route configurations in the Bright Data network. Use this tool when you need to discover zones that can be created or used, regardless of their active status. Do not use this tool to list only currently active zones — use bright_data_list_active_zones for that. This is a read-only operation with no side effects.

        Args:
            zone: Specifies the zone for the request. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def bright_data_list_countries(
        self,
    ) -> Dict[str, Any]:
        """Retrieves the full list of countries supported by the Bright Data proxy network for geo-targeting. Use this tool when you need to identify valid country codes or names to use in zone configuration, city lookups, or service status checks. Do not use this tool to retrieve city-level targeting options — use bright_data_list_country_cities for that. This is a read-only operation with no side effects.
        Returns:
            API response as a dictionary.
        """
        ...

    def bright_data_list_country_cities(
        self,
        country: str,
    ) -> Dict[str, Any]:
        """Retrieves a list of cities available for targeting within a specified country on the Bright Data network. Use this tool when you need to configure city-level geo-targeting for proxy zones or scraping jobs. Do not use this tool to retrieve country-level data — use bright_data_list_countries for that. This is a read-only operation with no side effects.

        Args:
            country: The target country for the data request. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def bright_data_list_datacenters_and_isp_count(
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
        """Retrieves a list of available Bright Data data centers along with the count of ISP IPs available in each, for a specified zone or region. Use this tool when you need to evaluate capacity before configuring a datacenter or ISP proxy zone. Do not use this tool to add IPs to a zone — use bright_data_add_static_ips for that. This is a read-only operation with no side effects.

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

    def bright_data_set_domain_permissions(
        self,
        type: str,
        zone: str,
        domain: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Configures domain-level access permissions for a Bright Data proxy zone, either allowing or denying traffic to specified domains based on the supplied settings. Use this tool when you need to restrict or explicitly permit which target domains can be accessed through a zone. Do not use this tool to manage IP-level access — use bright_data_add_allowlist_ips for that. This operation modifies zone security settings and takes effect immediately.

        Args:
            type: The type of data to be retrieved. (required)
            zone: The geographical zone for the data request. (required)
            domain: The domain for the data request.
        Returns:
            API response as a dictionary.
        """
        ...

    def bright_data_trigger_chatgpt_scrape(
        self,
        custom_output_fields: str,
        dataset_id: str,
        format: str,
        body: Optional[List[Any]] = None,
    ) -> Dict[str, Any]:
        """Triggers an asynchronous scraping job to collect data from ChatGPT (chat.openai.com) based on specified parameters. Use this tool when you need to extract publicly accessible ChatGPT interface content or responses at scale. Do not use this tool for Perplexity, LinkedIn, TikTok, or Instagram scraping — use the platform-specific trigger tools for those. This tool initiates a job and returns a snapshot or job ID; it does not return scraped data immediately. Note: triggers a billable scraping job on Bright Data.

        Args:
            custom_output_fields: Specify custom fields to be included in the output. (required)
            dataset_id: The ID of the dataset to query. (required)
            format: The desired format for the output data (e.g., JSON, CSV). (required)
            body: 
        Returns:
            API response as a dictionary.
        """
        ...

    def bright_data_trigger_discover_instagram_posts_by_username(
        self,
        dataset_id: str,
        body: Optional[List[Any]] = None,
        discover_by: Optional[str] = None,
        include_errors: Optional[str] = None,
        type: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Triggers an asynchronous job to discover and collect Instagram posts published by a specific user, identified by their Instagram username. Use this tool when you need post content, image metadata, captions, or engagement statistics for an Instagram account. Do not use this tool for TikTok or other social platforms — use bright_data_trigger_discover_tiktok_posts_by_username for TikTok. This tool initiates a job and returns a snapshot or job ID; it does not return scraped data immediately. Note: triggers a billable scraping job on Bright Data.

        Args:
            dataset_id: The ID of the dataset to access. (required)
            body: 
            discover_by: Method for discovering data within the dataset.
            include_errors: Whether to include error records in the response.
            type: Specifies the type of data to retrieve.
        Returns:
            API response as a dictionary.
        """
        ...

    def bright_data_trigger_discover_linkedin_posts(
        self,
        body: List[Any],
        dataset_id: str,
        discover_by: Optional[str] = None,
        format: Optional[str] = None,
        include_errors: Optional[str] = None,
        type: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Triggers an asynchronous job to discover and collect LinkedIn posts authored by a specified user, identified by their profile URL or username. Use this tool when you need post content, engagement metrics, or activity history for a LinkedIn user. Do not use this tool to scrape LinkedIn profile details — use bright_data_trigger_linkedin_profiles_scrape for that. This tool initiates a job and returns a snapshot or job ID; it does not return scraped data immediately. Note: triggers a billable scraping job on Bright Data.

        Args:
            body:  (required)
            dataset_id: The ID of the dataset to query. (required)
            discover_by: Specifies the method used to discover data.
            format: The desired format for the returned data.
            include_errors: Specifies whether to include error details in the response.
            type: The type of data to retrieve.
        Returns:
            API response as a dictionary.
        """
        ...

    def bright_data_trigger_discover_tiktok_posts_by_username(
        self,
        dataset_id: str,
        body: Optional[List[Any]] = None,
        include_errors: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Triggers an asynchronous job to discover and collect TikTok posts published by a specific user, identified by their TikTok username. Use this tool when you need post content, video metadata, or engagement statistics for a TikTok account. Do not use this tool for Instagram or other social platforms — use bright_data_trigger_discover_instagram_posts_by_username for Instagram. This tool initiates a job and returns a snapshot or job ID; it does not return scraped data immediately. Note: triggers a billable scraping job on Bright Data.

        Args:
            dataset_id: The ID of the dataset to query. (required)
            body: 
            include_errors: Specifies whether to include error details in the response.
        Returns:
            API response as a dictionary.
        """
        ...

    def bright_data_trigger_linkedin_profiles_scrape(
        self,
        dataset_id: str,
        body: Optional[List[Any]] = None,
        format: Optional[str] = None,
        include_errors: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Triggers an asynchronous scraping job to collect LinkedIn profile data for one or more specified profiles. Use this tool when you need structured data from LinkedIn profiles (e.g. name, title, company, connections). Do not use this tool to retrieve posts or activity — use bright_data_trigger_discover_linkedin_posts for that. This tool initiates a job and returns a snapshot or job ID; it does not return scraped data immediately. Note: triggers a billable scraping job on Bright Data.

        Args:
            dataset_id: The ID of the dataset to query. (required)
            body: 
            format: The desired format for the returned data (e.g., JSON, CSV).
            include_errors: Whether to include error details in the response.
        Returns:
            API response as a dictionary.
        """
        ...

    def bright_data_trigger_perplexity_scrape(
        self,
        body: List[Any],
        dataset_id: str,
        custom_output_fields: Optional[str] = None,
        format: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Triggers an asynchronous scraping job to collect data from Perplexity.ai based on configured query criteria. Use this tool when you need to extract search results or AI-generated answer content from Perplexity. Do not use this tool for LinkedIn, TikTok, Instagram, or ChatGPT scraping — use the platform-specific trigger tools for those. This tool initiates a job and returns a snapshot or job ID; it does not return scraped data immediately. Note: triggers a billable scraping job on Bright Data.

        Args:
            body:  (required)
            dataset_id: The ID of the dataset to query. (required)
            custom_output_fields: Specify custom fields to be included in the output.
            format: The desired format for the output data (e.g., JSON, CSV).
        Returns:
            API response as a dictionary.
        """
        ...

