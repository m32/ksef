from typing import Any, Dict, Type, TypeVar, Tuple, Optional, BinaryIO, TextIO, TYPE_CHECKING

from typing import List


from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from typing import Dict
from typing import cast, List
from typing import cast

if TYPE_CHECKING:
  from ..models.credentials_role_request_token_type import CredentialsRoleRequestTokenType





T = TypeVar("T", bound="GenerateTokenRequestType")


@_attrs_define
class GenerateTokenRequestType:
    """ 
        Attributes:
            credentials_role_list (List['CredentialsRoleRequestTokenType']):
            description (str):
     """

    credentials_role_list: List['CredentialsRoleRequestTokenType']
    description: str
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)


    def to_dict(self) -> Dict[str, Any]:
        from ..models.credentials_role_request_token_type import CredentialsRoleRequestTokenType
        credentials_role_list = []
        for credentials_role_list_item_data in self.credentials_role_list:
            credentials_role_list_item = credentials_role_list_item_data.to_dict()

            credentials_role_list.append(credentials_role_list_item)




        description = self.description

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "credentialsRoleList": credentials_role_list,
            "description": description,
        })

        return field_dict



    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.credentials_role_request_token_type import CredentialsRoleRequestTokenType
        d = src_dict.copy()
        credentials_role_list = []
        _credentials_role_list = d.pop("credentialsRoleList")
        for credentials_role_list_item_data in (_credentials_role_list):
            credentials_role_list_item = CredentialsRoleRequestTokenType.from_dict(credentials_role_list_item_data)



            credentials_role_list.append(credentials_role_list_item)


        description = d.pop("description")

        generate_token_request_type = cls(
            credentials_role_list=credentials_role_list,
            description=description,
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
