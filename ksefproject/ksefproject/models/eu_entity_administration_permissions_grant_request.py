from collections.abc import Mapping
from typing import Any, TypeVar, Optional, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from typing import cast

if TYPE_CHECKING:
  from ..models.eu_entity_administration_permissions_subject_identifier import EuEntityAdministrationPermissionsSubjectIdentifier
  from ..models.eu_entity_administration_permissions_context_identifier import EuEntityAdministrationPermissionsContextIdentifier





T = TypeVar("T", bound="EuEntityAdministrationPermissionsGrantRequest")



@_attrs_define
class EuEntityAdministrationPermissionsGrantRequest:
    """ 
        Attributes:
            subject_identifier (EuEntityAdministrationPermissionsSubjectIdentifier): Identyfikator podmiotu uprawnionego.
                | Type | Value |
                | --- | --- |
                | Fingerprint | Odcisk palca certyfikatu |
            context_identifier (EuEntityAdministrationPermissionsContextIdentifier): Identyfikator kontekstu złożonego.
                | Type | Value |
                | --- | --- |
                | NipVatUe | Dwuczłonowy identyfikator składający się z numeru NIP i numeru VAT-UE: `{nip}-{vat_ue}` |
            description (str): Opis uprawnienia
            eu_entity_name (str): Nazwa i adres podmiotu unijnego w formacie:
                `{euSubjectName}, {euSubjectAddress}`
     """

    subject_identifier: 'EuEntityAdministrationPermissionsSubjectIdentifier'
    context_identifier: 'EuEntityAdministrationPermissionsContextIdentifier'
    description: str
    eu_entity_name: str





    def to_dict(self) -> dict[str, Any]:
        from ..models.eu_entity_administration_permissions_subject_identifier import EuEntityAdministrationPermissionsSubjectIdentifier
        from ..models.eu_entity_administration_permissions_context_identifier import EuEntityAdministrationPermissionsContextIdentifier
        subject_identifier = self.subject_identifier.to_dict()

        context_identifier = self.context_identifier.to_dict()

        description = self.description

        eu_entity_name = self.eu_entity_name


        field_dict: dict[str, Any] = {}

        field_dict.update({
            "subjectIdentifier": subject_identifier,
            "contextIdentifier": context_identifier,
            "description": description,
            "euEntityName": eu_entity_name,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.eu_entity_administration_permissions_subject_identifier import EuEntityAdministrationPermissionsSubjectIdentifier
        from ..models.eu_entity_administration_permissions_context_identifier import EuEntityAdministrationPermissionsContextIdentifier
        d = dict(src_dict)
        subject_identifier = EuEntityAdministrationPermissionsSubjectIdentifier.from_dict(d.pop("subjectIdentifier"))




        context_identifier = EuEntityAdministrationPermissionsContextIdentifier.from_dict(d.pop("contextIdentifier"))




        description = d.pop("description")

        eu_entity_name = d.pop("euEntityName")

        eu_entity_administration_permissions_grant_request = cls(
            subject_identifier=subject_identifier,
            context_identifier=context_identifier,
            description=description,
            eu_entity_name=eu_entity_name,
        )

        return eu_entity_administration_permissions_grant_request

