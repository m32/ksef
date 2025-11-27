from collections.abc import Mapping
from typing import Any, TypeVar, Optional, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.permission_state import PermissionState
from ..models.person_permission_type import PersonPermissionType
from ..models.person_permissions_query_type import PersonPermissionsQueryType
from ..types import UNSET, Unset
from typing import cast
from typing import cast, Union
from typing import Union

if TYPE_CHECKING:
  from ..models.person_permissions_authorized_identifier import PersonPermissionsAuthorizedIdentifier
  from ..models.person_permissions_target_identifier import PersonPermissionsTargetIdentifier
  from ..models.person_permissions_context_identifier import PersonPermissionsContextIdentifier
  from ..models.person_permissions_author_identifier import PersonPermissionsAuthorIdentifier





T = TypeVar("T", bound="PersonPermissionsQueryRequest")



@_attrs_define
class PersonPermissionsQueryRequest:
    """ 
        Attributes:
            query_type (PersonPermissionsQueryType):
            author_identifier (Union['PersonPermissionsAuthorIdentifier', None, Unset]): Identyfikator osoby lub podmiotu
                nadającego uprawnienie.
                | Type | Value |
                | --- | --- |
                | Nip | 10 cyfrowy numer NIP |
                | Pesel | 11 cyfrowy numer PESEL |
                | Fingerprint | Odcisk palca certyfikatu |
                | System | Identyfikator systemowy KSeF |
            authorized_identifier (Union['PersonPermissionsAuthorizedIdentifier', None, Unset]): Identyfikator osoby lub
                podmiotu uprawnionego.
                | Type | Value |
                | --- | --- |
                | Nip | 10 cyfrowy numer NIP |
                | Pesel | 11 cyfrowy numer PESEL |
                | Fingerprint | Odcisk palca certyfikatu |
            context_identifier (Union['PersonPermissionsContextIdentifier', None, Unset]): Identyfikator kontekstu
                uprawnienia (dla uprawnień nadanych administratorom jednostek podrzędnych).
                | Type | Value |
                | --- | --- |
                | Nip | 10 cyfrowy numer NIP |
                | InternalId | Dwuczłonowy identyfikator składający się z numeru NIP i 5 cyfr: `{nip}-{5_cyfr}` |
            target_identifier (Union['PersonPermissionsTargetIdentifier', None, Unset]): Identyfikator podmiotu docelowego
                dla uprawnień nadanych pośrednio.
                | Type | Value |
                | --- | --- |
                | Nip | 10 cyfrowy numer NIP |
                | AllPartners | Identyfikator oznaczający, że uprawnienie nadane w sposób pośredni jest typu generalnego |
                | InternalId | Dwuczłonowy identyfikator składający się z numeru NIP i 5 cyfr: `{nip}-{5_cyfr}` |
            permission_types (Union[None, Unset, list[PersonPermissionType]]): Lista rodzajów wyszukiwanych uprawnień.
            permission_state (Union[None, PermissionState, Unset]): Stan uprawnienia.
                | Type | Value |
                | --- | --- |
                | Active | Uprawnienia aktywne |
                | Inactive | Uprawnienia nieaktywne, nadane w sposób poœredni |
     """

    query_type: PersonPermissionsQueryType
    author_identifier: Union['PersonPermissionsAuthorIdentifier', None, Unset] = UNSET
    authorized_identifier: Union['PersonPermissionsAuthorizedIdentifier', None, Unset] = UNSET
    context_identifier: Union['PersonPermissionsContextIdentifier', None, Unset] = UNSET
    target_identifier: Union['PersonPermissionsTargetIdentifier', None, Unset] = UNSET
    permission_types: Union[None, Unset, list[PersonPermissionType]] = UNSET
    permission_state: Union[None, PermissionState, Unset] = UNSET





    def to_dict(self) -> dict[str, Any]:
        from ..models.person_permissions_authorized_identifier import PersonPermissionsAuthorizedIdentifier
        from ..models.person_permissions_target_identifier import PersonPermissionsTargetIdentifier
        from ..models.person_permissions_context_identifier import PersonPermissionsContextIdentifier
        from ..models.person_permissions_author_identifier import PersonPermissionsAuthorIdentifier
        query_type = self.query_type.value

        author_identifier: Union[None, Unset, dict[str, Any]]
        if isinstance(self.author_identifier, Unset):
            author_identifier = UNSET
        elif isinstance(self.author_identifier, PersonPermissionsAuthorIdentifier):
            author_identifier = self.author_identifier.to_dict()
        else:
            author_identifier = self.author_identifier

        authorized_identifier: Union[None, Unset, dict[str, Any]]
        if isinstance(self.authorized_identifier, Unset):
            authorized_identifier = UNSET
        elif isinstance(self.authorized_identifier, PersonPermissionsAuthorizedIdentifier):
            authorized_identifier = self.authorized_identifier.to_dict()
        else:
            authorized_identifier = self.authorized_identifier

        context_identifier: Union[None, Unset, dict[str, Any]]
        if isinstance(self.context_identifier, Unset):
            context_identifier = UNSET
        elif isinstance(self.context_identifier, PersonPermissionsContextIdentifier):
            context_identifier = self.context_identifier.to_dict()
        else:
            context_identifier = self.context_identifier

        target_identifier: Union[None, Unset, dict[str, Any]]
        if isinstance(self.target_identifier, Unset):
            target_identifier = UNSET
        elif isinstance(self.target_identifier, PersonPermissionsTargetIdentifier):
            target_identifier = self.target_identifier.to_dict()
        else:
            target_identifier = self.target_identifier

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

        permission_state: Union[None, Unset, str]
        if isinstance(self.permission_state, Unset):
            permission_state = UNSET
        elif isinstance(self.permission_state, PermissionState):
            permission_state = self.permission_state.value
        else:
            permission_state = self.permission_state


        field_dict: dict[str, Any] = {}

        field_dict.update({
            "queryType": query_type,
        })
        if author_identifier is not UNSET:
            field_dict["authorIdentifier"] = author_identifier
        if authorized_identifier is not UNSET:
            field_dict["authorizedIdentifier"] = authorized_identifier
        if context_identifier is not UNSET:
            field_dict["contextIdentifier"] = context_identifier
        if target_identifier is not UNSET:
            field_dict["targetIdentifier"] = target_identifier
        if permission_types is not UNSET:
            field_dict["permissionTypes"] = permission_types
        if permission_state is not UNSET:
            field_dict["permissionState"] = permission_state

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.person_permissions_authorized_identifier import PersonPermissionsAuthorizedIdentifier
        from ..models.person_permissions_target_identifier import PersonPermissionsTargetIdentifier
        from ..models.person_permissions_context_identifier import PersonPermissionsContextIdentifier
        from ..models.person_permissions_author_identifier import PersonPermissionsAuthorIdentifier
        d = dict(src_dict)
        query_type = PersonPermissionsQueryType(d.pop("queryType"))




        def _parse_author_identifier(data: object) -> Union['PersonPermissionsAuthorIdentifier', None, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                author_identifier_type_1 = PersonPermissionsAuthorIdentifier.from_dict(data)



                return author_identifier_type_1
            except: # noqa: E722
                pass
            return cast(Union['PersonPermissionsAuthorIdentifier', None, Unset], data)

        author_identifier = _parse_author_identifier(d.pop("authorIdentifier", UNSET))


        def _parse_authorized_identifier(data: object) -> Union['PersonPermissionsAuthorizedIdentifier', None, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                authorized_identifier_type_1 = PersonPermissionsAuthorizedIdentifier.from_dict(data)



                return authorized_identifier_type_1
            except: # noqa: E722
                pass
            return cast(Union['PersonPermissionsAuthorizedIdentifier', None, Unset], data)

        authorized_identifier = _parse_authorized_identifier(d.pop("authorizedIdentifier", UNSET))


        def _parse_context_identifier(data: object) -> Union['PersonPermissionsContextIdentifier', None, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                context_identifier_type_1 = PersonPermissionsContextIdentifier.from_dict(data)



                return context_identifier_type_1
            except: # noqa: E722
                pass
            return cast(Union['PersonPermissionsContextIdentifier', None, Unset], data)

        context_identifier = _parse_context_identifier(d.pop("contextIdentifier", UNSET))


        def _parse_target_identifier(data: object) -> Union['PersonPermissionsTargetIdentifier', None, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                target_identifier_type_1 = PersonPermissionsTargetIdentifier.from_dict(data)



                return target_identifier_type_1
            except: # noqa: E722
                pass
            return cast(Union['PersonPermissionsTargetIdentifier', None, Unset], data)

        target_identifier = _parse_target_identifier(d.pop("targetIdentifier", UNSET))


        def _parse_permission_types(data: object) -> Union[None, Unset, list[PersonPermissionType]]:
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
                    permission_types_type_0_item = PersonPermissionType(permission_types_type_0_item_data)



                    permission_types_type_0.append(permission_types_type_0_item)

                return permission_types_type_0
            except: # noqa: E722
                pass
            return cast(Union[None, Unset, list[PersonPermissionType]], data)

        permission_types = _parse_permission_types(d.pop("permissionTypes", UNSET))


        def _parse_permission_state(data: object) -> Union[None, PermissionState, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                permission_state_type_1 = PermissionState(data)



                return permission_state_type_1
            except: # noqa: E722
                pass
            return cast(Union[None, PermissionState, Unset], data)

        permission_state = _parse_permission_state(d.pop("permissionState", UNSET))


        person_permissions_query_request = cls(
            query_type=query_type,
            author_identifier=author_identifier,
            authorized_identifier=authorized_identifier,
            context_identifier=context_identifier,
            target_identifier=target_identifier,
            permission_types=permission_types,
            permission_state=permission_state,
        )

        return person_permissions_query_request

