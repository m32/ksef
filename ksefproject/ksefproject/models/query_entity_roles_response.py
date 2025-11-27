from collections.abc import Mapping
from typing import Any, TypeVar, Optional, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from typing import cast

if TYPE_CHECKING:
  from ..models.entity_role import EntityRole





T = TypeVar("T", bound="QueryEntityRolesResponse")



@_attrs_define
class QueryEntityRolesResponse:
    """ 
        Attributes:
            roles (list['EntityRole']): Lista odczytanych ról podmiotu.
            has_more (bool): Flaga informująca o dostępności kolejnej strony wyników.
     """

    roles: list['EntityRole']
    has_more: bool





    def to_dict(self) -> dict[str, Any]:
        from ..models.entity_role import EntityRole
        roles = []
        for roles_item_data in self.roles:
            roles_item = roles_item_data.to_dict()
            roles.append(roles_item)



        has_more = self.has_more


        field_dict: dict[str, Any] = {}

        field_dict.update({
            "roles": roles,
            "hasMore": has_more,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.entity_role import EntityRole
        d = dict(src_dict)
        roles = []
        _roles = d.pop("roles")
        for roles_item_data in (_roles):
            roles_item = EntityRole.from_dict(roles_item_data)



            roles.append(roles_item)


        has_more = d.pop("hasMore")

        query_entity_roles_response = cls(
            roles=roles,
            has_more=has_more,
        )

        return query_entity_roles_response

