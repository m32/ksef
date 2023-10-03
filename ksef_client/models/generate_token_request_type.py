from typing import Any, Dict, List, Type, TypeVar

import attr

from ..models.credentials_role_request_token_type import CredentialsRoleRequestTokenType

T = TypeVar("T", bound="GenerateTokenRequestType")


@attr.s(auto_attribs=True)
class GenerateTokenRequestType:
    """
    Attributes:
        description (str):
        credentials_role_list (List[CredentialsRoleRequestTokenType]):
    """

    description: str
    credentials_role_list: List[CredentialsRoleRequestTokenType]
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        description = self.description
        credentials_role_list = []
        for credentials_role_list_item_data in self.credentials_role_list:
            credentials_role_list_item = credentials_role_list_item_data.to_dict()

            credentials_role_list.append(credentials_role_list_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "description": description,
                "credentialsRoleList": credentials_role_list,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        description = d.pop("description")

        credentials_role_list = []
        _credentials_role_list = d.pop("credentialsRoleList")
        for credentials_role_list_item_data in _credentials_role_list:
            credentials_role_list_item = CredentialsRoleRequestTokenType.from_dict(credentials_role_list_item_data)

            credentials_role_list.append(credentials_role_list_item)

        generate_token_request_type = cls(
            description=description,
            credentials_role_list=credentials_role_list,
        )

        generate_token_request_type.additional_properties = d
        return generate_token_request_type

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
