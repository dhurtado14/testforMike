# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from transcend import Transcend, AsyncTranscend
from tests.utils import assert_matches_type
from transcend.types import (
    DataSubjectRequestCreateResponse,
    DataSubjectRequestRetrieveResponse,
    DataSubjectRequestDownloadKeysResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestDataSubjectRequest:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_create(self, client: Transcend) -> None:
        data_subject_request = client.data_subject_request.create(
            subject={"core_identifier": "id-123456789"},
            subject_type="customer",
            type="ACCESS",
        )
        assert_matches_type(DataSubjectRequestCreateResponse, data_subject_request, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_create_with_all_params(self, client: Transcend) -> None:
        data_subject_request = client.data_subject_request.create(
            subject={
                "core_identifier": "id-123456789",
                "attested_extra_identifiers": {
                    "adobe_advertising_cloud_id": [{"value": "x"}],
                    "adobe_audience_manager_id": [{"value": "x"}],
                    "adobe_experience_cloud_id": [{"value": "x"}],
                    "adobe_target_id": [{"value": "x"}],
                    "advertising_id": [{"value": "x"}],
                    "amazon_fire_advertising_id": [{"value": "x"}],
                    "braintree_customer_id": [{"value": "x"}],
                    "browser_id": [{"value": "x"}],
                    "chargebee_id": [{"value": "x"}],
                    "core_identifier": [{"value": "x"}],
                    "custom": [
                        {
                            "name": "x",
                            "value": "x",
                        }
                    ],
                    "customer_io_id": [{"value": "x"}],
                    "email": [{"value": "dev@stainless.com"}],
                    "filestack_handle": [{"value": "x"}],
                    "gaid": [{"value": "x"}],
                    "idfa": [{"value": "x"}],
                    "idfv": [{"value": "x"}],
                    "linked_in_url": [{"value": "x"}],
                    "microsoft_advertising_id": [{"value": "x"}],
                    "onfido_applicant_id": [{"value": "x"}],
                    "persona_reference_id": [{"value": "x"}],
                    "phone": [{"value": "x"}],
                    "plaid_processor_token": [{"value": "x"}],
                    "recurly_id": [{"value": "x"}],
                    "rida": [{"value": "x"}],
                    "sprig_visitor_id": [{"value": "x"}],
                    "stream_user_id": [{"value": "x"}],
                    "stripe_id": [{"value": "x"}],
                    "talkable_uuid": [{"value": "x"}],
                    "thrive_trm_contact_id": [{"value": "x"}],
                    "vero_user_id": [{"value": "x"}],
                },
                "email": "user@example.com",
                "email_is_verified": True,
            },
            subject_type="customer",
            type="ACCESS",
            attributes=[
                {
                    "key": "x",
                    "values": ["string"],
                }
            ],
            completed_request_status="FAILED_VERIFICATION",
            created_at="x",
            data_silo_ids=["182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"],
            details="x",
            email_receipt_template_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            ignore_data_silo_ids=["182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"],
            is_silent=True,
            is_test=True,
            locale="en",
            region={
                "country": "EU",
                "country_sub_division": "AD-02",
            },
            reply_to_email_addresses=["dev@stainless.com"],
            request_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            skip_enrichment_checks=["182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"],
            skip_sending_receipt=True,
            skip_waiting_period=True,
            x_sombra_authorization="x-sombra-authorization",
        )
        assert_matches_type(DataSubjectRequestCreateResponse, data_subject_request, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_create(self, client: Transcend) -> None:
        response = client.data_subject_request.with_raw_response.create(
            subject={"core_identifier": "id-123456789"},
            subject_type="customer",
            type="ACCESS",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        data_subject_request = response.parse()
        assert_matches_type(DataSubjectRequestCreateResponse, data_subject_request, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_create(self, client: Transcend) -> None:
        with client.data_subject_request.with_streaming_response.create(
            subject={"core_identifier": "id-123456789"},
            subject_type="customer",
            type="ACCESS",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            data_subject_request = response.parse()
            assert_matches_type(DataSubjectRequestCreateResponse, data_subject_request, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_retrieve(self, client: Transcend) -> None:
        data_subject_request = client.data_subject_request.retrieve(
            id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(DataSubjectRequestRetrieveResponse, data_subject_request, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_retrieve_with_all_params(self, client: Transcend) -> None:
        data_subject_request = client.data_subject_request.retrieve(
            id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            x_sombra_authorization="x-sombra-authorization",
        )
        assert_matches_type(DataSubjectRequestRetrieveResponse, data_subject_request, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_retrieve(self, client: Transcend) -> None:
        response = client.data_subject_request.with_raw_response.retrieve(
            id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        data_subject_request = response.parse()
        assert_matches_type(DataSubjectRequestRetrieveResponse, data_subject_request, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_retrieve(self, client: Transcend) -> None:
        with client.data_subject_request.with_streaming_response.retrieve(
            id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            data_subject_request = response.parse()
            assert_matches_type(DataSubjectRequestRetrieveResponse, data_subject_request, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_retrieve(self, client: Transcend) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.data_subject_request.with_raw_response.retrieve(
                id="",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_download_keys(self, client: Transcend) -> None:
        data_subject_request = client.data_subject_request.download_keys(
            id="id",
        )
        assert_matches_type(DataSubjectRequestDownloadKeysResponse, data_subject_request, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_download_keys_with_all_params(self, client: Transcend) -> None:
        data_subject_request = client.data_subject_request.download_keys(
            id="id",
            limit=0,
            offset=0,
            x_sombra_authorization="x-sombra-authorization",
        )
        assert_matches_type(DataSubjectRequestDownloadKeysResponse, data_subject_request, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_download_keys(self, client: Transcend) -> None:
        response = client.data_subject_request.with_raw_response.download_keys(
            id="id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        data_subject_request = response.parse()
        assert_matches_type(DataSubjectRequestDownloadKeysResponse, data_subject_request, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_download_keys(self, client: Transcend) -> None:
        with client.data_subject_request.with_streaming_response.download_keys(
            id="id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            data_subject_request = response.parse()
            assert_matches_type(DataSubjectRequestDownloadKeysResponse, data_subject_request, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_download_keys(self, client: Transcend) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.data_subject_request.with_raw_response.download_keys(
                id="",
            )


class TestAsyncDataSubjectRequest:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_create(self, async_client: AsyncTranscend) -> None:
        data_subject_request = await async_client.data_subject_request.create(
            subject={"core_identifier": "id-123456789"},
            subject_type="customer",
            type="ACCESS",
        )
        assert_matches_type(DataSubjectRequestCreateResponse, data_subject_request, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncTranscend) -> None:
        data_subject_request = await async_client.data_subject_request.create(
            subject={
                "core_identifier": "id-123456789",
                "attested_extra_identifiers": {
                    "adobe_advertising_cloud_id": [{"value": "x"}],
                    "adobe_audience_manager_id": [{"value": "x"}],
                    "adobe_experience_cloud_id": [{"value": "x"}],
                    "adobe_target_id": [{"value": "x"}],
                    "advertising_id": [{"value": "x"}],
                    "amazon_fire_advertising_id": [{"value": "x"}],
                    "braintree_customer_id": [{"value": "x"}],
                    "browser_id": [{"value": "x"}],
                    "chargebee_id": [{"value": "x"}],
                    "core_identifier": [{"value": "x"}],
                    "custom": [
                        {
                            "name": "x",
                            "value": "x",
                        }
                    ],
                    "customer_io_id": [{"value": "x"}],
                    "email": [{"value": "dev@stainless.com"}],
                    "filestack_handle": [{"value": "x"}],
                    "gaid": [{"value": "x"}],
                    "idfa": [{"value": "x"}],
                    "idfv": [{"value": "x"}],
                    "linked_in_url": [{"value": "x"}],
                    "microsoft_advertising_id": [{"value": "x"}],
                    "onfido_applicant_id": [{"value": "x"}],
                    "persona_reference_id": [{"value": "x"}],
                    "phone": [{"value": "x"}],
                    "plaid_processor_token": [{"value": "x"}],
                    "recurly_id": [{"value": "x"}],
                    "rida": [{"value": "x"}],
                    "sprig_visitor_id": [{"value": "x"}],
                    "stream_user_id": [{"value": "x"}],
                    "stripe_id": [{"value": "x"}],
                    "talkable_uuid": [{"value": "x"}],
                    "thrive_trm_contact_id": [{"value": "x"}],
                    "vero_user_id": [{"value": "x"}],
                },
                "email": "user@example.com",
                "email_is_verified": True,
            },
            subject_type="customer",
            type="ACCESS",
            attributes=[
                {
                    "key": "x",
                    "values": ["string"],
                }
            ],
            completed_request_status="FAILED_VERIFICATION",
            created_at="x",
            data_silo_ids=["182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"],
            details="x",
            email_receipt_template_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            ignore_data_silo_ids=["182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"],
            is_silent=True,
            is_test=True,
            locale="en",
            region={
                "country": "EU",
                "country_sub_division": "AD-02",
            },
            reply_to_email_addresses=["dev@stainless.com"],
            request_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            skip_enrichment_checks=["182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"],
            skip_sending_receipt=True,
            skip_waiting_period=True,
            x_sombra_authorization="x-sombra-authorization",
        )
        assert_matches_type(DataSubjectRequestCreateResponse, data_subject_request, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_create(self, async_client: AsyncTranscend) -> None:
        response = await async_client.data_subject_request.with_raw_response.create(
            subject={"core_identifier": "id-123456789"},
            subject_type="customer",
            type="ACCESS",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        data_subject_request = await response.parse()
        assert_matches_type(DataSubjectRequestCreateResponse, data_subject_request, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncTranscend) -> None:
        async with async_client.data_subject_request.with_streaming_response.create(
            subject={"core_identifier": "id-123456789"},
            subject_type="customer",
            type="ACCESS",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            data_subject_request = await response.parse()
            assert_matches_type(DataSubjectRequestCreateResponse, data_subject_request, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_retrieve(self, async_client: AsyncTranscend) -> None:
        data_subject_request = await async_client.data_subject_request.retrieve(
            id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(DataSubjectRequestRetrieveResponse, data_subject_request, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_retrieve_with_all_params(self, async_client: AsyncTranscend) -> None:
        data_subject_request = await async_client.data_subject_request.retrieve(
            id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            x_sombra_authorization="x-sombra-authorization",
        )
        assert_matches_type(DataSubjectRequestRetrieveResponse, data_subject_request, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncTranscend) -> None:
        response = await async_client.data_subject_request.with_raw_response.retrieve(
            id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        data_subject_request = await response.parse()
        assert_matches_type(DataSubjectRequestRetrieveResponse, data_subject_request, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncTranscend) -> None:
        async with async_client.data_subject_request.with_streaming_response.retrieve(
            id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            data_subject_request = await response.parse()
            assert_matches_type(DataSubjectRequestRetrieveResponse, data_subject_request, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncTranscend) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.data_subject_request.with_raw_response.retrieve(
                id="",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_download_keys(self, async_client: AsyncTranscend) -> None:
        data_subject_request = await async_client.data_subject_request.download_keys(
            id="id",
        )
        assert_matches_type(DataSubjectRequestDownloadKeysResponse, data_subject_request, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_download_keys_with_all_params(self, async_client: AsyncTranscend) -> None:
        data_subject_request = await async_client.data_subject_request.download_keys(
            id="id",
            limit=0,
            offset=0,
            x_sombra_authorization="x-sombra-authorization",
        )
        assert_matches_type(DataSubjectRequestDownloadKeysResponse, data_subject_request, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_download_keys(self, async_client: AsyncTranscend) -> None:
        response = await async_client.data_subject_request.with_raw_response.download_keys(
            id="id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        data_subject_request = await response.parse()
        assert_matches_type(DataSubjectRequestDownloadKeysResponse, data_subject_request, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_download_keys(self, async_client: AsyncTranscend) -> None:
        async with async_client.data_subject_request.with_streaming_response.download_keys(
            id="id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            data_subject_request = await response.parse()
            assert_matches_type(DataSubjectRequestDownloadKeysResponse, data_subject_request, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_download_keys(self, async_client: AsyncTranscend) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.data_subject_request.with_raw_response.download_keys(
                id="",
            )
