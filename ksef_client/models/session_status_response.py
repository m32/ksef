import datetime
from typing import Any, Dict, List, Type, TypeVar

import attr
from dateutil.parser import isoparse

from ..models.session_invoice_status_type import SessionInvoiceStatusType

T = TypeVar("T", bound="SessionStatusResponse")


@attr.s(auto_attribs=True)
class SessionStatusResponse:
    """
    Attributes:
        timestamp (datetime.datetime):
        reference_number (str):
        number_of_elements (int):
        page_size (int):
        page_offset (int):
        processing_code (int):
        processing_description (str):
        invoice_status_list (List[SessionInvoiceStatusType]):
    """

    timestamp: datetime.datetime
    reference_number: str
    number_of_elements: int
    page_size: int
    page_offset: int
    processing_code: int
    processing_description: str
    #invoice_status_list: List[SessionInvoiceStatusType]
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        timestamp = self.timestamp.isoformat()

        reference_number = self.reference_number
        number_of_elements = self.number_of_elements
        page_size = self.page_size
        page_offset = self.page_offset
        processing_code = self.processing_code
        processing_description = self.processing_description
        #invoice_status_list = []
        #for invoice_status_list_item_data in self.invoice_status_list:
        #    invoice_status_list_item = invoice_status_list_item_data.to_dict()
        #    invoice_status_list.append(invoice_status_list_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "timestamp": timestamp,
                "referenceNumber": reference_number,
                "numberOfElements": number_of_elements,
                "pageSize": page_size,
                "pageOffset": page_offset,
                "processingCode": processing_code,
                "processingDescription": processing_description,
        #        "invoiceStatusList": invoice_status_list,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        timestamp = isoparse(d.pop("timestamp"))

        reference_number = d.pop("referenceNumber")

        number_of_elements = d.pop("numberOfElements")

        page_size = d.pop("pageSize")

        page_offset = d.pop("pageOffset")

        processing_code = d.pop("processingCode")

        processing_description = d.pop("processingDescription")

        #invoice_status_list = []
        #_invoice_status_list = d.pop("invoiceStatusList")
        #for invoice_status_list_item_data in _invoice_status_list:
        #    invoice_status_list_item = SessionInvoiceStatusType.from_dict(invoice_status_list_item_data)
        #    invoice_status_list.append(invoice_status_list_item)

        session_status_response = cls(
            timestamp=timestamp,
            reference_number=reference_number,
            number_of_elements=number_of_elements,
            page_size=page_size,
            page_offset=page_offset,
            processing_code=processing_code,
            processing_description=processing_description,
        #    invoice_status_list=invoice_status_list,
        )

        session_status_response.additional_properties = d
        return session_status_response

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
