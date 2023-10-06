from typing import Any, Dict, Type, TypeVar, Tuple, Optional, BinaryIO, TextIO, TYPE_CHECKING

from typing import List


from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

import datetime
from typing import cast, List
from dateutil.parser import isoparse
from typing import cast






T = TypeVar("T", bound="GetPaymentIdentifierReferenceNumbersResponse")


@_attrs_define
class GetPaymentIdentifierReferenceNumbersResponse:
    """ 
        Attributes:
            ksef_reference_number_list (List[str]):
            reference_number (str):
            timestamp (datetime.datetime):
     """

    ksef_reference_number_list: List[str]
    reference_number: str
    timestamp: datetime.datetime
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)


    def to_dict(self) -> Dict[str, Any]:
        ksef_reference_number_list = self.ksef_reference_number_list




        reference_number = self.reference_number
        timestamp = self.timestamp.isoformat()


        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "ksefReferenceNumberList": ksef_reference_number_list,
            "referenceNumber": reference_number,
            "timestamp": timestamp,
        })

        return field_dict



    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        ksef_reference_number_list = cast(List[str], d.pop("ksefReferenceNumberList"))


        reference_number = d.pop("referenceNumber")

        timestamp = isoparse(d.pop("timestamp"))




        get_payment_identifier_reference_numbers_response = cls(
            ksef_reference_number_list=ksef_reference_number_list,
            reference_number=reference_number,
            timestamp=timestamp,
        )

        get_payment_identifier_reference_numbers_response.additional_properties = d
        return get_payment_identifier_reference_numbers_response

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
