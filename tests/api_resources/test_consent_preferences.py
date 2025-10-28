# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from transcend import Transcend, AsyncTranscend
from tests.utils import assert_matches_type
from transcend.types import ConsentPreferenceDeprecatedCreateResponse
from transcend._utils import parse_datetime

# pyright: reportDeprecated=false

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestConsentPreferences:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_deprecated_create(self, client: Transcend) -> None:
        with pytest.warns(DeprecationWarning):
            consent_preference = client.consent_preferences.deprecated_create(
                partition="ea3a0845-694e-4820-9d51-50c7d0a23467",
            )

        assert_matches_type(ConsentPreferenceDeprecatedCreateResponse, consent_preference, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_deprecated_create_with_all_params(self, client: Transcend) -> None:
        with pytest.warns(DeprecationWarning):
            consent_preference = client.consent_preferences.deprecated_create(
                partition="ea3a0845-694e-4820-9d51-50c7d0a23467",
                identifiers=["no-track@example.com"],
                limit=0,
                start_key={
                    "decryption_status": "DECRYPTED",
                    "partition": "partition",
                    "user_id": "userId",
                    "timestamp": parse_datetime("2019-12-27T18:11:19.117Z"),
                    "updated_at": parse_datetime("2019-12-27T18:11:19.117Z"),
                },
                timestamp_after=parse_datetime("2019-12-27T18:11:19.117Z"),
                timestamp_before=parse_datetime("2019-12-27T18:11:19.117Z"),
                updated_after=parse_datetime("2019-12-27T18:11:19.117Z"),
                updated_before=parse_datetime("2019-12-27T18:11:19.117Z"),
                x_sombra_authorization="x-sombra-authorization",
            )

        assert_matches_type(ConsentPreferenceDeprecatedCreateResponse, consent_preference, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_deprecated_create(self, client: Transcend) -> None:
        with pytest.warns(DeprecationWarning):
            response = client.consent_preferences.with_raw_response.deprecated_create(
                partition="ea3a0845-694e-4820-9d51-50c7d0a23467",
            )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        consent_preference = response.parse()
        assert_matches_type(ConsentPreferenceDeprecatedCreateResponse, consent_preference, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_deprecated_create(self, client: Transcend) -> None:
        with pytest.warns(DeprecationWarning):
            with client.consent_preferences.with_streaming_response.deprecated_create(
                partition="ea3a0845-694e-4820-9d51-50c7d0a23467",
            ) as response:
                assert not response.is_closed
                assert response.http_request.headers.get("X-Stainless-Lang") == "python"

                consent_preference = response.parse()
                assert_matches_type(ConsentPreferenceDeprecatedCreateResponse, consent_preference, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncConsentPreferences:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_deprecated_create(self, async_client: AsyncTranscend) -> None:
        with pytest.warns(DeprecationWarning):
            consent_preference = await async_client.consent_preferences.deprecated_create(
                partition="ea3a0845-694e-4820-9d51-50c7d0a23467",
            )

        assert_matches_type(ConsentPreferenceDeprecatedCreateResponse, consent_preference, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_deprecated_create_with_all_params(self, async_client: AsyncTranscend) -> None:
        with pytest.warns(DeprecationWarning):
            consent_preference = await async_client.consent_preferences.deprecated_create(
                partition="ea3a0845-694e-4820-9d51-50c7d0a23467",
                identifiers=["no-track@example.com"],
                limit=0,
                start_key={
                    "decryption_status": "DECRYPTED",
                    "partition": "partition",
                    "user_id": "userId",
                    "timestamp": parse_datetime("2019-12-27T18:11:19.117Z"),
                    "updated_at": parse_datetime("2019-12-27T18:11:19.117Z"),
                },
                timestamp_after=parse_datetime("2019-12-27T18:11:19.117Z"),
                timestamp_before=parse_datetime("2019-12-27T18:11:19.117Z"),
                updated_after=parse_datetime("2019-12-27T18:11:19.117Z"),
                updated_before=parse_datetime("2019-12-27T18:11:19.117Z"),
                x_sombra_authorization="x-sombra-authorization",
            )

        assert_matches_type(ConsentPreferenceDeprecatedCreateResponse, consent_preference, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_deprecated_create(self, async_client: AsyncTranscend) -> None:
        with pytest.warns(DeprecationWarning):
            response = await async_client.consent_preferences.with_raw_response.deprecated_create(
                partition="ea3a0845-694e-4820-9d51-50c7d0a23467",
            )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        consent_preference = await response.parse()
        assert_matches_type(ConsentPreferenceDeprecatedCreateResponse, consent_preference, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_deprecated_create(self, async_client: AsyncTranscend) -> None:
        with pytest.warns(DeprecationWarning):
            async with async_client.consent_preferences.with_streaming_response.deprecated_create(
                partition="ea3a0845-694e-4820-9d51-50c7d0a23467",
            ) as response:
                assert not response.is_closed
                assert response.http_request.headers.get("X-Stainless-Lang") == "python"

                consent_preference = await response.parse()
                assert_matches_type(ConsentPreferenceDeprecatedCreateResponse, consent_preference, path=["response"])

        assert cast(Any, response.is_closed) is True
