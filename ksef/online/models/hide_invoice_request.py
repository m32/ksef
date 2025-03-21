from typing import Any, Dict, Type, TypeVar, Tuple, Optional, BinaryIO, TextIO, TYPE_CHECKING

from typing import List


from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from typing import Dict
from typing import cast

if TYPE_CHECKING:
  from ..models.hide_invoice_request_type import HideInvoiceRequestType





T = TypeVar("T", bound="HideInvoiceRequest")


@_attrs_define
class HideInvoiceRequest:
    """ 
        Attributes:
            invoice_hide_request (HideInvoiceRequestType):
     """

    invoice_hide_request: 'HideInvoiceRequestType'
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)


    def to_dict(self) -> Dict[str, Any]:
        from ..models.hide_invoice_request_type import HideInvoiceRequestType
        invoice_hide_request = self.invoice_hide_request.to_dict()


        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "invoiceHideRequest": invoice_hide_request,
        })

        return field_dict



    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.hide_invoice_request_type import HideInvoiceRequestType
        d = src_dict.copy()
        invoice_hide_request = HideInvoiceRequestType.from_dict(d.pop("invoiceHideRequest"))




        hide_invoice_request = cls(
            invoice_hide_request=invoice_hide_request,
        )

        hide_invoice_request.additional_properties = d
        return hide_invoice_request

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
