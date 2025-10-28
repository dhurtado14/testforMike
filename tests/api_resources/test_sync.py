# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from transcend import Transcend, AsyncTranscend
from tests.utils import assert_matches_type
from transcend.types import (
    SyncGetConsentPreferencesResponse,
    SyncSetConsentPreferencesResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestSync:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_get_consent_preferences(self, client: Transcend) -> None:
        sync = client.sync.get_consent_preferences(
            partition="partition",
        )
        assert_matches_type(SyncGetConsentPreferencesResponse, sync, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_get_consent_preferences(self, client: Transcend) -> None:
        response = client.sync.with_raw_response.get_consent_preferences(
            partition="partition",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        sync = response.parse()
        assert_matches_type(SyncGetConsentPreferencesResponse, sync, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_get_consent_preferences(self, client: Transcend) -> None:
        with client.sync.with_streaming_response.get_consent_preferences(
            partition="partition",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            sync = response.parse()
            assert_matches_type(SyncGetConsentPreferencesResponse, sync, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_set_consent_preferences(self, client: Transcend) -> None:
        sync = client.sync.set_consent_preferences(
            token="eyJhbGciOiJIUzM4NCIsInR5cCI6IkpXVCJ9.eyJlbmNyeXB0ZWRJZGVudGlmaWVyIjoiRkg2TitkZWdWY2IzNlgzMWF2L1p4dz09IiwiaWF0IjoxNjgzNjQ0OTQyfQ.IRNqiXOz8oYJuWqdWfstgIjmQ9B_uJ-gvkw1mT5uUT-G9xdlPJ7zeODCCvlNIbf_",
            consent={
                "confirmed": True,
                "purposes": {"TestPurpose": False},
                "timestamp": "2023-05-11T19:32:31.707Z",
            },
            partition="7b9916f1-a9f7-45bd-b6d4-4bd7decfddaa",
        )
        assert_matches_type(SyncSetConsentPreferencesResponse, sync, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_set_consent_preferences_with_all_params(self, client: Transcend) -> None:
        sync = client.sync.set_consent_preferences(
            token="eyJhbGciOiJIUzM4NCIsInR5cCI6IkpXVCJ9.eyJlbmNyeXB0ZWRJZGVudGlmaWVyIjoiRkg2TitkZWdWY2IzNlgzMWF2L1p4dz09IiwiaWF0IjoxNjgzNjQ0OTQyfQ.IRNqiXOz8oYJuWqdWfstgIjmQ9B_uJ-gvkw1mT5uUT-G9xdlPJ7zeODCCvlNIbf_",
            consent={
                "confirmed": True,
                "purposes": {"TestPurpose": False},
                "timestamp": "2023-05-11T19:32:31.707Z",
                "prompted": True,
                "updated": True,
            },
            partition="7b9916f1-a9f7-45bd-b6d4-4bd7decfddaa",
        )
        assert_matches_type(SyncSetConsentPreferencesResponse, sync, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_set_consent_preferences(self, client: Transcend) -> None:
        response = client.sync.with_raw_response.set_consent_preferences(
            token="eyJhbGciOiJIUzM4NCIsInR5cCI6IkpXVCJ9.eyJlbmNyeXB0ZWRJZGVudGlmaWVyIjoiRkg2TitkZWdWY2IzNlgzMWF2L1p4dz09IiwiaWF0IjoxNjgzNjQ0OTQyfQ.IRNqiXOz8oYJuWqdWfstgIjmQ9B_uJ-gvkw1mT5uUT-G9xdlPJ7zeODCCvlNIbf_",
            consent={
                "confirmed": True,
                "purposes": {"TestPurpose": False},
                "timestamp": "2023-05-11T19:32:31.707Z",
            },
            partition="7b9916f1-a9f7-45bd-b6d4-4bd7decfddaa",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        sync = response.parse()
        assert_matches_type(SyncSetConsentPreferencesResponse, sync, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_set_consent_preferences(self, client: Transcend) -> None:
        with client.sync.with_streaming_response.set_consent_preferences(
            token="eyJhbGciOiJIUzM4NCIsInR5cCI6IkpXVCJ9.eyJlbmNyeXB0ZWRJZGVudGlmaWVyIjoiRkg2TitkZWdWY2IzNlgzMWF2L1p4dz09IiwiaWF0IjoxNjgzNjQ0OTQyfQ.IRNqiXOz8oYJuWqdWfstgIjmQ9B_uJ-gvkw1mT5uUT-G9xdlPJ7zeODCCvlNIbf_",
            consent={
                "confirmed": True,
                "purposes": {"TestPurpose": False},
                "timestamp": "2023-05-11T19:32:31.707Z",
            },
            partition="7b9916f1-a9f7-45bd-b6d4-4bd7decfddaa",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            sync = response.parse()
            assert_matches_type(SyncSetConsentPreferencesResponse, sync, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncSync:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_get_consent_preferences(self, async_client: AsyncTranscend) -> None:
        sync = await async_client.sync.get_consent_preferences(
            partition="partition",
        )
        assert_matches_type(SyncGetConsentPreferencesResponse, sync, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_get_consent_preferences(self, async_client: AsyncTranscend) -> None:
        response = await async_client.sync.with_raw_response.get_consent_preferences(
            partition="partition",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        sync = await response.parse()
        assert_matches_type(SyncGetConsentPreferencesResponse, sync, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_get_consent_preferences(self, async_client: AsyncTranscend) -> None:
        async with async_client.sync.with_streaming_response.get_consent_preferences(
            partition="partition",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            sync = await response.parse()
            assert_matches_type(SyncGetConsentPreferencesResponse, sync, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_set_consent_preferences(self, async_client: AsyncTranscend) -> None:
        sync = await async_client.sync.set_consent_preferences(
            token="eyJhbGciOiJIUzM4NCIsInR5cCI6IkpXVCJ9.eyJlbmNyeXB0ZWRJZGVudGlmaWVyIjoiRkg2TitkZWdWY2IzNlgzMWF2L1p4dz09IiwiaWF0IjoxNjgzNjQ0OTQyfQ.IRNqiXOz8oYJuWqdWfstgIjmQ9B_uJ-gvkw1mT5uUT-G9xdlPJ7zeODCCvlNIbf_",
            consent={
                "confirmed": True,
                "purposes": {"TestPurpose": False},
                "timestamp": "2023-05-11T19:32:31.707Z",
            },
            partition="7b9916f1-a9f7-45bd-b6d4-4bd7decfddaa",
        )
        assert_matches_type(SyncSetConsentPreferencesResponse, sync, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_set_consent_preferences_with_all_params(self, async_client: AsyncTranscend) -> None:
        sync = await async_client.sync.set_consent_preferences(
            token="eyJhbGciOiJIUzM4NCIsInR5cCI6IkpXVCJ9.eyJlbmNyeXB0ZWRJZGVudGlmaWVyIjoiRkg2TitkZWdWY2IzNlgzMWF2L1p4dz09IiwiaWF0IjoxNjgzNjQ0OTQyfQ.IRNqiXOz8oYJuWqdWfstgIjmQ9B_uJ-gvkw1mT5uUT-G9xdlPJ7zeODCCvlNIbf_",
            consent={
                "confirmed": True,
                "purposes": {"TestPurpose": False},
                "timestamp": "2023-05-11T19:32:31.707Z",
                "prompted": True,
                "updated": True,
            },
            partition="7b9916f1-a9f7-45bd-b6d4-4bd7decfddaa",
        )
        assert_matches_type(SyncSetConsentPreferencesResponse, sync, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_set_consent_preferences(self, async_client: AsyncTranscend) -> None:
        response = await async_client.sync.with_raw_response.set_consent_preferences(
            token="eyJhbGciOiJIUzM4NCIsInR5cCI6IkpXVCJ9.eyJlbmNyeXB0ZWRJZGVudGlmaWVyIjoiRkg2TitkZWdWY2IzNlgzMWF2L1p4dz09IiwiaWF0IjoxNjgzNjQ0OTQyfQ.IRNqiXOz8oYJuWqdWfstgIjmQ9B_uJ-gvkw1mT5uUT-G9xdlPJ7zeODCCvlNIbf_",
            consent={
                "confirmed": True,
                "purposes": {"TestPurpose": False},
                "timestamp": "2023-05-11T19:32:31.707Z",
            },
            partition="7b9916f1-a9f7-45bd-b6d4-4bd7decfddaa",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        sync = await response.parse()
        assert_matches_type(SyncSetConsentPreferencesResponse, sync, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_set_consent_preferences(self, async_client: AsyncTranscend) -> None:
        async with async_client.sync.with_streaming_response.set_consent_preferences(
            token="eyJhbGciOiJIUzM4NCIsInR5cCI6IkpXVCJ9.eyJlbmNyeXB0ZWRJZGVudGlmaWVyIjoiRkg2TitkZWdWY2IzNlgzMWF2L1p4dz09IiwiaWF0IjoxNjgzNjQ0OTQyfQ.IRNqiXOz8oYJuWqdWfstgIjmQ9B_uJ-gvkw1mT5uUT-G9xdlPJ7zeODCCvlNIbf_",
            consent={
                "confirmed": True,
                "purposes": {"TestPurpose": False},
                "timestamp": "2023-05-11T19:32:31.707Z",
            },
            partition="7b9916f1-a9f7-45bd-b6d4-4bd7decfddaa",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            sync = await response.parse()
            assert_matches_type(SyncSetConsentPreferencesResponse, sync, path=["response"])

        assert cast(Any, response.is_closed) is True
