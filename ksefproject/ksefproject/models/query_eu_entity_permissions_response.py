from collections.abc import Mapping
from typing import Any, TypeVar, Optional, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from typing import cast

if TYPE_CHECKING:
  from ..models.eu_entity_permission import EuEntityPermission





T = TypeVar("T", bound="QueryEuEntityPermissionsResponse")



@_attrs_define
class QueryEuEntityPermissionsResponse:
    """ 
        Attributes:
            permissions (list['EuEntityPermission']): Lista odczytanych uprawnień.
            has_more (bool): Flaga informująca o dostępności kolejnej strony wyników.
     """

    permissions: list['EuEntityPermission']
    has_more: bool





    def to_dict(self) -> dict[str, Any]:
        from ..models.eu_entity_permission import EuEntityPermission
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
        from ..models.eu_entity_permission import EuEntityPermission
        d = dict(src_dict)
        permissions = []
        _permissions = d.pop("permissions")
        for permissions_item_data in (_permissions):
            permissions_item = EuEntityPermission.from_dict(permissions_item_data)



            permissions.append(permissions_item)


        has_more = d.pop("hasMore")

        query_eu_entity_permissions_response = cls(
            permissions=permissions,
            has_more=has_more,
        )

        return query_eu_entity_permissions_response

