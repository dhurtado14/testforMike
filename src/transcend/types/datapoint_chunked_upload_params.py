# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable
from typing_extensions import Required, Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["DatapointChunkedUploadParams"]


class DatapointChunkedUploadParams(TypedDict, total=False):
    data: Required[Iterable[object]]
    """An array of data to be uploaded for that datapoints.

    This is typically a page worth of JSON data
    """

    data_point_name: Required[Annotated[str, PropertyInfo(alias="dataPointName")]]
    """The name of the datapoint that data is being uploaded for."""

    x_transcend_nonce: Required[Annotated[str, PropertyInfo(alias="x-transcend-nonce")]]

    file_id: Annotated[str, PropertyInfo(alias="fileId")]
    """Give the chunk of data being uploaded a title.

    For example, if the data is some date range, you could title the file
    "mm/dd/yyy - mm/dd/yyy"
    """

    is_last_page: Annotated[bool, PropertyInfo(alias="isLastPage")]
    """
    Set to true when you upload your final page of data (you may also upload an
    empty list with isLastPage=true). When this value is set to true, the datapoint
    will be marked as completed.
    """

    x_sombra_authorization: Annotated[str, PropertyInfo(alias="x-sombra-authorization")]
