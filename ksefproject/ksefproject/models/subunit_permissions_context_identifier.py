from collections.abc import Mapping
from typing import Any, TypeVar, Optional, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.subunit_permissions_context_identifier_type import SubunitPermissionsContextIdentifierType






T = TypeVar("T", bound="SubunitPermissionsContextIdentifier")



@_attrs_define
class SubunitPermissionsContextIdentifier:
    """ Identyfikator podmiotu podrzędnego.
    | Type | Value |
    | --- | --- |
    | Nip | 10 cyfrowy numer NIP |
    | InternalId | Dwuczłonowy identyfikator składający się z numeru NIP i 5 cyfr: `{nip}-{5_cyfr}` |

        Attributes:
            type_ (SubunitPermissionsContextIdentifierType):
            value (str): Wartość identyfikatora.
     """

    type_: SubunitPermissionsContextIdentifierType
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
        type_ = SubunitPermissionsContextIdentifierType(d.pop("type"))




        value = d.pop("value")

        subunit_permissions_context_identifier = cls(
            type_=type_,
            value=value,
        )

        return subunit_permissions_context_identifier

