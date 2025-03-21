from typing import Any, Dict, Type, TypeVar, Tuple, Optional, BinaryIO, TextIO, TYPE_CHECKING

from typing import List


from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset







T = TypeVar("T", bound="HideInvoiceRequestType")


@_attrs_define
class HideInvoiceRequestType:
    """ 
        Attributes:
            hiding_reason (str):
            ksef_reference_number (str):
     """

    hiding_reason: str
    ksef_reference_number: str
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)


    def to_dict(self) -> Dict[str, Any]:
        hiding_reason = self.hiding_reason
        ksef_reference_number = self.ksef_reference_number

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "hidingReason": hiding_reason,
            "ksefReferenceNumber": ksef_reference_number,
        })

        return field_dict



    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        hiding_reason = d.pop("hidingReason")

        ksef_reference_number = d.pop("ksefReferenceNumber")

        hide_invoice_request_type = cls(
            hiding_reason=hiding_reason,
            ksef_reference_number=ksef_reference_number,
        )

        hide_invoice_request_type.additional_properties = d
        return hide_invoice_request_type

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
