from typing import Any, Dict, Type, TypeVar, Tuple, Optional, BinaryIO, TextIO, TYPE_CHECKING

from typing import List


from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from typing import Dict
from typing import cast

if TYPE_CHECKING:
  from ..models.credentials_identifier_request_type import CredentialsIdentifierRequestType





T = TypeVar("T", bound="RevokeTokenRequestType")


@_attrs_define
class RevokeTokenRequestType:
    """ 
        Attributes:
            source_token_identifier (CredentialsIdentifierRequestType):
            token_number (str):
     """

    source_token_identifier: 'CredentialsIdentifierRequestType'
    token_number: str
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)


    def to_dict(self) -> Dict[str, Any]:
        from ..models.credentials_identifier_request_type import CredentialsIdentifierRequestType
        source_token_identifier = self.source_token_identifier.to_dict()

        token_number = self.token_number

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "sourceTokenIdentifier": source_token_identifier,
            "tokenNumber": token_number,
        })

        return field_dict



    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.credentials_identifier_request_type import CredentialsIdentifierRequestType
        d = src_dict.copy()
        source_token_identifier = CredentialsIdentifierRequestType.from_dict(d.pop("sourceTokenIdentifier"))




        token_number = d.pop("tokenNumber")

        revoke_token_request_type = cls(
            source_token_identifier=source_token_identifier,
            token_number=token_number,
        )

        revoke_token_request_type.additional_properties = d
        return revoke_token_request_type

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
