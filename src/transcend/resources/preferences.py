# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable

import httpx

from ..types import preference_query_params, preference_upsert_params
from .._types import Body, Omit, Query, Headers, NotGiven, omit, not_given
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
from ..types.preference_query_response import PreferenceQueryResponse
from ..types.preference_upsert_response import PreferenceUpsertResponse

__all__ = ["PreferencesResource", "AsyncPreferencesResource"]


class PreferencesResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> PreferencesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/transcend-python#accessing-raw-response-data-eg-headers
        """
        return PreferencesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> PreferencesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/transcend-python#with_streaming_response
        """
        return PreferencesResourceWithStreamingResponse(self)

    def query(
        self,
        partition: str,
        *,
        filter: preference_query_params.Filter | Omit = omit,
        limit: float | Omit = omit,
        x_sombra_authorization: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PreferenceQueryResponse:
        """
        Query preferences for multiple users

        Args:
          partition: The ID of the partition in the Preference Store.

          filter: The filter to apply to the query.

          limit: Max number of users to return.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not partition:
            raise ValueError(f"Expected a non-empty value for `partition` but received {partition!r}")
        extra_headers = {**strip_not_given({"x-sombra-authorization": x_sombra_authorization}), **(extra_headers or {})}
        return self._post(
            f"/v1/preferences/{partition}/query",
            body=maybe_transform(
                {
                    "filter": filter,
                    "limit": limit,
                },
                preference_query_params.PreferenceQueryParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PreferenceQueryResponse,
        )

    def upsert(
        self,
        *,
        records: Iterable[preference_upsert_params.Record],
        skip_workflow_triggers: bool | Omit = omit,
        x_sombra_authorization: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PreferenceUpsertResponse:
        """
        Batch-upsert preference records for multiple users.

        **Rate Limits**

        - 3000 requests per organization per minute (default).
        - This limit can be increased upon request.

        **Rate Limiting Headers**

        - `X-RateLimit-Limit`: The maximum number of requests allowed in the current
          window.
        - `X-RateLimit-Remaining`: The number of requests remaining in the current
          window.
        - `X-RateLimit-Reset`: The time at which the current rate limit window resets in
          ISO 8601 format.
        - `Retry-After`: (on 429) The number of seconds to wait before making a new
          request.

        Args:
          records: The list of user preferences records to update.

          skip_workflow_triggers: Whether to skip triggering workflows associated with the purpose change event.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {**strip_not_given({"x-sombra-authorization": x_sombra_authorization}), **(extra_headers or {})}
        return self._put(
            "/v1/preferences",
            body=maybe_transform(
                {
                    "records": records,
                    "skip_workflow_triggers": skip_workflow_triggers,
                },
                preference_upsert_params.PreferenceUpsertParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PreferenceUpsertResponse,
        )


class AsyncPreferencesResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncPreferencesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/transcend-python#accessing-raw-response-data-eg-headers
        """
        return AsyncPreferencesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncPreferencesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/transcend-python#with_streaming_response
        """
        return AsyncPreferencesResourceWithStreamingResponse(self)

    async def query(
        self,
        partition: str,
        *,
        filter: preference_query_params.Filter | Omit = omit,
        limit: float | Omit = omit,
        x_sombra_authorization: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PreferenceQueryResponse:
        """
        Query preferences for multiple users

        Args:
          partition: The ID of the partition in the Preference Store.

          filter: The filter to apply to the query.

          limit: Max number of users to return.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not partition:
            raise ValueError(f"Expected a non-empty value for `partition` but received {partition!r}")
        extra_headers = {**strip_not_given({"x-sombra-authorization": x_sombra_authorization}), **(extra_headers or {})}
        return await self._post(
            f"/v1/preferences/{partition}/query",
            body=await async_maybe_transform(
                {
                    "filter": filter,
                    "limit": limit,
                },
                preference_query_params.PreferenceQueryParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PreferenceQueryResponse,
        )

    async def upsert(
        self,
        *,
        records: Iterable[preference_upsert_params.Record],
        skip_workflow_triggers: bool | Omit = omit,
        x_sombra_authorization: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PreferenceUpsertResponse:
        """
        Batch-upsert preference records for multiple users.

        **Rate Limits**

        - 3000 requests per organization per minute (default).
        - This limit can be increased upon request.

        **Rate Limiting Headers**

        - `X-RateLimit-Limit`: The maximum number of requests allowed in the current
          window.
        - `X-RateLimit-Remaining`: The number of requests remaining in the current
          window.
        - `X-RateLimit-Reset`: The time at which the current rate limit window resets in
          ISO 8601 format.
        - `Retry-After`: (on 429) The number of seconds to wait before making a new
          request.

        Args:
          records: The list of user preferences records to update.

          skip_workflow_triggers: Whether to skip triggering workflows associated with the purpose change event.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {**strip_not_given({"x-sombra-authorization": x_sombra_authorization}), **(extra_headers or {})}
        return await self._put(
            "/v1/preferences",
            body=await async_maybe_transform(
                {
                    "records": records,
                    "skip_workflow_triggers": skip_workflow_triggers,
                },
                preference_upsert_params.PreferenceUpsertParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PreferenceUpsertResponse,
        )


class PreferencesResourceWithRawResponse:
    def __init__(self, preferences: PreferencesResource) -> None:
        self._preferences = preferences

        self.query = to_raw_response_wrapper(
            preferences.query,
        )
        self.upsert = to_raw_response_wrapper(
            preferences.upsert,
        )


class AsyncPreferencesResourceWithRawResponse:
    def __init__(self, preferences: AsyncPreferencesResource) -> None:
        self._preferences = preferences

        self.query = async_to_raw_response_wrapper(
            preferences.query,
        )
        self.upsert = async_to_raw_response_wrapper(
            preferences.upsert,
        )


class PreferencesResourceWithStreamingResponse:
    def __init__(self, preferences: PreferencesResource) -> None:
        self._preferences = preferences

        self.query = to_streamed_response_wrapper(
            preferences.query,
        )
        self.upsert = to_streamed_response_wrapper(
            preferences.upsert,
        )


class AsyncPreferencesResourceWithStreamingResponse:
    def __init__(self, preferences: AsyncPreferencesResource) -> None:
        self._preferences = preferences

        self.query = async_to_streamed_response_wrapper(
            preferences.query,
        )
        self.upsert = async_to_streamed_response_wrapper(
            preferences.upsert,
        )
