from collections.abc import Mapping
from typing import Any, TypeVar, Optional, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.eu_entity_permissions_query_permission_type import EuEntityPermissionsQueryPermissionType
from ..types import UNSET, Unset
from dateutil.parser import isoparse
from typing import cast
from typing import cast, Union
from typing import Union
import datetime

if TYPE_CHECKING:
  from ..models.permissions_subject_person_by_fingerprint_details import PermissionsSubjectPersonByFingerprintDetails
  from ..models.eu_entity_permissions_author_identifier import EuEntityPermissionsAuthorIdentifier
  from ..models.permissions_eu_entity_details import PermissionsEuEntityDetails
  from ..models.permissions_subject_entity_by_fingerprint_details import PermissionsSubjectEntityByFingerprintDetails





T = TypeVar("T", bound="EuEntityPermission")



@_attrs_define
class EuEntityPermission:
    """ 
        Attributes:
            id (str): Techniczny identyfikator nadanego uprawnienia – wymagany m.in. przy operacjach odbierania.
            author_identifier (EuEntityPermissionsAuthorIdentifier): Identyfikator uprawniającego.
                | Type | Value |
                | --- | --- |
                | Nip | 10 cyfrowy numer NIP |
                | Pesel | 11 cyfrowy numer PESEL |
                | Fingerprint | Odcisk palca certyfikatu |
            vat_ue_identifier (str): Identyfikator podmiotu unijnego.
            eu_entity_name (str): Nazwa podmiotu unijnego.
            authorized_fingerprint_identifier (str): Uprawniony odcisk palca certyfikatu.
            permission_scope (EuEntityPermissionsQueryPermissionType):
            description (str): Opis uprawnienia.
            start_date (datetime.datetime): Data rozpoczęcia obowiązywania uprawnienia.
            subject_person_details (Union['PermissionsSubjectPersonByFingerprintDetails', None, Unset]): Dane osoby
                uprawnionej.
            subject_entity_details (Union['PermissionsSubjectEntityByFingerprintDetails', None, Unset]): Dane podmiotu
                uprawnionego.
            eu_entity_details (Union['PermissionsEuEntityDetails', None, Unset]): Dane podmiotu unijnego, w kontekście
                którego nadane jest uprawnienie.
     """

    id: str
    author_identifier: 'EuEntityPermissionsAuthorIdentifier'
    vat_ue_identifier: str
    eu_entity_name: str
    authorized_fingerprint_identifier: str
    permission_scope: EuEntityPermissionsQueryPermissionType
    description: str
    start_date: datetime.datetime
    subject_person_details: Union['PermissionsSubjectPersonByFingerprintDetails', None, Unset] = UNSET
    subject_entity_details: Union['PermissionsSubjectEntityByFingerprintDetails', None, Unset] = UNSET
    eu_entity_details: Union['PermissionsEuEntityDetails', None, Unset] = UNSET





    def to_dict(self) -> dict[str, Any]:
        from ..models.permissions_subject_person_by_fingerprint_details import PermissionsSubjectPersonByFingerprintDetails
        from ..models.eu_entity_permissions_author_identifier import EuEntityPermissionsAuthorIdentifier
        from ..models.permissions_eu_entity_details import PermissionsEuEntityDetails
        from ..models.permissions_subject_entity_by_fingerprint_details import PermissionsSubjectEntityByFingerprintDetails
        id = self.id

        author_identifier = self.author_identifier.to_dict()

        vat_ue_identifier = self.vat_ue_identifier

        eu_entity_name = self.eu_entity_name

        authorized_fingerprint_identifier = self.authorized_fingerprint_identifier

        permission_scope = self.permission_scope.value

        description = self.description

        start_date = self.start_date.isoformat()

        subject_person_details: Union[None, Unset, dict[str, Any]]
        if isinstance(self.subject_person_details, Unset):
            subject_person_details = UNSET
        elif isinstance(self.subject_person_details, PermissionsSubjectPersonByFingerprintDetails):
            subject_person_details = self.subject_person_details.to_dict()
        else:
            subject_person_details = self.subject_person_details

        subject_entity_details: Union[None, Unset, dict[str, Any]]
        if isinstance(self.subject_entity_details, Unset):
            subject_entity_details = UNSET
        elif isinstance(self.subject_entity_details, PermissionsSubjectEntityByFingerprintDetails):
            subject_entity_details = self.subject_entity_details.to_dict()
        else:
            subject_entity_details = self.subject_entity_details

        eu_entity_details: Union[None, Unset, dict[str, Any]]
        if isinstance(self.eu_entity_details, Unset):
            eu_entity_details = UNSET
        elif isinstance(self.eu_entity_details, PermissionsEuEntityDetails):
            eu_entity_details = self.eu_entity_details.to_dict()
        else:
            eu_entity_details = self.eu_entity_details


        field_dict: dict[str, Any] = {}

        field_dict.update({
            "id": id,
            "authorIdentifier": author_identifier,
            "vatUeIdentifier": vat_ue_identifier,
            "euEntityName": eu_entity_name,
            "authorizedFingerprintIdentifier": authorized_fingerprint_identifier,
            "permissionScope": permission_scope,
            "description": description,
            "startDate": start_date,
        })
        if subject_person_details is not UNSET:
            field_dict["subjectPersonDetails"] = subject_person_details
        if subject_entity_details is not UNSET:
            field_dict["subjectEntityDetails"] = subject_entity_details
        if eu_entity_details is not UNSET:
            field_dict["euEntityDetails"] = eu_entity_details

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.permissions_subject_person_by_fingerprint_details import PermissionsSubjectPersonByFingerprintDetails
        from ..models.eu_entity_permissions_author_identifier import EuEntityPermissionsAuthorIdentifier
        from ..models.permissions_eu_entity_details import PermissionsEuEntityDetails
        from ..models.permissions_subject_entity_by_fingerprint_details import PermissionsSubjectEntityByFingerprintDetails
        d = dict(src_dict)
        id = d.pop("id")

        author_identifier = EuEntityPermissionsAuthorIdentifier.from_dict(d.pop("authorIdentifier"))




        vat_ue_identifier = d.pop("vatUeIdentifier")

        eu_entity_name = d.pop("euEntityName")

        authorized_fingerprint_identifier = d.pop("authorizedFingerprintIdentifier")

        permission_scope = EuEntityPermissionsQueryPermissionType(d.pop("permissionScope"))




        description = d.pop("description")

        start_date = isoparse(d.pop("startDate"))




        def _parse_subject_person_details(data: object) -> Union['PermissionsSubjectPersonByFingerprintDetails', None, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                subject_person_details_type_1 = PermissionsSubjectPersonByFingerprintDetails.from_dict(data)



                return subject_person_details_type_1
            except: # noqa: E722
                pass
            return cast(Union['PermissionsSubjectPersonByFingerprintDetails', None, Unset], data)

        subject_person_details = _parse_subject_person_details(d.pop("subjectPersonDetails", UNSET))


        def _parse_subject_entity_details(data: object) -> Union['PermissionsSubjectEntityByFingerprintDetails', None, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                subject_entity_details_type_1 = PermissionsSubjectEntityByFingerprintDetails.from_dict(data)



                return subject_entity_details_type_1
            except: # noqa: E722
                pass
            return cast(Union['PermissionsSubjectEntityByFingerprintDetails', None, Unset], data)

        subject_entity_details = _parse_subject_entity_details(d.pop("subjectEntityDetails", UNSET))


        def _parse_eu_entity_details(data: object) -> Union['PermissionsEuEntityDetails', None, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                eu_entity_details_type_1 = PermissionsEuEntityDetails.from_dict(data)



                return eu_entity_details_type_1
            except: # noqa: E722
                pass
            return cast(Union['PermissionsEuEntityDetails', None, Unset], data)

        eu_entity_details = _parse_eu_entity_details(d.pop("euEntityDetails", UNSET))


        eu_entity_permission = cls(
            id=id,
            author_identifier=author_identifier,
            vat_ue_identifier=vat_ue_identifier,
            eu_entity_name=eu_entity_name,
            authorized_fingerprint_identifier=authorized_fingerprint_identifier,
            permission_scope=permission_scope,
            description=description,
            start_date=start_date,
            subject_person_details=subject_person_details,
            subject_entity_details=subject_entity_details,
            eu_entity_details=eu_entity_details,
        )

        return eu_entity_permission

