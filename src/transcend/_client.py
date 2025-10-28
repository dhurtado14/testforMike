# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, Dict, Mapping, cast
from typing_extensions import Self, Literal, override

import httpx

from . import _exceptions
from ._qs import Querystring
from ._types import (
    Omit,
    Timeout,
    NotGiven,
    Transport,
    ProxiesTypes,
    RequestOptions,
    not_given,
)
from ._utils import is_given, get_async_library
from ._version import __version__
from .resources import (
    llm,
    sync,
    files,
    classify,
    data_silo,
    datapoint,
    preferences,
    public_keys,
    datapoint_chunked,
    enrich_identifiers,
    consent_preferences,
    request_identifiers,
    data_subject_request,
)
from ._streaming import Stream as Stream, AsyncStream as AsyncStream
from ._exceptions import APIStatusError, TranscendError
from ._base_client import (
    DEFAULT_MAX_RETRIES,
    SyncAPIClient,
    AsyncAPIClient,
)

__all__ = [
    "ENVIRONMENTS",
    "Timeout",
    "Transport",
    "ProxiesTypes",
    "RequestOptions",
    "Transcend",
    "AsyncTranscend",
    "Client",
    "AsyncClient",
]

ENVIRONMENTS: Dict[str, str] = {
    "production": "https://multi-tenant.sombra.transcend.io",
    "environment_1": "https://multi-tenant.sombra.us.transcend.io",
    "environment_2": "https://_yourOrganizationSombraURL_.com",
    "environment_3": "https://consent.transcend.io",
    "environment_4": "https://consent.us.transcend.io",
}


