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






T = TypeVar("T", bound="VisibilityInvoiceGetResponseType")


@_attrs_define
class VisibilityInvoiceGetResponseType:
    """ 
        Attributes:
            ksef_reference_number (str):
            is_hidden (Union[Unset, bool]):
            reason (Union[Unset, str]):
            timestamp (Union[Unset, datetime.datetime]):
     """

    ksef_reference_number: str
    is_hidden: Union[Unset, bool] = UNSET
    reason: Union[Unset, str] = UNSET
    timestamp: Union[Unset, datetime.datetime] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)


    def to_dict(self) -> Dict[str, Any]:
        ksef_reference_number = self.ksef_reference_number
        is_hidden = self.is_hidden
        reason = self.reason
        timestamp: Union[Unset, str] = UNSET
        if not isinstance(self.timestamp, Unset):
            timestamp = self.timestamp.isoformat()


        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "ksefReferenceNumber": ksef_reference_number,
        })
        if is_hidden is not UNSET:
            field_dict["isHidden"] = is_hidden
        if reason is not UNSET:
            field_dict["reason"] = reason
        if timestamp is not UNSET:
            field_dict["timestamp"] = timestamp

        return field_dict



    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        ksef_reference_number = d.pop("ksefReferenceNumber")

        is_hidden = d.pop("isHidden", UNSET)

        reason = d.pop("reason", UNSET)

        _timestamp = d.pop("timestamp", UNSET)
        timestamp: Union[Unset, datetime.datetime]
        if isinstance(_timestamp,  Unset):
            timestamp = UNSET
        else:
            timestamp = isoparse(_timestamp)




        visibility_invoice_get_response_type = cls(
            ksef_reference_number=ksef_reference_number,
            is_hidden=is_hidden,
            reason=reason,
            timestamp=timestamp,
        )

        visibility_invoice_get_response_type.additional_properties = d
        return visibility_invoice_get_response_type

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
