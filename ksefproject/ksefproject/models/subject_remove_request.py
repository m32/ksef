from collections.abc import Mapping
from typing import Any, TypeVar, Optional, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast, Union
from typing import Union






T = TypeVar("T", bound="SubjectRemoveRequest")



@_attrs_define
class SubjectRemoveRequest:
    """ 
        Attributes:
            subject_nip (Union[None, Unset, str]):
     """

    subject_nip: Union[None, Unset, str] = UNSET





    def to_dict(self) -> dict[str, Any]:
        subject_nip: Union[None, Unset, str]
        if isinstance(self.subject_nip, Unset):
            subject_nip = UNSET
        else:
            subject_nip = self.subject_nip


        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
        if subject_nip is not UNSET:
            field_dict["subjectNip"] = subject_nip

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


        subject_remove_request = cls(
            subject_nip=subject_nip,
        )

        return subject_remove_request

