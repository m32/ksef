from typing import Any, Dict, List, Type, TypeVar

import attr

from ..models.file_1mb_hash_type import File1MBHashType
from ..models.invoice_payload_type import InvoicePayloadType

T = TypeVar("T", bound="SendInvoiceRequest")


@attr.s(auto_attribs=True)
class SendInvoiceRequest:
    """
    Attributes:
        invoice_hash (File1MBHashType):
        invoice_payload (InvoicePayloadType):
    """

    invoice_hash: File1MBHashType
    invoice_payload: InvoicePayloadType
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        invoice_hash = self.invoice_hash.to_dict()

        invoice_payload = self.invoice_payload.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "invoiceHash": invoice_hash,
                "invoicePayload": invoice_payload,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
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
