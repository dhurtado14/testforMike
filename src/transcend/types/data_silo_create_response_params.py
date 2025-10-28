# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable
from typing_extensions import Literal, Required, Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["DataSiloCreateResponseParams", "Profile"]


class DataSiloCreateResponseParams(TypedDict, total=False):
    x_transcend_nonce: Required[Annotated[str, PropertyInfo(alias="x-transcend-nonce")]]

    profiles: Iterable[Profile]
    """An array of profiles found.

    Typically this of length 1, but if your system finds multiple profiles (or
    accounts) for this user, you can upload multiple profiles with this array. Or
    zero!
    """

    profile_status: Annotated[
        Literal["RESOLVED", "SKIPPED", "SKIPPED_DUE_TO_EXCEPTION", "WAITING"], PropertyInfo(alias="profileStatus")
    ]
    """
    Override the profile datapoints that have profileData set to be in a specific
    state. Any unreported datapoints will be updated according to the `status` field
    instead of this field.
    """

    status: Literal["READY", "RESOLVED", "SKIPPED", "SKIPPED_DUE_TO_EXCEPTION", "ACTION_REQUIRED", "WAITING"]
    """Override the integration to be in a specific state.

    Any unreported datapoints will be marked as "no data" when status is "READY",
    "RESOLVED", or "ACTION_REQUIRED". Any unreported datapoints will be marked as
    "skipped" when status is "SKIPPED" or "SKIPPED_DUE_TO_EXCEPTION". When status is
    "WAITING", unreported datapoints will not have their statuses changed. Typically
    this isn't needed, since the integration automatically becomes "ready" once all
    datapoints have been reported.
    """

    x_sombra_authorization: Annotated[str, PropertyInfo(alias="x-sombra-authorization")]


class Profile(TypedDict, total=False):
    profile_data: Annotated[object, PropertyInfo(alias="profileData")]
    """Arbitrary JSON data.

    Each key should match the datapoint name which you can define on the
    integration. This field can be left empty when status is passed, but must be
    provided otherwise.
    """

    profile_id: Annotated[str, PropertyInfo(alias="profileId")]
    """
    [DEPRECATED] A unique name for this profile (or account), such as a username or
    user ID. When passing a list of length 1, you should not set this value if you
    are using multi tenant Sombra or have a Sombra version at or above 7.199.0. For
    recent versions of Sombra, the profile identifier is pulled from the nonce.
    """
