from collections.abc import Mapping
from typing import Any, TypeVar, Optional, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.entity_subject_by_identifier_details_type import EntitySubjectByIdentifierDetailsType






T = TypeVar("T", bound="PermissionsSubjectEntityByIdentifierDetails")



@_attrs_define
class PermissionsSubjectEntityByIdentifierDetails:
    """ 
        Attributes:
            subject_details_type (EntitySubjectByIdentifierDetailsType): | Wartość | Opis |
                | --- | --- |
                | EntityByIdentifier | Podmiot identyfikowany numerem NIP. |
            full_name (str): Pełna nazwa podmiotu.
     """

    subject_details_type: EntitySubjectByIdentifierDetailsType
    full_name: str





    def to_dict(self) -> dict[str, Any]:
        subject_details_type = self.subject_details_type.value

        full_name = self.full_name


        field_dict: dict[str, Any] = {}

        field_dict.update({
            "subjectDetailsType": subject_details_type,
            "fullName": full_name,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        subject_details_type = EntitySubjectByIdentifierDetailsType(d.pop("subjectDetailsType"))




        full_name = d.pop("fullName")

        permissions_subject_entity_by_identifier_details = cls(
            subject_details_type=subject_details_type,
            full_name=full_name,
        )

        return permissions_subject_entity_by_identifier_details

