from typing import Any, Dict, Type, TypeVar, Tuple, Optional, BinaryIO, TextIO, TYPE_CHECKING

from typing import List


from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from typing import cast, List
from ..types import UNSET, Unset
from typing import Union
from typing import cast
from typing import Dict

if TYPE_CHECKING:
  from ..models.credentials_base_type_object_object_identifier import CredentialsBaseTypeObjectObjectIdentifier
  from ..models.credentials_base_type_object_object_credentials_role_list_item import CredentialsBaseTypeObjectObjectCredentialsRoleListItem





T = TypeVar("T", bound="CredentialsBaseTypeObjectObject")


@_attrs_define
class CredentialsBaseTypeObjectObject:
    """ 
        Attributes:
            type (str):
            credentials_role_list (Union[Unset, List['CredentialsBaseTypeObjectObjectCredentialsRoleListItem']]):
            identifier (Union[Unset, CredentialsBaseTypeObjectObjectIdentifier]):
     """

    type: str
    credentials_role_list: Union[Unset, List['CredentialsBaseTypeObjectObjectCredentialsRoleListItem']] = UNSET
    identifier: Union[Unset, 'CredentialsBaseTypeObjectObjectIdentifier'] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)


    def to_dict(self) -> Dict[str, Any]:
        from ..models.credentials_base_type_object_object_identifier import CredentialsBaseTypeObjectObjectIdentifier
        from ..models.credentials_base_type_object_object_credentials_role_list_item import CredentialsBaseTypeObjectObjectCredentialsRoleListItem
        type = self.type
        credentials_role_list: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.credentials_role_list, Unset):
            credentials_role_list = []
            for credentials_role_list_item_data in self.credentials_role_list:
                credentials_role_list_item = credentials_role_list_item_data.to_dict()

                credentials_role_list.append(credentials_role_list_item)




        identifier: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.identifier, Unset):
            identifier = self.identifier.to_dict()


        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "type": type,
        })
        if credentials_role_list is not UNSET:
            field_dict["credentialsRoleList"] = credentials_role_list
        if identifier is not UNSET:
            field_dict["identifier"] = identifier

        return field_dict



    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.credentials_base_type_object_object_identifier import CredentialsBaseTypeObjectObjectIdentifier
        from ..models.credentials_base_type_object_object_credentials_role_list_item import CredentialsBaseTypeObjectObjectCredentialsRoleListItem
        d = src_dict.copy()
        type = d.pop("type")

        credentials_role_list = []
        _credentials_role_list = d.pop("credentialsRoleList", UNSET)
        for credentials_role_list_item_data in (_credentials_role_list or []):
            credentials_role_list_item = CredentialsBaseTypeObjectObjectCredentialsRoleListItem.from_dict(credentials_role_list_item_data)



            credentials_role_list.append(credentials_role_list_item)


        _identifier = d.pop("identifier", UNSET)
        identifier: Union[Unset, CredentialsBaseTypeObjectObjectIdentifier]
        if isinstance(_identifier,  Unset):
            identifier = UNSET
        else:
            identifier = CredentialsBaseTypeObjectObjectIdentifier.from_dict(_identifier)




        credentials_base_type_object_object = cls(
            type=type,
            credentials_role_list=credentials_role_list,
            identifier=identifier,
        )

        credentials_base_type_object_object.additional_properties = d
        return credentials_base_type_object_object

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
