import datetime
from typing import Any, Dict, List, Type, TypeVar

import attr
from dateutil.parser import isoparse

T = TypeVar("T", bound="RequestPaymentIdentifierResponse")


@attr.s(auto_attribs=True)
class RequestPaymentIdentifierResponse:
    """
    Attributes:
        timestamp (datetime.datetime):
        reference_number (str):
        payment_identifier (str):
    """

    timestamp: datetime.datetime
    reference_number: str
    payment_identifier: str
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        timestamp = self.timestamp.isoformat()

        reference_number = self.reference_number
        payment_identifier = self.payment_identifier

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "timestamp": timestamp,
                "referenceNumber": reference_number,
                "paymentIdentifier": payment_identifier,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        timestamp = isoparse(d.pop("timestamp"))

        reference_number = d.pop("referenceNumber")

        payment_identifier = d.pop("paymentIdentifier")

        request_payment_identifier_response = cls(
            timestamp=timestamp,
            reference_number=reference_number,
            payment_identifier=payment_identifier,
        )

        request_payment_identifier_response.additional_properties = d
        return request_payment_identifier_response

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
