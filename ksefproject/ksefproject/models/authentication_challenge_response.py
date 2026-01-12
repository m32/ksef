from collections.abc import Mapping
from typing import Any, TypeVar, Optional, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from dateutil.parser import isoparse
from typing import cast
import datetime






T = TypeVar("T", bound="AuthenticationChallengeResponse")



@_attrs_define
class AuthenticationChallengeResponse:
    """ 
        Attributes:
            challenge (str): Unikalny challenge.
            timestamp (datetime.datetime): Czas wygenerowania challenge-a.
            timestamp_ms (int): Czas wygenerowania challenge-a w milisekundach od 1 stycznia 1970 roku (Unix timestamp).
     """

    challenge: str
    timestamp: datetime.datetime
    timestamp_ms: int





    def to_dict(self) -> dict[str, Any]:
        challenge = self.challenge

        timestamp = self.timestamp.isoformat()

        timestamp_ms = self.timestamp_ms


        field_dict: dict[str, Any] = {}

        field_dict.update({
            "challenge": challenge,
            "timestamp": timestamp,
            "timestampMs": timestamp_ms,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        challenge = d.pop("challenge")

        timestamp = isoparse(d.pop("timestamp"))




        timestamp_ms = d.pop("timestampMs")

        authentication_challenge_response = cls(
            challenge=challenge,
            timestamp=timestamp,
            timestamp_ms=timestamp_ms,
        )

        return authentication_challenge_response

