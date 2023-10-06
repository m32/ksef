import datetime
from typing import Any, Dict, List, Type, TypeVar

import attr
from dateutil.parser import isoparse

from ..models.file_unlimited_hash_type import FileUnlimitedHashType

T = TypeVar("T", bound="InvoiceDivisionPlainPartType")


@attr.s(auto_attribs=True)
class InvoiceDivisionPlainPartType:
    """
    Attributes:
        part_reference_number (str):
        part_name (str):
        part_number (int):
        part_range_from (datetime.datetime):
        part_range_to (datetime.datetime):
        part_expiration (datetime.datetime):
        plain_part_hash (FileUnlimitedHashType):
    """

    part_reference_number: str
    part_name: str
    part_number: int
    part_range_from: datetime.datetime
    part_range_to: datetime.datetime
    part_expiration: datetime.datetime
    plain_part_hash: FileUnlimitedHashType
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        part_reference_number = self.part_reference_number
        part_name = self.part_name
        part_number = self.part_number
        part_range_from = self.part_range_from.isoformat()

        part_range_to = self.part_range_to.isoformat()

        part_expiration = self.part_expiration.isoformat()

        plain_part_hash = self.plain_part_hash.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "partReferenceNumber": part_reference_number,
                "partName": part_name,
                "partNumber": part_number,
                "partRangeFrom": part_range_from,
                "partRangeTo": part_range_to,
                "partExpiration": part_expiration,
                "plainPartHash": plain_part_hash,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        part_reference_number = d.pop("partReferenceNumber")

        part_name = d.pop("partName")

        part_number = d.pop("partNumber")

        part_range_from = isoparse(d.pop("partRangeFrom"))

        part_range_to = isoparse(d.pop("partRangeTo"))

        part_expiration = isoparse(d.pop("partExpiration"))

        plain_part_hash = FileUnlimitedHashType.from_dict(d.pop("plainPartHash"))

        invoice_division_plain_part_type = cls(
            part_reference_number=part_reference_number,
            part_name=part_name,
            part_number=part_number,
            part_range_from=part_range_from,
            part_range_to=part_range_to,
            part_expiration=part_expiration,
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
