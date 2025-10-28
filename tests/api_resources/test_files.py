# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import httpx
import pytest
from respx import MockRouter

from transcend import Transcend, AsyncTranscend
from transcend._response import (
    BinaryAPIResponse,
    AsyncBinaryAPIResponse,
    StreamedBinaryAPIResponse,
    AsyncStreamedBinaryAPIResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestFiles:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    def test_method_download(self, client: Transcend, respx_mock: MockRouter) -> None:
        respx_mock.get("/v1/files").mock(return_value=httpx.Response(200, json={"foo": "bar"}))
        file = client.files.download(
            download_key="downloadKey",
        )
        assert file.is_closed
        assert file.json() == {"foo": "bar"}
        assert cast(Any, file.is_closed) is True
        assert isinstance(file, BinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    def test_method_download_with_all_params(self, client: Transcend, respx_mock: MockRouter) -> None:
        respx_mock.get("/v1/files").mock(return_value=httpx.Response(200, json={"foo": "bar"}))
        file = client.files.download(
            download_key="downloadKey",
            x_sombra_authorization="x-sombra-authorization",
        )
        assert file.is_closed
        assert file.json() == {"foo": "bar"}
        assert cast(Any, file.is_closed) is True
        assert isinstance(file, BinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    def test_raw_response_download(self, client: Transcend, respx_mock: MockRouter) -> None:
        respx_mock.get("/v1/files").mock(return_value=httpx.Response(200, json={"foo": "bar"}))

        file = client.files.with_raw_response.download(
            download_key="downloadKey",
        )

        assert file.is_closed is True
        assert file.http_request.headers.get("X-Stainless-Lang") == "python"
        assert file.json() == {"foo": "bar"}
        assert isinstance(file, BinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    def test_streaming_response_download(self, client: Transcend, respx_mock: MockRouter) -> None:
        respx_mock.get("/v1/files").mock(return_value=httpx.Response(200, json={"foo": "bar"}))
        with client.files.with_streaming_response.download(
            download_key="downloadKey",
        ) as file:
            assert not file.is_closed
            assert file.http_request.headers.get("X-Stainless-Lang") == "python"

            assert file.json() == {"foo": "bar"}
            assert cast(Any, file.is_closed) is True
            assert isinstance(file, StreamedBinaryAPIResponse)

        assert cast(Any, file.is_closed) is True


class TestAsyncFiles:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    async def test_method_download(self, async_client: AsyncTranscend, respx_mock: MockRouter) -> None:
        respx_mock.get("/v1/files").mock(return_value=httpx.Response(200, json={"foo": "bar"}))
        file = await async_client.files.download(
            download_key="downloadKey",
        )
        assert file.is_closed
        assert await file.json() == {"foo": "bar"}
        assert cast(Any, file.is_closed) is True
        assert isinstance(file, AsyncBinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    async def test_method_download_with_all_params(self, async_client: AsyncTranscend, respx_mock: MockRouter) -> None:
        respx_mock.get("/v1/files").mock(return_value=httpx.Response(200, json={"foo": "bar"}))
        file = await async_client.files.download(
            download_key="downloadKey",
            x_sombra_authorization="x-sombra-authorization",
        )
        assert file.is_closed
        assert await file.json() == {"foo": "bar"}
        assert cast(Any, file.is_closed) is True
        assert isinstance(file, AsyncBinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    async def test_raw_response_download(self, async_client: AsyncTranscend, respx_mock: MockRouter) -> None:
        respx_mock.get("/v1/files").mock(return_value=httpx.Response(200, json={"foo": "bar"}))

        file = await async_client.files.with_raw_response.download(
            download_key="downloadKey",
        )

        assert file.is_closed is True
        assert file.http_request.headers.get("X-Stainless-Lang") == "python"
        assert await file.json() == {"foo": "bar"}
        assert isinstance(file, AsyncBinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    async def test_streaming_response_download(self, async_client: AsyncTranscend, respx_mock: MockRouter) -> None:
        respx_mock.get("/v1/files").mock(return_value=httpx.Response(200, json={"foo": "bar"}))
        async with async_client.files.with_streaming_response.download(
            download_key="downloadKey",
        ) as file:
            assert not file.is_closed
            assert file.http_request.headers.get("X-Stainless-Lang") == "python"

            assert await file.json() == {"foo": "bar"}
            assert cast(Any, file.is_closed) is True
            assert isinstance(file, AsyncStreamedBinaryAPIResponse)

        assert cast(Any, file.is_closed) is True
