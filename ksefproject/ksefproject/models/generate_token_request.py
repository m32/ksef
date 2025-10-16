from collections.abc import Mapping
from typing import Any, TypeVar, Optional, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.token_permission_type import TokenPermissionType
from ..types import UNSET, Unset
from typing import cast
from typing import cast, Union
from typing import Union






T = TypeVar("T", bound="GenerateTokenRequest")



@_attrs_define
class GenerateTokenRequest:
    """ 
        Attributes:
            permissions (Union[None, Unset, list[TokenPermissionType]]): Uprawnienia przypisane tokenowi.
            description (Union[None, Unset, str]): Opis tokena.
     """

    permissions: Union[None, Unset, list[TokenPermissionType]] = UNSET
    description: Union[None, Unset, str] = UNSET





    def to_dict(self) -> dict[str, Any]:
        permissions: Union[None, Unset, list[str]]
        if isinstance(self.permissions, Unset):
            permissions = UNSET
        elif isinstance(self.permissions, list):
            permissions = []
            for permissions_type_0_item_data in self.permissions:
                permissions_type_0_item = permissions_type_0_item_data.value
                permissions.append(permissions_type_0_item)


        else:
            permissions = self.permissions

        description: Union[None, Unset, str]
        if isinstance(self.description, Unset):
            description = UNSET
        else:
            description = self.description


        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
        if permissions is not UNSET:
            field_dict["permissions"] = permissions
        if description is not UNSET:
            field_dict["description"] = description

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        def _parse_permissions(data: object) -> Union[None, Unset, list[TokenPermissionType]]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                permissions_type_0 = []
                _permissions_type_0 = data
                for permissions_type_0_item_data in (_permissions_type_0):
                    permissions_type_0_item = TokenPermissionType(permissions_type_0_item_data)



                    permissions_type_0.append(permissions_type_0_item)

                return permissions_type_0
            except: # noqa: E722
                pass
            return cast(Union[None, Unset, list[TokenPermissionType]], data)

        permissions = _parse_permissions(d.pop("permissions", UNSET))


        def _parse_description(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        description = _parse_description(d.pop("description", UNSET))


        generate_token_request = cls(
            permissions=permissions,
            description=description,
        )

        return generate_token_request

