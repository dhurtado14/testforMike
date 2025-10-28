# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable

import httpx

from ..types import datapoint_chunked_upload_params
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

__all__ = ["DatapointChunkedResource", "AsyncDatapointChunkedResource"]


class DatapointChunkedResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> DatapointChunkedResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/dhurtado14/testforMike#accessing-raw-response-data-eg-headers
        """
        return DatapointChunkedResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> DatapointChunkedResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/dhurtado14/testforMike#with_streaming_response
        """
        return DatapointChunkedResourceWithStreamingResponse(self)

    def upload(
        self,
        *,
        data: Iterable[object],
        data_point_name: str,
        x_transcend_nonce: str,
        file_id: str | Omit = omit,
        is_last_page: bool | Omit = omit,
        x_sombra_authorization: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> object:
        """
        If you need to page over a large amount of JSON data, then use this endpoint to
        send the JSON in chunks. Transcend will create a file and append each JSON chunk
        to the file as you post the data. You will specify when your service has
        completed paging over the data, after which, Transcend will mark the Datapoint
        as ready.

        Args:
          data: An array of data to be uploaded for that datapoints. This is typically a page
              worth of JSON data

          data_point_name: The name of the datapoint that data is being uploaded for.

          file_id: Give the chunk of data being uploaded a title. For example, if the data is some
              date range, you could title the file "mm/dd/yyy - mm/dd/yyy"

          is_last_page: Set to true when you upload your final page of data (you may also upload an
              empty list with isLastPage=true). When this value is set to true, the datapoint
              will be marked as completed.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {
            **strip_not_given(
                {
                    "x-transcend-nonce": x_transcend_nonce,
                    "x-sombra-authorization": x_sombra_authorization,
                }
            ),
            **(extra_headers or {}),
        }
        return self._post(
            "/v1/datapoint-chunked",
            body=maybe_transform(
                {
                    "data": data,
                    "data_point_name": data_point_name,
                    "file_id": file_id,
                    "is_last_page": is_last_page,
                },
                datapoint_chunked_upload_params.DatapointChunkedUploadParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=object,
        )


class AsyncDatapointChunkedResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncDatapointChunkedResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/dhurtado14/testforMike#accessing-raw-response-data-eg-headers
        """
        return AsyncDatapointChunkedResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncDatapointChunkedResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/dhurtado14/testforMike#with_streaming_response
        """
        return AsyncDatapointChunkedResourceWithStreamingResponse(self)

    async def upload(
        self,
        *,
        data: Iterable[object],
        data_point_name: str,
        x_transcend_nonce: str,
        file_id: str | Omit = omit,
        is_last_page: bool | Omit = omit,
        x_sombra_authorization: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> object:
        """
        If you need to page over a large amount of JSON data, then use this endpoint to
        send the JSON in chunks. Transcend will create a file and append each JSON chunk
        to the file as you post the data. You will specify when your service has
        completed paging over the data, after which, Transcend will mark the Datapoint
        as ready.

        Args:
          data: An array of data to be uploaded for that datapoints. This is typically a page
              worth of JSON data

          data_point_name: The name of the datapoint that data is being uploaded for.

          file_id: Give the chunk of data being uploaded a title. For example, if the data is some
              date range, you could title the file "mm/dd/yyy - mm/dd/yyy"

          is_last_page: Set to true when you upload your final page of data (you may also upload an
              empty list with isLastPage=true). When this value is set to true, the datapoint
              will be marked as completed.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {
            **strip_not_given(
                {
                    "x-transcend-nonce": x_transcend_nonce,
                    "x-sombra-authorization": x_sombra_authorization,
                }
            ),
            **(extra_headers or {}),
        }
        return await self._post(
            "/v1/datapoint-chunked",
            body=await async_maybe_transform(
                {
                    "data": data,
                    "data_point_name": data_point_name,
                    "file_id": file_id,
                    "is_last_page": is_last_page,
                },
                datapoint_chunked_upload_params.DatapointChunkedUploadParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=object,
        )


class DatapointChunkedResourceWithRawResponse:
    def __init__(self, datapoint_chunked: DatapointChunkedResource) -> None:
        self._datapoint_chunked = datapoint_chunked

        self.upload = to_raw_response_wrapper(
            datapoint_chunked.upload,
        )


class AsyncDatapointChunkedResourceWithRawResponse:
    def __init__(self, datapoint_chunked: AsyncDatapointChunkedResource) -> None:
        self._datapoint_chunked = datapoint_chunked

        self.upload = async_to_raw_response_wrapper(
            datapoint_chunked.upload,
        )


class DatapointChunkedResourceWithStreamingResponse:
    def __init__(self, datapoint_chunked: DatapointChunkedResource) -> None:
        self._datapoint_chunked = datapoint_chunked

        self.upload = to_streamed_response_wrapper(
            datapoint_chunked.upload,
        )


class AsyncDatapointChunkedResourceWithStreamingResponse:
    def __init__(self, datapoint_chunked: AsyncDatapointChunkedResource) -> None:
        self._datapoint_chunked = datapoint_chunked

        self.upload = async_to_streamed_response_wrapper(
            datapoint_chunked.upload,
        )
