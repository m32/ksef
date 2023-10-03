from typing import Any, Dict, List, Type, TypeVar

import attr

from ..models.credentials_identifier_request_type import CredentialsIdentifierRequestType

T = TypeVar("T", bound="RevokeTokenRequestType")


@attr.s(auto_attribs=True)
class RevokeTokenRequestType:
    """
    Attributes:
        source_token_identifier (CredentialsIdentifierRequestType):
        token_number (str):
    """

    source_token_identifier: CredentialsIdentifierRequestType
    token_number: str
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        source_token_identifier = self.source_token_identifier.to_dict()

        token_number = self.token_number

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "sourceTokenIdentifier": source_token_identifier,
                "tokenNumber": token_number,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
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