class Transcend(SyncAPIClient):
    llm: llm.LlmResource
    classify: classify.ClassifyResource
    public_keys: public_keys.PublicKeysResource
    datapoint: datapoint.DatapointResource
    datapoint_chunked: datapoint_chunked.DatapointChunkedResource
    data_silo: data_silo.DataSiloResource
    enrich_identifiers: enrich_identifiers.EnrichIdentifiersResource
    request_identifiers: request_identifiers.RequestIdentifiersResource
    data_subject_request: data_subject_request.DataSubjectRequestResource
    files: files.FilesResource
    consent_preferences: consent_preferences.ConsentPreferencesResource
    preferences: preferences.PreferencesResource
    sync: sync.SyncResource
    with_raw_response: TranscendWithRawResponse
    with_streaming_response: TranscendWithStreamedResponse

    # client options
    api_key: str
    bearer_token: str

    _environment: Literal["production", "environment_1", "environment_2", "environment_3", "environment_4"] | NotGiven

    def __init__(
        self,
        *,
        api_key: str | None = None,
        bearer_token: str | None = None,
        environment: Literal["production", "environment_1", "environment_2", "environment_3", "environment_4"]
        | NotGiven = not_given,
        base_url: str | httpx.URL | None | NotGiven = not_given,
        timeout: float | Timeout | None | NotGiven = not_given,
        max_retries: int = DEFAULT_MAX_RETRIES,
        default_headers: Mapping[str, str] | None = None,
        default_query: Mapping[str, object] | None = None,
        # Configure a custom httpx client.
        # We provide a `DefaultHttpxClient` class that you can pass to retain the default values we use for `limits`, `timeout` & `follow_redirects`.
        # See the [httpx documentation](https://www.python-httpx.org/api/#client) for more details.
        http_client: httpx.Client | None = None,
        # Enable or disable schema validation for data returned by the API.
        # When enabled an error APIResponseValidationError is raised
        # if the API responds with invalid data for the expected schema.
        #
        # This parameter may be removed or changed in the future.
        # If you rely on this feature, please open a GitHub issue
        # outlining your use-case to help us decide if it should be
        # part of our public interface in the future.
        _strict_response_validation: bool = False,
    ) -> None:
        """Construct a new synchronous Transcend client instance.

        This automatically infers the following arguments from their corresponding environment variables if they are not provided:
        - `api_key` from `TRANSCEND_API_KEY`
        - `bearer_token` from `TRANSCEND_BEARER_TOKEN`
        """
        if api_key is None:
            api_key = os.environ.get("TRANSCEND_API_KEY")
        if api_key is None:
            raise TranscendError(
                "The api_key client option must be set either by passing api_key to the client or by setting the TRANSCEND_API_KEY environment variable"
            )
        self.api_key = api_key

        if bearer_token is None:
            bearer_token = os.environ.get("TRANSCEND_BEARER_TOKEN")
        if bearer_token is None:
            raise TranscendError(
                "The bearer_token client option must be set either by passing bearer_token to the client or by setting the TRANSCEND_BEARER_TOKEN environment variable"
            )
        self.bearer_token = bearer_token

        self._environment = environment

        base_url_env = os.environ.get("TRANSCEND_BASE_URL")
        if is_given(base_url) and base_url is not None:
            # cast required because mypy doesn't understand the type narrowing
            base_url = cast("str | httpx.URL", base_url)  # pyright: ignore[reportUnnecessaryCast]
        elif is_given(environment):
            if base_url_env and base_url is not None:
                raise ValueError(
                    "Ambiguous URL; The `TRANSCEND_BASE_URL` env var and the `environment` argument are given. If you want to use the environment, you must pass base_url=None",
                )

            try:
                base_url = ENVIRONMENTS[environment]
            except KeyError as exc:
                raise ValueError(f"Unknown environment: {environment}") from exc
        elif base_url_env is not None:
            base_url = base_url_env
        else:
            self._environment = environment = "production"

            try:
                base_url = ENVIRONMENTS[environment]
            except KeyError as exc:
                raise ValueError(f"Unknown environment: {environment}") from exc

        super().__init__(
            version=__version__,
            base_url=base_url,
            max_retries=max_retries,
            timeout=timeout,
            http_client=http_client,
            custom_headers=default_headers,
            custom_query=default_query,
            _strict_response_validation=_strict_response_validation,
        )

        self.llm = llm.LlmResource(self)
        self.classify = classify.ClassifyResource(self)
        self.public_keys = public_keys.PublicKeysResource(self)
        self.datapoint = datapoint.DatapointResource(self)
        self.datapoint_chunked = datapoint_chunked.DatapointChunkedResource(self)
        self.data_silo = data_silo.DataSiloResource(self)
        self.enrich_identifiers = enrich_identifiers.EnrichIdentifiersResource(self)
        self.request_identifiers = request_identifiers.RequestIdentifiersResource(self)
        self.data_subject_request = data_subject_request.DataSubjectRequestResource(self)
        self.files = files.FilesResource(self)
        self.consent_preferences = consent_preferences.ConsentPreferencesResource(self)
        self.preferences = preferences.PreferencesResource(self)
        self.sync = sync.SyncResource(self)
        self.with_raw_response = TranscendWithRawResponse(self)
        self.with_streaming_response = TranscendWithStreamedResponse(self)

    @property
    @override
    def qs(self) -> Querystring:
        return Querystring(array_format="comma")

    @property
    @override
    def auth_headers(self) -> dict[str, str]:
        return {**self._transcend_api_key_if_multitenant, **self._sombra_token}

    @property
    def _transcend_api_key_if_multitenant(self) -> dict[str, str]:
        bearer_token = self.bearer_token
        return {"Authorization": f"Bearer {bearer_token}"}

    @property
    def _sombra_token(self) -> dict[str, str]:
        api_key = self.api_key
        return {"Authorization": f"Bearer {api_key}"}

    @property
    @override
    def default_headers(self) -> dict[str, str | Omit]:
        return {
            **super().default_headers,
            "X-Stainless-Async": "false",
            **self._custom_headers,
        }

    def copy(
        self,
        *,
        api_key: str | None = None,
        bearer_token: str | None = None,
        environment: Literal["production", "environment_1", "environment_2", "environment_3", "environment_4"]
        | None = None,
        base_url: str | httpx.URL | None = None,
        timeout: float | Timeout | None | NotGiven = not_given,
        http_client: httpx.Client | None = None,
        max_retries: int | NotGiven = not_given,
        default_headers: Mapping[str, str] | None = None,
        set_default_headers: Mapping[str, str] | None = None,
        default_query: Mapping[str, object] | None = None,
        set_default_query: Mapping[str, object] | None = None,
        _extra_kwargs: Mapping[str, Any] = {},
    ) -> Self:
        """
        Create a new client instance re-using the same options given to the current client with optional overriding.
        """
        if default_headers is not None and set_default_headers is not None:
            raise ValueError("The `default_headers` and `set_default_headers` arguments are mutually exclusive")

        if default_query is not None and set_default_query is not None:
            raise ValueError("The `default_query` and `set_default_query` arguments are mutually exclusive")

        headers = self._custom_headers
        if default_headers is not None:
            headers = {**headers, **default_headers}
        elif set_default_headers is not None:
            headers = set_default_headers

        params = self._custom_query
        if default_query is not None:
            params = {**params, **default_query}
        elif set_default_query is not None:
            params = set_default_query

        http_client = http_client or self._client
        return self.__class__(
            api_key=api_key or self.api_key,
            bearer_token=bearer_token or self.bearer_token,
            base_url=base_url or self.base_url,
            environment=environment or self._environment,
            timeout=self.timeout if isinstance(timeout, NotGiven) else timeout,
            http_client=http_client,
            max_retries=max_retries if is_given(max_retries) else self.max_retries,
            default_headers=headers,
            default_query=params,
            **_extra_kwargs,
        )

    # Alias for `copy` for nicer inline usage, e.g.
    # client.with_options(timeout=10).foo.create(...)
    with_options = copy

    @override
    def _make_status_error(
        self,
        err_msg: str,
        *,
        body: object,
        response: httpx.Response,
    ) -> APIStatusError:
        if response.status_code == 400:
            return _exceptions.BadRequestError(err_msg, response=response, body=body)

        if response.status_code == 401:
            return _exceptions.AuthenticationError(err_msg, response=response, body=body)

        if response.status_code == 403:
            return _exceptions.PermissionDeniedError(err_msg, response=response, body=body)

        if response.status_code == 404:
            return _exceptions.NotFoundError(err_msg, response=response, body=body)

        if response.status_code == 409:
            return _exceptions.ConflictError(err_msg, response=response, body=body)

        if response.status_code == 422:
            return _exceptions.UnprocessableEntityError(err_msg, response=response, body=body)

        if response.status_code == 429:
            return _exceptions.RateLimitError(err_msg, response=response, body=body)

        if response.status_code >= 500:
            return _exceptions.InternalServerError(err_msg, response=response, body=body)
        return APIStatusError(err_msg, response=response, body=body)


