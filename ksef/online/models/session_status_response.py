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
  from ..models.session_invoice_status_type import SessionInvoiceStatusType





T = TypeVar("T", bound="SessionStatusResponse")


@_attrs_define
class SessionStatusResponse:
    """ 
        Attributes:
            creation_timestamp (datetime.datetime):
            entity_type (str):
            last_update_timestamp (datetime.datetime):
            processing_code (int):
            processing_description (str):
            reference_number (str):
            timestamp (datetime.datetime):
            invoice_status_list (Union[Unset, List['SessionInvoiceStatusType']]):
            number_of_elements (Union[Unset, int]):
            page_offset (Union[Unset, int]):
            page_size (Union[Unset, int]):
     """

    creation_timestamp: datetime.datetime
    entity_type: str
    last_update_timestamp: datetime.datetime
    processing_code: int
    processing_description: str
    reference_number: str
    timestamp: datetime.datetime
    invoice_status_list: Union[Unset, List['SessionInvoiceStatusType']] = UNSET
    number_of_elements: Union[Unset, int] = UNSET
    page_offset: Union[Unset, int] = UNSET
    page_size: Union[Unset, int] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)


    def to_dict(self) -> Dict[str, Any]:
        from ..models.session_invoice_status_type import SessionInvoiceStatusType
        creation_timestamp = self.creation_timestamp.isoformat()

        entity_type = self.entity_type
        last_update_timestamp = self.last_update_timestamp.isoformat()

        processing_code = self.processing_code
        processing_description = self.processing_description
        reference_number = self.reference_number
        timestamp = self.timestamp.isoformat()

        invoice_status_list: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.invoice_status_list, Unset):
            invoice_status_list = []
            for invoice_status_list_item_data in self.invoice_status_list:
                invoice_status_list_item = invoice_status_list_item_data.to_dict()

                invoice_status_list.append(invoice_status_list_item)




        number_of_elements = self.number_of_elements
        page_offset = self.page_offset
        page_size = self.page_size

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "creationTimestamp": creation_timestamp,
            "entityType": entity_type,
            "lastUpdateTimestamp": last_update_timestamp,
            "processingCode": processing_code,
            "processingDescription": processing_description,
            "referenceNumber": reference_number,
            "timestamp": timestamp,
        })
        if invoice_status_list is not UNSET:
            field_dict["invoiceStatusList"] = invoice_status_list
        if number_of_elements is not UNSET:
            field_dict["numberOfElements"] = number_of_elements
        if page_offset is not UNSET:
            field_dict["pageOffset"] = page_offset
        if page_size is not UNSET:
            field_dict["pageSize"] = page_size

        return field_dict



    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.session_invoice_status_type import SessionInvoiceStatusType
        d = src_dict.copy()
        creation_timestamp = isoparse(d.pop("creationTimestamp"))




        entity_type = d.pop("entityType")

        last_update_timestamp = isoparse(d.pop("lastUpdateTimestamp"))




        processing_code = d.pop("processingCode")

        processing_description = d.pop("processingDescription")

        reference_number = d.pop("referenceNumber")

        timestamp = isoparse(d.pop("timestamp"))




        invoice_status_list = []
        _invoice_status_list = d.pop("invoiceStatusList", UNSET)
        for invoice_status_list_item_data in (_invoice_status_list or []):
            invoice_status_list_item = SessionInvoiceStatusType.from_dict(invoice_status_list_item_data)



            invoice_status_list.append(invoice_status_list_item)


        number_of_elements = d.pop("numberOfElements", UNSET)

        page_offset = d.pop("pageOffset", UNSET)

        page_size = d.pop("pageSize", UNSET)

        session_status_response = cls(
            creation_timestamp=creation_timestamp,
            entity_type=entity_type,
            last_update_timestamp=last_update_timestamp,
            processing_code=processing_code,
            processing_description=processing_description,
            reference_number=reference_number,
            timestamp=timestamp,
            invoice_status_list=invoice_status_list,
            number_of_elements=number_of_elements,
            page_offset=page_offset,
            page_size=page_size,
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
