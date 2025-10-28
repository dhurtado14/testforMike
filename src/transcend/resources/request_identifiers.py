# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ..types import request_identifier_create_params
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
from ..types.request_identifier_create_response import RequestIdentifierCreateResponse

__all__ = ["RequestIdentifiersResource", "AsyncRequestIdentifiersResource"]


class RequestIdentifiersResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> RequestIdentifiersResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/transcend-python#accessing-raw-response-data-eg-headers
        """
        return RequestIdentifiersResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> RequestIdentifiersResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/transcend-python#with_streaming_response
        """
        return RequestIdentifiersResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        request_id: str,
        first: float | Omit = omit,
        offset: float | Omit = omit,
        x_sombra_authorization: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> RequestIdentifierCreateResponse:
        """List out all of the identifiers that are attached to DSRs.

        These may be the
        emails, coreIdentifiers, phone numbers, user IDs, advertising IDs and more.

        Args:
          request_id: The UUID of the request to fetch request identifiers for

          first: The number of results to return on this page. Defaults to 10, maximum is 100.

          offset: The offset to use while paginating.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {**strip_not_given({"x-sombra-authorization": x_sombra_authorization}), **(extra_headers or {})}
        return self._post(
            "/v1/request-identifiers",
            body=maybe_transform(
                {
                    "request_id": request_id,
                    "first": first,
                    "offset": offset,
                },
                request_identifier_create_params.RequestIdentifierCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=RequestIdentifierCreateResponse,
        )


class AsyncRequestIdentifiersResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncRequestIdentifiersResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/transcend-python#accessing-raw-response-data-eg-headers
        """
        return AsyncRequestIdentifiersResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncRequestIdentifiersResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/transcend-python#with_streaming_response
        """
        return AsyncRequestIdentifiersResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        request_id: str,
        first: float | Omit = omit,
        offset: float | Omit = omit,
        x_sombra_authorization: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> RequestIdentifierCreateResponse:
        """List out all of the identifiers that are attached to DSRs.

        These may be the
        emails, coreIdentifiers, phone numbers, user IDs, advertising IDs and more.

        Args:
          request_id: The UUID of the request to fetch request identifiers for

          first: The number of results to return on this page. Defaults to 10, maximum is 100.

          offset: The offset to use while paginating.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {**strip_not_given({"x-sombra-authorization": x_sombra_authorization}), **(extra_headers or {})}
        return await self._post(
            "/v1/request-identifiers",
            body=await async_maybe_transform(
                {
                    "request_id": request_id,
                    "first": first,
                    "offset": offset,
                },
                request_identifier_create_params.RequestIdentifierCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=RequestIdentifierCreateResponse,
        )


class RequestIdentifiersResourceWithRawResponse:
    def __init__(self, request_identifiers: RequestIdentifiersResource) -> None:
        self._request_identifiers = request_identifiers

        self.create = to_raw_response_wrapper(
            request_identifiers.create,
        )


class AsyncRequestIdentifiersResourceWithRawResponse:
    def __init__(self, request_identifiers: AsyncRequestIdentifiersResource) -> None:
        self._request_identifiers = request_identifiers

        self.create = async_to_raw_response_wrapper(
            request_identifiers.create,
        )


class RequestIdentifiersResourceWithStreamingResponse:
    def __init__(self, request_identifiers: RequestIdentifiersResource) -> None:
        self._request_identifiers = request_identifiers

        self.create = to_streamed_response_wrapper(
            request_identifiers.create,
        )


class AsyncRequestIdentifiersResourceWithStreamingResponse:
    def __init__(self, request_identifiers: AsyncRequestIdentifiersResource) -> None:
        self._request_identifiers = request_identifiers

        self.create = async_to_streamed_response_wrapper(
            request_identifiers.create,
        )
