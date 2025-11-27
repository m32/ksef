from collections.abc import Mapping
from typing import Any, TypeVar, Optional, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset







T = TypeVar("T", bound="Subunit")



@_attrs_define
class Subunit:
    """ 
        Attributes:
            subject_nip (str): 10 cyfrowy numer NIP.
            description (str):
     """

    subject_nip: str
    description: str





    def to_dict(self) -> dict[str, Any]:
        subject_nip = self.subject_nip

        description = self.description


        field_dict: dict[str, Any] = {}

        field_dict.update({
            "subjectNip": subject_nip,
            "description": description,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        subject_nip = d.pop("subjectNip")

        description = d.pop("description")

        subunit = cls(
            subject_nip=subject_nip,
            description=description,
        )

        return subunit

