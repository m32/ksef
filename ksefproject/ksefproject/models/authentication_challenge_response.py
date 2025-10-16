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
     """

    challenge: str
    timestamp: datetime.datetime





    def to_dict(self) -> dict[str, Any]:
        challenge = self.challenge

        timestamp = self.timestamp.isoformat()


        field_dict: dict[str, Any] = {}

        field_dict.update({
            "challenge": challenge,
            "timestamp": timestamp,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        challenge = d.pop("challenge")

        timestamp = isoparse(d.pop("timestamp"))




        authentication_challenge_response = cls(
            challenge=challenge,
            timestamp=timestamp,
        )

        return authentication_challenge_response

