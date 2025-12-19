# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union, Iterable
from datetime import datetime
from typing_extensions import Required, Annotated, TypeAlias, TypedDict

from .._utils import PropertyInfo

__all__ = [
    "PreferenceQueryParams",
    "Filter",
    "FilterIdentifiers",
    "FilterIdentifiersIdentifier",
    "FilterUnionMember1",
    "FilterSystem",
    "FilterSystemSystem",
]


class PreferenceQueryParams(TypedDict, total=False):
    filter: Filter
    """The filter to apply to the query."""

    limit: float
    """Max number of users to return."""

    x_sombra_authorization: Annotated[str, PropertyInfo(alias="x-sombra-authorization")]


class FilterIdentifiersIdentifier(TypedDict, total=False):
    value: Required[str]
    """The unique identifier value used to look up the preference record"""

    name: str
    """The identifier name. Defaults to email when not provided."""


class FilterIdentifiers(TypedDict, total=False):
    """Filter by user identifiers"""

    identifiers: Iterable[FilterIdentifiersIdentifier]
    """The list of identifiers, each corresponding to a unique user.

    Cannot be used in combination with timestampBefore and timestampAfter filters.
    """


class FilterUnionMember1(TypedDict, total=False):
    """Filter by when the preference was last updated"""

    timestamp_after: Annotated[Union[str, datetime], PropertyInfo(alias="timestampAfter", format="iso8601")]
    """Filter for preferences updated after a given timestamp."""

    timestamp_before: Annotated[Union[str, datetime], PropertyInfo(alias="timestampBefore", format="iso8601")]
    """Filter for preferences updated before a given timestamp."""


class FilterSystemSystem(TypedDict, total=False):
    """System metadata on the database record."""

    updated_after: Annotated[Union[str, datetime], PropertyInfo(alias="updatedAfter", format="iso8601")]
    """Filter for records updated after a given timestamp.

    This is when the database record was updated, and NOT when the preference was
    last updated.
    """

    updated_before: Annotated[Union[str, datetime], PropertyInfo(alias="updatedBefore", format="iso8601")]
    """Filter for records updated before a given timestamp.

    This is when the database record was updated, and NOT when the preference was
    last updated.
    """


class FilterSystem(TypedDict, total=False):
    """Filter by system metadata"""

    system: FilterSystemSystem
    """System metadata on the database record."""


Filter: TypeAlias = Union[FilterIdentifiers, FilterUnionMember1, FilterSystem]
