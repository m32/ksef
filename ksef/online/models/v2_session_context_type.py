from typing import Any, Dict, Type, TypeVar, Tuple, Optional, BinaryIO, TextIO, TYPE_CHECKING

from typing import List


from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from typing import Dict
from ..types import UNSET, Unset
from typing import cast, List
from typing import Union
from typing import cast

if TYPE_CHECKING:
  from ..models.subject_identifier_by_type import SubjectIdentifierByType
  from ..models.subject_name_type import SubjectNameType
  from ..models.v2_credentials_role_response_base_type_object import V2CredentialsRoleResponseBaseTypeObject





T = TypeVar("T", bound="V2SessionContextType")


@_attrs_define
class V2SessionContextType:
    """ 
        Attributes:
            context_identifier (SubjectIdentifierByType):
            credentials_role_list (List['V2CredentialsRoleResponseBaseTypeObject']):
            context_name (Union[Unset, SubjectNameType]):
     """

    context_identifier: 'SubjectIdentifierByType'
    credentials_role_list: List['V2CredentialsRoleResponseBaseTypeObject']
    context_name: Union[Unset, 'SubjectNameType'] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)


    def to_dict(self) -> Dict[str, Any]:
        from ..models.subject_identifier_by_type import SubjectIdentifierByType
        from ..models.subject_name_type import SubjectNameType
        from ..models.v2_credentials_role_response_base_type_object import V2CredentialsRoleResponseBaseTypeObject
        context_identifier = self.context_identifier.to_dict()

        credentials_role_list = []
        for credentials_role_list_item_data in self.credentials_role_list:
            credentials_role_list_item = credentials_role_list_item_data.to_dict()

            credentials_role_list.append(credentials_role_list_item)




        context_name: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.context_name, Unset):
            context_name = self.context_name.to_dict()


        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "contextIdentifier": context_identifier,
            "credentialsRoleList": credentials_role_list,
        })
        if context_name is not UNSET:
            field_dict["contextName"] = context_name

        return field_dict



    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.subject_identifier_by_type import SubjectIdentifierByType
        from ..models.subject_name_type import SubjectNameType
        from ..models.v2_credentials_role_response_base_type_object import V2CredentialsRoleResponseBaseTypeObject
        d = src_dict.copy()
        context_identifier = SubjectIdentifierByType.from_dict(d.pop("contextIdentifier"))




        credentials_role_list = []
        _credentials_role_list = d.pop("credentialsRoleList")
        for credentials_role_list_item_data in (_credentials_role_list):
            credentials_role_list_item = V2CredentialsRoleResponseBaseTypeObject.from_dict(credentials_role_list_item_data)



            credentials_role_list.append(credentials_role_list_item)


        _context_name = d.pop("contextName", UNSET)
        context_name: Union[Unset, SubjectNameType]
        if isinstance(_context_name,  Unset):
            context_name = UNSET
        else:
            context_name = SubjectNameType.from_dict(_context_name)




        v2_session_context_type = cls(
            context_identifier=context_identifier,
            credentials_role_list=credentials_role_list,
            context_name=context_name,
        )

        v2_session_context_type.additional_properties = d
        return v2_session_context_type

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
