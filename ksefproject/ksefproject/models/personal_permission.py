from collections.abc import Mapping
from typing import Any, TypeVar, Optional, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.permission_state import PermissionState
from ..models.personal_permission_scope import PersonalPermissionScope
from ..types import UNSET, Unset
from dateutil.parser import isoparse
from typing import cast
from typing import cast, Union
from typing import Union
import datetime

if TYPE_CHECKING:
  from ..models.permissions_subject_entity_details import PermissionsSubjectEntityDetails
  from ..models.personal_permissions_target_identifier import PersonalPermissionsTargetIdentifier
  from ..models.personal_permissions_context_identifier import PersonalPermissionsContextIdentifier
  from ..models.permissions_subject_person_details import PermissionsSubjectPersonDetails
  from ..models.personal_permissions_authorized_identifier import PersonalPermissionsAuthorizedIdentifier





T = TypeVar("T", bound="PersonalPermission")



@_attrs_define
class PersonalPermission:
    """ 
        Attributes:
            id (str): Techniczny identyfikator nadanego uprawnienia – wymagany m.in. przy operacjach odbierania.
            permission_scope (PersonalPermissionScope):
            description (str): Opis uprawnienia.
            permission_state (PermissionState):
            start_date (datetime.datetime): Data rozpoczęcia obowiązywania uprawnienia.
            can_delegate (bool): Flaga określająca, czy uprawnienie ma być możliwe do dalszego przekazywania.
            context_identifier (Union['PersonalPermissionsContextIdentifier', None, Unset]): Identyfikator kontekstu
                podmiotu, który nadał uprawnienia do obsługi faktur.
                | Type | Value |
                | --- | --- |
                | Nip | 10 cyfrowy numer NIP |
                | InternalId | Dwuczłonowy identyfikator składający się z numeru NIP i 5 cyfr: `{nip}-{5_cyfr}` |
            authorized_identifier (Union['PersonalPermissionsAuthorizedIdentifier', None, Unset]): Identyfikator podmiotu
                uprawnionego, jeżeli jest inny niż identyfikator uwierzytelnionego klienta API.
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
            subject_person_details (Union['PermissionsSubjectPersonDetails', None, Unset]): Dane osoby uprawnionej.
            subject_entity_details (Union['PermissionsSubjectEntityDetails', None, Unset]): Dane podmiotu uprawnionego.
     """

    id: str
    permission_scope: PersonalPermissionScope
    description: str
    permission_state: PermissionState
    start_date: datetime.datetime
    can_delegate: bool
    context_identifier: Union['PersonalPermissionsContextIdentifier', None, Unset] = UNSET
    authorized_identifier: Union['PersonalPermissionsAuthorizedIdentifier', None, Unset] = UNSET
    target_identifier: Union['PersonalPermissionsTargetIdentifier', None, Unset] = UNSET
    subject_person_details: Union['PermissionsSubjectPersonDetails', None, Unset] = UNSET
    subject_entity_details: Union['PermissionsSubjectEntityDetails', None, Unset] = UNSET





    def to_dict(self) -> dict[str, Any]:
        from ..models.permissions_subject_entity_details import PermissionsSubjectEntityDetails
        from ..models.personal_permissions_target_identifier import PersonalPermissionsTargetIdentifier
        from ..models.personal_permissions_context_identifier import PersonalPermissionsContextIdentifier
        from ..models.permissions_subject_person_details import PermissionsSubjectPersonDetails
        from ..models.personal_permissions_authorized_identifier import PersonalPermissionsAuthorizedIdentifier
        id = self.id

        permission_scope = self.permission_scope.value

        description = self.description

        permission_state = self.permission_state.value

        start_date = self.start_date.isoformat()

        can_delegate = self.can_delegate

        context_identifier: Union[None, Unset, dict[str, Any]]
        if isinstance(self.context_identifier, Unset):
            context_identifier = UNSET
        elif isinstance(self.context_identifier, PersonalPermissionsContextIdentifier):
            context_identifier = self.context_identifier.to_dict()
        else:
            context_identifier = self.context_identifier

        authorized_identifier: Union[None, Unset, dict[str, Any]]
        if isinstance(self.authorized_identifier, Unset):
            authorized_identifier = UNSET
        elif isinstance(self.authorized_identifier, PersonalPermissionsAuthorizedIdentifier):
            authorized_identifier = self.authorized_identifier.to_dict()
        else:
            authorized_identifier = self.authorized_identifier

        target_identifier: Union[None, Unset, dict[str, Any]]
        if isinstance(self.target_identifier, Unset):
            target_identifier = UNSET
        elif isinstance(self.target_identifier, PersonalPermissionsTargetIdentifier):
            target_identifier = self.target_identifier.to_dict()
        else:
            target_identifier = self.target_identifier

        subject_person_details: Union[None, Unset, dict[str, Any]]
        if isinstance(self.subject_person_details, Unset):
            subject_person_details = UNSET
        elif isinstance(self.subject_person_details, PermissionsSubjectPersonDetails):
            subject_person_details = self.subject_person_details.to_dict()
        else:
            subject_person_details = self.subject_person_details

        subject_entity_details: Union[None, Unset, dict[str, Any]]
        if isinstance(self.subject_entity_details, Unset):
            subject_entity_details = UNSET
        elif isinstance(self.subject_entity_details, PermissionsSubjectEntityDetails):
            subject_entity_details = self.subject_entity_details.to_dict()
        else:
            subject_entity_details = self.subject_entity_details


        field_dict: dict[str, Any] = {}

        field_dict.update({
            "id": id,
            "permissionScope": permission_scope,
            "description": description,
            "permissionState": permission_state,
            "startDate": start_date,
            "canDelegate": can_delegate,
        })
        if context_identifier is not UNSET:
            field_dict["contextIdentifier"] = context_identifier
        if authorized_identifier is not UNSET:
            field_dict["authorizedIdentifier"] = authorized_identifier
        if target_identifier is not UNSET:
            field_dict["targetIdentifier"] = target_identifier
        if subject_person_details is not UNSET:
            field_dict["subjectPersonDetails"] = subject_person_details
        if subject_entity_details is not UNSET:
            field_dict["subjectEntityDetails"] = subject_entity_details

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.permissions_subject_entity_details import PermissionsSubjectEntityDetails
        from ..models.personal_permissions_target_identifier import PersonalPermissionsTargetIdentifier
        from ..models.personal_permissions_context_identifier import PersonalPermissionsContextIdentifier
        from ..models.permissions_subject_person_details import PermissionsSubjectPersonDetails
        from ..models.personal_permissions_authorized_identifier import PersonalPermissionsAuthorizedIdentifier
        d = dict(src_dict)
        id = d.pop("id")

        permission_scope = PersonalPermissionScope(d.pop("permissionScope"))




        description = d.pop("description")

        permission_state = PermissionState(d.pop("permissionState"))




        start_date = isoparse(d.pop("startDate"))




        can_delegate = d.pop("canDelegate")

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


        def _parse_authorized_identifier(data: object) -> Union['PersonalPermissionsAuthorizedIdentifier', None, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                authorized_identifier_type_1 = PersonalPermissionsAuthorizedIdentifier.from_dict(data)



                return authorized_identifier_type_1
            except: # noqa: E722
                pass
            return cast(Union['PersonalPermissionsAuthorizedIdentifier', None, Unset], data)

        authorized_identifier = _parse_authorized_identifier(d.pop("authorizedIdentifier", UNSET))


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


        def _parse_subject_person_details(data: object) -> Union['PermissionsSubjectPersonDetails', None, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                subject_person_details_type_1 = PermissionsSubjectPersonDetails.from_dict(data)



                return subject_person_details_type_1
            except: # noqa: E722
                pass
            return cast(Union['PermissionsSubjectPersonDetails', None, Unset], data)

        subject_person_details = _parse_subject_person_details(d.pop("subjectPersonDetails", UNSET))


        def _parse_subject_entity_details(data: object) -> Union['PermissionsSubjectEntityDetails', None, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                subject_entity_details_type_1 = PermissionsSubjectEntityDetails.from_dict(data)



                return subject_entity_details_type_1
            except: # noqa: E722
                pass
            return cast(Union['PermissionsSubjectEntityDetails', None, Unset], data)

        subject_entity_details = _parse_subject_entity_details(d.pop("subjectEntityDetails", UNSET))


        personal_permission = cls(
            id=id,
            permission_scope=permission_scope,
            description=description,
            permission_state=permission_state,
            start_date=start_date,
            can_delegate=can_delegate,
            context_identifier=context_identifier,
            authorized_identifier=authorized_identifier,
            target_identifier=target_identifier,
            subject_person_details=subject_person_details,
            subject_entity_details=subject_entity_details,
        )

        return personal_permission

