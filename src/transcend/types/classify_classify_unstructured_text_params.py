# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, Annotated, TypedDict

from .._types import SequenceNotStr
from .._utils import PropertyInfo

__all__ = ["ClassifyClassifyUnstructuredTextParams"]


class ClassifyClassifyUnstructuredTextParams(TypedDict, total=False):
    input_list: Required[Annotated[SequenceNotStr[str], PropertyInfo(alias="inputList")]]
    """List of inputs to classify"""

    labels: Required[SequenceNotStr[str]]
    """The list of labels to classify against"""

    x_sombra_authorization: Annotated[str, PropertyInfo(alias="x-sombra-authorization")]
