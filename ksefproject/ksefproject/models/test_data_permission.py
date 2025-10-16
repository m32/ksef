from collections.abc import Mapping
from typing import Any, TypeVar, Optional, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.test_data_permission_type import TestDataPermissionType
from ..types import UNSET, Unset
from typing import cast, Union
from typing import Union






T = TypeVar("T", bound="TestDataPermission")



@_attrs_define
class TestDataPermission:
    """ 
        Attributes:
            description (Union[None, Unset, str]):
            permission_type (Union[Unset, TestDataPermissionType]):
     """

    description: Union[None, Unset, str] = UNSET
    permission_type: Union[Unset, TestDataPermissionType] = UNSET





    def to_dict(self) -> dict[str, Any]:
        description: Union[None, Unset, str]
        if isinstance(self.description, Unset):
            description = UNSET
        else:
            description = self.description

        permission_type: Union[Unset, str] = UNSET
        if not isinstance(self.permission_type, Unset):
            permission_type = self.permission_type.value



        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
        if description is not UNSET:
            field_dict["description"] = description
        if permission_type is not UNSET:
            field_dict["permissionType"] = permission_type

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        def _parse_description(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        description = _parse_description(d.pop("description", UNSET))


        _permission_type = d.pop("permissionType", UNSET)
        permission_type: Union[Unset, TestDataPermissionType]
        if isinstance(_permission_type,  Unset):
            permission_type = UNSET
        else:
            permission_type = TestDataPermissionType(_permission_type)




        test_data_permission = cls(
            description=description,
            permission_type=permission_type,
        )

        return test_data_permission

