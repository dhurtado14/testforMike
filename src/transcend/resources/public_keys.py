# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from .._types import Body, Query, Headers, NotGiven, not_given
from .._compat import cached_property
from .._resource import SyncAPIResource, AsyncAPIResource
from .._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from .._base_client import make_request_options

__all__ = ["PublicKeysResource", "AsyncPublicKeysResource"]


class PublicKeysResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> PublicKeysResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/transcend-python#accessing-raw-response-data-eg-headers
        """
        return PublicKeysResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> PublicKeysResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/transcend-python#with_streaming_response
        """
        return PublicKeysResourceWithStreamingResponse(self)

    def retrieve_signing_key(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> str:
        """
        Fetch the public key, which you should use to validate incoming webhooks from
        Transcend. This value can be cached for 1 hour. Please refer to
        [this guide](/docs/dsr-automation/api-integration/receiving-a-webhook-from-transcend)
        for more information on how to verify webhooks with this public key.
        """
        extra_headers = {"Accept": "text/plain", **(extra_headers or {})}
        return self._get(
            "/public-keys/sombra-general-signing-key",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=str,
        )


class AsyncPublicKeysResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncPublicKeysResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/transcend-python#accessing-raw-response-data-eg-headers
        """
        return AsyncPublicKeysResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncPublicKeysResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/transcend-python#with_streaming_response
        """
        return AsyncPublicKeysResourceWithStreamingResponse(self)

    async def retrieve_signing_key(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> str:
        """
        Fetch the public key, which you should use to validate incoming webhooks from
        Transcend. This value can be cached for 1 hour. Please refer to
        [this guide](/docs/dsr-automation/api-integration/receiving-a-webhook-from-transcend)
        for more information on how to verify webhooks with this public key.
        """
        extra_headers = {"Accept": "text/plain", **(extra_headers or {})}
        return await self._get(
            "/public-keys/sombra-general-signing-key",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=str,
        )


class PublicKeysResourceWithRawResponse:
    def __init__(self, public_keys: PublicKeysResource) -> None:
        self._public_keys = public_keys

        self.retrieve_signing_key = to_raw_response_wrapper(
            public_keys.retrieve_signing_key,
        )


class AsyncPublicKeysResourceWithRawResponse:
    def __init__(self, public_keys: AsyncPublicKeysResource) -> None:
        self._public_keys = public_keys

        self.retrieve_signing_key = async_to_raw_response_wrapper(
            public_keys.retrieve_signing_key,
        )


class PublicKeysResourceWithStreamingResponse:
    def __init__(self, public_keys: PublicKeysResource) -> None:
        self._public_keys = public_keys

        self.retrieve_signing_key = to_streamed_response_wrapper(
            public_keys.retrieve_signing_key,
        )


class AsyncPublicKeysResourceWithStreamingResponse:
    def __init__(self, public_keys: AsyncPublicKeysResource) -> None:
        self._public_keys = public_keys

        self.retrieve_signing_key = async_to_streamed_response_wrapper(
            public_keys.retrieve_signing_key,
        )
