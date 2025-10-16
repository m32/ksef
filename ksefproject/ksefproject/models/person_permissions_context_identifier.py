from collections.abc import Mapping
from typing import Any, TypeVar, Optional, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.person_permissions_context_identifier_type import PersonPermissionsContextIdentifierType






T = TypeVar("T", bound="PersonPermissionsContextIdentifier")



@_attrs_define
class PersonPermissionsContextIdentifier:
    """ Identyfikator kontekstu uprawnienia (dla uprawnień nadanych administratorom jednostek podrzędnych).
    | Type | Value |
    | --- | --- |
    | Nip | 10 cyfrowy numer NIP |
    | InternalId | Dwuczłonowy identyfikator składający się z numeru NIP i 5 cyfr: `{nip}-{5_cyfr}` |

        Attributes:
            type_ (PersonPermissionsContextIdentifierType):
            value (str): Wartość identyfikatora.
     """

    type_: PersonPermissionsContextIdentifierType
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
        type_ = PersonPermissionsContextIdentifierType(d.pop("type"))




        value = d.pop("value")

        person_permissions_context_identifier = cls(
            type_=type_,
            value=value,
        )

        return person_permissions_context_identifier

