# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import TYPE_CHECKING, Any, Dict, Mapping, cast
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
from ._compat import cached_property
from ._version import __version__
from ._streaming import Stream as Stream, AsyncStream as AsyncStream
from ._exceptions import APIStatusError, TranscendError
from ._base_client import (
    DEFAULT_MAX_RETRIES,
    SyncAPIClient,
    AsyncAPIClient,
)

if TYPE_CHECKING:
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
    from .resources.llm import LlmResource, AsyncLlmResource
    from .resources.sync import SyncResource, AsyncSyncResource
    from .resources.files import FilesResource, AsyncFilesResource
    from .resources.classify import ClassifyResource, AsyncClassifyResource
    from .resources.data_silo import DataSiloResource, AsyncDataSiloResource
    from .resources.datapoint import DatapointResource, AsyncDatapointResource
    from .resources.preferences import PreferencesResource, AsyncPreferencesResource
    from .resources.public_keys import PublicKeysResource, AsyncPublicKeysResource
    from .resources.datapoint_chunked import DatapointChunkedResource, AsyncDatapointChunkedResource
    from .resources.enrich_identifiers import EnrichIdentifiersResource, AsyncEnrichIdentifiersResource
    from .resources.consent_preferences import ConsentPreferencesResource, AsyncConsentPreferencesResource
    from .resources.request_identifiers import RequestIdentifiersResource, AsyncRequestIdentifiersResource
    from .resources.data_subject_request import DataSubjectRequestResource, AsyncDataSubjectRequestResource

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

    @cached_property
    def llm(self) -> LlmResource:
        from .resources.llm import LlmResource

        return LlmResource(self)

    @cached_property
    def classify(self) -> ClassifyResource:
        from .resources.classify import ClassifyResource

        return ClassifyResource(self)

    @cached_property
    def public_keys(self) -> PublicKeysResource:
        from .resources.public_keys import PublicKeysResource

        return PublicKeysResource(self)

    @cached_property
    def datapoint(self) -> DatapointResource:
        from .resources.datapoint import DatapointResource

        return DatapointResource(self)

    @cached_property
    def datapoint_chunked(self) -> DatapointChunkedResource:
        from .resources.datapoint_chunked import DatapointChunkedResource

        return DatapointChunkedResource(self)

    @cached_property
    def data_silo(self) -> DataSiloResource:
        from .resources.data_silo import DataSiloResource

        return DataSiloResource(self)

    @cached_property
    def enrich_identifiers(self) -> EnrichIdentifiersResource:
        from .resources.enrich_identifiers import EnrichIdentifiersResource

        return EnrichIdentifiersResource(self)

    @cached_property
    def request_identifiers(self) -> RequestIdentifiersResource:
        from .resources.request_identifiers import RequestIdentifiersResource

        return RequestIdentifiersResource(self)

    @cached_property
    def data_subject_request(self) -> DataSubjectRequestResource:
        from .resources.data_subject_request import DataSubjectRequestResource

        return DataSubjectRequestResource(self)

    @cached_property
    def files(self) -> FilesResource:
        from .resources.files import FilesResource

        return FilesResource(self)

    @cached_property
    def consent_preferences(self) -> ConsentPreferencesResource:
        from .resources.consent_preferences import ConsentPreferencesResource

        return ConsentPreferencesResource(self)

    @cached_property
    def preferences(self) -> PreferencesResource:
        from .resources.preferences import PreferencesResource

        return PreferencesResource(self)

    @cached_property
    def sync(self) -> SyncResource:
        from .resources.sync import SyncResource

        return SyncResource(self)

    @cached_property
    def with_raw_response(self) -> TranscendWithRawResponse:
        return TranscendWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> TranscendWithStreamedResponse:
        return TranscendWithStreamedResponse(self)

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

    @cached_property
    def llm(self) -> AsyncLlmResource:
        from .resources.llm import AsyncLlmResource

        return AsyncLlmResource(self)

    @cached_property
    def classify(self) -> AsyncClassifyResource:
        from .resources.classify import AsyncClassifyResource

        return AsyncClassifyResource(self)

    @cached_property
    def public_keys(self) -> AsyncPublicKeysResource:
        from .resources.public_keys import AsyncPublicKeysResource

        return AsyncPublicKeysResource(self)

    @cached_property
    def datapoint(self) -> AsyncDatapointResource:
        from .resources.datapoint import AsyncDatapointResource

        return AsyncDatapointResource(self)

    @cached_property
    def datapoint_chunked(self) -> AsyncDatapointChunkedResource:
        from .resources.datapoint_chunked import AsyncDatapointChunkedResource

        return AsyncDatapointChunkedResource(self)

    @cached_property
    def data_silo(self) -> AsyncDataSiloResource:
        from .resources.data_silo import AsyncDataSiloResource

        return AsyncDataSiloResource(self)

    @cached_property
    def enrich_identifiers(self) -> AsyncEnrichIdentifiersResource:
        from .resources.enrich_identifiers import AsyncEnrichIdentifiersResource

        return AsyncEnrichIdentifiersResource(self)

    @cached_property
    def request_identifiers(self) -> AsyncRequestIdentifiersResource:
        from .resources.request_identifiers import AsyncRequestIdentifiersResource

        return AsyncRequestIdentifiersResource(self)

    @cached_property
    def data_subject_request(self) -> AsyncDataSubjectRequestResource:
        from .resources.data_subject_request import AsyncDataSubjectRequestResource

        return AsyncDataSubjectRequestResource(self)

    @cached_property
    def files(self) -> AsyncFilesResource:
        from .resources.files import AsyncFilesResource

        return AsyncFilesResource(self)

    @cached_property
    def consent_preferences(self) -> AsyncConsentPreferencesResource:
        from .resources.consent_preferences import AsyncConsentPreferencesResource

        return AsyncConsentPreferencesResource(self)

    @cached_property
    def preferences(self) -> AsyncPreferencesResource:
        from .resources.preferences import AsyncPreferencesResource

        return AsyncPreferencesResource(self)

    @cached_property
    def sync(self) -> AsyncSyncResource:
        from .resources.sync import AsyncSyncResource

        return AsyncSyncResource(self)

    @cached_property
    def with_raw_response(self) -> AsyncTranscendWithRawResponse:
        return AsyncTranscendWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncTranscendWithStreamedResponse:
        return AsyncTranscendWithStreamedResponse(self)

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
    _client: Transcend

    def __init__(self, client: Transcend) -> None:
        self._client = client

    @cached_property
    def llm(self) -> llm.LlmResourceWithRawResponse:
        from .resources.llm import LlmResourceWithRawResponse

        return LlmResourceWithRawResponse(self._client.llm)

    @cached_property
    def classify(self) -> classify.ClassifyResourceWithRawResponse:
        from .resources.classify import ClassifyResourceWithRawResponse

        return ClassifyResourceWithRawResponse(self._client.classify)

    @cached_property
    def public_keys(self) -> public_keys.PublicKeysResourceWithRawResponse:
        from .resources.public_keys import PublicKeysResourceWithRawResponse

        return PublicKeysResourceWithRawResponse(self._client.public_keys)

    @cached_property
    def datapoint(self) -> datapoint.DatapointResourceWithRawResponse:
        from .resources.datapoint import DatapointResourceWithRawResponse

        return DatapointResourceWithRawResponse(self._client.datapoint)

    @cached_property
    def datapoint_chunked(self) -> datapoint_chunked.DatapointChunkedResourceWithRawResponse:
        from .resources.datapoint_chunked import DatapointChunkedResourceWithRawResponse

        return DatapointChunkedResourceWithRawResponse(self._client.datapoint_chunked)

    @cached_property
    def data_silo(self) -> data_silo.DataSiloResourceWithRawResponse:
        from .resources.data_silo import DataSiloResourceWithRawResponse

        return DataSiloResourceWithRawResponse(self._client.data_silo)

    @cached_property
    def enrich_identifiers(self) -> enrich_identifiers.EnrichIdentifiersResourceWithRawResponse:
        from .resources.enrich_identifiers import EnrichIdentifiersResourceWithRawResponse

        return EnrichIdentifiersResourceWithRawResponse(self._client.enrich_identifiers)

    @cached_property
    def request_identifiers(self) -> request_identifiers.RequestIdentifiersResourceWithRawResponse:
        from .resources.request_identifiers import RequestIdentifiersResourceWithRawResponse

        return RequestIdentifiersResourceWithRawResponse(self._client.request_identifiers)

    @cached_property
    def data_subject_request(self) -> data_subject_request.DataSubjectRequestResourceWithRawResponse:
        from .resources.data_subject_request import DataSubjectRequestResourceWithRawResponse

        return DataSubjectRequestResourceWithRawResponse(self._client.data_subject_request)

    @cached_property
    def files(self) -> files.FilesResourceWithRawResponse:
        from .resources.files import FilesResourceWithRawResponse

        return FilesResourceWithRawResponse(self._client.files)

    @cached_property
    def consent_preferences(self) -> consent_preferences.ConsentPreferencesResourceWithRawResponse:
        from .resources.consent_preferences import ConsentPreferencesResourceWithRawResponse

        return ConsentPreferencesResourceWithRawResponse(self._client.consent_preferences)

    @cached_property
    def preferences(self) -> preferences.PreferencesResourceWithRawResponse:
        from .resources.preferences import PreferencesResourceWithRawResponse

        return PreferencesResourceWithRawResponse(self._client.preferences)

    @cached_property
    def sync(self) -> sync.SyncResourceWithRawResponse:
        from .resources.sync import SyncResourceWithRawResponse

        return SyncResourceWithRawResponse(self._client.sync)


