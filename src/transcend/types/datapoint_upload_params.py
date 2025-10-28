# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["DatapointUploadParams"]


class DatapointUploadParams(TypedDict, total=False):
    x_transcend_datapoint_name: Required[Annotated[str, PropertyInfo(alias="x-transcend-datapoint-name")]]

    x_transcend_nonce: Required[Annotated[str, PropertyInfo(alias="x-transcend-nonce")]]

    x_sombra_authorization: Annotated[str, PropertyInfo(alias="x-sombra-authorization")]

    x_transcend_profile_id: Annotated[str, PropertyInfo(alias="x-transcend-profile-id")]

    x_transcend_remote_id: Annotated[str, PropertyInfo(alias="x-transcend-remote-id")]

    x_transcend_skip_status_update: Annotated[bool, PropertyInfo(alias="x-transcend-skip-status-update")]
