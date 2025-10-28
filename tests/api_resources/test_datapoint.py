# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from transcend import Transcend, AsyncTranscend
from tests.utils import assert_matches_type

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestDatapoint:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_upload(self, client: Transcend) -> None:
        datapoint = client.datapoint.upload(
            body=b"raw file contents",
            x_transcend_datapoint_name="x-transcend-datapoint-name",
            x_transcend_nonce="x-transcend-nonce",
        )
        assert_matches_type(object, datapoint, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_upload_with_all_params(self, client: Transcend) -> None:
        datapoint = client.datapoint.upload(
            body=b"raw file contents",
            x_transcend_datapoint_name="x-transcend-datapoint-name",
            x_transcend_nonce="x-transcend-nonce",
            x_sombra_authorization="x-sombra-authorization",
            x_transcend_profile_id="x-transcend-profile-id",
            x_transcend_remote_id="x-transcend-remote-id",
            x_transcend_skip_status_update=True,
        )
        assert_matches_type(object, datapoint, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_upload(self, client: Transcend) -> None:
        response = client.datapoint.with_raw_response.upload(
            body=b"raw file contents",
            x_transcend_datapoint_name="x-transcend-datapoint-name",
            x_transcend_nonce="x-transcend-nonce",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        datapoint = response.parse()
        assert_matches_type(object, datapoint, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_upload(self, client: Transcend) -> None:
        with client.datapoint.with_streaming_response.upload(
            body=b"raw file contents",
            x_transcend_datapoint_name="x-transcend-datapoint-name",
            x_transcend_nonce="x-transcend-nonce",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            datapoint = response.parse()
            assert_matches_type(object, datapoint, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncDatapoint:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_upload(self, async_client: AsyncTranscend) -> None:
        datapoint = await async_client.datapoint.upload(
            body=b"raw file contents",
            x_transcend_datapoint_name="x-transcend-datapoint-name",
            x_transcend_nonce="x-transcend-nonce",
        )
        assert_matches_type(object, datapoint, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_upload_with_all_params(self, async_client: AsyncTranscend) -> None:
        datapoint = await async_client.datapoint.upload(
            body=b"raw file contents",
            x_transcend_datapoint_name="x-transcend-datapoint-name",
            x_transcend_nonce="x-transcend-nonce",
            x_sombra_authorization="x-sombra-authorization",
            x_transcend_profile_id="x-transcend-profile-id",
            x_transcend_remote_id="x-transcend-remote-id",
            x_transcend_skip_status_update=True,
        )
        assert_matches_type(object, datapoint, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_upload(self, async_client: AsyncTranscend) -> None:
        response = await async_client.datapoint.with_raw_response.upload(
            body=b"raw file contents",
            x_transcend_datapoint_name="x-transcend-datapoint-name",
            x_transcend_nonce="x-transcend-nonce",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        datapoint = await response.parse()
        assert_matches_type(object, datapoint, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_upload(self, async_client: AsyncTranscend) -> None:
        async with async_client.datapoint.with_streaming_response.upload(
            body=b"raw file contents",
            x_transcend_datapoint_name="x-transcend-datapoint-name",
            x_transcend_nonce="x-transcend-nonce",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            datapoint = await response.parse()
            assert_matches_type(object, datapoint, path=["response"])

        assert cast(Any, response.is_closed) is True
