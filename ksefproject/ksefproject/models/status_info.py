from collections.abc import Mapping
from typing import Any, TypeVar, Optional, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast
from typing import cast, Union
from typing import Union






T = TypeVar("T", bound="StatusInfo")



@_attrs_define
class StatusInfo:
    """ 
        Attributes:
            code (int): Kod statusu
            description (str): Opis statusu
            details (Union[None, Unset, list[str]]): Dodatkowe szczegóły statusu
     """

    code: int
    description: str
    details: Union[None, Unset, list[str]] = UNSET





    def to_dict(self) -> dict[str, Any]:
        code = self.code

        description = self.description

        details: Union[None, Unset, list[str]]
        if isinstance(self.details, Unset):
            details = UNSET
        elif isinstance(self.details, list):
            details = self.details


        else:
            details = self.details


        field_dict: dict[str, Any] = {}

        field_dict.update({
            "code": code,
            "description": description,
        })
        if details is not UNSET:
            field_dict["details"] = details

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        code = d.pop("code")

        description = d.pop("description")

        def _parse_details(data: object) -> Union[None, Unset, list[str]]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                details_type_0 = cast(list[str], data)

                return details_type_0
            except: # noqa: E722
                pass
            return cast(Union[None, Unset, list[str]], data)

        details = _parse_details(d.pop("details", UNSET))


        status_info = cls(
            code=code,
            description=description,
            details=details,
        )

        return status_info

