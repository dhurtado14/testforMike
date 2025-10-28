# Llm

Types:

```python
from transcend.types import LlmClassifyTextResponse
```

Methods:

- <code title="post /llm/classify-text">client.llm.<a href="./src/transcend/resources/llm.py">classify_text</a>(\*\*<a href="src/transcend/types/llm_classify_text_params.py">params</a>) -> <a href="./src/transcend/types/llm_classify_text_response.py">LlmClassifyTextResponse</a></code>

# Classify

Types:

```python
from transcend.types import ClassifyClassifyUnstructuredTextResponse
```

Methods:

- <code title="post /classify/unstructured-text">client.classify.<a href="./src/transcend/resources/classify.py">classify_unstructured_text</a>(\*\*<a href="src/transcend/types/classify_classify_unstructured_text_params.py">params</a>) -> <a href="./src/transcend/types/classify_classify_unstructured_text_response.py">ClassifyClassifyUnstructuredTextResponse</a></code>

# PublicKeys

Types:

```python
from transcend.types import PublicKeyRetrieveSigningKeyResponse
```

Methods:

- <code title="get /public-keys/sombra-general-signing-key">client.public_keys.<a href="./src/transcend/resources/public_keys.py">retrieve_signing_key</a>() -> str</code>

# Datapoint

Methods:

- <code title="post /v1/datapoint">client.datapoint.<a href="./src/transcend/resources/datapoint.py">upload</a>(body, \*\*<a href="src/transcend/types/datapoint_upload_params.py">params</a>) -> object</code>

# DatapointChunked

Methods:

- <code title="post /v1/datapoint-chunked">client.datapoint_chunked.<a href="./src/transcend/resources/datapoint_chunked.py">upload</a>(\*\*<a href="src/transcend/types/datapoint_chunked_upload_params.py">params</a>) -> object</code>

# DataSilo

Types:

```python
from transcend.types import DataSiloListPendingRequestsResponse
```

Methods:

- <code title="put /v1/data-silo">client.data_silo.<a href="./src/transcend/resources/data_silo.py">confirm_erasure</a>(\*\*<a href="src/transcend/types/data_silo_confirm_erasure_params.py">params</a>) -> object</code>
- <code title="post /v1/data-silo">client.data_silo.<a href="./src/transcend/resources/data_silo.py">create_response</a>(\*\*<a href="src/transcend/types/data_silo_create_response_params.py">params</a>) -> object</code>
- <code title="get /v1/data-silo/{id}/pending-requests/{type}">client.data_silo.<a href="./src/transcend/resources/data_silo.py">list_pending_requests</a>(type, \*, id, \*\*<a href="src/transcend/types/data_silo_list_pending_requests_params.py">params</a>) -> <a href="./src/transcend/types/data_silo_list_pending_requests_response.py">DataSiloListPendingRequestsResponse</a></code>

# EnrichIdentifiers

Methods:

- <code title="post /v1/enrich-identifiers">client.enrich_identifiers.<a href="./src/transcend/resources/enrich_identifiers.py">create</a>(\*\*<a href="src/transcend/types/enrich_identifier_create_params.py">params</a>) -> object</code>

# RequestIdentifiers

Types:

```python
from transcend.types import RequestIdentifierCreateResponse
```

Methods:

- <code title="post /v1/request-identifiers">client.request_identifiers.<a href="./src/transcend/resources/request_identifiers.py">create</a>(\*\*<a href="src/transcend/types/request_identifier_create_params.py">params</a>) -> <a href="./src/transcend/types/request_identifier_create_response.py">RequestIdentifierCreateResponse</a></code>

# DataSubjectRequest

Types:

```python
from transcend.types import (
    DataSubjectRequestCreateResponse,
    DataSubjectRequestRetrieveResponse,
    DataSubjectRequestDownloadKeysResponse,
)
```

Methods:

- <code title="post /v1/data-subject-request">client.data_subject_request.<a href="./src/transcend/resources/data_subject_request.py">create</a>(\*\*<a href="src/transcend/types/data_subject_request_create_params.py">params</a>) -> <a href="./src/transcend/types/data_subject_request_create_response.py">DataSubjectRequestCreateResponse</a></code>
- <code title="get /v1/data-subject-request/{id}">client.data_subject_request.<a href="./src/transcend/resources/data_subject_request.py">retrieve</a>(id) -> <a href="./src/transcend/types/data_subject_request_retrieve_response.py">DataSubjectRequestRetrieveResponse</a></code>
- <code title="get /v1/data-subject-request/{id}/download-keys">client.data_subject_request.<a href="./src/transcend/resources/data_subject_request.py">download_keys</a>(id, \*\*<a href="src/transcend/types/data_subject_request_download_keys_params.py">params</a>) -> <a href="./src/transcend/types/data_subject_request_download_keys_response.py">DataSubjectRequestDownloadKeysResponse</a></code>

# Files

Methods:

- <code title="get /v1/files">client.files.<a href="./src/transcend/resources/files.py">download</a>(\*\*<a href="src/transcend/types/file_download_params.py">params</a>) -> BinaryAPIResponse</code>

# ConsentPreferences

Types:

```python
from transcend.types import ConsentPreferenceDeprecatedCreateResponse
```

Methods:

- <code title="post /v1/consent-preferences">client.consent_preferences.<a href="./src/transcend/resources/consent_preferences.py">deprecated_create</a>(\*\*<a href="src/transcend/types/consent_preference_deprecated_create_params.py">params</a>) -> <a href="./src/transcend/types/consent_preference_deprecated_create_response.py">ConsentPreferenceDeprecatedCreateResponse</a></code>

# Preferences

Types:

```python
from transcend.types import PreferenceQueryResponse, PreferenceUpsertResponse
```

Methods:

- <code title="post /v1/preferences/{partition}/query">client.preferences.<a href="./src/transcend/resources/preferences.py">query</a>(partition, \*\*<a href="src/transcend/types/preference_query_params.py">params</a>) -> <a href="./src/transcend/types/preference_query_response.py">PreferenceQueryResponse</a></code>
- <code title="put /v1/preferences">client.preferences.<a href="./src/transcend/resources/preferences.py">upsert</a>(\*\*<a href="src/transcend/types/preference_upsert_params.py">params</a>) -> <a href="./src/transcend/types/preference_upsert_response.py">PreferenceUpsertResponse</a></code>

# Sync

Types:

```python
from transcend.types import SyncGetConsentPreferencesResponse, SyncSetConsentPreferencesResponse
```

Methods:

- <code title="get /sync">client.sync.<a href="./src/transcend/resources/sync.py">get_consent_preferences</a>(\*\*<a href="src/transcend/types/sync_get_consent_preferences_params.py">params</a>) -> <a href="./src/transcend/types/sync_get_consent_preferences_response.py">SyncGetConsentPreferencesResponse</a></code>
- <code title="post /sync">client.sync.<a href="./src/transcend/resources/sync.py">set_consent_preferences</a>(\*\*<a href="src/transcend/types/sync_set_consent_preferences_params.py">params</a>) -> <a href="./src/transcend/types/sync_set_consent_preferences_response.py">SyncSetConsentPreferencesResponse</a></code>
