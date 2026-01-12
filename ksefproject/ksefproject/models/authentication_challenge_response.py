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
            timestampMs (int): Czas wygenerowania challenge-a w milisekundach od 1 stycznia 1970 roku (Unix timestamp).
     """

    challenge: str
    timestamp: datetime.datetime
    timestampMs: int




    def to_dict(self) -> dict[str, Any]:
        challenge = self.challenge

        timestamp = self.timestamp.isoformat()

        timestampMS = self.timestampMs


        field_dict: dict[str, Any] = {}

        field_dict.update({
            "challenge": challenge,
            "timestamp": timestamp,
            "timestampMs": timestampMs,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        challenge = d.pop("challenge")

        timestamp = isoparse(d.pop("timestamp"))

        timestampMs = d.pop("timestampMs")


        authentication_challenge_response = cls(
            challenge=challenge,
            timestamp=timestamp,
            timestampMs=timestampMs,
        )

        return authentication_challenge_response