class AsyncTranscendWithRawResponse:
    _client: AsyncTranscend

    def __init__(self, client: AsyncTranscend) -> None:
        self._client = client

    @cached_property
    def llm(self) -> llm.AsyncLlmResourceWithRawResponse:
        from .resources.llm import AsyncLlmResourceWithRawResponse

        return AsyncLlmResourceWithRawResponse(self._client.llm)

    @cached_property
    def classify(self) -> classify.AsyncClassifyResourceWithRawResponse:
        from .resources.classify import AsyncClassifyResourceWithRawResponse

        return AsyncClassifyResourceWithRawResponse(self._client.classify)

    @cached_property
    def public_keys(self) -> public_keys.AsyncPublicKeysResourceWithRawResponse:
        from .resources.public_keys import AsyncPublicKeysResourceWithRawResponse

        return AsyncPublicKeysResourceWithRawResponse(self._client.public_keys)

    @cached_property
    def datapoint(self) -> datapoint.AsyncDatapointResourceWithRawResponse:
        from .resources.datapoint import AsyncDatapointResourceWithRawResponse

        return AsyncDatapointResourceWithRawResponse(self._client.datapoint)

    @cached_property
    def datapoint_chunked(self) -> datapoint_chunked.AsyncDatapointChunkedResourceWithRawResponse:
        from .resources.datapoint_chunked import AsyncDatapointChunkedResourceWithRawResponse

        return AsyncDatapointChunkedResourceWithRawResponse(self._client.datapoint_chunked)

    @cached_property
    def data_silo(self) -> data_silo.AsyncDataSiloResourceWithRawResponse:
        from .resources.data_silo import AsyncDataSiloResourceWithRawResponse

        return AsyncDataSiloResourceWithRawResponse(self._client.data_silo)

    @cached_property
    def enrich_identifiers(self) -> enrich_identifiers.AsyncEnrichIdentifiersResourceWithRawResponse:
        from .resources.enrich_identifiers import AsyncEnrichIdentifiersResourceWithRawResponse

        return AsyncEnrichIdentifiersResourceWithRawResponse(self._client.enrich_identifiers)

    @cached_property
    def request_identifiers(self) -> request_identifiers.AsyncRequestIdentifiersResourceWithRawResponse:
        from .resources.request_identifiers import AsyncRequestIdentifiersResourceWithRawResponse

        return AsyncRequestIdentifiersResourceWithRawResponse(self._client.request_identifiers)

    @cached_property
    def data_subject_request(self) -> data_subject_request.AsyncDataSubjectRequestResourceWithRawResponse:
        from .resources.data_subject_request import AsyncDataSubjectRequestResourceWithRawResponse

        return AsyncDataSubjectRequestResourceWithRawResponse(self._client.data_subject_request)

    @cached_property
    def files(self) -> files.AsyncFilesResourceWithRawResponse:
        from .resources.files import AsyncFilesResourceWithRawResponse

        return AsyncFilesResourceWithRawResponse(self._client.files)

    @cached_property
    def consent_preferences(self) -> consent_preferences.AsyncConsentPreferencesResourceWithRawResponse:
        from .resources.consent_preferences import AsyncConsentPreferencesResourceWithRawResponse

        return AsyncConsentPreferencesResourceWithRawResponse(self._client.consent_preferences)

    @cached_property
    def preferences(self) -> preferences.AsyncPreferencesResourceWithRawResponse:
        from .resources.preferences import AsyncPreferencesResourceWithRawResponse

        return AsyncPreferencesResourceWithRawResponse(self._client.preferences)

    @cached_property
    def sync(self) -> sync.AsyncSyncResourceWithRawResponse:
        from .resources.sync import AsyncSyncResourceWithRawResponse

        return AsyncSyncResourceWithRawResponse(self._client.sync)


