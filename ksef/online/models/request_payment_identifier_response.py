from typing import Any, Dict, Type, TypeVar, Tuple, Optional, BinaryIO, TextIO, TYPE_CHECKING

from typing import List


from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from typing import cast
import datetime
from dateutil.parser import isoparse






T = TypeVar("T", bound="RequestPaymentIdentifierResponse")


@_attrs_define
class RequestPaymentIdentifierResponse:
    """ 
        Attributes:
            payment_identifier (str):
            reference_number (str):
            timestamp (datetime.datetime):
     """

    payment_identifier: str
    reference_number: str
    timestamp: datetime.datetime
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)


    def to_dict(self) -> Dict[str, Any]:
        payment_identifier = self.payment_identifier
        reference_number = self.reference_number
        timestamp = self.timestamp.isoformat()


        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "paymentIdentifier": payment_identifier,
            "referenceNumber": reference_number,
            "timestamp": timestamp,
        })

        return field_dict



    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        payment_identifier = d.pop("paymentIdentifier")

        reference_number = d.pop("referenceNumber")

        timestamp = isoparse(d.pop("timestamp"))




        request_payment_identifier_response = cls(
            payment_identifier=payment_identifier,
            reference_number=reference_number,
            timestamp=timestamp,
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
