from typing import Any, Dict, Type, TypeVar, Tuple, Optional, BinaryIO, TextIO, TYPE_CHECKING

from typing import List


from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

import datetime
from dateutil.parser import isoparse
from typing import cast






T = TypeVar("T", bound="PaymentIdentifierObject")


@_attrs_define
class PaymentIdentifierObject:
    """ 
        Attributes:
            created_at (datetime.datetime):
            number_of_ksef_reference_numbers (int):
            payment_identifier (str):
     """

    created_at: datetime.datetime
    number_of_ksef_reference_numbers: int
    payment_identifier: str
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)


    def to_dict(self) -> Dict[str, Any]:
        created_at = self.created_at.isoformat()

        number_of_ksef_reference_numbers = self.number_of_ksef_reference_numbers
        payment_identifier = self.payment_identifier

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "createdAt": created_at,
            "numberOfKsefReferenceNumbers": number_of_ksef_reference_numbers,
            "paymentIdentifier": payment_identifier,
        })

        return field_dict



    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        created_at = isoparse(d.pop("createdAt"))




        number_of_ksef_reference_numbers = d.pop("numberOfKsefReferenceNumbers")

        payment_identifier = d.pop("paymentIdentifier")

        payment_identifier_object = cls(
            created_at=created_at,
            number_of_ksef_reference_numbers=number_of_ksef_reference_numbers,
            payment_identifier=payment_identifier,
        )

        payment_identifier_object.additional_properties = d
        return payment_identifier_object

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
