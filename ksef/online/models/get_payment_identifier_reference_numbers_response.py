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
  from ..models.ksef_reference_number_list_response_object import KsefReferenceNumberListResponseObject





T = TypeVar("T", bound="GetPaymentIdentifierReferenceNumbersResponse")


@_attrs_define
class GetPaymentIdentifierReferenceNumbersResponse:
    """ 
        Attributes:
            created_at (datetime.datetime):
            ksef_reference_number_list (List['KsefReferenceNumberListResponseObject']):
            number_of_elements (int):
            page_offset (int):
            page_size (int):
            reference_number (str):
            timestamp (datetime.datetime):
     """

    created_at: datetime.datetime
    ksef_reference_number_list: List['KsefReferenceNumberListResponseObject']
    number_of_elements: int
    page_offset: int
    page_size: int
    reference_number: str
    timestamp: datetime.datetime
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)


    def to_dict(self) -> Dict[str, Any]:
        from ..models.ksef_reference_number_list_response_object import KsefReferenceNumberListResponseObject
        created_at = self.created_at.isoformat()

        ksef_reference_number_list = []
        for ksef_reference_number_list_item_data in self.ksef_reference_number_list:
            ksef_reference_number_list_item = ksef_reference_number_list_item_data.to_dict()

            ksef_reference_number_list.append(ksef_reference_number_list_item)




        number_of_elements = self.number_of_elements
        page_offset = self.page_offset
        page_size = self.page_size
        reference_number = self.reference_number
        timestamp = self.timestamp.isoformat()


        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "createdAt": created_at,
            "ksefReferenceNumberList": ksef_reference_number_list,
            "numberOfElements": number_of_elements,
            "pageOffset": page_offset,
            "pageSize": page_size,
            "referenceNumber": reference_number,
            "timestamp": timestamp,
        })

        return field_dict



    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.ksef_reference_number_list_response_object import KsefReferenceNumberListResponseObject
        d = src_dict.copy()
        created_at = isoparse(d.pop("createdAt"))




        ksef_reference_number_list = []
        _ksef_reference_number_list = d.pop("ksefReferenceNumberList")
        for ksef_reference_number_list_item_data in (_ksef_reference_number_list):
            ksef_reference_number_list_item = KsefReferenceNumberListResponseObject.from_dict(ksef_reference_number_list_item_data)



            ksef_reference_number_list.append(ksef_reference_number_list_item)


        number_of_elements = d.pop("numberOfElements")

        page_offset = d.pop("pageOffset")

        page_size = d.pop("pageSize")

        reference_number = d.pop("referenceNumber")

        timestamp = isoparse(d.pop("timestamp"))




        get_payment_identifier_reference_numbers_response = cls(
            created_at=created_at,
            ksef_reference_number_list=ksef_reference_number_list,
            number_of_elements=number_of_elements,
            page_offset=page_offset,
            page_size=page_size,
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
