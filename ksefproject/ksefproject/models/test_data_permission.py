from collections.abc import Mapping
from typing import Any, TypeVar, Optional, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.test_data_permission_type import TestDataPermissionType






T = TypeVar("T", bound="TestDataPermission")



@_attrs_define
class TestDataPermission:
    """ 
        Attributes:
            description (str):
            permission_type (TestDataPermissionType):
     """

    description: str
    permission_type: TestDataPermissionType





    def to_dict(self) -> dict[str, Any]:
        description = self.description

        permission_type = self.permission_type.value


        field_dict: dict[str, Any] = {}

        field_dict.update({
            "description": description,
            "permissionType": permission_type,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        description = d.pop("description")

        permission_type = TestDataPermissionType(d.pop("permissionType"))




        test_data_permission = cls(
            description=description,
            permission_type=permission_type,
        )

        return test_data_permission

