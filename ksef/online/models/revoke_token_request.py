from typing import Any, Dict, Type, TypeVar, Tuple, Optional, BinaryIO, TextIO, TYPE_CHECKING

from typing import List


from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from typing import Dict
from typing import cast

if TYPE_CHECKING:
  from ..models.revoke_token_request_type import RevokeTokenRequestType





T = TypeVar("T", bound="RevokeTokenRequest")


@_attrs_define
class RevokeTokenRequest:
    """ 
        Attributes:
            revoke_token (RevokeTokenRequestType):
     """

    revoke_token: 'RevokeTokenRequestType'
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)


    def to_dict(self) -> Dict[str, Any]:
        from ..models.revoke_token_request_type import RevokeTokenRequestType
        revoke_token = self.revoke_token.to_dict()


        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "revokeToken": revoke_token,
        })

        return field_dict



    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.revoke_token_request_type import RevokeTokenRequestType
        d = src_dict.copy()
        revoke_token = RevokeTokenRequestType.from_dict(d.pop("revokeToken"))




        revoke_token_request = cls(
            revoke_token=revoke_token,
        )

        revoke_token_request.additional_properties = d
        return revoke_token_request

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
