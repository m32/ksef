from typing import Any, Dict, Type, TypeVar, Tuple, Optional, BinaryIO, TextIO, TYPE_CHECKING

from typing import List


from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from typing import Dict
from typing import cast

if TYPE_CHECKING:
  from ..models.invoice_query_details_type import InvoiceQueryDetailsType





T = TypeVar("T", bound="InvoiceRequestKSeF")


@_attrs_define
class InvoiceRequestKSeF:
    """ 
        Attributes:
            invoice_details (InvoiceQueryDetailsType):
            ksef_reference_number (str):
     """

    invoice_details: 'InvoiceQueryDetailsType'
    ksef_reference_number: str
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)


    def to_dict(self) -> Dict[str, Any]:
        from ..models.invoice_query_details_type import InvoiceQueryDetailsType
        invoice_details = self.invoice_details.to_dict()

        ksef_reference_number = self.ksef_reference_number

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "invoiceDetails": invoice_details,
            "ksefReferenceNumber": ksef_reference_number,
        })

        return field_dict



    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.invoice_query_details_type import InvoiceQueryDetailsType
        d = src_dict.copy()
        invoice_details = InvoiceQueryDetailsType.from_dict(d.pop("invoiceDetails"))




        ksef_reference_number = d.pop("ksefReferenceNumber")

        invoice_request_k_se_f = cls(
            invoice_details=invoice_details,
            ksef_reference_number=ksef_reference_number,
        )

        invoice_request_k_se_f.additional_properties = d
        return invoice_request_k_se_f

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
