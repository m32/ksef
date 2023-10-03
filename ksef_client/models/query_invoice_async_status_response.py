import datetime
from typing import Any, Dict, List, Type, TypeVar

import attr
from dateutil.parser import isoparse

from ..models.invoice_division_plain_part_type import InvoiceDivisionPlainPartType
from ..models.query_invoice_async_status_response_division_type import QueryInvoiceAsyncStatusResponseDivisionType

T = TypeVar("T", bound="QueryInvoiceAsyncStatusResponse")


@attr.s(auto_attribs=True)
class QueryInvoiceAsyncStatusResponse:
    """
    Attributes:
        timestamp (datetime.datetime):
        reference_number (str):
        processing_code (int):
        processing_description (str):
        element_reference_number (str):
        number_of_parts (int):
        number_of_elements (int):
        division_type (QueryInvoiceAsyncStatusResponseDivisionType):
        part_list (List[InvoiceDivisionPlainPartType]):
    """

    timestamp: datetime.datetime
    reference_number: str
    processing_code: int
    processing_description: str
    element_reference_number: str
    number_of_parts: int
    number_of_elements: int
    division_type: QueryInvoiceAsyncStatusResponseDivisionType
    part_list: List[InvoiceDivisionPlainPartType]
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        timestamp = self.timestamp.isoformat()

        reference_number = self.reference_number
        processing_code = self.processing_code
        processing_description = self.processing_description
        element_reference_number = self.element_reference_number
        number_of_parts = self.number_of_parts
        number_of_elements = self.number_of_elements
        division_type = self.division_type.value

        part_list = []
        for part_list_item_data in self.part_list:
            part_list_item = part_list_item_data.to_dict()

            part_list.append(part_list_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "timestamp": timestamp,
                "referenceNumber": reference_number,
                "processingCode": processing_code,
                "processingDescription": processing_description,
                "elementReferenceNumber": element_reference_number,
                "numberOfParts": number_of_parts,
                "numberOfElements": number_of_elements,
                "divisionType": division_type,
                "partList": part_list,
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

        number_of_parts = d.pop("numberOfParts")

        number_of_elements = d.pop("numberOfElements")

        division_type = QueryInvoiceAsyncStatusResponseDivisionType(d.pop("divisionType"))

        part_list = []
        _part_list = d.pop("partList")
        for part_list_item_data in _part_list:
            part_list_item = InvoiceDivisionPlainPartType.from_dict(part_list_item_data)

            part_list.append(part_list_item)

        query_invoice_async_status_response = cls(
            timestamp=timestamp,
            reference_number=reference_number,
            processing_code=processing_code,
            processing_description=processing_description,
            element_reference_number=element_reference_number,
            number_of_parts=number_of_parts,
            number_of_elements=number_of_elements,
            division_type=division_type,
            part_list=part_list,
        )

        query_invoice_async_status_response.additional_properties = d
        return query_invoice_async_status_response

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
