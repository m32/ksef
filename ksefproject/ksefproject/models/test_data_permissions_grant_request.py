from collections.abc import Mapping
from typing import Any, TypeVar, Optional, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from typing import cast

if TYPE_CHECKING:
  from ..models.test_data_authorized_identifier import TestDataAuthorizedIdentifier
  from ..models.test_data_permission import TestDataPermission
  from ..models.test_data_context_identifier import TestDataContextIdentifier





T = TypeVar("T", bound="TestDataPermissionsGrantRequest")



@_attrs_define
class TestDataPermissionsGrantRequest:
    """ 
        Attributes:
            context_identifier (TestDataContextIdentifier):
            authorized_identifier (TestDataAuthorizedIdentifier):
            permissions (list['TestDataPermission']):
     """

    context_identifier: 'TestDataContextIdentifier'
    authorized_identifier: 'TestDataAuthorizedIdentifier'
    permissions: list['TestDataPermission']





    def to_dict(self) -> dict[str, Any]:
        from ..models.test_data_authorized_identifier import TestDataAuthorizedIdentifier
        from ..models.test_data_permission import TestDataPermission
        from ..models.test_data_context_identifier import TestDataContextIdentifier
        context_identifier = self.context_identifier.to_dict()

        authorized_identifier = self.authorized_identifier.to_dict()

        permissions = []
        for permissions_item_data in self.permissions:
            permissions_item = permissions_item_data.to_dict()
            permissions.append(permissions_item)




        field_dict: dict[str, Any] = {}

        field_dict.update({
            "contextIdentifier": context_identifier,
            "authorizedIdentifier": authorized_identifier,
            "permissions": permissions,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.test_data_authorized_identifier import TestDataAuthorizedIdentifier
        from ..models.test_data_permission import TestDataPermission
        from ..models.test_data_context_identifier import TestDataContextIdentifier
        d = dict(src_dict)
        context_identifier = TestDataContextIdentifier.from_dict(d.pop("contextIdentifier"))




        authorized_identifier = TestDataAuthorizedIdentifier.from_dict(d.pop("authorizedIdentifier"))




        permissions = []
        _permissions = d.pop("permissions")
        for permissions_item_data in (_permissions):
            permissions_item = TestDataPermission.from_dict(permissions_item_data)



            permissions.append(permissions_item)


        test_data_permissions_grant_request = cls(
            context_identifier=context_identifier,
            authorized_identifier=authorized_identifier,
            permissions=permissions,
        )

        return test_data_permissions_grant_request

