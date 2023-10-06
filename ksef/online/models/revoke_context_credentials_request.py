from typing import Any, Dict, Type, TypeVar, Tuple, Optional, BinaryIO, TextIO, TYPE_CHECKING

from typing import List


from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from typing import Dict
from typing import cast

if TYPE_CHECKING:
  from ..models.revoke_context_credentials_request_type import RevokeContextCredentialsRequestType





T = TypeVar("T", bound="RevokeContextCredentialsRequest")


@_attrs_define
class RevokeContextCredentialsRequest:
    """ 
        Attributes:
            revoke_context_credentials (RevokeContextCredentialsRequestType):
     """

    revoke_context_credentials: 'RevokeContextCredentialsRequestType'
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)


    def to_dict(self) -> Dict[str, Any]:
        from ..models.revoke_context_credentials_request_type import RevokeContextCredentialsRequestType
        revoke_context_credentials = self.revoke_context_credentials.to_dict()


        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "revokeContextCredentials": revoke_context_credentials,
        })

        return field_dict



    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.revoke_context_credentials_request_type import RevokeContextCredentialsRequestType
        d = src_dict.copy()
        revoke_context_credentials = RevokeContextCredentialsRequestType.from_dict(d.pop("revokeContextCredentials"))




        revoke_context_credentials_request = cls(
            revoke_context_credentials=revoke_context_credentials,
        )

        revoke_context_credentials_request.additional_properties = d
        return revoke_context_credentials_request

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
