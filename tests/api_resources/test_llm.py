# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from transcend import Transcend, AsyncTranscend
from tests.utils import assert_matches_type
from transcend.types import LlmClassifyTextResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestLlm:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_classify_text(self, client: Transcend) -> None:
        llm = client.llm.classify_text(
            input_list=["+141562712314", "user@gmail.com", "transcend user ID"],
            labels=["Personal Identifier", "Medical", "Generic Personal Information"],
        )
        assert_matches_type(LlmClassifyTextResponse, llm, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_classify_text_with_all_params(self, client: Transcend) -> None:
        llm = client.llm.classify_text(
            input_list=["+141562712314", "user@gmail.com", "transcend user ID"],
            labels=["Personal Identifier", "Medical", "Generic Personal Information"],
            x_sombra_authorization="x-sombra-authorization",
        )
        assert_matches_type(LlmClassifyTextResponse, llm, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_classify_text(self, client: Transcend) -> None:
        response = client.llm.with_raw_response.classify_text(
            input_list=["+141562712314", "user@gmail.com", "transcend user ID"],
            labels=["Personal Identifier", "Medical", "Generic Personal Information"],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        llm = response.parse()
        assert_matches_type(LlmClassifyTextResponse, llm, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_classify_text(self, client: Transcend) -> None:
        with client.llm.with_streaming_response.classify_text(
            input_list=["+141562712314", "user@gmail.com", "transcend user ID"],
            labels=["Personal Identifier", "Medical", "Generic Personal Information"],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            llm = response.parse()
            assert_matches_type(LlmClassifyTextResponse, llm, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncLlm:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_classify_text(self, async_client: AsyncTranscend) -> None:
        llm = await async_client.llm.classify_text(
            input_list=["+141562712314", "user@gmail.com", "transcend user ID"],
            labels=["Personal Identifier", "Medical", "Generic Personal Information"],
        )
        assert_matches_type(LlmClassifyTextResponse, llm, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_classify_text_with_all_params(self, async_client: AsyncTranscend) -> None:
        llm = await async_client.llm.classify_text(
            input_list=["+141562712314", "user@gmail.com", "transcend user ID"],
            labels=["Personal Identifier", "Medical", "Generic Personal Information"],
            x_sombra_authorization="x-sombra-authorization",
        )
        assert_matches_type(LlmClassifyTextResponse, llm, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_classify_text(self, async_client: AsyncTranscend) -> None:
        response = await async_client.llm.with_raw_response.classify_text(
            input_list=["+141562712314", "user@gmail.com", "transcend user ID"],
            labels=["Personal Identifier", "Medical", "Generic Personal Information"],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        llm = await response.parse()
        assert_matches_type(LlmClassifyTextResponse, llm, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_classify_text(self, async_client: AsyncTranscend) -> None:
        async with async_client.llm.with_streaming_response.classify_text(
            input_list=["+141562712314", "user@gmail.com", "transcend user ID"],
            labels=["Personal Identifier", "Medical", "Generic Personal Information"],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            llm = await response.parse()
            assert_matches_type(LlmClassifyTextResponse, llm, path=["response"])

        assert cast(Any, response.is_closed) is True
