# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = [
    "PreferenceUpsertResponse",
    "Node",
    "NodeIdentifier",
    "NodeConsentManagement",
    "NodeMetadata",
    "NodePurpose",
    "NodePurposePreference",
    "NodePurposePreferenceChoice",
    "NodeSystem",
]


class NodeIdentifier(BaseModel):
    name: str
    """The identifier name"""

    value: str
    """The identifier value"""


class NodeConsentManagement(BaseModel):
    airgap_version: Optional[str] = FieldInfo(alias="airgapVersion", default=None)
    """
    If this preference was ever set by the Transcend Consent Manager, Airgap, this
    is the Airgap.js version that set this preference.
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


class NodePurposePreferenceChoice(BaseModel):
    boolean_value: Optional[bool] = FieldInfo(alias="booleanValue", default=None)
    """The boolean value of the preference"""

    select_value: Optional[str] = FieldInfo(alias="selectValue", default=None)
    """The select value of the preference"""

    select_values: Optional[List[str]] = FieldInfo(alias="selectValues", default=None)
    """The select values (multi-select) of the preference"""


class NodePurposePreference(BaseModel):
    choice: NodePurposePreferenceChoice
    """The choice made by the user for this preference topic"""

    topic: str
    """The slug (a unique identifier) of the preference topic"""


class NodePurpose(BaseModel):
    enabled: bool
    """If the purpose is enabled"""

    purpose: str
    """The slug (a unique identifer) of the purpose"""

    preferences: Optional[List[NodePurposePreference]] = None
    """The list of any preferences associated with this purpose"""


class NodeSystem(BaseModel):
    decryption_status: Optional[Literal["DECRYPTED", "ERROR"]] = FieldInfo(alias="decryptionStatus", default=None)
    """The decryption status of the identifiers field."""

    updated_at: Optional[datetime] = FieldInfo(alias="updatedAt", default=None)
    """Timestamp of when the record was last updated in the Preference Store."""


class Node(BaseModel):
    identifiers: List[NodeIdentifier]

    partition: str
    """The database partition (by default, the ID of your Airgap bundle.

    You can find this value under Consent Management > Developer Settings)
    """

    timestamp: datetime
    """Timestamp of when the preference was set."""

    consent_management: Optional[NodeConsentManagement] = FieldInfo(alias="consentManagement", default=None)
    """Consent management metadata on the preference record."""

    metadata: Optional[List[NodeMetadata]] = None
    """The metadata associated with the user's preference record"""

    metadata_timestamp: Optional[datetime] = FieldInfo(alias="metadataTimestamp", default=None)
    """Timestamp of when the metadata was last updated"""

    purposes: Optional[List[NodePurpose]] = None
    """
    A list of all tracking (Consent Management), communication, marketing and custom
    purposes that the user has opted into or out of, along with any other
    preferences associated with each purpose.
    """

    system: Optional[NodeSystem] = None
    """System specific metadata"""


class PreferenceUpsertResponse(BaseModel):
    nodes: Optional[List[Node]] = None
    """User's preference records"""

    success: Optional[bool] = None
    """Whether the preferences were updated successfully"""
