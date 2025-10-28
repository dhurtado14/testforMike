# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from transcend import Transcend, AsyncTranscend
from tests.utils import assert_matches_type

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestPublicKeys:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_retrieve_signing_key(self, client: Transcend) -> None:
        public_key = client.public_keys.retrieve_signing_key()
        assert_matches_type(str, public_key, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_retrieve_signing_key(self, client: Transcend) -> None:
        response = client.public_keys.with_raw_response.retrieve_signing_key()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        public_key = response.parse()
        assert_matches_type(str, public_key, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_retrieve_signing_key(self, client: Transcend) -> None:
        with client.public_keys.with_streaming_response.retrieve_signing_key() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            public_key = response.parse()
            assert_matches_type(str, public_key, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncPublicKeys:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_retrieve_signing_key(self, async_client: AsyncTranscend) -> None:
        public_key = await async_client.public_keys.retrieve_signing_key()
        assert_matches_type(str, public_key, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_retrieve_signing_key(self, async_client: AsyncTranscend) -> None:
        response = await async_client.public_keys.with_raw_response.retrieve_signing_key()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        public_key = await response.parse()
        assert_matches_type(str, public_key, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve_signing_key(self, async_client: AsyncTranscend) -> None:
        async with async_client.public_keys.with_streaming_response.retrieve_signing_key() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            public_key = await response.parse()
            assert_matches_type(str, public_key, path=["response"])

        assert cast(Any, response.is_closed) is True
