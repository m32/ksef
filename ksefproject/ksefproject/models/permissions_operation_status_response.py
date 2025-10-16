from collections.abc import Mapping
from typing import Any, TypeVar, Optional, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from typing import cast

if TYPE_CHECKING:
  from ..models.status_info import StatusInfo





T = TypeVar("T", bound="PermissionsOperationStatusResponse")



@_attrs_define
class PermissionsOperationStatusResponse:
    """ 
        Attributes:
            status (StatusInfo):
     """

    status: 'StatusInfo'





    def to_dict(self) -> dict[str, Any]:
        from ..models.status_info import StatusInfo
        status = self.status.to_dict()


        field_dict: dict[str, Any] = {}

        field_dict.update({
            "status": status,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.status_info import StatusInfo
        d = dict(src_dict)
        status = StatusInfo.from_dict(d.pop("status"))




        permissions_operation_status_response = cls(
            status=status,
        )

        return permissions_operation_status_response

