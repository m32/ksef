from typing import Any, Dict, Type, TypeVar, Tuple, Optional, BinaryIO, TextIO, TYPE_CHECKING

from typing import List


from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from typing import cast
import datetime
from dateutil.parser import isoparse
from typing import Dict

if TYPE_CHECKING:
  from ..models.package_signature_init_response_type import PackageSignatureInitResponseType





T = TypeVar("T", bound="InitResponse")


@_attrs_define
class InitResponse:
    """ 
        Attributes:
            package_signature (PackageSignatureInitResponseType):
            reference_number (str):
            timestamp (datetime.datetime):
     """

    package_signature: 'PackageSignatureInitResponseType'
    reference_number: str
    timestamp: datetime.datetime
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)


    def to_dict(self) -> Dict[str, Any]:
        from ..models.package_signature_init_response_type import PackageSignatureInitResponseType
        package_signature = self.package_signature.to_dict()

        reference_number = self.reference_number
        timestamp = self.timestamp.isoformat()


        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "packageSignature": package_signature,
            "referenceNumber": reference_number,
            "timestamp": timestamp,
        })

        return field_dict



    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.package_signature_init_response_type import PackageSignatureInitResponseType
        d = src_dict.copy()
        package_signature = PackageSignatureInitResponseType.from_dict(d.pop("packageSignature"))




        reference_number = d.pop("referenceNumber")

        timestamp = isoparse(d.pop("timestamp"))




        init_response = cls(
            package_signature=package_signature,
            reference_number=reference_number,
            timestamp=timestamp,
        )

        init_response.additional_properties = d
        return init_response

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
