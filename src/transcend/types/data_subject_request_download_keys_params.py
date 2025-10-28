# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["DataSubjectRequestDownloadKeysParams"]


class DataSubjectRequestDownloadKeysParams(TypedDict, total=False):
    limit: float
    """The maximum number of file keys to return on this page."""

    offset: float
    """The pagination offset."""

    x_sombra_authorization: Annotated[str, PropertyInfo(alias="x-sombra-authorization")]
