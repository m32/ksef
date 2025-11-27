from collections.abc import Mapping
from typing import Any, TypeVar, Optional, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.person_permission_type import PersonPermissionType
from typing import cast

if TYPE_CHECKING:
  from ..models.person_permissions_subject_identifier import PersonPermissionsSubjectIdentifier





T = TypeVar("T", bound="PersonPermissionsGrantRequest")



@_attrs_define
class PersonPermissionsGrantRequest:
    """ 
        Attributes:
            subject_identifier (PersonPermissionsSubjectIdentifier): Identyfikator osoby fizycznej.
                | Type | Value |
                | --- | --- |
                | Nip | 10 cyfrowy numer NIP |
                | Pesel | 11 cyfrowy numer PESEL |
                | Fingerprint | Odcisk palca certyfikatu |
            permissions (list[PersonPermissionType]): Lista nadawanych uprawnień. Każda wartość może wystąpić tylko raz.
            description (str): Opis uprawnienia
     """

    subject_identifier: 'PersonPermissionsSubjectIdentifier'
    permissions: list[PersonPermissionType]
    description: str





    def to_dict(self) -> dict[str, Any]:
        from ..models.person_permissions_subject_identifier import PersonPermissionsSubjectIdentifier
        subject_identifier = self.subject_identifier.to_dict()

        permissions = []
        for permissions_item_data in self.permissions:
            permissions_item = permissions_item_data.value
            permissions.append(permissions_item)



        description = self.description


        field_dict: dict[str, Any] = {}

        field_dict.update({
            "subjectIdentifier": subject_identifier,
            "permissions": permissions,
            "description": description,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.person_permissions_subject_identifier import PersonPermissionsSubjectIdentifier
        d = dict(src_dict)
        subject_identifier = PersonPermissionsSubjectIdentifier.from_dict(d.pop("subjectIdentifier"))




        permissions = []
        _permissions = d.pop("permissions")
        for permissions_item_data in (_permissions):
            permissions_item = PersonPermissionType(permissions_item_data)



            permissions.append(permissions_item)


        description = d.pop("description")

        person_permissions_grant_request = cls(
            subject_identifier=subject_identifier,
            permissions=permissions,
            description=description,
        )

        return person_permissions_grant_request

