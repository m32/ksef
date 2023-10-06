import datetime
from typing import Any, Dict, List, Type, TypeVar

import attr
from dateutil.parser import isoparse

T = TypeVar("T", bound="QueryInvoiceAsyncInitResponse")


@attr.s(auto_attribs=True)
class QueryInvoiceAsyncInitResponse:
    """
    Attributes:
        timestamp (datetime.datetime):
        reference_number (str):
        processing_code (int):
        processing_description (str):
        element_reference_number (str):
    """

    timestamp: datetime.datetime
    reference_number: str
    processing_code: int
    processing_description: str
    element_reference_number: str
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        timestamp = self.timestamp.isoformat()

        reference_number = self.reference_number
        processing_code = self.processing_code
        processing_description = self.processing_description
        element_reference_number = self.element_reference_number

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "timestamp": timestamp,
                "referenceNumber": reference_number,
                "processingCode": processing_code,
                "processingDescription": processing_description,
                "elementReferenceNumber": element_reference_number,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        timestamp = isoparse(d.pop("timestamp"))

        reference_number = d.pop("referenceNumber")

        processing_code = d.pop("processingCode")

        processing_description = d.pop("processingDescription")

        element_reference_number = d.pop("elementReferenceNumber")

        query_invoice_async_init_response = cls(
            timestamp=timestamp,
            reference_number=reference_number,
            processing_code=processing_code,
            processing_description=processing_description,
            element_reference_number=element_reference_number,
        )

        query_invoice_async_init_response.additional_properties = d
        return query_invoice_async_init_response

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
