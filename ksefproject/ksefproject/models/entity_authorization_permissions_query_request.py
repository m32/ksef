from collections.abc import Mapping
from typing import Any, TypeVar, Optional, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.invoice_permission_type import InvoicePermissionType
from ..models.query_type import QueryType
from ..types import UNSET, Unset
from typing import cast
from typing import cast, Union
from typing import Union

if TYPE_CHECKING:
  from ..models.entity_authorizations_authorizing_entity_identifier import EntityAuthorizationsAuthorizingEntityIdentifier
  from ..models.entity_authorizations_authorized_entity_identifier import EntityAuthorizationsAuthorizedEntityIdentifier





T = TypeVar("T", bound="EntityAuthorizationPermissionsQueryRequest")



@_attrs_define
class EntityAuthorizationPermissionsQueryRequest:
    """ 
        Attributes:
            query_type (QueryType):
            authorizing_identifier (Union['EntityAuthorizationsAuthorizingEntityIdentifier', None, Unset]): Identyfikator
                podmiotu uprawniającego.
                | Type | Value |
                | --- | --- |
                | Nip | 10 cyfrowy numer NIP |
            authorized_identifier (Union['EntityAuthorizationsAuthorizedEntityIdentifier', None, Unset]): Identyfikator
                podmiotu uprawnionego.
                | Type | Value |
                | --- | --- |
                | Nip | 10 cyfrowy numer NIP |
                | PeppolId | Identyfikator dostawcy usług Peppol |
            permission_types (Union[None, Unset, list[InvoicePermissionType]]): Lista rodzajów wyszukiwanych uprawnień.
     """

    query_type: QueryType
    authorizing_identifier: Union['EntityAuthorizationsAuthorizingEntityIdentifier', None, Unset] = UNSET
    authorized_identifier: Union['EntityAuthorizationsAuthorizedEntityIdentifier', None, Unset] = UNSET
    permission_types: Union[None, Unset, list[InvoicePermissionType]] = UNSET





    def to_dict(self) -> dict[str, Any]:
        from ..models.entity_authorizations_authorizing_entity_identifier import EntityAuthorizationsAuthorizingEntityIdentifier
        from ..models.entity_authorizations_authorized_entity_identifier import EntityAuthorizationsAuthorizedEntityIdentifier
        query_type = self.query_type.value

        authorizing_identifier: Union[None, Unset, dict[str, Any]]
        if isinstance(self.authorizing_identifier, Unset):
            authorizing_identifier = UNSET
        elif isinstance(self.authorizing_identifier, EntityAuthorizationsAuthorizingEntityIdentifier):
            authorizing_identifier = self.authorizing_identifier.to_dict()
        else:
            authorizing_identifier = self.authorizing_identifier

        authorized_identifier: Union[None, Unset, dict[str, Any]]
        if isinstance(self.authorized_identifier, Unset):
            authorized_identifier = UNSET
        elif isinstance(self.authorized_identifier, EntityAuthorizationsAuthorizedEntityIdentifier):
            authorized_identifier = self.authorized_identifier.to_dict()
        else:
            authorized_identifier = self.authorized_identifier

        permission_types: Union[None, Unset, list[str]]
        if isinstance(self.permission_types, Unset):
            permission_types = UNSET
        elif isinstance(self.permission_types, list):
            permission_types = []
            for permission_types_type_0_item_data in self.permission_types:
                permission_types_type_0_item = permission_types_type_0_item_data.value
                permission_types.append(permission_types_type_0_item)


        else:
            permission_types = self.permission_types


        field_dict: dict[str, Any] = {}

        field_dict.update({
            "queryType": query_type,
        })
        if authorizing_identifier is not UNSET:
            field_dict["authorizingIdentifier"] = authorizing_identifier
        if authorized_identifier is not UNSET:
            field_dict["authorizedIdentifier"] = authorized_identifier
        if permission_types is not UNSET:
            field_dict["permissionTypes"] = permission_types

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.entity_authorizations_authorizing_entity_identifier import EntityAuthorizationsAuthorizingEntityIdentifier
        from ..models.entity_authorizations_authorized_entity_identifier import EntityAuthorizationsAuthorizedEntityIdentifier
        d = dict(src_dict)
        query_type = QueryType(d.pop("queryType"))




        def _parse_authorizing_identifier(data: object) -> Union['EntityAuthorizationsAuthorizingEntityIdentifier', None, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                authorizing_identifier_type_1 = EntityAuthorizationsAuthorizingEntityIdentifier.from_dict(data)



                return authorizing_identifier_type_1
            except: # noqa: E722
                pass
            return cast(Union['EntityAuthorizationsAuthorizingEntityIdentifier', None, Unset], data)

        authorizing_identifier = _parse_authorizing_identifier(d.pop("authorizingIdentifier", UNSET))


        def _parse_authorized_identifier(data: object) -> Union['EntityAuthorizationsAuthorizedEntityIdentifier', None, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                authorized_identifier_type_1 = EntityAuthorizationsAuthorizedEntityIdentifier.from_dict(data)



                return authorized_identifier_type_1
            except: # noqa: E722
                pass
            return cast(Union['EntityAuthorizationsAuthorizedEntityIdentifier', None, Unset], data)

        authorized_identifier = _parse_authorized_identifier(d.pop("authorizedIdentifier", UNSET))


        def _parse_permission_types(data: object) -> Union[None, Unset, list[InvoicePermissionType]]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                permission_types_type_0 = []
                _permission_types_type_0 = data
                for permission_types_type_0_item_data in (_permission_types_type_0):
                    permission_types_type_0_item = InvoicePermissionType(permission_types_type_0_item_data)



                    permission_types_type_0.append(permission_types_type_0_item)

                return permission_types_type_0
            except: # noqa: E722
                pass
            return cast(Union[None, Unset, list[InvoicePermissionType]], data)

        permission_types = _parse_permission_types(d.pop("permissionTypes", UNSET))


        entity_authorization_permissions_query_request = cls(
            query_type=query_type,
            authorizing_identifier=authorizing_identifier,
            authorized_identifier=authorized_identifier,
            permission_types=permission_types,
        )

        return entity_authorization_permissions_query_request

