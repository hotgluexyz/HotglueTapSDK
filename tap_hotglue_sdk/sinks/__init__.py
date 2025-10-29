"""Sink classes for targets."""

from tap_hotglue_sdk.sinks.batch import BatchSink
from tap_hotglue_sdk.sinks.core import Sink
from tap_hotglue_sdk.sinks.record import RecordSink
from tap_hotglue_sdk.sinks.sql import SQLConnector, SQLSink

__all__ = [
    "BatchSink",
    "RecordSink",
    "Sink",
    "SQLSink",
    "SQLConnector",
]
