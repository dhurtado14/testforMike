# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from transcend import Transcend, AsyncTranscend
from tests.utils import assert_matches_type

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestEnrichIdentifiers:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_create(self, client: Transcend) -> None:
        enrich_identifier = client.enrich_identifiers.create(
            x_transcend_nonce="x-transcend-nonce",
        )
        assert_matches_type(object, enrich_identifier, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_create_with_all_params(self, client: Transcend) -> None:
        enrich_identifier = client.enrich_identifiers.create(
            x_transcend_nonce="x-transcend-nonce",
            enriched_identifiers={
                "googleAnalyticsInternalId": [{"value": "SOME-GOOGLE-ANALYTICS-ID"}],
                "gpadvid": [{"value": "b20f48d8-9f50-447a-a446-1d398a9f9b1b"}],
            },
            status="CANCELED",
            template_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            template_title="templateTitle",
            x_sombra_authorization="x-sombra-authorization",
        )
        assert_matches_type(object, enrich_identifier, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_create(self, client: Transcend) -> None:
        response = client.enrich_identifiers.with_raw_response.create(
            x_transcend_nonce="x-transcend-nonce",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        enrich_identifier = response.parse()
        assert_matches_type(object, enrich_identifier, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_create(self, client: Transcend) -> None:
        with client.enrich_identifiers.with_streaming_response.create(
            x_transcend_nonce="x-transcend-nonce",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            enrich_identifier = response.parse()
            assert_matches_type(object, enrich_identifier, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncEnrichIdentifiers:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_create(self, async_client: AsyncTranscend) -> None:
        enrich_identifier = await async_client.enrich_identifiers.create(
            x_transcend_nonce="x-transcend-nonce",
        )
        assert_matches_type(object, enrich_identifier, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncTranscend) -> None:
        enrich_identifier = await async_client.enrich_identifiers.create(
            x_transcend_nonce="x-transcend-nonce",
            enriched_identifiers={
                "googleAnalyticsInternalId": [{"value": "SOME-GOOGLE-ANALYTICS-ID"}],
                "gpadvid": [{"value": "b20f48d8-9f50-447a-a446-1d398a9f9b1b"}],
            },
            status="CANCELED",
            template_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            template_title="templateTitle",
            x_sombra_authorization="x-sombra-authorization",
        )
        assert_matches_type(object, enrich_identifier, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_create(self, async_client: AsyncTranscend) -> None:
        response = await async_client.enrich_identifiers.with_raw_response.create(
            x_transcend_nonce="x-transcend-nonce",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        enrich_identifier = await response.parse()
        assert_matches_type(object, enrich_identifier, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncTranscend) -> None:
        async with async_client.enrich_identifiers.with_streaming_response.create(
            x_transcend_nonce="x-transcend-nonce",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            enrich_identifier = await response.parse()
            assert_matches_type(object, enrich_identifier, path=["response"])

        assert cast(Any, response.is_closed) is True
