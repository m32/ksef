from collections.abc import Mapping
from typing import Any, TypeVar, Optional, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.person_permissions_subject_identifier_type import PersonPermissionsSubjectIdentifierType






T = TypeVar("T", bound="PersonPermissionsSubjectIdentifier")



@_attrs_define
class PersonPermissionsSubjectIdentifier:
    """ Identyfikator osoby fizycznej.
    | Type | Value |
    | --- | --- |
    | Nip | 10 cyfrowy numer NIP |
    | Pesel | 11 cyfrowy numer PESEL |
    | Fingerprint | Odcisk palca certyfikatu |

        Attributes:
            type_ (PersonPermissionsSubjectIdentifierType):
            value (str): Wartość identyfikatora.
     """

    type_: PersonPermissionsSubjectIdentifierType
    value: str





    def to_dict(self) -> dict[str, Any]:
        type_ = self.type_.value

        value = self.value


        field_dict: dict[str, Any] = {}

        field_dict.update({
            "type": type_,
            "value": value,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        type_ = PersonPermissionsSubjectIdentifierType(d.pop("type"))




        value = d.pop("value")

        person_permissions_subject_identifier = cls(
            type_=type_,
            value=value,
        )

        return person_permissions_subject_identifier

