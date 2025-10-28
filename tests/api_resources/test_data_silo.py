# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from transcend import Transcend, AsyncTranscend
from tests.utils import assert_matches_type
from transcend.types import (
    DataSiloListPendingRequestsResponse,
)
from transcend._utils import parse_datetime

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestDataSilo:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_confirm_erasure(self, client: Transcend) -> None:
        data_silo = client.data_silo.confirm_erasure(
            x_transcend_nonce="x-transcend-nonce",
        )
        assert_matches_type(object, data_silo, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_confirm_erasure_with_all_params(self, client: Transcend) -> None:
        data_silo = client.data_silo.confirm_erasure(
            x_transcend_nonce="x-transcend-nonce",
            message="message",
            poll_id="pollId",
            profiles=[{"profile_id": "x"}],
            profile_status="RESOLVED",
            retry_after_date=parse_datetime("2019-12-27T18:11:19.117Z"),
            status="READY",
            x_sombra_authorization="x-sombra-authorization",
        )
        assert_matches_type(object, data_silo, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_confirm_erasure(self, client: Transcend) -> None:
        response = client.data_silo.with_raw_response.confirm_erasure(
            x_transcend_nonce="x-transcend-nonce",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        data_silo = response.parse()
        assert_matches_type(object, data_silo, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_confirm_erasure(self, client: Transcend) -> None:
        with client.data_silo.with_streaming_response.confirm_erasure(
            x_transcend_nonce="x-transcend-nonce",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            data_silo = response.parse()
            assert_matches_type(object, data_silo, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_create_response(self, client: Transcend) -> None:
        data_silo = client.data_silo.create_response(
            x_transcend_nonce="x-transcend-nonce",
        )
        assert_matches_type(object, data_silo, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_create_response_with_all_params(self, client: Transcend) -> None:
        data_silo = client.data_silo.create_response(
            x_transcend_nonce="x-transcend-nonce",
            profiles=[
                {
                    "profile_data": {
                        "name": "Ben Farrell",
                        "favoriteFood": ["pie", "fries"],
                        "address": None,
                    },
                    "profile_id": "x",
                }
            ],
            profile_status="RESOLVED",
            status="READY",
            x_sombra_authorization="x-sombra-authorization",
        )
        assert_matches_type(object, data_silo, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_create_response(self, client: Transcend) -> None:
        response = client.data_silo.with_raw_response.create_response(
            x_transcend_nonce="x-transcend-nonce",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        data_silo = response.parse()
        assert_matches_type(object, data_silo, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_create_response(self, client: Transcend) -> None:
        with client.data_silo.with_streaming_response.create_response(
            x_transcend_nonce="x-transcend-nonce",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            data_silo = response.parse()
            assert_matches_type(object, data_silo, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_list_pending_requests(self, client: Transcend) -> None:
        data_silo = client.data_silo.list_pending_requests(
            type="ACCESS",
            id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(DataSiloListPendingRequestsResponse, data_silo, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_list_pending_requests_with_all_params(self, client: Transcend) -> None:
        data_silo = client.data_silo.list_pending_requests(
            type="ACCESS",
            id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            limit=1,
            offset=0,
            x_sombra_authorization="x-sombra-authorization",
        )
        assert_matches_type(DataSiloListPendingRequestsResponse, data_silo, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_list_pending_requests(self, client: Transcend) -> None:
        response = client.data_silo.with_raw_response.list_pending_requests(
            type="ACCESS",
            id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        data_silo = response.parse()
        assert_matches_type(DataSiloListPendingRequestsResponse, data_silo, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_list_pending_requests(self, client: Transcend) -> None:
        with client.data_silo.with_streaming_response.list_pending_requests(
            type="ACCESS",
            id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            data_silo = response.parse()
            assert_matches_type(DataSiloListPendingRequestsResponse, data_silo, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_list_pending_requests(self, client: Transcend) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.data_silo.with_raw_response.list_pending_requests(
                type="ACCESS",
                id="",
            )


class TestAsyncDataSilo:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_confirm_erasure(self, async_client: AsyncTranscend) -> None:
        data_silo = await async_client.data_silo.confirm_erasure(
            x_transcend_nonce="x-transcend-nonce",
        )
        assert_matches_type(object, data_silo, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_confirm_erasure_with_all_params(self, async_client: AsyncTranscend) -> None:
        data_silo = await async_client.data_silo.confirm_erasure(
            x_transcend_nonce="x-transcend-nonce",
            message="message",
            poll_id="pollId",
            profiles=[{"profile_id": "x"}],
            profile_status="RESOLVED",
            retry_after_date=parse_datetime("2019-12-27T18:11:19.117Z"),
            status="READY",
            x_sombra_authorization="x-sombra-authorization",
        )
        assert_matches_type(object, data_silo, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_confirm_erasure(self, async_client: AsyncTranscend) -> None:
        response = await async_client.data_silo.with_raw_response.confirm_erasure(
            x_transcend_nonce="x-transcend-nonce",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        data_silo = await response.parse()
        assert_matches_type(object, data_silo, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_confirm_erasure(self, async_client: AsyncTranscend) -> None:
        async with async_client.data_silo.with_streaming_response.confirm_erasure(
            x_transcend_nonce="x-transcend-nonce",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            data_silo = await response.parse()
            assert_matches_type(object, data_silo, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_create_response(self, async_client: AsyncTranscend) -> None:
        data_silo = await async_client.data_silo.create_response(
            x_transcend_nonce="x-transcend-nonce",
        )
        assert_matches_type(object, data_silo, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_create_response_with_all_params(self, async_client: AsyncTranscend) -> None:
        data_silo = await async_client.data_silo.create_response(
            x_transcend_nonce="x-transcend-nonce",
            profiles=[
                {
                    "profile_data": {
                        "name": "Ben Farrell",
                        "favoriteFood": ["pie", "fries"],
                        "address": None,
                    },
                    "profile_id": "x",
                }
            ],
            profile_status="RESOLVED",
            status="READY",
            x_sombra_authorization="x-sombra-authorization",
        )
        assert_matches_type(object, data_silo, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_create_response(self, async_client: AsyncTranscend) -> None:
        response = await async_client.data_silo.with_raw_response.create_response(
            x_transcend_nonce="x-transcend-nonce",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        data_silo = await response.parse()
        assert_matches_type(object, data_silo, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_create_response(self, async_client: AsyncTranscend) -> None:
        async with async_client.data_silo.with_streaming_response.create_response(
            x_transcend_nonce="x-transcend-nonce",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            data_silo = await response.parse()
            assert_matches_type(object, data_silo, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_list_pending_requests(self, async_client: AsyncTranscend) -> None:
        data_silo = await async_client.data_silo.list_pending_requests(
            type="ACCESS",
            id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(DataSiloListPendingRequestsResponse, data_silo, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_list_pending_requests_with_all_params(self, async_client: AsyncTranscend) -> None:
        data_silo = await async_client.data_silo.list_pending_requests(
            type="ACCESS",
            id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            limit=1,
            offset=0,
            x_sombra_authorization="x-sombra-authorization",
        )
        assert_matches_type(DataSiloListPendingRequestsResponse, data_silo, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_list_pending_requests(self, async_client: AsyncTranscend) -> None:
        response = await async_client.data_silo.with_raw_response.list_pending_requests(
            type="ACCESS",
            id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        data_silo = await response.parse()
        assert_matches_type(DataSiloListPendingRequestsResponse, data_silo, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_list_pending_requests(self, async_client: AsyncTranscend) -> None:
        async with async_client.data_silo.with_streaming_response.list_pending_requests(
            type="ACCESS",
            id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            data_silo = await response.parse()
            assert_matches_type(DataSiloListPendingRequestsResponse, data_silo, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_list_pending_requests(self, async_client: AsyncTranscend) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.data_silo.with_raw_response.list_pending_requests(
                type="ACCESS",
                id="",
            )
