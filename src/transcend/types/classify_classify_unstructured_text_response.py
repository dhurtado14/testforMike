# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from typing_extensions import TypeAlias

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["ClassifyClassifyUnstructuredTextResponse", "ClassifyClassifyUnstructuredTextResponseItem"]


class ClassifyClassifyUnstructuredTextResponseItem(BaseModel):
    classification_method: Optional[str] = FieldInfo(alias="classificationMethod", default=None)
    """
    The classification method used, which will always be the LLM classifier in this
    case
    """

    classifier_version: Optional[str] = FieldInfo(alias="classifierVersion", default=None)
    """LLM classifier version"""

    confidence: Optional[float] = None
    """How confident the classifier is of this input being classifies as this label"""

    snippet: Optional[str] = None
    """The context snippet (associated with the value that was classified)"""

    type: Optional[str] = None
    """Label that the input is classified into"""

    value: Optional[str] = None
    """The entity that was classified"""


ClassifyClassifyUnstructuredTextResponse: TypeAlias = List[List[ClassifyClassifyUnstructuredTextResponseItem]]
