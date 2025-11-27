from collections.abc import Mapping
from typing import Any, TypeVar, Optional, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from typing import cast

if TYPE_CHECKING:
  from ..models.entity_permission import EntityPermission
  from ..models.entity_permissions_subject_identifier import EntityPermissionsSubjectIdentifier





T = TypeVar("T", bound="EntityPermissionsGrantRequest")



@_attrs_define
class EntityPermissionsGrantRequest:
    """ 
        Attributes:
            subject_identifier (EntityPermissionsSubjectIdentifier): Identyfikator podmiotu.
                | Type | Value |
                | --- | --- |
                | Nip | 10 cyfrowy numer NIP |
            permissions (list['EntityPermission']): Lista nadawanych uprawnień. Każda wartość może wystąpić tylko raz.
            description (str): Opis uprawnienia
     """

    subject_identifier: 'EntityPermissionsSubjectIdentifier'
    permissions: list['EntityPermission']
    description: str





    def to_dict(self) -> dict[str, Any]:
        from ..models.entity_permission import EntityPermission
        from ..models.entity_permissions_subject_identifier import EntityPermissionsSubjectIdentifier
        subject_identifier = self.subject_identifier.to_dict()

        permissions = []
        for permissions_item_data in self.permissions:
            permissions_item = permissions_item_data.to_dict()
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
        from ..models.entity_permission import EntityPermission
        from ..models.entity_permissions_subject_identifier import EntityPermissionsSubjectIdentifier
        d = dict(src_dict)
        subject_identifier = EntityPermissionsSubjectIdentifier.from_dict(d.pop("subjectIdentifier"))




        permissions = []
        _permissions = d.pop("permissions")
        for permissions_item_data in (_permissions):
            permissions_item = EntityPermission.from_dict(permissions_item_data)



            permissions.append(permissions_item)


        description = d.pop("description")

        entity_permissions_grant_request = cls(
            subject_identifier=subject_identifier,
            permissions=permissions,
            description=description,
        )

        return entity_permissions_grant_request

