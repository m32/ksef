from typing import Any, Dict, List, Type, TypeVar

import attr

from ..models.grant_credentials_request_type import GrantCredentialsRequestType

T = TypeVar("T", bound="GrantCredentialsRequest")


@attr.s(auto_attribs=True)
class GrantCredentialsRequest:
    """
    Attributes:
        grant_credentials (GrantCredentialsRequestType):
    """

    grant_credentials: GrantCredentialsRequestType
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        grant_credentials = self.grant_credentials.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "grantCredentials": grant_credentials,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        grant_credentials = GrantCredentialsRequestType.from_dict(d.pop("grantCredentials"))

        grant_credentials_request = cls(
            grant_credentials=grant_credentials,
        )

        grant_credentials_request.additional_properties = d
        return grant_credentials_request

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
