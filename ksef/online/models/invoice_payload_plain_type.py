from typing import Any, Dict, Type, TypeVar, Tuple, Optional, BinaryIO, TextIO, TYPE_CHECKING

from typing import List


from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from io import BytesIO
from ..types import File, FileJsonType






T = TypeVar("T", bound="InvoicePayloadPlainType")


@_attrs_define
class InvoicePayloadPlainType:
    """ 
        Attributes:
            type (str):
            invoice_body (File):
     """

    type: str
    invoice_body: File
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)


    def to_dict(self) -> Dict[str, Any]:
        type = self.type
        invoice_body = self.invoice_body.to_tuple()


        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "type": type,
            "invoiceBody": invoice_body,
        })

        return field_dict



    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        type = d.pop("type")

        invoice_body = File(
             payload = BytesIO(d.pop("invoiceBody"))
        )




        invoice_payload_plain_type = cls(
            type=type,
            invoice_body=invoice_body,
        )

        invoice_payload_plain_type.additional_properties = d
        return invoice_payload_plain_type

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
