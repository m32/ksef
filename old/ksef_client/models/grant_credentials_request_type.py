from typing import Any, Dict, List, Type, TypeVar

import attr

from ..models.credentials_identifier_request_type import CredentialsIdentifierRequestType
from ..models.credentials_role_request_standard_described_type import CredentialsRoleRequestStandardDescribedType

T = TypeVar("T", bound="GrantCredentialsRequestType")


@attr.s(auto_attribs=True)
class GrantCredentialsRequestType:
    """
    Attributes:
        credentials_identifier (CredentialsIdentifierRequestType):
        description (str):
        credentials_role_list (List[CredentialsRoleRequestStandardDescribedType]):
    """

    credentials_identifier: CredentialsIdentifierRequestType
    description: str
    credentials_role_list: List[CredentialsRoleRequestStandardDescribedType]
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        credentials_identifier = self.credentials_identifier.to_dict()

        description = self.description
        credentials_role_list = []
        for credentials_role_list_item_data in self.credentials_role_list:
            credentials_role_list_item = credentials_role_list_item_data.to_dict()

            credentials_role_list.append(credentials_role_list_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "credentialsIdentifier": credentials_identifier,
                "description": description,
                "credentialsRoleList": credentials_role_list,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        credentials_identifier = CredentialsIdentifierRequestType.from_dict(d.pop("credentialsIdentifier"))

        description = d.pop("description")

        credentials_role_list = []
        _credentials_role_list = d.pop("credentialsRoleList")
        for credentials_role_list_item_data in _credentials_role_list:
            credentials_role_list_item = CredentialsRoleRequestStandardDescribedType.from_dict(
                credentials_role_list_item_data
            )

            credentials_role_list.append(credentials_role_list_item)

        grant_credentials_request_type = cls(
            credentials_identifier=credentials_identifier,
            description=description,
            credentials_role_list=credentials_role_list,
        )

        grant_credentials_request_type.additional_properties = d
        return grant_credentials_request_type

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
