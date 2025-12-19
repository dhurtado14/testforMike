# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union, Iterable
from datetime import datetime
from typing_extensions import Literal

import httpx

from ..types import (
    data_silo_confirm_erasure_params,
    data_silo_create_response_params,
    data_silo_list_pending_requests_params,
)
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
from ..types.data_silo_list_pending_requests_response import DataSiloListPendingRequestsResponse

__all__ = ["DataSiloResource", "AsyncDataSiloResource"]


class DataSiloResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> DataSiloResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/dhurtado14/testforMike#accessing-raw-response-data-eg-headers
        """
        return DataSiloResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> DataSiloResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/dhurtado14/testforMike#with_streaming_response
        """
        return DataSiloResourceWithStreamingResponse(self)

    def confirm_erasure(
        self,
        *,
        x_transcend_nonce: str,
        message: str | Omit = omit,
        poll_id: str | Omit = omit,
        profiles: Iterable[data_silo_confirm_erasure_params.Profile] | Omit = omit,
        profile_status: Literal["RESOLVED", "SKIPPED", "SKIPPED_DUE_TO_EXCEPTION", "WAITING", "ERROR"] | Omit = omit,
        retry_after_date: Union[str, datetime] | Omit = omit,
        status: Literal["READY", "RESOLVED", "SKIPPED", "SKIPPED_DUE_TO_EXCEPTION", "ACTION_REQUIRED", "WAITING"]
        | Omit = omit,
        x_sombra_authorization: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> object:
        """
        When responding to an erasure request, use this PUT method to confirm completion
        of an erasure in your system.

        Args:
          message: A message to include in the response to provide an update about the response.
              This is displayed in the Transcend dashboard. This can be an error message or a
              description about the current state of the request job.

          poll_id: If this DSR is in a polling state, this field will contain the ID of the async
              job that is polling for the DSR. You can use this ID to check the status of the
              DSR in your system.

          profiles: [DEPRECATED] An array of each of the profiles that were erased. You should not
              set this value if you are using multi tenant Sombra or have a Sombra version at
              or above 7.199.0. For recent versions of Sombra, the profile identifier is
              pulled from the nonce, which means you can pass an empty body.

          profile_status: Override the specified profiles to be in a specific state.

          retry_after_date: A date in the future that indicates when the user can retry the request. This is
              used for workflows that are asynchronous or to indicate when an error should be
              retried.

          status: Override the integration to be in a specific state. If `status` is set to
              "READY" or "RESOLVED", this will also mark all specified profiles as resolved.

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
        return self._put(
            "/v1/data-silo",
            body=maybe_transform(
                {
                    "message": message,
                    "poll_id": poll_id,
                    "profiles": profiles,
                    "profile_status": profile_status,
                    "retry_after_date": retry_after_date,
                    "status": status,
                },
                data_silo_confirm_erasure_params.DataSiloConfirmErasureParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=object,
        )

    def create_response(
        self,
        *,
        x_transcend_nonce: str,
        profiles: Iterable[data_silo_create_response_params.Profile] | Omit = omit,
        profile_status: Literal["RESOLVED", "SKIPPED", "SKIPPED_DUE_TO_EXCEPTION", "WAITING"] | Omit = omit,
        status: Literal["READY", "RESOLVED", "SKIPPED", "SKIPPED_DUE_TO_EXCEPTION", "ACTION_REQUIRED", "WAITING"]
        | Omit = omit,
        x_sombra_authorization: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> object:
        """When responding to an access request, use this POST method.

        You can upload to
        many datapoints at once when the files uploaded to each Datapoint is valid JSON.

        Args:
          profiles: An array of profiles found. Typically this of length 1, but if your system finds
              multiple profiles (or accounts) for this user, you can upload multiple profiles
              with this array. Or zero!

          profile_status: Override the profile datapoints that have profileData set to be in a specific
              state. Any unreported datapoints will be updated according to the `status` field
              instead of this field.

          status: Override the integration to be in a specific state. Any unreported datapoints
              will be marked as "no data" when status is "READY", "RESOLVED", or
              "ACTION_REQUIRED". Any unreported datapoints will be marked as "skipped" when
              status is "SKIPPED" or "SKIPPED_DUE_TO_EXCEPTION". When status is "WAITING",
              unreported datapoints will not have their statuses changed. Typically this isn't
              needed, since the integration automatically becomes "ready" once all datapoints
              have been reported.

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
            "/v1/data-silo",
            body=maybe_transform(
                {
                    "profiles": profiles,
                    "profile_status": profile_status,
                    "status": status,
                },
                data_silo_create_response_params.DataSiloCreateResponseParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=object,
        )

    def list_pending_requests(
        self,
        type: Literal[
            "ACCESS",
            "ERASURE",
            "RECTIFICATION",
            "RESTRICTION",
            "BUSINESS_PURPOSE",
            "PLACE_ON_LEGAL_HOLD",
            "REMOVE_FROM_LEGAL_HOLD",
            "AUTOMATED_DECISION_MAKING_OPT_OUT",
            "USE_OF_SENSITIVE_INFORMATION_OPT_OUT",
            "CONTACT_OPT_OUT",
            "SALE_OPT_OUT",
            "TRACKING_OPT_OUT",
            "CUSTOM_OPT_OUT",
            "AUTOMATED_DECISION_MAKING_OPT_IN",
            "USE_OF_SENSITIVE_INFORMATION_OPT_IN",
            "SALE_OPT_IN",
            "TRACKING_OPT_IN",
            "CONTACT_OPT_IN",
            "CUSTOM_OPT_IN",
        ],
        *,
        id: str,
        limit: float | Omit = omit,
        offset: float | Omit = omit,
        x_sombra_authorization: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> DataSiloListPendingRequestsResponse:
        """
        List the outstanding identifiers that need to be processed for a particular
        integration and type of DSR. This route will list requests in order from oldest
        to newest requests.You can define new identifiers that your integration requires
        in order to process requests
        [here](https://app.transcend.io/privacy-requests/identifiers). On the DSR
        Automation tab for your data, ensure these identifiers are exposed to your
        script or service.

        Args:
          limit: The number of results to return

          offset: The page offset when paging over data.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        if not type:
            raise ValueError(f"Expected a non-empty value for `type` but received {type!r}")
        extra_headers = {**strip_not_given({"x-sombra-authorization": x_sombra_authorization}), **(extra_headers or {})}
        return self._get(
            f"/v1/data-silo/{id}/pending-requests/{type}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "limit": limit,
                        "offset": offset,
                    },
                    data_silo_list_pending_requests_params.DataSiloListPendingRequestsParams,
                ),
            ),
            cast_to=DataSiloListPendingRequestsResponse,
        )


class AsyncDataSiloResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncDataSiloResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/dhurtado14/testforMike#accessing-raw-response-data-eg-headers
        """
        return AsyncDataSiloResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncDataSiloResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/dhurtado14/testforMike#with_streaming_response
        """
        return AsyncDataSiloResourceWithStreamingResponse(self)

    async def confirm_erasure(
        self,
        *,
        x_transcend_nonce: str,
        message: str | Omit = omit,
        poll_id: str | Omit = omit,
        profiles: Iterable[data_silo_confirm_erasure_params.Profile] | Omit = omit,
        profile_status: Literal["RESOLVED", "SKIPPED", "SKIPPED_DUE_TO_EXCEPTION", "WAITING", "ERROR"] | Omit = omit,
        retry_after_date: Union[str, datetime] | Omit = omit,
        status: Literal["READY", "RESOLVED", "SKIPPED", "SKIPPED_DUE_TO_EXCEPTION", "ACTION_REQUIRED", "WAITING"]
        | Omit = omit,
        x_sombra_authorization: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> object:
        """
        When responding to an erasure request, use this PUT method to confirm completion
        of an erasure in your system.

        Args:
          message: A message to include in the response to provide an update about the response.
              This is displayed in the Transcend dashboard. This can be an error message or a
              description about the current state of the request job.

          poll_id: If this DSR is in a polling state, this field will contain the ID of the async
              job that is polling for the DSR. You can use this ID to check the status of the
              DSR in your system.

          profiles: [DEPRECATED] An array of each of the profiles that were erased. You should not
              set this value if you are using multi tenant Sombra or have a Sombra version at
              or above 7.199.0. For recent versions of Sombra, the profile identifier is
              pulled from the nonce, which means you can pass an empty body.

          profile_status: Override the specified profiles to be in a specific state.

          retry_after_date: A date in the future that indicates when the user can retry the request. This is
              used for workflows that are asynchronous or to indicate when an error should be
              retried.

          status: Override the integration to be in a specific state. If `status` is set to
              "READY" or "RESOLVED", this will also mark all specified profiles as resolved.

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
        return await self._put(
            "/v1/data-silo",
            body=await async_maybe_transform(
                {
                    "message": message,
                    "poll_id": poll_id,
                    "profiles": profiles,
                    "profile_status": profile_status,
                    "retry_after_date": retry_after_date,
                    "status": status,
                },
                data_silo_confirm_erasure_params.DataSiloConfirmErasureParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=object,
        )

    async def create_response(
        self,
        *,
        x_transcend_nonce: str,
        profiles: Iterable[data_silo_create_response_params.Profile] | Omit = omit,
        profile_status: Literal["RESOLVED", "SKIPPED", "SKIPPED_DUE_TO_EXCEPTION", "WAITING"] | Omit = omit,
        status: Literal["READY", "RESOLVED", "SKIPPED", "SKIPPED_DUE_TO_EXCEPTION", "ACTION_REQUIRED", "WAITING"]
        | Omit = omit,
        x_sombra_authorization: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> object:
        """When responding to an access request, use this POST method.

        You can upload to
        many datapoints at once when the files uploaded to each Datapoint is valid JSON.

        Args:
          profiles: An array of profiles found. Typically this of length 1, but if your system finds
              multiple profiles (or accounts) for this user, you can upload multiple profiles
              with this array. Or zero!

          profile_status: Override the profile datapoints that have profileData set to be in a specific
              state. Any unreported datapoints will be updated according to the `status` field
              instead of this field.

          status: Override the integration to be in a specific state. Any unreported datapoints
              will be marked as "no data" when status is "READY", "RESOLVED", or
              "ACTION_REQUIRED". Any unreported datapoints will be marked as "skipped" when
              status is "SKIPPED" or "SKIPPED_DUE_TO_EXCEPTION". When status is "WAITING",
              unreported datapoints will not have their statuses changed. Typically this isn't
              needed, since the integration automatically becomes "ready" once all datapoints
              have been reported.

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
            "/v1/data-silo",
            body=await async_maybe_transform(
                {
                    "profiles": profiles,
                    "profile_status": profile_status,
                    "status": status,
                },
                data_silo_create_response_params.DataSiloCreateResponseParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=object,
        )

    async def list_pending_requests(
        self,
        type: Literal[
            "ACCESS",
            "ERASURE",
            "RECTIFICATION",
            "RESTRICTION",
            "BUSINESS_PURPOSE",
            "PLACE_ON_LEGAL_HOLD",
            "REMOVE_FROM_LEGAL_HOLD",
            "AUTOMATED_DECISION_MAKING_OPT_OUT",
            "USE_OF_SENSITIVE_INFORMATION_OPT_OUT",
            "CONTACT_OPT_OUT",
            "SALE_OPT_OUT",
            "TRACKING_OPT_OUT",
            "CUSTOM_OPT_OUT",
            "AUTOMATED_DECISION_MAKING_OPT_IN",
            "USE_OF_SENSITIVE_INFORMATION_OPT_IN",
            "SALE_OPT_IN",
            "TRACKING_OPT_IN",
            "CONTACT_OPT_IN",
            "CUSTOM_OPT_IN",
        ],
        *,
        id: str,
        limit: float | Omit = omit,
        offset: float | Omit = omit,
        x_sombra_authorization: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> DataSiloListPendingRequestsResponse:
        """
        List the outstanding identifiers that need to be processed for a particular
        integration and type of DSR. This route will list requests in order from oldest
        to newest requests.You can define new identifiers that your integration requires
        in order to process requests
        [here](https://app.transcend.io/privacy-requests/identifiers). On the DSR
        Automation tab for your data, ensure these identifiers are exposed to your
        script or service.

        Args:
          limit: The number of results to return

          offset: The page offset when paging over data.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        if not type:
            raise ValueError(f"Expected a non-empty value for `type` but received {type!r}")
        extra_headers = {**strip_not_given({"x-sombra-authorization": x_sombra_authorization}), **(extra_headers or {})}
        return await self._get(
            f"/v1/data-silo/{id}/pending-requests/{type}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "limit": limit,
                        "offset": offset,
                    },
                    data_silo_list_pending_requests_params.DataSiloListPendingRequestsParams,
                ),
            ),
            cast_to=DataSiloListPendingRequestsResponse,
        )


class DataSiloResourceWithRawResponse:
    def __init__(self, data_silo: DataSiloResource) -> None:
        self._data_silo = data_silo

        self.confirm_erasure = to_raw_response_wrapper(
            data_silo.confirm_erasure,
        )
        self.create_response = to_raw_response_wrapper(
            data_silo.create_response,
        )
        self.list_pending_requests = to_raw_response_wrapper(
            data_silo.list_pending_requests,
        )


class AsyncDataSiloResourceWithRawResponse:
    def __init__(self, data_silo: AsyncDataSiloResource) -> None:
        self._data_silo = data_silo

        self.confirm_erasure = async_to_raw_response_wrapper(
            data_silo.confirm_erasure,
        )
        self.create_response = async_to_raw_response_wrapper(
            data_silo.create_response,
        )
        self.list_pending_requests = async_to_raw_response_wrapper(
            data_silo.list_pending_requests,
        )


class DataSiloResourceWithStreamingResponse:
    def __init__(self, data_silo: DataSiloResource) -> None:
        self._data_silo = data_silo

        self.confirm_erasure = to_streamed_response_wrapper(
            data_silo.confirm_erasure,
        )
        self.create_response = to_streamed_response_wrapper(
            data_silo.create_response,
        )
        self.list_pending_requests = to_streamed_response_wrapper(
            data_silo.list_pending_requests,
        )


class AsyncDataSiloResourceWithStreamingResponse:
    def __init__(self, data_silo: AsyncDataSiloResource) -> None:
        self._data_silo = data_silo

        self.confirm_erasure = async_to_streamed_response_wrapper(
            data_silo.confirm_erasure,
        )
        self.create_response = async_to_streamed_response_wrapper(
            data_silo.create_response,
        )
        self.list_pending_requests = async_to_streamed_response_wrapper(
            data_silo.list_pending_requests,
        )
