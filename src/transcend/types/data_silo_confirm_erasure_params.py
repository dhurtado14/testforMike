# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union, Iterable
from datetime import datetime
from typing_extensions import Literal, Required, Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["DataSiloConfirmErasureParams", "Profile"]


class DataSiloConfirmErasureParams(TypedDict, total=False):
    x_transcend_nonce: Required[Annotated[str, PropertyInfo(alias="x-transcend-nonce")]]

    message: str
    """A message to include in the response to provide an update about the response.

    This is displayed in the Transcend dashboard. This can be an error message or a
    description about the current state of the request job.
    """

    poll_id: Annotated[str, PropertyInfo(alias="pollId")]
    """
    If this DSR is in a polling state, this field will contain the ID of the async
    job that is polling for the DSR. You can use this ID to check the status of the
    DSR in your system.
    """

    profiles: Iterable[Profile]
    """[DEPRECATED] An array of each of the profiles that were erased.

    You should not set this value if you are using multi tenant Sombra or have a
    Sombra version at or above 7.199.0. For recent versions of Sombra, the profile
    identifier is pulled from the nonce, which means you can pass an empty body.
    """

    profile_status: Annotated[
        Literal["RESOLVED", "SKIPPED", "SKIPPED_DUE_TO_EXCEPTION", "WAITING", "ERROR"],
        PropertyInfo(alias="profileStatus"),
    ]
    """Override the specified profiles to be in a specific state."""

    retry_after_date: Annotated[Union[str, datetime], PropertyInfo(alias="retryAfterDate", format="iso8601")]
    """A date in the future that indicates when the user can retry the request.

    This is used for workflows that are asynchronous or to indicate when an error
    should be retried.
    """

    status: Literal["READY", "RESOLVED", "SKIPPED", "SKIPPED_DUE_TO_EXCEPTION", "ACTION_REQUIRED", "WAITING"]
    """Override the integration to be in a specific state.

    If `status` is set to "READY" or "RESOLVED", this will also mark all specified
    profiles as resolved.
    """

    x_sombra_authorization: Annotated[str, PropertyInfo(alias="x-sombra-authorization")]


class Profile(TypedDict, total=False):
    profile_id: Annotated[str, PropertyInfo(alias="profileId")]
    """
    [DEPRECATED] A unique name for this profile (or account), such as a username or
    user ID. You should not set this value if you are using multi tenant Sombra or
    have a Sombra version at or above 7.199.0. For recent versions of Sombra, the
    profile identifier is pulled from the nonce. You should pass an empty body.
    """
