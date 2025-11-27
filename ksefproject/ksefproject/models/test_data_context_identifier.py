from collections.abc import Mapping
from typing import Any, TypeVar, Optional, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.test_data_context_identifier_type import TestDataContextIdentifierType






T = TypeVar("T", bound="TestDataContextIdentifier")



@_attrs_define
class TestDataContextIdentifier:
    """ 
        Attributes:
            type_ (TestDataContextIdentifierType):
            value (str):
     """

    type_: TestDataContextIdentifierType
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
        type_ = TestDataContextIdentifierType(d.pop("type"))




        value = d.pop("value")

        test_data_context_identifier = cls(
            type_=type_,
            value=value,
        )

        return test_data_context_identifier

