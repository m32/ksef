from typing import Any, Dict, Type, TypeVar, Tuple, Optional, BinaryIO, TextIO, TYPE_CHECKING

from typing import List


from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from typing import Dict
from typing import cast

if TYPE_CHECKING:
  from ..models.hash_sha_type import HashSHAType





T = TypeVar("T", bound="InvoiceVerificationRequest")


@_attrs_define
class InvoiceVerificationRequest:
    """ 
        Attributes:
            hash_sha (HashSHAType):
     """

    hash_sha: 'HashSHAType'
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)


    def to_dict(self) -> Dict[str, Any]:
        from ..models.hash_sha_type import HashSHAType
        hash_sha = self.hash_sha.to_dict()


        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "hashSHA": hash_sha,
        })

        return field_dict



    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.hash_sha_type import HashSHAType
        d = src_dict.copy()
        hash_sha = HashSHAType.from_dict(d.pop("hashSHA"))




        invoice_verification_request = cls(
            hash_sha=hash_sha,
        )

        invoice_verification_request.additional_properties = d
        return invoice_verification_request

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
