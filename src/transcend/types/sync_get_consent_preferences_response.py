# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from .._models import BaseModel

__all__ = ["SyncGetConsentPreferencesResponse"]


class SyncGetConsentPreferencesResponse(BaseModel):
    confirmed: bool
    """
    Was tracking consent confirmed by the user? If this is false, the consent was
    resolved from defaults & is not yet confirmed
    """

    purposes: object
    """Consent purposes to update"""

    timestamp: str
    """Timestamp of when consent was collected"""

    prompted: Optional[bool] = None
    """
    Whether or not the UI has been shown to the end-user (undefined in older
    versions of airgap.js)
    """

    tcf: Optional[str] = None
    """IAB Transparency & Consent Framework (TCF) 2.0 consent metadata"""

    updated: Optional[bool] = None
    """
    Has the consent been updated (including no-change confirmation) since default
    resolution
    """

    usp: Optional[str] = None
    """US Privacy (USP) String"""
