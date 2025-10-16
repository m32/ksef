from collections.abc import Mapping
from typing import Any, TypeVar, Optional, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast
from typing import cast, Union
from typing import Union

if TYPE_CHECKING:
  from ..models.allowed_ips import AllowedIps





T = TypeVar("T", bound="AuthorizationPolicy")



@_attrs_define
class AuthorizationPolicy:
    """ 
        Attributes:
            allowed_ips (Union['AllowedIps', None, Unset]): Lista dozwolonych adresów IP.
     """

    allowed_ips: Union['AllowedIps', None, Unset] = UNSET





    def to_dict(self) -> dict[str, Any]:
        from ..models.allowed_ips import AllowedIps
        allowed_ips: Union[None, Unset, dict[str, Any]]
        if isinstance(self.allowed_ips, Unset):
            allowed_ips = UNSET
        elif isinstance(self.allowed_ips, AllowedIps):
            allowed_ips = self.allowed_ips.to_dict()
        else:
            allowed_ips = self.allowed_ips


        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
        if allowed_ips is not UNSET:
            field_dict["allowedIps"] = allowed_ips

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.allowed_ips import AllowedIps
        d = dict(src_dict)
        def _parse_allowed_ips(data: object) -> Union['AllowedIps', None, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                allowed_ips_type_1 = AllowedIps.from_dict(data)



                return allowed_ips_type_1
            except: # noqa: E722
                pass
            return cast(Union['AllowedIps', None, Unset], data)

        allowed_ips = _parse_allowed_ips(d.pop("allowedIps", UNSET))


        authorization_policy = cls(
            allowed_ips=allowed_ips,
        )

        return authorization_policy

