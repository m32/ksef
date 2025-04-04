from typing import Any, Dict, Type, TypeVar, Tuple, Optional, BinaryIO, TextIO, TYPE_CHECKING

from typing import List


from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset







T = TypeVar("T", bound="ShowInvoiceRequestType")


@_attrs_define
class ShowInvoiceRequestType:
    """ 
        Attributes:
            hiding_cancelation_reason (str):
            ksef_reference_number (str):
     """

    hiding_cancelation_reason: str
    ksef_reference_number: str
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)


    def to_dict(self) -> Dict[str, Any]:
        hiding_cancelation_reason = self.hiding_cancelation_reason
        ksef_reference_number = self.ksef_reference_number

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "hidingCancelationReason": hiding_cancelation_reason,
            "ksefReferenceNumber": ksef_reference_number,
        })

        return field_dict



    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        hiding_cancelation_reason = d.pop("hidingCancelationReason")

        ksef_reference_number = d.pop("ksefReferenceNumber")

        show_invoice_request_type = cls(
            hiding_cancelation_reason=hiding_cancelation_reason,
            ksef_reference_number=ksef_reference_number,
        )

        show_invoice_request_type.additional_properties = d
        return show_invoice_request_type

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
