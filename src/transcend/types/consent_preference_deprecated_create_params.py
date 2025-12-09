# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union
from datetime import datetime
from typing_extensions import Literal, Required, Annotated, TypedDict

from .._types import SequenceNotStr
from .._utils import PropertyInfo

__all__ = ["ConsentPreferenceDeprecatedCreateParams", "StartKey"]


class ConsentPreferenceDeprecatedCreateParams(TypedDict, total=False):
    partition: Required[str]
    """The ID of the partition in the Preference Store."""

    identifiers: SequenceNotStr[str]
    """The list of identifiers, each corresponding to a unique user.

    Cannot be used in combination with timestampBefore and timestampAfter filters.
    """

    limit: float
    """Max number of users to return. Defaults to 50."""

    start_key: Annotated[StartKey, PropertyInfo(alias="startKey")]
    """The key after which to start looking for consent preferences.

    Used for cursor pagination.
    """

    timestamp_after: Annotated[Union[str, datetime], PropertyInfo(alias="timestampAfter", format="iso8601")]
    """Filter for consent preferences set after a given timestamp.

    Cannot be used in combination with identifiers or updated filters.
    """

    timestamp_before: Annotated[Union[str, datetime], PropertyInfo(alias="timestampBefore", format="iso8601")]
    """Filter for consent preferences set before a given timestamp.

    Defaults to now. Cannot be used in combination with identifiers or updated
    filters.
    """

    updated_after: Annotated[Union[str, datetime], PropertyInfo(alias="updatedAfter", format="iso8601")]
    """Filter for consent preferences updated after a given timestamp.

    Cannot be used in combination with identifiers or timestamp filter. If you are
    self-hosting Sombra, your Sombra version must be >=7.236.0 to query by
    updatedAfter.
    """

    updated_before: Annotated[Union[str, datetime], PropertyInfo(alias="updatedBefore", format="iso8601")]
    """Filter for consent preferences updated before a given timestamp.

    Defaults to now. Cannot be used in combination with identifiers or timestamp
    filter. If you are self-hosting Sombra, your Sombra version must be >=7.236.0 to
    query by updatedBefore.
    """

    x_sombra_authorization: Annotated[str, PropertyInfo(alias="x-sombra-authorization")]


class StartKey(TypedDict, total=False):
    """The key after which to start looking for consent preferences.

    Used for cursor pagination.
    """

    decryption_status: Required[Annotated[Literal["DECRYPTED", "ERROR"], PropertyInfo(alias="decryptionStatus")]]
    """The decryption status of the userId field in the start key.

    Can be one of: `DECRYPTED`, `ERROR`
    """

    partition: Required[str]
    """The ID of the partition in the Preference Store."""

    user_id: Required[Annotated[str, PropertyInfo(alias="userId")]]
    """
    A concatenated string of (1) the identifier associated with this user when their
    preference was set, and (2) the partition key of the database.
    """

    timestamp: Annotated[Union[str, datetime], PropertyInfo(format="iso8601")]
    """Timestamp of when the preference was set.

    The start key should either contain a timestamp or updatedAt, but not both.
    """

    updated_at: Annotated[Union[str, datetime], PropertyInfo(alias="updatedAt", format="iso8601")]
    """Timestamp of when the record was last updated in the Preference Store.

    The start key should either contain a timestamp or updatedAt, but not both.
    """
