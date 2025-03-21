from typing import Any, Dict, Type, TypeVar, Tuple, Optional, BinaryIO, TextIO, TYPE_CHECKING

from typing import List


from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from typing import Dict
from typing import cast

if TYPE_CHECKING:
  from ..models.hash_sha_type import HashSHAType
  from ..models.anonymous_subject_identifier_to_type import AnonymousSubjectIdentifierToType





T = TypeVar("T", bound="InvoiceDownloadRequest")


@_attrs_define
class InvoiceDownloadRequest:
    """ 
        Attributes:
            due_value (str):
            hash_sha (HashSHAType):
            invoice_number (str):
            subject_to (AnonymousSubjectIdentifierToType):
     """

    due_value: str
    hash_sha: 'HashSHAType'
    invoice_number: str
    subject_to: 'AnonymousSubjectIdentifierToType'
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)


    def to_dict(self) -> Dict[str, Any]:
        from ..models.hash_sha_type import HashSHAType
        from ..models.anonymous_subject_identifier_to_type import AnonymousSubjectIdentifierToType
        due_value = self.due_value
        hash_sha = self.hash_sha.to_dict()

        invoice_number = self.invoice_number
        subject_to = self.subject_to.to_dict()


        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "dueValue": due_value,
            "hashSHA": hash_sha,
            "invoiceNumber": invoice_number,
            "subjectTo": subject_to,
        })

        return field_dict



    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.hash_sha_type import HashSHAType
        from ..models.anonymous_subject_identifier_to_type import AnonymousSubjectIdentifierToType
        d = src_dict.copy()
        due_value = d.pop("dueValue")

        hash_sha = HashSHAType.from_dict(d.pop("hashSHA"))




        invoice_number = d.pop("invoiceNumber")

        subject_to = AnonymousSubjectIdentifierToType.from_dict(d.pop("subjectTo"))




        invoice_download_request = cls(
            due_value=due_value,
            hash_sha=hash_sha,
            invoice_number=invoice_number,
            subject_to=subject_to,
        )

        invoice_download_request.additional_properties = d
        return invoice_download_request

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
