from collections.abc import Mapping
from typing import Any, TypeVar, Optional, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.permission_state import PermissionState
from ..models.person_permission_scope import PersonPermissionScope
from ..types import UNSET, Unset
from dateutil.parser import isoparse
from typing import cast
from typing import cast, Union
from typing import Union
import datetime

if TYPE_CHECKING:
  from ..models.person_permissions_authorized_identifier import PersonPermissionsAuthorizedIdentifier
  from ..models.person_permissions_target_identifier import PersonPermissionsTargetIdentifier
  from ..models.person_permissions_context_identifier import PersonPermissionsContextIdentifier
  from ..models.person_permissions_author_identifier import PersonPermissionsAuthorIdentifier





T = TypeVar("T", bound="PersonPermission")



@_attrs_define
class PersonPermission:
    """ 
        Attributes:
            id (str): Techniczny identyfikator nadanego uprawnienia – wymagany m.in. przy operacjach odbierania.
            authorized_identifier (PersonPermissionsAuthorizedIdentifier): Identyfikator osoby lub podmiotu uprawnionego.
                | Type | Value |
                | --- | --- |
                | Nip | 10 cyfrowy numer NIP |
                | Pesel | 11 cyfrowy numer PESEL |
                | Fingerprint | Odcisk palca certyfikatu |
            author_identifier (PersonPermissionsAuthorIdentifier): Identyfikator osoby lub podmiotu nadającego uprawnienie.
                | Type | Value |
                | --- | --- |
                | Nip | 10 cyfrowy numer NIP |
                | Pesel | 11 cyfrowy numer PESEL |
                | Fingerprint | Odcisk palca certyfikatu |
                | System | Identyfikator systemowy KSeF |
            permission_scope (PersonPermissionScope):
            description (str): Opis uprawnienia.
            permission_state (PermissionState):
            start_date (datetime.datetime): Data rozpoczęcia obowiązywania uprawnienia.
            can_delegate (bool): Flaga określająca, czy uprawnienie ma być możliwe do dalszego przekazywania.
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
     """

    id: str
    authorized_identifier: 'PersonPermissionsAuthorizedIdentifier'
    author_identifier: 'PersonPermissionsAuthorIdentifier'
    permission_scope: PersonPermissionScope
    description: str
    permission_state: PermissionState
    start_date: datetime.datetime
    can_delegate: bool
    context_identifier: Union['PersonPermissionsContextIdentifier', None, Unset] = UNSET
    target_identifier: Union['PersonPermissionsTargetIdentifier', None, Unset] = UNSET





    def to_dict(self) -> dict[str, Any]:
        from ..models.person_permissions_authorized_identifier import PersonPermissionsAuthorizedIdentifier
        from ..models.person_permissions_target_identifier import PersonPermissionsTargetIdentifier
        from ..models.person_permissions_context_identifier import PersonPermissionsContextIdentifier
        from ..models.person_permissions_author_identifier import PersonPermissionsAuthorIdentifier
        id = self.id

        authorized_identifier = self.authorized_identifier.to_dict()

        author_identifier = self.author_identifier.to_dict()

        permission_scope = self.permission_scope.value

        description = self.description

        permission_state = self.permission_state.value

        start_date = self.start_date.isoformat()

        can_delegate = self.can_delegate

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


        field_dict: dict[str, Any] = {}

        field_dict.update({
            "id": id,
            "authorizedIdentifier": authorized_identifier,
            "authorIdentifier": author_identifier,
            "permissionScope": permission_scope,
            "description": description,
            "permissionState": permission_state,
            "startDate": start_date,
            "canDelegate": can_delegate,
        })
        if context_identifier is not UNSET:
            field_dict["contextIdentifier"] = context_identifier
        if target_identifier is not UNSET:
            field_dict["targetIdentifier"] = target_identifier

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.person_permissions_authorized_identifier import PersonPermissionsAuthorizedIdentifier
        from ..models.person_permissions_target_identifier import PersonPermissionsTargetIdentifier
        from ..models.person_permissions_context_identifier import PersonPermissionsContextIdentifier
        from ..models.person_permissions_author_identifier import PersonPermissionsAuthorIdentifier
        d = dict(src_dict)
        id = d.pop("id")

        authorized_identifier = PersonPermissionsAuthorizedIdentifier.from_dict(d.pop("authorizedIdentifier"))




        author_identifier = PersonPermissionsAuthorIdentifier.from_dict(d.pop("authorIdentifier"))




        permission_scope = PersonPermissionScope(d.pop("permissionScope"))




        description = d.pop("description")

        permission_state = PermissionState(d.pop("permissionState"))




        start_date = isoparse(d.pop("startDate"))




        can_delegate = d.pop("canDelegate")

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


        person_permission = cls(
            id=id,
            authorized_identifier=authorized_identifier,
            author_identifier=author_identifier,
            permission_scope=permission_scope,
            description=description,
            permission_state=permission_state,
            start_date=start_date,
            can_delegate=can_delegate,
            context_identifier=context_identifier,
            target_identifier=target_identifier,
        )

        return person_permission

