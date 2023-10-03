import datetime
from typing import Any, Dict, List, Type, TypeVar

import attr
from dateutil.parser import isoparse

from ..models.invoice_header_type import InvoiceHeaderType

T = TypeVar("T", bound="QueryInvoiceSyncResponse")


@attr.s(auto_attribs=True)
class QueryInvoiceSyncResponse:
    """
    Attributes:
        timestamp (datetime.datetime):
        reference_number (str):
        number_of_elements (int):
        page_size (int):
        page_offset (int):
        invoice_header_list (List[InvoiceHeaderType]):
    """

    timestamp: datetime.datetime
    reference_number: str
    number_of_elements: int
    page_size: int
    page_offset: int
    invoice_header_list: List[InvoiceHeaderType]
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        timestamp = self.timestamp.isoformat()

        reference_number = self.reference_number
        number_of_elements = self.number_of_elements
        page_size = self.page_size
        page_offset = self.page_offset
        invoice_header_list = []
        for invoice_header_list_item_data in self.invoice_header_list:
            invoice_header_list_item = invoice_header_list_item_data.to_dict()

            invoice_header_list.append(invoice_header_list_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "timestamp": timestamp,
                "referenceNumber": reference_number,
                "numberOfElements": number_of_elements,
                "pageSize": page_size,
                "pageOffset": page_offset,
                "invoiceHeaderList": invoice_header_list,
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

        invoice_header_list = []
        _invoice_header_list = d.pop("invoiceHeaderList")
        for invoice_header_list_item_data in _invoice_header_list:
            invoice_header_list_item = InvoiceHeaderType.from_dict(invoice_header_list_item_data)

            invoice_header_list.append(invoice_header_list_item)

        query_invoice_sync_response = cls(
            timestamp=timestamp,
            reference_number=reference_number,
            number_of_elements=number_of_elements,
            page_size=page_size,
            page_offset=page_offset,
            invoice_header_list=invoice_header_list,
        )

        query_invoice_sync_response.additional_properties = d
        return query_invoice_sync_response

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
