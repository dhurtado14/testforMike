# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable
from typing_extensions import Literal

import httpx

from ..types import data_subject_request_create_params, data_subject_request_download_keys_params
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
from ..types.data_subject_request_create_response import DataSubjectRequestCreateResponse
from ..types.data_subject_request_retrieve_response import DataSubjectRequestRetrieveResponse
from ..types.data_subject_request_download_keys_response import DataSubjectRequestDownloadKeysResponse

__all__ = ["DataSubjectRequestResource", "AsyncDataSubjectRequestResource"]


class DataSubjectRequestResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> DataSubjectRequestResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/transcend-python#accessing-raw-response-data-eg-headers
        """
        return DataSubjectRequestResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> DataSubjectRequestResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/transcend-python#with_streaming_response
        """
        return DataSubjectRequestResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        subject: data_subject_request_create_params.Subject,
        subject_type: str,
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
        attributes: Iterable[data_subject_request_create_params.Attribute] | Omit = omit,
        completed_request_status: Literal[
            "FAILED_VERIFICATION", "COMPLETED", "CANCELED", "SECONDARY_COMPLETED", "REVOKED"
        ]
        | Omit = omit,
        created_at: str | Omit = omit,
        data_silo_ids: SequenceNotStr[str] | Omit = omit,
        details: str | Omit = omit,
        email_receipt_template_id: str | Omit = omit,
        ignore_data_silo_ids: SequenceNotStr[str] | Omit = omit,
        is_silent: bool | Omit = omit,
        is_test: bool | Omit = omit,
        locale: Literal[
            "en",
            "ar",
            "fr",
            "es",
            "de",
            "it",
            "ja",
            "ru",
            "af",
            "bg",
            "zh",
            "hr",
            "cs",
            "da",
            "fi",
            "el",
            "hi",
            "hu",
            "ko",
            "lt",
            "ms",
            "mr",
            "nb",
            "pl",
            "pt",
            "ro",
            "sr",
            "sv",
            "ta",
            "th",
            "tr",
            "uk",
            "vi",
            "zu",
            "he",
            "nl",
            "et",
            "is",
            "lv",
            "mt",
            "sk",
            "sl",
            "fil",
            "bs",
            "ca",
            "eu",
            "gl",
            "dv",
            "ur",
            "sq",
            "am",
            "hy",
            "az",
            "bn",
            "fa-AF",
            "tl",
            "ka",
            "gu",
            "ht",
            "ha",
            "ga",
            "kn",
            "kk",
            "mk",
            "ml",
            "mn",
            "ps",
            "pa",
            "si",
            "so",
            "sw",
            "te",
            "uz",
            "cy",
            "ar-AE",
            "fr-FR",
            "de-DE",
            "de-AT",
            "de-CH",
            "it-IT",
            "it-CH",
            "af-ZA",
            "bg-BG",
            "zh-CN",
            "zh-TW",
            "hr-HR",
            "cs-CZ",
            "da-DK",
            "en-GB",
            "en-CA",
            "en-AE",
            "fi-FI",
            "el-GR",
            "hi-IN",
            "hu-HU",
            "id-ID",
            "ja-JP",
            "ko-KR",
            "lt-LT",
            "ms-MY",
            "ms-SG",
            "mr-IN",
            "nb-NO",
            "pl-PL",
            "pt-BR",
            "pt-PT",
            "ro-RO",
            "ru-RU",
            "sr-Latn-RS",
            "sr-Cyrl-RS",
            "sv-SE",
            "ta-IN",
            "th-TH",
            "tr-TR",
            "uk-UA",
            "vi-VN",
            "zu-ZA",
            "en-US",
            "en-AU",
            "fr-BE",
            "fr-CA",
            "fr-CH",
            "en-IE",
            "nl-NL",
            "nl-BE",
            "es-ES",
            "es-AR",
            "es-CR",
            "es-CL",
            "es-CO",
            "es-MX",
            "es-419",
            "zh-HK",
            "he-IL",
            "en-NZ",
            "et-EE",
            "is-IS",
            "lv-LV",
            "mt-MT",
            "sk-SK",
            "sl-SL",
            "fil-PH",
            "sq-AL",
            "sq-MK",
            "sq-XK",
            "am-ET",
            "hy-AM",
            "az-AZ",
            "bn-BD",
            "bn-IN",
            "bs-BA",
            "bs-Cyrl-BA",
            "bs-Latn-BA",
            "ca-ES",
            "ca-AD",
            "ca-FR",
            "ca-IT",
            "tl-PH",
            "ka-GE",
            "gu-IN",
            "ht-HT",
            "ha-NG",
            "ha-NE",
            "ha-GH",
            "ga-IE",
            "kn-IN",
            "kk-KZ",
            "mk-MK",
            "ml-IN",
            "mn-MN",
            "ps-AF",
            "pa-Guru-IN",
            "pa-Arab-PK",
            "si-LK",
            "so-SO",
            "so-DJ",
            "so-ET",
            "so-KE",
            "sw-KE",
            "sw-TZ",
            "sw-UG",
            "sw-CD",
            "te-IN",
            "ur-PK",
            "ur-IN",
            "uz-UZ",
            "cy-GB",
            "eu-ES",
            "gl-ES",
        ]
        | Omit = omit,
        region: data_subject_request_create_params.Region | Omit = omit,
        reply_to_email_addresses: SequenceNotStr[str] | Omit = omit,
        request_id: str | Omit = omit,
        skip_enrichment_checks: SequenceNotStr[str] | Omit = omit,
        skip_sending_receipt: bool | Omit = omit,
        skip_waiting_period: bool | Omit = omit,
        x_sombra_authorization: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> DataSubjectRequestCreateResponse:
        """
        To initiate a data subject request use this endpoint.

        Args:
          subject_type: The class of data subject, e.g. "customer", "subscriber".

          type: Type of data subject request, can be any one of these events
              (https://docs.transcend.io/docs/receiving-webhooks#events).

          attributes: Key-value pairs used to label data subject requests. These are Custom Fields in
              Transcend, and formerly known as Attributes.

          completed_request_status: When uploaded a backlog of past DSRs, use this field to upload a request
              directly into a completed state.

          created_at: The date at which you received the request and the SLA for completion should
              begin.

          data_silo_ids: The set of data system IDs that SHOULD be processed. When dataSiloIds is set,
              ONLY these data systems will be processed. dataSiloIds and ignoreDataSiloIds
              cannot both be set. When neither are set, the full set of data systems will be
              processed.

          details: Miscellaneous details about the request.

          email_receipt_template_id: Specific email template to be sent to the end user upon request submission. When
              not provided, default template for workflow will be user.

          ignore_data_silo_ids: The set of data system IDs that SHOULD NOT be processed. dataSiloIds and
              ignoreDataSiloIds cannot both be set. When neither are set, the full set of data
              systems will be processed. When ignoreDataSiloIds is set, the full set of data
              systems except these data systems will be processed.

          is_silent: When true, no emails will be sent to the data subject (including confirmation
              emails).

          is_test: When true, the request will be flagged as a test request. (useful for auditing
              purposes). Test requests still operate on your live integrations.

          locale: Language preference, defaults to English ('en').

          region: Specify the region that the request is submitting from. See
              https://github.com/transcend-io/privacy-types/blob/main/src/isoConstants/iso3166-1.ts

          reply_to_email_addresses: The set of email addresses that should be included on CC for any outbound emails
              send to the data subject during the course of the request.

          request_id: When restarting an existing request, specify the ID of the request to restart

          skip_enrichment_checks: Specify the IDs of the enrichers/preflights that should be skipped when running
              this request. When omitted, all enrichers/preflight checks defined for the
              workflow will be run.

          skip_sending_receipt: When true, do not send an email receipt. This is not needed if isSilent=true,
              but can be useful when isSilent=false but no email receipt is desired.

          skip_waiting_period: When true, skip any waiting period associated with the workflow.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {**strip_not_given({"x-sombra-authorization": x_sombra_authorization}), **(extra_headers or {})}
        return self._post(
            "/v1/data-subject-request",
            body=maybe_transform(
                {
                    "subject": subject,
                    "subject_type": subject_type,
                    "type": type,
                    "attributes": attributes,
                    "completed_request_status": completed_request_status,
                    "created_at": created_at,
                    "data_silo_ids": data_silo_ids,
                    "details": details,
                    "email_receipt_template_id": email_receipt_template_id,
                    "ignore_data_silo_ids": ignore_data_silo_ids,
                    "is_silent": is_silent,
                    "is_test": is_test,
                    "locale": locale,
                    "region": region,
                    "reply_to_email_addresses": reply_to_email_addresses,
                    "request_id": request_id,
                    "skip_enrichment_checks": skip_enrichment_checks,
                    "skip_sending_receipt": skip_sending_receipt,
                    "skip_waiting_period": skip_waiting_period,
                },
                data_subject_request_create_params.DataSubjectRequestCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=DataSubjectRequestCreateResponse,
        )

    def retrieve(
        self,
        id: str,
        *,
        x_sombra_authorization: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> DataSubjectRequestRetrieveResponse:
        """Once a DSR has been submitted, it will take some time to complete.

        The status of
        the DSR can be accessed via the following endpoint. Read more
        [about DSR State here](https://docs.transcend.io/docs/using-the-api-for-data-subject-requests#data-subject-request-status).

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        extra_headers = {**strip_not_given({"x-sombra-authorization": x_sombra_authorization}), **(extra_headers or {})}
        return self._get(
            f"/v1/data-subject-request/{id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=DataSubjectRequestRetrieveResponse,
        )

    def download_keys(
        self,
        id: str,
        *,
        limit: float | Omit = omit,
        offset: float | Omit = omit,
        x_sombra_authorization: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> DataSubjectRequestDownloadKeysResponse:
        """
        Once the status of the original DSR indicates there are files available to
        download, it is possible to get a list of these files for download.

        Args:
          limit: The maximum number of file keys to return on this page.

          offset: The pagination offset.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        extra_headers = {**strip_not_given({"x-sombra-authorization": x_sombra_authorization}), **(extra_headers or {})}
        return self._get(
            f"/v1/data-subject-request/{id}/download-keys",
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
                    data_subject_request_download_keys_params.DataSubjectRequestDownloadKeysParams,
                ),
            ),
            cast_to=DataSubjectRequestDownloadKeysResponse,
        )


class AsyncDataSubjectRequestResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncDataSubjectRequestResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/transcend-python#accessing-raw-response-data-eg-headers
        """
        return AsyncDataSubjectRequestResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncDataSubjectRequestResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/transcend-python#with_streaming_response
        """
        return AsyncDataSubjectRequestResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        subject: data_subject_request_create_params.Subject,
        subject_type: str,
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
        attributes: Iterable[data_subject_request_create_params.Attribute] | Omit = omit,
        completed_request_status: Literal[
            "FAILED_VERIFICATION", "COMPLETED", "CANCELED", "SECONDARY_COMPLETED", "REVOKED"
        ]
        | Omit = omit,
        created_at: str | Omit = omit,
        data_silo_ids: SequenceNotStr[str] | Omit = omit,
        details: str | Omit = omit,
        email_receipt_template_id: str | Omit = omit,
        ignore_data_silo_ids: SequenceNotStr[str] | Omit = omit,
        is_silent: bool | Omit = omit,
        is_test: bool | Omit = omit,
        locale: Literal[
            "en",
            "ar",
            "fr",
            "es",
            "de",
            "it",
            "ja",
            "ru",
            "af",
            "bg",
            "zh",
            "hr",
            "cs",
            "da",
            "fi",
            "el",
            "hi",
            "hu",
            "ko",
            "lt",
            "ms",
            "mr",
            "nb",
            "pl",
            "pt",
            "ro",
            "sr",
            "sv",
            "ta",
            "th",
            "tr",
            "uk",
            "vi",
            "zu",
            "he",
            "nl",
            "et",
            "is",
            "lv",
            "mt",
            "sk",
            "sl",
            "fil",
            "bs",
            "ca",
            "eu",
            "gl",
            "dv",
            "ur",
            "sq",
            "am",
            "hy",
            "az",
            "bn",
            "fa-AF",
            "tl",
            "ka",
            "gu",
            "ht",
            "ha",
            "ga",
            "kn",
            "kk",
            "mk",
            "ml",
            "mn",
            "ps",
            "pa",
            "si",
            "so",
            "sw",
            "te",
            "uz",
            "cy",
            "ar-AE",
            "fr-FR",
            "de-DE",
            "de-AT",
            "de-CH",
            "it-IT",
            "it-CH",
            "af-ZA",
            "bg-BG",
            "zh-CN",
            "zh-TW",
            "hr-HR",
            "cs-CZ",
            "da-DK",
            "en-GB",
            "en-CA",
            "en-AE",
            "fi-FI",
            "el-GR",
            "hi-IN",
            "hu-HU",
            "id-ID",
            "ja-JP",
            "ko-KR",
            "lt-LT",
            "ms-MY",
            "ms-SG",
            "mr-IN",
            "nb-NO",
            "pl-PL",
            "pt-BR",
            "pt-PT",
            "ro-RO",
            "ru-RU",
            "sr-Latn-RS",
            "sr-Cyrl-RS",
            "sv-SE",
            "ta-IN",
            "th-TH",
            "tr-TR",
            "uk-UA",
            "vi-VN",
            "zu-ZA",
            "en-US",
            "en-AU",
            "fr-BE",
            "fr-CA",
            "fr-CH",
            "en-IE",
            "nl-NL",
            "nl-BE",
            "es-ES",
            "es-AR",
            "es-CR",
            "es-CL",
            "es-CO",
            "es-MX",
            "es-419",
            "zh-HK",
            "he-IL",
            "en-NZ",
            "et-EE",
            "is-IS",
            "lv-LV",
            "mt-MT",
            "sk-SK",
            "sl-SL",
            "fil-PH",
            "sq-AL",
            "sq-MK",
            "sq-XK",
            "am-ET",
            "hy-AM",
            "az-AZ",
            "bn-BD",
            "bn-IN",
            "bs-BA",
            "bs-Cyrl-BA",
            "bs-Latn-BA",
            "ca-ES",
            "ca-AD",
            "ca-FR",
            "ca-IT",
            "tl-PH",
            "ka-GE",
            "gu-IN",
            "ht-HT",
            "ha-NG",
            "ha-NE",
            "ha-GH",
            "ga-IE",
            "kn-IN",
            "kk-KZ",
            "mk-MK",
            "ml-IN",
            "mn-MN",
            "ps-AF",
            "pa-Guru-IN",
            "pa-Arab-PK",
            "si-LK",
            "so-SO",
            "so-DJ",
            "so-ET",
            "so-KE",
            "sw-KE",
            "sw-TZ",
            "sw-UG",
            "sw-CD",
            "te-IN",
            "ur-PK",
            "ur-IN",
            "uz-UZ",
            "cy-GB",
            "eu-ES",
            "gl-ES",
        ]
        | Omit = omit,
        region: data_subject_request_create_params.Region | Omit = omit,
        reply_to_email_addresses: SequenceNotStr[str] | Omit = omit,
        request_id: str | Omit = omit,
        skip_enrichment_checks: SequenceNotStr[str] | Omit = omit,
        skip_sending_receipt: bool | Omit = omit,
        skip_waiting_period: bool | Omit = omit,
        x_sombra_authorization: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> DataSubjectRequestCreateResponse:
        """
        To initiate a data subject request use this endpoint.

        Args:
          subject_type: The class of data subject, e.g. "customer", "subscriber".

          type: Type of data subject request, can be any one of these events
              (https://docs.transcend.io/docs/receiving-webhooks#events).

          attributes: Key-value pairs used to label data subject requests. These are Custom Fields in
              Transcend, and formerly known as Attributes.

          completed_request_status: When uploaded a backlog of past DSRs, use this field to upload a request
              directly into a completed state.

          created_at: The date at which you received the request and the SLA for completion should
              begin.

          data_silo_ids: The set of data system IDs that SHOULD be processed. When dataSiloIds is set,
              ONLY these data systems will be processed. dataSiloIds and ignoreDataSiloIds
              cannot both be set. When neither are set, the full set of data systems will be
              processed.

          details: Miscellaneous details about the request.

          email_receipt_template_id: Specific email template to be sent to the end user upon request submission. When
              not provided, default template for workflow will be user.

          ignore_data_silo_ids: The set of data system IDs that SHOULD NOT be processed. dataSiloIds and
              ignoreDataSiloIds cannot both be set. When neither are set, the full set of data
              systems will be processed. When ignoreDataSiloIds is set, the full set of data
              systems except these data systems will be processed.

          is_silent: When true, no emails will be sent to the data subject (including confirmation
              emails).

          is_test: When true, the request will be flagged as a test request. (useful for auditing
              purposes). Test requests still operate on your live integrations.

          locale: Language preference, defaults to English ('en').

          region: Specify the region that the request is submitting from. See
              https://github.com/transcend-io/privacy-types/blob/main/src/isoConstants/iso3166-1.ts

          reply_to_email_addresses: The set of email addresses that should be included on CC for any outbound emails
              send to the data subject during the course of the request.

          request_id: When restarting an existing request, specify the ID of the request to restart

          skip_enrichment_checks: Specify the IDs of the enrichers/preflights that should be skipped when running
              this request. When omitted, all enrichers/preflight checks defined for the
              workflow will be run.

          skip_sending_receipt: When true, do not send an email receipt. This is not needed if isSilent=true,
              but can be useful when isSilent=false but no email receipt is desired.

          skip_waiting_period: When true, skip any waiting period associated with the workflow.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {**strip_not_given({"x-sombra-authorization": x_sombra_authorization}), **(extra_headers or {})}
        return await self._post(
            "/v1/data-subject-request",
            body=await async_maybe_transform(
                {
                    "subject": subject,
                    "subject_type": subject_type,
                    "type": type,
                    "attributes": attributes,
                    "completed_request_status": completed_request_status,
                    "created_at": created_at,
                    "data_silo_ids": data_silo_ids,
                    "details": details,
                    "email_receipt_template_id": email_receipt_template_id,
                    "ignore_data_silo_ids": ignore_data_silo_ids,
                    "is_silent": is_silent,
                    "is_test": is_test,
                    "locale": locale,
                    "region": region,
                    "reply_to_email_addresses": reply_to_email_addresses,
                    "request_id": request_id,
                    "skip_enrichment_checks": skip_enrichment_checks,
                    "skip_sending_receipt": skip_sending_receipt,
                    "skip_waiting_period": skip_waiting_period,
                },
                data_subject_request_create_params.DataSubjectRequestCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=DataSubjectRequestCreateResponse,
        )

    async def retrieve(
        self,
        id: str,
        *,
        x_sombra_authorization: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> DataSubjectRequestRetrieveResponse:
        """Once a DSR has been submitted, it will take some time to complete.

        The status of
        the DSR can be accessed via the following endpoint. Read more
        [about DSR State here](https://docs.transcend.io/docs/using-the-api-for-data-subject-requests#data-subject-request-status).

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        extra_headers = {**strip_not_given({"x-sombra-authorization": x_sombra_authorization}), **(extra_headers or {})}
        return await self._get(
            f"/v1/data-subject-request/{id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=DataSubjectRequestRetrieveResponse,
        )

    async def download_keys(
        self,
        id: str,
        *,
        limit: float | Omit = omit,
        offset: float | Omit = omit,
        x_sombra_authorization: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> DataSubjectRequestDownloadKeysResponse:
        """
        Once the status of the original DSR indicates there are files available to
        download, it is possible to get a list of these files for download.

        Args:
          limit: The maximum number of file keys to return on this page.

          offset: The pagination offset.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        extra_headers = {**strip_not_given({"x-sombra-authorization": x_sombra_authorization}), **(extra_headers or {})}
        return await self._get(
            f"/v1/data-subject-request/{id}/download-keys",
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
                    data_subject_request_download_keys_params.DataSubjectRequestDownloadKeysParams,
                ),
            ),
            cast_to=DataSubjectRequestDownloadKeysResponse,
        )


class DataSubjectRequestResourceWithRawResponse:
    def __init__(self, data_subject_request: DataSubjectRequestResource) -> None:
        self._data_subject_request = data_subject_request

        self.create = to_raw_response_wrapper(
            data_subject_request.create,
        )
        self.retrieve = to_raw_response_wrapper(
            data_subject_request.retrieve,
        )
        self.download_keys = to_raw_response_wrapper(
            data_subject_request.download_keys,
        )


class AsyncDataSubjectRequestResourceWithRawResponse:
    def __init__(self, data_subject_request: AsyncDataSubjectRequestResource) -> None:
        self._data_subject_request = data_subject_request

        self.create = async_to_raw_response_wrapper(
            data_subject_request.create,
        )
        self.retrieve = async_to_raw_response_wrapper(
            data_subject_request.retrieve,
        )
        self.download_keys = async_to_raw_response_wrapper(
            data_subject_request.download_keys,
        )


class DataSubjectRequestResourceWithStreamingResponse:
    def __init__(self, data_subject_request: DataSubjectRequestResource) -> None:
        self._data_subject_request = data_subject_request

        self.create = to_streamed_response_wrapper(
            data_subject_request.create,
        )
        self.retrieve = to_streamed_response_wrapper(
            data_subject_request.retrieve,
        )
        self.download_keys = to_streamed_response_wrapper(
            data_subject_request.download_keys,
        )


class AsyncDataSubjectRequestResourceWithStreamingResponse:
    def __init__(self, data_subject_request: AsyncDataSubjectRequestResource) -> None:
        self._data_subject_request = data_subject_request

        self.create = async_to_streamed_response_wrapper(
            data_subject_request.create,
        )
        self.retrieve = async_to_streamed_response_wrapper(
            data_subject_request.retrieve,
        )
        self.download_keys = async_to_streamed_response_wrapper(
            data_subject_request.download_keys,
        )
