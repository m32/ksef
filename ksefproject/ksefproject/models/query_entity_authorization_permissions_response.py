from collections.abc import Mapping
from typing import Any, TypeVar, Optional, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from typing import cast

if TYPE_CHECKING:
  from ..models.entity_authorization_grant import EntityAuthorizationGrant





T = TypeVar("T", bound="QueryEntityAuthorizationPermissionsResponse")



@_attrs_define
class QueryEntityAuthorizationPermissionsResponse:
    """ 
        Attributes:
            authorization_grants (list['EntityAuthorizationGrant']): Lista odczytanych uprawnień.
            has_more (bool): Flaga informująca o dostępności kolejnej strony wyników.
     """

    authorization_grants: list['EntityAuthorizationGrant']
    has_more: bool





    def to_dict(self) -> dict[str, Any]:
        from ..models.entity_authorization_grant import EntityAuthorizationGrant
        authorization_grants = []
        for authorization_grants_item_data in self.authorization_grants:
            authorization_grants_item = authorization_grants_item_data.to_dict()
            authorization_grants.append(authorization_grants_item)



        has_more = self.has_more


        field_dict: dict[str, Any] = {}

        field_dict.update({
            "authorizationGrants": authorization_grants,
            "hasMore": has_more,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.entity_authorization_grant import EntityAuthorizationGrant
        d = dict(src_dict)
        authorization_grants = []
        _authorization_grants = d.pop("authorizationGrants")
        for authorization_grants_item_data in (_authorization_grants):
            authorization_grants_item = EntityAuthorizationGrant.from_dict(authorization_grants_item_data)



            authorization_grants.append(authorization_grants_item)


        has_more = d.pop("hasMore")

        query_entity_authorization_permissions_response = cls(
            authorization_grants=authorization_grants,
            has_more=has_more,
        )

        return query_entity_authorization_permissions_response

