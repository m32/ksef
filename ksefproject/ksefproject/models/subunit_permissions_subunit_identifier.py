from collections.abc import Mapping
from typing import Any, TypeVar, Optional, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.subunit_permissions_subunit_identifier_type import SubunitPermissionsSubunitIdentifierType






T = TypeVar("T", bound="SubunitPermissionsSubunitIdentifier")



@_attrs_define
class SubunitPermissionsSubunitIdentifier:
    """ Identyfikator jednostki lub podmiotu podrzędnego.
    | Type | Value |
    | --- | --- |
    | InternalId | Dwuczłonowy identyfikator składający się z numeru NIP i 5 cyfr: `{nip}-{5_cyfr}` |
    | Nip | 10 cyfrowy numer NIP |

        Attributes:
            type_ (SubunitPermissionsSubunitIdentifierType):
            value (str): Wartość identyfikatora.
     """

    type_: SubunitPermissionsSubunitIdentifierType
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
        type_ = SubunitPermissionsSubunitIdentifierType(d.pop("type"))




        value = d.pop("value")

        subunit_permissions_subunit_identifier = cls(
            type_=type_,
            value=value,
        )

        return subunit_permissions_subunit_identifier

