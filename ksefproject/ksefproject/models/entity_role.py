from collections.abc import Mapping
from typing import Any, TypeVar, Optional, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.entity_role_type import EntityRoleType
from ..types import UNSET, Unset
from dateutil.parser import isoparse
from typing import cast
from typing import cast, Union
from typing import Union
import datetime

if TYPE_CHECKING:
  from ..models.entity_roles_parent_entity_identifier import EntityRolesParentEntityIdentifier





T = TypeVar("T", bound="EntityRole")



@_attrs_define
class EntityRole:
    """ 
        Attributes:
            role (EntityRoleType):
            description (str): Opis roli.
            start_date (datetime.datetime): Data rozpoczęcia obowiązywania roli.
            parent_entity_identifier (Union['EntityRolesParentEntityIdentifier', None, Unset]): Identyfikator podmiotu
                nadrzędnego.
                | Type | Value |
                | --- | --- |
                | Nip | 10 cyfrowy numer NIP |
     """

    role: EntityRoleType
    description: str
    start_date: datetime.datetime
    parent_entity_identifier: Union['EntityRolesParentEntityIdentifier', None, Unset] = UNSET





    def to_dict(self) -> dict[str, Any]:
        from ..models.entity_roles_parent_entity_identifier import EntityRolesParentEntityIdentifier
        role = self.role.value

        description = self.description

        start_date = self.start_date.isoformat()

        parent_entity_identifier: Union[None, Unset, dict[str, Any]]
        if isinstance(self.parent_entity_identifier, Unset):
            parent_entity_identifier = UNSET
        elif isinstance(self.parent_entity_identifier, EntityRolesParentEntityIdentifier):
            parent_entity_identifier = self.parent_entity_identifier.to_dict()
        else:
            parent_entity_identifier = self.parent_entity_identifier


        field_dict: dict[str, Any] = {}

        field_dict.update({
            "role": role,
            "description": description,
            "startDate": start_date,
        })
        if parent_entity_identifier is not UNSET:
            field_dict["parentEntityIdentifier"] = parent_entity_identifier

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.entity_roles_parent_entity_identifier import EntityRolesParentEntityIdentifier
        d = dict(src_dict)
        role = EntityRoleType(d.pop("role"))




        description = d.pop("description")

        start_date = isoparse(d.pop("startDate"))




        def _parse_parent_entity_identifier(data: object) -> Union['EntityRolesParentEntityIdentifier', None, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                parent_entity_identifier_type_1 = EntityRolesParentEntityIdentifier.from_dict(data)



                return parent_entity_identifier_type_1
            except: # noqa: E722
                pass
            return cast(Union['EntityRolesParentEntityIdentifier', None, Unset], data)

        parent_entity_identifier = _parse_parent_entity_identifier(d.pop("parentEntityIdentifier", UNSET))


        entity_role = cls(
            role=role,
            description=description,
            start_date=start_date,
            parent_entity_identifier=parent_entity_identifier,
        )

        return entity_role

