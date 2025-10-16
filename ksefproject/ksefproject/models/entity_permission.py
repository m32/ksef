from collections.abc import Mapping
from typing import Any, TypeVar, Optional, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.entity_permission_type import EntityPermissionType
from ..types import UNSET, Unset
from typing import Union






T = TypeVar("T", bound="EntityPermission")



@_attrs_define
class EntityPermission:
    """ 
        Attributes:
            type_ (EntityPermissionType):
            can_delegate (Union[Unset, bool]): Flaga pozwalająca na pośrednie przekazywanie danego uprawnienia
     """

    type_: EntityPermissionType
    can_delegate: Union[Unset, bool] = UNSET





    def to_dict(self) -> dict[str, Any]:
        type_ = self.type_.value

        can_delegate = self.can_delegate


        field_dict: dict[str, Any] = {}

        field_dict.update({
            "type": type_,
        })
        if can_delegate is not UNSET:
            field_dict["canDelegate"] = can_delegate

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        type_ = EntityPermissionType(d.pop("type"))




        can_delegate = d.pop("canDelegate", UNSET)

        entity_permission = cls(
            type_=type_,
            can_delegate=can_delegate,
        )

        return entity_permission

