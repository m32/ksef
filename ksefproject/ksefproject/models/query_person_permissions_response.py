from collections.abc import Mapping
from typing import Any, TypeVar, Optional, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from typing import cast

if TYPE_CHECKING:
  from ..models.person_permission import PersonPermission





T = TypeVar("T", bound="QueryPersonPermissionsResponse")



@_attrs_define
class QueryPersonPermissionsResponse:
    """ 
        Attributes:
            permissions (list['PersonPermission']): Lista odczytanych uprawnień.
            has_more (bool): Flaga informująca o dostępności kolejnej strony wyników.
     """

    permissions: list['PersonPermission']
    has_more: bool





    def to_dict(self) -> dict[str, Any]:
        from ..models.person_permission import PersonPermission
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
        from ..models.person_permission import PersonPermission
        d = dict(src_dict)
        permissions = []
        _permissions = d.pop("permissions")
        for permissions_item_data in (_permissions):
            permissions_item = PersonPermission.from_dict(permissions_item_data)



            permissions.append(permissions_item)


        has_more = d.pop("hasMore")

        query_person_permissions_response = cls(
            permissions=permissions,
            has_more=has_more,
        )

        return query_person_permissions_response

