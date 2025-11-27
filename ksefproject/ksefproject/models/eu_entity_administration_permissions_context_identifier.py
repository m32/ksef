from collections.abc import Mapping
from typing import Any, TypeVar, Optional, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.eu_entity_administration_permissions_context_identifier_type import EuEntityAdministrationPermissionsContextIdentifierType






T = TypeVar("T", bound="EuEntityAdministrationPermissionsContextIdentifier")



@_attrs_define
class EuEntityAdministrationPermissionsContextIdentifier:
    """ Identyfikator kontekstu złożonego.
    | Type | Value |
    | --- | --- |
    | NipVatUe | Dwuczłonowy identyfikator składający się z numeru NIP i numeru VAT-UE: `{nip}-{vat_ue}` |

        Attributes:
            type_ (EuEntityAdministrationPermissionsContextIdentifierType):
            value (str): Wartość identyfikatora.
     """

    type_: EuEntityAdministrationPermissionsContextIdentifierType
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
        type_ = EuEntityAdministrationPermissionsContextIdentifierType(d.pop("type"))




        value = d.pop("value")

        eu_entity_administration_permissions_context_identifier = cls(
            type_=type_,
            value=value,
        )

        return eu_entity_administration_permissions_context_identifier

