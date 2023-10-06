from typing import Any, Dict, Type, TypeVar, Tuple, Optional, BinaryIO, TextIO, TYPE_CHECKING

from typing import List


from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from typing import cast
from typing import Dict

if TYPE_CHECKING:
  from ..models.invoice_payload_type import InvoicePayloadType
  from ..models.file_1mb_hash_type import File1MBHashType





T = TypeVar("T", bound="SendInvoiceRequest")


@_attrs_define
class SendInvoiceRequest:
    """ 
        Attributes:
            invoice_hash (File1MBHashType):
            invoice_payload (InvoicePayloadType):
     """

    invoice_hash: 'File1MBHashType'
    invoice_payload: 'InvoicePayloadType'
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)


    def to_dict(self) -> Dict[str, Any]:
        from ..models.invoice_payload_type import InvoicePayloadType
        from ..models.file_1mb_hash_type import File1MBHashType
        invoice_hash = self.invoice_hash.to_dict()

        invoice_payload = self.invoice_payload.to_dict()


        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "invoiceHash": invoice_hash,
            "invoicePayload": invoice_payload,
        })

        return field_dict



    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.invoice_payload_type import InvoicePayloadType
        from ..models.file_1mb_hash_type import File1MBHashType
        d = src_dict.copy()
        invoice_hash = File1MBHashType.from_dict(d.pop("invoiceHash"))




        invoice_payload = InvoicePayloadType.from_dict(d.pop("invoicePayload"))




        send_invoice_request = cls(
            invoice_hash=invoice_hash,
            invoice_payload=invoice_payload,
        )

        send_invoice_request.additional_properties = d
        return send_invoice_request

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
