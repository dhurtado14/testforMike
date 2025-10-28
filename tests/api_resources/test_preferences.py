# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from transcend import Transcend, AsyncTranscend
from tests.utils import assert_matches_type
from transcend.types import (
    PreferenceQueryResponse,
    PreferenceUpsertResponse,
)
from transcend._utils import parse_datetime

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestPreferences:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_query(self, client: Transcend) -> None:
        preference = client.preferences.query(
            partition="partition",
        )
        assert_matches_type(PreferenceQueryResponse, preference, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_query_with_all_params(self, client: Transcend) -> None:
        preference = client.preferences.query(
            partition="partition",
            filter={
                "identifiers": [
                    {
                        "value": "no-track@example.com",
                        "name": "email",
                    }
                ]
            },
            limit=1,
            x_sombra_authorization="x-sombra-authorization",
        )
        assert_matches_type(PreferenceQueryResponse, preference, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_query(self, client: Transcend) -> None:
        response = client.preferences.with_raw_response.query(
            partition="partition",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        preference = response.parse()
        assert_matches_type(PreferenceQueryResponse, preference, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_query(self, client: Transcend) -> None:
        with client.preferences.with_streaming_response.query(
            partition="partition",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            preference = response.parse()
            assert_matches_type(PreferenceQueryResponse, preference, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_query(self, client: Transcend) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `partition` but received ''"):
            client.preferences.with_raw_response.query(
                partition="",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_upsert(self, client: Transcend) -> None:
        preference = client.preferences.upsert(
            records=[
                {
                    "identifiers": [
                        {
                            "name": "email",
                            "value": "no-track@example.com",
                        },
                        {
                            "name": "phone",
                            "value": "+11234567890",
                        },
                    ],
                    "partition": "ea3a0845-694e-4820-9d51-50c7d0a23467",
                    "purposes": [
                        {
                            "enabled": True,
                            "purpose": "Advertising",
                        },
                        {
                            "enabled": False,
                            "purpose": "Analytics",
                        },
                        {
                            "enabled": True,
                            "purpose": "ProductUpdates",
                        },
                    ],
                    "timestamp": parse_datetime("2023-05-11T19:32:31.707Z"),
                },
                {
                    "identifiers": [
                        {
                            "name": "email",
                            "value": "no-track-pls@example.com",
                        }
                    ],
                    "partition": "ea3a0845-694e-4820-9d51-50c7d0a2346",
                    "purposes": [
                        {
                            "enabled": True,
                            "purpose": "Advertising",
                        },
                        {
                            "enabled": True,
                            "purpose": "Analytics",
                        },
                        {
                            "enabled": False,
                            "purpose": "ProductUpdates",
                        },
                    ],
                    "timestamp": parse_datetime("2023-05-11T19:32:31.707Z"),
                },
            ],
        )
        assert_matches_type(PreferenceUpsertResponse, preference, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_upsert_with_all_params(self, client: Transcend) -> None:
        preference = client.preferences.upsert(
            records=[
                {
                    "identifiers": [
                        {
                            "name": "email",
                            "value": "no-track@example.com",
                        },
                        {
                            "name": "phone",
                            "value": "+11234567890",
                        },
                    ],
                    "partition": "ea3a0845-694e-4820-9d51-50c7d0a23467",
                    "purposes": [
                        {
                            "enabled": True,
                            "purpose": "Advertising",
                            "preferences": [
                                {
                                    "choice": {
                                        "boolean_value": True,
                                        "select_value": "selectValue",
                                        "select_values": ["string"],
                                    },
                                    "topic": "topic",
                                }
                            ],
                            "workflow_settings": {
                                "attributes": [
                                    {
                                        "key": "x",
                                        "values": ["string"],
                                    }
                                ],
                                "data_silo_ids": ["string"],
                                "ignore_data_silo_ids": ["string"],
                                "is_silent": True,
                                "is_test": True,
                                "region": {
                                    "country": "EU",
                                    "country_sub_division": "AD-02",
                                },
                                "skip_sending_receipt": True,
                                "skip_waiting_period": True,
                                "skip_workflow_trigger": True,
                            },
                        },
                        {
                            "enabled": False,
                            "purpose": "Analytics",
                            "preferences": [
                                {
                                    "choice": {
                                        "boolean_value": True,
                                        "select_value": "selectValue",
                                        "select_values": ["string"],
                                    },
                                    "topic": "topic",
                                }
                            ],
                            "workflow_settings": {
                                "attributes": [
                                    {
                                        "key": "x",
                                        "values": ["string"],
                                    }
                                ],
                                "data_silo_ids": ["string"],
                                "ignore_data_silo_ids": ["string"],
                                "is_silent": True,
                                "is_test": True,
                                "region": {
                                    "country": "EU",
                                    "country_sub_division": "AD-02",
                                },
                                "skip_sending_receipt": True,
                                "skip_waiting_period": True,
                                "skip_workflow_trigger": True,
                            },
                        },
                        {
                            "enabled": True,
                            "purpose": "ProductUpdates",
                            "preferences": [
                                {
                                    "choice": {
                                        "boolean_value": True,
                                        "select_value": "Weekly",
                                        "select_values": ["string"],
                                    },
                                    "topic": "Frequency",
                                },
                                {
                                    "choice": {
                                        "boolean_value": True,
                                        "select_value": "selectValue",
                                        "select_values": ["Email", "Sms"],
                                    },
                                    "topic": "Channel",
                                },
                                {
                                    "choice": {
                                        "boolean_value": True,
                                        "select_value": "selectValue",
                                        "select_values": ["string"],
                                    },
                                    "topic": "Unsubscribe",
                                },
                            ],
                            "workflow_settings": {
                                "attributes": [
                                    {
                                        "key": "Source",
                                        "values": ["Mobile iOS App"],
                                    }
                                ],
                                "data_silo_ids": ["string"],
                                "ignore_data_silo_ids": ["string"],
                                "is_silent": True,
                                "is_test": True,
                                "region": {
                                    "country": "EU",
                                    "country_sub_division": "AD-02",
                                },
                                "skip_sending_receipt": True,
                                "skip_waiting_period": True,
                                "skip_workflow_trigger": True,
                            },
                        },
                    ],
                    "timestamp": parse_datetime("2023-05-11T19:32:31.707Z"),
                    "consent_management": {
                        "gpp": "gpp",
                        "tcf": "tcf",
                        "usp": "usp",
                    },
                    "locale": "en",
                    "metadata": [
                        {
                            "key": "version",
                            "value": "1.0.0",
                        }
                    ],
                },
                {
                    "identifiers": [
                        {
                            "name": "email",
                            "value": "no-track-pls@example.com",
                        }
                    ],
                    "partition": "ea3a0845-694e-4820-9d51-50c7d0a2346",
                    "purposes": [
                        {
                            "enabled": True,
                            "purpose": "Advertising",
                            "preferences": [
                                {
                                    "choice": {
                                        "boolean_value": True,
                                        "select_value": "selectValue",
                                        "select_values": ["string"],
                                    },
                                    "topic": "topic",
                                }
                            ],
                            "workflow_settings": {
                                "attributes": [
                                    {
                                        "key": "x",
                                        "values": ["string"],
                                    }
                                ],
                                "data_silo_ids": ["string"],
                                "ignore_data_silo_ids": ["string"],
                                "is_silent": True,
                                "is_test": True,
                                "region": {
                                    "country": "EU",
                                    "country_sub_division": "AD-02",
                                },
                                "skip_sending_receipt": True,
                                "skip_waiting_period": True,
                                "skip_workflow_trigger": True,
                            },
                        },
                        {
                            "enabled": True,
                            "purpose": "Analytics",
                            "preferences": [
                                {
                                    "choice": {
                                        "boolean_value": True,
                                        "select_value": "selectValue",
                                        "select_values": ["string"],
                                    },
                                    "topic": "topic",
                                }
                            ],
                            "workflow_settings": {
                                "attributes": [
                                    {
                                        "key": "x",
                                        "values": ["string"],
                                    }
                                ],
                                "data_silo_ids": ["string"],
                                "ignore_data_silo_ids": ["string"],
                                "is_silent": True,
                                "is_test": True,
                                "region": {
                                    "country": "EU",
                                    "country_sub_division": "AD-02",
                                },
                                "skip_sending_receipt": True,
                                "skip_waiting_period": True,
                                "skip_workflow_trigger": True,
                            },
                        },
                        {
                            "enabled": False,
                            "purpose": "ProductUpdates",
                            "preferences": [
                                {
                                    "choice": {
                                        "boolean_value": True,
                                        "select_value": "selectValue",
                                        "select_values": ["string"],
                                    },
                                    "topic": "topic",
                                }
                            ],
                            "workflow_settings": {
                                "attributes": [
                                    {
                                        "key": "x",
                                        "values": ["string"],
                                    }
                                ],
                                "data_silo_ids": ["string"],
                                "ignore_data_silo_ids": ["string"],
                                "is_silent": True,
                                "is_test": True,
                                "region": {
                                    "country": "EU",
                                    "country_sub_division": "AD-02",
                                },
                                "skip_sending_receipt": True,
                                "skip_waiting_period": True,
                                "skip_workflow_trigger": True,
                            },
                        },
                    ],
                    "timestamp": parse_datetime("2023-05-11T19:32:31.707Z"),
                    "consent_management": {
                        "gpp": "gpp",
                        "tcf": "tcf",
                        "usp": "usp",
                    },
                    "locale": "en",
                    "metadata": [
                        {
                            "key": "version",
                            "value": "1.0.0",
                        }
                    ],
                },
            ],
            skip_workflow_triggers=False,
            x_sombra_authorization="x-sombra-authorization",
        )
        assert_matches_type(PreferenceUpsertResponse, preference, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_upsert(self, client: Transcend) -> None:
        response = client.preferences.with_raw_response.upsert(
            records=[
                {
                    "identifiers": [
                        {
                            "name": "email",
                            "value": "no-track@example.com",
                        },
                        {
                            "name": "phone",
                            "value": "+11234567890",
                        },
                    ],
                    "partition": "ea3a0845-694e-4820-9d51-50c7d0a23467",
                    "purposes": [
                        {
                            "enabled": True,
                            "purpose": "Advertising",
                        },
                        {
                            "enabled": False,
                            "purpose": "Analytics",
                        },
                        {
                            "enabled": True,
                            "purpose": "ProductUpdates",
                        },
                    ],
                    "timestamp": parse_datetime("2023-05-11T19:32:31.707Z"),
                },
                {
                    "identifiers": [
                        {
                            "name": "email",
                            "value": "no-track-pls@example.com",
                        }
                    ],
                    "partition": "ea3a0845-694e-4820-9d51-50c7d0a2346",
                    "purposes": [
                        {
                            "enabled": True,
                            "purpose": "Advertising",
                        },
                        {
                            "enabled": True,
                            "purpose": "Analytics",
                        },
                        {
                            "enabled": False,
                            "purpose": "ProductUpdates",
                        },
                    ],
                    "timestamp": parse_datetime("2023-05-11T19:32:31.707Z"),
                },
            ],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        preference = response.parse()
        assert_matches_type(PreferenceUpsertResponse, preference, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_upsert(self, client: Transcend) -> None:
        with client.preferences.with_streaming_response.upsert(
            records=[
                {
                    "identifiers": [
                        {
                            "name": "email",
                            "value": "no-track@example.com",
                        },
                        {
                            "name": "phone",
                            "value": "+11234567890",
                        },
                    ],
                    "partition": "ea3a0845-694e-4820-9d51-50c7d0a23467",
                    "purposes": [
                        {
                            "enabled": True,
                            "purpose": "Advertising",
                        },
                        {
                            "enabled": False,
                            "purpose": "Analytics",
                        },
                        {
                            "enabled": True,
                            "purpose": "ProductUpdates",
                        },
                    ],
                    "timestamp": parse_datetime("2023-05-11T19:32:31.707Z"),
                },
                {
                    "identifiers": [
                        {
                            "name": "email",
                            "value": "no-track-pls@example.com",
                        }
                    ],
                    "partition": "ea3a0845-694e-4820-9d51-50c7d0a2346",
                    "purposes": [
                        {
                            "enabled": True,
                            "purpose": "Advertising",
                        },
                        {
                            "enabled": True,
                            "purpose": "Analytics",
                        },
                        {
                            "enabled": False,
                            "purpose": "ProductUpdates",
                        },
                    ],
                    "timestamp": parse_datetime("2023-05-11T19:32:31.707Z"),
                },
            ],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            preference = response.parse()
            assert_matches_type(PreferenceUpsertResponse, preference, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncPreferences:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_query(self, async_client: AsyncTranscend) -> None:
        preference = await async_client.preferences.query(
            partition="partition",
        )
        assert_matches_type(PreferenceQueryResponse, preference, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_query_with_all_params(self, async_client: AsyncTranscend) -> None:
        preference = await async_client.preferences.query(
            partition="partition",
            filter={
                "identifiers": [
                    {
                        "value": "no-track@example.com",
                        "name": "email",
                    }
                ]
            },
            limit=1,
            x_sombra_authorization="x-sombra-authorization",
        )
        assert_matches_type(PreferenceQueryResponse, preference, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_query(self, async_client: AsyncTranscend) -> None:
        response = await async_client.preferences.with_raw_response.query(
            partition="partition",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        preference = await response.parse()
        assert_matches_type(PreferenceQueryResponse, preference, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_query(self, async_client: AsyncTranscend) -> None:
        async with async_client.preferences.with_streaming_response.query(
            partition="partition",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            preference = await response.parse()
            assert_matches_type(PreferenceQueryResponse, preference, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_query(self, async_client: AsyncTranscend) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `partition` but received ''"):
            await async_client.preferences.with_raw_response.query(
                partition="",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_upsert(self, async_client: AsyncTranscend) -> None:
        preference = await async_client.preferences.upsert(
            records=[
                {
                    "identifiers": [
                        {
                            "name": "email",
                            "value": "no-track@example.com",
                        },
                        {
                            "name": "phone",
                            "value": "+11234567890",
                        },
                    ],
                    "partition": "ea3a0845-694e-4820-9d51-50c7d0a23467",
                    "purposes": [
                        {
                            "enabled": True,
                            "purpose": "Advertising",
                        },
                        {
                            "enabled": False,
                            "purpose": "Analytics",
                        },
                        {
                            "enabled": True,
                            "purpose": "ProductUpdates",
                        },
                    ],
                    "timestamp": parse_datetime("2023-05-11T19:32:31.707Z"),
                },
                {
                    "identifiers": [
                        {
                            "name": "email",
                            "value": "no-track-pls@example.com",
                        }
                    ],
                    "partition": "ea3a0845-694e-4820-9d51-50c7d0a2346",
                    "purposes": [
                        {
                            "enabled": True,
                            "purpose": "Advertising",
                        },
                        {
                            "enabled": True,
                            "purpose": "Analytics",
                        },
                        {
                            "enabled": False,
                            "purpose": "ProductUpdates",
                        },
                    ],
                    "timestamp": parse_datetime("2023-05-11T19:32:31.707Z"),
                },
            ],
        )
        assert_matches_type(PreferenceUpsertResponse, preference, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_upsert_with_all_params(self, async_client: AsyncTranscend) -> None:
        preference = await async_client.preferences.upsert(
            records=[
                {
                    "identifiers": [
                        {
                            "name": "email",
                            "value": "no-track@example.com",
                        },
                        {
                            "name": "phone",
                            "value": "+11234567890",
                        },
                    ],
                    "partition": "ea3a0845-694e-4820-9d51-50c7d0a23467",
                    "purposes": [
                        {
                            "enabled": True,
                            "purpose": "Advertising",
                            "preferences": [
                                {
                                    "choice": {
                                        "boolean_value": True,
                                        "select_value": "selectValue",
                                        "select_values": ["string"],
                                    },
                                    "topic": "topic",
                                }
                            ],
                            "workflow_settings": {
                                "attributes": [
                                    {
                                        "key": "x",
                                        "values": ["string"],
                                    }
                                ],
                                "data_silo_ids": ["string"],
                                "ignore_data_silo_ids": ["string"],
                                "is_silent": True,
                                "is_test": True,
                                "region": {
                                    "country": "EU",
                                    "country_sub_division": "AD-02",
                                },
                                "skip_sending_receipt": True,
                                "skip_waiting_period": True,
                                "skip_workflow_trigger": True,
                            },
                        },
                        {
                            "enabled": False,
                            "purpose": "Analytics",
                            "preferences": [
                                {
                                    "choice": {
                                        "boolean_value": True,
                                        "select_value": "selectValue",
                                        "select_values": ["string"],
                                    },
                                    "topic": "topic",
                                }
                            ],
                            "workflow_settings": {
                                "attributes": [
                                    {
                                        "key": "x",
                                        "values": ["string"],
                                    }
                                ],
                                "data_silo_ids": ["string"],
                                "ignore_data_silo_ids": ["string"],
                                "is_silent": True,
                                "is_test": True,
                                "region": {
                                    "country": "EU",
                                    "country_sub_division": "AD-02",
                                },
                                "skip_sending_receipt": True,
                                "skip_waiting_period": True,
                                "skip_workflow_trigger": True,
                            },
                        },
                        {
                            "enabled": True,
                            "purpose": "ProductUpdates",
                            "preferences": [
                                {
                                    "choice": {
                                        "boolean_value": True,
                                        "select_value": "Weekly",
                                        "select_values": ["string"],
                                    },
                                    "topic": "Frequency",
                                },
                                {
                                    "choice": {
                                        "boolean_value": True,
                                        "select_value": "selectValue",
                                        "select_values": ["Email", "Sms"],
                                    },
                                    "topic": "Channel",
                                },
                                {
                                    "choice": {
                                        "boolean_value": True,
                                        "select_value": "selectValue",
                                        "select_values": ["string"],
                                    },
                                    "topic": "Unsubscribe",
                                },
                            ],
                            "workflow_settings": {
                                "attributes": [
                                    {
                                        "key": "Source",
                                        "values": ["Mobile iOS App"],
                                    }
                                ],
                                "data_silo_ids": ["string"],
                                "ignore_data_silo_ids": ["string"],
                                "is_silent": True,
                                "is_test": True,
                                "region": {
                                    "country": "EU",
                                    "country_sub_division": "AD-02",
                                },
                                "skip_sending_receipt": True,
                                "skip_waiting_period": True,
                                "skip_workflow_trigger": True,
                            },
                        },
                    ],
                    "timestamp": parse_datetime("2023-05-11T19:32:31.707Z"),
                    "consent_management": {
                        "gpp": "gpp",
                        "tcf": "tcf",
                        "usp": "usp",
                    },
                    "locale": "en",
                    "metadata": [
                        {
                            "key": "version",
                            "value": "1.0.0",
                        }
                    ],
                },
                {
                    "identifiers": [
                        {
                            "name": "email",
                            "value": "no-track-pls@example.com",
                        }
                    ],
                    "partition": "ea3a0845-694e-4820-9d51-50c7d0a2346",
                    "purposes": [
                        {
                            "enabled": True,
                            "purpose": "Advertising",
                            "preferences": [
                                {
                                    "choice": {
                                        "boolean_value": True,
                                        "select_value": "selectValue",
                                        "select_values": ["string"],
                                    },
                                    "topic": "topic",
                                }
                            ],
                            "workflow_settings": {
                                "attributes": [
                                    {
                                        "key": "x",
                                        "values": ["string"],
                                    }
                                ],
                                "data_silo_ids": ["string"],
                                "ignore_data_silo_ids": ["string"],
                                "is_silent": True,
                                "is_test": True,
                                "region": {
                                    "country": "EU",
                                    "country_sub_division": "AD-02",
                                },
                                "skip_sending_receipt": True,
                                "skip_waiting_period": True,
                                "skip_workflow_trigger": True,
                            },
                        },
                        {
                            "enabled": True,
                            "purpose": "Analytics",
                            "preferences": [
                                {
                                    "choice": {
                                        "boolean_value": True,
                                        "select_value": "selectValue",
                                        "select_values": ["string"],
                                    },
                                    "topic": "topic",
                                }
                            ],
                            "workflow_settings": {
                                "attributes": [
                                    {
                                        "key": "x",
                                        "values": ["string"],
                                    }
                                ],
                                "data_silo_ids": ["string"],
                                "ignore_data_silo_ids": ["string"],
                                "is_silent": True,
                                "is_test": True,
                                "region": {
                                    "country": "EU",
                                    "country_sub_division": "AD-02",
                                },
                                "skip_sending_receipt": True,
                                "skip_waiting_period": True,
                                "skip_workflow_trigger": True,
                            },
                        },
                        {
                            "enabled": False,
                            "purpose": "ProductUpdates",
                            "preferences": [
                                {
                                    "choice": {
                                        "boolean_value": True,
                                        "select_value": "selectValue",
                                        "select_values": ["string"],
                                    },
                                    "topic": "topic",
                                }
                            ],
                            "workflow_settings": {
                                "attributes": [
                                    {
                                        "key": "x",
                                        "values": ["string"],
                                    }
                                ],
                                "data_silo_ids": ["string"],
                                "ignore_data_silo_ids": ["string"],
                                "is_silent": True,
                                "is_test": True,
                                "region": {
                                    "country": "EU",
                                    "country_sub_division": "AD-02",
                                },
                                "skip_sending_receipt": True,
                                "skip_waiting_period": True,
                                "skip_workflow_trigger": True,
                            },
                        },
                    ],
                    "timestamp": parse_datetime("2023-05-11T19:32:31.707Z"),
                    "consent_management": {
                        "gpp": "gpp",
                        "tcf": "tcf",
                        "usp": "usp",
                    },
                    "locale": "en",
                    "metadata": [
                        {
                            "key": "version",
                            "value": "1.0.0",
                        }
                    ],
                },
            ],
            skip_workflow_triggers=False,
            x_sombra_authorization="x-sombra-authorization",
        )
        assert_matches_type(PreferenceUpsertResponse, preference, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_upsert(self, async_client: AsyncTranscend) -> None:
        response = await async_client.preferences.with_raw_response.upsert(
            records=[
                {
                    "identifiers": [
                        {
                            "name": "email",
                            "value": "no-track@example.com",
                        },
                        {
                            "name": "phone",
                            "value": "+11234567890",
                        },
                    ],
                    "partition": "ea3a0845-694e-4820-9d51-50c7d0a23467",
                    "purposes": [
                        {
                            "enabled": True,
                            "purpose": "Advertising",
                        },
                        {
                            "enabled": False,
                            "purpose": "Analytics",
                        },
                        {
                            "enabled": True,
                            "purpose": "ProductUpdates",
                        },
                    ],
                    "timestamp": parse_datetime("2023-05-11T19:32:31.707Z"),
                },
                {
                    "identifiers": [
                        {
                            "name": "email",
                            "value": "no-track-pls@example.com",
                        }
                    ],
                    "partition": "ea3a0845-694e-4820-9d51-50c7d0a2346",
                    "purposes": [
                        {
                            "enabled": True,
                            "purpose": "Advertising",
                        },
                        {
                            "enabled": True,
                            "purpose": "Analytics",
                        },
                        {
                            "enabled": False,
                            "purpose": "ProductUpdates",
                        },
                    ],
                    "timestamp": parse_datetime("2023-05-11T19:32:31.707Z"),
                },
            ],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        preference = await response.parse()
        assert_matches_type(PreferenceUpsertResponse, preference, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_upsert(self, async_client: AsyncTranscend) -> None:
        async with async_client.preferences.with_streaming_response.upsert(
            records=[
                {
                    "identifiers": [
                        {
                            "name": "email",
                            "value": "no-track@example.com",
                        },
                        {
                            "name": "phone",
                            "value": "+11234567890",
                        },
                    ],
                    "partition": "ea3a0845-694e-4820-9d51-50c7d0a23467",
                    "purposes": [
                        {
                            "enabled": True,
                            "purpose": "Advertising",
                        },
                        {
                            "enabled": False,
                            "purpose": "Analytics",
                        },
                        {
                            "enabled": True,
                            "purpose": "ProductUpdates",
                        },
                    ],
                    "timestamp": parse_datetime("2023-05-11T19:32:31.707Z"),
                },
                {
                    "identifiers": [
                        {
                            "name": "email",
                            "value": "no-track-pls@example.com",
                        }
                    ],
                    "partition": "ea3a0845-694e-4820-9d51-50c7d0a2346",
                    "purposes": [
                        {
                            "enabled": True,
                            "purpose": "Advertising",
                        },
                        {
                            "enabled": True,
                            "purpose": "Analytics",
                        },
                        {
                            "enabled": False,
                            "purpose": "ProductUpdates",
                        },
                    ],
                    "timestamp": parse_datetime("2023-05-11T19:32:31.707Z"),
                },
            ],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            preference = await response.parse()
            assert_matches_type(PreferenceUpsertResponse, preference, path=["response"])

        assert cast(Any, response.is_closed) is True
