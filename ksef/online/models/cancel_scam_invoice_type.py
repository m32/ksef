from typing import Any, Dict, Type, TypeVar, Tuple, Optional, BinaryIO, TextIO, TYPE_CHECKING

from typing import List


from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset







T = TypeVar("T", bound="CancelScamInvoiceType")


@_attrs_define
class CancelScamInvoiceType:
    """ 
        Attributes:
            ksef_reference_number (str):
            report_cancelation_reason (str):
     """

    ksef_reference_number: str
    report_cancelation_reason: str
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)


    def to_dict(self) -> Dict[str, Any]:
        ksef_reference_number = self.ksef_reference_number
        report_cancelation_reason = self.report_cancelation_reason

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "ksefReferenceNumber": ksef_reference_number,
            "reportCancelationReason": report_cancelation_reason,
        })

        return field_dict



    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        ksef_reference_number = d.pop("ksefReferenceNumber")

        report_cancelation_reason = d.pop("reportCancelationReason")

        cancel_scam_invoice_type = cls(
            ksef_reference_number=ksef_reference_number,
            report_cancelation_reason=report_cancelation_reason,
        )

        cancel_scam_invoice_type.additional_properties = d
        return cancel_scam_invoice_type

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
