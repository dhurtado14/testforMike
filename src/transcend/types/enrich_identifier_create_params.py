# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Iterable
from typing_extensions import Literal, Required, Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["EnrichIdentifierCreateParams", "EnrichedIdentifier"]


class EnrichIdentifierCreateParams(TypedDict, total=False):
    x_transcend_nonce: Required[Annotated[str, PropertyInfo(alias="x-transcend-nonce")]]

    enriched_identifiers: Annotated[Dict[str, Iterable[EnrichedIdentifier]], PropertyInfo(alias="enrichedIdentifiers")]
    """An object where the keys are the identifier names (i.e.

    email, phone, idfa, ...), and the values are a list of enriched identifiers.
    """

    status: Literal["CANCELED", "ON_HOLD"]

    template_id: Annotated[str, PropertyInfo(alias="templateId")]
    """
    When status is set to ON_HOLD or CANCELED, you may include the ID of a custom
    email template to send to the data subject.
    """

    template_title: Annotated[str, PropertyInfo(alias="templateTitle")]
    """
    When status is set to ON_HOLD or CANCELED, you may include the title of a custom
    email template to send to the data subject.
    """

    x_sombra_authorization: Annotated[str, PropertyInfo(alias="x-sombra-authorization")]


class EnrichedIdentifier(TypedDict, total=False):
    value: Required[str]
    """The identifier value (e.g. "ben@example.com", or "+18005551234", ...)"""
