from collections.abc import Mapping
from typing import Any, TypeVar, Optional, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.test_data_authentication_context_identifier_type import TestDataAuthenticationContextIdentifierType






T = TypeVar("T", bound="TestDataAuthenticationContextIdentifier")



@_attrs_define
class TestDataAuthenticationContextIdentifier:
    """ 
        Attributes:
            value (str):
            type_ (TestDataAuthenticationContextIdentifierType):
     """

    value: str
    type_: TestDataAuthenticationContextIdentifierType





    def to_dict(self) -> dict[str, Any]:
        value = self.value

        type_ = self.type_.value


        field_dict: dict[str, Any] = {}

        field_dict.update({
            "value": value,
            "type": type_,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        value = d.pop("value")

        type_ = TestDataAuthenticationContextIdentifierType(d.pop("type"))




        test_data_authentication_context_identifier = cls(
            value=value,
            type_=type_,
        )

        return test_data_authentication_context_identifier

