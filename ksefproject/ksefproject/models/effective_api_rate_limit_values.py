from collections.abc import Mapping
from typing import Any, TypeVar, Optional, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset







T = TypeVar("T", bound="EffectiveApiRateLimitValues")



@_attrs_define
class EffectiveApiRateLimitValues:
    """ 
        Attributes:
            per_second (int): Limit na sekundę.
            per_minute (int): Limit na minutę.
            per_hour (int): Limit na godzinę.
     """

    per_second: int
    per_minute: int
    per_hour: int





    def to_dict(self) -> dict[str, Any]:
        per_second = self.per_second

        per_minute = self.per_minute

        per_hour = self.per_hour


        field_dict: dict[str, Any] = {}

        field_dict.update({
            "perSecond": per_second,
            "perMinute": per_minute,
            "perHour": per_hour,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        per_second = d.pop("perSecond")

        per_minute = d.pop("perMinute")

        per_hour = d.pop("perHour")

        effective_api_rate_limit_values = cls(
            per_second=per_second,
            per_minute=per_minute,
            per_hour=per_hour,
        )

        return effective_api_rate_limit_values

