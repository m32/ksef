from collections.abc import Mapping
from typing import Any, TypeVar, Optional, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from typing import cast

if TYPE_CHECKING:
  from ..models.api_rate_limits_override import ApiRateLimitsOverride





T = TypeVar("T", bound="SetRateLimitsRequest")



@_attrs_define
class SetRateLimitsRequest:
    """ 
        Attributes:
            rate_limits (ApiRateLimitsOverride):
     """

    rate_limits: 'ApiRateLimitsOverride'





    def to_dict(self) -> dict[str, Any]:
        from ..models.api_rate_limits_override import ApiRateLimitsOverride
        rate_limits = self.rate_limits.to_dict()


        field_dict: dict[str, Any] = {}

        field_dict.update({
            "rateLimits": rate_limits,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.api_rate_limits_override import ApiRateLimitsOverride
        d = dict(src_dict)
        rate_limits = ApiRateLimitsOverride.from_dict(d.pop("rateLimits"))




        set_rate_limits_request = cls(
            rate_limits=rate_limits,
        )

        return set_rate_limits_request

