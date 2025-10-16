from collections.abc import Mapping
from typing import Any, TypeVar, Optional, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from dateutil.parser import isoparse
from typing import cast
import datetime






T = TypeVar("T", bound="TokenInfo")



@_attrs_define
class TokenInfo:
    """ 
        Attributes:
            token (str): Token w formacie JWT.
            valid_until (datetime.datetime): Data ważności tokena.
     """

    token: str
    valid_until: datetime.datetime





    def to_dict(self) -> dict[str, Any]:
        token = self.token

        valid_until = self.valid_until.isoformat()


        field_dict: dict[str, Any] = {}

        field_dict.update({
            "token": token,
            "validUntil": valid_until,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        token = d.pop("token")

        valid_until = isoparse(d.pop("validUntil"))




        token_info = cls(
            token=token,
            valid_until=valid_until,
        )

        return token_info