class TranscendWithStreamedResponse:
    _client: Transcend

    def __init__(self, client: Transcend) -> None:
        self._client = client

    @cached_property
    def llm(self) -> llm.LlmResourceWithStreamingResponse:
        from .resources.llm import LlmResourceWithStreamingResponse

        return LlmResourceWithStreamingResponse(self._client.llm)

    @cached_property
    def classify(self) -> classify.ClassifyResourceWithStreamingResponse:
        from .resources.classify import ClassifyResourceWithStreamingResponse

        return ClassifyResourceWithStreamingResponse(self._client.classify)

    @cached_property
    def public_keys(self) -> public_keys.PublicKeysResourceWithStreamingResponse:
        from .resources.public_keys import PublicKeysResourceWithStreamingResponse

        return PublicKeysResourceWithStreamingResponse(self._client.public_keys)

    @cached_property
    def datapoint(self) -> datapoint.DatapointResourceWithStreamingResponse:
        from .resources.datapoint import DatapointResourceWithStreamingResponse

        return DatapointResourceWithStreamingResponse(self._client.datapoint)

    @cached_property
    def datapoint_chunked(self) -> datapoint_chunked.DatapointChunkedResourceWithStreamingResponse:
        from .resources.datapoint_chunked import DatapointChunkedResourceWithStreamingResponse

        return DatapointChunkedResourceWithStreamingResponse(self._client.datapoint_chunked)

    @cached_property
    def data_silo(self) -> data_silo.DataSiloResourceWithStreamingResponse:
        from .resources.data_silo import DataSiloResourceWithStreamingResponse

        return DataSiloResourceWithStreamingResponse(self._client.data_silo)

    @cached_property
    def enrich_identifiers(self) -> enrich_identifiers.EnrichIdentifiersResourceWithStreamingResponse:
        from .resources.enrich_identifiers import EnrichIdentifiersResourceWithStreamingResponse

        return EnrichIdentifiersResourceWithStreamingResponse(self._client.enrich_identifiers)

    @cached_property
    def request_identifiers(self) -> request_identifiers.RequestIdentifiersResourceWithStreamingResponse:
        from .resources.request_identifiers import RequestIdentifiersResourceWithStreamingResponse

        return RequestIdentifiersResourceWithStreamingResponse(self._client.request_identifiers)

    @cached_property
    def data_subject_request(self) -> data_subject_request.DataSubjectRequestResourceWithStreamingResponse:
        from .resources.data_subject_request import DataSubjectRequestResourceWithStreamingResponse

        return DataSubjectRequestResourceWithStreamingResponse(self._client.data_subject_request)

    @cached_property
    def files(self) -> files.FilesResourceWithStreamingResponse:
        from .resources.files import FilesResourceWithStreamingResponse

        return FilesResourceWithStreamingResponse(self._client.files)

    @cached_property
    def consent_preferences(self) -> consent_preferences.ConsentPreferencesResourceWithStreamingResponse:
        from .resources.consent_preferences import ConsentPreferencesResourceWithStreamingResponse

        return ConsentPreferencesResourceWithStreamingResponse(self._client.consent_preferences)

    @cached_property
    def preferences(self) -> preferences.PreferencesResourceWithStreamingResponse:
        from .resources.preferences import PreferencesResourceWithStreamingResponse

        return PreferencesResourceWithStreamingResponse(self._client.preferences)

    @cached_property
    def sync(self) -> sync.SyncResourceWithStreamingResponse:
        from .resources.sync import SyncResourceWithStreamingResponse

        return SyncResourceWithStreamingResponse(self._client.sync)


