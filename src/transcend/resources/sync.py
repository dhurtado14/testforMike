# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ..types import sync_get_consent_preferences_params, sync_set_consent_preferences_params
from .._types import Body, Query, Headers, NotGiven, not_given
from .._utils import maybe_transform, async_maybe_transform
from .._compat import cached_property
from .._resource import SyncAPIResource, AsyncAPIResource
from .._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from .._base_client import make_request_options
from ..types.sync_get_consent_preferences_response import SyncGetConsentPreferencesResponse
from ..types.sync_set_consent_preferences_response import SyncSetConsentPreferencesResponse

__all__ = ["SyncResource", "AsyncSyncResource"]


class SyncResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> SyncResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/dhurtado14/testforMike#accessing-raw-response-data-eg-headers
        """
        return SyncResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> SyncResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/dhurtado14/testforMike#with_streaming_response
        """
        return SyncResourceWithStreamingResponse(self)

    def get_consent_preferences(
        self,
        *,
        partition: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SyncGetConsentPreferencesResponse:
        """
        Get consent preferences for a user at `https://consent.transcend.io` or
        `https://consent.us.transcend.io`. **_N.B._** This is **_not_** a Sombra route.
        This API requires a signed token including an encrypted identifier. See
        [reference](https://docs.transcend.io/docs/preference-store/storing-consent-preferences)
        for details.

        Args:
          partition: The consent partition or bundle ID. You can find the partition value under
              Consent Management > Developer Settings. If this value is not set, please use
              your bundle ID.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/sync",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {"partition": partition}, sync_get_consent_preferences_params.SyncGetConsentPreferencesParams
                ),
            ),
            cast_to=SyncGetConsentPreferencesResponse,
        )

    def set_consent_preferences(
        self,
        *,
        token: str,
        consent: sync_set_consent_preferences_params.Consent,
        partition: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SyncSetConsentPreferencesResponse:
        """
        Set consent preferences for a user at `https://consent.transcend.io` or
        `https://consent.us.transcend.io`. **_N.B._** This is **_not_** a Sombra route.
        This API requires a signed token including an encrypted identifier. See
        [reference](https://docs.transcend.io/docs/preference-store/storing-consent-preferences)
        for details.

        Args:
          token: A JWT including an encrypted identifier

          partition: The consent partition or bundle ID. You can find the partition value under
              Consent Management > Developer Settings. If this value is not set, please use
              your bundle ID.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/sync",
            body=maybe_transform(
                {
                    "token": token,
                    "consent": consent,
                    "partition": partition,
                },
                sync_set_consent_preferences_params.SyncSetConsentPreferencesParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SyncSetConsentPreferencesResponse,
        )


class AsyncSyncResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncSyncResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/dhurtado14/testforMike#accessing-raw-response-data-eg-headers
        """
        return AsyncSyncResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncSyncResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/dhurtado14/testforMike#with_streaming_response
        """
        return AsyncSyncResourceWithStreamingResponse(self)

    async def get_consent_preferences(
        self,
        *,
        partition: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SyncGetConsentPreferencesResponse:
        """
        Get consent preferences for a user at `https://consent.transcend.io` or
        `https://consent.us.transcend.io`. **_N.B._** This is **_not_** a Sombra route.
        This API requires a signed token including an encrypted identifier. See
        [reference](https://docs.transcend.io/docs/preference-store/storing-consent-preferences)
        for details.

        Args:
          partition: The consent partition or bundle ID. You can find the partition value under
              Consent Management > Developer Settings. If this value is not set, please use
              your bundle ID.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/sync",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {"partition": partition}, sync_get_consent_preferences_params.SyncGetConsentPreferencesParams
                ),
            ),
            cast_to=SyncGetConsentPreferencesResponse,
        )

    async def set_consent_preferences(
        self,
        *,
        token: str,
        consent: sync_set_consent_preferences_params.Consent,
        partition: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SyncSetConsentPreferencesResponse:
        """
        Set consent preferences for a user at `https://consent.transcend.io` or
        `https://consent.us.transcend.io`. **_N.B._** This is **_not_** a Sombra route.
        This API requires a signed token including an encrypted identifier. See
        [reference](https://docs.transcend.io/docs/preference-store/storing-consent-preferences)
        for details.

        Args:
          token: A JWT including an encrypted identifier

          partition: The consent partition or bundle ID. You can find the partition value under
              Consent Management > Developer Settings. If this value is not set, please use
              your bundle ID.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/sync",
            body=await async_maybe_transform(
                {
                    "token": token,
                    "consent": consent,
                    "partition": partition,
                },
                sync_set_consent_preferences_params.SyncSetConsentPreferencesParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SyncSetConsentPreferencesResponse,
        )


class SyncResourceWithRawResponse:
    def __init__(self, sync: SyncResource) -> None:
        self._sync = sync

        self.get_consent_preferences = to_raw_response_wrapper(
            sync.get_consent_preferences,
        )
        self.set_consent_preferences = to_raw_response_wrapper(
            sync.set_consent_preferences,
        )


class AsyncSyncResourceWithRawResponse:
    def __init__(self, sync: AsyncSyncResource) -> None:
        self._sync = sync

        self.get_consent_preferences = async_to_raw_response_wrapper(
            sync.get_consent_preferences,
        )
        self.set_consent_preferences = async_to_raw_response_wrapper(
            sync.set_consent_preferences,
        )


class SyncResourceWithStreamingResponse:
    def __init__(self, sync: SyncResource) -> None:
        self._sync = sync

        self.get_consent_preferences = to_streamed_response_wrapper(
            sync.get_consent_preferences,
        )
        self.set_consent_preferences = to_streamed_response_wrapper(
            sync.set_consent_preferences,
        )


class AsyncSyncResourceWithStreamingResponse:
    def __init__(self, sync: AsyncSyncResource) -> None:
        self._sync = sync

        self.get_consent_preferences = async_to_streamed_response_wrapper(
            sync.get_consent_preferences,
        )
        self.set_consent_preferences = async_to_streamed_response_wrapper(
            sync.set_consent_preferences,
        )
