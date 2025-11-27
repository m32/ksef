from collections.abc import Mapping
from typing import Any, TypeVar, Optional, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.entity_authorization_permissions_subject_identifier_type import EntityAuthorizationPermissionsSubjectIdentifierType






T = TypeVar("T", bound="EntityAuthorizationPermissionsSubjectIdentifier")



@_attrs_define
class EntityAuthorizationPermissionsSubjectIdentifier:
    """ Identyfikator podmiotu uprawnianego.
    | Type | Value |
    | --- | --- |
    | Nip | 10 cyfrowy numer NIP |
    | PeppolId | Identyfikator dostawcy usług Peppol |

        Attributes:
            type_ (EntityAuthorizationPermissionsSubjectIdentifierType):
            value (str): Wartość identyfikatora.
     """

    type_: EntityAuthorizationPermissionsSubjectIdentifierType
    value: str





    def to_dict(self) -> dict[str, Any]:
        type_ = self.type_.value

        value = self.value


        field_dict: dict[str, Any] = {}

        field_dict.update({
            "type": type_,
            "value": value,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        type_ = EntityAuthorizationPermissionsSubjectIdentifierType(d.pop("type"))




        value = d.pop("value")

        entity_authorization_permissions_subject_identifier = cls(
            type_=type_,
            value=value,
        )

        return entity_authorization_permissions_subject_identifier

