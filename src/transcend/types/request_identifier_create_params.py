# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["RequestIdentifierCreateParams"]


class RequestIdentifierCreateParams(TypedDict, total=False):
    request_id: Required[Annotated[str, PropertyInfo(alias="requestId")]]
    """The UUID of the request to fetch request identifiers for"""

    first: float
    """The number of results to return on this page. Defaults to 10, maximum is 100."""

    offset: float
    """The offset to use while paginating."""

    x_sombra_authorization: Annotated[str, PropertyInfo(alias="x-sombra-authorization")]
