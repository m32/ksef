from typing import Any, Dict, Type, TypeVar, Tuple, Optional, BinaryIO, TextIO, TYPE_CHECKING

from typing import List


from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from typing import cast
from typing import Dict

if TYPE_CHECKING:
  from ..models.revoke_credentials_request_type import RevokeCredentialsRequestType





T = TypeVar("T", bound="RevokeCredentialsRequest")


@_attrs_define
class RevokeCredentialsRequest:
    """ 
        Attributes:
            revoke_credentials (RevokeCredentialsRequestType):
     """

    revoke_credentials: 'RevokeCredentialsRequestType'
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)


    def to_dict(self) -> Dict[str, Any]:
        from ..models.revoke_credentials_request_type import RevokeCredentialsRequestType
        revoke_credentials = self.revoke_credentials.to_dict()


        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "revokeCredentials": revoke_credentials,
        })

        return field_dict



    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.revoke_credentials_request_type import RevokeCredentialsRequestType
        d = src_dict.copy()
        revoke_credentials = RevokeCredentialsRequestType.from_dict(d.pop("revokeCredentials"))




        revoke_credentials_request = cls(
            revoke_credentials=revoke_credentials,
        )

        revoke_credentials_request.additional_properties = d
        return revoke_credentials_request

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
