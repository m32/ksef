from typing import Any, Dict, Type, TypeVar, Tuple, Optional, BinaryIO, TextIO, TYPE_CHECKING

from typing import List


from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from typing import Dict
from io import BytesIO
from typing import cast
from ..types import File, FileJsonType

if TYPE_CHECKING:
  from ..models.file_2mb_hash_type import File2MBHashType





T = TypeVar("T", bound="InvoicePayloadEncryptedType")


@_attrs_define
class InvoicePayloadEncryptedType:
    """ 
        Attributes:
            type (str):
            encrypted_invoice_body (File):
            encrypted_invoice_hash (File2MBHashType):
     """

    type: str
    encrypted_invoice_body: File
    encrypted_invoice_hash: 'File2MBHashType'
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)


    def to_dict(self) -> Dict[str, Any]:
        from ..models.file_2mb_hash_type import File2MBHashType
        type = self.type
        encrypted_invoice_body = self.encrypted_invoice_body.to_tuple()

        encrypted_invoice_hash = self.encrypted_invoice_hash.to_dict()


        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "type": type,
            "encryptedInvoiceBody": encrypted_invoice_body,
            "encryptedInvoiceHash": encrypted_invoice_hash,
        })

        return field_dict



    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.file_2mb_hash_type import File2MBHashType
        d = src_dict.copy()
        type = d.pop("type")

        encrypted_invoice_body = File(
             payload = BytesIO(d.pop("encryptedInvoiceBody"))
        )




        encrypted_invoice_hash = File2MBHashType.from_dict(d.pop("encryptedInvoiceHash"))




        invoice_payload_encrypted_type = cls(
            type=type,
            encrypted_invoice_body=encrypted_invoice_body,
            encrypted_invoice_hash=encrypted_invoice_hash,
        )

        invoice_payload_encrypted_type.additional_properties = d
        return invoice_payload_encrypted_type

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
