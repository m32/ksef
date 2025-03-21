from typing import Any, Dict, Type, TypeVar, Tuple, Optional, BinaryIO, TextIO, TYPE_CHECKING

from typing import List


from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from typing import Union
from ..types import UNSET, Unset
from typing import cast
from typing import Dict

if TYPE_CHECKING:
  from ..models.cancel_scam_invoice_type import CancelScamInvoiceType





T = TypeVar("T", bound="CancelScamInvoiceRequest")


@_attrs_define
class CancelScamInvoiceRequest:
    """ 
        Attributes:
            scam_report_cancelation (Union[Unset, CancelScamInvoiceType]):
     """

    scam_report_cancelation: Union[Unset, 'CancelScamInvoiceType'] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)


    def to_dict(self) -> Dict[str, Any]:
        from ..models.cancel_scam_invoice_type import CancelScamInvoiceType
        scam_report_cancelation: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.scam_report_cancelation, Unset):
            scam_report_cancelation = self.scam_report_cancelation.to_dict()


        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if scam_report_cancelation is not UNSET:
            field_dict["scamReportCancelation"] = scam_report_cancelation

        return field_dict



    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.cancel_scam_invoice_type import CancelScamInvoiceType
        d = src_dict.copy()
        _scam_report_cancelation = d.pop("scamReportCancelation", UNSET)
        scam_report_cancelation: Union[Unset, CancelScamInvoiceType]
        if isinstance(_scam_report_cancelation,  Unset):
            scam_report_cancelation = UNSET
        else:
            scam_report_cancelation = CancelScamInvoiceType.from_dict(_scam_report_cancelation)




        cancel_scam_invoice_request = cls(
            scam_report_cancelation=scam_report_cancelation,
        )

        cancel_scam_invoice_request.additional_properties = d
        return cancel_scam_invoice_request

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
