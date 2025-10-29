"""SDK for building singer-compliant taps."""

from tap_hotglue_sdk.streams.core import Stream
from tap_hotglue_sdk.streams.graphql import GraphQLStream
from tap_hotglue_sdk.streams.rest import RESTStream
from tap_hotglue_sdk.streams.sql import SQLConnector, SQLStream

__all__ = [
    "Stream",
    "GraphQLStream",
    "RESTStream",
    "SQLStream",
    "SQLConnector",
]
