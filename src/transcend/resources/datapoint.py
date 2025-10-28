# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from .._files import read_file_content, async_read_file_content
from .._types import Body, Omit, Query, Headers, NotGiven, FileContent, omit, not_given
from .._utils import is_given, strip_not_given
from .._compat import cached_property
from .._resource import SyncAPIResource, AsyncAPIResource
from .._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from .._base_client import make_request_options

__all__ = ["DatapointResource", "AsyncDatapointResource"]


class DatapointResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> DatapointResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/transcend-python#accessing-raw-response-data-eg-headers
        """
        return DatapointResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> DatapointResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/transcend-python#with_streaming_response
        """
        return DatapointResourceWithStreamingResponse(self)

    def upload(
        self,
        body: FileContent,
        *,
        x_transcend_datapoint_name: str,
        x_transcend_nonce: str,
        x_sombra_authorization: str | Omit = omit,
        x_transcend_profile_id: str | Omit = omit,
        x_transcend_remote_id: str | Omit = omit,
        x_transcend_skip_status_update: bool | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> object:
        """If you need to upload a files (e.g.

        photos, movies, audio, PDFs, ...) then use
        this endpoint to send a binary stream to the Datapoint within the integration.
        Unlike /v1/data-silo, this uploads to one datapoint only, rather than several at
        once.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {
            **strip_not_given(
                {
                    "x-transcend-datapoint-name": x_transcend_datapoint_name,
                    "x-transcend-nonce": x_transcend_nonce,
                    "x-sombra-authorization": x_sombra_authorization,
                    "x-transcend-profile-id": x_transcend_profile_id,
                    "x-transcend-remote-id": x_transcend_remote_id,
                    "x-transcend-skip-status-update": ("true" if x_transcend_skip_status_update else "false")
                    if is_given(x_transcend_skip_status_update)
                    else not_given,
                }
            ),
            **(extra_headers or {}),
        }
        extra_headers = {"Content-Type": "application/octet-stream", **(extra_headers or {})}
        return self._post(
            "/v1/datapoint",
            body=read_file_content(body),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=object,
        )


class AsyncDatapointResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncDatapointResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/transcend-python#accessing-raw-response-data-eg-headers
        """
        return AsyncDatapointResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncDatapointResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/transcend-python#with_streaming_response
        """
        return AsyncDatapointResourceWithStreamingResponse(self)

    async def upload(
        self,
        body: FileContent,
        *,
        x_transcend_datapoint_name: str,
        x_transcend_nonce: str,
        x_sombra_authorization: str | Omit = omit,
        x_transcend_profile_id: str | Omit = omit,
        x_transcend_remote_id: str | Omit = omit,
        x_transcend_skip_status_update: bool | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> object:
        """If you need to upload a files (e.g.

        photos, movies, audio, PDFs, ...) then use
        this endpoint to send a binary stream to the Datapoint within the integration.
        Unlike /v1/data-silo, this uploads to one datapoint only, rather than several at
        once.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {
            **strip_not_given(
                {
                    "x-transcend-datapoint-name": x_transcend_datapoint_name,
                    "x-transcend-nonce": x_transcend_nonce,
                    "x-sombra-authorization": x_sombra_authorization,
                    "x-transcend-profile-id": x_transcend_profile_id,
                    "x-transcend-remote-id": x_transcend_remote_id,
                    "x-transcend-skip-status-update": ("true" if x_transcend_skip_status_update else "false")
                    if is_given(x_transcend_skip_status_update)
                    else not_given,
                }
            ),
            **(extra_headers or {}),
        }
        extra_headers = {"Content-Type": "application/octet-stream", **(extra_headers or {})}
        return await self._post(
            "/v1/datapoint",
            body=await async_read_file_content(body),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=object,
        )


class DatapointResourceWithRawResponse:
    def __init__(self, datapoint: DatapointResource) -> None:
        self._datapoint = datapoint

        self.upload = to_raw_response_wrapper(
            datapoint.upload,
        )


class AsyncDatapointResourceWithRawResponse:
    def __init__(self, datapoint: AsyncDatapointResource) -> None:
        self._datapoint = datapoint

        self.upload = async_to_raw_response_wrapper(
            datapoint.upload,
        )


class DatapointResourceWithStreamingResponse:
    def __init__(self, datapoint: DatapointResource) -> None:
        self._datapoint = datapoint

        self.upload = to_streamed_response_wrapper(
            datapoint.upload,
        )


class AsyncDatapointResourceWithStreamingResponse:
    def __init__(self, datapoint: AsyncDatapointResource) -> None:
        self._datapoint = datapoint

        self.upload = async_to_streamed_response_wrapper(
            datapoint.upload,
        )
