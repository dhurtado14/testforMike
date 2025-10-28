# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from transcend import Transcend, AsyncTranscend
from tests.utils import assert_matches_type
from transcend.types import RequestIdentifierCreateResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestRequestIdentifiers:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_create(self, client: Transcend) -> None:
        request_identifier = client.request_identifiers.create(
            request_id="96946f0d-6453-4d52-9d66-d5f2089acbc1",
        )
        assert_matches_type(RequestIdentifierCreateResponse, request_identifier, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_create_with_all_params(self, client: Transcend) -> None:
        request_identifier = client.request_identifiers.create(
            request_id="96946f0d-6453-4d52-9d66-d5f2089acbc1",
            first=100,
            offset=0,
            x_sombra_authorization="x-sombra-authorization",
        )
        assert_matches_type(RequestIdentifierCreateResponse, request_identifier, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_create(self, client: Transcend) -> None:
        response = client.request_identifiers.with_raw_response.create(
            request_id="96946f0d-6453-4d52-9d66-d5f2089acbc1",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        request_identifier = response.parse()
        assert_matches_type(RequestIdentifierCreateResponse, request_identifier, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_create(self, client: Transcend) -> None:
        with client.request_identifiers.with_streaming_response.create(
            request_id="96946f0d-6453-4d52-9d66-d5f2089acbc1",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            request_identifier = response.parse()
            assert_matches_type(RequestIdentifierCreateResponse, request_identifier, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncRequestIdentifiers:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_create(self, async_client: AsyncTranscend) -> None:
        request_identifier = await async_client.request_identifiers.create(
            request_id="96946f0d-6453-4d52-9d66-d5f2089acbc1",
        )
        assert_matches_type(RequestIdentifierCreateResponse, request_identifier, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncTranscend) -> None:
        request_identifier = await async_client.request_identifiers.create(
            request_id="96946f0d-6453-4d52-9d66-d5f2089acbc1",
            first=100,
            offset=0,
            x_sombra_authorization="x-sombra-authorization",
        )
        assert_matches_type(RequestIdentifierCreateResponse, request_identifier, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_create(self, async_client: AsyncTranscend) -> None:
        response = await async_client.request_identifiers.with_raw_response.create(
            request_id="96946f0d-6453-4d52-9d66-d5f2089acbc1",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        request_identifier = await response.parse()
        assert_matches_type(RequestIdentifierCreateResponse, request_identifier, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncTranscend) -> None:
        async with async_client.request_identifiers.with_streaming_response.create(
            request_id="96946f0d-6453-4d52-9d66-d5f2089acbc1",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            request_identifier = await response.parse()
            assert_matches_type(RequestIdentifierCreateResponse, request_identifier, path=["response"])

        assert cast(Any, response.is_closed) is True
