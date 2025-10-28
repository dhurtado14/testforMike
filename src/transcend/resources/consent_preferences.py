# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import typing_extensions
from typing import Union
from datetime import datetime

import httpx

from ..types import consent_preference_deprecated_create_params
from .._types import Body, Omit, Query, Headers, NotGiven, SequenceNotStr, omit, not_given
from .._utils import maybe_transform, strip_not_given, async_maybe_transform
from .._compat import cached_property
from .._resource import SyncAPIResource, AsyncAPIResource
from .._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from .._base_client import make_request_options
from ..types.consent_preference_deprecated_create_response import ConsentPreferenceDeprecatedCreateResponse

__all__ = ["ConsentPreferencesResource", "AsyncConsentPreferencesResource"]


class ConsentPreferencesResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> ConsentPreferencesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/transcend-python#accessing-raw-response-data-eg-headers
        """
        return ConsentPreferencesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ConsentPreferencesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/transcend-python#with_streaming_response
        """
        return ConsentPreferencesResourceWithStreamingResponse(self)

    @typing_extensions.deprecated("deprecated")
    def deprecated_create(
        self,
        *,
        partition: str,
        identifiers: SequenceNotStr[str] | Omit = omit,
        limit: float | Omit = omit,
        start_key: consent_preference_deprecated_create_params.StartKey | Omit = omit,
        timestamp_after: Union[str, datetime] | Omit = omit,
        timestamp_before: Union[str, datetime] | Omit = omit,
        updated_after: Union[str, datetime] | Omit = omit,
        updated_before: Union[str, datetime] | Omit = omit,
        x_sombra_authorization: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ConsentPreferenceDeprecatedCreateResponse:
        """
        **Deprecated:** This endpoint has been replaced by the new
        [Query user preferences](</docs/api-reference/POST/v1/preferences/(partition)/query>)
        endpoint.

        ## Migration Guide

        The new endpoint provides enhanced functionality and a more flexible structure.
        Here are the key differences and migration steps:

        ### URL Structure

        - **Old:** `POST /v1/consent-preferences`
        - **New:** `POST /v1/preferences/{partition}/query`

        ### Request Body Changes

        1. **Partition**: Move from request body to URL path
        2. **Filters**: Wrap filtering parameters in a `filter` object
        3. **Identifiers**: Change from simple strings to objects with `name` and
           `value` properties
        4. **Pagination**: Use `cursor` instead of `startKey`

        ### Example Migration

        **Old Request:**

        ```json
        {
          "partition": "ea3a0845-694e-4820-9d51-50c7d0a23467",
          "identifiers": ["user@example.com"],
          "timestampAfter": "2023-06-26T21:39:31.677769"
        }
        ```

        **New Request:**

        ```json
        // POST /v1/preferences/ea3a0845-694e-4820-9d51-50c7d0a23467/query
        {
          "filter": {
            "identifiers": [{ "name": "email", "value": "user@example.com" }]
          }
        }
        ```

        ### Response Format Changes

        - **Identifiers**: Changed from single `userId` string to array of `identifiers`
          objects
        - **Purposes**: Enhanced from simple object to detailed array with nested
          preferences
        - **Pagination**: Uses `cursor` instead of `lastKey`
        - **Additional Fields**: New `consentManagement`, `system`, and `metadata`
          fields provide more context

        ### Key Benefits of the New Endpoint

        - Support for multiple identifier types (email, phone, etc.)
        - More granular preference choices (boolean, select, multi-select)
        - Enhanced filtering capabilities
        - Improved response structure with additional metadata
        - Simplified pagination with cursor-based approach

        Batch-lookup consent preferences for multiple users.

        Args:
          partition: The ID of the partition in the Preference Store.

          identifiers: The list of identifiers, each corresponding to a unique user. Cannot be used in
              combination with timestampBefore and timestampAfter filters.

          limit: Max number of users to return. Defaults to 50.

          start_key: The key after which to start looking for consent preferences. Used for cursor
              pagination.

          timestamp_after: Filter for consent preferences set after a given timestamp. Cannot be used in
              combination with identifiers or updated filters.

          timestamp_before: Filter for consent preferences set before a given timestamp. Defaults to now.
              Cannot be used in combination with identifiers or updated filters.

          updated_after: Filter for consent preferences updated after a given timestamp. Cannot be used
              in combination with identifiers or timestamp filter. If you are self-hosting
              Sombra, your Sombra version must be >=7.236.0 to query by updatedAfter.

          updated_before: Filter for consent preferences updated before a given timestamp. Defaults to
              now. Cannot be used in combination with identifiers or timestamp filter. If you
              are self-hosting Sombra, your Sombra version must be >=7.236.0 to query by
              updatedBefore.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {**strip_not_given({"x-sombra-authorization": x_sombra_authorization}), **(extra_headers or {})}
        return self._post(
            "/v1/consent-preferences",
            body=maybe_transform(
                {
                    "partition": partition,
                    "identifiers": identifiers,
                    "limit": limit,
                    "start_key": start_key,
                    "timestamp_after": timestamp_after,
                    "timestamp_before": timestamp_before,
                    "updated_after": updated_after,
                    "updated_before": updated_before,
                },
                consent_preference_deprecated_create_params.ConsentPreferenceDeprecatedCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ConsentPreferenceDeprecatedCreateResponse,
        )


class AsyncConsentPreferencesResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncConsentPreferencesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/transcend-python#accessing-raw-response-data-eg-headers
        """
        return AsyncConsentPreferencesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncConsentPreferencesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/transcend-python#with_streaming_response
        """
        return AsyncConsentPreferencesResourceWithStreamingResponse(self)

    @typing_extensions.deprecated("deprecated")
    async def deprecated_create(
        self,
        *,
        partition: str,
        identifiers: SequenceNotStr[str] | Omit = omit,
        limit: float | Omit = omit,
        start_key: consent_preference_deprecated_create_params.StartKey | Omit = omit,
        timestamp_after: Union[str, datetime] | Omit = omit,
        timestamp_before: Union[str, datetime] | Omit = omit,
        updated_after: Union[str, datetime] | Omit = omit,
        updated_before: Union[str, datetime] | Omit = omit,
        x_sombra_authorization: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ConsentPreferenceDeprecatedCreateResponse:
        """
        **Deprecated:** This endpoint has been replaced by the new
        [Query user preferences](</docs/api-reference/POST/v1/preferences/(partition)/query>)
        endpoint.

        ## Migration Guide

        The new endpoint provides enhanced functionality and a more flexible structure.
        Here are the key differences and migration steps:

        ### URL Structure

        - **Old:** `POST /v1/consent-preferences`
        - **New:** `POST /v1/preferences/{partition}/query`

        ### Request Body Changes

        1. **Partition**: Move from request body to URL path
        2. **Filters**: Wrap filtering parameters in a `filter` object
        3. **Identifiers**: Change from simple strings to objects with `name` and
           `value` properties
        4. **Pagination**: Use `cursor` instead of `startKey`

        ### Example Migration

        **Old Request:**

        ```json
        {
          "partition": "ea3a0845-694e-4820-9d51-50c7d0a23467",
          "identifiers": ["user@example.com"],
          "timestampAfter": "2023-06-26T21:39:31.677769"
        }
        ```

        **New Request:**

        ```json
        // POST /v1/preferences/ea3a0845-694e-4820-9d51-50c7d0a23467/query
        {
          "filter": {
            "identifiers": [{ "name": "email", "value": "user@example.com" }]
          }
        }
        ```

        ### Response Format Changes

        - **Identifiers**: Changed from single `userId` string to array of `identifiers`
          objects
        - **Purposes**: Enhanced from simple object to detailed array with nested
          preferences
        - **Pagination**: Uses `cursor` instead of `lastKey`
        - **Additional Fields**: New `consentManagement`, `system`, and `metadata`
          fields provide more context

        ### Key Benefits of the New Endpoint

        - Support for multiple identifier types (email, phone, etc.)
        - More granular preference choices (boolean, select, multi-select)
        - Enhanced filtering capabilities
        - Improved response structure with additional metadata
        - Simplified pagination with cursor-based approach

        Batch-lookup consent preferences for multiple users.

        Args:
          partition: The ID of the partition in the Preference Store.

          identifiers: The list of identifiers, each corresponding to a unique user. Cannot be used in
              combination with timestampBefore and timestampAfter filters.

          limit: Max number of users to return. Defaults to 50.

          start_key: The key after which to start looking for consent preferences. Used for cursor
              pagination.

          timestamp_after: Filter for consent preferences set after a given timestamp. Cannot be used in
              combination with identifiers or updated filters.

          timestamp_before: Filter for consent preferences set before a given timestamp. Defaults to now.
              Cannot be used in combination with identifiers or updated filters.

          updated_after: Filter for consent preferences updated after a given timestamp. Cannot be used
              in combination with identifiers or timestamp filter. If you are self-hosting
              Sombra, your Sombra version must be >=7.236.0 to query by updatedAfter.

          updated_before: Filter for consent preferences updated before a given timestamp. Defaults to
              now. Cannot be used in combination with identifiers or timestamp filter. If you
              are self-hosting Sombra, your Sombra version must be >=7.236.0 to query by
              updatedBefore.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {**strip_not_given({"x-sombra-authorization": x_sombra_authorization}), **(extra_headers or {})}
        return await self._post(
            "/v1/consent-preferences",
            body=await async_maybe_transform(
                {
                    "partition": partition,
                    "identifiers": identifiers,
                    "limit": limit,
                    "start_key": start_key,
                    "timestamp_after": timestamp_after,
                    "timestamp_before": timestamp_before,
                    "updated_after": updated_after,
                    "updated_before": updated_before,
                },
                consent_preference_deprecated_create_params.ConsentPreferenceDeprecatedCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ConsentPreferenceDeprecatedCreateResponse,
        )


class ConsentPreferencesResourceWithRawResponse:
    def __init__(self, consent_preferences: ConsentPreferencesResource) -> None:
        self._consent_preferences = consent_preferences

        self.deprecated_create = (  # pyright: ignore[reportDeprecated]
            to_raw_response_wrapper(
                consent_preferences.deprecated_create,  # pyright: ignore[reportDeprecated],
            )
        )


class AsyncConsentPreferencesResourceWithRawResponse:
    def __init__(self, consent_preferences: AsyncConsentPreferencesResource) -> None:
        self._consent_preferences = consent_preferences

        self.deprecated_create = (  # pyright: ignore[reportDeprecated]
            async_to_raw_response_wrapper(
                consent_preferences.deprecated_create,  # pyright: ignore[reportDeprecated],
            )
        )


class ConsentPreferencesResourceWithStreamingResponse:
    def __init__(self, consent_preferences: ConsentPreferencesResource) -> None:
        self._consent_preferences = consent_preferences

        self.deprecated_create = (  # pyright: ignore[reportDeprecated]
            to_streamed_response_wrapper(
                consent_preferences.deprecated_create,  # pyright: ignore[reportDeprecated],
            )
        )


class AsyncConsentPreferencesResourceWithStreamingResponse:
    def __init__(self, consent_preferences: AsyncConsentPreferencesResource) -> None:
        self._consent_preferences = consent_preferences

        self.deprecated_create = (  # pyright: ignore[reportDeprecated]
            async_to_streamed_response_wrapper(
                consent_preferences.deprecated_create,  # pyright: ignore[reportDeprecated],
            )
        )
