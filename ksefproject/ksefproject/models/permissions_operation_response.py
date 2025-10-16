from collections.abc import Mapping
from typing import Any, TypeVar, Optional, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast, Union
from typing import Union






T = TypeVar("T", bound="PermissionsOperationResponse")



@_attrs_define
class PermissionsOperationResponse:
    """ 
        Attributes:
            operation_reference_number (Union[None, Unset, str]): Numer referencyjny asynchronicznej operacji nadawania lub
                odbierania uprawnień.
     """

    operation_reference_number: Union[None, Unset, str] = UNSET





    def to_dict(self) -> dict[str, Any]:
        operation_reference_number: Union[None, Unset, str]
        if isinstance(self.operation_reference_number, Unset):
            operation_reference_number = UNSET
        else:
            operation_reference_number = self.operation_reference_number


        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
        if operation_reference_number is not UNSET:
            field_dict["operationReferenceNumber"] = operation_reference_number

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        def _parse_operation_reference_number(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        operation_reference_number = _parse_operation_reference_number(d.pop("operationReferenceNumber", UNSET))


        permissions_operation_response = cls(
            operation_reference_number=operation_reference_number,
        )

        return permissions_operation_response

