from collections.abc import Mapping
from typing import Any, TypeVar, Optional, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset







T = TypeVar("T", bound="CertificateLimit")



@_attrs_define
class CertificateLimit:
    """ 
        Attributes:
            remaining (int): Pozostała wartość limitu.
            limit (int): Maksymalna liczba zasobów dozwolona w ramach limitu.
     """

    remaining: int
    limit: int





    def to_dict(self) -> dict[str, Any]:
        remaining = self.remaining

        limit = self.limit


        field_dict: dict[str, Any] = {}

        field_dict.update({
            "remaining": remaining,
            "limit": limit,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        remaining = d.pop("remaining")

        limit = d.pop("limit")

        certificate_limit = cls(
            remaining=remaining,
            limit=limit,
        )

        return certificate_limit

