from collections.abc import Mapping
from typing import Any, TypeVar, Optional, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.entity_authorization_permission_type import EntityAuthorizationPermissionType
from typing import cast

if TYPE_CHECKING:
  from ..models.entity_details import EntityDetails
  from ..models.entity_authorization_permissions_subject_identifier import EntityAuthorizationPermissionsSubjectIdentifier





T = TypeVar("T", bound="EntityAuthorizationPermissionsGrantRequest")



@_attrs_define
class EntityAuthorizationPermissionsGrantRequest:
    """ 
        Attributes:
            subject_identifier (EntityAuthorizationPermissionsSubjectIdentifier): Identyfikator podmiotu uprawnianego.
                | Type | Value |
                | --- | --- |
                | Nip | 10 cyfrowy numer NIP |
                | PeppolId | Identyfikator dostawcy usług Peppol |
            permission (EntityAuthorizationPermissionType):
            description (str): Opis uprawnienia
            subject_details (EntityDetails):
     """

    subject_identifier: 'EntityAuthorizationPermissionsSubjectIdentifier'
    permission: EntityAuthorizationPermissionType
    description: str
    subject_details: 'EntityDetails'





    def to_dict(self) -> dict[str, Any]:
        from ..models.entity_details import EntityDetails
        from ..models.entity_authorization_permissions_subject_identifier import EntityAuthorizationPermissionsSubjectIdentifier
        subject_identifier = self.subject_identifier.to_dict()

        permission = self.permission.value

        description = self.description

        subject_details = self.subject_details.to_dict()


        field_dict: dict[str, Any] = {}

        field_dict.update({
            "subjectIdentifier": subject_identifier,
            "permission": permission,
            "description": description,
            "subjectDetails": subject_details,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.entity_details import EntityDetails
        from ..models.entity_authorization_permissions_subject_identifier import EntityAuthorizationPermissionsSubjectIdentifier
        d = dict(src_dict)
        subject_identifier = EntityAuthorizationPermissionsSubjectIdentifier.from_dict(d.pop("subjectIdentifier"))




        permission = EntityAuthorizationPermissionType(d.pop("permission"))




        description = d.pop("description")

        subject_details = EntityDetails.from_dict(d.pop("subjectDetails"))




        entity_authorization_permissions_grant_request = cls(
            subject_identifier=subject_identifier,
            permission=permission,
            description=description,
            subject_details=subject_details,
        )

        return entity_authorization_permissions_grant_request

