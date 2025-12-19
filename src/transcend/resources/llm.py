# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ..types import llm_classify_text_params
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
from ..types.llm_classify_text_response import LlmClassifyTextResponse

__all__ = ["LlmResource", "AsyncLlmResource"]


class LlmResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> LlmResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/dhurtado14/testforMike#accessing-raw-response-data-eg-headers
        """
        return LlmResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> LlmResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/dhurtado14/testforMike#with_streaming_response
        """
        return LlmResourceWithStreamingResponse(self)

    def classify_text(
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
    ) -> LlmClassifyTextResponse:
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
            "/llm/classify-text",
            body=maybe_transform(
                {
                    "input_list": input_list,
                    "labels": labels,
                },
                llm_classify_text_params.LlmClassifyTextParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=LlmClassifyTextResponse,
        )


class AsyncLlmResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncLlmResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/dhurtado14/testforMike#accessing-raw-response-data-eg-headers
        """
        return AsyncLlmResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncLlmResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/dhurtado14/testforMike#with_streaming_response
        """
        return AsyncLlmResourceWithStreamingResponse(self)

    async def classify_text(
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
    ) -> LlmClassifyTextResponse:
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
            "/llm/classify-text",
            body=await async_maybe_transform(
                {
                    "input_list": input_list,
                    "labels": labels,
                },
                llm_classify_text_params.LlmClassifyTextParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=LlmClassifyTextResponse,
        )


class LlmResourceWithRawResponse:
    def __init__(self, llm: LlmResource) -> None:
        self._llm = llm

        self.classify_text = to_raw_response_wrapper(
            llm.classify_text,
        )


class AsyncLlmResourceWithRawResponse:
    def __init__(self, llm: AsyncLlmResource) -> None:
        self._llm = llm

        self.classify_text = async_to_raw_response_wrapper(
            llm.classify_text,
        )


class LlmResourceWithStreamingResponse:
    def __init__(self, llm: LlmResource) -> None:
        self._llm = llm

        self.classify_text = to_streamed_response_wrapper(
            llm.classify_text,
        )


class AsyncLlmResourceWithStreamingResponse:
    def __init__(self, llm: AsyncLlmResource) -> None:
        self._llm = llm

        self.classify_text = async_to_streamed_response_wrapper(
            llm.classify_text,
        )
