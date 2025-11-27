from collections.abc import Mapping
from typing import Any, TypeVar, Optional, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset







T = TypeVar("T", bound="AttachmentPermissionGrantRequest")



@_attrs_define
class AttachmentPermissionGrantRequest:
    """ 
        Attributes:
            nip (str): 10 cyfrowy numer NIP.
     """

    nip: str





    def to_dict(self) -> dict[str, Any]:
        nip = self.nip


        field_dict: dict[str, Any] = {}

        field_dict.update({
            "nip": nip,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        nip = d.pop("nip")

        attachment_permission_grant_request = cls(
            nip=nip,
        )

        return attachment_permission_grant_request

