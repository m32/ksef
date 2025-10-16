from collections.abc import Mapping
from typing import Any, TypeVar, Optional, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast, Union
from typing import Union






T = TypeVar("T", bound="AttachmentPermissionRevokeRequest")



@_attrs_define
class AttachmentPermissionRevokeRequest:
    """ 
        Attributes:
            nip (Union[None, Unset, str]):
     """

    nip: Union[None, Unset, str] = UNSET





    def to_dict(self) -> dict[str, Any]:
        nip: Union[None, Unset, str]
        if isinstance(self.nip, Unset):
            nip = UNSET
        else:
            nip = self.nip


        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
        if nip is not UNSET:
            field_dict["nip"] = nip

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        def _parse_nip(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        nip = _parse_nip(d.pop("nip", UNSET))


        attachment_permission_revoke_request = cls(
            nip=nip,
        )

        return attachment_permission_revoke_request

