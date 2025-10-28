# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Iterable
from typing_extensions import Literal

import httpx

from ..types import enrich_identifier_create_params
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

__all__ = ["EnrichIdentifiersResource", "AsyncEnrichIdentifiersResource"]


class EnrichIdentifiersResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> EnrichIdentifiersResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/transcend-python#accessing-raw-response-data-eg-headers
        """
        return EnrichIdentifiersResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> EnrichIdentifiersResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/transcend-python#with_streaming_response
        """
        return EnrichIdentifiersResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        x_transcend_nonce: str,
        enriched_identifiers: Dict[str, Iterable[enrich_identifier_create_params.EnrichedIdentifier]] | Omit = omit,
        status: Literal["CANCELED", "ON_HOLD"] | Omit = omit,
        template_id: str | Omit = omit,
        template_title: str | Omit = omit,
        x_sombra_authorization: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> object:
        """Before processing a new DSR, we can coordinate with your server to:

        1.

        Confirm that this request should be processed (or canceled, or put on hold).
        2. Obtain additional user identifiers, such as a phone number, to find the data
           subject with.

        See
        [the uploading enriched identifiers guide](/docs/dsr-automation/api-integration/identity-enrichment#uploading-enriched-identifiers)
        for more information.

        Args:
          enriched_identifiers: An object where the keys are the identifier names (i.e. email, phone, idfa,
              ...), and the values are a list of enriched identifiers.

          template_id: When status is set to ON_HOLD or CANCELED, you may include the ID of a custom
              email template to send to the data subject.

          template_title: When status is set to ON_HOLD or CANCELED, you may include the title of a custom
              email template to send to the data subject.

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
            "/v1/enrich-identifiers",
            body=maybe_transform(
                {
                    "enriched_identifiers": enriched_identifiers,
                    "status": status,
                    "template_id": template_id,
                    "template_title": template_title,
                },
                enrich_identifier_create_params.EnrichIdentifierCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=object,
        )


class AsyncEnrichIdentifiersResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncEnrichIdentifiersResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/transcend-python#accessing-raw-response-data-eg-headers
        """
        return AsyncEnrichIdentifiersResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncEnrichIdentifiersResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/transcend-python#with_streaming_response
        """
        return AsyncEnrichIdentifiersResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        x_transcend_nonce: str,
        enriched_identifiers: Dict[str, Iterable[enrich_identifier_create_params.EnrichedIdentifier]] | Omit = omit,
        status: Literal["CANCELED", "ON_HOLD"] | Omit = omit,
        template_id: str | Omit = omit,
        template_title: str | Omit = omit,
        x_sombra_authorization: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> object:
        """Before processing a new DSR, we can coordinate with your server to:

        1.

        Confirm that this request should be processed (or canceled, or put on hold).
        2. Obtain additional user identifiers, such as a phone number, to find the data
           subject with.

        See
        [the uploading enriched identifiers guide](/docs/dsr-automation/api-integration/identity-enrichment#uploading-enriched-identifiers)
        for more information.

        Args:
          enriched_identifiers: An object where the keys are the identifier names (i.e. email, phone, idfa,
              ...), and the values are a list of enriched identifiers.

          template_id: When status is set to ON_HOLD or CANCELED, you may include the ID of a custom
              email template to send to the data subject.

          template_title: When status is set to ON_HOLD or CANCELED, you may include the title of a custom
              email template to send to the data subject.

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
            "/v1/enrich-identifiers",
            body=await async_maybe_transform(
                {
                    "enriched_identifiers": enriched_identifiers,
                    "status": status,
                    "template_id": template_id,
                    "template_title": template_title,
                },
                enrich_identifier_create_params.EnrichIdentifierCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=object,
        )


class EnrichIdentifiersResourceWithRawResponse:
    def __init__(self, enrich_identifiers: EnrichIdentifiersResource) -> None:
        self._enrich_identifiers = enrich_identifiers

        self.create = to_raw_response_wrapper(
            enrich_identifiers.create,
        )


class AsyncEnrichIdentifiersResourceWithRawResponse:
    def __init__(self, enrich_identifiers: AsyncEnrichIdentifiersResource) -> None:
        self._enrich_identifiers = enrich_identifiers

        self.create = async_to_raw_response_wrapper(
            enrich_identifiers.create,
        )


class EnrichIdentifiersResourceWithStreamingResponse:
    def __init__(self, enrich_identifiers: EnrichIdentifiersResource) -> None:
        self._enrich_identifiers = enrich_identifiers

        self.create = to_streamed_response_wrapper(
            enrich_identifiers.create,
        )


class AsyncEnrichIdentifiersResourceWithStreamingResponse:
    def __init__(self, enrich_identifiers: AsyncEnrichIdentifiersResource) -> None:
        self._enrich_identifiers = enrich_identifiers

        self.create = async_to_streamed_response_wrapper(
            enrich_identifiers.create,
        )