class AsyncTranscendWithStreamedResponse:
    _client: AsyncTranscend

    def __init__(self, client: AsyncTranscend) -> None:
        self._client = client

    @cached_property
    def llm(self) -> llm.AsyncLlmResourceWithStreamingResponse:
        from .resources.llm import AsyncLlmResourceWithStreamingResponse

        return AsyncLlmResourceWithStreamingResponse(self._client.llm)

    @cached_property
    def classify(self) -> classify.AsyncClassifyResourceWithStreamingResponse:
        from .resources.classify import AsyncClassifyResourceWithStreamingResponse

        return AsyncClassifyResourceWithStreamingResponse(self._client.classify)

    @cached_property
    def public_keys(self) -> public_keys.AsyncPublicKeysResourceWithStreamingResponse:
        from .resources.public_keys import AsyncPublicKeysResourceWithStreamingResponse

        return AsyncPublicKeysResourceWithStreamingResponse(self._client.public_keys)

    @cached_property
    def datapoint(self) -> datapoint.AsyncDatapointResourceWithStreamingResponse:
        from .resources.datapoint import AsyncDatapointResourceWithStreamingResponse

        return AsyncDatapointResourceWithStreamingResponse(self._client.datapoint)

    @cached_property
    def datapoint_chunked(self) -> datapoint_chunked.AsyncDatapointChunkedResourceWithStreamingResponse:
        from .resources.datapoint_chunked import AsyncDatapointChunkedResourceWithStreamingResponse

        return AsyncDatapointChunkedResourceWithStreamingResponse(self._client.datapoint_chunked)

    @cached_property
    def data_silo(self) -> data_silo.AsyncDataSiloResourceWithStreamingResponse:
        from .resources.data_silo import AsyncDataSiloResourceWithStreamingResponse

        return AsyncDataSiloResourceWithStreamingResponse(self._client.data_silo)

    @cached_property
    def enrich_identifiers(self) -> enrich_identifiers.AsyncEnrichIdentifiersResourceWithStreamingResponse:
        from .resources.enrich_identifiers import AsyncEnrichIdentifiersResourceWithStreamingResponse

        return AsyncEnrichIdentifiersResourceWithStreamingResponse(self._client.enrich_identifiers)

    @cached_property
    def request_identifiers(self) -> request_identifiers.AsyncRequestIdentifiersResourceWithStreamingResponse:
        from .resources.request_identifiers import AsyncRequestIdentifiersResourceWithStreamingResponse

        return AsyncRequestIdentifiersResourceWithStreamingResponse(self._client.request_identifiers)

    @cached_property
    def data_subject_request(self) -> data_subject_request.AsyncDataSubjectRequestResourceWithStreamingResponse:
        from .resources.data_subject_request import AsyncDataSubjectRequestResourceWithStreamingResponse

        return AsyncDataSubjectRequestResourceWithStreamingResponse(self._client.data_subject_request)

    @cached_property
    def files(self) -> files.AsyncFilesResourceWithStreamingResponse:
        from .resources.files import AsyncFilesResourceWithStreamingResponse

        return AsyncFilesResourceWithStreamingResponse(self._client.files)

    @cached_property
    def consent_preferences(self) -> consent_preferences.AsyncConsentPreferencesResourceWithStreamingResponse:
        from .resources.consent_preferences import AsyncConsentPreferencesResourceWithStreamingResponse

        return AsyncConsentPreferencesResourceWithStreamingResponse(self._client.consent_preferences)

    @cached_property
    def preferences(self) -> preferences.AsyncPreferencesResourceWithStreamingResponse:
        from .resources.preferences import AsyncPreferencesResourceWithStreamingResponse

        return AsyncPreferencesResourceWithStreamingResponse(self._client.preferences)

    @cached_property
    def sync(self) -> sync.AsyncSyncResourceWithStreamingResponse:
        from .resources.sync import AsyncSyncResourceWithStreamingResponse

        return AsyncSyncResourceWithStreamingResponse(self._client.sync)


Client = Transcend

AsyncClient = AsyncTranscend
