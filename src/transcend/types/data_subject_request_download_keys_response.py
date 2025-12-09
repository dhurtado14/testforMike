# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = [
    "DataSubjectRequestDownloadKeysResponse",
    "_Links",
    "Node",
    "NodeDataPoint",
    "NodeDataPointDataSilo",
    "NodeDataPointDescription",
    "NodeDataPointMetadata",
    "NodeDataPointTitle",
]


class _Links(BaseModel):
    """Pagination information"""

    self: str
    """The URL path of this page."""

    next: Optional[str] = None
    """The URL path for the next page."""

    prev: Optional[str] = None
    """The URL path of the previous page."""


class NodeDataPointDataSilo(BaseModel):
    """Information about the associated integration in Transcend."""

    id: str
    """The ID of this integration in Transcend."""

    description: str
    """The description of integration in Transcend."""

    outer_type: Optional[str] = FieldInfo(alias="outerType", default=None)
    """The outer type of the integration in Transcend."""

    title: str
    """The title of integration in Transcend."""

    type: str
    """The type of integration in Transcend."""


class NodeDataPointDescription(BaseModel):
    """Information about an internationalized message."""

    id: str
    """The ID of this message in Transcend."""

    default_message: str = FieldInfo(alias="defaultMessage")
    """The defaultMessage of the message."""


class NodeDataPointMetadata(BaseModel):
    """Metadata about the datapoint."""

    references: Optional[List[str]] = None
    """References to documentation about the datapoint."""


class NodeDataPointTitle(BaseModel):
    """Information about an internationalized message."""

    id: str
    """The ID of this message in Transcend."""

    default_message: str = FieldInfo(alias="defaultMessage")
    """The defaultMessage of the message."""


class NodeDataPoint(BaseModel):
    """Information about the associated with a datapoint when listing request files."""

    id: str
    """The ID of this datapoint in Transcend."""

    data_silo: NodeDataPointDataSilo = FieldInfo(alias="dataSilo")
    """Information about the associated integration in Transcend."""

    description: Optional[NodeDataPointDescription] = None
    """Information about an internationalized message."""

    encryption: Optional[str] = None
    """The encryption of the datapoint."""

    metadata: NodeDataPointMetadata
    """Metadata about the datapoint."""

    name: str
    """The name of the datapoint."""

    slug: str
    """The slug of the datapoint."""

    title: Optional[NodeDataPointTitle] = None
    """Information about an internationalized message."""

    path: Optional[List[str]] = None
    """The schema of the datapoint within the database."""


class Node(BaseModel):
    data_point: NodeDataPoint = FieldInfo(alias="dataPoint")
    """Information about the associated with a datapoint when listing request files."""

    download_key: str = FieldInfo(alias="downloadKey")
    """Access key for file, a long string"""

    error: Optional[str] = None
    """Nullable"""

    mimetype: str
    """The media type as a MIMETYPE."""

    size: float
    """Size of the file in bytes."""

    file_name: Optional[str] = FieldInfo(alias="fileName", default=None)


class DataSubjectRequestDownloadKeysResponse(BaseModel):
    api_links: _Links = FieldInfo(alias="_links")
    """Pagination information"""

    nodes: List[Node]
    """List of files available for download."""

    total_count: float = FieldInfo(alias="totalCount")
    """Total number of files available for download."""
