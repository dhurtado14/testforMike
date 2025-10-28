# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["DataSubjectRequestCreateResponse", "Request"]


class Request(BaseModel):
    id: str

    core_identifier: str = FieldInfo(alias="coreIdentifier")

    is_silent: bool = FieldInfo(alias="isSilent")

    is_test: bool = FieldInfo(alias="isTest")

    link: str

    reply_to_email_addresses: List[str] = FieldInfo(alias="replyToEmailAddresses")
    """
    The set of email addresses that should be included on CC for any outbound emails
    send to the data subject during the course of the request.
    """

    status: Literal[
        "REQUEST_MADE",
        "FAILED_VERIFICATION",
        "ENRICHING",
        "ON_HOLD",
        "WAITING",
        "COMPILING",
        "APPROVING",
        "DELAYED",
        "COMPLETED",
        "DOWNLOADABLE",
        "VIEW_CATEGORIES",
        "CANCELED",
        "SECONDARY",
        "SECONDARY_COMPLETED",
        "SECONDARY_APPROVING",
        "REVOKED",
    ]

    subject_type: str = FieldInfo(alias="subjectType")

    type: Literal[
        "ACCESS",
        "ERASURE",
        "RECTIFICATION",
        "RESTRICTION",
        "BUSINESS_PURPOSE",
        "PLACE_ON_LEGAL_HOLD",
        "REMOVE_FROM_LEGAL_HOLD",
        "AUTOMATED_DECISION_MAKING_OPT_OUT",
        "USE_OF_SENSITIVE_INFORMATION_OPT_OUT",
        "CONTACT_OPT_OUT",
        "SALE_OPT_OUT",
        "TRACKING_OPT_OUT",
        "CUSTOM_OPT_OUT",
        "AUTOMATED_DECISION_MAKING_OPT_IN",
        "USE_OF_SENSITIVE_INFORMATION_OPT_IN",
        "SALE_OPT_IN",
        "TRACKING_OPT_IN",
        "CONTACT_OPT_IN",
        "CUSTOM_OPT_IN",
    ]

    email: Optional[str] = None


class DataSubjectRequestCreateResponse(BaseModel):
    request: Request