class AsyncTranscend(AsyncAPIClient):
    llm: llm.AsyncLlmResource
    classify: classify.AsyncClassifyResource
    public_keys: public_keys.AsyncPublicKeysResource
    datapoint: datapoint.AsyncDatapointResource
    datapoint_chunked: datapoint_chunked.AsyncDatapointChunkedResource
    data_silo: data_silo.AsyncDataSiloResource
    enrich_identifiers: enrich_identifiers.AsyncEnrichIdentifiersResource
    request_identifiers: request_identifiers.AsyncRequestIdentifiersResource
    data_subject_request: data_subject_request.AsyncDataSubjectRequestResource
    files: files.AsyncFilesResource
    consent_preferences: consent_preferences.AsyncConsentPreferencesResource
    preferences: preferences.AsyncPreferencesResource
    sync: sync.AsyncSyncResource
    with_raw_response: AsyncTranscendWithRawResponse
    with_streaming_response: AsyncTranscendWithStreamedResponse

    # client options
    api_key: str
    bearer_token: str

    _environment: Literal["production", "environment_1", "environment_2", "environment_3", "environment_4"] | NotGiven

    def __init__(
        self,
        *,
        api_key: str | None = None,
        bearer_token: str | None = None,
        environment: Literal["production", "environment_1", "environment_2", "environment_3", "environment_4"]
        | NotGiven = not_given,
        base_url: str | httpx.URL | None | NotGiven = not_given,
        timeout: float | Timeout | None | NotGiven = not_given,
        max_retries: int = DEFAULT_MAX_RETRIES,
        default_headers: Mapping[str, str] | None = None,
        default_query: Mapping[str, object] | None = None,
        # Configure a custom httpx client.
        # We provide a `DefaultAsyncHttpxClient` class that you can pass to retain the default values we use for `limits`, `timeout` & `follow_redirects`.
        # See the [httpx documentation](https://www.python-httpx.org/api/#asyncclient) for more details.
        http_client: httpx.AsyncClient | None = None,
        # Enable or disable schema validation for data returned by the API.
        # When enabled an error APIResponseValidationError is raised
        # if the API responds with invalid data for the expected schema.
        #
        # This parameter may be removed or changed in the future.
        # If you rely on this feature, please open a GitHub issue
        # outlining your use-case to help us decide if it should be
        # part of our public interface in the future.
        _strict_response_validation: bool = False,
    ) -> None:
        """Construct a new async AsyncTranscend client instance.

        This automatically infers the following arguments from their corresponding environment variables if they are not provided:
        - `api_key` from `TRANSCEND_API_KEY`
        - `bearer_token` from `TRANSCEND_BEARER_TOKEN`
        """
        if api_key is None:
            api_key = os.environ.get("TRANSCEND_API_KEY")
        if api_key is None:
            raise TranscendError(
                "The api_key client option must be set either by passing api_key to the client or by setting the TRANSCEND_API_KEY environment variable"
            )
        self.api_key = api_key

        if bearer_token is None:
            bearer_token = os.environ.get("TRANSCEND_BEARER_TOKEN")
        if bearer_token is None:
            raise TranscendError(
                "The bearer_token client option must be set either by passing bearer_token to the client or by setting the TRANSCEND_BEARER_TOKEN environment variable"
            )
        self.bearer_token = bearer_token

        self._environment = environment

        base_url_env = os.environ.get("TRANSCEND_BASE_URL")
        if is_given(base_url) and base_url is not None:
            # cast required because mypy doesn't understand the type narrowing
            base_url = cast("str | httpx.URL", base_url)  # pyright: ignore[reportUnnecessaryCast]
        elif is_given(environment):
            if base_url_env and base_url is not None:
                raise ValueError(
                    "Ambiguous URL; The `TRANSCEND_BASE_URL` env var and the `environment` argument are given. If you want to use the environment, you must pass base_url=None",
                )

            try:
                base_url = ENVIRONMENTS[environment]
            except KeyError as exc:
                raise ValueError(f"Unknown environment: {environment}") from exc
        elif base_url_env is not None:
            base_url = base_url_env
        else:
            self._environment = environment = "production"

            try:
                base_url = ENVIRONMENTS[environment]
            except KeyError as exc:
                raise ValueError(f"Unknown environment: {environment}") from exc

        super().__init__(
            version=__version__,
            base_url=base_url,
            max_retries=max_retries,
            timeout=timeout,
            http_client=http_client,
            custom_headers=default_headers,
            custom_query=default_query,
            _strict_response_validation=_strict_response_validation,
        )

        self.llm = llm.AsyncLlmResource(self)
        self.classify = classify.AsyncClassifyResource(self)
        self.public_keys = public_keys.AsyncPublicKeysResource(self)
        self.datapoint = datapoint.AsyncDatapointResource(self)
        self.datapoint_chunked = datapoint_chunked.AsyncDatapointChunkedResource(self)
        self.data_silo = data_silo.AsyncDataSiloResource(self)
        self.enrich_identifiers = enrich_identifiers.AsyncEnrichIdentifiersResource(self)
        self.request_identifiers = request_identifiers.AsyncRequestIdentifiersResource(self)
        self.data_subject_request = data_subject_request.AsyncDataSubjectRequestResource(self)
        self.files = files.AsyncFilesResource(self)
        self.consent_preferences = consent_preferences.AsyncConsentPreferencesResource(self)
        self.preferences = preferences.AsyncPreferencesResource(self)
        self.sync = sync.AsyncSyncResource(self)
        self.with_raw_response = AsyncTranscendWithRawResponse(self)
        self.with_streaming_response = AsyncTranscendWithStreamedResponse(self)

    @property
    @override
    def qs(self) -> Querystring:
        return Querystring(array_format="comma")

    @property
    @override
    def auth_headers(self) -> dict[str, str]:
        return {**self._transcend_api_key_if_multitenant, **self._sombra_token}

    @property
    def _transcend_api_key_if_multitenant(self) -> dict[str, str]:
        bearer_token = self.bearer_token
        return {"Authorization": f"Bearer {bearer_token}"}

    @property
    def _sombra_token(self) -> dict[str, str]:
        api_key = self.api_key
        return {"Authorization": f"Bearer {api_key}"}

    @property
    @override
    def default_headers(self) -> dict[str, str | Omit]:
        return {
            **super().default_headers,
            "X-Stainless-Async": f"async:{get_async_library()}",
            **self._custom_headers,
        }

    def copy(
        self,
        *,
        api_key: str | None = None,
        bearer_token: str | None = None,
        environment: Literal["production", "environment_1", "environment_2", "environment_3", "environment_4"]
        | None = None,
        base_url: str | httpx.URL | None = None,
        timeout: float | Timeout | None | NotGiven = not_given,
        http_client: httpx.AsyncClient | None = None,
        max_retries: int | NotGiven = not_given,
        default_headers: Mapping[str, str] | None = None,
        set_default_headers: Mapping[str, str] | None = None,
        default_query: Mapping[str, object] | None = None,
        set_default_query: Mapping[str, object] | None = None,
        _extra_kwargs: Mapping[str, Any] = {},
    ) -> Self:
        """
        Create a new client instance re-using the same options given to the current client with optional overriding.
        """
        if default_headers is not None and set_default_headers is not None:
            raise ValueError("The `default_headers` and `set_default_headers` arguments are mutually exclusive")

        if default_query is not None and set_default_query is not None:
            raise ValueError("The `default_query` and `set_default_query` arguments are mutually exclusive")

        headers = self._custom_headers
        if default_headers is not None:
            headers = {**headers, **default_headers}
        elif set_default_headers is not None:
            headers = set_default_headers

        params = self._custom_query
        if default_query is not None:
            params = {**params, **default_query}
        elif set_default_query is not None:
            params = set_default_query

        http_client = http_client or self._client
        return self.__class__(
            api_key=api_key or self.api_key,
            bearer_token=bearer_token or self.bearer_token,
            base_url=base_url or self.base_url,
            environment=environment or self._environment,
            timeout=self.timeout if isinstance(timeout, NotGiven) else timeout,
            http_client=http_client,
            max_retries=max_retries if is_given(max_retries) else self.max_retries,
            default_headers=headers,
            default_query=params,
            **_extra_kwargs,
        )

    # Alias for `copy` for nicer inline usage, e.g.
    # client.with_options(timeout=10).foo.create(...)
    with_options = copy

    @override
    def _make_status_error(
        self,
        err_msg: str,
        *,
        body: object,
        response: httpx.Response,
    ) -> APIStatusError:
        if response.status_code == 400:
            return _exceptions.BadRequestError(err_msg, response=response, body=body)

        if response.status_code == 401:
            return _exceptions.AuthenticationError(err_msg, response=response, body=body)

        if response.status_code == 403:
            return _exceptions.PermissionDeniedError(err_msg, response=response, body=body)

        if response.status_code == 404:
            return _exceptions.NotFoundError(err_msg, response=response, body=body)

        if response.status_code == 409:
            return _exceptions.ConflictError(err_msg, response=response, body=body)

        if response.status_code == 422:
            return _exceptions.UnprocessableEntityError(err_msg, response=response, body=body)

        if response.status_code == 429:
            return _exceptions.RateLimitError(err_msg, response=response, body=body)

        if response.status_code >= 500:
            return _exceptions.InternalServerError(err_msg, response=response, body=body)
        return APIStatusError(err_msg, response=response, body=body)


