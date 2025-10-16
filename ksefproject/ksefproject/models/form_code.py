from collections.abc import Mapping
from typing import Any, TypeVar, Optional, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset







T = TypeVar("T", bound="FormCode")



@_attrs_define
class FormCode:
    """ 
        Attributes:
            system_code (str): Kod systemowy
            schema_version (str): Wersja schematu
            value (str): Wartość
     """

    system_code: str
    schema_version: str
    value: str





    def to_dict(self) -> dict[str, Any]:
        system_code = self.system_code

        schema_version = self.schema_version

        value = self.value


        field_dict: dict[str, Any] = {}

        field_dict.update({
            "systemCode": system_code,
            "schemaVersion": schema_version,
            "value": value,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        system_code = d.pop("systemCode")

        schema_version = d.pop("schemaVersion")

        value = d.pop("value")

        form_code = cls(
            system_code=system_code,
            schema_version=schema_version,
            value=value,
        )

        return form_code

