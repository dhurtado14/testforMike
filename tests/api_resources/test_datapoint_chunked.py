# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from transcend import Transcend, AsyncTranscend
from tests.utils import assert_matches_type

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestDatapointChunked:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_upload(self, client: Transcend) -> None:
        datapoint_chunked = client.datapoint_chunked.upload(
            data=[
                {
                    "id": "d8e57222-43c6-4fd7-b928-4a8ae106fe98",
                    "time_stamp": "2022-04-07T04:58:19.900Z",
                    "metric": 4,
                    "isCool": True,
                },
                {
                    "id": "31a17418-ec6e-4b3a-9056-b5c17278d053",
                    "time_stamp": "2022-04-08T04:58:19.900Z",
                    "metric": 0,
                    "isCool": False,
                },
            ],
            data_point_name="activities",
            x_transcend_nonce="x-transcend-nonce",
        )
        assert_matches_type(object, datapoint_chunked, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_upload_with_all_params(self, client: Transcend) -> None:
        datapoint_chunked = client.datapoint_chunked.upload(
            data=[
                {
                    "id": "d8e57222-43c6-4fd7-b928-4a8ae106fe98",
                    "time_stamp": "2022-04-07T04:58:19.900Z",
                    "metric": 4,
                    "isCool": True,
                },
                {
                    "id": "31a17418-ec6e-4b3a-9056-b5c17278d053",
                    "time_stamp": "2022-04-08T04:58:19.900Z",
                    "metric": 0,
                    "isCool": False,
                },
            ],
            data_point_name="activities",
            x_transcend_nonce="x-transcend-nonce",
            file_id="History 04/07 - 04/08",
            is_last_page=True,
            x_sombra_authorization="x-sombra-authorization",
        )
        assert_matches_type(object, datapoint_chunked, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_upload(self, client: Transcend) -> None:
        response = client.datapoint_chunked.with_raw_response.upload(
            data=[
                {
                    "id": "d8e57222-43c6-4fd7-b928-4a8ae106fe98",
                    "time_stamp": "2022-04-07T04:58:19.900Z",
                    "metric": 4,
                    "isCool": True,
                },
                {
                    "id": "31a17418-ec6e-4b3a-9056-b5c17278d053",
                    "time_stamp": "2022-04-08T04:58:19.900Z",
                    "metric": 0,
                    "isCool": False,
                },
            ],
            data_point_name="activities",
            x_transcend_nonce="x-transcend-nonce",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        datapoint_chunked = response.parse()
        assert_matches_type(object, datapoint_chunked, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_upload(self, client: Transcend) -> None:
        with client.datapoint_chunked.with_streaming_response.upload(
            data=[
                {
                    "id": "d8e57222-43c6-4fd7-b928-4a8ae106fe98",
                    "time_stamp": "2022-04-07T04:58:19.900Z",
                    "metric": 4,
                    "isCool": True,
                },
                {
                    "id": "31a17418-ec6e-4b3a-9056-b5c17278d053",
                    "time_stamp": "2022-04-08T04:58:19.900Z",
                    "metric": 0,
                    "isCool": False,
                },
            ],
            data_point_name="activities",
            x_transcend_nonce="x-transcend-nonce",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            datapoint_chunked = response.parse()
            assert_matches_type(object, datapoint_chunked, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncDatapointChunked:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_upload(self, async_client: AsyncTranscend) -> None:
        datapoint_chunked = await async_client.datapoint_chunked.upload(
            data=[
                {
                    "id": "d8e57222-43c6-4fd7-b928-4a8ae106fe98",
                    "time_stamp": "2022-04-07T04:58:19.900Z",
                    "metric": 4,
                    "isCool": True,
                },
                {
                    "id": "31a17418-ec6e-4b3a-9056-b5c17278d053",
                    "time_stamp": "2022-04-08T04:58:19.900Z",
                    "metric": 0,
                    "isCool": False,
                },
            ],
            data_point_name="activities",
            x_transcend_nonce="x-transcend-nonce",
        )
        assert_matches_type(object, datapoint_chunked, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_upload_with_all_params(self, async_client: AsyncTranscend) -> None:
        datapoint_chunked = await async_client.datapoint_chunked.upload(
            data=[
                {
                    "id": "d8e57222-43c6-4fd7-b928-4a8ae106fe98",
                    "time_stamp": "2022-04-07T04:58:19.900Z",
                    "metric": 4,
                    "isCool": True,
                },
                {
                    "id": "31a17418-ec6e-4b3a-9056-b5c17278d053",
                    "time_stamp": "2022-04-08T04:58:19.900Z",
                    "metric": 0,
                    "isCool": False,
                },
            ],
            data_point_name="activities",
            x_transcend_nonce="x-transcend-nonce",
            file_id="History 04/07 - 04/08",
            is_last_page=True,
            x_sombra_authorization="x-sombra-authorization",
        )
        assert_matches_type(object, datapoint_chunked, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_upload(self, async_client: AsyncTranscend) -> None:
        response = await async_client.datapoint_chunked.with_raw_response.upload(
            data=[
                {
                    "id": "d8e57222-43c6-4fd7-b928-4a8ae106fe98",
                    "time_stamp": "2022-04-07T04:58:19.900Z",
                    "metric": 4,
                    "isCool": True,
                },
                {
                    "id": "31a17418-ec6e-4b3a-9056-b5c17278d053",
                    "time_stamp": "2022-04-08T04:58:19.900Z",
                    "metric": 0,
                    "isCool": False,
                },
            ],
            data_point_name="activities",
            x_transcend_nonce="x-transcend-nonce",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        datapoint_chunked = await response.parse()
        assert_matches_type(object, datapoint_chunked, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_upload(self, async_client: AsyncTranscend) -> None:
        async with async_client.datapoint_chunked.with_streaming_response.upload(
            data=[
                {
                    "id": "d8e57222-43c6-4fd7-b928-4a8ae106fe98",
                    "time_stamp": "2022-04-07T04:58:19.900Z",
                    "metric": 4,
                    "isCool": True,
                },
                {
                    "id": "31a17418-ec6e-4b3a-9056-b5c17278d053",
                    "time_stamp": "2022-04-08T04:58:19.900Z",
                    "metric": 0,
                    "isCool": False,
                },
            ],
            data_point_name="activities",
            x_transcend_nonce="x-transcend-nonce",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            datapoint_chunked = await response.parse()
            assert_matches_type(object, datapoint_chunked, path=["response"])

        assert cast(Any, response.is_closed) is True