class TranscendWithRawResponse:
    def __init__(self, client: Transcend) -> None:
        self.llm = llm.LlmResourceWithRawResponse(client.llm)
        self.classify = classify.ClassifyResourceWithRawResponse(client.classify)
        self.public_keys = public_keys.PublicKeysResourceWithRawResponse(client.public_keys)
        self.datapoint = datapoint.DatapointResourceWithRawResponse(client.datapoint)
        self.datapoint_chunked = datapoint_chunked.DatapointChunkedResourceWithRawResponse(client.datapoint_chunked)
        self.data_silo = data_silo.DataSiloResourceWithRawResponse(client.data_silo)
        self.enrich_identifiers = enrich_identifiers.EnrichIdentifiersResourceWithRawResponse(client.enrich_identifiers)
        self.request_identifiers = request_identifiers.RequestIdentifiersResourceWithRawResponse(
            client.request_identifiers
        )
        self.data_subject_request = data_subject_request.DataSubjectRequestResourceWithRawResponse(
            client.data_subject_request
        )
        self.files = files.FilesResourceWithRawResponse(client.files)
        self.consent_preferences = consent_preferences.ConsentPreferencesResourceWithRawResponse(
            client.consent_preferences
        )
        self.preferences = preferences.PreferencesResourceWithRawResponse(client.preferences)
        self.sync = sync.SyncResourceWithRawResponse(client.sync)


