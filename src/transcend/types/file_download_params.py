# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["FileDownloadParams"]


class FileDownloadParams(TypedDict, total=False):
    download_key: Required[Annotated[str, PropertyInfo(alias="downloadKey")]]
    """A download key retrieved from /v1/data-subject-request/{id}/download-keys"""

    x_sombra_authorization: Annotated[str, PropertyInfo(alias="x-sombra-authorization")]
