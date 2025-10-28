# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["RequestIdentifierCreateResponse", "Identifier"]


class Identifier(BaseModel):
    id: str
    """The unique database UUID for this request identifier.

    This is unique per request, per identifier.
    """

    name: str
    """The name of the identifier, this uniquely defines the identifier type"""

    type: Literal[
        "email",
        "phone",
        "coreIdentifier",
        "custom",
        "gaid",
        "idfa",
        "idfv",
        "browserId",
        "microsoftAdvertisingId",
        "amazonFireAdvertisingId",
        "rida",
        "filestackHandle",
        "stripeId",
        "braintreeCustomerId",
        "chargebeeId",
        "thriveTrmContactId",
        "talkableUUID",
        "recurlyId",
        "customerIoId",
        "sprigVisitorId",
        "linkedInURL",
        "advertisingId",
        "personaReferenceId",
        "streamUserId",
        "plaidProcessorToken",
        "onfidoApplicantId",
        "veroUserId",
        "adobeAdvertisingCloudId",
        "adobeAudienceManagerId",
        "adobeExperienceCloudId",
        "adobeTargetId",
    ]
    """
    The static type representation of the identifier type in Transcend - indicating
    if this is a customer or out-of-the-box identifier
    """

    value: str
    """The value of the identifier"""


class RequestIdentifierCreateResponse(BaseModel):
    identifiers: List[Identifier]
