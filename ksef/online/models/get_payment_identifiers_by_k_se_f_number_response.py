from typing import Any, Dict, Type, TypeVar, Tuple, Optional, BinaryIO, TextIO, TYPE_CHECKING

from typing import List


from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from dateutil.parser import isoparse
from typing import Dict
from typing import cast, List
from typing import cast
import datetime

if TYPE_CHECKING:
  from ..models.payment_identifier_type import PaymentIdentifierType





T = TypeVar("T", bound="GetPaymentIdentifiersByKSeFNumberResponse")


@_attrs_define
class GetPaymentIdentifiersByKSeFNumberResponse:
    """ 
        Attributes:
            is_subject (float):
            number_of_elements (int):
            page_offset (int):
            page_size (int):
            payment_identifiers_list (List['PaymentIdentifierType']):
            reference_number (str):
            timestamp (datetime.datetime):
     """

    is_subject: float
    number_of_elements: int
    page_offset: int
    page_size: int
    payment_identifiers_list: List['PaymentIdentifierType']
    reference_number: str
    timestamp: datetime.datetime
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)


    def to_dict(self) -> Dict[str, Any]:
        from ..models.payment_identifier_type import PaymentIdentifierType
        is_subject = self.is_subject
        number_of_elements = self.number_of_elements
        page_offset = self.page_offset
        page_size = self.page_size
        payment_identifiers_list = []
        for payment_identifiers_list_item_data in self.payment_identifiers_list:
            payment_identifiers_list_item = payment_identifiers_list_item_data.to_dict()

            payment_identifiers_list.append(payment_identifiers_list_item)




        reference_number = self.reference_number
        timestamp = self.timestamp.isoformat()


        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "isSubject": is_subject,
            "numberOfElements": number_of_elements,
            "pageOffset": page_offset,
            "pageSize": page_size,
            "paymentIdentifiersList": payment_identifiers_list,
            "referenceNumber": reference_number,
            "timestamp": timestamp,
        })

        return field_dict



    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.payment_identifier_type import PaymentIdentifierType
        d = src_dict.copy()
        is_subject = d.pop("isSubject")

        number_of_elements = d.pop("numberOfElements")

        page_offset = d.pop("pageOffset")

        page_size = d.pop("pageSize")

        payment_identifiers_list = []
        _payment_identifiers_list = d.pop("paymentIdentifiersList")
        for payment_identifiers_list_item_data in (_payment_identifiers_list):
            payment_identifiers_list_item = PaymentIdentifierType.from_dict(payment_identifiers_list_item_data)



            payment_identifiers_list.append(payment_identifiers_list_item)


        reference_number = d.pop("referenceNumber")

        timestamp = isoparse(d.pop("timestamp"))




        get_payment_identifiers_by_k_se_f_number_response = cls(
            is_subject=is_subject,
            number_of_elements=number_of_elements,
            page_offset=page_offset,
            page_size=page_size,
            payment_identifiers_list=payment_identifiers_list,
            reference_number=reference_number,
            timestamp=timestamp,
        )

        get_payment_identifiers_by_k_se_f_number_response.additional_properties = d
        return get_payment_identifiers_by_k_se_f_number_response

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
