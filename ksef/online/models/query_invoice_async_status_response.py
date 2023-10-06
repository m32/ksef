from typing import Any, Dict, Type, TypeVar, Tuple, Optional, BinaryIO, TextIO, TYPE_CHECKING

from typing import List


from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from dateutil.parser import isoparse
from typing import Dict
import datetime
from ..types import UNSET, Unset
from typing import cast, List
from typing import Union
from typing import cast

if TYPE_CHECKING:
  from ..models.invoice_division_plain_part_type import InvoiceDivisionPlainPartType





T = TypeVar("T", bound="QueryInvoiceAsyncStatusResponse")


@_attrs_define
class QueryInvoiceAsyncStatusResponse:
    """ 
        Attributes:
            element_reference_number (str):
            processing_code (int):
            processing_description (str):
            reference_number (str):
            timestamp (datetime.datetime):
            number_of_elements (Union[Unset, int]):
            number_of_parts (Union[Unset, int]):
            part_list (Union[Unset, List['InvoiceDivisionPlainPartType']]):
     """

    element_reference_number: str
    processing_code: int
    processing_description: str
    reference_number: str
    timestamp: datetime.datetime
    number_of_elements: Union[Unset, int] = UNSET
    number_of_parts: Union[Unset, int] = UNSET
    part_list: Union[Unset, List['InvoiceDivisionPlainPartType']] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)


    def to_dict(self) -> Dict[str, Any]:
        from ..models.invoice_division_plain_part_type import InvoiceDivisionPlainPartType
        element_reference_number = self.element_reference_number
        processing_code = self.processing_code
        processing_description = self.processing_description
        reference_number = self.reference_number
        timestamp = self.timestamp.isoformat()

        number_of_elements = self.number_of_elements
        number_of_parts = self.number_of_parts
        part_list: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.part_list, Unset):
            part_list = []
            for part_list_item_data in self.part_list:
                part_list_item = part_list_item_data.to_dict()

                part_list.append(part_list_item)





        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "elementReferenceNumber": element_reference_number,
            "processingCode": processing_code,
            "processingDescription": processing_description,
            "referenceNumber": reference_number,
            "timestamp": timestamp,
        })
        if number_of_elements is not UNSET:
            field_dict["numberOfElements"] = number_of_elements
        if number_of_parts is not UNSET:
            field_dict["numberOfParts"] = number_of_parts
        if part_list is not UNSET:
            field_dict["partList"] = part_list

        return field_dict



    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.invoice_division_plain_part_type import InvoiceDivisionPlainPartType
        d = src_dict.copy()
        element_reference_number = d.pop("elementReferenceNumber")

        processing_code = d.pop("processingCode")

        processing_description = d.pop("processingDescription")

        reference_number = d.pop("referenceNumber")

        timestamp = isoparse(d.pop("timestamp"))




        number_of_elements = d.pop("numberOfElements", UNSET)

        number_of_parts = d.pop("numberOfParts", UNSET)

        part_list = []
        _part_list = d.pop("partList", UNSET)
        for part_list_item_data in (_part_list or []):
            part_list_item = InvoiceDivisionPlainPartType.from_dict(part_list_item_data)



            part_list.append(part_list_item)


        query_invoice_async_status_response = cls(
            element_reference_number=element_reference_number,
            processing_code=processing_code,
            processing_description=processing_description,
            reference_number=reference_number,
            timestamp=timestamp,
            number_of_elements=number_of_elements,
            number_of_parts=number_of_parts,
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
