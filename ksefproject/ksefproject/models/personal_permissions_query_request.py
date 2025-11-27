from collections.abc import Mapping
from typing import Any, TypeVar, Optional, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.permission_state import PermissionState
from ..models.personal_permission_type import PersonalPermissionType
from ..types import UNSET, Unset
from typing import cast
from typing import cast, Union
from typing import Union

if TYPE_CHECKING:
  from ..models.personal_permissions_context_identifier import PersonalPermissionsContextIdentifier
  from ..models.personal_permissions_target_identifier import PersonalPermissionsTargetIdentifier





T = TypeVar("T", bound="PersonalPermissionsQueryRequest")



@_attrs_define
class PersonalPermissionsQueryRequest:
    """ 
        Attributes:
            context_identifier (Union['PersonalPermissionsContextIdentifier', None, Unset]): Identyfikator kontekstu
                podmiotu, który nadał uprawnienia do obsługi faktur.
                | Type | Value |
                | --- | --- |
                | Nip | 10 cyfrowy numer NIP |
            target_identifier (Union['PersonalPermissionsTargetIdentifier', None, Unset]): Identyfikator podmiotu docelowego
                dla uprawnień selektywnych nadanych pośrednio.
                | Type | Value |
                | --- | --- |
                | Nip | 10 cyfrowy numer NIP |
                | AllPartners | Identyfikator oznaczający, że wyszukiwanie dotyczy uprawnień generalnych nadanych w sposób
                pośredni |
                | InternalId | Dwuczłonowy identyfikator składający się z numeru NIP i 5 cyfr: `{nip}-{5_cyfr}` |
            permission_types (Union[None, Unset, list[PersonalPermissionType]]): Lista rodzajów wyszukiwanych uprawnień.
            permission_state (Union[None, PermissionState, Unset]): Stan uprawnienia.
                | Type | Value |
                | --- | --- |
                | Active | Uprawnienia aktywne |
                | Inactive | Uprawnienia nieaktywne |
     """

    context_identifier: Union['PersonalPermissionsContextIdentifier', None, Unset] = UNSET
    target_identifier: Union['PersonalPermissionsTargetIdentifier', None, Unset] = UNSET
    permission_types: Union[None, Unset, list[PersonalPermissionType]] = UNSET
    permission_state: Union[None, PermissionState, Unset] = UNSET





    def to_dict(self) -> dict[str, Any]:
        from ..models.personal_permissions_context_identifier import PersonalPermissionsContextIdentifier
        from ..models.personal_permissions_target_identifier import PersonalPermissionsTargetIdentifier
        context_identifier: Union[None, Unset, dict[str, Any]]
        if isinstance(self.context_identifier, Unset):
            context_identifier = UNSET
        elif isinstance(self.context_identifier, PersonalPermissionsContextIdentifier):
            context_identifier = self.context_identifier.to_dict()
        else:
            context_identifier = self.context_identifier

        target_identifier: Union[None, Unset, dict[str, Any]]
        if isinstance(self.target_identifier, Unset):
            target_identifier = UNSET
        elif isinstance(self.target_identifier, PersonalPermissionsTargetIdentifier):
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
        })
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
        from ..models.personal_permissions_context_identifier import PersonalPermissionsContextIdentifier
        from ..models.personal_permissions_target_identifier import PersonalPermissionsTargetIdentifier
        d = dict(src_dict)
        def _parse_context_identifier(data: object) -> Union['PersonalPermissionsContextIdentifier', None, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                context_identifier_type_1 = PersonalPermissionsContextIdentifier.from_dict(data)



                return context_identifier_type_1
            except: # noqa: E722
                pass
            return cast(Union['PersonalPermissionsContextIdentifier', None, Unset], data)

        context_identifier = _parse_context_identifier(d.pop("contextIdentifier", UNSET))


        def _parse_target_identifier(data: object) -> Union['PersonalPermissionsTargetIdentifier', None, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                target_identifier_type_1 = PersonalPermissionsTargetIdentifier.from_dict(data)



                return target_identifier_type_1
            except: # noqa: E722
                pass
            return cast(Union['PersonalPermissionsTargetIdentifier', None, Unset], data)

        target_identifier = _parse_target_identifier(d.pop("targetIdentifier", UNSET))


        def _parse_permission_types(data: object) -> Union[None, Unset, list[PersonalPermissionType]]:
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
                    permission_types_type_0_item = PersonalPermissionType(permission_types_type_0_item_data)



                    permission_types_type_0.append(permission_types_type_0_item)

                return permission_types_type_0
            except: # noqa: E722
                pass
            return cast(Union[None, Unset, list[PersonalPermissionType]], data)

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


        personal_permissions_query_request = cls(
            context_identifier=context_identifier,
            target_identifier=target_identifier,
            permission_types=permission_types,
            permission_state=permission_state,
        )

        return personal_permissions_query_request

