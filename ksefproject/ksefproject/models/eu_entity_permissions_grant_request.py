from collections.abc import Mapping
from typing import Any, TypeVar, Optional, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.eu_entity_permission_type import EuEntityPermissionType
from typing import cast

if TYPE_CHECKING:
  from ..models.eu_entity_permissions_subject_identifier import EuEntityPermissionsSubjectIdentifier





T = TypeVar("T", bound="EuEntityPermissionsGrantRequest")



@_attrs_define
class EuEntityPermissionsGrantRequest:
    """ 
        Attributes:
            subject_identifier (EuEntityPermissionsSubjectIdentifier): Identyfikator podmiotu uprawnianego.
                | Type | Value |
                | --- | --- |
                | Fingerprint | Odcisk palca certyfikatu |
            permissions (list[EuEntityPermissionType]): Lista nadawanych uprawnień. Każda wartość może wystąpić tylko raz.
            description (str): Opis uprawnienia
     """

    subject_identifier: 'EuEntityPermissionsSubjectIdentifier'
    permissions: list[EuEntityPermissionType]
    description: str





    def to_dict(self) -> dict[str, Any]:
        from ..models.eu_entity_permissions_subject_identifier import EuEntityPermissionsSubjectIdentifier
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
        from ..models.eu_entity_permissions_subject_identifier import EuEntityPermissionsSubjectIdentifier
        d = dict(src_dict)
        subject_identifier = EuEntityPermissionsSubjectIdentifier.from_dict(d.pop("subjectIdentifier"))




        permissions = []
        _permissions = d.pop("permissions")
        for permissions_item_data in (_permissions):
            permissions_item = EuEntityPermissionType(permissions_item_data)



            permissions.append(permissions_item)


        description = d.pop("description")

        eu_entity_permissions_grant_request = cls(
            subject_identifier=subject_identifier,
            permissions=permissions,
            description=description,
        )

        return eu_entity_permissions_grant_request

