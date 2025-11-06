"""SDK for building singer-compliant Singer taps."""

from tap_hotglue_sdk import streams
from tap_hotglue_sdk.mapper_base import InlineMapper
from tap_hotglue_sdk.plugin_base import PluginBase
from tap_hotglue_sdk.sinks import BatchSink, RecordSink, Sink, SQLSink
from tap_hotglue_sdk.streams import (
    GraphQLStream,
    RESTStream,
    SQLConnector,
    SQLStream,
    Stream,
)
from tap_hotglue_sdk.tap_base import SQLTap, Tap
from tap_hotglue_sdk.target_base import SQLTarget, Target

__all__ = [
    "BatchSink",
    "GraphQLStream",
    "InlineMapper",
    "PluginBase",
    "RecordSink",
    "RESTStream",
    "Sink",
    "SQLConnector",
    "SQLSink",
    "SQLStream",
    "SQLTap",
    "SQLTarget",
    "Stream",
    "streams",
    "Tap",
    "Target",
]
