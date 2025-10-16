from collections.abc import Mapping
from typing import Any, TypeVar, Optional, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.token_author_identifier_type import TokenAuthorIdentifierType






T = TypeVar("T", bound="TokenAuthorIdentifierTypeIdentifier")



@_attrs_define
class TokenAuthorIdentifierTypeIdentifier:
    """ 
        Attributes:
            type_ (TokenAuthorIdentifierType): | Wartość | Opis |
                | --- | --- |
                | Nip | NIP. |
                | Pesel | PESEL. |
                | Fingerprint | Odcisk palca certyfikatu. |
            value (str): Wartość identyfikatora.
     """

    type_: TokenAuthorIdentifierType
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
        type_ = TokenAuthorIdentifierType(d.pop("type"))




        value = d.pop("value")

        token_author_identifier_type_identifier = cls(
            type_=type_,
            value=value,
        )

        return token_author_identifier_type_identifier

