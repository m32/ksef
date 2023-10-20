from typing import Any, Dict, Type, TypeVar, Tuple, Optional, BinaryIO, TextIO, TYPE_CHECKING

from typing import List


from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from dateutil.parser import isoparse
import datetime
from typing import Dict
from typing import cast

if TYPE_CHECKING:
  from ..models.invoice_status_type import InvoiceStatusType





T = TypeVar("T", bound="StatusInvoiceResponse")


@_attrs_define
class StatusInvoiceResponse:
    """ 
        Attributes:
            element_reference_number (str):
            invoice_status (InvoiceStatusType):
            processing_code (int):
            processing_description (str):
            reference_number (str):
            timestamp (datetime.datetime):
     """

    element_reference_number: str
    invoice_status: 'InvoiceStatusType'
    processing_code: int
    processing_description: str
    reference_number: str
    timestamp: datetime.datetime
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)


    def to_dict(self) -> Dict[str, Any]:
        from ..models.invoice_status_type import InvoiceStatusType
        element_reference_number = self.element_reference_number
        invoice_status = self.invoice_status.to_dict()

        processing_code = self.processing_code
        processing_description = self.processing_description
        reference_number = self.reference_number
        timestamp = self.timestamp.isoformat()


        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "elementReferenceNumber": element_reference_number,
            "invoiceStatus": invoice_status,
            "processingCode": processing_code,
            "processingDescription": processing_description,
            "referenceNumber": reference_number,
            "timestamp": timestamp,
        })

        return field_dict



    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.invoice_status_type import InvoiceStatusType
        d = src_dict.copy()
        element_reference_number = d.pop("elementReferenceNumber")

        invoice_status = InvoiceStatusType.from_dict(d.pop("invoiceStatus"))




        processing_code = d.pop("processingCode")

        processing_description = d.pop("processingDescription")

        reference_number = d.pop("referenceNumber")

        timestamp = isoparse(d.pop("timestamp"))




        status_invoice_response = cls(
            element_reference_number=element_reference_number,
            invoice_status=invoice_status,
            processing_code=processing_code,
            processing_description=processing_description,
            reference_number=reference_number,
            timestamp=timestamp,
        )

        status_invoice_response.additional_properties = d
        return status_invoice_response

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
