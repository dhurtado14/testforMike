# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from transcend import Transcend, AsyncTranscend
from tests.utils import assert_matches_type
from transcend.types import ClassifyClassifyUnstructuredTextResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestClassify:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_classify_unstructured_text(self, client: Transcend) -> None:
        classify = client.classify.classify_unstructured_text(
            input_list=['"userId":"05179687877722385190"', "Medical ID: 15179687877722385199", "transcend user ID"],
            labels=["Personal Identifier", "Medical", "Generic Personal Information"],
        )
        assert_matches_type(ClassifyClassifyUnstructuredTextResponse, classify, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_classify_unstructured_text_with_all_params(self, client: Transcend) -> None:
        classify = client.classify.classify_unstructured_text(
            input_list=['"userId":"05179687877722385190"', "Medical ID: 15179687877722385199", "transcend user ID"],
            labels=["Personal Identifier", "Medical", "Generic Personal Information"],
            x_sombra_authorization="x-sombra-authorization",
        )
        assert_matches_type(ClassifyClassifyUnstructuredTextResponse, classify, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_classify_unstructured_text(self, client: Transcend) -> None:
        response = client.classify.with_raw_response.classify_unstructured_text(
            input_list=['"userId":"05179687877722385190"', "Medical ID: 15179687877722385199", "transcend user ID"],
            labels=["Personal Identifier", "Medical", "Generic Personal Information"],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        classify = response.parse()
        assert_matches_type(ClassifyClassifyUnstructuredTextResponse, classify, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_classify_unstructured_text(self, client: Transcend) -> None:
        with client.classify.with_streaming_response.classify_unstructured_text(
            input_list=['"userId":"05179687877722385190"', "Medical ID: 15179687877722385199", "transcend user ID"],
            labels=["Personal Identifier", "Medical", "Generic Personal Information"],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            classify = response.parse()
            assert_matches_type(ClassifyClassifyUnstructuredTextResponse, classify, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncClassify:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_classify_unstructured_text(self, async_client: AsyncTranscend) -> None:
        classify = await async_client.classify.classify_unstructured_text(
            input_list=['"userId":"05179687877722385190"', "Medical ID: 15179687877722385199", "transcend user ID"],
            labels=["Personal Identifier", "Medical", "Generic Personal Information"],
        )
        assert_matches_type(ClassifyClassifyUnstructuredTextResponse, classify, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_classify_unstructured_text_with_all_params(self, async_client: AsyncTranscend) -> None:
        classify = await async_client.classify.classify_unstructured_text(
            input_list=['"userId":"05179687877722385190"', "Medical ID: 15179687877722385199", "transcend user ID"],
            labels=["Personal Identifier", "Medical", "Generic Personal Information"],
            x_sombra_authorization="x-sombra-authorization",
        )
        assert_matches_type(ClassifyClassifyUnstructuredTextResponse, classify, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_classify_unstructured_text(self, async_client: AsyncTranscend) -> None:
        response = await async_client.classify.with_raw_response.classify_unstructured_text(
            input_list=['"userId":"05179687877722385190"', "Medical ID: 15179687877722385199", "transcend user ID"],
            labels=["Personal Identifier", "Medical", "Generic Personal Information"],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        classify = await response.parse()
        assert_matches_type(ClassifyClassifyUnstructuredTextResponse, classify, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_classify_unstructured_text(self, async_client: AsyncTranscend) -> None:
        async with async_client.classify.with_streaming_response.classify_unstructured_text(
            input_list=['"userId":"05179687877722385190"', "Medical ID: 15179687877722385199", "transcend user ID"],
            labels=["Personal Identifier", "Medical", "Generic Personal Information"],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            classify = await response.parse()
            assert_matches_type(ClassifyClassifyUnstructuredTextResponse, classify, path=["response"])

        assert cast(Any, response.is_closed) is True
