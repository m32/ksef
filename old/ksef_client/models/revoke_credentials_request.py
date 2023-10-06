from typing import Any, Dict, List, Type, TypeVar

import attr

from ..models.revoke_credentials_request_type import RevokeCredentialsRequestType

T = TypeVar("T", bound="RevokeCredentialsRequest")


@attr.s(auto_attribs=True)
class RevokeCredentialsRequest:
    """
    Attributes:
        revoke_credentials (RevokeCredentialsRequestType):
    """

    revoke_credentials: RevokeCredentialsRequestType
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        revoke_credentials = self.revoke_credentials.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "revokeCredentials": revoke_credentials,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
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
