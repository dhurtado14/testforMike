# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing_extensions import Literal

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["DataSubjectRequestRetrieveResponse"]


class DataSubjectRequestRetrieveResponse(BaseModel):
    id: str

    core_identifier: str = FieldInfo(alias="coreIdentifier")

    email: str

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