class AsyncTranscendWithRawResponse:
    def __init__(self, client: AsyncTranscend) -> None:
        self.llm = llm.AsyncLlmResourceWithRawResponse(client.llm)
        self.classify = classify.AsyncClassifyResourceWithRawResponse(client.classify)
        self.public_keys = public_keys.AsyncPublicKeysResourceWithRawResponse(client.public_keys)
        self.datapoint = datapoint.AsyncDatapointResourceWithRawResponse(client.datapoint)
        self.datapoint_chunked = datapoint_chunked.AsyncDatapointChunkedResourceWithRawResponse(
            client.datapoint_chunked
        )
        self.data_silo = data_silo.AsyncDataSiloResourceWithRawResponse(client.data_silo)
        self.enrich_identifiers = enrich_identifiers.AsyncEnrichIdentifiersResourceWithRawResponse(
            client.enrich_identifiers
        )
        self.request_identifiers = request_identifiers.AsyncRequestIdentifiersResourceWithRawResponse(
            client.request_identifiers
        )
        self.data_subject_request = data_subject_request.AsyncDataSubjectRequestResourceWithRawResponse(
            client.data_subject_request
        )
        self.files = files.AsyncFilesResourceWithRawResponse(client.files)
        self.consent_preferences = consent_preferences.AsyncConsentPreferencesResourceWithRawResponse(
            client.consent_preferences
        )
        self.preferences = preferences.AsyncPreferencesResourceWithRawResponse(client.preferences)
        self.sync = sync.AsyncSyncResourceWithRawResponse(client.sync)


