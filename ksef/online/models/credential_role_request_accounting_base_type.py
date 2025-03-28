from typing import Any, Dict, Type, TypeVar, Tuple, Optional, BinaryIO, TextIO, TYPE_CHECKING

from typing import List


from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from typing import Union
from ..types import UNSET, Unset
from ..models.credential_role_request_accounting_base_type_role_type import CredentialRoleRequestAccountingBaseTypeRoleType






T = TypeVar("T", bound="CredentialRoleRequestAccountingBaseType")


@_attrs_define
class CredentialRoleRequestAccountingBaseType:
    """ 
        Attributes:
            role_description (str):
            role_type (CredentialRoleRequestAccountingBaseTypeRoleType):
            description (Union[Unset, str]):
     """

    role_description: str
    role_type: CredentialRoleRequestAccountingBaseTypeRoleType
    description: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)


    def to_dict(self) -> Dict[str, Any]:
        role_description = self.role_description
        role_type = self.role_type.value

        description = self.description

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "roleDescription": role_description,
            "roleType": role_type,
        })
        if description is not UNSET:
            field_dict["description"] = description

        return field_dict



    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        role_description = d.pop("roleDescription")

        role_type = CredentialRoleRequestAccountingBaseTypeRoleType(d.pop("roleType"))




        description = d.pop("description", UNSET)

        credential_role_request_accounting_base_type = cls(
            role_description=role_description,
            role_type=role_type,
            description=description,
        )

        credential_role_request_accounting_base_type.additional_properties = d
        return credential_role_request_accounting_base_type

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
