from typing import Any, Dict, List, Type, TypeVar

import attr

from ..models.credentials_role_request_standard_described_type_role_type import (
    CredentialsRoleRequestStandardDescribedTypeRoleType,
)

T = TypeVar("T", bound="CredentialsRoleRequestStandardDescribedType")


@attr.s(auto_attribs=True)
class CredentialsRoleRequestStandardDescribedType:
    """
    Attributes:
        role_type (CredentialsRoleRequestStandardDescribedTypeRoleType):
        role_description (str):
    """

    role_type: CredentialsRoleRequestStandardDescribedTypeRoleType
    role_description: str
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        role_type = self.role_type.value

        role_description = self.role_description

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "roleType": role_type,
                "roleDescription": role_description,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        role_type = CredentialsRoleRequestStandardDescribedTypeRoleType(d.pop("roleType"))

        role_description = d.pop("roleDescription")

        credentials_role_request_standard_described_type = cls(
            role_type=role_type,
            role_description=role_description,
        )

        credentials_role_request_standard_described_type.additional_properties = d
        return credentials_role_request_standard_described_type

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
