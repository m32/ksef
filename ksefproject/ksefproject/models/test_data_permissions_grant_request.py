from collections.abc import Mapping
from typing import Any, TypeVar, Optional, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast
from typing import cast, Union
from typing import Union

if TYPE_CHECKING:
  from ..models.test_data_context_identifier import TestDataContextIdentifier
  from ..models.test_data_authorized_identifier import TestDataAuthorizedIdentifier
  from ..models.test_data_permission import TestDataPermission





T = TypeVar("T", bound="TestDataPermissionsGrantRequest")



@_attrs_define
class TestDataPermissionsGrantRequest:
    """ 
        Attributes:
            context_identifier (Union['TestDataContextIdentifier', None, Unset]):
            authorized_identifier (Union['TestDataAuthorizedIdentifier', None, Unset]):
            permissions (Union[None, Unset, list['TestDataPermission']]):
     """

    context_identifier: Union['TestDataContextIdentifier', None, Unset] = UNSET
    authorized_identifier: Union['TestDataAuthorizedIdentifier', None, Unset] = UNSET
    permissions: Union[None, Unset, list['TestDataPermission']] = UNSET





    def to_dict(self) -> dict[str, Any]:
        from ..models.test_data_context_identifier import TestDataContextIdentifier
        from ..models.test_data_authorized_identifier import TestDataAuthorizedIdentifier
        from ..models.test_data_permission import TestDataPermission
        context_identifier: Union[None, Unset, dict[str, Any]]
        if isinstance(self.context_identifier, Unset):
            context_identifier = UNSET
        elif isinstance(self.context_identifier, TestDataContextIdentifier):
            context_identifier = self.context_identifier.to_dict()
        else:
            context_identifier = self.context_identifier

        authorized_identifier: Union[None, Unset, dict[str, Any]]
        if isinstance(self.authorized_identifier, Unset):
            authorized_identifier = UNSET
        elif isinstance(self.authorized_identifier, TestDataAuthorizedIdentifier):
            authorized_identifier = self.authorized_identifier.to_dict()
        else:
            authorized_identifier = self.authorized_identifier

        permissions: Union[None, Unset, list[dict[str, Any]]]
        if isinstance(self.permissions, Unset):
            permissions = UNSET
        elif isinstance(self.permissions, list):
            permissions = []
            for permissions_type_0_item_data in self.permissions:
                permissions_type_0_item = permissions_type_0_item_data.to_dict()
                permissions.append(permissions_type_0_item)


        else:
            permissions = self.permissions


        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
        if context_identifier is not UNSET:
            field_dict["contextIdentifier"] = context_identifier
        if authorized_identifier is not UNSET:
            field_dict["authorizedIdentifier"] = authorized_identifier
        if permissions is not UNSET:
            field_dict["permissions"] = permissions

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.test_data_context_identifier import TestDataContextIdentifier
        from ..models.test_data_authorized_identifier import TestDataAuthorizedIdentifier
        from ..models.test_data_permission import TestDataPermission
        d = dict(src_dict)
        def _parse_context_identifier(data: object) -> Union['TestDataContextIdentifier', None, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                context_identifier_type_1 = TestDataContextIdentifier.from_dict(data)



                return context_identifier_type_1
            except: # noqa: E722
                pass
            return cast(Union['TestDataContextIdentifier', None, Unset], data)

        context_identifier = _parse_context_identifier(d.pop("contextIdentifier", UNSET))


        def _parse_authorized_identifier(data: object) -> Union['TestDataAuthorizedIdentifier', None, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                authorized_identifier_type_1 = TestDataAuthorizedIdentifier.from_dict(data)



                return authorized_identifier_type_1
            except: # noqa: E722
                pass
            return cast(Union['TestDataAuthorizedIdentifier', None, Unset], data)

        authorized_identifier = _parse_authorized_identifier(d.pop("authorizedIdentifier", UNSET))


        def _parse_permissions(data: object) -> Union[None, Unset, list['TestDataPermission']]:
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
                    permissions_type_0_item = TestDataPermission.from_dict(permissions_type_0_item_data)



                    permissions_type_0.append(permissions_type_0_item)

                return permissions_type_0
            except: # noqa: E722
                pass
            return cast(Union[None, Unset, list['TestDataPermission']], data)

        permissions = _parse_permissions(d.pop("permissions", UNSET))


        test_data_permissions_grant_request = cls(
            context_identifier=context_identifier,
            authorized_identifier=authorized_identifier,
            permissions=permissions,
        )

        return test_data_permissions_grant_request

