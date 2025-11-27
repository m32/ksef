from collections.abc import Mapping
from typing import Any, TypeVar, Optional, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.subordinate_entity_role_type import SubordinateEntityRoleType
from dateutil.parser import isoparse
from typing import cast
import datetime

if TYPE_CHECKING:
  from ..models.subordinate_role_subordinate_entity_identifier import SubordinateRoleSubordinateEntityIdentifier





T = TypeVar("T", bound="SubordinateEntityRole")



@_attrs_define
class SubordinateEntityRole:
    """ 
        Attributes:
            subordinate_entity_identifier (SubordinateRoleSubordinateEntityIdentifier): Identyfikator podmiotu podrzędnego.
                | Type | Value |
                | --- | --- |
                | Nip | 10 cyfrowy numer NIP |
            role (SubordinateEntityRoleType):
            description (str): Opis powiązania.
            start_date (datetime.datetime): Data rozpoczęcia obowiązywania powiązania.
     """

    subordinate_entity_identifier: 'SubordinateRoleSubordinateEntityIdentifier'
    role: SubordinateEntityRoleType
    description: str
    start_date: datetime.datetime





    def to_dict(self) -> dict[str, Any]:
        from ..models.subordinate_role_subordinate_entity_identifier import SubordinateRoleSubordinateEntityIdentifier
        subordinate_entity_identifier = self.subordinate_entity_identifier.to_dict()

        role = self.role.value

        description = self.description

        start_date = self.start_date.isoformat()


        field_dict: dict[str, Any] = {}

        field_dict.update({
            "subordinateEntityIdentifier": subordinate_entity_identifier,
            "role": role,
            "description": description,
            "startDate": start_date,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.subordinate_role_subordinate_entity_identifier import SubordinateRoleSubordinateEntityIdentifier
        d = dict(src_dict)
        subordinate_entity_identifier = SubordinateRoleSubordinateEntityIdentifier.from_dict(d.pop("subordinateEntityIdentifier"))




        role = SubordinateEntityRoleType(d.pop("role"))




        description = d.pop("description")

        start_date = isoparse(d.pop("startDate"))




        subordinate_entity_role = cls(
            subordinate_entity_identifier=subordinate_entity_identifier,
            role=role,
            description=description,
            start_date=start_date,
        )

        return subordinate_entity_role

