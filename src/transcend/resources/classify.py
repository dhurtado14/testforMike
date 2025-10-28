# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ..types import classify_classify_unstructured_text_params
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
from ..types.classify_classify_unstructured_text_response import ClassifyClassifyUnstructuredTextResponse

__all__ = ["ClassifyResource", "AsyncClassifyResource"]


class ClassifyResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> ClassifyResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/dhurtado14/testforMike#accessing-raw-response-data-eg-headers
        """
        return ClassifyResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ClassifyResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/dhurtado14/testforMike#with_streaming_response
        """
        return ClassifyResourceWithStreamingResponse(self)

    def classify_unstructured_text(
        self,
        *,
        input_list: SequenceNotStr[str],
        labels: SequenceNotStr[str],
        x_sombra_authorization: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ClassifyClassifyUnstructuredTextResponse:
        """
        Classify a given text array input using the LLM classifier

        Args:
          input_list: List of inputs to classify

          labels: The list of labels to classify against

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {**strip_not_given({"x-sombra-authorization": x_sombra_authorization}), **(extra_headers or {})}
        return self._post(
            "/classify/unstructured-text",
            body=maybe_transform(
                {
                    "input_list": input_list,
                    "labels": labels,
                },
                classify_classify_unstructured_text_params.ClassifyClassifyUnstructuredTextParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ClassifyClassifyUnstructuredTextResponse,
        )


class AsyncClassifyResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncClassifyResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/dhurtado14/testforMike#accessing-raw-response-data-eg-headers
        """
        return AsyncClassifyResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncClassifyResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/dhurtado14/testforMike#with_streaming_response
        """
        return AsyncClassifyResourceWithStreamingResponse(self)

    async def classify_unstructured_text(
        self,
        *,
        input_list: SequenceNotStr[str],
        labels: SequenceNotStr[str],
        x_sombra_authorization: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ClassifyClassifyUnstructuredTextResponse:
        """
        Classify a given text array input using the LLM classifier

        Args:
          input_list: List of inputs to classify

          labels: The list of labels to classify against

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {**strip_not_given({"x-sombra-authorization": x_sombra_authorization}), **(extra_headers or {})}
        return await self._post(
            "/classify/unstructured-text",
            body=await async_maybe_transform(
                {
                    "input_list": input_list,
                    "labels": labels,
                },
                classify_classify_unstructured_text_params.ClassifyClassifyUnstructuredTextParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ClassifyClassifyUnstructuredTextResponse,
        )


class ClassifyResourceWithRawResponse:
    def __init__(self, classify: ClassifyResource) -> None:
        self._classify = classify

        self.classify_unstructured_text = to_raw_response_wrapper(
            classify.classify_unstructured_text,
        )


class AsyncClassifyResourceWithRawResponse:
    def __init__(self, classify: AsyncClassifyResource) -> None:
        self._classify = classify

        self.classify_unstructured_text = async_to_raw_response_wrapper(
            classify.classify_unstructured_text,
        )


class ClassifyResourceWithStreamingResponse:
    def __init__(self, classify: ClassifyResource) -> None:
        self._classify = classify

        self.classify_unstructured_text = to_streamed_response_wrapper(
            classify.classify_unstructured_text,
        )


class AsyncClassifyResourceWithStreamingResponse:
    def __init__(self, classify: AsyncClassifyResource) -> None:
        self._classify = classify

        self.classify_unstructured_text = async_to_streamed_response_wrapper(
            classify.classify_unstructured_text,
        )
