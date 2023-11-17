""" Diaspora Event Fabric: Resilience-enabling services for science from HPC to edge.

"""
from diaspora_event_sdk.version import __version__ as _version

__author__ = "The Diaspora Event Team"
__version__ = _version

from diaspora_event_sdk.sdk.client import Client  # Globus client
from diaspora_event_sdk.sdk.kafka_client import Producer, Consumer, KafkaAdmin, NewTopic


__all__ = ("Client", "Producer", "Consumer", "KafkaAdmin", "NewTopic")
