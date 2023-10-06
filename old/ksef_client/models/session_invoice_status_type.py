import datetime
from typing import Any, Dict, List, Type, TypeVar, Union

import attr
from dateutil.parser import isoparse

from ..types import UNSET, Unset

T = TypeVar("T", bound="SessionInvoiceStatusType")


@attr.s(auto_attribs=True)
class SessionInvoiceStatusType:
    """
    Attributes:
        processing_code (int):
        processing_description (str):
        element_reference_number (str):
        invoice_number (Union[Unset, str]):
        ksef_reference_number (Union[Unset, str]):
        acquisition_timestamp (Union[Unset, datetime.datetime]):
    """

    processing_code: int
    processing_description: str
    element_reference_number: str
    invoice_number: Union[Unset, str] = UNSET
    ksef_reference_number: Union[Unset, str] = UNSET
    acquisition_timestamp: Union[Unset, datetime.datetime] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        processing_code = self.processing_code
        processing_description = self.processing_description
        element_reference_number = self.element_reference_number
        invoice_number = self.invoice_number
        ksef_reference_number = self.ksef_reference_number
        acquisition_timestamp: Union[Unset, str] = UNSET
        if not isinstance(self.acquisition_timestamp, Unset):
            acquisition_timestamp = self.acquisition_timestamp.isoformat()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "processingCode": processing_code,
                "processingDescription": processing_description,
                "elementReferenceNumber": element_reference_number,
            }
        )
        if invoice_number is not UNSET:
            field_dict["invoiceNumber"] = invoice_number
        if ksef_reference_number is not UNSET:
            field_dict["ksefReferenceNumber"] = ksef_reference_number
        if acquisition_timestamp is not UNSET:
            field_dict["acquisitionTimestamp"] = acquisition_timestamp

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        processing_code = d.pop("processingCode")

        processing_description = d.pop("processingDescription")

        element_reference_number = d.pop("elementReferenceNumber")

        invoice_number = d.pop("invoiceNumber", UNSET)

        ksef_reference_number = d.pop("ksefReferenceNumber", UNSET)

        _acquisition_timestamp = d.pop("acquisitionTimestamp", UNSET)
        acquisition_timestamp: Union[Unset, datetime.datetime]
        if isinstance(_acquisition_timestamp, Unset):
            acquisition_timestamp = UNSET
        else:
            acquisition_timestamp = isoparse(_acquisition_timestamp)

        session_invoice_status_type = cls(
            processing_code=processing_code,
            processing_description=processing_description,
            element_reference_number=element_reference_number,
            invoice_number=invoice_number,
            ksef_reference_number=ksef_reference_number,
            acquisition_timestamp=acquisition_timestamp,
        )

        session_invoice_status_type.additional_properties = d
        return session_invoice_status_type

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
