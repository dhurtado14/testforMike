# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["SyncSetConsentPreferencesParams", "Consent"]


class SyncSetConsentPreferencesParams(TypedDict, total=False):
    token: Required[str]
    """A JWT including an encrypted identifier"""

    consent: Required[Consent]

    partition: Required[str]
    """The consent partition or bundle ID.

    You can find the partition value under Consent Management > Developer Settings.
    If this value is not set, please use your bundle ID.
    """


class Consent(TypedDict, total=False):
    confirmed: Required[bool]
    """
    Was tracking consent confirmed by the user? If this is false, the consent was
    resolved from defaults & is not yet confirmed
    """

    purposes: Required[object]
    """Consent purposes to update"""

    timestamp: Required[str]
    """Timestamp of when consent was collected"""

    prompted: bool
    """
    Whether or not the UI has been shown to the end-user (undefined in older
    versions of airgap.js)
    """

    updated: bool
    """
    Has the consent been updated (including no-change confirmation) since default
    resolution
    """
