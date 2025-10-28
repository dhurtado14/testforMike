# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["ConsentPreferenceDeprecatedCreateResponse", "Node", "LastKey"]


class Node(BaseModel):
    decryption_status: Literal["DECRYPTED", "ERROR"] = FieldInfo(alias="decryptionStatus")
    """The decryption status of the userId field."""

    partition: str
    """The database partition (by default, the ID of your Airgap bundle.

    You can find this value under Consent Management > Developer Settings)
    """

    purposes: object
    """
    Object with keys representing that tracking purposes (Consent Management) and
    values that represent whether the user has opted in or out of it.
    """

    timestamp: datetime
    """Timestamp of when the preference was originally set by the user."""

    updated_at: datetime = FieldInfo(alias="updatedAt")
    """Timestamp of when the record was last updated in the Preference Store."""

    user_id: str = FieldInfo(alias="userId")
    """The identifier associated with this user when their preference was set."""

    airgap_version: Optional[str] = FieldInfo(alias="airgapVersion", default=None)
    """
    If this preference was set by the Transcend Consent Manager, Airgap, this is the
    Airgap.js version that set this preference.
    """

    gpp: Optional[str] = None
    """IAB GPP String, encoding both USP and USNAT"""

    tcf: Optional[str] = None
    """IAB TCF String"""

    usp: Optional[str] = None
    """US Privacy (USP) String"""


class LastKey(BaseModel):
    decryption_status: Literal["DECRYPTED", "ERROR"] = FieldInfo(alias="decryptionStatus")
    """The decryption status of the userId field in the last key.

    Can be one of: `DECRYPTED`, `ERROR`
    """

    partition: str
    """The ID of the partition in the Preference Store."""

    user_id: str = FieldInfo(alias="userId")
    """
    A concatenated string of (1) the identifier associated with this user when their
    preference was set, and (2) the partition key of the database.
    """

    timestamp: Optional[datetime] = None
    """Timestamp of when the preference was set.

    The last key should either contain a timestamp or updatedAt, but not both.
    """

    updated_at: Optional[datetime] = FieldInfo(alias="updatedAt", default=None)
    """Timestamp of when the record was last updated in the Preference Store.

    The last key should either contain a timestamp or updatedAt, but not both.
    """


class ConsentPreferenceDeprecatedCreateResponse(BaseModel):
    nodes: List[Node]

    last_key: Optional[LastKey] = FieldInfo(alias="lastKey", default=None)
    """Key for cursor pagination.

    To fetch the next page, set the startAt property to equal this lastKey.
    """
