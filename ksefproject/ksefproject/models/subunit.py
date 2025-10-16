from collections.abc import Mapping
from typing import Any, TypeVar, Optional, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast, Union
from typing import Union






T = TypeVar("T", bound="Subunit")



@_attrs_define
class Subunit:
    """ 
        Attributes:
            subject_nip (Union[None, Unset, str]):
            description (Union[None, Unset, str]):
     """

    subject_nip: Union[None, Unset, str] = UNSET
    description: Union[None, Unset, str] = UNSET





    def to_dict(self) -> dict[str, Any]:
        subject_nip: Union[None, Unset, str]
        if isinstance(self.subject_nip, Unset):
            subject_nip = UNSET
        else:
            subject_nip = self.subject_nip

        description: Union[None, Unset, str]
        if isinstance(self.description, Unset):
            description = UNSET
        else:
            description = self.description


        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
        if subject_nip is not UNSET:
            field_dict["subjectNip"] = subject_nip
        if description is not UNSET:
            field_dict["description"] = description

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        def _parse_subject_nip(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        subject_nip = _parse_subject_nip(d.pop("subjectNip", UNSET))


        def _parse_description(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        description = _parse_description(d.pop("description", UNSET))


        subunit = cls(
            subject_nip=subject_nip,
            description=description,
        )

        return subunit

