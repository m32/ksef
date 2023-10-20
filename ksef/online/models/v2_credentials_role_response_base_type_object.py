from typing import Any, Dict, Type, TypeVar, Tuple, Optional, BinaryIO, TextIO, TYPE_CHECKING

from typing import List


from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from typing import Union
from typing import cast
from ..types import UNSET, Unset
from typing import Dict

if TYPE_CHECKING:
  from ..models.v2_credentials_role_response_base_type_object_role_type import V2CredentialsRoleResponseBaseTypeObjectRoleType





T = TypeVar("T", bound="V2CredentialsRoleResponseBaseTypeObject")


@_attrs_define
class V2CredentialsRoleResponseBaseTypeObject:
    """ 
        Attributes:
            type (str):
            role_description (Union[Unset, str]):
            role_type (Union[Unset, V2CredentialsRoleResponseBaseTypeObjectRoleType]):
     """

    type: str
    role_description: Union[Unset, str] = UNSET
    role_type: Union[Unset, 'V2CredentialsRoleResponseBaseTypeObjectRoleType'] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)


    def to_dict(self) -> Dict[str, Any]:
        from ..models.v2_credentials_role_response_base_type_object_role_type import V2CredentialsRoleResponseBaseTypeObjectRoleType
        type = self.type
        role_description = self.role_description
        role_type: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.role_type, Unset):
            role_type = self.role_type.to_dict()


        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "type": type,
        })
        if role_description is not UNSET:
            field_dict["roleDescription"] = role_description
        if role_type is not UNSET:
            field_dict["roleType"] = role_type

        return field_dict



    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.v2_credentials_role_response_base_type_object_role_type import V2CredentialsRoleResponseBaseTypeObjectRoleType
        d = src_dict.copy()
        type = d.pop("type")

        role_description = d.pop("roleDescription", UNSET)

        _role_type = d.pop("roleType", UNSET)
        role_type: Union[Unset, V2CredentialsRoleResponseBaseTypeObjectRoleType]
        if isinstance(_role_type,  Unset):
            role_type = UNSET
        else:
            role_type = V2CredentialsRoleResponseBaseTypeObjectRoleType.from_dict(_role_type)




        v2_credentials_role_response_base_type_object = cls(
            type=type,
            role_description=role_description,
            role_type=role_type,
        )

        v2_credentials_role_response_base_type_object.additional_properties = d
        return v2_credentials_role_response_base_type_object

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
