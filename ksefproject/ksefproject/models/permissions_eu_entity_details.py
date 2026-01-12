from collections.abc import Mapping
from typing import Any, TypeVar, Optional, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset







T = TypeVar("T", bound="PermissionsEuEntityDetails")



@_attrs_define
class PermissionsEuEntityDetails:
    """ 
        Attributes:
            full_name (str): Pełna nazwa podmiotu unijnego.
            address (str): Adres podmiotu unijnego.
     """

    full_name: str
    address: str





    def to_dict(self) -> dict[str, Any]:
        full_name = self.full_name

        address = self.address


        field_dict: dict[str, Any] = {}

        field_dict.update({
            "fullName": full_name,
            "address": address,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        full_name = d.pop("fullName")

        address = d.pop("address")

        permissions_eu_entity_details = cls(
            full_name=full_name,
            address=address,
        )

        return permissions_eu_entity_details

