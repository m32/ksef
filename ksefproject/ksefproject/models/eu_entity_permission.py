from collections.abc import Mapping
from typing import Any, TypeVar, Optional, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.eu_entity_permissions_query_permission_type import EuEntityPermissionsQueryPermissionType
from dateutil.parser import isoparse
from typing import cast
import datetime

if TYPE_CHECKING:
  from ..models.eu_entity_permissions_author_identifier import EuEntityPermissionsAuthorIdentifier





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
     """

    id: str
    author_identifier: 'EuEntityPermissionsAuthorIdentifier'
    vat_ue_identifier: str
    eu_entity_name: str
    authorized_fingerprint_identifier: str
    permission_scope: EuEntityPermissionsQueryPermissionType
    description: str
    start_date: datetime.datetime





    def to_dict(self) -> dict[str, Any]:
        from ..models.eu_entity_permissions_author_identifier import EuEntityPermissionsAuthorIdentifier
        id = self.id

        author_identifier = self.author_identifier.to_dict()

        vat_ue_identifier = self.vat_ue_identifier

        eu_entity_name = self.eu_entity_name

        authorized_fingerprint_identifier = self.authorized_fingerprint_identifier

        permission_scope = self.permission_scope.value

        description = self.description

        start_date = self.start_date.isoformat()


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

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.eu_entity_permissions_author_identifier import EuEntityPermissionsAuthorIdentifier
        d = dict(src_dict)
        id = d.pop("id")

        author_identifier = EuEntityPermissionsAuthorIdentifier.from_dict(d.pop("authorIdentifier"))




        vat_ue_identifier = d.pop("vatUeIdentifier")

        eu_entity_name = d.pop("euEntityName")

        authorized_fingerprint_identifier = d.pop("authorizedFingerprintIdentifier")

        permission_scope = EuEntityPermissionsQueryPermissionType(d.pop("permissionScope"))




        description = d.pop("description")

        start_date = isoparse(d.pop("startDate"))




        eu_entity_permission = cls(
            id=id,
            author_identifier=author_identifier,
            vat_ue_identifier=vat_ue_identifier,
            eu_entity_name=eu_entity_name,
            authorized_fingerprint_identifier=authorized_fingerprint_identifier,
            permission_scope=permission_scope,
            description=description,
            start_date=start_date,
        )

        return eu_entity_permission

