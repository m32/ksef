from collections.abc import Mapping
from typing import Any, TypeVar, Optional, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset







T = TypeVar("T", bound="EntityDetails")



@_attrs_define
class EntityDetails:
    """ 
        Attributes:
            full_name (str): Pełna nazwa podmiotu.
     """

    full_name: str





    def to_dict(self) -> dict[str, Any]:
        full_name = self.full_name


        field_dict: dict[str, Any] = {}

        field_dict.update({
            "fullName": full_name,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        full_name = d.pop("fullName")

        entity_details = cls(
            full_name=full_name,
        )

        return entity_details

