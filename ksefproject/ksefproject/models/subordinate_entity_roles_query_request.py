from collections.abc import Mapping
from typing import Any, TypeVar, Optional, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast
from typing import cast, Union
from typing import Union

if TYPE_CHECKING:
  from ..models.entity_permissions_subordinate_entity_identifier import EntityPermissionsSubordinateEntityIdentifier





T = TypeVar("T", bound="SubordinateEntityRolesQueryRequest")



@_attrs_define
class SubordinateEntityRolesQueryRequest:
    """ 
        Attributes:
            subordinate_entity_identifier (Union['EntityPermissionsSubordinateEntityIdentifier', None, Unset]):
                Identyfikator podmiotu podrzędnego.
                | Type | Value |
                | --- | --- |
                | Nip | 10 cyfrowy numer NIP |
     """

    subordinate_entity_identifier: Union['EntityPermissionsSubordinateEntityIdentifier', None, Unset] = UNSET





    def to_dict(self) -> dict[str, Any]:
        from ..models.entity_permissions_subordinate_entity_identifier import EntityPermissionsSubordinateEntityIdentifier
        subordinate_entity_identifier: Union[None, Unset, dict[str, Any]]
        if isinstance(self.subordinate_entity_identifier, Unset):
            subordinate_entity_identifier = UNSET
        elif isinstance(self.subordinate_entity_identifier, EntityPermissionsSubordinateEntityIdentifier):
            subordinate_entity_identifier = self.subordinate_entity_identifier.to_dict()
        else:
            subordinate_entity_identifier = self.subordinate_entity_identifier


        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
        if subordinate_entity_identifier is not UNSET:
            field_dict["subordinateEntityIdentifier"] = subordinate_entity_identifier

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.entity_permissions_subordinate_entity_identifier import EntityPermissionsSubordinateEntityIdentifier
        d = dict(src_dict)
        def _parse_subordinate_entity_identifier(data: object) -> Union['EntityPermissionsSubordinateEntityIdentifier', None, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                subordinate_entity_identifier_type_1 = EntityPermissionsSubordinateEntityIdentifier.from_dict(data)



                return subordinate_entity_identifier_type_1
            except: # noqa: E722
                pass
            return cast(Union['EntityPermissionsSubordinateEntityIdentifier', None, Unset], data)

        subordinate_entity_identifier = _parse_subordinate_entity_identifier(d.pop("subordinateEntityIdentifier", UNSET))


        subordinate_entity_roles_query_request = cls(
            subordinate_entity_identifier=subordinate_entity_identifier,
        )

        return subordinate_entity_roles_query_request

