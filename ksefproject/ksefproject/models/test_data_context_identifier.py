from collections.abc import Mapping
from typing import Any, TypeVar, Optional, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.test_data_context_identifier_type import TestDataContextIdentifierType
from ..types import UNSET, Unset
from typing import cast, Union
from typing import Union






T = TypeVar("T", bound="TestDataContextIdentifier")



@_attrs_define
class TestDataContextIdentifier:
    """ 
        Attributes:
            type_ (Union[Unset, TestDataContextIdentifierType]):
            value (Union[None, Unset, str]):
     """

    type_: Union[Unset, TestDataContextIdentifierType] = UNSET
    value: Union[None, Unset, str] = UNSET





    def to_dict(self) -> dict[str, Any]:
        type_: Union[Unset, str] = UNSET
        if not isinstance(self.type_, Unset):
            type_ = self.type_.value


        value: Union[None, Unset, str]
        if isinstance(self.value, Unset):
            value = UNSET
        else:
            value = self.value


        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
        if type_ is not UNSET:
            field_dict["type"] = type_
        if value is not UNSET:
            field_dict["value"] = value

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        _type_ = d.pop("type", UNSET)
        type_: Union[Unset, TestDataContextIdentifierType]
        if isinstance(_type_,  Unset):
            type_ = UNSET
        else:
            type_ = TestDataContextIdentifierType(_type_)




        def _parse_value(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        value = _parse_value(d.pop("value", UNSET))


        test_data_context_identifier = cls(
            type_=type_,
            value=value,
        )

        return test_data_context_identifier

