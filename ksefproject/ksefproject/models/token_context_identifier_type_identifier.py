from collections.abc import Mapping
from typing import Any, TypeVar, Optional, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.token_context_identifier_type import TokenContextIdentifierType






T = TypeVar("T", bound="TokenContextIdentifierTypeIdentifier")



@_attrs_define
class TokenContextIdentifierTypeIdentifier:
    """ 
        Attributes:
            type_ (TokenContextIdentifierType): | Wartość | Opis |
                | --- | --- |
                | Nip | NIP. |
                | InternalId | Identyfikator wewnętrzny. |
                | NipVatUe | Dwuczłonowy identyfikator składający się z numeru NIP i numeru VAT-UE: `{nip}-{vat_ue}`. |
                | PeppolId | Identyfikator dostawcy usług Peppol. |
            value (str): Wartość identyfikatora.
     """

    type_: TokenContextIdentifierType
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
        type_ = TokenContextIdentifierType(d.pop("type"))




        value = d.pop("value")

        token_context_identifier_type_identifier = cls(
            type_=type_,
            value=value,
        )

        return token_context_identifier_type_identifier

