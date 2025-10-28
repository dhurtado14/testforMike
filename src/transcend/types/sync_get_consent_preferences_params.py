# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["SyncGetConsentPreferencesParams"]


class SyncGetConsentPreferencesParams(TypedDict, total=False):
    partition: Required[str]
    """The consent partition or bundle ID.

    You can find the partition value under Consent Management > Developer Settings.
    If this value is not set, please use your bundle ID.
    """
