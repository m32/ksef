from collections.abc import Mapping
from typing import Any, TypeVar, Optional, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.token_permission_type import TokenPermissionType
from typing import cast






T = TypeVar("T", bound="GenerateTokenRequest")



@_attrs_define
class GenerateTokenRequest:
    """ 
        Attributes:
            permissions (list[TokenPermissionType]): Uprawnienia przypisane tokenowi.
            description (str): Opis tokena.
     """

    permissions: list[TokenPermissionType]
    description: str





    def to_dict(self) -> dict[str, Any]:
        permissions = []
        for permissions_item_data in self.permissions:
            permissions_item = permissions_item_data.value
            permissions.append(permissions_item)



        description = self.description


        field_dict: dict[str, Any] = {}

        field_dict.update({
            "permissions": permissions,
            "description": description,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        permissions = []
        _permissions = d.pop("permissions")
        for permissions_item_data in (_permissions):
            permissions_item = TokenPermissionType(permissions_item_data)



            permissions.append(permissions_item)


        description = d.pop("description")

        generate_token_request = cls(
            permissions=permissions,
            description=description,
        )

        return generate_token_request