class TranscendWithStreamedResponse:
    def __init__(self, client: Transcend) -> None:
        self.llm = llm.LlmResourceWithStreamingResponse(client.llm)
        self.classify = classify.ClassifyResourceWithStreamingResponse(client.classify)
        self.public_keys = public_keys.PublicKeysResourceWithStreamingResponse(client.public_keys)
        self.datapoint = datapoint.DatapointResourceWithStreamingResponse(client.datapoint)
        self.datapoint_chunked = datapoint_chunked.DatapointChunkedResourceWithStreamingResponse(
            client.datapoint_chunked
        )
        self.data_silo = data_silo.DataSiloResourceWithStreamingResponse(client.data_silo)
        self.enrich_identifiers = enrich_identifiers.EnrichIdentifiersResourceWithStreamingResponse(
            client.enrich_identifiers
        )
        self.request_identifiers = request_identifiers.RequestIdentifiersResourceWithStreamingResponse(
            client.request_identifiers
        )
        self.data_subject_request = data_subject_request.DataSubjectRequestResourceWithStreamingResponse(
            client.data_subject_request
        )
        self.files = files.FilesResourceWithStreamingResponse(client.files)
        self.consent_preferences = consent_preferences.ConsentPreferencesResourceWithStreamingResponse(
            client.consent_preferences
        )
        self.preferences = preferences.PreferencesResourceWithStreamingResponse(client.preferences)
        self.sync = sync.SyncResourceWithStreamingResponse(client.sync)


class AsyncTranscendWithStreamedResponse:
    def __init__(self, client: AsyncTranscend) -> None:
        self.llm = llm.AsyncLlmResourceWithStreamingResponse(client.llm)
        self.classify = classify.AsyncClassifyResourceWithStreamingResponse(client.classify)
        self.public_keys = public_keys.AsyncPublicKeysResourceWithStreamingResponse(client.public_keys)
        self.datapoint = datapoint.AsyncDatapointResourceWithStreamingResponse(client.datapoint)
        self.datapoint_chunked = datapoint_chunked.AsyncDatapointChunkedResourceWithStreamingResponse(
            client.datapoint_chunked
        )
        self.data_silo = data_silo.AsyncDataSiloResourceWithStreamingResponse(client.data_silo)
        self.enrich_identifiers = enrich_identifiers.AsyncEnrichIdentifiersResourceWithStreamingResponse(
            client.enrich_identifiers
        )
        self.request_identifiers = request_identifiers.AsyncRequestIdentifiersResourceWithStreamingResponse(
            client.request_identifiers
        )
        self.data_subject_request = data_subject_request.AsyncDataSubjectRequestResourceWithStreamingResponse(
            client.data_subject_request
        )
        self.files = files.AsyncFilesResourceWithStreamingResponse(client.files)
        self.consent_preferences = consent_preferences.AsyncConsentPreferencesResourceWithStreamingResponse(
            client.consent_preferences
        )
        self.preferences = preferences.AsyncPreferencesResourceWithStreamingResponse(client.preferences)
        self.sync = sync.AsyncSyncResourceWithStreamingResponse(client.sync)


Client = Transcend

AsyncClient = AsyncTranscend
