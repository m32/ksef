import datetime
from typing import Any, Dict, List, Type, TypeVar, Union

import attr
from dateutil.parser import isoparse

from ..types import UNSET, Unset

T = TypeVar("T", bound="InvoiceStatusType")


@attr.s(auto_attribs=True)
class InvoiceStatusType:
    """
    Attributes:
        invoice_number (Union[Unset, str]):
        ksef_reference_number (Union[Unset, str]):
        acquisition_timestamp (Union[Unset, datetime.datetime]):
    """

    invoice_number: Union[Unset, str] = UNSET
    ksef_reference_number: Union[Unset, str] = UNSET
    acquisition_timestamp: Union[Unset, datetime.datetime] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        invoice_number = self.invoice_number
        ksef_reference_number = self.ksef_reference_number
        acquisition_timestamp: Union[Unset, str] = UNSET
        if not isinstance(self.acquisition_timestamp, Unset):
            acquisition_timestamp = self.acquisition_timestamp.isoformat()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
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
        invoice_number = d.pop("invoiceNumber", UNSET)

        ksef_reference_number = d.pop("ksefReferenceNumber", UNSET)

        _acquisition_timestamp = d.pop("acquisitionTimestamp", UNSET)
        acquisition_timestamp: Union[Unset, datetime.datetime]
        if isinstance(_acquisition_timestamp, Unset):
            acquisition_timestamp = UNSET
        else:
            acquisition_timestamp = isoparse(_acquisition_timestamp)

        invoice_status_type = cls(
            invoice_number=invoice_number,
            ksef_reference_number=ksef_reference_number,
            acquisition_timestamp=acquisition_timestamp,
        )

        invoice_status_type.additional_properties = d
        return invoice_status_type

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
