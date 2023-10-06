from typing import Any, Dict, Type, TypeVar, Tuple, Optional, BinaryIO, TextIO, TYPE_CHECKING

from typing import List


from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

import datetime
from dateutil.parser import isoparse
from typing import cast
from typing import Dict

if TYPE_CHECKING:
  from ..models.file_unlimited_hash_type import FileUnlimitedHashType





T = TypeVar("T", bound="InvoiceDivisionPlainPartType")


@_attrs_define
class InvoiceDivisionPlainPartType:
    """ 
        Attributes:
            part_expiration (datetime.datetime):
            part_name (str):
            part_number (int):
            part_range_from (datetime.datetime):
            part_range_to (datetime.datetime):
            part_reference_number (str):
            plain_part_hash (FileUnlimitedHashType):
     """

    part_expiration: datetime.datetime
    part_name: str
    part_number: int
    part_range_from: datetime.datetime
    part_range_to: datetime.datetime
    part_reference_number: str
    plain_part_hash: 'FileUnlimitedHashType'
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)


    def to_dict(self) -> Dict[str, Any]:
        from ..models.file_unlimited_hash_type import FileUnlimitedHashType
        part_expiration = self.part_expiration.isoformat()

        part_name = self.part_name
        part_number = self.part_number
        part_range_from = self.part_range_from.isoformat()

        part_range_to = self.part_range_to.isoformat()

        part_reference_number = self.part_reference_number
        plain_part_hash = self.plain_part_hash.to_dict()


        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "partExpiration": part_expiration,
            "partName": part_name,
            "partNumber": part_number,
            "partRangeFrom": part_range_from,
            "partRangeTo": part_range_to,
            "partReferenceNumber": part_reference_number,
            "plainPartHash": plain_part_hash,
        })

        return field_dict



    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.file_unlimited_hash_type import FileUnlimitedHashType
        d = src_dict.copy()
        part_expiration = isoparse(d.pop("partExpiration"))




        part_name = d.pop("partName")

        part_number = d.pop("partNumber")

        part_range_from = isoparse(d.pop("partRangeFrom"))




        part_range_to = isoparse(d.pop("partRangeTo"))




        part_reference_number = d.pop("partReferenceNumber")

        plain_part_hash = FileUnlimitedHashType.from_dict(d.pop("plainPartHash"))




        invoice_division_plain_part_type = cls(
            part_expiration=part_expiration,
            part_name=part_name,
            part_number=part_number,
            part_range_from=part_range_from,
            part_range_to=part_range_to,
            part_reference_number=part_reference_number,
            plain_part_hash=plain_part_hash,
        )

        invoice_division_plain_part_type.additional_properties = d
        return invoice_division_plain_part_type

    @property
    def additional_keys(self) -> List[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
