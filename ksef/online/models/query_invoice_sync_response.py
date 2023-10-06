from typing import Any, Dict, Type, TypeVar, Tuple, Optional, BinaryIO, TextIO, TYPE_CHECKING

from typing import List


from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from dateutil.parser import isoparse
from typing import Dict
import datetime
from typing import cast, List
from typing import cast

if TYPE_CHECKING:
  from ..models.invoice_header_type import InvoiceHeaderType





T = TypeVar("T", bound="QueryInvoiceSyncResponse")


@_attrs_define
class QueryInvoiceSyncResponse:
    """ 
        Attributes:
            invoice_header_list (List['InvoiceHeaderType']):
            number_of_elements (int):
            page_offset (int):
            page_size (int):
            reference_number (str):
            timestamp (datetime.datetime):
     """

    invoice_header_list: List['InvoiceHeaderType']
    number_of_elements: int
    page_offset: int
    page_size: int
    reference_number: str
    timestamp: datetime.datetime
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)


    def to_dict(self) -> Dict[str, Any]:
        from ..models.invoice_header_type import InvoiceHeaderType
        invoice_header_list = []
        for invoice_header_list_item_data in self.invoice_header_list:
            invoice_header_list_item = invoice_header_list_item_data.to_dict()

            invoice_header_list.append(invoice_header_list_item)




        number_of_elements = self.number_of_elements
        page_offset = self.page_offset
        page_size = self.page_size
        reference_number = self.reference_number
        timestamp = self.timestamp.isoformat()


        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "invoiceHeaderList": invoice_header_list,
            "numberOfElements": number_of_elements,
            "pageOffset": page_offset,
            "pageSize": page_size,
            "referenceNumber": reference_number,
            "timestamp": timestamp,
        })

        return field_dict



    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.invoice_header_type import InvoiceHeaderType
        d = src_dict.copy()
        invoice_header_list = []
        _invoice_header_list = d.pop("invoiceHeaderList")
        for invoice_header_list_item_data in (_invoice_header_list):
            invoice_header_list_item = InvoiceHeaderType.from_dict(invoice_header_list_item_data)



            invoice_header_list.append(invoice_header_list_item)


        number_of_elements = d.pop("numberOfElements")

        page_offset = d.pop("pageOffset")

        page_size = d.pop("pageSize")

        reference_number = d.pop("referenceNumber")

        timestamp = isoparse(d.pop("timestamp"))




        query_invoice_sync_response = cls(
            invoice_header_list=invoice_header_list,
            number_of_elements=number_of_elements,
            page_offset=page_offset,
            page_size=page_size,
            reference_number=reference_number,
            timestamp=timestamp,
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
