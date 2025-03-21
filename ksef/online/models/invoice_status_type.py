from typing import Any, Dict, Type, TypeVar, Tuple, Optional, BinaryIO, TextIO, TYPE_CHECKING

from typing import List


from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from typing import Union
from dateutil.parser import isoparse
from typing import cast
import datetime
from ..types import UNSET, Unset






T = TypeVar("T", bound="InvoiceStatusType")


@_attrs_define
class InvoiceStatusType:
    """ 
        Attributes:
            acquisition_timestamp (Union[Unset, datetime.datetime]):
            invoice_number (Union[Unset, str]):
            ksef_reference_number (Union[Unset, str]):
     """

    acquisition_timestamp: Union[Unset, datetime.datetime] = UNSET
    invoice_number: Union[Unset, str] = UNSET
    ksef_reference_number: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)


    def to_dict(self) -> Dict[str, Any]:
        acquisition_timestamp: Union[Unset, str] = UNSET
        if not isinstance(self.acquisition_timestamp, Unset):
            acquisition_timestamp = self.acquisition_timestamp.isoformat()

        invoice_number = self.invoice_number
        ksef_reference_number = self.ksef_reference_number

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if acquisition_timestamp is not UNSET:
            field_dict["acquisitionTimestamp"] = acquisition_timestamp
        if invoice_number is not UNSET:
            field_dict["invoiceNumber"] = invoice_number
        if ksef_reference_number is not UNSET:
            field_dict["ksefReferenceNumber"] = ksef_reference_number

        return field_dict



    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        _acquisition_timestamp = d.pop("acquisitionTimestamp", UNSET)
        acquisition_timestamp: Union[Unset, datetime.datetime]
        if isinstance(_acquisition_timestamp,  Unset):
            acquisition_timestamp = UNSET
        else:
            acquisition_timestamp = isoparse(_acquisition_timestamp)




        invoice_number = d.pop("invoiceNumber", UNSET)

        ksef_reference_number = d.pop("ksefReferenceNumber", UNSET)

        invoice_status_type = cls(
            acquisition_timestamp=acquisition_timestamp,
            invoice_number=invoice_number,
            ksef_reference_number=ksef_reference_number,
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
