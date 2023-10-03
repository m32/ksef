from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.credentials_role_response_base_type_object_role_type import CredentialsRoleResponseBaseTypeObjectRoleType
from ..types import UNSET, Unset

T = TypeVar("T", bound="CredentialsRoleResponseBaseTypeObject")


@attr.s(auto_attribs=True)
class CredentialsRoleResponseBaseTypeObject:
    """
    Attributes:
        type (str):
        role_type (Union[Unset, CredentialsRoleResponseBaseTypeObjectRoleType]):
        role_description (Union[Unset, str]):
    """

    type: str
    role_type: Union[Unset, CredentialsRoleResponseBaseTypeObjectRoleType] = UNSET
    role_description: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        type = self.type
        role_type: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.role_type, Unset):
            role_type = self.role_type.to_dict()

        role_description = self.role_description

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "type": type,
            }
        )
        if role_type is not UNSET:
            field_dict["roleType"] = role_type
        if role_description is not UNSET:
            field_dict["roleDescription"] = role_description

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        type = d.pop("type")

        _role_type = d.pop("roleType", UNSET)
        role_type: Union[Unset, CredentialsRoleResponseBaseTypeObjectRoleType]
        if isinstance(_role_type, Unset):
            role_type = UNSET
        else:
            role_type = CredentialsRoleResponseBaseTypeObjectRoleType.from_dict(_role_type)

        role_description = d.pop("roleDescription", UNSET)

        credentials_role_response_base_type_object = cls(
            type=type,
            role_type=role_type,
            role_description=role_description,
        )

        credentials_role_response_base_type_object.additional_properties = d
        return credentials_role_response_base_type_object

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
