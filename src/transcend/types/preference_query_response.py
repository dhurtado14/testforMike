# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = [
    "PreferenceQueryResponse",
    "Node",
    "NodeIdentifier",
    "NodePurpose",
    "NodePurposePreference",
    "NodePurposePreferenceChoice",
    "NodeConsentManagement",
    "NodeMetadata",
    "NodeSystem",
]


class NodeIdentifier(BaseModel):
    name: str
    """The identifier name"""

    value: str
    """The identifier value"""


class NodePurposePreferenceChoice(BaseModel):
    boolean_value: Optional[bool] = FieldInfo(alias="booleanValue", default=None)
    """The boolean value of the preference"""

    select_value: Optional[str] = FieldInfo(alias="selectValue", default=None)
    """The single select value of the preference"""

    select_values: Optional[List[str]] = FieldInfo(alias="selectValues", default=None)
    """The select values (multi-select) of the preference"""


class NodePurposePreference(BaseModel):
    choice: NodePurposePreferenceChoice
    """The choice made by the user for this preference topic"""

    topic: str
    """The slug (a unique identifier) of the preference topic"""


class NodePurpose(BaseModel):
    enabled: bool
    """If the purpose was enabled by the user"""

    purpose: str
    """The slug (a unique identifer) of the purpose"""

    preferences: Optional[List[NodePurposePreference]] = None
    """The list of any preferences associated with this purpose"""


class NodeConsentManagement(BaseModel):
    airgap_version: Optional[str] = FieldInfo(alias="airgapVersion", default=None)
    """
    If this preference was set by the Transcend Consent Manager, Airgap, this is the
    Airgap.js version that set this preference.
    """

    gpp: Optional[str] = None
    """
    For consent management purposes, the IAB GPP String, encoding both USP and USNAT
    """

    tcf: Optional[str] = None
    """For consent management purposes, the IAB TCF String"""

    usp: Optional[str] = None
    """For consent management purposes, the IAB US Privacy (USP) string"""


class NodeMetadata(BaseModel):
    key: Optional[str] = None
    """The metadata key"""

    value: Optional[str] = None
    """The metadata value"""


class NodeSystem(BaseModel):
    decryption_status: Literal["DECRYPTED", "ERROR"] = FieldInfo(alias="decryptionStatus")
    """The decryption status of the identifiers field."""

    updated_at: datetime = FieldInfo(alias="updatedAt")
    """Timestamp of when the record was last updated in the Preference Store."""


class Node(BaseModel):
    identifiers: List[NodeIdentifier]

    partition: str
    """The database partition (by default, the ID of your Airgap bundle.

    You can find this value under Consent Management > Developer Settings)
    """

    purposes: List[NodePurpose]
    """
    A list of all tracking (Consent Management), communication, marketing and custom
    purposes that the user has opted into or out of, along with any other
    preferences associated with each purpose.
    """

    timestamp: datetime
    """Timestamp of when the preference was originally set by the user."""

    consent_management: Optional[NodeConsentManagement] = FieldInfo(alias="consentManagement", default=None)
    """Consent management metadata on the preference record."""

    metadata: Optional[List[NodeMetadata]] = None
    """The metadata associated with the preference record."""

    metadata_timestamp: Optional[datetime] = FieldInfo(alias="metadataTimestamp", default=None)
    """Timestamp of when the metadata was last updated"""

    system: Optional[NodeSystem] = None
    """System metadata on the database record."""


class PreferenceQueryResponse(BaseModel):
    nodes: List[Node]
    """List of all user preference records that match the query filters."""

    cursor: Optional[str] = None
    """The cursor for the next page.

    This is an opaque value that our servers use to track the next page of results.
    """
