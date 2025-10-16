from collections.abc import Mapping
from typing import Any, TypeVar, Optional, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.authentication_context_identifier_type import AuthenticationContextIdentifierType






T = TypeVar("T", bound="AuthenticationContextIdentifier")



@_attrs_define
class AuthenticationContextIdentifier:
    """ 
        Attributes:
            type_ (AuthenticationContextIdentifierType):
            value (str): Wartość identyfikatora
     """

    type_: AuthenticationContextIdentifierType
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
        type_ = AuthenticationContextIdentifierType(d.pop("type"))




        value = d.pop("value")

        authentication_context_identifier = cls(
            type_=type_,
            value=value,
        )

        return authentication_context_identifier

