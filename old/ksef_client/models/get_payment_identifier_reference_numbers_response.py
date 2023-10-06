import datetime
from typing import Any, Dict, List, Type, TypeVar, cast

import attr
from dateutil.parser import isoparse

T = TypeVar("T", bound="GetPaymentIdentifierReferenceNumbersResponse")


@attr.s(auto_attribs=True)
class GetPaymentIdentifierReferenceNumbersResponse:
    """
    Attributes:
        timestamp (datetime.datetime):
        reference_number (str):
        ksef_reference_number_list (List[str]):
    """

    timestamp: datetime.datetime
    reference_number: str
    ksef_reference_number_list: List[str]
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        timestamp = self.timestamp.isoformat()

        reference_number = self.reference_number
        ksef_reference_number_list = self.ksef_reference_number_list

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "timestamp": timestamp,
                "referenceNumber": reference_number,
                "ksefReferenceNumberList": ksef_reference_number_list,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        timestamp = isoparse(d.pop("timestamp"))

        reference_number = d.pop("referenceNumber")

        ksef_reference_number_list = cast(List[str], d.pop("ksefReferenceNumberList"))

        get_payment_identifier_reference_numbers_response = cls(
            timestamp=timestamp,
            reference_number=reference_number,
            ksef_reference_number_list=ksef_reference_number_list,
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
