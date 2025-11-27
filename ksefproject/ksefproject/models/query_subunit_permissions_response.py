from collections.abc import Mapping
from typing import Any, TypeVar, Optional, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from typing import cast

if TYPE_CHECKING:
  from ..models.subunit_permission import SubunitPermission





T = TypeVar("T", bound="QuerySubunitPermissionsResponse")



@_attrs_define
class QuerySubunitPermissionsResponse:
    """ 
        Attributes:
            permissions (list['SubunitPermission']): Lista odczytanych uprawnień.
            has_more (bool): Flaga informująca o dostępności kolejnej strony wyników.
     """

    permissions: list['SubunitPermission']
    has_more: bool





    def to_dict(self) -> dict[str, Any]:
        from ..models.subunit_permission import SubunitPermission
        permissions = []
        for permissions_item_data in self.permissions:
            permissions_item = permissions_item_data.to_dict()
            permissions.append(permissions_item)



        has_more = self.has_more


        field_dict: dict[str, Any] = {}

        field_dict.update({
            "permissions": permissions,
            "hasMore": has_more,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.subunit_permission import SubunitPermission
        d = dict(src_dict)
        permissions = []
        _permissions = d.pop("permissions")
        for permissions_item_data in (_permissions):
            permissions_item = SubunitPermission.from_dict(permissions_item_data)



            permissions.append(permissions_item)


        has_more = d.pop("hasMore")

        query_subunit_permissions_response = cls(
            permissions=permissions,
            has_more=has_more,
        )

        return query_subunit_permissions_response

