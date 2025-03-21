from typing import Any, Dict, Type, TypeVar, Tuple, Optional, BinaryIO, TextIO, TYPE_CHECKING

from typing import List


from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from typing import Union
from ..types import UNSET, Unset






T = TypeVar("T", bound="ScamInvoiceStatusResponse")


@_attrs_define
class ScamInvoiceStatusResponse:
    """ 
        Attributes:
            active_scam_report (bool):
            ksef_reference_number (str):
            reason (Union[Unset, str]):
            timestamp (Union[Unset, str]):
     """

    active_scam_report: bool
    ksef_reference_number: str
    reason: Union[Unset, str] = UNSET
    timestamp: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)


    def to_dict(self) -> Dict[str, Any]:
        active_scam_report = self.active_scam_report
        ksef_reference_number = self.ksef_reference_number
        reason = self.reason
        timestamp = self.timestamp

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "activeScamReport": active_scam_report,
            "ksefReferenceNumber": ksef_reference_number,
        })
        if reason is not UNSET:
            field_dict["reason"] = reason
        if timestamp is not UNSET:
            field_dict["timestamp"] = timestamp

        return field_dict



    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        active_scam_report = d.pop("activeScamReport")

        ksef_reference_number = d.pop("ksefReferenceNumber")

        reason = d.pop("reason", UNSET)

        timestamp = d.pop("timestamp", UNSET)

        scam_invoice_status_response = cls(
            active_scam_report=active_scam_report,
            ksef_reference_number=ksef_reference_number,
            reason=reason,
            timestamp=timestamp,
        )

        scam_invoice_status_response.additional_properties = d
        return scam_invoice_status_response

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
